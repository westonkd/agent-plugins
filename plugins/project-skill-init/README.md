# project-skill-init

A Claude Code plugin that adds a meta-skill for scaffolding new project-context skills.
Invoke it in any repository to generate `.claude/skills/<skill-name>/` pre-populated with a
thin `SKILL.md`, a living `references/PRD.md`, a `references/DESIGN.md` stub, and an
append-only `references/ADR/` decision log with its own `scripts/new_adr.sh` generator —
the pattern used by instructure-hosted-agents' `hosted-agents` skill for keeping a
project's problem statement, architecture, and decision history next to the code instead of
scattered across docs and chat history. Full details:
[`skills/project-skill-init/SKILL.md`](skills/project-skill-init/SKILL.md).

## Example Result
This is an example of what this skill produces in a project called `sprint`
```
sprint
├── references
│   ├── ADR
│   │   ├── 20260822183250_target_the_chrome_webmcp_standard_not_the_webmcp_dev_library.md
│   │   ├── 20260822192124_agent_view_is_a_dom_projection_not_a_second_render_path.md
│   │   ├── 20260822192124_css_token_layer_cascade_layers_and_semantic_roles_as_public_contract.md
│   │   ├── 20260822192124_packaging_side_effects_and_registration_as_a_data_dependency.md
│   │   ├── 20260822192124_tool_names_derive_from_the_accessible_label_and_compose_by_scope.md
│   ├── DESIGN.md
│   └── PRD.md
├── scripts
│   └── new_adr.sh
└── SKILL.md
```

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
