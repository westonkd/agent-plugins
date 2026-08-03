# agent-plugins

[![Validate plugins](https://github.com/westonkd/agent-plugins/actions/workflows/validate-plugins.yml/badge.svg)](https://github.com/westonkd/agent-plugins/actions/workflows/validate-plugins.yml)

A catalog of plugins you can add to Claude Code and install individually.

## Plugins

| Plugin | Description |
| --- | --- |
| [`canvas-lms-api`](plugins/canvas-lms-api) | Subject-matter expert on the Canvas LMS REST API — all 142 resource groups (~1,078 endpoints), object models, and guides for auth, pagination, SIS imports, LTI, Live Events, and RBAC permissions. |
| [`no-ai-prose`](plugins/no-ai-prose) | Write prose without AI-telltale patterns: no em-dashes for drama, no filler openers, no transition-word inflation, no trailing offers to help. A `SessionStart` hook loads the rules automatically each session. |
| [`no-comment`](plugins/no-comment) | Write comment-free code — no line/block comments, docstrings, TODOs, or banners, with narrow exceptions for functional directives and pragmas. A `SessionStart` hook loads the rules automatically each session. |
| [`project-skill-init`](plugins/project-skill-init) | Scaffolds a new project-context skill — `SKILL.md`, a living PRD, a `DESIGN.md` stub, and an append-only ADR log with its own generator script — into any repository. |

## Install

Add the marketplace, then install a plugin from it:

```shell
/plugin marketplace add westonkd/agent-plugins
/plugin install canvas-lms-api@agent-plugins
```

To test locally from a clone:

```shell
/plugin marketplace add ./agent-plugins
/plugin install canvas-lms-api@agent-plugins
```

Refresh later with `/plugin marketplace update agent-plugins`.

## Repository layout

```
.claude-plugin/marketplace.json      Marketplace catalog (lists the plugins)
plugins/<plugin>/                     One directory per plugin
  .claude-plugin/plugin.json          Plugin manifest
  skills/, hooks/, scripts/, …        Plugin content
scripts/validate_plugins.py           Structure validator (used by CI)
.github/workflows/                    CI
```

Each plugin ships its own generated content committed to the repo, so installs
are self-contained. See a plugin's own README for build/regeneration details.

## Licensing

Each plugin carries its own `LICENSE` and, where it redistributes third-party
material, a `NOTICE` with attribution. The `canvas-lms-api` plugin is
**AGPL-3.0-only** because its reference content is derived from the open-source
Canvas LMS documentation ([instructure/canvas-lms](https://github.com/instructure/canvas-lms),
© Instructure, Inc.); see
[`plugins/canvas-lms-api/LICENSE`](plugins/canvas-lms-api/LICENSE) and
[`plugins/canvas-lms-api/NOTICE`](plugins/canvas-lms-api/NOTICE). The `no-comment`, `no-ai-prose`, and `project-skill-init` plugins are original content and are
**MIT** licensed; see [`plugins/no-comment/LICENSE`](plugins/no-comment/LICENSE),
[`plugins/no-ai-prose/LICENSE`](plugins/no-ai-prose/LICENSE),
and [`plugins/project-skill-init/LICENSE`](plugins/project-skill-init/LICENSE).

