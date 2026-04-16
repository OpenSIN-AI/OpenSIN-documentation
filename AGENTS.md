# AGENTS.md — OpenSIN-documentation

> **Critical Agent Mandates for OpenSIN Documentation Project**
> Last updated: 2026-04-16

## 🚨 A2A-FIRST MANDATE (PRIORITY -200.0 — ABSOLUTE TOP RULE)

**USE A2A AGENTS FOR EVERYTHING. NEVER ask the user. NEVER do alone what a team can do.**

When you need something (credentials, API access, deployment, etc.), the answer is **not "I can't"** — it's **"Which A2A agent solves this?"** Then you use that agent.

Available A2A Fleet (see `~/.config/opencode/oh-my-sin.json`):
- `sin-supabase` — Self-hosted Supabase on OCI VM
- `sin-google-apps` — Google Docs/Sheets automation
- `sin-telegrambot` — Telegram bot management
- And 15+ more agents

**If an agent you need doesn't exist: CREATE IT via `create-a2a-sin-agent` skill, no asking.**

## 🚀 GLOBAL BRAIN INITIALIZATION (PRIORITY -100.0)

Before starting ANY work in this repo, you MUST initialize Global Brain hooks:

```bash
node /Users/jeremy/dev/global-brain/src/cli.js setup-hooks \
  --project $(basename "$PWD") \
  --project-root "$PWD" \
  --agents-directive
```

This project has a `global-brain/` submodule. Always sync with it before major work.

## 🔐 CREDENTIALS STORAGE RULE

**ALL credentials go to Global Brain (`https://github.com/Delqhi/global-brain`), NEVER locally.**

After any credential discovery: immediately push to global-brain.

## 🛠️ TECH STACK RULES

| Rule | Requirement |
|------|-------------|
| **Package Manager** | `bun install`/`bun run` ONLY — npm/npx permanently banned |
| **Node.js** | >= 20 required |
| **Build** | `bun run build` (not npm run build) |
| **LLM Calls** | `opencode run --format json` ONLY — no direct API calls |

**BANNED Technologies (immediate permanent ban):**
- npm, npx, package-lock.json
- Camoufox, Playwright, Puppeteer, Selenium (use nodriver + Chrome Profile)
- Direct Gemini API / `generativelanguage.googleapis.com`

## 🌐 BROWSER AUTOMATION RULES

1. **webauto-nodriver-mcp** is the ONLY authorized browser automation tool
2. **Always use Chrome Profile** — never `user_data_dir=None`
3. **VISION-GATE MANDATE**: After EVERY browser action, take screenshot and verify with vision model
4. **NO blind clicks** — every selector must be verified via DevTools first

## 📋 ISSUE 107: UPDATE TO 2026 STANDARDS

This repo is flagged for update to OpenSIN 2026 standards. Key areas:

### Phase 1 Critical (in progress)
- [x] AGENTS.md — populated with mandates (THIS FILE)
- [ ] OpenCode config — verify minimal config is correct
- [ ] Dependencies — check all use bun, not npm
- [ ] Check for outdated patterns in docs

### Phase 2 Standardization
- [ ] Docs: verify README.md current
- [ ] MCP config in .opencode/opencode.json
- [ ] CI/CD uses bun in GitHub Actions

## 📁 PROJECT STRUCTURE

```
OpenSIN-documentation/
├── docs/               # VitePress documentation
│   ├── guide/          # User guides
│   ├── api/            # API reference
│   ├── architecture/   # System architecture
│   ├── fleet/          # A2A Agent Fleet docs
│   ├── governance/     # Zeus, Hermes, PR-Watcher
│   └── ...
├── global-brain/       # Submodule — PCPM system
├── .opencode/          # OpenCode hooks + flows
├── .pcpm/              # Persistent Code Plan Memory
└── package.json        # VitePress + wrangler
```

## 🔗 REFERENCE DOCUMENTS

- Global Brain AGENTS.md: `global-brain/AGENTS.md`
- OpenSIN Main: `https://github.com/OpenSIN-AI/OpenSIN`
- A2A Template: `https://github.com/OpenSIN-AI/Template-A2A-SIN-Agent`
- Global Brain Repo: `https://github.com/Delqhi/global-brain`

## ✅ VERIFICATION COMMANDS

Before claiming work complete, run:

```bash
# Verify bun only
grep -r "npm install\|npm run" . --include="*.md" --include="*.json" | grep -v node_modules || echo "CLEAN"

# Verify OpenCode JSON valid
cat .opencode/opencode.json | python3 -c "import json,sys; json.load(sys.stdin)" && echo "VALID JSON"

# Verify docs build
bun run docs:build
```

## 🚫 ABSOLUTE PROHIBITIONS

1. **NEVER assume** — verify everything with real data/logs
2. **NEVER commit without visual evidence** of working functionality
3. **NEVER use npm** — instant ban
4. **NEVER blind browser automation** — screenshot + vision gate required
5. **NEVER store credentials locally** — global-brain only

---

*This AGENTS.md is the project-specific overlay. The global brain (`global-brain/AGENTS.md`) contains the full mandate stack.*