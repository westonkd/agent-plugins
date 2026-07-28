# no-comment

A Claude Code plugin that makes the agent write **comment-free code**.

Once installed, it applies automatically: a `SessionStart` hook loads the rules
into context at the start of every session, so you never have to ask. You can
also invoke the skill explicitly with `/no-comment:no-comment`, or just say
something like "stop adding comments".

## What it does

Once loaded, the agent stops emitting comments in code it writes: no line
comments (`//`, `#`, `--`), block comments, JSDoc/docstrings, TODO/FIXME notes,
or section banners, in any language or file type. Existing comments in files it
edits are left alone. Instead of commentary, it leans on clear names, small
functions, and obvious control flow, and puts any genuinely subtle explanation
in its reply to you rather than in the file.

Comments that are *functionally* required still get written — shebangs,
`# frozen_string_literal: true`, `// @ts-ignore`, `# noqa`, `eslint-disable`,
required license headers, and comment syntax the language uses to scope
behavior. An explicit request for a comment on something also wins over the
skill.

## Always-on via SessionStart

`hooks/hooks.json` registers a `SessionStart` command hook that runs
`hooks/load-skill.sh`. The script strips the YAML frontmatter from `SKILL.md`
and prints the body to stdout; for `SessionStart`, stdout is injected into
Claude's context before the first prompt.

No matcher is set, so it fires for every session source — `startup`, `resume`,
`clear`, `compact`, and `fork` — which means the rules survive `/clear` and
context compaction. The script has no dependencies beyond `bash` and `awk`, and
exits 0 even if `SKILL.md` is missing so it can never block a session from
starting.

Because the hook is unconditional, installing this plugin makes comment-free
code the default everywhere, not just where you ask for it. To turn it off for a
session, disable the plugin with `/plugin`.

## Layout

```
.claude-plugin/plugin.json     Plugin manifest
skills/no-comment/SKILL.md     The rules (single file, no references)
hooks/hooks.json               SessionStart hook registration
hooks/load-skill.sh            Prints SKILL.md body as session context
```

## Install

```shell
/plugin marketplace add westonkd/agent-plugins
/plugin install no-comment@agent-plugins
```

## Licensing

MIT — see [`LICENSE`](LICENSE).
