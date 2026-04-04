# 🔧 OpenSIN Architektur Deep-Dive

Zusätzliche Architektur-Dokumentation aus dem OpenSIN Haupt-Repo.

## A2A Coding Boundaries

Trennung zwischen **Infrastruktur-Agenten** (Plattform-Management) und **Coder-Agenten** (Projekt-Logik):

| Bereich | Infrastruktur-Agent | Coder-Agent |
|---------|-------------------|-------------|
| **Database** | A2A-SIN-Supabase: OCI Instanz, Docker, Backups, Connection Pooling | A2A-SIN-Code-Database: SQL Schemas, RLS Policies, Edge Functions, Vector Tables |
| **Workflows** | A2A-SIN-N8N: Installation, Patches, Volume Mounts, Docker Updates | A2A-SIN-Code-Integration: Workflow JSONs, Webhooks, API-Integration, Data Transformation |
| **AI** | A2A-SIN-Research: Web-Suche, Scraping, Raw Facts | A2A-SIN-Code-AI: RAG Pipelines, Prompt Templates, Context Windows, Semantic Search |

**Prinzip:** "Platform Provisioning vs. Project Logic Implementation"

## Autonomous Self-Healing Pipeline (Fleet V2)

```
Telegram Error → A2A-SIN-TelegramBot (Watcher)
         ↓
   n8n Webhook (92.5.60.87:5678)
         ↓
   SIN-GitHub-Issues (Ticket mit Label: bug + autonomous-dispatch)
         ↓
   SIN-Hermes (Dispatcher → generiert Dispatch-Contract)
         ↓
   A2A-Coder auf HF VM (holt Account aus Rotator-Pool → opencode CLI → Fix → PR)
```

**Payload-Schema:**
```json
{
  "incident_type": "telegram_detected_failure",
  "reporter": "A2A-SIN-TelegramBot",
  "target_repo": "Delqhi/simone-webshop",
  "error_context": "Checkout fails on step 3 with 'PaymentIntent not found'."
}
```

## Named Subagents (@mention Typeahead)

Operatoren delegieren Tasks an spezialisierte Sub-Agenten via `@mention`:

| Agent | Slug | Beschreibung |
|-------|------|-------------|
| Code Reviewer | `@code-review` | Code-Qualität und Security |
| Researcher | `@research` | Themen und Best Practices |
| Deployer | `@deploy` | Deployment-Workflows |
| Tester | `@test` | Tests ausführen und schreiben |
| Documenter | `@docs` | Dokumentation generieren |
| Refactorer | `@refactor` | Code sicher umstrukturieren |
| Debugger | `@debug` | Bugs untersuchen und fixen |

**API:** `GET /api/sub-agents`, `POST /api/sub-agents/:slug/dispatch`, `GET /api/sub-agents/tasks/:task_id`

## Context Optimizer (`/context`)

Intelligentes Context-Window-Management mit 4 Komprimierungs-Stufen:

| Stufe | Name | Trigger | Aktion |
|-------|------|---------|--------|
| 1 | Auto-Compact | 80% Nutzung | Ältere Konversation zusammenfassen |
| 2 | Micro-Compact | 85% Nutzung | `context_management` API-Parameter |
| 3 | Reactive-Compact | Context-too-large Error | Aggressive Komprimierung |
| 4 | Snip | Alle Stufen erschöpft | Nicht-kritischen Content verwerfen |

**Commands:** `/context status`, `/context compact`, `/context clear`, `/context add <file>`, `/context pin <file>`

## Memory Timestamps — Fresh vs Stale

Jeder Memory-Eintrag bekommt temporale Metadaten:

| State | Zeit seit letztem Zugriff | Staleness Score |
|-------|-------------------------|-----------------|
| `fresh` | < 24 Stunden | 0.0 - 0.5 |
| `stale` | 24 - 168 Stunden (1-7 Tage) | 0.5 - 0.8 |
| `expired` | > 168 Stunden (> 7 Tage) | 0.8 - 1.0 |

**Formel:** `staleness_score = min(1.0, time_since_last_access / expired_threshold_hours)`

## Reactive Hooks

Automatische Reaktion auf Environment-Changes:

| Hook Type | Trigger | Aktion |
|-----------|---------|--------|
| `CwdChanged` | Working Directory wechselt | .env laden, Projekt scannen |
| `FileChanged` | Datei modifiziert | Re-analysieren, Tests updaten |
| `FileCreated` | Neue Datei erscheint | Analysieren, indexieren |
| `FileDeleted` | Datei gelöscht | Referenzen updaten, Cache cleanen |
| `DirChanged` | Verzeichnis-Struktur ändert | Re-scannen, Project Map updaten |

## Automations

Always-on Agents mit Triggers für Hintergrund-Betrieb:

| Trigger | Beschreibung | Beispiel |
|---------|-------------|----------|
| `file_changed` | Datei/Verzeichnis Modifikation | `src/**/*.ts` ändert sich |
| `cron` | Geplante Ausführung | Alle 15 Minuten |
| `webhook` | Externer HTTP Trigger | GitHub Push Event |
| `agent_state` | Agent Lifecycle Event | Agent完成任务 |
| `nats_event` | NATS JetStream Subject | `sin.event.task.completed` |

## Design Mode

UI-Annotation-System für visuelles Design-Intent:

- **Annotation Types:** Point, Region, Arrow, Text, Color
- **Export:** Design Tokens (CSS Variables), Component Specs (React Props), Implementation Checklist
- **Framework Support:** React + Tailwind (default), erweiterbar

## 🔗 Verknüpfte Dokumentation

- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
- [OpenSIN Packages](./opensin-packages.md) – Alle 372 Packages
- [OpenSIN Plattform](./opensin-platform.md) – Architektur-Übersicht
