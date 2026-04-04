# 🔌 API Reference

Vollständige API-Referenz für die OpenSIN-Plattform.

## Room-13 FastAPI Coordinator

**Base Path:** `services/room-13-fastapi-coordinator`

### Health & Monitoring

| Method | Path | Beschreibung |
|--------|------|-------------|
| GET | `/health` | Overall API health |
| GET | `/ready` | Automation-ready (non-200 wenn nicht ready) |
| GET | `/version` | Service version |
| GET | `/metrics` | Prometheus-compatible plaintext metrics |

### Task API

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/tasks` | Task erstellen |
| GET | `/api/tasks` | Alle Tasks auflisten |
| GET | `/api/tasks/{task_id}` | Task Details |
| POST | `/api/tasks/claim-next` | Nächsten Task claimen |
| PUT | `/api/tasks/{task_id}/assign` | Task zuweisen |
| PUT | `/api/tasks/{task_id}/start` | Task starten |
| PUT | `/api/tasks/{task_id}/complete` | Task abschließen |
| DELETE | `/api/tasks/{task_id}` | Task löschen |

### Worker API

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/workers` | Worker registrieren |
| GET | `/api/workers` | Alle Worker auflisten |
| GET | `/api/workers/{worker_id}` | Worker Details |
| PUT | `/api/workers/{worker_id}` | Worker updaten |
| POST | `/api/workers/{worker_id}/heartbeat` | Heartbeat senden |
| POST | `/api/workers/{worker_id}/claim` | Task claimen |
| POST | `/api/workers/{worker_id}/checkpoint` | Checkpoint speichern |
| POST | `/api/workers/{worker_id}/resume` | Von Checkpoint resumed |
| POST | `/api/workers/{worker_id}/release` | Task freigeben |
| POST | `/api/workers/{worker_id}/task/complete` | Task als completed melden |
| DELETE | `/api/workers/{worker_id}` | Worker deregistrieren |

### Additional Coordinator Groups

| Prefix | Zweck |
|--------|-------|
| `/api/services` | Service Management |
| `/api/credentials` | Credential Management |
| `/api/gateway` | API Gateway |
| `/api/captcha` | CAPTCHA Solving |
| `/api/webhooks` | Webhook Management |
| `/api/workflows` | Workflow Management |
| `/api/n8n` | n8n Integration |
| `/api/steel` | Steel Browser Integration |

## Omma AI Integration (v2.1.0)

### Parallel Agent Orchestrator

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v2/parallel/orchestrate` | Fan-out/fan-in Execution |
| POST | `/api/v2/parallel/layers/sync` | Layer Sync mit Conflict Resolution |
| GET | `/api/v2/parallel/orchestrations/{id}` | Orchestration Status |
| POST | `/api/v2/parallel/a2a/dispatch` | A2A Sub-Task Dispatch |

**Request Body `/orchestrate`:**
```json
{
  "task": "string",
  "agents": ["agent-1", "agent-2"],
  "merge_strategy": "consensus | best-of-n | append",
  "timeout_sec": 60
}
```

### Asset Pipeline

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v2/assets/upload` | Asset Upload (CSV, JSON, XLSX, Images, Videos, 3D) |
| GET | `/api/v2/assets/{asset_id}` | Asset Metadata |
| GET | `/api/v2/assets/{asset_id}/schema` | Auto-detected Schema |
| POST | `/api/v2/assets/{asset_id}/dashboard` | Data-driven Dashboard generieren |
| GET | `/api/v2/assets/{asset_id}/dashboard/{dashboard_id}` | Dashboard abrufen |
| DELETE | `/api/v2/assets/{asset_id}` | Asset löschen |

### Preview Server

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v2/previews` | Ephemeral Preview erstellen |
| GET | `/api/v2/previews/{preview_id}` | Preview Status + URL |
| GET | `/api/v2/previews/{preview_id}/feedback` | Feedback sammeln |
| POST | `/api/v2/previews/{preview_id}/feedback` | Feedback einreichen |
| POST | `/api/v2/previews/{preview_id}/improve` | Auto-Improvement triggern |
| GET | `/api/v2/previews/{preview_id}/versions` | Version History |
| POST | `/api/v2/previews/{preview_id}/rollback` | Zu vorheriger Version rollback |
| DELETE | `/api/v2/previews/{preview_id}` | Preview teardown |

### Unified Pipeline

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v2/pipeline/run` | Unified Multi-Layer Pipeline |
| GET | `/api/v2/pipeline/runs/{run_id}` | Pipeline Run Status |
| GET | `/api/v2/pipeline/runs/{run_id}/layers` | Per-Layer Outputs |

### App Builder

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v2/app-builder/create` | App aus Prompt erstellen |
| GET | `/api/v2/app-builder/apps/{app_id}` | App abrufen |
| POST | `/api/v2/app-builder/apps/{app_id}/revise` | App revidieren |
| GET | `/api/v2/app-builder/apps/{app_id}/versions` | Version History |
| POST | `/api/v2/app-builder/apps/{app_id}/export` | App exportieren (HTML/CSS/JS oder ZIP) |
| GET | `/api/v2/app-builder/templates` | Templates auflisten |
| GET | `/api/v2/app-builder/templates/{template_id}` | Template abrufen |

## A2A Agent API

Jeder A2A-Agent expose folgende Standard-Endpoints:

| Method | Path | Beschreibung |
|--------|------|-------------|
| GET | `/health` | Health Check |
| POST | `/a2a/v1` | A2A Protocol Endpoint |
| GET | `/.well-known/agent-card.json` | Agent Discovery Card |

## Legacy API (v1)

| Method | Path | Beschreibung |
|--------|------|-------------|
| POST | `/api/v1/auth/login` | Authentifizierung |
| POST | `/api/v1/auth/logout` | Token invalidieren |
| POST | `/api/v1/solve/captcha` | CAPTCHA einreichen |
| GET | `/api/v1/solve/status/{task_id}` | CAPTCHA Status |
| POST | `/api/v2/enterprise/consensus` | Multi-Model Consensus |
| GET | `/api/v1/health/rooms` | Room Status |

## 🔗 Verknüpfte Dokumentation

- [OpenSIN Plattform](./opensin-platform.md) – Architektur-Übersicht
- [n8n CI/CD](./n8n-cicd.md) – Pipeline-Dokumentation
- [Best Practices](./best-practices.md) – Entwicklungsstandards
