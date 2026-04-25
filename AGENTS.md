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
| **Package Manager** | `bun install` / direct `bun` scripts ONLY — npm/bunx permanently banned |
| **Node.js** | >= 20 required |
| **Build** | `bun ./scripts/build-docs.mjs` |
| **LLM Calls** | `opencode run --format json` ONLY — no direct API calls |

**BANNED Technologies (immediate permanent ban):**
- npm, bunx, package-lock.json
- Camoufox, Playwright, Puppeteer, Selenium (use nodriver + Chrome Profile)
- Direct Gemini API / `generativelanguage.googleapis.com`

## 🌐 BROWSER AUTOMATION RULES

1. **webauto-nodriver-mcp** is the ONLY authorized browser automation tool
2. **Always use Chrome Profile** — never `user_data_dir=None`
3. **VISION-GATE MANDATE**: After EVERY browser action, take screenshot and verify with vision model
4. **NO blind clicks** — every selector must be verified via DevTools first

## 📋 ISSUE 107: UPDATE TO 2026 STANDARDS

**OpenAI Token Rotator Pipeline (2026)** is now documented at [`docs/examples/openai-token-rotator-pipeline-2026.md`](docs/examples/openai-token-rotator-pipeline-2026.md).

Three production modules:
- [`modul-google-alias-rotator`](https://github.com/SIN-Rotator/modul-google-alias-rotator)
- [`modul-openai-auth-rotator`](https://github.com/SIN-Rotator/modul-openai-auth-rotator) (dynamic birthday/age UI + signal-file keep-alive)
- [`modul-opencode-gpt-rotator`](https://github.com/SIN-Rotator/modul-opencode-gpt-rotator) (CDP connect to live Chrome session)

All issues closed, main branches clean, full E2E architecture with `/tmp/auth_rotator_done` + `/tmp/auth_rotator_release` signal files verified.

This repo is flagged for update to OpenSIN 2026 standards. Key areas:

### Phase 1 Critical (in progress)
- [x] AGENTS.md — populated with mandates (THIS FILE) ✅
- [x] OpenCode config — verify minimal config is correct ✅
- [x] Dependencies — check all use bun, not npm ✅ (uses bun, no npm)
- [x] Check for outdated patterns in docs ✅
- [x] **NEW: Dynamic Input Commands ($ARGUMENTS/$1/$2)** — INTEGRATED

### Phase 2 Standardization
- [x] Docs: verify README.md current ✅ (updated with new structure)
- [x] MCP config in .opencode/opencode.json ✅ (webauto-nodriver, sin-brain, sin-github-issues, simone-mcp, sin-document-forge, sin-telegrambot)
- [x] CI/CD uses direct Bun build in GitHub Actions ✅ (Cloudflare Pages action, no npm/bunx)

### ✅ COMPLETED: Dynamic Input Commands (2026-04-16)

25 new browser-automation commands with `$ARGUMENTS`/`$1`/`$2` substitution:

| Command | Purpose |
|---------|---------|
| `/browser-goto $ARGUMENTS` | URL navigation + Vision-Gate |
| `/click-at $1 $2` | Coordinate click + Vision-Gate |
| `/click-element-safe $ARGUMENTS` | Safe element click + Vision-Gate |
| `/vision-gate-check $ARGUMENTS` | MANDATORY Vision verification |
| `/whatsapp-send $1 $ARGUMENTS` | WhatsApp messaging |
| `/mac-calendar-create $ARGUMENTS` | Calendar events |
| `/run-shell-cmd $ARGUMENTS` | Shell commands |
| `/execute-javascript $ARGUMENTS` | Browser JS execution |

**Reference:** `docs/guides/dynamic-input-commands.md`

---

### 🚀 QUICK START: Browser Automation

```bash
# Navigate + Vision-Gate
/browser-goto https://github.com/OpenSIN-AI

# Click at coordinates + Vision-Gate
/click-at 512 384

# Safe element click (selector first, then coords fallback)
/click-element-safe "a[data-tab-item='i1issues-tab']"

# MANDATORY after EVERY action:
/vision-gate-check "Klick auf Button"
```

**Rule: NO blind clicks! Every browser action MUST have Vision-Gate!**

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
# Verify bun only (no npm)
grep -r "npm install\|npm run\|npx \|bunx " . --include="*.md" --include="*.json" | grep -v node_modules || echo "CLEAN"

# Verify OpenCode JSON valid
cat .opencode/opencode.json | python3 -c "import json,sys; json.load(sys.stdin)" && echo "VALID JSON"

# Verify docs build (direct Bun invocation; bun run is broken on this machine)
bun ./scripts/build-docs.mjs
```

## 🚫 ABSOLUTE PROHIBITIONS

1. **NEVER assume** — verify everything with real data/logs
2. **NEVER commit without visual evidence** of working functionality
3. **NEVER use npm** — instant ban
4. **NEVER blind browser automation** — screenshot + vision gate required
5. **NEVER store credentials locally** — global-brain only
6. **NEVER leak top-secret project details** (SIN-Rotator pipeline internals, credentials, CLI commands) into public or global-facing docs — modul-level AGENTS.md only

---

*This AGENTS.md is the project-specific overlay. The global brain (`global-brain/AGENTS.md`) contains the full mandate stack.*

## Boundary Guidance for Agents

When modifying this repo:

- Prefer official documentation work.
- Keep claims scoped to documentation canon.
- Do not redefine runtime, product, ops, or org registry ownership from here.
