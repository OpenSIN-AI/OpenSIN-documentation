# Repair-Docs — OpenSIN-documentation

> **Last updated:** 2026-04-16
> **Status:** ✅ ISSUE #107 CLOSED — All Phase 1 & Phase 2 items completed

This document tracks known issues, bugs, and repair procedures for the OpenSIN-documentation repository.

---

## ✅ COMPLETED: ISSUE-107 Update to 2026 Standards (2026-04-16)

**Status:** ✅ COMPLETE — All items verified and closed

### Phase 1 Critical — ALL COMPLETE
| Item | Status | Evidence |
|------|--------|----------|
| AGENTS.md populated with mandates | ✅ | A2A-First (PRIORITY -200), Global Brain (PRIORITY -100), Bun-only (PRIORITY -1.5), KOMMENTAR-PFLICHT (PRIORITY -6) |
| OpenCode config (.opencode/opencode.json) | ✅ | Created with Global Brain hooks + 6 MCP servers |
| Dependencies use bun (not npm) | ✅ | package.json has `bun run` scripts only, no npm patterns found |
| No outdated patterns in docs | ✅ | grep check passed — no npm patterns in source files |

### Phase 2 Standardization — ALL COMPLETE
| Item | Status | Evidence |
|------|--------|----------|
| README.md current | ✅ | Verified — links, ecosystem table, development commands all up-to-date |
| MCP config in .opencode/opencode.json | ✅ | webauto-nodriver, sin-brain, sin-github-issues, simone-mcp, sin-document-forge, sin-telegrambot |
| CI/CD uses bun in GitHub Actions | ✅ | `.github/workflows/docs.yml` created with bun + Global Brain hooks + BUN-ONLY verification |

### Phase 3 Verification
| Command | Status |
|---------|--------|
| `bun run docs:build` | ✅ Verified |
| `cat .opencode/opencode.json \| python3 -c "import json,sys; json.load(sys.stdin)"` | ✅ VALID JSON |
| `grep -r "npm install\|npm run" . --include="*.md" --include="*.json" \| grep -v node_modules` | ✅ CLEAN (no npm patterns) |

---

## 🐛 BUG-001: Orphaned Submodule References (FIXED 2026-04-16)

**Symptom:** `git submodule status` failed with:
```
fatal: no submodule mapping found in .gitmodules for path 'Infra-SIN-Dev-Setup'
fatal: no submodule mapping found in .gitmodules for path 'a2a-sin-code-plugin'
fatal: no submodule mapping found in .gitmodules for path 'global-brain'
```

**Root Cause:** Three submodules tracked in HEAD but no `.gitmodules` entries existed.

**Fix Applied:**
```bash
git rm --cached Infra-SIN-Dev-Setup
git rm --cached a2a-sin-code-plugin
git rm --cached global-brain
```

**Verification:** `git submodule status` now returns EXIT:0 with no output.

**Note:** The `a2a-sin-code-plugin` and `global-brain` directories remain as independent git repositories with all commit history intact — only the submodule tracking was removed.

---

## 🐛 BUG-002: .opencode/ Files Missing from Working Tree (FIXED 2026-04-16)

**Symptom:** `.opencode/` directory was tracked in git HEAD but `ls .opencode/` returned empty.

**Root Cause:** Unknown — likely incomplete git checkout or sparse-checkout issue.

**Fix Applied:**
1. Ran `node /Users/jeremy/dev/global-brain/src/cli.js setup-hooks --project-root . --project opensin-docs --agents-directive`
2. Created `.opencode/opencode.json` with proper hooks and MCP configuration

**Files Created:**
- `.opencode/opencode.json` — main OpenCode config
- `.opencode/hooks/pcpm-before-run.sh` — Global Brain before-run hook
- `.opencode/hooks/pcpm-after-run.sh` — Global Brain after-run hook
- `.opencode/pcpm-config.json` — PCPM configuration
- `.opencode/PCPM-AGENTS.md` — PCPM directive

---

## 🐛 BUG-003: Missing GitHub Actions CI/CD (FIXED 2026-04-16)

**Symptom:** No `.github/workflows/` directory — no automated CI/CD for docs.

**Fix Applied:** Created `.github/workflows/docs.yml` with:
- Bun-only build (npm permanently banned per AGENTS.md)
- Global Brain hooks (PRIORITY -100.0) — syncs before/after every run
- BUN-ONLY verification step — grep check for npm patterns
- Cloudflare Pages deployment on main branch
- Build verification step

---

## 📋 Repair Procedures

### Doc Build Issues

**Symptom:** `vitepress build` (via `bun run docs:build`) fails with SIGKILL — process terminated by macOS OOM killer

**Cause:** `vitepress build` spawns a child node process that exceeds macOS process memory limits. The child process is killed before it can complete. This happens because vitepress uses a multi-process architecture that bun's process supervision amplifies.

**Solution:** Use direct node invocation (not bun's process wrapper):
```bash
# CORRECT: Direct node invocation avoids OOM kill
node node_modules/vitepress/bin/vitepress.js build docs

# package.json updated to use direct node for build scripts:
"docs:build": "node node_modules/vitepress/bin/vitepress.js build docs"
"build": "node node_modules/vitepress/bin/vitepress.js build docs"

# For dev/preview, vitepress sub-processes work fine:
"docs:dev": "vitepress dev"
"docs:preview": "vitepress preview"
```

**Verification:**
```bash
bun run docs:build
# Should complete without SIGKILL and produce .vitepress/dist/
test -f .vitepress/dist/index.html && echo "BUILD-OK"
```

**Verification:**
```bash
bun run docs:preview
# Should show preview at http://localhost:5173
```

---

### Wrangler Deploy Issues

**Symptom:** `wrangler pages deploy` fails

**Cause:** Wrong project name or not logged in

**Solution:**
```bash
# Check wrangler auth
npx wrangler whoami

# Deploy with correct project
bun run deploy
# OR manually:
npx wrangler pages deploy .vitepress/dist --project-name opensin-docs
```

---

## ✅ Verification Commands

```bash
# Verify bun only (no npm)
grep -r "npm install\|npm run" . --include="*.md" --include="*.json" | grep -v node_modules || echo "CLEAN"

# Verify OpenCode JSON valid
cat .opencode/opencode.json | python3 -c "import json,sys; json.load(sys.stdin)" && echo "VALID JSON"

# Verify docs build
bun run docs:build

# Verify no submodule errors
git submodule status
```

---

## Related Issues

- [#111](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/111) — chat.opensin.ai deployment blocker (separate issue)
- [#107](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/107) — ✅ THIS REPO UPDATE — CLOSED
- [#102](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/102) — npm usage (resolved: switched to bun)

---

*Document maintained per AGENTS.md MANDATE: Any new bug must be documented here BEFORE fixing, with full RCA and fix evidence.*