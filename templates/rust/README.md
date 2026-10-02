# Rust / Cargo overlay

Use this overlay for Rust projects managed with Cargo.

## Typical project files

- `Cargo.toml`
- `Cargo.lock`
- optional `rust-toolchain.toml`

For applications and binaries, keep `Cargo.lock` committed. Libraries should follow the project's release/reproducibility policy explicitly.

## AGENTS.md command examples

Replace with the exact commands supported by the project.

```text
Setup: cargo fetch
Test: cargo test --all-targets
Format check: cargo fmt --all -- --check
Lint: cargo clippy --all-targets --all-features -- -D warnings
Build: cargo build
```

Adjust feature flags and workspace scope to the repository rather than copying these commands mechanically.

## .gitignore additions

```gitignore
# Cargo build output
/target/

# Coverage / profiling output when used
coverage/
profraw/
*.profraw
```

Keep Cargo manifests, toolchain files, benchmarks, and repository-managed hooks tracked.

## Validation

For behavior changes, tests plus `cargo fmt` and `cargo clippy` are the normal baseline when configured.
