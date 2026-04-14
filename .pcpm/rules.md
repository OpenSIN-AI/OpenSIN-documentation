# Project Rules
## 🚨 ABSOLUTES CI/CD VERBOT — KEINE GITHUB ACTIONS (PRIORITY -10.0 — HÖCHSTE REGEL, KEINE AUSNAHMEN) 🚨

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
