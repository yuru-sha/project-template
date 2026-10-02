#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/create-project.sh OWNER/REPO [--private|--public] [--description TEXT]

Creates a repository from yuru-sha/project-template and immediately applies
the shared non-default labels, including ORCA lifecycle labels.

Examples:
  scripts/create-project.sh yuru-sha/example
  scripts/create-project.sh yuru-sha/example --private
  scripts/create-project.sh yuru-sha/example --description "Example service"
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 2
fi

repo="$1"
shift

visibility="--public"
description=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --public|--private)
      visibility="$1"
      shift
      ;;
    --description)
      description="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

command -v gh >/dev/null 2>&1 || {
  echo "gh CLI is required." >&2
  exit 1
}

command -v python3 >/dev/null 2>&1 || {
  echo "python3 is required." >&2
  exit 1
}

args=(
  repo create "$repo"
  --template yuru-sha/project-template
  "$visibility"
)

if [[ -n "$description" ]]; then
  args+=(--description "$description")
fi

echo "Creating $repo from yuru-sha/project-template..."
gh "${args[@]}"

echo "Applying shared labels..."
python3 scripts/sync-labels.py --repo "$repo"

cat <<EOF

Created: https://github.com/$repo

Next:
  1. Replace README placeholders.
  2. Update AGENTS.md with exact project commands.
  3. Apply the relevant language overlay from templates/.
EOF
