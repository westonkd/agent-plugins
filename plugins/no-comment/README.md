# no-comment

A Claude Code plugin that makes Claude write comment-free code — no line or
block comments, docstrings, TODOs, or banners, except where they are
functionally required (shebangs, pragmas, license headers). Full rules:
[`skills/no-comment/SKILL.md`](skills/no-comment/SKILL.md).

A `SessionStart` hook loads the rules every session, including after `/clear`
and compaction, so once installed it applies everywhere — not only when you ask.
Turn it off with `/plugin`.

## Install

```shell
/plugin marketplace add westonkd/agent-plugins
/plugin install no-comment@agent-plugins
```

MIT — see [`LICENSE`](LICENSE).
