#!/usr/bin/env python3
"""Validate the marketplace catalog and plugin layout in this repo.

`claude plugin validate` checks the manifest *schemas*. This script checks the
repo-level invariants it can't see, because it only ever looks at one manifest
at a time:

    - every directory under plugins/ is registered in marketplace.json
    - name and version agree between marketplace.json and each plugin.json
    - components live at the plugin root, not inside .claude-plugin/
    - every skill has a SKILL.md with a description
    - hook command paths resolve, and hook scripts are executable

Deterministic and stdlib-only, so CI needs nothing but Python.

Usage (from the repo root):
    python3 scripts/validate_plugins.py
    python3 scripts/validate_plugins.py --strict   # warnings become errors

Exits 0 when clean, 1 when a check fails.
"""

from __future__ import annotations

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKETPLACE_PATH = os.path.join(REPO_ROOT, ".claude-plugin", "marketplace.json")
PLUGINS_DIR = os.path.join(REPO_ROOT, "plugins")

# Directories Claude Code reads from the plugin root. A component directory
# nested inside .claude-plugin/ is silently ignored at runtime, which is the
# single most common way a plugin ends up shipping nothing.
COMPONENT_DIRS = ("skills", "commands", "agents", "hooks", "monitors", "bin")

# Hook events accepted by the runtime. A typo here fails open: the hook simply
# never fires, with no error anywhere.
KNOWN_HOOK_EVENTS = frozenset(
    """
    SessionStart Setup InstructionsLoaded UserPromptSubmit UserPromptExpansion
    MessageDisplay PreToolUse PermissionRequest PermissionDenied PostToolUse
    PostToolUseFailure PostToolBatch Notification SubagentStart SubagentStop
    TaskCreated TaskCompleted Stop StopFailure TeammateIdle ConfigChange
    CwdChanged FileChanged WorktreeCreate WorktreeRemove PreCompact PostCompact
    Elicitation ElicitationResult SessionEnd
    """.split()
)

SCRIPT_SUFFIXES = (".sh", ".bash", ".py", ".js", ".mjs", ".rb", ".ps1")


class Report:
    """Collects findings so one run surfaces every problem, not just the first."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"{where}: {message}")


def rel(path: str) -> str:
    return os.path.relpath(path, REPO_ROOT)


def load_json(path: str, report: Report) -> dict | list | None:
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        report.error(rel(path), "missing")
    except json.JSONDecodeError as exc:
        report.error(rel(path), f"invalid JSON: {exc}")
    return None


def read_frontmatter(path: str) -> dict[str, str] | None:
    """Return top-level scalar keys from a YAML frontmatter block.

    Intentionally not a YAML parser: it reads the `key: value` pairs at column
    zero and ignores nested structures such as a skill's `hooks:` block. That
    is enough to check the fields a skill is required to declare.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError:
        return None

    if not lines or lines[0].strip() != "---":
        return None

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if sep and key.strip():
            fields[key.strip()] = value.strip().strip("\"'")
    return None


def is_executable(path: str) -> bool:
    return os.access(path, os.X_OK)


def check_skills(plugin_dir: str, report: Report) -> int:
    """Validate skills/<name>/SKILL.md plus the single-skill root layout."""
    found = 0

    root_skill = os.path.join(plugin_dir, "SKILL.md")
    if os.path.isfile(root_skill):
        found += 1
        if read_frontmatter(root_skill) is None:
            report.error(rel(root_skill), "missing or unterminated frontmatter")

    skills_dir = os.path.join(plugin_dir, "skills")
    if not os.path.isdir(skills_dir):
        return found

    for name in sorted(os.listdir(skills_dir)):
        entry = os.path.join(skills_dir, name)
        if not os.path.isdir(entry):
            report.warn(rel(entry), "not a directory; skills must be <name>/SKILL.md")
            continue

        skill_md = os.path.join(entry, "SKILL.md")
        if not os.path.isfile(skill_md):
            report.error(rel(entry), "skill directory has no SKILL.md")
            continue

        found += 1
        fields = read_frontmatter(skill_md)
        if fields is None:
            report.error(rel(skill_md), "missing or unterminated frontmatter")
            continue
        if not fields.get("description"):
            report.error(rel(skill_md), "frontmatter has no description")
        declared = fields.get("name")
        if declared and declared != name:
            report.error(
                rel(skill_md),
                f"frontmatter name {declared!r} does not match directory {name!r}",
            )

    return found


def resolve_plugin_root_refs(value: str) -> list[str]:
    """Extract the paths a hook command references via ${CLAUDE_PLUGIN_ROOT}."""
    refs = []
    marker = "${CLAUDE_PLUGIN_ROOT}"
    start = value.find(marker)
    while start != -1:
        tail = value[start + len(marker) :]
        path = ""
        for char in tail:
            if char.isspace() or char in "\"'":
                break
            path += char
        if path:
            refs.append(path.lstrip("/"))
        start = value.find(marker, start + len(marker))
    return refs


def check_hook_handler(plugin_dir: str, handler: object, where: str, report: Report) -> None:
    if not isinstance(handler, dict):
        report.error(where, "hook handler must be an object")
        return

    hook_type = handler.get("type")
    if not hook_type:
        report.error(where, "hook handler has no type")
        return
    if hook_type not in ("command", "http", "mcp_tool", "prompt", "agent"):
        report.error(where, f"unknown hook type {hook_type!r}")
        return
    if hook_type != "command":
        return

    command = handler.get("command")
    if not isinstance(command, str) or not command:
        report.error(where, "command hook has no command")
        return

    refs = resolve_plugin_root_refs(command)
    for arg in handler.get("args") or []:
        if isinstance(arg, str):
            refs.extend(resolve_plugin_root_refs(arg))

    if "${CLAUDE_PLUGIN_ROOT}" in command and handler.get("args") is None:
        report.warn(
            where,
            "shell-form command uses ${CLAUDE_PLUGIN_ROOT}; add \"args\": [] to use "
            "exec form so paths with spaces need no quoting",
        )

    for ref in refs:
        target = os.path.join(plugin_dir, ref)
        if not os.path.exists(target):
            report.error(where, f"references ${{CLAUDE_PLUGIN_ROOT}}/{ref}, which does not exist")
            continue
        if ref.endswith(SCRIPT_SUFFIXES) and not is_executable(target):
            report.error(
                rel(target),
                "referenced by a hook but not executable; run: git update-index "
                f"--chmod=+x {rel(target)}",
            )


def check_hooks(plugin_dir: str, report: Report) -> int:
    hooks_json = os.path.join(plugin_dir, "hooks", "hooks.json")
    if not os.path.isfile(hooks_json):
        hooks_dir = os.path.join(plugin_dir, "hooks")
        if os.path.isdir(hooks_dir):
            report.error(rel(hooks_dir), "hooks directory has no hooks.json")
        return 0

    data = load_json(hooks_json, report)
    if data is None:
        return 0
    if not isinstance(data, dict):
        report.error(rel(hooks_json), "top level must be an object")
        return 0

    events = data.get("hooks")
    if not isinstance(events, dict) or not events:
        report.error(rel(hooks_json), 'missing a non-empty "hooks" object')
        return 0

    count = 0
    for event, groups in events.items():
        if event not in KNOWN_HOOK_EVENTS:
            report.error(rel(hooks_json), f"unknown hook event {event!r}")
        if not isinstance(groups, list):
            report.error(rel(hooks_json), f"{event}: matcher groups must be a list")
            continue
        for index, group in enumerate(groups):
            where = f"{rel(hooks_json)} [{event}][{index}]"
            if not isinstance(group, dict):
                report.error(where, "matcher group must be an object")
                continue
            handlers = group.get("hooks")
            if not isinstance(handlers, list) or not handlers:
                report.error(where, 'missing a non-empty "hooks" array')
                continue
            for handler in handlers:
                count += 1
                check_hook_handler(plugin_dir, handler, where, report)

    return count


def check_plugin(name: str, entry: dict, report: Report) -> None:
    """Validate one plugin directory against its marketplace entry."""
    plugin_dir = os.path.join(PLUGINS_DIR, name)
    manifest_dir = os.path.join(plugin_dir, ".claude-plugin")
    manifest_path = os.path.join(manifest_dir, "plugin.json")

    manifest = load_json(manifest_path, report)
    if manifest is None:
        return
    if not isinstance(manifest, dict):
        report.error(rel(manifest_path), "top level must be an object")
        return

    where = rel(manifest_path)
    declared = manifest.get("name")
    if declared != name:
        report.error(where, f"name {declared!r} does not match directory {name!r}")
    if not manifest.get("description"):
        report.error(where, "missing description")

    # Version drift is the failure mode this catches in practice: bumping one
    # manifest and forgetting the other means installs never see the update.
    version = manifest.get("version")
    if not version:
        report.warn(where, "no version; installs will key off the commit SHA")
    elif entry.get("version") and entry["version"] != version:
        report.error(
            where,
            f"version {version!r} does not match marketplace.json {entry['version']!r}",
        )

    for field in ("license", "author"):
        if entry.get(field) and manifest.get(field) != entry.get(field):
            report.warn(where, f"{field} differs from the marketplace.json entry")

    for component in COMPONENT_DIRS:
        misplaced = os.path.join(manifest_dir, component)
        if os.path.exists(misplaced):
            report.error(
                rel(misplaced),
                f"{component}/ must live at the plugin root, not inside .claude-plugin/",
            )

    if manifest.get("license") and not os.path.isfile(os.path.join(plugin_dir, "LICENSE")):
        report.error(rel(plugin_dir), f"declares license {manifest['license']!r} but ships no LICENSE")

    if not os.path.isfile(os.path.join(plugin_dir, "README.md")):
        report.warn(rel(plugin_dir), "no README.md")

    skills = check_skills(plugin_dir, report)
    hooks = check_hooks(plugin_dir, report)
    has_other = any(
        os.path.exists(os.path.join(plugin_dir, extra))
        for extra in ("commands", "agents", "monitors", "bin", ".mcp.json", ".lsp.json")
    )
    if not skills and not hooks and not has_other:
        report.error(rel(plugin_dir), "ships no skills, hooks, or other components")

    print(f"  {name}: {skills} skill(s), {hooks} hook handler(s)")


def main(argv: list[str]) -> int:
    strict = "--strict" in argv[1:]
    report = Report()

    print(f"Validating {rel(MARKETPLACE_PATH)}")
    marketplace = load_json(MARKETPLACE_PATH, report)
    if not isinstance(marketplace, dict):
        if marketplace is not None:
            report.error(rel(MARKETPLACE_PATH), "top level must be an object")
        return finish(report, strict)

    for field in ("name", "owner", "plugins"):
        if not marketplace.get(field):
            report.error(rel(MARKETPLACE_PATH), f"missing {field}")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        report.error(rel(MARKETPLACE_PATH), '"plugins" must be a list')
        return finish(report, strict)

    registered: dict[str, dict] = {}
    for index, entry in enumerate(entries):
        where = f"{rel(MARKETPLACE_PATH)} [plugins][{index}]"
        if not isinstance(entry, dict):
            report.error(where, "entry must be an object")
            continue
        name = entry.get("name")
        if not name:
            report.error(where, "entry has no name")
            continue
        if name in registered:
            report.error(where, f"duplicate entry for {name!r}")
            continue
        registered[name] = entry

        source = entry.get("source")
        expected = f"./plugins/{name}"
        if source != expected:
            report.error(where, f"source {source!r} should be {expected!r}")
        if not os.path.isdir(os.path.join(PLUGINS_DIR, name)):
            report.error(where, f"source directory plugins/{name}/ does not exist")

    on_disk = {
        name
        for name in os.listdir(PLUGINS_DIR)
        if os.path.isdir(os.path.join(PLUGINS_DIR, name)) and not name.startswith(".")
    } if os.path.isdir(PLUGINS_DIR) else set()

    for name in sorted(on_disk - set(registered)):
        report.error(
            f"plugins/{name}",
            "not listed in marketplace.json, so nobody can install it",
        )

    # Unregistered directories are still checked, so one run reports everything
    # wrong with a new plugin rather than only that it needs registering.
    for name in sorted(on_disk):
        check_plugin(name, registered.get(name, {}), report)

    return finish(report, strict)


def finish(report: Report, strict: bool) -> int:
    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}")

    failed = bool(report.errors) or (strict and bool(report.warnings))
    if failed:
        print(
            f"\nFAIL: {len(report.errors)} error(s), {len(report.warnings)} warning(s)"
        )
        return 1

    print(f"\nOK: structure valid ({len(report.warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
