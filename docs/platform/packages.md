# 📦 OpenSIN Packages Übersicht

Übersicht aller **372 Packages** im OpenSIN Haupt-Repo.

## Core Packages

| Package | Zweck |
|---------|-------|
| `opensin-sdk` | TypeScript SDK für alle OpenSIN APIs – type-safe Client für ACP, A2A, REST |
| `opensin-runtime` | Zentrale Agent Runtime Engine – Execution Loop, Tool Dispatch, State Management |
| `opensin-memory` | Semantic Memory + Supabase Integration – Langzeit-Gedächtnis für Agenten |
| `opensin-coordinator` | Multi-Agent Coordination – Task-Verteilung, Dependency Resolution |
| `opensin-governance` | Policy Enforcement + Approval Gates – Runtime Policy, Human-in-the-Loop |
| `opensin-observability` | Fleet Telemetry + Tracing – OpenTelemetry, Metrics, Logging |
| `opensin-daemon` | Background Service Manager – Persistente Hintergrundprozesse |
| `opensin-hooks` | Reactive Event Hooks – File-System-Watcher, Git-Hooks, Webhooks |

## Agent Packages

| Package | Zweck |
|---------|-------|
| `opensin-agent-teams` | Team Orchestration – Multi-Agent-Koordination in Teams |
| `opensin-agent-tool` | Agent Tool System – Tool-Registry, Permission Matrix |
| `opensin-agent-cache` | Agent Response Cache – Caching für wiederkehrende Anfragen |
| `opensin-agent-governance` | Agent Governance – Policy Enforcement pro Agent |
| `opensin-agent-safety` | Agent Safety – Input/Output Guardrails, Jailbreak Detection |
| `opensin-self-healing` | Autonomous Error Recovery – Auto-Debug, Auto-Fix, Auto-Test |
| `opensin-proactive` | Proactive Analysis – Automatische Code-Reviews on Save |
| `opensin-adversary` | Adversary Mode – Selbstkritik, Gegenargumente, Stress-Tests |

## Integration Packages

| Package | Zweck |
|---------|-------|
| `opensin-mcp-registry` | MCP Server Registry – Discovery, Konfiguration, Health Checks |
| `opensin-plugin-marketplace` | Plugin Registry + Installation – Marketplace für Community-Plugins |
| `opensin-office-integrations` | Google/Microsoft Office Integration – Docs, Sheets, Drive, Outlook |
| `opensin-credential-vault` | Secure Credential Management – Verschlüsselte Credential-Speicherung |
| `opensin-merge-guard` | PR Merge Policy Enforcement – Automatische Merge-Gates |

## UI/UX Packages

| Package | Zweck |
|---------|-------|
| `opensin-grid-dashboard` | A2A Control Dashboard UI – Fleet-Übersicht, Agent-Status, Metrics |
| `opensin-computer-use` | Computer Use / CDP Integration – Browser-Automatisierung via Chrome DevTools |
| `opensin-voice-mode` | Voice Input/Output – Spracherkennung und -ausgabe |
| `opensin-collab-workspace` | Collaborative Workspace – Echtzeit-Zusammenarbeit mehrerer Agenten |

## Code Intelligence Packages

| Package | Zweck |
|---------|-------|
| `opensin-ultraplan` | Long-Horizon Planning – Multi-Schritt-Planung mit Abhängigkeiten |
| `opensin-context-compression` | Context Window Optimization – Intelligente Kontext-Komprimierung |
| `opensin-semantic-search` | Semantic Code Search – Vektor-basierte Code-Suche |
| `opensin-skill-system` | Skill System – Wiederverwendbare Agenten-Fähigkeiten |
| `opensin-tool-system` | Tool System – Ausführbare Agenten-Tools |

## Infrastructure Packages

| Package | Zweck |
|---------|-------|
| `opensin-rust-core` | Rust Core Library – Performance-kritische Komponenten |
| `opensin-cli` | Command Line Interface – CLI für OpenSIN-Operationen |
| `opensin-mailbox` | Mail System – Email-Integration für Agenten |

## 🔗 Verknüpfte Dokumentation

- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
- [OpenSIN Plattform](./opensin-platform.md) – Architektur-Übersicht
- [API Reference](./api-reference.md) – Vollständige API-Referenz
