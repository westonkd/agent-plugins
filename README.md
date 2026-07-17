# agent-plugins

A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces).
A catalog of plugins you can add to Claude Code and install individually.

## Plugins

| Plugin | Description |
| --- | --- |
| [`canvas-lms-api`](plugins/canvas-lms-api) | Subject-matter expert on the Canvas LMS REST API — all 142 resource groups (~1,078 endpoints), object models, and guides for auth, pagination, SIS imports, LTI, Live Events, and RBAC permissions. |

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
  skills/, scripts/, …                Plugin content
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
[`plugins/canvas-lms-api/NOTICE`](plugins/canvas-lms-api/NOTICE).

