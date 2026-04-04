# 🚀 n8n Workflows — Documentation

> **Stand:** 2026-04-04 | **Total Workflows:** 22 active | **Source:** OpenSIN-backend/n8n-workflows/

## Active Workflows

| # | Workflow | Trigger | Purpose |
|---|----------|---------|---------|
| 1 | [Global Fleet Self-Healing Protocol](./n8n-fleet-self-healing.md) | — | Automatisches Self-Healing der A2A Flotte bei Fehlern und Incidents |
| 2 | [GitHub @opnsin-code Mention → Auto-Delegate](./n8n-github-mention-auto-delegation.md) | — | Auto-Delegation bei GitHub @opnsin-code Mentions |
| 3 | [Hugging Face Keep-Alive Pinger](./n8n-hf-keepalive.md) | — | HF Spaces wachhalten durch periodische Pings (alle 6h) |
| 4 | [OpenSIN-AI Issue Watcher + Auto-Delegation](./n8n-issue-watcher-auto-delegation.md) | — | GitHub Issues überwachen und automatisch an A2A Agents delegieren |
| 5 | [SIN-Fleet Incident Watcher (Telegram -> Hermes)](./n8n-telegram-incident-watcher.md) | — | Incident-Weiterleitung von Telegram an Hermes Dispatcher |
| 6 | [Token Pool Monitor](./n8n-token-pool-monitor.md) | — | Token Pool überwachen und bei Bedarf nachfüllen |
| 7 | [YouTube Playlist → GitHub Issues Watcher](./n8n-youtube-playlist-watcher.md) | — | YouTube Playlist überwachen und neue Videos als GitHub Issues erstellen |

## Workflow JSON Files

```
OpenSIN-backend/n8n-workflows/
├── fleet-self-healing.json
├── github-mention-auto-delegation.json
├── hf-keepalive.json
├── issue-watcher-auto-delegation.json
├── telegram-incident-watcher.json
├── token-pool-monitor.json
└── youtube-playlist-watcher.json
```

---

*Last updated: 2026-04-04 by SIN-Zeus*