# OpenSIN-AI Agent: Feature Comparison & Roadmap

> How OpenSIN-AI Agent compares against OpenClaw, Google Gemini Agent, and Claude Code — and our plan to surpass them all.

---

## Feature Comparison Matrix

| Feature                    | OpenSIN-AI | OpenClaw | Gemini Agent | Claude Code |
| -------------------------- | :--------: | :------: | :----------: | :---------: |
| **Core**                   |            |          |              |             |
| Open Source                |     ✅     |    ✅    |      ❌      |     ❌      |
| Self-Hosted                |     ✅     |    ✅    |      ❌      |     ❌      |
| 24/7 Autonomous            |     ✅     |    ✅    |      ❌      | ✅ (3 days) |
| Multi-Model                |     ✅     |    ✅    |      ❌      |     ❌      |
| **Intelligence**           |            |          |              |             |
| Heartbeat/Cron             |     ✅     |    ✅    | ✅ (limited) | ✅ (/loop)  |
| Persistent Memory          |     ✅     |    ✅    |      ❌      |     ✅      |
| Structured Wiki            |     ✅     |    ✅    |      ❌      |     ❌      |
| Session Branching          |     ✅     |    ✅    |      ❌      |     ❌      |
| **Communication**          |            |          |              |             |
| Telegram                   |     ✅     |    ✅    |      ❌      |     ✅      |
| WhatsApp                   |     ✅     |    ✅    |      ❌      |     ❌      |
| Discord                    |     ✅     |    ✅    |      ❌      |     ✅      |
| Signal                     |     ✅     |    ✅    |      ❌      |     ❌      |
| iMessage                   |     ✅     |    ✅    |      ❌      |     ❌      |
| Slack                      |     🔲     |    ✅    |      ❌      |     ❌      |
| MS Teams                   |     🔲     |    ❌    |      ❌      |     ❌      |
| **Automation**             |            |          |              |             |
| Subagent Spawning          |     ✅     |    ✅    |      ❌      |     ✅      |
| External Harness (ACP)     |     ✅     |    ✅    |      ❌      |     ❌      |
| Webhook Triggers           |     ✅     |    ✅    |      ❌      |     ❌      |
| Unified Agent Orchestrator |     ✅     |    ✅    |      ❌      |     ❌      |
| Browser Automation         |     ✅     |    ✅    |      ✅      |     ✅      |
| **Workspace**              |            |          |              |             |
| Google Workspace           |     ✅     |    ✅    |      ✅      |     ❌      |
| Apple Ecosystem            |     ✅     |    ❌    |      ❌      |     ❌      |
| Microsoft 365              |     🔲     |    ❌    |      ❌      |     ❌      |
| **SDK & Dev**              |            |          |              |             |
| Agent SDK                  |     ✅     |    ❌    |      ❌      |     ✅      |
| Plugin System              |     ✅     |    ✅    |      ❌      |     ❌      |
| MCP Support                |     ✅     |    ✅    |      ❌      |     ✅      |
| **Safety**                 |            |          |              |             |
| Approval Hooks             |     ✅     |    ✅    |      ❌      |     ❌      |
| Audit Logging              |     🔲     |    ✅    |      ❌      |     ❌      |
| Risk Classification        |     🔲     |    ✅    |      ❌      |     ❌      |
| **Advanced**               |            |          |              |             |
| Voice Wake                 | ✅ (Siri)  |    ✅    |      ✅      |     ❌      |
| Canvas/A2UI                |     ✅     |    ✅    |      ❌      |     ❌      |
| Computer Use               |     ✅     |    ✅    |      ✅      |     ✅      |

**Legend:** ✅ Implemented | 🔲 Planned | ❌ Not available

---

## OpenSIN-AI Unique Advantages

### 1. A2A Fleet Architecture (92+ Workers)

Unlike competitors that run as a single process, OpenSIN-AI has **92+ specialized agents** — each with its own CLI, MCP server, and A2A endpoint. This means:

- **Specialization beats generalization** — each agent is an expert in its domain
- **Horizontal scaling** — add more agents without changing the core
- **Fault isolation** — one agent crash doesn't take down the system

### 2. n8n Foundation (Free, Indestructible)

OpenSIN-AI uses n8n on a free OCI VM as its routing backbone:

- **Zero cost** — Oracle Cloud Always-Free tier
- **Visual workflows** — drag-and-drop automation
- **200+ integrations** — n8n's built-in connector library
- **No vendor lock-in** — self-hosted, full control

### 3. Apple Ecosystem Native (12 Agents)

No competitor has native Apple automation:

- FaceTime, iMessage, Notes, Calendar, Reminders, Safari, Shortcuts
- macOS system control (AppleScript, System Events)
- iPhone integration (USB, screenshots, shortcuts)
- Siri voice commands via Shortcuts

### 4. Triple Trigger System

OpenSIN-AI supports three independent trigger mechanisms:

1. **Heartbeat** — Periodic agent check-in (like OpenClaw)
2. **Cron Scheduler** — Scheduled recurring tasks (like Gemini)
3. **Webhook** — External event triggers (like OpenClaw)

### 5. Multi-Model Freedom

Unlike Claude Code (Claude only) or Gemini Agent (Gemini only):

- OpenAI GPT-5.4 (primary, via Antigravity)
- Google Gemini 3.1 Pro/Flash (via Antigravity)
- Anthropic Claude Sonnet/Opus (via Antigravity)
- NVIDIA Qwen 3.5 (via NIM)
- Any local model (via Ollama)

---

## Implementation Roadmap

### Phase 1: Foundation (Sprint 1-2)

- Heartbeat system in `opensin-ai-cli`
- Multi-model router with failover
- Cron scheduler and unified agent orchestrator
- Approval hooks and permission gate integration
- Unified messaging API
- Extended memory system

### Phase 2: Reach & Control (Sprint 3-4)

- Channel-based remote control
- Generic subagent spawning
- Progress tracking
- Approval hooks framework

### Phase 3: Orchestration (Sprint 5-6)

- External harness control (ACP)
- Session branching & compaction
- Audit logging

### Phase 4: Differentiation (Sprint 7-8)

- Canvas/A2UI workspace
- Voice interaction
- Extended Google Workspace (Gmail, Calendar, Slides)

---

## Sprint 1 Verified

- `HeartbeatSystem` now handles autonomous check-ins, queue polling, backoff, and graceful shutdown.
- `FailoverRouter` now selects across OpenAI OCI, Antigravity, and NIM with health-based fallback.
- `CronScheduler` now parses cron expressions and executes scheduled tasks.
- `ApprovalHooks` now enforces risk-based gating for safe, write, destructive, network, financial, and auth actions.
- `AgentOrchestrator` ties the systems together with `AgentLoop`, `LoopMode`, `SmartModelRouter`, and `PermissionEvaluator`.
- `CLIAgent` now routes through the orchestrator for model selection and approval policy checks.

---

_See also: [OpenSIN-AI Agent Feature Spec](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/opensin-ai-agent-feature-spec.md)_

---

## Relevante Mandate

| Mandat                   | Priority | Doku                                                    |
| ------------------------ | -------- | ------------------------------------------------------- |
| **Bun-Only**             | -1.5     | `bun install` / `bun run` statt npm                     |
| **LLM via opencode CLI** | -2.5     | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht**  | -200.0   | SELBST MACHEN via `create-a2a-sin-agent`                |
| **Kommentar-Pflicht**    | -6.0     | EXTREM umfangreiche Kommentare                          |

→ [Alle Mandate](/best-practices/a2a-communication)
