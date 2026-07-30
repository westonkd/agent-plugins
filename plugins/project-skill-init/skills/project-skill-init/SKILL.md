---
name: project-skill-init
description: Scaffold a new project-context skill — SKILL.md plus references/PRD.md, references/DESIGN.md, references/ADR/, and scripts/new_adr.sh — into any repository, following the PRD/DESIGN/ADR pattern used by instructure-hosted-agents' hosted-agents skill. Use when starting work on a new project, feature area, or subsystem that needs a durable place to record its problem statement, architecture, and decision history, or when asked to set up a "project skill", "living spec", or "ADR log" for a repo.
---

# project-skill-init

Scaffolds a new `.claude/skills/<skill-name>/` in any repository, pre-populated with a thin
`SKILL.md`, a living PRD, a `DESIGN.md` stub, and an append-only `references/ADR/` decision
log with its own `new_adr.sh` generator — so a project's problem statement, architecture,
and decision history live next to the code instead of scattered across docs and chat
history.

## How to use this

1. Read [references/pattern.md](references/pattern.md) first. It explains *why* the
   pattern is shaped this way (thin `SKILL.md`, a status blockquote in the PRD, append-only
   ADRs, timestamp-prefixed filenames) — you need this to apply the pattern well and to
   explain it to the user, not just to mechanically copy files.
2. Pick a kebab-case `<skill-name>` for the new skill, and write a `<description>` ending
   in a "Use when..." clause, the same way this skill's own frontmatter does.
3. Run the scaffold script from the repository you want to scaffold into:

   ```
   ${CLAUDE_PLUGIN_ROOT}/skills/project-skill-init/scripts/init_skill.sh <skill-name> "<description>" [target-dir]
   ```

   - `<skill-name>` — kebab-case identifier (lowercase letters, digits, hyphens). Becomes
     the directory name and the generated `SKILL.md`'s frontmatter `name`.
   - `<description>` — a quoted, single-line description used verbatim as the generated
     `SKILL.md`'s frontmatter `description` and restated as its mission statement. Avoid
     embedded `"` characters and `": "` sequences — both can corrupt YAML frontmatter.
   - `[target-dir]` — the repository root to scaffold into. Defaults to the current
     directory, so when you're already working inside the target repo you can omit it.

   The script refuses to run if `.claude/skills/<skill-name>/` already exists, so it never
   overwrites existing work. It prints the created skill directory's path on success.
4. Open the generated `references/PRD.md` and fill in Summary through Phasing for the real
   project. Leave `references/DESIGN.md` as a stub until there's real architecture to
   record — that's expected, not a gap.
5. From then on, record decisions with the generated skill's own generator rather than
   hand-editing `PRD.md`/`DESIGN.md`:

   ```
   .claude/skills/<skill-name>/scripts/new_adr.sh "Title of the decision"
   ```

## References

- [references/pattern.md](references/pattern.md) — the rationale behind the PRD/DESIGN/ADR
  pattern: why `SKILL.md` stays thin, why `PRD.md` carries a status blockquote, why ADRs
  are append-only, why filenames are timestamp-prefixed slugs.

## Scripts

- `scripts/init_skill.sh <skill-name> "<description>" [target-dir]` — creates the scaffold
  described above. Safe to re-run with a different `skill-name`; exits with an error rather
  than touching anything if the target skill directory already exists.
