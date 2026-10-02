# Project Name

> Replace this file when creating a repository from the template.

Briefly describe what the project does and who it is for.

[日本語](README.ja.md)

## Requirements

Document the required runtime, toolchain, and external services.

## Getting started

```sh
# Add the canonical setup commands for this project.
```

## Development

Document the canonical development, test, lint, format, type-check, and build commands. Keep these commands consistent with `AGENTS.md`.

## Documentation

Long-form project documentation belongs under [`docs/`](docs/).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).


## Starting a new project

After creating a repository from this template:

1. Replace the placeholder project name and description in both README files.
2. Update `AGENTS.md` with the project's exact setup and validation commands.
3. Apply only the relevant language-specific additions from [`templates/`](templates/).
4. Extend `.gitignore` only for generated artifacts actually produced by the selected toolchain.
5. Keep project-specific CI/workflows local to the new repository.
6. Review `.github/release.yml` against the repository's actual labels before relying on generated release categories.

The shared Issue and Pull Request defaults are maintained separately in [`yuru-sha/.github`](https://github.com/yuru-sha/.github).


## One-command project creation

For a fully initialized repository, prefer the wrapper instead of creating the repository manually:

```sh
bash scripts/create-project.sh yuru-sha/my-project
```

Private repository:

```sh
bash scripts/create-project.sh yuru-sha/my-project --private
```

The wrapper:

1. creates the repository from `yuru-sha/project-template`;
2. preserves GitHub's default labels;
3. creates or updates the shared non-default labels;
4. creates the reserved `orca:*` lifecycle labels.

Requirements: authenticated GitHub CLI (`gh`) and Python 3.

The canonical label definitions live only in [`yuru-sha/project-template/.github/labels.json`](.github/labels.json). The synchronization script is idempotent, so it can also be used for an existing repository:

```sh
python3 scripts/sync-labels.py --repo yuru-sha/existing-project
```

The included GitHub Actions workflow fetches the canonical label definition from `yuru-sha/project-template` every day and can also be run manually. This keeps copied repositories aligned without editing their local label definition.
