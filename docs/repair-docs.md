# Repair-Docs — OpenSIN-documentation

> **Last updated:** 2026-04-16

This document tracks known issues, bugs, and repair procedures for the OpenSIN-documentation repository.

---

## Known Issues

### ISSUE-107: OpenSIN-documentation Update to 2026 Standards

**Status:** 🟡 IN PROGRESS

**Phase 1 Completed:**
- ✅ AGENTS.md populated with latest mandates (A2A-First, Global Brain, Bun-only)
- ✅ OpenCode config verified (minimal `{}` schema is correct)
- ✅ Dependencies use bun (package.json has `bun run` scripts)
- ✅ No GitHub Actions (uses Wrangler for deployment per mandate)

**Phase 2 In Progress:**
- 🔄 repair-docs.md creation (THIS FILE)
- ⬜ MCP config verification in .opencode/opencode.json

**Phase 3 Pending:**
- ⬜ Verification commands run

---

## Repair Procedures

### Doc Build Issues

**Symptom:** `vitepress build` fails with memory issues

**Cause:** Node.js/Vite can consume 4-6 GB RAM

**Solution:**
```bash
# Use bun instead of npm (bun uses ~500MB)
bun run docs:build

# If still failing, try with limited concurrency
NODE_OPTIONS="--max-old-space-size=4096" bun run docs:build
```

**Verification:**
```bash
bun run docs:preview
# Should show preview at http://localhost:5173
```

---

### Submodule Sync Issues

**Symptom:** Submodule shows "modified content" in git status

**Cause:** global-brain submodule not synced

**Solution:**
```bash
cd /Users/jeremy/dev/OpenSIN-documentation
git submodule update --init --recursive
# OR
git submodule update --remote global-brain
```

**Verification:**
```bash
git submodule status
# Should show commit hash without +/- prefix
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

## Validation Commands

```bash
# Verify bun only (no npm)
grep -r "npm install\|npm run" . --include="*.md" --include="*.json" | grep -v node_modules || echo "CLEAN"

# Verify OpenCode JSON valid
cat .opencode/opencode.json | python3 -c "import json,sys; json.load(sys.stdin)" && echo "VALID JSON"

# Verify docs build
bun run docs:preview &
# Then check http://localhost:5173
```

---

## Related Issues

- [#111](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/111) — chat.opensin.ai deployment blocker
- [#107](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/107) — This repository update
- [#102](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/102) — npm usage (resolved: switched to bun)

---

*Document created as part of Issue #107 cleanup*