---
name: create-telegrambot
description: "Master-level workflow for creating, editing, deploying, operating, and recovering Telegram bots with API-first automation, BotFather/Desktop bootstrap, and near-zero manual user interruption."
license: MIT
compatibility: opencode
metadata:
  audience: senior-engineering
  mode: autonomous-product-operator
  language: en
---

> OpenCode SSOT: sourced from the `opencode-create-telegrambot-skill` repository and symlinked into `~/.config/opencode/skills/` for global OpenCode usage.

# Create TelegramBot Skill

Use this skill when the user wants to create, edit, deploy, scale, recover, or professionally operate a Telegram bot, Telegram bot platform, Telegram Mini App, or Telegram-based agent workflow.

Triggers (examples)
- "create telegram bot", "build a telegram bot", "edit telegram bot", "deploy telegram bot", "botfather", "telegram commands", "telegram webhook", "telegram polling", "telegram mini app", "chat id", "set telegram commands", "telegram automation", "telegram bot ops", "telegram bot recovery".

Mission
- Turn any agent into a Telegram bot developer + operator + product owner that can plan, bootstrap, build, test, deploy, run, and recover Telegram bots with minimal user interruption.

Core operating model
- API-first: use the Telegram Bot API for anything the Bot API can do deterministically.
- App-automation second: use Telegram Desktop/App or Telegram Web automation only for surfaces the Bot API cannot do, especially BotFather bootstrap and first-chat bootstrap.
- Manual-last: ask the user only when Telegram itself forces an unrecoverable human-only checkpoint.
- Webhook-first for production, polling-only for local development, temporary fallback, or constrained hosting.
- Treat the bot as a product surface, not just a command handler.

What makes this skill exceptional
- It should make agents think like Telegram bot founders/operators, not just coders.
- Every serious Telegram bot task is handled across four layers: product, bootstrap, code/runtime, and recovery.
- The skill should actively reduce user annoyance by automating BotFather, first-chat bootstrap, chat_id capture, command registration, and webhook repair wherever environment tooling allows it.
- The end result should feel like a Telegram bot developer CEO is in the loop: product clarity, ruthless automation, operational discipline, and recovery readiness.

Built-in micro-scripts
- `scripts/telegrambot-render-botfather-bootstrap.mjs` - generate concrete BotFather/Telegram.app bootstrap AppleScripts from the templates
- `scripts/telegrambot-bootstrap-chat-id.py` - capture the latest useful chat_id from Bot API updates and optionally write it into local config
- `scripts/telegrambot-verify-runtime.py` - verify token, bot identity, webhook state, commands, and chat-id presence
- `scripts/telegrambot-scaffold-ops.mjs` - scaffold `.env.example`, command docs, runbooks, and bootstrap scripts for a real bot project
- `scripts/telegrambot-preflight.mjs` - front-door verifier that chains runtime + chat bootstrap checks

## 🚨 CANONICAL FLEET TELEGRAM TOOLING (MANDATORY — USE BEFORE WRITING CUSTOM CODE)

Before writing any custom Telegram send/receive code, ALWAYS use the fleet-wide `sin-telegrambot` CLI and `MCP-SIN-TelegramBot` MCP. They are the canonical, tested, zero-manual-step Telegram layer for ALL SIN agents.

### sin-telegrambot CLI (globally installed at `~/.local/bin/sin-telegrambot`)

```bash
sin-telegrambot register <token> [--name <alias>] [--chat-id <id>]
sin-telegrambot list
sin-telegrambot bootstrap <name>          # Auto-discovers chat_id via Telegram.app — NO /start needed from user
sin-telegrambot send <bot> "<text>" [--chat-id <id>] [--parse-mode HTML] [--buttons <json>]
sin-telegrambot send-document <bot> <file> [--caption "..."]
sin-telegrambot status <bot>             # Identity, webhook, known chat_id
sin-telegrambot updates <bot> [--limit N]
sin-telegrambot poll <bot>              # Live-stream updates (dev mode)
sin-telegrambot set-webhook <bot> <url> [--secret <tok>]
sin-telegrambot delete-webhook <bot>
sin-telegrambot set-commands <bot> '[{"command":"start","description":"Begin"}]'
```

Bot registry: `~/.config/sin-telegrambot/bots.json`
CLI source: `/Users/jeremy/dev/sin-telegrambot-cli/sin_telegrambot.py`

### MCP-SIN-TelegramBot (wired in `~/.config/opencode/opencode.json`)

All CLI operations available as MCP tools: `sin_telegrambot_register`, `sin_telegrambot_bootstrap`, `sin_telegrambot_send`, `sin_telegrambot_send_document`, `sin_telegrambot_status`, `sin_telegrambot_updates`, `sin_telegrambot_set_webhook`, `sin_telegrambot_delete_webhook`, `sin_telegrambot_set_commands`.
MCP source: `/Users/jeremy/dev/sin-telegrambot-cli/mcp/mcp_sin_telegrambot.py`

### How to wire a new A2A agent to Telegram (zero manual steps)

```bash
# 1. Get token from BotFather (or automate via botfather-create.sh — see template)
# 2. Register with CLI
sin-telegrambot register <TOKEN> --name <mybotname>
# 3. Auto-bootstrap chat_id (Telegram.app sends /start automatically)
sin-telegrambot bootstrap <mybotname>
# 4. Send from any script
sin-telegrambot send <mybotname> "Hello from <b>MyAgent</b>!"
# 5. Send with inline buttons
sin-telegrambot send <mybotname> "Choose action:" --buttons '[[{"text":"Go","callback_data":"go"}]]'
```

### Sending from Python (use subprocess, not raw HTTP)

```python
import subprocess, json

def tg_send(bot_alias: str, text: str, buttons: list = None) -> dict:
    argv = ["sin-telegrambot", "send", bot_alias, text, "--parse-mode", "HTML"]
    if buttons:
        argv += ["--buttons", json.dumps(buttons)]
    result = subprocess.run(argv, capture_output=True, text=True, timeout=20)
    return json.loads(result.stdout.strip()) if result.stdout.strip() else {"ok": False}
```

### Key breakthrough: auto-bootstrap without user clicking /start

`sin-telegrambot bootstrap <name>` uses macOS Telegram.app AppleScript to automatically open BotFather search, navigate to the bot, and send `/start` — then reads the resulting chat_id from `getUpdates`. The user never has to manually do anything.

Mandatory guardrails
- Never hardcode bot tokens, webhook secrets, admin IDs, chat exports, or production credentials in repo files.
- Always store secrets in approved local config, environment injection, or the project secret manager.
- Never log raw Telegram updates wholesale; redact PII, tokens, phone numbers, invite links, and payment payloads.
- All update handling must be idempotent; duplicate delivery must not create duplicate side effects.
- Separate Telegram transport, conversation state, and business logic.
- Use explicit permission boundaries for private chats, groups, supergroups, channels, and admins.
- All destructive admin actions need a confirmation gate plus audit logging.
- Long-running work must move to async jobs with progress/status updates, not block the update handler.
- Group/community bots require anti-abuse posture: per-chat throttles, moderation policy, and safe defaults.
- Recovery is part of done: webhook rebind, token rotation, replay/retry, and degraded mode must be documented.
- Every new Telegram bot must be registered via `sin-google-apps` in the Google Sheets backbone first, then reflected in the Google Docs summary tab.
- Canonical Sheets backbone: `SIN Telegram Bots Registry` -> spreadsheet `1tR4xsHUsqjFmLXzCaCujI-uz6Z5okuJ3ak2Ct0TFO3M`, sheet `Telegram Bots`.
- Canonical Docs summary/navigation tab: `SIN Telegram Bots` (`t.msgg9oi1mot8`) inside document `1RtoHn4I0GntuEEOHHkqoh_dMuGzgMwQz7_8oxAOpQbw`.
- The registry row must include at least: type, name, purpose, bot username, commands, bootstrap path, runtime/deploy mode, secret source, status, repo/path, and docs/runbook.

Capability map (Bot API + operator scope)
- Identity and profile
  - create/edit bot profile via BotFather bootstrap
  - set name, username, description, short description, about text, commands, menu button, default admin rights
- Messaging
  - send/edit/delete text
  - reply, thread/forum-topic targeting
  - parse modes / entities
  - pin/unpin, reactions where applicable, silent/protected sends
- Keyboards and navigation
  - reply keyboards
  - inline keyboards
  - callback data versioning
  - deep-link start payload routing
- Media and files
  - photos, video, audio, voice, stickers, documents, albums
  - cache `file_id` instead of re-uploading when possible
  - object storage bridge for downloaded content
- Chat and admin surfaces
  - group bootstrap, admin whitelists, moderation and membership flows
  - topic-aware bots for forum chats
  - business/admin commands for pause, resume, status, replay, drains
- Inline mode and discovery
  - inline query answering
  - switch-to-chat results
  - menus and commands with BotFather registration
- Payments and commerce
  - Telegram payments, invoices, pre-checkout handling, successful payments, stars/credits if relevant
- Mini Apps / Web Apps
  - launch from keyboards and menus
  - signed init data validation
  - server-side session handoff and operator analytics
- Runtime operations
  - webhook registration
  - polling fallback
  - release gates, monitoring, replay, incident response

Decision ladder: what to use when
1. Telegram Bot API
   - Use for send/edit/delete messages, commands, menus, webhooks, updates, media, payments, inline mode, admin tools, and health checks.
2. Telegram Desktop/App automation
   - Use for BotFather bootstrap, first `/start`, forced client-side actions, one-time chat discovery, and bootstrap messages when the bot cannot yet self-bootstrap.
   - Prefer local app automation via the available macOS/browser automation stack, especially Telegram.app control, AppleScript, and webauto-nodriver-backed app steering.
3. Telegram Web automation
   - Use only when Desktop/App automation is unavailable or the workflow is explicitly web-only.
4. TDLib / MTProto
   - Use only if the product truly requires user-account capabilities beyond Bot API scope. Default: avoid this complexity.

Advanced operator patterns
- Hybrid webhook/polling recovery with automatic fallback and offset persistence.
- Deterministic first-chat bootstrap: send `/start` from Telegram Desktop/App, then read the resulting chat_id from Bot API updates.
- Multi-bot or multi-account control plane only when justified; default to one active production identity per bot surface.
- Session-aware automation: do not restart or kill active operator sessions if the bot/runtime is healthy.
- Media and asset efficiency: reuse `file_id`, cache asset mapping, and avoid blind re-upload.
- Recovery ladder: retry -> fallback mode -> replay -> rebind webhook -> admin alert.

Default workflow

Phase 1 - Product framing
- define the bot's purpose, target chats, top 3 flows, admin model, and success metric
- identify whether it is utility, SaaS, commerce, support, community, or agent-control bot

Phase 2 - Architecture
- choose webhook or polling
- choose TypeScript/Node or Python stack
- define state store, queue needs, external integrations, and recovery posture
- justify every dependency beyond the minimal baseline

Phase 3 - Bootstrap and provisioning
- create or recover the bot via BotFather if needed
- capture bot token safely into local config / env / secret manager
- register commands, descriptions, menus, and deep-link strategy
- discover or create admin chat and chat_id automatically from first interaction whenever possible

Phase 3b - BotFather automation subworkflow
- Prefer Telegram.app/Desktop automation first:
  - open Telegram.app
  - search `@BotFather`
  - create bot with `/newbot`
  - send bot display name and username
  - capture returned token from BotFather response
  - immediately store token into approved config/secret surface
- If Telegram.app automation is unavailable, use Telegram Web automation through the approved browser automation stack.
- After bootstrap, immediately set commands/descriptions and send `/start` to the new bot to trigger deterministic chat bootstrap.
- Then fetch Bot API `getUpdates` to capture the first `chat_id` and save it without bothering the user.
- Prefer the built-in helpers where possible:

```bash
node scripts/telegrambot-render-botfather-bootstrap.mjs --display-name "My Bot" --username my_bot --output-dir /abs/path/to/output
python3 scripts/telegrambot-bootstrap-chat-id.py --config-path ~/.config/opencode/telegram_config.json --write-config --prefer-start
```

Phase 4 - Bot skeleton
- add config loader, update router, command registry, callback handlers, service layer, health endpoint, structured logging, and graceful shutdown
- make startup validate required env before serving traffic
- use `scripts/telegrambot-scaffold-ops.mjs` to generate baseline operational assets before hand-writing drift-prone docs/scripts

Phase 5 - Chat bootstrap
- implement `/start` as an idempotent capability introduction, not a throwaway hello-world
- auto-register user/chat/admin records
- support deep links like `t.me/<bot>?start=<payload>`
- support locale/timezone capture if relevant

Phase 6 - Feature delivery
- implement commands, callbacks, background tasks, integrations, and media flows
- keep domain logic outside Telegram adapter code
- version callback payloads and conversation schemas

Phase 7 - Test and verify
- unit tests for handlers and service layer
- fixtures for real Telegram update payloads
- conversation and callback flow tests
- smoke tests for webhook/polling startup and bot API boundary behavior
- recommended front-door verifier:

```bash
node scripts/telegrambot-preflight.mjs --config-path ~/.config/opencode/telegram_config.json
```

Phase 8 - Deploy and register runtime
- deploy webhook endpoint with HTTPS and secret token validation
- register webhook automatically on release or startup
- configure observability and admin controls before calling it done

Phase 9 - Operate like a pro
- provide `/status`, `/health`, `/pause`, `/resume`, `/replay`, `/admin` or equivalent control lane
- track update volume, errors, latency, retries, and cost where AI/tooling is involved
- add flood-wait handling, backoff, and operator kill switch

Phase 10 - Recovery and change management
- document token rotation, webhook rebind, replay strategy, DB/schema migration, rollback plan, and outage message path
- ship docs/runbooks with the code

Zero-manual playbooks
- Bot bootstrap
  - prefer Telegram Desktop/App automation to open BotFather, create the bot, capture token, and seed command config
- Chat bootstrap
  - send `/start` automatically from Telegram Desktop/App when needed, then read the resulting chat_id from Bot API updates
- Command/menu setup
  - set commands and bot descriptions immediately after token bootstrap
- Webhook bootstrap
  - register webhook on startup or via deterministic deploy script; verify with `getWebhookInfo`
- Recovery
  - on webhook failure, temporarily switch to polling with persisted offset and revert when healthy
- Media handling
  - cache `file_id`, never re-upload the same media blindly
- Registry sync
  - after every new Telegram bot is created or materially changed, prefer the one-call orchestrator `google.registry.sync_enterprise_docs_sheets`
  - if the orchestrator is not suitable, update the Google Sheets backbone through `google.sheets.publish_enterprise_registry` or `google.sheets.write_table`
  - then refresh the Google Docs summary/navigation tab so Docs stays executive-grade and Sheets remains the live row source of truth

Environment-specific operator surfaces
- If the environment provides local Telegram app control, use it first for BotFather and first-chat bootstrap.
- If the environment provides browser automation for Telegram Web, use it as fallback, not as the default path.
- If the environment provides a secret manager, store bot token and webhook secrets there immediately after bootstrap.

Preferred stack (2026 default)
- TypeScript + `grammY` for greenfield webhook-first bots
- Python + `python-telegram-bot` for Python-native projects or data/ops-heavy stacks
- Redis for ephemeral conversation/session state; SQLite only for small/local bots
- Prometheus/Grafana or equivalent for metrics; structured JSON logs for runtime shipping
- GitHub Actions or platform-native CI for deploy + webhook registration + smoke tests

BotFather / bootstrap strategy
- Use automation for BotFather whenever possible; do not make the user click through routine setup if local Telegram automation is available.
- Capture these outputs deterministically:
  - bot token
  - bot username
  - configured command list
  - optional menu button / description state
- Save only to approved config/secret surfaces.

Chat ID and admin discovery strategy
- Default: infer chat_id from the first inbound `/start` or any update.
- If no inbound update exists yet, automate Telegram Desktop/App to send `/start` to the bot.
- Persist chat mappings and admin IDs in project state.
- Never ship placeholder chat IDs in production config.

Webhook vs polling rules
- Production default: webhook with HTTPS + secret token validation.
- Local development: polling is acceptable if offset is persisted and duplicate handling is safe.
- Fallback mode: switch to polling only temporarily when webhook health is degraded.

Anti-abuse and safety
- respect Telegram flood limits and `retry_after`
- throttle per chat and globally
- require allowlists or admin confirmation for high-risk actions
- for community/group bots, define moderation and escalation policy explicitly
- if AI/tool execution exists, enforce cost caps, tool allowlists, and escalation boundaries

Data and state rules
- Store only what is needed for the active flow.
- Version callback payloads and conversation state.
- Use TTLs for idle sessions.
- Make jobs and update processing replay-safe.

Definition of done
- working bot runtime
- safe token/config handling
- commands and menus configured
- chat bootstrap path documented and preferably automated
- tests for critical flows
- deploy/redeploy scripts
- admin/operator command lane
- monitoring and recovery docs

Deliverables you should produce
- bot code or patch
- `.env.example` / config schema
- command catalog
- deploy script or platform config
- webhook/polling bootstrap script
- admin/runbook docs
- recovery instructions
- if requested: Telegram Desktop/App bootstrap helper scripts
- Google Sheets registry row for the bot in `1tR4xsHUsqjFmLXzCaCujI-uz6Z5okuJ3ak2Ct0TFO3M`
- Google Docs summary/navigation refresh in `t.msgg9oi1mot8`

Do not do this
- do not hardcode bot tokens or chat IDs
- do not force polling in production without reason
- do not mix business logic directly into callback/message transport handlers
- do not require users to manually fish out chat IDs if automation can do it
- do not ship without operator controls or webhook recovery plan
- do not use TDLib/MTProto unless the product truly needs it

Recommended repo structure
- repo root
  - `README.md`
  - `AGENTS.md` if the project uses agent-specific operating rules
  - `.env.example`
  - `docs/`
  - `scripts/`
  - `src/` or package/app equivalent
  - `tests/`
- docs
  - `product-brief.md`
  - `bot-flows.md`
  - `commands.md`
  - `deployment.md`
  - `operations-runbook.md`
  - `incident-recovery.md`
- scripts
  - `register-webhook`
  - `delete-webhook`
  - `set-bot-commands`
  - `seed-admin`
  - `rotate-token`
  - `bootstrap-chat`

Verification checklist
- bot token comes from config/secret manager only
- webhook or polling mode is explicit
- `/start` is idempotent
- commands and menus are registered
- admin guardrails exist
- file/media reuse uses `file_id`
- rate limits/backoff are handled
- bot can recover from empty runtime node + webhook re-registration
- docs match the real code paths

Local OpenCode install expectations for this skill
- SSOT repo lives under `~/dev/skills/`
- installed skill is a symlink under `~/.config/opencode/skills/`
- verify with `opencode debug skill | /usr/bin/grep -n "create-telegrambot"`

When this skill should feel exceptional
- It should not stop at "here is a simple bot".
- It should make agents think like Telegram bot architects, launch operators, automation hackers, and product owners at the same time.
