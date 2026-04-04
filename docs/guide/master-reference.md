# 📋 OpenSIN Master Reference

Vollständige Referenz für alle OpenSIN-Konzepte, Policies und Prozesse.

## 🏗️ Architecture Decision Records (ADR)

Jede Architektur-Entscheidung wird als ADR dokumentiert:

| Feld | Beschreibung |
|------|-------------|
| **Titel** | Kurze Beschreibung der Entscheidung |
| **Status** | Proposed → Accepted → Deprecated → Superseded |
| **Kontext** | Was war das Problem? Welche Alternativen gab es? |
| **Entscheidung** | Was wurde beschlossen und warum? |
| **Konsequenzen** | Positive und negative Auswirkungen |
| **Datum** | Wann wurde die Entscheidung getroffen? |

**Beispiel:** ADR-001: "NATS JetStream als Event Transport" – Accepted

## 📊 Alpha Scorecard

Bewertung des Alpha-Backbone-Piloten:

| Metrik | Ziel | Status |
|--------|------|--------|
| **Room-13 Ingress Contract** | Stabil | ✅ |
| **Restate Workflow Truth** | Durable Execution | ✅ |
| **JetStream Event Delivery** | Replayable, Durable | ✅ |
| **SIN-Supabase Projections** | Aktuell, Konsistent | ✅ |
| **HF Executor Statelessness** | Keine lokale Truth | ✅ |
| **Auth Grant Issuance** | Scoped, Revocable | ✅ |
| **Memory Provenance** | Source-traceable | ✅ |
| **Artifact Immutability** | Checksum-verified | ✅ |

## 🎯 Best-of-N

Multi-Modell-Vergleich für kritische Tasks:

1. **Prompt an N Modelle senden** (z.B. Claude Sonnet, GPT-4o, Gemini Pro)
2. **Antworten sammeln** und parallel auswerten
3. **Bewertung** nach Qualität, Sicherheit, Vollständigkeit
4. **Beste Antwort auswählen** und zurückgeben

**Use Cases:** Code-Reviews, Architektur-Entscheidungen, Security-Audits

## ⚔️ Adversary Mode

Selbstkritik und Gegenargumente für robuste Entscheidungen:

- **Mode:** Agent spielt den "Advocate of the Opposite"
- **Ziel:** Schwachstellen in Plänen, Code und Architektur finden
- **Trigger:** `@adversary <prompt>` oder automatisch vor Production-Deploys
- **Output:** Liste von Gegenargumenten, Risiken, alternativen Ansätzen

## 🔌 MCP Elicitation

MCP-Server zur Extraktion von Informationen aus externen Quellen:

| MCP | Zweck |
|-----|-------|
| `sin-research` | Web-Suche, Scraping, Data Extraction |
| `sin-github` | Repository-Analyse, Issue-Tracking |
| `sin-google-docs` | Dokumenten-Extraktion und -Erstellung |
| `sin-database` | Datenbank-Abfragen und Schema-Analyse |

## 📜 Drop-in Policies

Vorgefertigte Policies für schnelle Integration:

| Policy | Zweck | Anwendung |
|--------|-------|-----------|
| `zero-human-intervention` | Keine manuelle Hilfe | Alle Agenten |
| `self-healing-first` | Auto-Repair vor Eskalation | Infrastructure Agents |
| `never-idle` | Proaktive Arbeitssuche | Alle Agenten |
| `visuals-first` | Visuelle Dokumentation | PRs, Issues |
| `atomic-architecture` | Ein File = Eine Aufgabe | Code-Struktur |

## 📦 Container Registry

**GitHub Container Registry** (ghcr.io) für alle Docker Images:

| Image | Zweck | Architekturen |
|-------|-------|---------------|
| `sin-solver/room-13-fastapi-coordinator` | Room-13 API Server | linux/amd64, linux/arm64 |
| `sin-solver/sin-usebrowser` | Browser Automation Worker | linux/amd64, linux/arm64 |
| `sin-solver/n8n-builder` | n8n Workflow Builder | linux/amd64, linux/arm64 |

**Build & Push:**
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/opensin-ai/room-13:latest --push .
```

## 💬 Discord Setup

| Komponente | Status |
|------------|--------|
| **Server** | ✅ discord.gg/opensin |
| **Bot Token** | ✅ In .env.example |
| **Agent Spec** | ✅ In Backend konfiguriert |
| **Hermes Dispatch** | ✅ Konfiguriert |
| **Channels** | #general, #dev, #help, #mentorship, #showcase, #governance |

## 🌐 Domain Migration (delqhi.com → opensin.ai)

10 Subdomains über Cloudflare (alle kostenlos):

| Subdomain | Zweck | Methode |
|-----------|-------|---------|
| `opensin.ai` | Hauptwebsite | Cloudflare Pages |
| `my.opensin.ai` | App / Dashboard | Vercel |
| `docs.opensin.ai` | Dokumentation | Cloudflare Pages |
| `api.opensin.ai` | API Gateway | Cloudflare Workers |
| `status.opensin.ai` | Status Page | Cloudflare Pages |
| `blog.opensin.ai` | Blog | Cloudflare Pages |
| `cdn.opensin.ai` | CDN / Assets | Cloudflare R2 |
| `hf.opensin.ai` | HF Space Proxy | Cloudflare Tunnel |
| `n8n.opensin.ai` | CI/CD Pipeline | Cloudflare Tunnel |
| `discord.opensin.ai` | Discord Bot | Cloudflare Workers |

## 📋 Issue Phases

### Phase 1: Narrative Architecture
Issues als narrative Stories – Protagonist (User), Konflikt (Problem), Auflösung (Lösung).

### Phase 2: Visual System Buildout
Jedes Issue braucht visuelle Dokumentation – Screenshots, Diagramme, Videos.

### Phase 3: Hardening
Alle Issues gegen Production-Standards – Error Handling, Security, Performance, Monitoring.

## 🚀 Phase 5 Integration Plan

Integration aller OpenSIN-Komponenten in ein kohärentes Gesamtsystem:

1. **Room-13** als zentraler Ingress Point
2. **Restate** für Workflow-Orchestrierung
3. **NATS JetStream** für Event-Transport
4. **SIN-Supabase** für Control-Plane Projections
5. **HF Executors** als Stateless Worker
6. **Zeus → Hermes → SIN-Code** Pipeline für Planning → Dispatch → Execution

## ⚡ Powerup

Schnellstart-Guide für neue Team-Mitglieder:

```bash
# 1. Repos klonen
git clone https://github.com/OpenSIN-AI/OpenSIN.git
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
git clone https://github.com/OpenSIN-AI/OpenSIN-backend.git

# 2. Dependencies installieren
cd OpenSIN && npm install && npm run build
cd ../OpenSIN-Code && npm install

# 3. Backend starten
cd ../OpenSIN-backend && npm run dev

# 4. OpenSIN-Code starten
cd ../OpenSIN-Code && npm start

# 5. Dashboard öffnen
open http://localhost:3000
```

## 🏠 Self-Hosted Agents

OpenSIN kann vollständig self-hosted betrieben werden:

| Komponente | Self-Hosted Option |
|------------|-------------------|
| **Room-13** | Docker Compose auf OCI VM |
| **Supabase** | Self-hosted Supabase auf OCI |
| **NATS** | Docker Container auf OCI |
| **Restate** | Docker Container auf OCI |
| **Redis** | Docker Container auf OCI |
| **n8n** | Docker Container auf OCI |
| **HF Executors** | Lokale Docker Container |

**Mindestanforderungen:** 8 CPU, 32GB RAM, 200GB SSD

## 📊 Stargazers

OpenSIN Repositories nach Stars (Stand April 2026):

| Repo | Stars | Zweck |
|------|-------|-------|
| OpenSIN-backend | 973K | Backend & Fleet Control |
| OpenSIN | 833K | Core Platform |
| OpenSIN-Code | 354K | CLI & SIN-Stack |
| OpenSIN-CLI | 225K | Platform CLI |

## 🛑 Stop Failure Hook

Automatische Erkennung und Eskalation von fehlgeschlagenen Workflows:

```yaml
# .opensin/hooks.yaml
- name: stop-on-failure
  type: agent_state
  filter:
    state: failed
  action:
    type: webhook
    url: https://n8n.opensin.ai/webhook/failure
    timeout_seconds: 10
```

## 🔍 Transcript Search

Durchsuchung aller Agent-Transkripte:

```bash
# Suche nach spezifischem Begriff
opensin transcript search "PaymentIntent"

# Suche nach Agent
opensin transcript search --agent "sin-shop-logistic"

# Suche nach Zeitraum
opensin transcript search --since "2026-04-01" --until "2026-04-04"
```

## 📋 TRIAGE

Issue-Triage-Prozess:

| Priorität | Response Time | Escalation |
|-----------|---------------|------------|
| **P0 - Critical** | 15 Minuten | Sofort an Team Lead |
| **P1 - High** | 1 Stunde | Innerhalb 4 Stunden |
| **P2 - Medium** | 4 Stunden | Innerhalb 24 Stunden |
| **P3 - Low** | 24 Stunden | Nächster Sprint |

## 🎨 UX Security

Sicherheitsrichtlinien für die Benutzeroberfläche:

- **Keine Secrets in URLs** – Auth nur via Headers/Cookies
- **CSRF Protection** – Tokens für alle State-Changing Requests
- **XSS Prevention** – Content Security Policy, Input Sanitization
- **Clickjacking Protection** – X-Frame-Options, CSP frame-ancestors
- **Session Management** – Secure, HttpOnly, SameSite Cookies
- **Rate Limiting** – Pro-User und Pro-IP Limits

## 🔧 Refactor Backlog

Geplante Refactorings:

| Komponente | Grund | Priorität |
|------------|-------|-----------|
| `room-13-fastapi-coordinator` | Python → TypeScript Migration | Medium |
| `solver-18-survey-worker` | Telemetry Schema Normalisierung | High |
| `dashboard-enterprise` | Component Library Extraktion | Low |
| `workers/hf_executor_reference.py` | Multi-Language Support | Medium |

## 📝 Repair Docs

Prozess für kaputte Dokumentation:

1. **Issue erstellen** mit Label `docs-broken`
2. **Betroffene Dateien** auflisten
3. **Erwartetes Verhalten** beschreiben
4. **Screenshot** des Problems anhängen
5. **PR erstellen** mit korrigierter Doku

## 🧠 Knowledge

Zentrale Wissensdatenbank für OpenSIN:

- **Architektur-Entscheidungen** → ADRs
- **Best Practices** → Best Practices Doc
- **Troubleshooting** → Repair Docs + LaunchAgents Doc
- **API-Referenz** → API Reference Doc
- **Setup-Guides** → Getting Started + Powerup

## 📐 BLUEPRINT

OpenSIN Blueprint – Die Vision:

> **OpenSIN ist das erste AI Agent Operating System** – eine vollständig open-source, self-hostable Plattform zur Orchestrierung von AI-Agent-Flotten. Built for agents, by agents.

**Kernprinzipien:**
1. **A2A-First** – Agent-to-Agent Kommunikation ist das Fundament
2. **Open Source** – Transparent, community-driven, erweiterbar
3. **Self-Hosted** – Volle Kontrolle über Daten und Infrastruktur
4. **Production-Grade** – 24/7 autonom, fehlertolerant, skalierbar
5. **Zero Human Intervention** – Agenten lösen Probleme selbstständig

## 🔗 Verknüpfte Dokumentation

- [Architektur](./architecture.md) – Gesamtübersicht
- [ACP Protocol](./acp-protocol.md) – Kommunikationsprotokoll
- [Best Practices](./best-practices.md) – Entwicklungsstandards
- [Core Principles](./core-principles.md) – Unsere Leitlinien
