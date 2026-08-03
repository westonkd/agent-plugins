#!/usr/bin/env bash
set -euo pipefail

root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
skill="$root/skills/no-ai-prose/SKILL.md"

if [ ! -f "$skill" ]; then
  echo "no-ai-prose: SKILL.md not found at $skill" >&2
  exit 0
fi

echo "The no-ai-prose plugin is enabled for this session. Its rules follow."
echo

awk '
  NR == 1 && /^---[[:space:]]*$/ { fm = 1; next }
  fm && /^---[[:space:]]*$/ { fm = 0; next }
  !fm { print }
' "$skill"
