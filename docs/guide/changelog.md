# Changelog

## v1.0.10 (2026-04-26)

### Fixed
- Security surface claims corrected and aligned with private advisory flow.
- Cloudflare Pages deployment pipeline stabilized; CI/CD green on `main`.
- Resolved design/deploy inconsistencies merged from `docs/design/security/deploy`.

### Pending
- Issue #150 remains open pending external credential-rotation confirmation (blocked/external).

---

## v1.2.0 (2026-04-21)

### Changed
- Added a repeatable best-practice page pattern for VitePress-first docs authoring.
- Normalized the `browser-automation`, `seo-pipeline`, and `simone-mcp-pcpm` pages around the shared pattern.
- Improved code-block and inline-code readability across light and dark themes.

---

## v1.1.0 (2026-04-21)

### Changed
- Polished the docs homepage inside the existing VitePress `layout: home` contract instead of rebuilding it.
- Unified hero, feature, and custom homepage card styling behind shared surface tokens so the premium treatment is consistent across light and dark mode.
- Added in-code comments around the protected 3/2/4 homepage structure and homepage-only theme logic to reduce accidental regressions.

---

## v0.1.0 (2026-04-04)

### Added
- Initial OpenSIN release
- QueryEngine with async generator pattern
- Hook System with 20+ events
- Tool System with 8+ built-in tools
- Permission System with 6 modes
- Subagent System with fork pattern
- MCP Client with 5 transports
- Sandbox with filesystem/network rules
- Memory System with file-based storage
- CLI for agent and team management
- API Server with REST endpoints
- Python SDK for programmatic access

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
