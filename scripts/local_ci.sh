#!/usr/bin/env bash
set -euo pipefail
# Local CI runner (offline-first)
# This script runs the project's quality and test commands locally using the
# UV-managed environment if the virtual environment already exists.
# It will NOT perform network installs by default. To create the environment
# (network access) run `uv sync --dev` explicitly and intentionally.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

failures=()

function run_cmd() {
  echo "\n>>> $*"
  if ! uv run "$@"; then
    failures+=("$*")
  fi
}

if [ ! -d ".venv" ]; then
  echo "No .venv found in repository root. This runner will not auto-install dependencies."
  echo "If you intentionally want to create the environment (network access required), run:"
  echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
  echo "  uv sync --dev"
  echo "After that, re-run this script."
  exit 2
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "uv CLI not found in PATH. Install it first (one-time):"
  echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 3
fi

echo "Running local CI checks (offline-first) using existing .venv..."

# Lint & format
run_cmd ruff check --fix src/
run_cmd ruff format src/

# Type check
run_cmd mypy src/ || true

# Security scan (may require network to fetch bandit db, but usually local)
run_cmd bandit -r src/ || true

# Tests
run_cmd pytest tests/ || true

echo "\nLocal CI run complete."
if [ ${#failures[@]} -ne 0 ]; then
  echo "Some steps failed:" >&2
  for f in "${failures[@]}"; do
    echo " - $f" >&2
  done
  exit 4
fi

echo "All steps passed." 
