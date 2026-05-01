# Project Rules

## 🚨 ABSOLUTES CI/CD VERBOT — KEINE GITHUB ACTIONS (PRIORITY -10.0 — HÖCHSTE REGEL, KEINE AUSNAHMEN) 🚨

- [2026-04-14T17:00:00Z] DYNAMIC AGENT DISCOVERY PFLICHT! VOR jeder Aufgabe: `node /Users/jeremy/dev/global-brain/src/engines/discover-agents.js` ausfuehren. Registry unter .pcpm/agent-registry.json lesen. byTrigger/byCapability Indexe nutzen. NIEMALS statische Listen! NEUE Agenten werden AUTOMATISCH erkannt. (priority: -9.0)
- [2026-04-14T16:30:00Z] A2A-SIN AGENT ROUTING PFLICHT! Jeder Agent MUSS bei jeder Aufgabe sofort prüfen: Welcher A2A-SIN-Agent ist dafür zuständig? Delegation MUSS automatisch erfolgen — User muss es NICHT extra sagen! Google Docs → A2A-SIN-Google-Apps, Passwörter → A2A-SIN-PasswordManager, Code → Team-SIN-Code-\*, etc. (priority: -9.0)
- [2026-04-14T18:30:00Z] BOX STORAGE DEFAULT: All logs, screenshots, videos, reports MUST use A2A-SIN-Box-Storage (room-09). GitLab LogCenter is DEPRECATED. Use `BOX_STORAGE_API_KEY` env var. Migration deadline: 2026-05-01. (priority: 00)

**KEINE GITHUB ACTIONS FÜR CI/CD, DEPLOYMENT ODER AUTOMATION!**

- OpenSIN-AI nutzt **AUSSCHLIESSLICH A2A-SIN-GitHub-Action + n8n** für alle CI/CD, Deployment, Build, Test und Automation Tasks.
- GitHub Actions Workflows (`.github/workflows/*.yml`) sind **PERMANENT VERBOTEN**.
- Der n8n-Router auf der OCI VM (`92.5.60.87:5678`) ist unser zentrales Automation-Backend.
- A2A-SIN-GitHub-Action ist unser GitHub Event Listener und n8n Bridge.
- Wer GitHub Actions erstellt oder vorschlägt: **Protokollverstoß**.

## Global Rules (synced from AGENTS.md)

- [2026-04-13T14:00:00Z] Images MUST be opened in macOS Preview.app — never tell users to check /tmp (priority: -4.5)
- [2026-04-13T14:00:00Z] Auto-sync after every chat turn via sync-chat-turn hook (priority: -4.0)

## Project-Specific Rules

- All architecture docs must include code examples and diagrams
- New features must have corresponding documentation pages
- VitePress config.js must be updated when adding new pages
