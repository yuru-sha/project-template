# Python / uv overlay

Use this overlay for Python projects managed with `uv`.

## Typical project files

Common repository files may include:

- `pyproject.toml`
- `uv.lock`
- `.python-version`

Commit lockfiles when the project uses them for reproducible environments.

## AGENTS.md command examples

Replace with the exact commands supported by the project.

```text
Setup: uv sync
Test: uv run pytest
Lint: uv run ruff check .
Format check: uv run ruff format --check .
Typecheck: uv run mypy .   # only when configured
Build: uv build            # only for distributable packages
```

Do not document tools that are not configured in `pyproject.toml`.

## .gitignore additions

Add only the entries relevant to the project:

```gitignore
# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/

# Virtual environments
.venv/
venv/

# Build/package output
build/
dist/
*.egg-info/
```

Keep `uv.lock` tracked when reproducibility is desired.

## Validation

A normal change should run the smallest applicable set of configured checks, typically tests plus lint/format and type checking when present.
