# 🔧 Refactor Backlog

Automatisch generierte Priorisierung (Stand: 2026-03-25).

## Top 10 Refactoring-Kandidaten

| Priority | Service | LOC | Risk | Grund |
|----------|---------|-----|------|-------|
| 1 | sin-survey-worker | 1.082.983 | 7 | Größter Service, höchstes Risiko |
| 2 | sin-solver-enterprise-dashboard | 88.783 | 5 | Dashboard-Komplexität |
| 3 | scira (room-30-scira-ai-search) | 82.479 | 5 | Search-Engine-Kern |
| 4 | memu | 19.408 | 5 | Memory-System |
| 5 | room-13-fastapi-coordinator | 6.660 | 4 | Ingress-API |
| 6 | agent-10-work-os | 5.925 | 4 | Work OS Integration |
| 7 | delqhi-platform-clawdbot | 4.457 | 4 | Messenger-Plattform |
| 8 | solver-19-captcha-solver | 3.843 | 3 | CAPTCHA-Infrastruktur |
| 9 | browser-captcha-worker | 2.550 | 3 | Browser-Worker |
| 10 | delqhi-platform-website-worker | 2.517 | 3 | Website-Builder |

## Lifecycle Exclusions (Geplant, nicht aktiv)

- services/workers, services/authd, services/nodriver-service, services/mcp-wrappers
- services/extensions, services/integrations, services/work-os, services/modules
- services/infrastructure, services/memu-server, services/auth-core
- services/provider-huggingface, services/provider-github, services/provider-discord, services/provider-x
- services/supabase, services/n8n-workflows, services/monitoring

## Drift Checks

- [ ] Root README Runtime Architecture gegen `docker-compose.yml` prüfen
- [ ] Jeder aktive Service braucht `service.manifest.json`
- [ ] Aktive Service Contracts müssen `/health`, `/ready`, `/version`, `/metrics` haben
- [ ] Generierte Artefakte müssen von `artifact-policy.json` + Janitor verwaltet werden

## 🔗 Verknüpfte Dokumentation

- [Testing & Database](./testing-environment-database.md) – Testing Guide
- [OpenSIN Packages](./opensin-packages.md) – Alle Packages
