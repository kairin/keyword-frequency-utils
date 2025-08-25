# Keyword Frequency Utilities

Purpose
-------

This repository contains a small, local-first utility to extract and aggregate
comma-separated keywords from text files and produce a keyword frequency report.

Key features
------------
- Scans the repository directory for `*.txt` files containing comma-separated
	keywords, normalizes tokens (strip + lower), and counts frequencies across all
	files.
- Writes `keyword_frequency.csv` and saves a bar chart `top_keywords_bar_chart.png`.
- Uses a headless matplotlib backend so it can run on machines without a display.
- Project enforces a local-only CI policy (see `POLICY.md`) and provides a
	local CI runner and pre-push hook template under `scripts/` so checks run on
	developer machines only.
# Keyword Frequency Utilities

Purpose
-------

This repository provides a small, local-first utility for extracting and
aggregating comma-separated keywords from text files and producing a simple
keyword frequency report.

What's included
---------------
- `run.py` — the main script: scans `*.txt` files, normalizes tokens,
	aggregates frequencies, writes `keyword_frequency.csv`, and saves a
	`top_keywords_bar_chart.png` visualization.
- `scripts/` — local CI runner, hook installer, and helpers for offline-first
	workflows.
- `tests/` — minimal pytest coverage for the keyword utility.
- `POLICY.md` and `LLM_RUNBOOK.md` — guidance for contributors and
	automation-friendly safe commit/push steps.

Quick start
-----------

1. Install UV (recommended) and sync dev dependencies:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --dev
```

2. Run the keyword utility from the repository root:

```bash
uv run python run.py
```

3. Run tests:

```bash
uv run pytest -q
```

Local CI policy
---------------

This project enforces a local-only CI policy to avoid accidental remote runs
and cloud costs. See `POLICY.md` for required developer setup and the
pre-push hook installer under `scripts/`.

Contributing
------------

Please follow `POLICY.md` and install the provided git hooks with:

```bash
./scripts/install-hooks.sh
```

If you need to rename the repo, change branch protections, or modify the CI
strategy, contact the repository owners for approval.

License
-------

This project intentionally contains no dataset or personal data; the
repository holds only code, tests, and documentation. Add a license file as
needed.
