#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORKFLOWS_DIR="$REPO_ROOT/.github/workflows"
ARCHIVE_DIR="$REPO_ROOT/.github/workflows.disabled"

if [ ! -d "$WORKFLOWS_DIR" ]; then
  echo "No workflows directory found at $WORKFLOWS_DIR"
  exit 0
fi

echo "Archiving workflows from $WORKFLOWS_DIR to $ARCHIVE_DIR"
mkdir -p "$ARCHIVE_DIR"
mv "$WORKFLOWS_DIR"/* "$ARCHIVE_DIR/"
rmdir "$WORKFLOWS_DIR" || true
echo "Workflows moved. Commit the change to make it permanent."
