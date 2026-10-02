# TypeScript / Node.js overlay

Use this overlay for TypeScript or Node.js projects.

## Package manager

Choose and document the package manager actually used by the repository. Do not include npm, pnpm, and yarn command variants simultaneously in `AGENTS.md`.

Commit the corresponding lockfile.

## AGENTS.md command examples

For an npm project, adapt the scripts that actually exist in `package.json`:

```text
Setup: npm ci
Test: npm test
Lint: npm run lint
Format check: npm run format:check   # only when configured
Typecheck: npm run typecheck
Build: npm run build
```

If the repository is a monorepo, document workspace boundaries and targeted commands.

## .gitignore additions

Add only paths produced by the selected framework/tooling:

```gitignore
# Dependencies
node_modules/

# Build output
dist/
build/

# Tests / tooling
coverage/
*.tsbuildinfo
.eslintcache

# Package-manager/debug logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
```

Framework-specific directories such as `.next/`, `.nuxt/`, or Playwright reports belong in the project only when those tools are actually used.

## Validation

Treat `package.json` scripts as the source of truth. Do not invent wrapper scripts merely to match the template.
