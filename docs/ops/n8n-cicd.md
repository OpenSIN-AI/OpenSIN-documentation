# 🚀 n8n CI/CD Pipeline

OpenSIN betreibt ein **autonomes CI/CD-System** basierend auf n8n und A2A-Agenten – keine GitHub Actions, kein Dependabot, kein manuelles Deployment.

## 📐 Architektur

```
┌──────────────────────────────────────────────────────────────┐
│                   n8n + A2A CI/CD Pipeline                    │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────────┐ │
│  │   GitHub     │    │   n8n Master │    │   A2A Agents   │ │
│  │   Webhook    │───→│   Workflow   │───→│   (Autonomous) │ │
│  │   (Push/PR)  │    │   (Router)   │    │                │ │
│  └──────────────┘    └──────────────┘    └────────────────┘ │
│                                              │                │
│                              ┌───────────────┼──────────────┐│
│                              │               │              ││
│                        ┌─────┴─────┐  ┌─────┴─────┐  ┌────┴───┐│
│                        │ CI/CD     │  │ Deploy    │  │Notify  ││
│                        │ Agent     │  │ Agent     │  │Agent   ││
│                        └───────────┘  └───────────┘  └────────┘│
└──────────────────────────────────────────────────────────────┘
```

## 🔄 Pipeline-Flow

### 1. GitHub Webhook → n8n

| Event | Trigger | Aktion |
|-------|---------|--------|
| `push` (any branch) | Code-Änderung | Lint + Test |
| `push` (main) | Merge to main | Lint + Test + Build + Deploy |
| `pull_request` | PR eröffnet | Lint + Test + Security Scan |
| `release` published | Release erstellt | Full Pipeline + Notify |

### 2. n8n Master Workflow

Das Master-Workflow (im `A2A-SIN-N8N` Repo) parsed das GitHub-Event und routed an den passenden A2A-Agenten:

```json
{
  "workflow": "n8n-master",
  "triggers": ["github_webhook"],
  "routes": {
    "push": "a2a-cicd-agent",
    "pull_request": "a2a-cicd-agent",
    "release": "a2a-deploy-agent"
  }
}
```

### 3. A2A CI/CD Agent

Der CI/CD-Agent ist autonom und führt folgende Stages aus:

| Stage | Befehl | Ziel |
|-------|--------|------|
| **Clone** | `git clone <repo>` | Repo klonen |
| **Detect** | Auto-detect (TypeScript/Python/Go) | Sprache/Framework erkennen |
| **Lint** | `bun lint` / `eslint` / `ruff` / `flake8` | Code-Qualität prüfen |
| **Test** | `bun test` / `pytest` / `vitest` | Tests mit Coverage |
| **Security** | `trivy` / `npm audit` / `bandit` | Vulnerability Scan |
| **Build** | `bun build` / `docker build` | Artefakt erstellen |
| **Deploy** | OCI CLI / HF CLI | Deploy wenn alle Stages grün |

### 4. A2A Deploy Agent

Deployt erfolgreiche Builds zu:

| Ziel | Methode | Trigger |
|------|---------|---------|
| **Hugging Face Spaces** | `hf push` + Docker | `main` push, alle Stages grün |
| **OCI (Oracle Cloud)** | `oci compute` CLI | `main` push, alle Stages grün |
| **Vercel** | `vercel deploy` | Frontend-Repos |

### 5. A2A Notification Agent

Berichtet Ergebnisse an:

| Kanal | Inhalt |
|-------|--------|
| **Telegram** | Pass/Fail-Status, Link zum PR/Build |
| **Discord** | Detaillierte Pipeline-Ergebnisse |
| **GitHub** | PR-Comment mit Check-Status |

## 🚫 KEINE GitHub Actions

OpenSIN nutzt **niemals** GitHub Actions:

| Verboten | Grund |
|----------|-------|
| `.github/workflows/ci.yml` | Ersetzt durch n8n + A2A CI/CD |
| `.github/dependabot.yml` | Ersetzt durch A2A Dependency Agent |
| `.github/workflows/deploy.yml` | Ersetzt durch A2A Deploy Agent |

**Regel:** Existierende GitHub-Actions-Dateien müssen aus allen Repos entfernt werden.

## 🤖 A2A Dependency Agent

Ersetzt Dependabot vollständig:

| Feature | Implementierung |
|---------|----------------|
| **Schedule** | Wöchentlich via n8n Cron |
| **Detection** | Prüft alle Repos auf veraltete Dependencies |
| **PR-Erstellung** | Erstellt PRs mit aktualisierten Versionen |
| **Auto-Merge** | Wenn Tests passieren → Auto-Merge |
| **Notification** | Telegram/Discord bei Updates |

## 🏛️ A2A Governance Agent

Erzwingt Branch-Protection:

| Regel | enforced |
|-------|----------|
| PR vor Merge zu `main` erforderlich | ✅ |
| CI/CD Pipeline muss passieren | ✅ |
| Mindestens 1 Approval erforderlich | ✅ |
| Keine Force Pushes zu `main` | ✅ |
| Kein Löschen von `main` | ✅ |

## 📁 Konfiguration

### n8n Webhook URL

Jedes Repo muss einen Webhook zu n8n konfigurieren:

```
https://n8n.opensin.ai/webhook/github
```

### Webhook Events

Folgende Events müssen subscribed sein:
- `push`
- `pull_request`
- `release`

### n8n Master Workflow

Das Workflow liegt im `A2A-SIN-N8N` Repo und enthält:
- GitHub Webhook Trigger
- Event Parser (JSON → strukturiert)
- Router (push → CI/CD, PR → CI/CD, release → Deploy)
- A2A Agent Dispatcher
- Error Handler + Retry Logic

## 🔗 Verknüpfte Dokumentation

- [Best Practices: CI/CD](./best-practices.md#6--cicd-n8n--a2a-pipeline)
- [Hugging Space Deployment](./best-practices.md#8--hugging-face-space-deployment)
- [A2A Fleet](./a2a-fleet.md)
