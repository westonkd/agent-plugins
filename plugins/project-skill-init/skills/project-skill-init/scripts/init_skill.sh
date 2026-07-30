#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: init_skill.sh <skill-name> "<description>" [target-dir]

  <skill-name>   kebab-case identifier, e.g. "billing-redesign".
                 Becomes .claude/skills/<skill-name>/ and the generated
                 SKILL.md's frontmatter `name`.
  <description>  Quoted, single-line description, ideally ending in a
                 "Use when ..." clause. Used verbatim as the generated
                 SKILL.md's frontmatter `description` and mission statement.
                 Must not contain a double-quote character or a ": "
                 sequence (both can corrupt YAML frontmatter).
  [target-dir]   Repository root to scaffold into. Defaults to the current
                 directory.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage
  exit 1
fi

skill_name="$1"
description="$2"
target_dir="${3:-$(pwd)}"

if [[ -z "$description" ]]; then
  echo "error: <description> must not be empty" >&2
  usage
  exit 1
fi

if [[ "$description" == *'"'* ]]; then
  echo "error: <description> must not contain a double-quote character (breaks YAML frontmatter)" >&2
  exit 1
fi

if [[ "$description" =~ :[[:space:]] ]]; then
  echo "error: <description> must not contain ': ' — YAML frontmatter treats colon-space as a mapping separator; rephrase without it" >&2
  exit 1
fi

if [[ ${#description} -gt 1024 ]]; then
  echo "error: <description> is ${#description} characters; the Agent Skills spec caps it at 1024" >&2
  exit 1
fi

if [[ ! "$skill_name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: '$skill_name' is not a valid skill name; use lowercase letters, digits, and hyphens only (e.g. 'billing-redesign')" >&2
  exit 1
fi

if [[ ${#skill_name} -gt 64 ]]; then
  echo "error: '$skill_name' is ${#skill_name} characters; the Agent Skills spec caps skill names at 64" >&2
  exit 1
fi

if [[ ! -d "$target_dir" ]]; then
  echo "error: target directory '$target_dir' does not exist" >&2
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
assets_dir="$script_dir/../assets"
target_dir="$(cd "$target_dir" && pwd)"
skill_root="$target_dir/.claude/skills/$skill_name"

if [[ -e "$skill_root" ]]; then
  echo "error: $skill_root already exists; remove it or choose a different skill name" >&2
  exit 1
fi

escape_for_sed() {
  printf '%s' "$1" | sed -e 's/[\/&]/\\&/g'
}

render() {
  local template="$1" dest="$2"
  sed \
    -e "s/{{SKILL_NAME}}/$(escape_for_sed "$skill_name")/g" \
    -e "s/{{DESCRIPTION}}/$(escape_for_sed "$description")/g" \
    -e "s/{{DATE}}/$(date +%Y-%m-%d)/g" \
    "$template" > "$dest"
}

mkdir -p "$skill_root/references/ADR" "$skill_root/scripts"

render "$assets_dir/SKILL.md.tmpl" "$skill_root/SKILL.md"
render "$assets_dir/PRD.md.tmpl" "$skill_root/references/PRD.md"
render "$assets_dir/DESIGN.md.tmpl" "$skill_root/references/DESIGN.md"

cp "$assets_dir/new_adr.sh" "$skill_root/scripts/new_adr.sh"
chmod +x "$skill_root/scripts/new_adr.sh"

echo "$skill_root"
