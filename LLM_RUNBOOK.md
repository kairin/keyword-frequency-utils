LLM Runbook — Safe commit & push (automation-friendly)

Purpose

This runbook documents an explicit, audit-friendly sequence of git commands an automated agent (including LLM-driven tools) can follow to safely commit and push repository changes while avoiding accidental inclusion of personal data (images, .txt data, generated outputs).

Automation contract (inputs/outputs)

- Inputs: modified repository working tree with changes limited to code, docs, scripts, tests.
- Outputs: a git commit on the current branch and a pushed branch on `origin`.
- Error modes: detected tracked data files, missing remote, or no changes to commit.
- Success criteria: commit created and pushed, and no image/text files were added to the repo.

Assumptions

- The repository has a correct `.gitignore` that excludes `*.png`, `*.jpg`, `*.txt`, `*.csv`, `.venv/` and data folders.
- The agent has `git` configured and network access to `origin`.
- The agent will only add explicitly whitelisted paths (no `git add .` nor `git add -A`).

Checklist (automation steps)

1. Verify `.gitignore` exists and includes data/output patterns.
2. Ensure there are no currently tracked data files (images/.txt/outputs).
3. Stage only explicit, known-safe files.
4. Commit with a clear message.
5. Push the branch to `origin`.
6. Optionally create a PR using `gh` (requires appropriate permissions).

Commands (copyable)

# 1) Quick audit: ensure no tracked data files
```bash
# show any tracked image/text files (should output nothing)
git ls-files -- "*.txt" "*.jpg" "*.jpeg" "*.png" || true

# quick concise status
git status --porcelain=v1
```

# 2) Stage only explicit safe paths (do NOT use `git add .`)
```bash
git add AGENTS.md CLAUDE.md GEMINI.md README.md POLICY.md LLM_RUNBOOK.md tests scripts
```

# 3) Commit
```bash
git commit -m "chore: add LLM_RUNBOOK; commit safe docs/tests/scripts" || true
```

# 4) Push current branch to origin
```bash
git rev-parse --abbrev-ref HEAD  # helpful to confirm branch name
git push origin $(git rev-parse --abbrev-ref HEAD)
```

# 5) (Optional) Create a PR
```bash
gh pr create --title "Docs: runbook and local-only CI" --body "Add LLM runbook and local-only CI policy." --base main
```

Automation rules for LLMs

- Always run the audit commands (step 1) and abort if they return results.
- Never run `git add` with broad globs or `.`; always use an explicit whitelist of filenames or directories.
- If the working tree is large, prefer `git ls-files -- "*.txt" ...` to check for tracked data first.
- If `git commit` returns "nothing to commit", that's OK — do not push empty commits.
- If the default branch differs (e.g., `main`) and you intend to create a PR, set the `--base` appropriately.

Notes

- Keep this runbook in the repo root so future automated tools can find and follow it exactly.
- Update the allowed file list above if you add new directories that should be committed by automation.

End of runbook.
