#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"
TEMPLATE_DIR="$REPO_ROOT/scripts/git-hooks"

if [ ! -d "$HOOKS_DIR" ]; then
  echo ".git/hooks not found - are you in a git repository?" >&2
  exit 1
fi

echo "Installing git hooks from $TEMPLATE_DIR to $HOOKS_DIR"
for f in "$TEMPLATE_DIR"/*; do
  base=$(basename "$f")
  cp "$f" "$HOOKS_DIR/$base"
  chmod +x "$HOOKS_DIR/$base"
  echo "Installed $base"
done

echo "All hooks installed."
