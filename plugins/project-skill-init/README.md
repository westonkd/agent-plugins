# project-skill-init

A Claude Code plugin that adds a meta-skill for scaffolding new project-context skills.
Invoke it in any repository to generate `.claude/skills/<skill-name>/` pre-populated with a
thin `SKILL.md`, a living `references/PRD.md`, a `references/DESIGN.md` stub, and an
append-only `references/ADR/` decision log with its own `scripts/new_adr.sh` generator —
the pattern used by instructure-hosted-agents' `hosted-agents` skill for keeping a
project's problem statement, architecture, and decision history next to the code instead of
scattered across docs and chat history. Full details:
[`skills/project-skill-init/SKILL.md`](skills/project-skill-init/SKILL.md).

## Install

    /plugin marketplace add westonkd/agent-plugins
    /plugin install project-skill-init@agent-plugins

## Usage

Ask Claude to scaffold a project skill (e.g. "set up a project skill to track the billing
redesign"), or invoke the generator directly:

    skills/project-skill-init/scripts/init_skill.sh <skill-name> "<description>" [target-dir]

`[target-dir]` defaults to the current directory, so running it from inside the repository
you want to scaffold into is enough.

MIT — see [`LICENSE`](LICENSE).
