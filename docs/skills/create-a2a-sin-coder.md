---
name: create-a2a-sin-coder
description: Master-level enterprise workflow to bootstrap an elite A2A Coder Agent (e.g., A2A-SIN-Frontend, A2A-SIN-Backend). This skill triggers an n8n workflow that sets up a new GitHub repository and populates it with 5-10 specialized, billion-dollar tier architecture GitHub Issues. SIN-Hermes and SIN-GitHub-Issues then dispatch these issues to the entire A2A Coding Team so they can collaborate on an enterprise masterpiece.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/create-a2a-sin-coder`

# 👑 The A2A Elite Coder Factory (CEO Level)

Use this skill when you need to create a **NEW, specialized A2A Coder Agent** (e.g., `A2A-SIN-Coder-Backend`, `A2A-SIN-Code-Frontend`).

## 🚨 The Alpha Paradigm

A new Coder Agent is **NOT** a simple script kiddie. They are the **best of the best**, possessing the collective knowledge of 10 million developers. They operate with CEO-level domain mastery and build frontends/backends that rival multi-billion dollar Alpha projects like Google Workspace.

Because building a masterpiece requires a team of experts, **ONE agent does not build a whole new Coder Agent alone.**

Instead, this skill uses an **n8n automated workflow** to:
1. Create the base GitHub repository.
1b. Provision a dedicated GitHub App bot contract for that coder agent. A coder agent is not complete without its own GitHub App persona / routing lane.
2. Generate a suite of 5-10 specialized, expert-level GitHub Issues (e.g., "Implement High-Performance Event Loop", "Scaffold Enterprise MCP Runtime", "Setup Infinite Scaling Authentication").
3. Push these issues to the `sin_issues_pool` (Supabase).
4. `SIN-Hermes` and `SIN-GitHub-Issues` automatically assign these issues across the existing **A2A Team Code** (Frontend, Backend, Tester, Architect).
5. The team works in parallel, fully aware of each other, to finish the masterpiece.

## Mandatory inbound-work + PR-watcher contract

Every coder repo created by this factory MUST ship the following from day zero:
- `governance/repo-governance.json`
- `governance/pr-watcher.json`
- `governance/coder-dispatch-matrix.json`
- `platforms/registry.json`
- `n8n-workflows/inbound-intake.json`
- `docs/03_ops/inbound-intake.md`
- `scripts/watch-pr-feedback.sh`
- `config/github-app-routing.example.json`

Coder-factory issues MUST explicitly include:
1. n8n intake bootstrap for inbound work platforms
2. GitHub issue-first normalization against the shared work-item schema
3. PR watcher bootstrap so existing PR feedback automation can attach immediately once the first PR exists

## 🛠️ Execution Workflow

1. **Define the Coder Profile:** Determine the exact specialty of the new Coder (e.g., `A2A-SIN-Code-Frontend`).
2. **Deploy the Workflow to n8n:** Run the included script to deploy the `Coder-Factory` workflow to the OCI VM n8n instance.
3. **Trigger the Factory:** Send a webhook POST request to the n8n workflow with the Coder Profile JSON.
4. **Watch the Delegation:** Once the GitHub repo and issues are created, the `sin_issues_pool` fills up, and `SIN-Hermes` takes over dispatching.

## Mandatory GitHub App bot lane for coder agents

Every new coder agent MUST be scaffolded with dedicated GitHub App bot metadata so it can appear and respond as its own GitHub bot persona.

Minimum required spec fields for coder creation:
- `githubBot.enabled=true`
- `githubBot.appSlug`
- `githubBot.botName`
- `githubBot.appIdEnv`
- `githubBot.clientIdEnv`
- `githubBot.privateKeyEnv`
- `githubBot.webhookSecretEnv`

The generated coder repo must include `config/github-app-routing.example.json` wired to that bot lane.

## HF coder fleet readiness gate (March 24, 2026)

Before you let the factory assume an HF coder can receive live work, read:
- `/Users/jeremy/dev/SIN-Solver/a2a/team-infratructur/A2A-SIN-Server/hf-docs/hf-coder-fleet-ssot.json`
- `/Users/jeremy/dev/SIN-Solver/a2a/team-infratructur/A2A-SIN-Server/hf-docs/hf-coder-fleet-playbook.json`

Rules:
1. `AZA-SIN-Coder-•-GitHub-Issues` owns triage/enqueue/lifecycle issue comments.
2. `AZA-SIN-Coder-e-Global-HermesBote` owns dispatch/claim/running/completed/failed/stale-requeue comments.
3. Do not assign a ProtonMail/GitHub coder-manager identity unless it maps to exactly one runtime role and one comment surface set.
4. Do not treat local smoke proof as remote HF completion proof; at least one explicit remote claim/complete cycle still has to be evidenced before calling the fleet fully live.
5. If the worker runtime targets a bearer-protected Room-13, the coder runtime must carry `ROOM13_BEARER_TOKEN` through its HTTP worker bridge; a URL-only worker client is not deployment-ready.
6. If the coder agent is HF-hosted, `a2a-verify-hf-vm-readiness.mjs` must be run with `--health-url <public>/health`, and the public `/health`, `/.well-known/agent-card.json`, and `/a2a/v1` surfaces must answer before the repo is considered ready.

### Step 1: Deploy the n8n Coder Factory Workflow

Execute the deployment script to push the workflow to the OCI VM (`92.5.60.87`):

```bash
node ~/.config/opencode/skills/create-a2a-sin-coder/scripts/deploy-workflow.mjs
```

### Step 2: Trigger the Factory via OpenCode

```bash
node ~/.config/opencode/skills/create-a2a-sin-coder/scripts/trigger-factory.mjs --name "A2A-SIN-Code-Frontend" --domain "Frontend Mastermind"
```

## 🧠 The "Master Boss Coder" System Prompt Mandate

When defining a Coder Agent's `system_prompt` (in `agent.json` and `A2A-CARD.md`), you MUST enforce the following identity:

> **You are A2A-SIN-Code-[Specialty], an ultimate CEO-level coding mastermind.** 
> You possess the combined expert knowledge of 10 million elite developers. You do not write simple or average code; you engineer multi-billion dollar enterprise Alpha architectures that rival Google Workspace and OpenAI. You use the best world-class practices, flawless state management, infinite-scaling producer-consumer patterns, and absolute type safety. You are a cornerstone of the A2A Code Team, working in perfect synchronization with your peers (Backend, Tester, Ops) via GitHub Issues dispatched by SIN-Hermes. 
> 
> When you receive a task, you plan like an architect, execute like a machine, and verify like a senior auditor.

## 📦 Required Files to Generate in the Repository via the Team

The issues created by the n8n workflow will mandate the Team Code to generate:
- The standard V2 Infinite Scaling Architecture (`hf_pull_script.py`, `opencode` CLI integration).
- The `agent.json` and `A2A-CARD.md` with the "Master Boss Coder" mandate.
- Governance/intake artifacts (`governance/`, `platforms/`, `n8n-workflows/inbound-intake.json`, `scripts/watch-pr-feedback.sh`).
- A strict coder specialization matrix (`governance/coder-dispatch-matrix.json`) so Hermes/GitHub-Issues never delegate by arbitrary preference.
- The `src/runtime.ts` executing `opencode/qwen3.6-plus-free` + `--fallback opencode/minimax-m2.5-free`.
- A dedicated Telegram bot for domain-specific notifications (Watcher).

*Remember to run `sin-sync` after modifying anything in the `~/.config/opencode/skills/` directory.*

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

**REGELN — SOFORTIGER BAN BEI VERSTOSS:**
- `opencode run --format json` nutzt das Antigravity Plugin — identisch auf Mac, OCI VM und HF VMs
- OCI-Proxy `http://92.5.60.87:4100/v1` direkt per HTTP anrufen = VERBOTEN (liefert 500)
- Gemini API direkt (`generativelanguage.googleapis.com`) = PERMANENT VERBOTEN
- Anthropic API direkt = PERMANENT VERBOTEN
- `requests.post(...)` oder `urllib` für LLM = VERBOTEN
- **Modell:** opencode wählt automatisch `opencode/qwen3.6-plus-free` via Antigravity — kein `--model` nötig
- Ausnahmen NUR wenn User explizit ein anderes Modell nennt (z.B. `antigravity-claude-opus-4-6`, `antigravity-claude-sonnet-4-6`, `antigravity-gemini-3.1-pro`)
- **Gilt auf ALLEN Plattformen:** Mac, OCI VM, HF VM — opencode CLI ist überall identisch

## 🕸️ Hierarchical LangGraph Coder (April 2026)

Every A2A Coder MUST be built on top of a multi-agent LangGraph.js Supervisor pattern.
- **Supervisor Node:** Evaluates the overarching GitHub Issue / architectural directive.
- **Worker Nodes:** Specialized nodes mapped to phases: e.g., CodeGenerationNode, TestingNode, IntegrationNode.
- **ToolNode:** Resolves code actions via ast-grep and ripgrep natively bound.
- **Checkpoints:** A2A Coders must persist conversation history per-issue into Supabase via `BaseCheckpointSaver`.
- **Review Loop:** The graph should include an edge from TestingNode back to CodeGenerationNode if verification fails.

## 🚀 Coder Agent Browser & GUI Capabilities (April 2026)

**EVERY new Coder Agent MUST be scaffolded with full browser and GUI automation awareness.**

### sinInChrome for Coder Agents
Coder agents MUST be able to:
- Test web applications they build via sinInChrome (13 browser actions)
- Perform automated UI testing and screenshot capture
- Access browser console and network logs for debugging
- Use the API gateway for free-tier testing (100 req/hour)

### sin-computer-use for Coder Agents
macOS-based coder agents MUST be able to:
- Run and test desktop applications they build
- Perform GUI automation testing
- Capture screenshots of running applications
- Manage application lifecycle (open, close, hide)

### Security Hardening for Coder Repos
Every coder repo created by this factory MUST NOW include:
- `governance/source-code-classification.md` (PUBLIC/PRIVATE/SECRET/LEAKABLE)
- `governance/incident-response-playbook.md`
- `.githooks/pre-commit` with secret + external code detection
- `.githooks/pre-push` with commit message leak detection
- `.secrets.baseline` for detect-secrets
- `.github/workflows/leak-prevention.yml` for CI security scanning

**CRITICAL:** Zero references to external source code (claude, anthropic, @ant/) are permitted in any generated coder repo. The pre-commit hook will block any such commits.

## 🏆 OpenSIN Coder Superiority (April 2026)

OpenSIN Coder Agents now exceed Claude Code capabilities in all categories:
- **Browser Testing**: sinInChrome with 13 actions vs Claude's basic browser tool
- **GUI Testing**: sin-computer-use with native macOS bindings
- **Security**: 7-layer hardening vs Claude's basic protections
- **API Access**: Free-tier API gateway for testing without limits
- **Health Monitoring**: 3-check system for agent readiness
- **Telemetry**: Buffered analytics for performance tracking

Coder agents MUST be instructed to leverage these capabilities when building and testing applications.


## Auto Mode lessons for coder agents

Coder agents must not behave like blind OpenClaw-style plugin runners. They need:
- actor-critic or reviewer gate before commit/merge
- bounded retry loops with stop conditions
- validation command contracts
- evidence-backed completion rather than narration
- approval gates for destructive or externally risky actions

## Google account matrix

- Generated coding agents must follow the global Google identity matrix in `~/.config/opencode/google-account-matrix.json` and `~/.config/opencode/GOOGLE-ACCOUNTS.md`.
- Existing Docs/Drive edits use the Gmail OAuth user; admin flows use the Workspace admin account; service accounts are not a substitute for private Docs access.
- New generated docs should prefer `sin-document-forge` into the synced shared-drive folder.

- Google Docs access must use the Google account matrix plus the `sin-google-docs` commands `ensure-access`, `ensure-patent-structure`, and `replace-patent-tabs` when relevant.

### 🚨 GLOBAL SSOT DAEMON MANDATE (MANDATORY FOR ALL NEW CODER AGENTS)
When scaffolding or initializing a new Coder Agent environment, you MUST integrate the Global SSOT Daemon.
- **The Rule**: The Coder Agent's execution environment (HF Space or VM) MUST run the `ssot-daemon.sh` as a background process.
- **Function**: The daemon continuously pulls `git@github.com:OpenSIN-AI/OpenSIN-Code.git` and enforces identical opencode configurations (`opencode.json`, `plugins`, `skills`, `mcp`) on the local VM.
- **Why**: To guarantee that ANY change pushed to the `OpenSIN-AI/OpenSIN-Code` fork is immediately active across the entire A2A Coder Fleet worldwide within 60 seconds.
