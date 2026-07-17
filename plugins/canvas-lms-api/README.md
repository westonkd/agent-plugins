# canvas-lms-api

A Claude Code plugin that makes an agent a subject-matter expert on the
**Canvas LMS REST API**.

> **Provenance:** this skill is built entirely from the official API
> documentation that ships in the open-source **Canvas LMS** codebase on GitHub:
> [instructure/canvas-lms](https://github.com/instructure/canvas-lms). Canvas
> generates its REST API docs (the Swagger definitions and prose guides) directly
> from that source, and this plugin extracts and reorganizes that documentation
> into the reference files below. Canvas LMS is published by Instructure under
> the AGPL-3.0 license.

The Canvas API is huge — 142 resource groups, ~1,078 endpoints, 274 object
models, plus dozens of conceptual guides and a large RBAC permission catalog.
Loading all of that into context is not great, so the plugin's skill is built
around **progressive disclosure**: a small always-loaded entrypoint
(`skills/canvas-lms-api/SKILL.md`) that routes to narrow, on-demand reference
files.

## Layout

```
.claude-plugin/plugin.json           Plugin manifest
scripts/build_reference.py           Deterministic extractor (Python stdlib only)
doc/                                 Raw Canvas Swagger dump — SOURCE ONLY, gitignored
skills/canvas-lms-api/
  SKILL.md                           Entrypoint: API essentials, routing, resource map
  reference/                         Generated, committed — what the skill actually uses
    catalog.md                       All 142 resources: description, #endpoints, #models
    endpoints-index.md               One grep-able line per endpoint (~1,078)
    resources/<slug>.md              Per-resource: every endpoint (params/returns) + models
    guides/README.md                 Index of the concept guides
    guides/<topic>.md                Extracted narrative guides (auth, SIS, LTI, …)
    permissions.md                   Consolidated account/course role permissions (RBAC)
```

## How the skill is used

1. `grep -i <keyword> reference/endpoints-index.md` to locate an endpoint.
2. Open the matching `reference/resources/<slug>.md` for full parameters + models.
3. Open a `reference/guides/<topic>.md` for concepts (auth, pagination, uploads,
   SIS CSV, LTI, Live Events).
4. `grep -i <permission> reference/permissions.md` for RBAC lookups.

See `skills/canvas-lms-api/SKILL.md` for the full routing rules and the
resource-map-by-domain.

## Source & regeneration

`reference/` is generated from `doc/api/` — a snapshot of Canvas's official
Swagger 1.2 documentation (per-resource `*.json` files plus `file.*.html` prose
guides), as produced by the open-source Canvas LMS codebase
([instructure/canvas-lms](https://github.com/instructure/canvas-lms)). That raw
dump is **gitignored**; the generated `reference/` is committed so the plugin is
self-contained for users who install it.

To regenerate after refreshing the `doc/api/` snapshot from a newer Canvas
version, run from this plugin's root:

```bash
python3 scripts/build_reference.py                 # defaults shown below
python3 scripts/build_reference.py <DOC_DIR> <OUT_DIR>
```

Defaults: `DOC_DIR=doc/api`, `OUT_DIR=skills/canvas-lms-api/reference`. The build
is deterministic and idempotent (no third-party dependencies) and prints a
summary of what it extracted (resources, endpoints, models, guides, permissions).

## License & attribution

The reference content is derived from the Canvas LMS documentation
([instructure/canvas-lms](https://github.com/instructure/canvas-lms)), which is
licensed under the **GNU Affero General Public License, version 3
(AGPL-3.0-only)** and copyright Instructure, Inc. Because this plugin
incorporates and redistributes that material, the plugin as a whole — including
the build tooling and skill authored for this project — is distributed under
AGPL-3.0-only.

- Full license text: [`LICENSE`](LICENSE)
- Attribution and what is derived from Canvas LMS: [`NOTICE`](NOTICE)

This plugin is an independent project, not affiliated with or endorsed by
Instructure, Inc. "Canvas" and "Canvas LMS" are trademarks of Instructure, Inc.,
used here only to identify the software this documentation describes.
