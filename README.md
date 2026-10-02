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
