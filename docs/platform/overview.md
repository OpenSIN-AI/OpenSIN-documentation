# 🏛️ OpenSIN Plattform-Architektur

Das OpenSIN Haupt-Repo ([OpenSIN-AI/OpenSIN](https://github.com/OpenSIN-AI/OpenSIN)) ist das Herzstück – **372 Packages, 620 Agent Teams**, Score: 98/100.

## 📊 Quick Stats

| Metrik | Wert |
|--------|------|
| **Packages** | 372 |
| **READMEs** | 375 (100%) |
| **Tests** | 379 (100%) |
| **Agent Teams** | 620 |
| **Blog Posts** | 76 |
| **Open Issues** | 0 |
| **Score** | 98/100 |
| **Repositories** | 157 |

## 🚀 Neueste Features (April 2026)

### OpenSIN Haupt-Repo

| Feature | Commit | Beschreibung |
|---------|--------|-------------|
| **Per-Workspace Codebase Indexing** | `ffd83c4` | RAG-basiertes Code-Verständnis wie Roo Code – indiziert jedes Workspace separat |
| **Long-Term Developer Memory** | `4e59625` | Persistenter Kontext über Sessions hinweg wie Pieces – merkt sich Präferenzen, Patterns, Entscheidungen |
| **One-Click Deploy** | `4e59625` | Integriertes Deployment wie Replit Agent 4 und Bolt.new – direkt aus der IDE |
| **Orchestrator/Delegation Mode** | `6dc7d8f` | Auto-Delegation zu spezialisierten Modi wie Roo Code Boomerang – erkennt Task-Typ und delegiert |
| **Git Worktree Support** | `6dc7d8f` | Parallele Entwicklung in isolierten Branches – mehrere Features gleichzeitig ohne Konflikte |

### OpenSIN-Code (VS Code Extension)

| Feature | Commit | Beschreibung |
|---------|--------|-------------|
| **File Changes Panel** | `07bceab` | Visuelle Änderungsverfolgung wie Roo Code – zeigt alle Modifikationen im aktuellen Task |
| **Nested Subtask Tree** | `a8af45c` | Rekursive Task-Visualisierung – verschachtelte Subtasks mit Abhängigkeiten |
| **Supercomplete** | `3311204` | Multi-Line Code-Predictions wie Windsurf/Codium – vervollständigt ganze Code-Blöcke |

### OpenSIN-Backend

| Feature | Commit | Beschreibung |
|---------|--------|-------------|
| **Fleet Registry** | `3f26aaf` | Vollständige Fleet-Registrierung aller 620 Agent Teams |
| **Handoffs Service** | `3f26aaf` | Strukturierter Agent-Handoff-Service für Multi-Agent-Workflows |
| **Runtime Fixes** | `182038c` | `execFileAsync` opencode Pattern in allen 133 runtime.ts Files |

## 🏗️ Alpha Backbone Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    OpenSIN Alpha Backbone                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │   Room-13    │    │   Restate    │    │   NATS JetStream │  │
│  │  (FastAPI    │───→│  (Workflow   │───→│   (Event         │  │
│  │  Ingress)    │    │   Truth)     │    │    Transport)    │  │
│  └──────┬───────┘    └──────┬───────┘    └────────┬─────────┘  │
│         │                   │                      │            │
│  ┌──────┴───────────────────┴──────────────────────┴───────┐  │
│  │              SIN-Supabase (OCI VM)                       │  │
│  │  Projections · Approvals · Auth Grants · Capabilities    │  │
│  │  Memory Metadata · Artifact Refs                         │  │
│  └──────────────────────────┬───────────────────────────────┘  │
│                             │                                   │
│  ┌──────────────────────────┴───────────────────────────────┐  │
│  │              Stateless HF Executors                       │  │
│  │  Subscribe via JetStream → Execute → Checkpoint → Emit   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Control Plane Split                          │  │
│  │  SIN-Zeus (Plan) → Hermes (Dispatch) → SIN-Code (Exec)  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## 🔑 Authority Matrix

| Concern | Authority | Notes |
|---------|-----------|-------|
| Workflow Status, Retries, Timers, Suspend/Resume | **Restate** | Single durable workflow truth |
| Event Transport & Replay Stream | **NATS JetStream** | Transport only, never business truth |
| Control-Plane Projections, Approvals, Auth Grants | **SIN-Supabase** | Operator and runtime read models |
| Cache, Lease, Dedupe Windows, Rate Limits | **Redis** | Ephemeral only; degraded mode ≠ authoritative |
| Artifact Blobs | **Object Storage** | Referenced from Supabase metadata |
| Scoped Workflow/Executor Grants | **SIN-Authenticator/authd** | Issue, revoke, rotate, audit |

## 🌐 Subdomains (opensin.ai)

| Subdomain | Zweck | Status |
|-----------|-------|--------|
| **opensin.ai** | Hauptwebsite | ⏳ DNS Propagation |
| **my.opensin.ai** | App / Dashboard | ⏳ DNS Propagation |
| **docs.opensin.ai** | Dokumentation | ⏳ DNS Propagation |
| **api.opensin.ai** | API Gateway | ⏳ DNS Propagation |
| **status.opensin.ai** | Status Page | ⏳ DNS Propagation |
| **blog.opensin.ai** | Blog | ⏳ DNS Propagation |
| **cdn.opensin.ai** | CDN / Assets | ⏳ DNS Propagation |
| **hf.opensin.ai** | HF Space Proxy | ⏳ DNS Propagation |
| **n8n.opensin.ai** | CI/CD Pipeline | ⏳ DNS Propagation |
| **discord.opensin.ai** | Discord Bot | ⏳ DNS Propagation |

## 🔄 Control Plane Split (Zeus Lane)

| Komponente | Authority | Forbidden | Output |
|------------|-----------|-----------|--------|
| **SIN-Zeus** (lokal) | Planning + GitHub Metadata | Product Code editieren, Tasks ausführen | Issues/Branches/Artifacts |
| **GitHub Projects/Issues** | Work Queue SSOT | Secrets in Issue Bodies | Issues + Branches |
| **Hermes** | Packaging + Routing | Requirements umplanen | Dispatch + Intake Artifacts |
| **Room-13** | Ingress API Contract | Workflow Truth werden | Tasks + Dual-Run Metadata |
| **Restate** | Workflow Truth | Durable Checkpoints umgehen | Run State |
| **JetStream** | Replayable Transport | Business Truth sein | Events to Executors |
| **SIN-Supabase** | Projections + Approvals | Local SQLite als Truth | cp_* Tables |
| **HF Executors** | Stateless Execution Plane | Local Disk/Session als Truth | Checkpoints + Terminal Events |

## 📦 Key Packages (Auszug)

| Package | Zweck |
|---------|-------|
| `opensin-sdk` | TypeScript SDK für alle APIs |
| `opensin-runtime` | Agent Runtime Engine |
| `opensin-memory` | Semantic Memory + Supabase Integration |
| `opensin-mcp-registry` | MCP Server Registry |
| `opensin-governance` | Policy Enforcement + Approval Gates |
| `opensin-observability` | Fleet Telemetry + Tracing |
| `opensin-coordinator` | Multi-Agent Coordination |
| `opensin-agent-teams` | Team Orchestration |
| `opensin-self-healing` | Autonomous Error Recovery |
| `opensin-credential-vault` | Secure Credential Management |
| `opensin-plugin-marketplace` | Plugin Registry + Installation |
| `opensin-grid-dashboard` | A2A Control Dashboard UI |
| `opensin-office-integrations` | Google/Microsoft Office Integration |
| `opensin-voice-mode` | Voice Input/Output |
| `opensin-ultraplan` | Long-Horizon Planning |
| `opensin-computer-use` | Computer Use / CDP Integration |
| `opensin-context-compression` | Context Window Optimization |
| `opensin-hooks` | Reactive Event Hooks |
| `opensin-daemon` | Background Service Manager |
| `opensin-merge-guard` | PR Merge Policy Enforcement |

## 🗺️ Roadmap Milestones

| Milestone | Owner | Status |
|-----------|-------|--------|
| **M1** – Documentation Baseline | Rico | ✅ Done |
| **M2** – Contract Stabilization | Rico | ✅ Done |
| **M3** – Storage & Environment Normalization | Rico | ✅ Done |
| **M4** – Dashboard & Control-Plane Alignment | Rico | ✅ Done |
| **M5** – Release Hardening | Jeremy | ✅ Done |
| **M6** – Agentic Platform Quality Layer | Jeremy | 🟡 In Progress |
| **M7** – Alpha Backbone Pilot | Jeremy | 🟡 In Progress |
| **M8** – Alpha Workforce Rollout | Jeremy | 🟡 In Progress |
| **M9** – Zeus Cloud Delegation | Jeremy | 🟡 In Progress |
| **M10** – GitHub Enterprise A2A Emulation | Jeremy | 🔴 Planned |
| **M11** – Omma AI Integration | Jeremy | ✅ Done (v2.1.0) |
| **M12** – Synthetic Operator | Jeremy | 🔴 Planned |

## 🔗 Verknüpfte Dokumentation

- [Architektur](./architecture.md) – Gesamtübersicht
- [A2A Fleet](./a2a-fleet.md) – Deployed Agents
- [API Reference](./api-reference.md) – Room-13, Solver-18, Omma AI
- [n8n CI/CD](./n8n-cicd.md) – Pipeline-Dokumentation
- [Repository Catalog](./repository-catalog.md) – Alle 147 Repos
