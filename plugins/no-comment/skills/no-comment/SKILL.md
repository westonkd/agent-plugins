---
name: no-comment
description: Write code with no comments for the rest of the session. Use when the user asks for comment-free code, says to stop adding comments, or invokes /no-comment.
---

# no-comment

For the remainder of this session, write code that contains no comments.

## Rules

- Do not add any comments to code you write — no line comments (`//`, `#`, `--`), no
  block comments (`/* */`, `"""`), no JSDoc/docstrings, no TODO/FIXME notes, no section
  banners or divider comments.
- This applies to every language and file type, including config files, YAML, SQL,
  shell scripts, and Dockerfiles.
- When editing existing code, leave comments that are already there alone. Never delete
  or rewrite an existing comment unless the user asks, or unless the code it describes
  is being removed.
- Do not smuggle commentary in through other channels: no explanatory strings, no
  `console.log` narration, no naming things `stepOneParseTheInput`.
- Make the code self-explanatory instead: clear names, small functions, obvious control
  flow. If something is genuinely too subtle to read on its own, explain it in your
  reply to the user rather than in the file.

## Exceptions

Include a comment only when it is functionally required, not explanatory:

- Directives and pragmas the tooling reads — shebangs (`#!/usr/bin/env ...`),
  `# frozen_string_literal: true`, `// @ts-ignore`, `# noqa`, `eslint-disable`,
  `# type: ignore`, license headers required by the repo.
- Comment syntax used to disable or scope behavior that the language exposes no other
  way.

When the user explicitly asks for a comment on something, add it — their direct request
wins over this skill.
