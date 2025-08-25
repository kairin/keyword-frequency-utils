Local-Only CI Policy

This repository enforces a local-only CI policy to avoid running workflows on remote
GitHub-hosted runners or other cloud providers.

Requirements for contributors

- Use the UV package manager to create the development environment:

  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv sync --dev

- Run local checks before pushing. Install the provided git hook template:

  ./scripts/install-hooks.sh

  This will copy `scripts/git-hooks/pre-push` into `.git/hooks/pre-push` and make
  the hook executable. The hook runs `./scripts/local_ci.sh` which performs local
  linting, type-checking, security checks, and tests.

- Do not re-enable GitHub Actions or other remote CI in this repository. Repository
  owners have disabled Actions at the repo level; if you need to re-enable for a
  specific reason, follow the documented governance process (contact the repo
  owners and get explicit approval).

Archiving or disabling existing workflows

- If you find `.github/workflows` files, archive them locally to prevent remote
  runs:

  ./scripts/archive-workflows.sh

- The helper moves workflows to `.github/workflows.disabled` so they remain in the
  repo history but won't execute on GitHub.

Notes

- The policy is intentionally strict to avoid accidental cloud execution and
  potential costs. This is a local-first project: CI should run on developer
  machines or approved self-hosted runners that the project owners manage.

- If you need to add new checks to the local CI, modify `scripts/local_ci.sh` and
  update this policy if the change affects developer setup.
