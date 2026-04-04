# 📋 OpenSIN Governance, Marketing & Operations

Zusammenfassung der Governance-, Marketing- und Operations-Dokumentation aus dem OpenSIN Haupt-Repo.

## 🏛️ Governance Framework – 10 Regeln

1. **Zero Human Intervention** – Agenten bitten NIEMALS um manuelle Hilfe
2. **Self-Healing First** – Bei Blockaden: Bypass selbst bauen, nicht warten
3. **Full Autonomy** – Agenten haben alle Permissions für JEDE Operation
4. **Research → Issue → Implementation** – Keine direkte Implementierung ohne Recherche
5. **Google Docs Supremacy** – Kein UI-Geklicke, nur `sin-document-forge` MCP
6. **No-Silo Mandate** – Jedes Problem wird zur gesamten Team-Aufgabe
7. **Top 20 Doc Rule** – Kein neues .md ohne Genehmigung
8. **Atomic Architecture** – Ein File = Eine Aufgabe
9. **Visuals First** – Keine PRs ohne visuelle Dokumentation
10. **Never Idle** – Agenten suchen proaktiv nach Arbeit (aber verändern nichts ohne Erlaubnis)

## 📊 Competitive Analysis 2026

| Konkurrent | Schwäche | OpenSIN Vorteil |
|------------|----------|----------------|
| **LangGraph** | Nur Orchestrierung, keine Execution | Full Stack: Orchestrierung + Execution |
| **AutoGen** | Microsoft-locked, nicht A2A-native | 100% Open Source, A2A-first |
| **CrewAI** | Klein (< 10 Agenten), kein Production-Grade | 620+ Agent Teams, 24/7 autonom |
| **GitHub Copilot** | Nur Code-Vervollständigung | Full Agent OS: Code + Infra + Social |
| **Cursor** | Nur IDE, kein Fleet Management | IDE + Fleet + A2A + Auth Rotator |
| **Windsurf** | Nur Code-Vervollständigung | Supercomplete + File Changes + Subtask Tree |
| **Replit Agent** | Cloud-only, kein Self-Hosting | Self-hosted + Cloud + Hybrid |
| **Bolt.new** | Nur Web-Apps, kein Enterprise | Enterprise: 372 Packages, 25+ Domains |

## 📝 Blog Post Regeln

Jeder Blog Post MUSS haben:
- **Titel:** Prägnant, Keyword-optimiert, < 60 Zeichen
- **Einleitung:** Problem → Lösung in 2-3 Sätzen
- **Hauptteil:** Code-Beispiele, Screenshots, Architektur-Diagramme
- **Fazit:** Zusammenfassung + Call-to-Action
- **Metadaten:** Author, Datum, Tags, Featured Image
- **SEO:** Meta Description < 160 Zeichen, Open Graph Tags

## 🚀 Marketing-Strategie

| Kanal | Taktik | Ziel |
|-------|--------|------|
| **GitHub** | README-Qualität, Blog-Promotion, Good First Issues | 10K Stars |
| **Discord** | Community-Server, Bot-Integration, Events | 5K Members |
| **Twitter/X** | Daily Updates, Thread-Serien, Demo-Videos | 10K Followers |
| **Blog** | 76 Posts (bestehend), wöchentliche neue | 50K Monthly Views |
| **YouTube** | Tutorial-Serien, Live-Demos, Architektur-Deep-Dives | 5K Subscribers |
| **Product Hunt** | Launch mit vollem Feature-Set | #1 Product of the Day |

## 🗄️ Database Architektur

| Komponente | Technologie | Zweck |
|------------|-------------|-------|
| **Supabase** | PostgreSQL + Row Level Security | Hauptdatenbank, Auth, Realtime |
| **Redis** | Cache, Lease, Dedupe, Rate Limits | Ephemeral State |
| **NATS JetStream** | Event Transport, Replay Stream | Message Bus |
| **Restate** | Durable Workflow Execution | Workflow Truth |
| **S3/R2** | Object Storage | Artifact Blobs |

## 🔗 Domain Migration (delqhi.com → opensin.ai)

10 Subdomains, alle über Cloudflare (kostenlos):
- `opensin.ai` (Hauptwebsite), `my` (App), `docs`, `api`, `status`, `blog`, `cdn`, `hf` (Tunnel), `n8n` (Tunnel), `discord` (Workers)

## 📦 Container Registry

- **GitHub Container Registry** (ghcr.io) für alle Docker Images
- Images: `sin-solver/room-13-fastapi-coordinator`, `sin-solver/sin-usebrowser`
- Multi-Arch: `linux/amd64`, `linux/arm64`

## 🤝 Discord Setup

| Komponente | Status |
|------------|--------|
| Server | ✅ Existiert (discord.gg/opensin) |
| Bot Token | ✅ In .env.example |
| Agent Spec | ✅ In Backend konfiguriert |
| Hermes Dispatch | ✅ Konfiguriert |

## 📋 ADR (Architecture Decision Records)

Jede Architektur-Entscheidung wird als ADR dokumentiert:
- **Kontext:** Was war das Problem?
- **Entscheidung:** Was wurde beschlossen?
- **Konsequenzen:** Was sind die Auswirkungen?
- **Status:** Proposed → Accepted → Deprecated → Superseded

## 🔍 Issue Phases

### Phase 1: Narrative Architecture
Issues werden als narrative Stories geschrieben – nicht als technische Tasks. Jede Story hat: Protagonist (User), Konflikt (Problem), Auflösung (Lösung).

### Phase 2: Visual System Buildout
Jedes Issue braucht visuelle Dokumentation – Screenshots, Diagramme, Videos. Kein Issue ohne visuellen Kontext.

### Phase 3: Hardening
Alle Issues werden gegen Production-Standards gehärtet – Error Handling, Security, Performance, Monitoring.

## 🔗 Verknüpfte Dokumentation

- [Architektur](./architecture.md) – Gesamtübersicht
- [Best Practices](./best-practices.md) – Entwicklungsstandards
- [Core Principles](./core-principles.md) – Unsere Leitlinien
