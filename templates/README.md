# Language-specific overlays

The root of this repository is the shared baseline for every project.

This directory contains **small language-specific overlays**, not complete project templates. Copy only the parts that match the new project, then replace examples with the project's exact commands.

Supported initial overlays:

- [Python / uv](python/README.md)
- [Go](go/README.md)
- [Rust / Cargo](rust/README.md)
- [TypeScript / Node.js](typescript/README.md)

## Rules

- Do not duplicate common README, CONTRIBUTING, LICENSE, Issue, PR, or release conventions here.
- Keep the root `.gitignore` small; add ecosystem-specific generated paths from the selected overlay.
- Update root `AGENTS.md` with exact commands after initializing the project.
- Treat CI examples as project-specific. Add a workflow only when the project has a concrete validation command set.
- Prefer one clear toolchain per project instead of supporting several alternatives speculatively.
