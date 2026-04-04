# 🧪 Testing, Environment & Database

Vollständige Referenz für Testing, Environment-Variablen und Datenbank-Architektur.

## 🧪 Testing Guide

### Test-Layer

| Layer | Commands | Zweck |
|-------|----------|-------|
| **Docs & Governance** | `npm run test:docs:root`, `npm run test:a2a:fleet`, `npm run test:a2a:live -- --agent <slug>` | Dokumentations-Qualität, Fleet-Validation |
| **Contract & Architecture** | `npm run test:contracts:active`, `npm run test:guardrails`, `npm run test:cycles` | API-Verträge, Architektur-Gates |
| **Python Tests** | `pytest tests/unit -q`, `python3 -m py_compile` | Python-Unit-Tests, Syntax-Checks |
| **Package Runtime** | `npm --prefix packages/research-core test`, `npm --prefix dashboard-enterprise run lint && type-check && build` | Package-spezifische Tests |
| **E2E** | `npm run test:e2e:playwright` | End-to-End Browser Tests |

### Empfohlene lokale Reihenfolge

```bash
npm run test:docs:root
npm run test:a2a:fleet
npm run test:a2a:live -- --agent <slug>
npm run test:contracts:active
pytest tests/unit -q
npm --prefix packages/research-core test && npm --prefix packages/research-core run build
npm --prefix dashboard-enterprise run lint && npm --prefix dashboard-enterprise run type-check
npm --prefix dashboard-enterprise run build
npm run test:e2e:playwright
```

### A2A Fleet Validation

- `npm run test:a2a:fleet` – Prüft kanonische OpenCode MCP-Abdeckung: `mcp-config.json`, `clients/opencode-mcp.json`, `.opencode/opencode.json`
- `npm run test:a2a:live -- --agent <slug>` – Hard Publish/Reachability Gate: lokaler Build, `print-card`, `agent.help`, `serve-mcp`, Remote-Verifikation

### CI-Guidance

- Fail fast auf Docs und Architecture Gates
- Python-Matrix auf 3.11 und 3.12
- Langsamere Dashboard-Tests erst nach schnellen Structural Checks
- Playwright HTML/JSON/Blob-Artefakte für fehlgeschlagene Runs aufbewahren

## 🔧 Environment Reference

### Core Coordinator Variables

| Variable | Zweck |
|----------|-------|
| `DATABASE_URL` / `POSTGRES_URL` | PostgreSQL Connection |
| `REDIS_URL` / `REDIS_HOST` / `REDIS_PORT` | Redis Connection |
| `NATS_URL` | NATS Client (default: `nats://nats:4222`) |
| `NATS_MONITORING_URL` | NATS Monitoring (default: `http://nats:8222`) |
| `RESTATE_ADMIN_URL` | Restate Admin API (default: `http://restate:9070`) |
| `RESTATE_INGRESS_URL` | Restate Ingress (default: `http://restate:9071`) |
| `HITL_TOKEN` / `HITL_TOKENS` | Human-in-the-Loop Auth |
| `PORT` | Service Port |

### Worker Runtime Variables

| Variable | Zweck |
|----------|-------|
| `ROOM13_COORDINATOR_URL` | Room-13 Coordinator Endpoint |
| `WORKER_RUN_ID` | Aktuelle Run-ID |
| `WORKER_LEASE_TTL_SEC` | Lease TTL |
| `WORKER_HEARTBEAT_INTERVAL_SEC` | Heartbeat Intervall |
| `SIN_WORKER_IDENTITY` | Worker Identität |

### TikTok Broker Variables

| Variable | Zweck |
|----------|-------|
| `TIKTOK_CLIENT_KEY` | TikTok API Client Key |
| `TIKTOK_CLIENT_SECRET` | TikTok API Client Secret |
| `TIKTOK_REDIRECT_URI` | OAuth Callback URL |
| `TIKTOK_CONNECT_SCOPES` | `user.info.basic,video.upload,video.publish` |

### Regeln

- Secrets NIEMALS in git – `.env` für lokal, Secret Store für Production
- Neue Env-Variablen HIER dokumentieren bevor sie in CI/Production genutzt werden
- Canonical Names bevorzugen, Aliases nur für Kompatibilität

## 🗄️ Database Architektur

### Storage Topology

| Layer | Technologie | Zweck |
|-------|-------------|-------|
| **SQLite** | Lokale Telemetry | Runtime-Telemetry, Event History |
| **Redis** | Cache/Lease/Dedupe | Task/Worker Koordination, Rate Limits |
| **Postgres** | Canonical Relational | Service-Daten via Supabase |
| **NATS JetStream** | Event Streaming | Durable Events, Replay, Consumer Groups |
| **Restate** | Workflow Orchestration | Durable Workflows mit Exactly-Once |
| **S3/R2** | Object Storage | Artifact Blobs |

### Alpha Control-Plane Schema (SIN-Supabase)

| Tabelle | Zweck |
|---------|-------|
| `cp_runs` | Workflow Runs mit Tenant/Team/Workflow/Run IDs |
| `cp_events` | Immutable Events mit Idempotency Keys |
| `cp_approvals` | Approval Gates mit SLA und Audit Trail |
| `cp_auth_grants` | Scoped Auth Tokens für Executoren |
| `cp_capabilities` | Machine-readable Agent Capabilities |
| `cp_world_edges` | Typed Relationships zwischen Agenten |
| `cp_projection_freshness` | Projection Staleness Tracking |
| `cp_artifact_refs` | Artifact Metadata (Checksum, Retention, Encryption) |
| `cp_memory_items` | Semantic Memory mit Vector Embeddings |
| `cp_memory_links` | Memory-Item Verknüpfungen |

### Memory Governance

- Jeder Memory-Eintrag MUSS Provenance haben (`provenance_type`, `source_run_id`)
- TTLs: Episodic (kurz), Semantic (lang, review-required), Procedural (versioned), Artifact (retention-based)
- Poisoning Controls: `poisoned=true` für Audit, aber ausgeschlossen von Runtime
- Retrieval Gates: Memory darf nur mit Provenance Execution beeinflussen

### Artifact Policy

- Blob Truth: Object Storage
- Metadata Truth: Supabase `cp_artifact_refs`
- Jede Artifact braucht: `tenant_id`, `run_id`, `checksum_sha256`, `retention_class`, `immutable`, `encryption_mode`
- Retention Classes: `ephemeral_debug`, `run_evidence`, `release_evidence`, `governance_record`, `pinned_manual`

## 🔗 Verknüpfte Dokumentation

- [API Reference](./api-reference.md) – Vollständige API-Referenz
- [OpenSIN Plattform](./opensin-platform.md) – Architektur-Übersicht
- [Best Practices](./best-practices.md) – Entwicklungsstandards
