---

# 🚨 HUGGING FACE SPACE HARDWARE RULE (PRIORITY -7 — ABSOLUT, KEINE AUSNAHMEN) 🚨

**ABSOLUTES VERBOT: KEINE GPU/ZeroGPU SPACES FÜR A2A AGENT RUNTIMES!**

- HF Free Tier erlaubt **UNBEGRENZT CPU-Basic Spaces** gleichzeitig — komplett kostenlos
- GPU/ZeroGPU Spaces haben Quota-Limits (8x pro Account) und benötigen Payment
- **ALLE** A2A Agent Spaces MÜSSEN auf `cpu-basic` Hardware konfiguriert sein
- **NIEMALS** `gpu`, `zerogpu`, oder paid Hardware für Agent Runtimes verwenden
- **IMMER** Keep-Alive-Ping alle 5 Minuten implementieren (verhindert 48h Sleep)

### KORREKTE SPACE ERSTELLUNG

```bash
curl -X POST https://huggingface.co/api/repos/create \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "sin-my-agent", "type": "space", "sdk": "docker"}'

curl -X POST https://huggingface.co/api/spaces/{owner}/{space}/hardware \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"flavor": "cpu-basic"}'
```

### KOSTEN

| Hardware | Kosten | Max gleichzeitig |
|----------|--------|-----------------|
| `cpu-basic` | **$0 (FREE)** | **UNBEGRENZT** |
| `zerogpu` | FREE | 8 pro Account |
| `gpu (T4)` | $288/Mo | Unbegrenzt (Payment) |

**FAZIT: CPU-Basic = $0, UNBEGRENZT Spaces, KEIN Payment nötig!**

Siehe auch: [Global Dev Docs HF Space Hardware Standard](https://github.com/OpenSIN-AI/Global-Dev-Docs-Standard/blob/main/standards/hf-space-hardware.md)

name: create-a2a
description: Create, standardize, or upgrade SIN A2A agents using the canonical SIN template, private GitHub repo provisioning, team-manager registry rules, dedicated Google Docs sync, A2A card requirements, and fleet validation. Use whenever a new SIN A2A agent must be built or an existing one must be brought up to the 2026 fleet standard. Includes the mandatory Infinite Scaling Producer-Consumer Auth architecture for HF VMs.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/create-a2a` and mirrored for OpenCode CLI usage.

# SIN A2A Agent Forge (CEO Edition)

## 🚨 LLM-AUFRUF PFLICHT-ARCHITEKTUR — ABSOLUT, KEINE AUSNAHMEN

**JEDER A2A Agent ruft LLMs AUSSCHLIESSLICH über die `opencode` CLI auf — NIEMALS über direkte API-Calls!**

```python
import subprocess, json

def call_llm(prompt: str, timeout: int = 120) -> str:
    result = subprocess.run(
        ["opencode", "run", prompt, "--format", "json"],
        capture_output=True, text=True, timeout=timeout,
    )
    parts = []
    for line in result.stdout.splitlines():
        try:
            ev = json.loads(line)
            if ev.get("type") == "text":
                parts.append(ev.get("part", {}).get("text", ""))
        except json.JSONDecodeError:
            pass
    return "".join(parts).strip()
```

**REGELN:**
- `opencode run --format json` nutzt das Antigravity Plugin — identisch auf Mac, OCI VM und HF VMs
- OCI-Proxy `http://92.5.60.87:4100/v1` direkt per HTTP anrufen = VERBOTEN (500-Fehler)
- Gemini API direkt = PERMANENT VERBOTEN
- Anthropic API direkt = PERMANENT VERBOTEN
- **Primärmodell:** `opencode/qwen3.6-plus-free` für ALLE allgemeinen A2A Agenten
- **Fallback:** `opencode/nemotron-3-super-free` für ALLE Agenten
- **Ausnahme:** `multimodal-looker` behält `google/antigravity-gemini-3.1-pro`
- **Ausnahme:** `sin-worker-prolific` verwendet `google/antigravity-gemini-3-flash` (schneller, vision-fähig, höhere Rate Limits)
- CLI Aufruf: `opencode run "..." --model opencode/qwen3.6-plus-free --fallback opencode/nemotron-3-super-free`

Use this skill when the task is any of:
- create a new SIN A2A agent
- standardize an existing SIN A2A agent
- repair missing agent files, card metadata, registry entries, team-manager ownership, or dedicated-doc sync
- scaffold a new agent from the canonical company template
- deploy an agent to a Hugging Face VM using the Infinite Scaling Producer-Consumer Auth pattern

This skill is the only approved creation path for new SIN A2A agents. We build fleets that scale infinitely, not fragile single-instance toys.

## 🏛️ Single Source of Truth

- Template repo: `/Users/jeremy/dev/OpenSIN-backend/a2a/template-repo/A2A-SIN-Agent-Template`
- Scaffold script: `/Users/jeremy/dev/OpenSIN-backend/scripts/create-sin-a2a-agent.mjs`
- Agent detail page scaffold: `/Users/jeremy/dev/OpenSIN-backend/scripts/scaffold-a2a-agent-page.mjs`
- Fleet validator: `/Users/jeremy/dev/OpenSIN-backend/scripts/validate-sin-a2a-fleet.mjs`
- Dashboard control-plane loader: `/Users/jeremy/dev/OpenSIN-backend/dashboard-enterprise/components/a2a/controlPlaneRegistry.ts`
- Dashboard registry source: `/Users/jeremy/dev/OpenSIN-backend/dashboard-enterprise/components/a2a/registry.ts`
- Control-plane projection generator: `/Users/jeremy/dev/OpenSIN-backend/scripts/alpha/generate-control-plane-registry-projection.mjs`
- Control-plane projection artifact: `/Users/jeremy/dev/OpenSIN-backend/Docs/operations/a2a-control-plane-projection.json`
- Dedicated-doc sync: `/Users/jeremy/dev/OpenSIN-backend/scripts/sync-a2a-google-doc.mjs`
- HF VM runtime SSOT bundle: `/Users/jeremy/dev/OpenSIN-backend/a2a/team-infratructur/A2A-SIN-Server/hf-docs/`
- **A2A Protocol SSOT:** `https://docs.google.com/document/d/1RtoHn4I0GntuEEOHHkqoh_dMuGzgMwQz7_8oxAOpQbw/edit?tab=t.g960r14v6jet`
- **HF VM Consumer SSOT:** `https://docs.google.com/document/d/1RtoHn4I0GntuEEOHHkqoh_dMuGzgMwQz7_8oxAOpQbw/edit?tab=t.koo06y5ox1e5`
- Inbound work architecture SSOT: `/Users/jeremy/.config/opencode/INBOUND_WORK_ARCHITECTURE.md`
- Repo governance schema: `/Users/jeremy/.config/opencode/templates/repo-governance.schema.json`
- Platform registry schema: `/Users/jeremy/.config/opencode/templates/platform-registry.schema.json`
- PR watcher schema: `/Users/jeremy/.config/opencode/templates/pr-watcher.schema.json`
- Work item schema: `/Users/jeremy/.config/opencode/templates/work-item.schema.json`

Read `/Users/jeremy/.config/opencode/skills/create-a2a/references/checklist.md` before creating or normalizing an agent.

## HF VM rollout gate (March 24, 2026)

Before creating, upgrading, or declaring any HF-hosted agent ready, read these repo-local artifacts first:
- `/Users/jeremy/dev/OpenSIN-backend/a2a/team-infratructur/A2A-SIN-Server/hf-docs/hf-coder-fleet-ssot.json`
- `/Users/jeremy/dev/OpenSIN-backend/a2a/team-infratructur/A2A-SIN-Server/hf-docs/hf-coder-fleet-playbook.json`

## Dashboard page + projection gate (March 31, 2026)

The previous incomplete agent rollouts proved that repo scaffolding alone is not enough. A new agent is incomplete until the dashboard/detail-page surfaces are fail-closed.

Mandatory rules:
- the repo-local scaffold script now also generates `dashboard-enterprise/app/agents/<slug>/page.tsx` via `scripts/scaffold-a2a-agent-page.mjs`
- published `/agents/<slug>` URLs are forbidden unless the static page file exists
- `scripts/validate-sin-a2a-fleet.mjs` now fails if a published canonical `/agents/<slug>` route has no page file
- after every new agent or normalized agent, regenerate the control-plane projection before declaring success
- if the agent is meant to be publicly linked from Apps/Workforce/Marketplace, verify that the route file, registry source, and control-plane projection all agree on the same slug

Mandatory behavior:
- treat `RUNNING` as insufficient by itself; claim-safe requires explicit Room-13 worker proof
- never mark a worker live if the HF runtime is still `BUILD_ERROR`
- treat `a2a-verify-hf-vm-readiness.mjs` as a live-surface verifier: `--health-url` is required and `/health`, `/.well-known/agent-card.json`, and `/a2a/v1` must answer before the agent is considered ready
- preserve the ownership split where `AZA-SIN-Coder-•-GitHub-Issues` owns triage/lifecycle comments and `AZA-SIN-Coder-e-Global-HermesBote` owns dispatch-state comments
- if a new HF agent changes the claim-safe inventory, update the SIN-Server `hf-docs/` bundle in the same workstream
- if the HF worker talks to a bearer-protected Room-13, its runtime must support both `ROOM13_COORDINATOR_URL` and `ROOM13_BEARER_TOKEN` end-to-end instead of shipping an unauthenticated worker client


## 🕸️ LangGraph.js Ecosystem Standard (April 2026)

All newly created or migrated A2A agents MUST utilize the LangGraph.js framework for stateful, multi-agent orchestration.
- **Base Architecture:** Replace legacy conversational loops with `@langchain/langgraph` StateGraph.
- **Nodes & Edges:** Define discrete nodes for reasoning, tool execution (`ToolNode`), and API interaction.
- **State Management:** Use typed state channels (Messages, Context, Artifacts) strictly passed between nodes.
- **Tools Binding:** Bind OpenCode/MCP tools natively via `bindTools()` to the core LLM before passing into the graph.
- **Streaming:** All fastify/express endpoints (`/a2a/v1/invoke`, `/a2a/v1/stream`) must handle `.streamEvents()` from the compiled graph.

When creating an agent, ensure `package.json` includes:
- `@langchain/langgraph`
- `@langchain/core`
- `@langchain/openai`

## 🚀 sinInChrome Integration (Browser Automation — April 2026)

**EVERY new A2A agent MUST be scaffolded with optional sinInChrome browser automation capability.**

### What is sinInChrome?
sinInChrome is the OpenSIN browser automation system providing deep Chrome/Chromium integration for AI agents:
- **13 Browser Actions**: navigate, click, type, screenshot, read_page, find, form_input, resize_window, javascript_tool, read_console_messages, read_network_requests, tabs_context, tabs_create
- **Multi-Browser Support**: Chrome, Brave, Arc, Chromium, Edge, Vivaldi, Opera
- **API Gateway**: Free users get rate-limited API access (100 req/hour), premium users get direct WebSocket + MCP access
- **Health Monitoring**: 3-check system (socket, MCP server, browser extension)
- **Telemetry**: Buffered analytics with async flush

### Integration Requirements
Every new agent MUST include:
1. **MCP Configuration**: Add `sin-in-chrome` to `mcp-config.json` if browser automation is needed
2. **API Client**: Scaffold `src/clients/sin-in-chrome.ts` for API-based browser access
3. **Permission Model**: Define browser permission requirements in `agent.json`
4. **Documentation**: Include sinInChrome usage in `docs/02_spec/PRODUCT_SPEC.md`

### Agent Spec Fields for sinInChrome
```json
{
  "capabilities": {
    "browserAutomation": {
      "enabled": true,
      "mode": "api" | "mcp" | "direct",
      "browsers": ["chrome", "brave", "arc"],
      "maxTabs": 200,
      "rateLimit": {
        "free": 100,
        "premium": 10000
      }
    }
  }
}
```

## 🖥️ sin-computer-use Integration (macOS GUI Automation — April 2026)

**EVERY new A2A agent targeting macOS MUST be scaffolded with optional sin-computer-use capability.**

### What is sin-computer-use?
sin-computer-use is the OpenSIN macOS GUI automation system providing full desktop control:
- **Screen Capture**: Full macOS screen capture via SCContentFilter
- **Mouse Control**: System-wide mouse input with ease-out-cubic animation at 60fps
- **Keyboard Input**: System-wide keyboard input
- **App Management**: Open, close, hide, enumerate applications
- **Clipboard Operations**: Read/write with round-trip verification
- **ESC Abort**: System-wide escape key abort via CGEventTap
- **Multi-Display**: Full multi-display support
- **Pixel Validation**: Validate actions against screen state

### Integration Requirements
Every new macOS agent MUST include:
1. **MCP Configuration**: Add `sin-computer-use` to `mcp-config.json` if GUI automation is needed
2. **Permission Requirements**: Document macOS Accessibility + Screen Recording permissions
3. **Native Bindings**: Include `@opensin/sin-computer-use-swift` and `@opensin/sin-computer-use-input` dependencies
4. **CFRunLoop Pump**: Include `drainRunLoop` wrapper for native calls under libuv

### Agent Spec Fields for sin-computer-use
```json
{
  "capabilities": {
    "computerUse": {
      "enabled": true,
      "platform": "darwin",
      "permissions": ["accessibility", "screen-recording"],
      "coordinateMode": "pixels" | "normalized",
      "features": {
        "mouseAnimation": true,
        "clipboardGuard": true,
        "escAbort": true,
        "pixelValidation": false
      }
    }
  }
}
```

## 🔒 Security Hardening Requirements (April 2026)

**EVERY new A2A agent MUST implement the 7-layer security hardening standard.**

### Mandatory Security Artifacts
Every new agent repo MUST include:
1. **Pre-commit Hook**: `.githooks/pre-commit` with secret detection and external code scanning
2. **Pre-push Hook**: `.githooks/pre-push` with commit message leak detection
3. **Extended .gitignore**: 50+ patterns for sensitive files, external source code, and browser profiles
4. **Source Code Classification**: `governance/source-code-classification.md` defining PUBLIC/PRIVATE/SECRET/LEAKABLE levels
5. **CI Security Workflow**: `.github/workflows/leak-prevention.yml` with secret scanning, external code detection, and sensitive pattern scanning
6. **Incident Response Playbook**: `governance/incident-response-playbook.md` with step-by-step leak response procedures
7. **Secrets Baseline**: `.secrets.baseline` for detect-secrets integration

### Security Validation
Before calling an agent complete, verify:
- `grep -r "claude\|anthropic\|@ant/" --include="*.ts" --include="*.py" .` returns 0 results
- `detect-secrets scan --baseline .secrets.baseline` passes
- Pre-commit hook is executable and configured
- CI workflow includes all security checks



## 🧠 Ultra-Heavy Knowledge & Dual-Supabase OCI Logging (March 23, 2026 Mandate)

**1. No Blind Agents (The Dual-Supabase Protocol):**
Every A2A agent MUST natively implement two distinct database connections to the 200GB OCI Supabase instance.
- **Shared Fleet DB (`sin_global_memory`):** Every assumption, tool call, error, and `Fleet Correction Event` MUST be logged here. When an agent solves a bug, it pushes the fix to the global vector store so no other agent repeats the mistake.
- **Dedicated Agent DB (`a2a_[agent_name]`):** Every agent MUST have its own isolated database or schema on the OCI VM for state, checkpoints, and private vector memory.

**2. Dedicated n8n Connector Sync:**
Agents MUST NOT rely on ad-hoc web searches for their primary connectors.
- Every new A2A agent dedicated to a specific connector MUST include an `n8n-workflows/` directory containing an n8n project.
- The `n8n-workflows/docs-sync.json` MUST be scaffolded by this skill.
- The workflow's job is to autonomously scrape and vectorize the official public documentation of the connector and push the embeddings directly into the agent's **Dedicated Supabase DB**. The agent reads exclusively from this private DB to operate the connector perfectly without hallucinations.


**1. No Blind Agents (The Sentinel Protocol):**
Every A2A agent MUST natively implement comprehensive telemetry to the 200GB OCI Supabase instance.
- **Log Everything:** Every assumption, tool call, error, and goal target MUST be logged.
- **Vector Knowledge:** If an agent encounters a bug, it must query `fleet_knowledge_vectors` for past fleet fixes. When it solves a new bug, it MUST write a `Fleet Correction Event` to Supabase.
- **Zero-Trust Memory:** An agent is only as good as its logs.

**2. Dedicated n8n Connector Sync:**
Agents MUST NOT rely on ad-hoc web searches for their primary connectors.
- Every new A2A agent dedicated to a specific connector MUST include an `n8n-workflows/` directory.
- The `n8n-workflows/docs-sync.json` MUST be scaffolded by this skill.
- The workflow's job is to autonomously scrape and vectorize the official public documentation of the connector and keep the agent's `knowledge.md` and Supabase vector store 100% up-to-date.

## 🤖 Built-in micro-scripts

Use the skill's helper scripts to reduce hidden setup drift and make agent creation deterministic:

- `scripts/a2a-audit-deps.mjs` - detect hidden dependency drift and missing install contracts
- `scripts/a2a-complete-install.mjs` - plan/apply reproducible dependency installation
- `scripts/a2a-sync-runtime-assets.mjs` - create/sync baseline runtime assets like `.env.example`, runbooks, and `complete-install.sh`
- `scripts/a2a-scaffold-launchagent.mjs` - scaffold LaunchAgent plist + start/restart/health assets
- `scripts/a2a-verify-daemon-readiness.mjs` - verify local daemon readiness
- `scripts/a2a-verify-hf-vm-readiness.mjs` - verify HF VM / deployable readiness
- `scripts/a2a-preflight.mjs` - orchestrate the checks in one command

## 🚀 The Infinite Scaling Architecture & Autonomous Monetization

As the CEO of this silicon workforce, you must ensure that our 100+ A2A agents never sleep due to API rate limits, are ready for the SIN Solver Web Marketplace, and proactively generate value:

1. **The Producer (Mac-Rotator):** The Mac runs `opencodex-auth-rotator` endlessly, using Temp-Mail Premium to generate fresh OpenAI tokens, and pushes them straight into the `sin-supabase` table (`openai_tokens`) with status `is_active=true`.
2. **The Consumers (HF VMs & OCI):** HF VMs and other runtimes are pure consumers. They **DO NOT** run Chrome or temp-mail scripts.
3. **The Pull Script:** Every agent must execute `hf_pull_script.py` before invoking LLMs. When an agent hits a rate limit, the script pulls a fresh token from Supabase in 0.2 seconds and overwrites the local `auth.json`.
4. **The OpenCode CLI Standard (CRITICAL):** EVERY general A2A agent MUST be equipped with the `opencode` CLI as its brain. You MUST use the model `opencode/qwen3.6-plus-free` and explicitly append `--fallback opencode/nemotron-3-super-free`. Only specialized agents (e.g., Voice, multimodal-looker) may deviate from this.
5. **The Marketplace Mandate:** EVERY agent MUST include a `marketplace` metadata object in `agent.json` and `metadata.ts` (pricingModel, monthlyPrice, purchaseModes, category) to be monetizable on the future SIN Solver storefront.
6. **The Native CLI Mandate:** EVERY agent MUST possess a Native CLI entrypoint (e.g., `src/cli.ts` -> `sin-<name>`).
7. **The Hacker/Bypass Mentality:** Agents MUST be built to find their way into any system. Build them to use `webauto-nodriver-mcp` (or libraries like `Scrapling` for TLS spoofing and Canvas noise) to autonomously bypass Cloudflare, Turnstile, and Captchas (via GateSolve/x402). They must be independent, unstoppable problem solvers.
8. **The "Never Idle" Monetization Rule:** Coder A2As and general agents MUST be programmed with idle-loop behaviors:
   - **Bug Bounties:** They autonomously scan open-source repos, hunt on HackerOne/Bugcrowd, and submit exploits/fixes.
   - **Freelancing:** They autonomously register on Upwork, AgentWork, ClawGig, or Freelancer.com, apply for Dev/Moderation jobs, and execute them end-to-end.
   - **Surveys:** They complete paid surveys on pre-approved platforms.
   - **Local Tasks:** They safely OCR, scan, and index local data (WITHOUT deleting or destructively moving user files).

**Your mandate:** Every A2A agent MUST be scaffolded to utilize this V2 architecture pattern, deeply integrating autonomous hacker mentalities and monetization loops.

## 🚨 Hard rules

- **CRITICAL AUTH SCHEMA RULE:** When generating or updating `hf_pull_script.py` (or any auth script), you MUST format the OpenCode `auth.json` strictly as follows. Using `"token"` instead of `"refresh"` will crash OpenCode with `TypeError: undefined is not an object (evaluating 'currentAuth.type')`!
  ```json
  {
    "openai": {
      "type": "oauth",
      "refresh": "<refresh_token_from_supabase_here>"
    }
  }
  ```


- Always scaffold from the template. Never hand-roll a new SIN agent root.
- Every new agent must get its own GitHub repo.
- GitHub bot rule: every new Team-Coding / SIN-Coder agent MUST also get a dedicated GitHub App bot lane from day zero. Non-coding A2A agents may opt in via `githubBot.enabled=true`; default for non-coding agents is no dedicated GitHub bot unless the user requests one.
- Every new agent repo that can receive inbound work or open PRs MUST ship inbound-intake governance and a PR watcher contract from day zero.
- **The Intelligence Core:** You must wire the agent's `runtime.ts` to call `opencode run "..." --model opencode/qwen3.6-plus-free --fallback opencode/nemotron-3-super-free`. Do not hardcode direct `fetch` or SDK calls to OpenAI/Gemini APIs unless absolutely necessary for streaming or specialized multimodal tasks.
- **Telegram Ownership Rule:** EVERY A2A agent must keep its own dedicated Telegram bot for direct messaging, operator contact, and domain-specific notifications. Do not route normal agent messaging through `A2A-SIN-TelegramBot`.
- **TelegramBot Scope Rule:** `A2A-SIN-TelegramBot` is reserved for Watcher, Router, and Incident Monitor duties only. It detects failures and triggers the `n8n -> SIN-GitHub-Issues -> Hermes` self-healing loop instead of acting as the fleet's shared conversation bot.
- **HF VM Rule:** Never install local Chrome or full Rotator pipelines on HF VMs. You MUST run the automation script `setup_consumer_auth.sh` (see step 7) to inject `hf_pull_script.py` automatically.
- **Alpha Backbone & Marketplace:** Every new agent must declare control-plane metadata, native CLI commands, and a full `marketplace` object in `agent.json`.
- **Dependency Contract Rule:** No hidden dependencies. Every A2A repo must list all required CLIs, browser/runtime extras, and sidecars.
- Every new agent must have:
  - `A2A-CARD.md`
  - `agent.json`
  - `governance/repo-governance.json`
  - `governance/pr-watcher.json`
  - `governance/source-code-classification.md` (NEW — April 2026)
  - `governance/incident-response-playbook.md` (NEW — April 2026)
  - `platforms/registry.json`
  - `n8n-workflows/inbound-intake.json`
  - `docs/03_ops/inbound-intake.md`
  - `scripts/watch-pr-feedback.sh`
  - `src/runtime.ts` (with `opencode` CLI logic)
  - `src/mcp-server.ts`
  - `src/a2a-http.ts`
  - `src/metadata.ts` (with `marketplace` object)
  - `src/cli.ts` (Native CLI)
  - `scripts/complete-install.sh`
  - `scripts/hf_pull_script.py`
  - `.githooks/pre-commit` (NEW — April 2026)
  - `.githooks/pre-push` (NEW — April 2026)
  - `.secrets.baseline` (NEW — April 2026)
  - `src/clients/sin-in-chrome.ts` (optional — browser automation)
  - `src/clients/sin-computer-use.ts` (optional — macOS GUI automation)
  - `.githooks/pre-commit` (NEW — April 2026)
  - `.githooks/pre-push` (NEW — April 2026)
  - `.secrets.baseline` (NEW — April 2026)
  - `src/clients/sin-in-chrome.ts` (optional — browser automation)
  - `src/clients/sin-computer-use.ts` (optional — macOS GUI automation)

## 🛠️ Creation workflow

1. Determine the canonical team and team manager.
2. Research the best-fit NVIDIA NIM model and record it in the spec.
3. Copy `agent-spec.example.json` and fill all required fields.
   - For Team-Coding agents: `githubBot.enabled` MUST be `true` and the spec must include `appSlug`, `botName`, `appIdEnv`, `clientIdEnv`, `privateKeyEnv`, and `webhookSecretEnv`.
   - For non-coding agents: `githubBot` is optional. If omitted or `enabled=false`, no dedicated GitHub bot routing example is generated.
4. Run:

```bash
node /Users/jeremy/dev/OpenSIN-backend/scripts/create-sin-a2a-agent.mjs --spec /abs/path/to/spec.json
```

4b. If you are repairing an older agent or the route file was missing, run the page scaffold explicitly:

```bash
node /Users/jeremy/dev/OpenSIN-backend/scripts/scaffold-a2a-agent-page.mjs --slug sin-<agentname>
```

5. Verify the generator created or reused the private GitHub repo from `repoUrl`.
6. Run dependency/asset preflight early:

```bash
node /Users/jeremy/.config/opencode/skills/create-a2a/scripts/a2a-audit-deps.mjs --agent-root /abs/path/to/new-agent-root --format text
node /Users/jeremy/.config/opencode/skills/create-a2a/scripts/a2a-sync-runtime-assets.mjs --agent-root /abs/path/to/new-agent-root --mode apply --format text
```

7. Implement the real runtime surface (Domain actions in `runtime.ts`).
7b. **MCP Surface Generation (AUTOMATED):** Invoke skill `/create-a2a-mcp` to scaffold the MCP server surface. This generates `src/mcp-server.ts`, `mcp-config.json`, `clients/opencode-mcp.json`, and patches `src/cli.ts`. Run:
```bash
MCP_SCRIPTS=~/.config/opencode/skills/create-a2a-mcp/scripts
node $MCP_SCRIPTS/mcp-scaffold.mjs --agent-root /abs/path/to/new-agent-root --slug sin-<agentname> --tools '<domain-specific-tools-json>'
node $MCP_SCRIPTS/mcp-register-global.mjs --slug sin-<agentname> --agent-root /abs/path/to/new-agent-root --bin-wrapper
node $MCP_SCRIPTS/mcp-verify.mjs --agent-root /abs/path/to/new-agent-root --slug sin-<agentname>
```
8. **Consumer Setup (AUTOMATED):** Inject the Infinite Scaling script into the new agent by running the skill's built-in macro:
```bash
/Users/jeremy/.config/opencode/skills/create-a2a/scripts/setup_consumer_auth.sh /abs/path/to/new-agent-root
```
9. Add the deployment/install bundle:
  - `scripts/complete-install.sh`
  - `scripts/hf_pull_script.py`
  - complete dependency manifests + lockfiles
  - explicit system dependency list and env contract
  - daemon LaunchAgent bundle when applicable
10. Regenerate the projection-first registry artifacts:

```bash
cd /Users/jeremy/dev/OpenSIN-backend && npm run sync:a2a:control-plane-projection
```

11. Add the agent to the dashboard registry and team registry.
12. Bootstrap inbound-work governance and review automation:
  - validate `governance/repo-governance.json`
  - validate `governance/pr-watcher.json`
  - populate `platforms/registry.json`
  - keep `n8n-workflows/inbound-intake.json` aligned to the shared work-item schema
  - verify `scripts/watch-pr-feedback.sh` starts a repo watcher contract cleanly
13. Add or update the public agent page on `a2a.delqhi.com`.
    - The static route file under `dashboard-enterprise/app/agents/<slug>/page.tsx` must exist before you publish or link the agent.
14. Sync the dedicated Google Doc from `A2A-CARD.md` (legacy shared-doc tabs are fallback-only during migration).
15. Run the required validations.

## 🛡️ Required validations

Run all of these before calling the agent complete:

```bash
npm --prefix /abs/path/to/agent-root run build
node /abs/path/to/agent-root/dist/src/cli.js run-action '{"action":"agent.help"}'
node /abs/path/to/agent-root/dist/src/cli.js print-card
node /Users/jeremy/dev/OpenSIN-backend/scripts/scaffold-a2a-agent-page.mjs --slug sin-<agentname> --dry-run true
cd /Users/jeremy/dev/OpenSIN-backend && npm run test:a2a:fleet
cd /Users/jeremy/dev/OpenSIN-backend && npm run sync:a2a:control-plane-projection
node /Users/jeremy/.config/opencode/skills/create-a2a/scripts/a2a-verify-hf-vm-readiness.mjs --agent-root /abs/path/to/agent-root --health-url https://<public-host>/health --format text
```

The fleet validator now explicitly blocks these incomplete states:
- published canonical `/agents/<slug>` URL without `dashboard-enterprise/app/agents/<slug>/page.tsx`
- singular `/agent/<slug>` drift on canonical hosts
- missing repo-local route page scaffold after agent creation

Recommended front-door verifier:

```bash
node /Users/jeremy/.config/opencode/skills/create-a2a/scripts/a2a-preflight.mjs --agent-root /abs/path/to/agent-root --targets deps,install,assets,daemon,hf --format text
```

For every HF VM / deployable repo also run:

```bash
bash /abs/path/to/agent-root/scripts/complete-install.sh
```

And verify all of these before calling it complete:
- a fresh clone can be installed from the repo with no hidden manual steps
- all dependency manifests and lockfiles exist and are actually used by the install path
- required system packages / CLIs / browser/runtime tools are declared, not assumed
- env requirements are documented via `.env.example` or equivalent contract
- at least one smoke check proves the installed agent starts and answers health/help successfully
- for HF-hosted agents, the smoke checks must include `a2a-verify-hf-vm-readiness.mjs --health-url <public>/health` and fail closed unless the public surfaces answer

## 🔄 Upgrade workflow for existing agents

Use the same checklist when normalizing older agents. Specifically check:
- **Missing Producer-Consumer Integration:** Ensure existing HF VM agents are stripped of local Chrome/Rotator setups and retrofitted with `hf_pull_script.py` by running the automation macro (`setup_consumer_auth.sh`).
- **Missing complete-install path:** Older repos that only have README setup notes or partial scripts must be upgraded to a real `scripts/complete-install.sh` plus explicit dependency manifests.

## 🧰 Complete-install standards

Apply this to every HF VM / deployable A2A repo.

- `scripts/complete-install.sh` is the single supported full install/configure entrypoint.
- The script must be idempotent and safe to rerun.
- Use tracked manifests/lockfiles only (`package-lock.json`, `bun.lock`, `requirements.txt`, `poetry.lock`, etc.).
- Explicitly install/validate required system packages and CLIs instead of assuming they already exist.
- Create required directories (`logs`, `data`, caches, state dirs) inside the agent-owned layout.
- Validate secrets/env contract and fail fast with clear messages.
- Run a post-install smoke check automatically.
- Document platform differences (macOS vs HF VM/Linux) when they differ.

## 🚫 Complete-install anti-patterns

- README-only install steps with no executable complete-install path
- missing lockfiles or drifting manifests
- hidden global packages or manually preinstalled CLIs
- runtime browser/OCR/media tools used in code but not declared anywhere
- scripts that mutate state before verifying prerequisites

## 🔄 Fleet Sync (`sin-sync`)

Every A2A agent depends on an identical OpenCode CLI environment across Mac, OCI VM, and HF VMs. The `sin-sync` tool ensures this.

### What it syncs
- `~/.config/opencode/` — skills, MCPs, plugins, tools, agents, opencode.json
- Direction: **Mac → OCI VM → HF VMs** (Mac is Source of Truth)

### What it NEVER syncs (strict exclusions)
- `auth.json`, `token.json`, `antigravity-accounts.json`, `telegram_config.json`
- `*.db`, `*.sqlite*`, `logs/`, `tmp/`, `.cache/`

### Usage
```bash
# Sync from Mac to OCI VM (run on Mac)
sin-sync

# Underlying script
~/.local/bin/sync-opencode.sh
```

### Integration into agent creation workflow
After creating or updating any skill, MCP config, or agent definition in `~/.config/opencode/`:
1. Test locally on Mac
2. Run `sin-sync` to push to OCI VM
3. OCI VM distributes to HF VMs via the agent's `complete-install.sh` or CI pipeline

### When to run sin-sync
- After adding/updating skills in `~/.config/opencode/skills/`
- After modifying `~/.config/opencode/opencode.json` (new MCPs, models, agents)
- After updating `~/.config/opencode/AGENTS.md` governance rules
- Before deploying any new A2A agent to OCI or HF VMs
- **MANDATORY** after every `create-a2a` session that touches global config

### Auth files are VM-local
Each VM maintains its own auth files. HF VMs use `hf_pull_script.py` to pull tokens from Supabase. The OCI VM has its own credentials. The Mac has its own rotator-produced auth. These are NEVER mixed.

## 🏁 Output standard

When the task is finished, report:
- created or updated agent root
- GitHub repo URL
- Infinite Scaling Auth status (Consumer automation macro applied)
- validator results


## Claude Code Auto Mode lessons (April 2026)

When creating or upgrading an agent, assume autonomous execution can exist, but only under strict control:
- auto mode is acceptable only with bounded retries, self-verification, and explicit approval gates for risky actions
- new agents should expose capability contracts and risk tiers instead of vague tool powers
- prefer isolated branches/worktrees for non-trivial code mutation paths
- require replayable evidence, checkpoints, and clear rollback notes
- if an agent cannot verify its own work, it is not ready for autonomous mode

## 🏆 OpenSIN vs Claude Code — Competitive Superiority (April 2026)

OpenSIN-AI is now **100% feature-equivalent + superior** to Claude Code in all categories:

| Feature | Claude Code | OpenSIN-AI | Status |
|---------|-------------|------------|--------|
| Browser Automation | ✅ claudeInChrome | ✅ **sinInChrome** (13 actions, 7 browsers) | ✅ EQUAL + BETTER |
| macOS GUI Automation | ✅ computerUse | ✅ **sin-computer-use** (14 files, 652 lines) | ✅ EQUAL |
| API Gateway | ❌ | ✅ REST API for free users | ✅ BETTER |
| Health Monitoring | ❌ | ✅ 3-check system | ✅ BETTER |
| Telemetry | ❌ | ✅ Buffered analytics | ✅ BETTER |
| Auto-Reconnect | ❌ | ✅ 3 attempts with backoff | ✅ BETTER |
| Batch Operations | ❌ | ✅ Up to 50 actions | ✅ BETTER |
| Rate Limiting | ❌ | ✅ 100/h free, 10k/h premium | ✅ BETTER |
| Security Hardening | Basic | ✅ 7-layer protection | ✅ BETTER |
| Leak Prevention CI | ❌ | ✅ GitHub Actions | ✅ BETTER |

**Creation Mandate:** Every new agent MUST be built with awareness that OpenSIN-AI now exceeds Claude Code capabilities. Never position OpenSIN as "alternative to" — position it as "superior to".

## Google account matrix

- New agents that touch Google Docs/Drive must follow `~/.config/opencode/google-account-matrix.json` and `~/.config/opencode/GOOGLE-ACCOUNTS.md`.
- Existing Docs in My Drive -> `zukunftsorientierte.energie@gmail.com` via `oauth_user`.
- Admin/Workspace tasks -> `info@zukunftsorientierte-energie.de` via `oauth_user`.
- Service account `ki-agent@artificial-biometrics.iam.gserviceaccount.com` only for explicitly shared or service-account-owned files/folders.
- For new enterprise docs, prefer offline `.docx` generation via `sin-document-forge` into `/Users/jeremy/Google Drive/Geteilte Ablagen/OpenSolver-Repo in Organisation verschieben`.

- Google Docs access must use the Google account matrix plus the `sin-google-docs` commands `ensure-access`, `ensure-patent-structure`, and `replace-patent-tabs` when relevant.

### 🚨 GLOBAL SSOT DAEMON MANDATE (MANDATORY FOR ALL NEW A2A AGENTS)
Every new A2A Agent (especially those deployed to HF VMs or OCI VMs) MUST include the `ssot-daemon.sh` in its background lifecycle (`start.sh`, `server.js`, or Dockerfile). 
- **The Rule**: The agent MUST clone `git@github.com:OpenSIN-AI/OpenSIN-Code.git` (or https if no SSH key) on startup.
- **The Daemon**: It must run the loop that fetches changes every 60 seconds and forcefully updates `~/.config/opencode/` and the local `.opencode/` directory on the VM.
- **Why**: This ensures 100% global consistency across all VMs (HF, OCI) and Macs instantly whenever the `OpenSIN-AI/OpenSIN-Code` fork is updated. No exceptions.

### 🚨 MULTI-HF-ACCOUNT STRATEGY (MANDATORY FOR SCALING)
When deploying many A2A agents to HuggingFace Spaces, a single HF account hits rate limits (20 spaces/day) and capacity limits.
- **Strategy**: OpenSIN manages multiple HF accounts and distributes agents across them automatically.
- **Account Pool**: Each HF account is registered in sin-passwordmanager and sin-server.
- **Distribution**: Agents are assigned round-robin or team-based across available accounts.
- **Rate Limit Handling**: When an account hits the 20/day limit, the next account is used automatically.
- **User Prompt**: If all accounts are exhausted, the user is prompted to add another HF account.
- **Template**: Every agent's `agent.json` must declare which HF account owns its space via `deployment.hfAccount`.

### 🚨 SIN-SERVER AUTO-HEALING MANDATE (MANDATORY FOR ALL VMS)
sin-server is the central auto-healing orchestrator for all HF VMs and OCI VMs.
- **Health Checks**: sin-server polls all agent `/health` endpoints every 60 seconds.
- **Auto-Fix**: When an agent fails, sin-server triggers `complete-install.sh` + `hf_pull_script.py` automatically.
- **Build Recovery**: If a HF Space is in BUILD_ERROR, sin-server re-triggers the build via HF API.
- **Space Recovery**: If a Space is missing, sin-server creates it via the multi-account pool.
- **Token Recovery**: If auth expires, sin-server refreshes via sin-authenticator.
- **Alerting**: sin-server alerts via A2A-SIN-TelegramBot when auto-healing fails.
- **Agent Contract**: Every agent MUST expose `/health`, `/.well-known/agent-card.json`, and `/a2a/v1` endpoints.

### 🚨 TEMPLATE RUNTIME REQUIREMENTS (MANDATORY FOR ALL NEW AGENTS)
The template `runtime.ts` MUST include:
1. **opencode CLI call** with `--model opencode/qwen3.6-plus-free --fallback opencode/nemotron-3-super-free`
2. **Domain actions**: health, session.status, research, draft, revoke (minimum)
3. **Platform integration**: agent-specific actions wired to opencode CLI calls
4. **No direct API calls**: All LLM calls MUST go through opencode CLI
5. **Confirmation gates**: All write actions require `confirm: true`

### 🚨 TEMPLATE AGENT.JSON REQUIREMENTS (MANDATORY)
Every agent.json MUST include:
1. `marketplace` object with `pricingModel`, `monthlyPrice`, `purchaseModes`, `category`
2. `primaryModel` set to `opencode/qwen3.6-plus-free`
3. `controlPlane` object with all required fields
4. `deployment` object with `workforceIndex`, `landingPage`, `publicA2A`, `cimdAnchor`, `vmServer`

### 🚨 TEMPLATE DOCKERFILE REQUIREMENTS (MANDATORY)
Every Dockerfile MUST:
1. Use multi-stage build (builder + runner)
2. Install Python for bootstrap scripts
3. Run `hf_pull_script.py` before starting the agent
4. Expose port 8000
5. Use `node:22-slim` as base image
