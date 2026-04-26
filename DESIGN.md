# OpenSIN Design System v2.0

## Overview

`OpenSIN-documentation` now follows the canonical `awesome-opensin-design` overhaul: OpenAI clarity, GitHub/Primer tokens, Apple spacing discipline, and Uber-style operational directness.

## Visual baseline

- White-first docs shell with dark-mode parity.
- GitHub/Primer blue action system.
- Neutral grays, thin borders, restrained shadows.
- OpenSIN identity is preserved through content and branding, not a competing neon accent system.

## Canonical tokens

- `--vp-c-brand-1`: `#0969da`
- `--vp-c-brand-2`: `#218bff`
- `--vp-c-brand-3`: `#0550ae`
- `--vp-c-brand-soft`: `rgba(9, 105, 218, 0.1)`
- `--vp-c-bg`: `#ffffff`
- `--vp-c-bg-soft`: `#f6f8fa`
- `--vp-c-bg-mute`: `#eaeef2`
- `--vp-c-text-1`: `#1f2328`
- `--vp-c-text-2`: `#656d76`
- `--vp-c-text-3`: `#8c959f`
- `--vp-c-divider`: `#d0d7de`

Dark mode mirrors the same system with GitHub dark tokens:

- `--vp-c-brand-1`: `#4493f8`
- `--vp-c-brand-2`: `#58a6ff`
- `--vp-c-brand-3`: `#388bfd`
- `--vp-c-bg`: `#0d1117`
- `--vp-c-bg-soft`: `#161b22`
- `--vp-c-bg-mute`: `#21262d`
- `--vp-c-text-1`: `#e6edf3`
- `--vp-c-text-2`: `#8b949e`
- `--vp-c-text-3`: `#6e7681`
- `--vp-c-divider`: `#30363d`

## Implementation touchpoints

- `docs/.vitepress/theme/index.ts`
- `docs/.vitepress/theme/style.css`
- `docs/.vitepress/theme/custom.css`

Custom Vue layouts must inherit the same token and interaction system.

## Rules

- Keep VitePress.
- No inline styles for canonical docs surfaces.
- Keep navigation, cards, buttons, icons, and code blocks visually consistent.
- Validate with `bun ./scripts/build-docs.mjs` before PR creation.
- Sync contract changes back to `awesome-OpenSIN-design` and the local skill copy.

::: tip
The full contract lives in `awesome-OpenSIN-design/DESIGN.md` and `awesome-OpenSIN-design/contract.json`.
:::
