# Go overlay

Use this overlay for Go modules.

## Typical project files

- `go.mod`
- `go.sum`
- optional `.golangci.yml` or equivalent lint configuration

Commit `go.mod` and `go.sum`.

## AGENTS.md command examples

Replace with the exact commands supported by the project.

```text
Setup: go mod download
Test: go test ./...
Format: test -z "$(gofmt -l .)"
Vet: go vet ./...
Lint: golangci-lint run   # only when configured
Build: go build ./...
```

Use repository Makefile targets when they are the canonical interface instead of documenting parallel command sets.

## .gitignore additions

Go normally needs very little:

```gitignore
# Go test/build artifacts
*.test
*.out
coverage.out
coverage.html

# Local binaries
bin/
```

Do not ignore source-generated files when the repository intentionally commits them.

## Testing

Prefer table-driven tests when they make multiple cases clearer, but do not force them for trivial single-case behavior.
