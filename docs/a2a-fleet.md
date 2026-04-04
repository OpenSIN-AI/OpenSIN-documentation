# 🤖 A2A Agent Fleet

Das OpenSIN A2A (Agent-to-Agent) Fleet ist das Herzstück der Plattform — über 108 modulare Agenten, die nahtlos zusammenarbeiten.

## 📊 Fleet-Übersicht

| Kategorie | Anzahl | Status | Deployment |
|-----------|--------|--------|------------|
| Infrastructure | 6 | ✅ Live | Hugging Face Spaces (delqhi) |
| Teams | 8 | ✅ Live | Hugging Face Spaces (delqhi) |
| Apple | 14 | 🟡 Local | Structural |
| Security | 16 | 🟡 Structural | Structural |
| Code | 6 | 🟡 Structural | Structural |
| Social/Comms | 25+ | ✅ Live | Hugging Face Spaces (easeeeclip) |
| Forum | 8 | 🟡 Structural | Structural |
| Legal/Finance | 9 | 🟡 Structural | Structural |
| Specialized | 12+ | 🟡 Structural | Structural |
| **Platform Workers** | **13** | ✅ Live | sinInChrome + sin-computer-use |

## 🚀 Platform Agents (8) — easeeeclip Account

| Agent | HF Space | Status | Auth |
|-------|----------|--------|------|
| sin-reddit | `easeeeclip/sin-reddit` | ✅ RUNNING | ❌ Not logged in |
| sin-discord | `easeeeclip/sin-discord` | ✅ RUNNING | ❌ Not logged in |
| sin-youtube | `easeeeclip/sin-youtube` | ✅ RUNNING | ✅ 29 auth cookies |
| sin-tiktok | `easeeeclip/sin-tiktok` | ✅ RUNNING | ⚠️ Visited |
| sin-medium | `easeeeclip/sin-medium` | ✅ RUNNING | ❌ Not logged in |
| sin-instagram | `easeeeclip/sin-instagram` | ✅ RUNNING | ❌ Not logged in |
| sin-x-twitter | `easeeeclip/sin-x-twitter` | ❌ RUNTIME_ERROR | ✅ 4 auth cookies |
| sin-community | `easeeeclip/sin-community` | ✅ RUNNING | ✅ 5 auth cookies |

## 🚀 Platform Workers (13)

Alle 13 Worker mit sinInChrome + sin-computer-use Integration:

| Worker | Plattform | Dashboard |
|--------|-----------|-----------|
| Prolific | Academic studies | https://participant-app.prolific.com |
| Outlier | AI training tasks | https://www.outlier.ai |
| Clickworker | Micro tasks | https://www.clickworker.com |
| Appen | Data annotation | https://appen.com |
| Scale AI | AI evaluation | https://scale.com |
| Mindrift | AI tasks | https://mindrift.ai |
| OneForma | Data collection | https://www.oneforma.com |
| DataAnnotation | Data annotation | https://dataannotation.tech |
| YouGov | Surveys | https://yougov.com |
| Freecash | Offers & surveys | https://freecash.com |
| Karya | Microsoft data tasks | https://karya.microsoft.com |
| Meinungsstudie | German surveys | https://www.meinungsstudie.de |
| Surge AI | AI training data | https://www.surge.ai |

## ✅ A2A Completion Checklist

Ein Agent gilt erst als **fertig**, wenn alle Punkte erfüllt sind:

- [ ] Lokaler Build erfolgreich (`npm run build`)
- [ ] Agent Card korrekt (`print-card`)
- [ ] Help-Text vorhanden (`agent.help`)
- [ ] Health-Action antwortet (`/health` → 200)
- [ ] MCP-Server startet (`serve-mcp` bleibt alive)
- [ ] Fleet-Validation grün (`npm run test:a2a:fleet`)
- [ ] Live-Audit grün (`npm run test:a2a:live -- --agent <slug>`)
- [ ] Public Reachability bestätigt (`a2a.delqhi.com/agents/<slug>` → 200)
- [ ] HF Space running (`/<slug>.hf.space/health` → 200)
- [ ] Google Docs Child-Tab synchronisiert
- [ ] README.md mit Screenshot/Video
- [ ] Eigene `README.md` im Agent-Verzeichnis

## 🔗 Verknüpfte Dokumentation

- [Platform Auth](./platform-auth.md)
- [Auth Rotator](./auth-rotator.md)
- [Repository Catalog](./repository-catalog.md)
