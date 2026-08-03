# no-ai-prose

A Claude Code plugin that makes Claude write prose without AI-telltale patterns:
no em-dashes for drama, no filler openers ("Certainly", "Absolutely"), no
transition-word inflation, no trailing offers to help. Full rules:
[`skills/no-ai-prose/SKILL.md`](skills/no-ai-prose/SKILL.md).

A `SessionStart` hook loads the rules every session, including after `/clear`
and compaction, so once installed it applies everywhere — not only when you ask.
Turn it off with `/plugin`.

## Install

```shell
/plugin marketplace add westonkd/agent-plugins
/plugin install no-ai-prose@agent-plugins
```

MIT — see [`LICENSE`](LICENSE).
