# Contributing

OpenSIN-documentation is a docs-only repo. Keep changes evidence-based, source-backed, and scoped to documentation canon.

## Boundary rules

Before adding a page or top-level claim, answer:

1. Is this official documentation content, or implementation truth that should live in another repo?
2. Does another OpenSIN repo already own the canonical source of truth?
3. If a surface changed, is the domain registry updated first?

### Put it in this repo if

- it is official docs content
- it explains, teaches, or documents owning repos clearly
- it improves discoverability, navigation, or registry accuracy

### Do not put it in this repo if

- it becomes the implementation repo for runtime, product, or ops
- it becomes a hidden registry that is not documented in public-facing pages

## Local workflow

```bash
bun install
bun ./scripts/dev-docs.mjs
bun ./scripts/build-docs.mjs
```

## Workspace hygiene

Keep `OpenSIN-documentation/` scoped to this repo only.

- Put companion repos, local clones, and worktrees in sibling directories such as `~/dev/<repo>`.
- Do **not** place side repos inside the docs repo root, even if they are temporary.
- Before opening a PR, verify the root stays clean with `git status --short`.

## PR checklist

- [ ] Claim is backed by evidence or a source link
- [ ] Surface registry updated when needed
- [ ] Links resolve and anchors still work
- [ ] Build passes locally
- [ ] No nested local repos or worktrees were introduced into the repo root
- [ ] llms files updated when docs map changes

## Review expectations

- Prefer small, surgical documentation updates.
- Keep headings anchor-friendly.
- Avoid overclaiming ownership of live systems.
