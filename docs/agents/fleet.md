# 🤖 A2A Agent Fleet

Das OpenSIN A2A (Agent-to-Agent) Fleet ist das Herzstück der Plattform – über 130 modulare Agenten, die nahtlos zusammenarbeiten.

## 📊 Fleet-Übersicht

| Kategorie | Anzahl | Status | Deployment |
|-----------|--------|--------|------------|
| Infrastructure | 6 | ✅ Live | Hugging Face Spaces |
| Teams | 8 | ✅ Live | Hugging Face Spaces |
| Apple | 13 | 🟡 Local | Structural |
| Security | 16 | 🟡 Structural | Structural |
| Code | 6 | 🟡 Structural | Structural |
| Social/Comms | 25+ | 🟡 Structural | Structural |
| Legal/Finance | 8 | 🟡 Structural | Structural |
| Specialized | 10+ | 🟡 Structural | Structural |

## 🏗️ Architektur

Jeder A2A-Agent folgt einem kanonischen Aufbau:

```
A2A-SIN-<Agent-Name>/
├── .opencode/
│   ├── opencode.json          # OpenCode MCP-Konfiguration
│   └── plugins/               # Optionale Plugins
├── clients/
│   └── opencode-mcp.json      # OpenCode Client Snippet
├── src/
│   ├── cli.ts                 # CLI-Einstiegspunkt
│   ├── metadata.ts            # Agent-Metadaten (PORT, HOST, publicBaseUrl)
│   └── actions/               # Agent-spezifische Aktionen
├── mcp-config.json            # MCP-Server-Konfiguration
├── card.json                  # A2A Agent Card
├── package.json               # @opensin/a2a-sin-<name>
├── .github/
│   ├── workflows/
│   │   ├── ci.yml             # CI/CD Pipeline
│   │   └── deploy-huggingface-space.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── Dockerfile                 # HF Space Deployment
└── README.md                  # HF-Space-fähige Dokumentation
```

## 🚀 Deployment-Pipeline

### Structural Agents (19 deployed)

Die Structural Agents sind auf Hugging Face Spaces deployed und über `a2a.delqhi.com/agents/<slug>` erreichbar:

| Agent | HF Space | Status |
|-------|----------|--------|
| sin-frontend | `delqhi/sin-frontend` | ✅ Running |
| sin-team-social | `delqhi/sin-team-social` | ✅ Running |
| sin-team-orchestrator | `delqhi/sin-team-orchestrator` | ✅ Running |
| sin-team-google-apps | `delqhi/sin-team-google-apps` | ✅ Running |
| sin-team-shop | `delqhi/sin-team-shop` | ✅ Running |
| sin-team-company | `delqhi/sin-team-company` | ✅ Running |
| sin-team-worker | `delqhi/sin-team-worker` | ✅ Running |
| sin-team-creator | `delqhi/sin-team-creator` | ✅ Running |
| sin-team-marketing | `delqhi/sin-team-marketing` | ✅ Running |
| sin-server | `delqhi/sin-server` | ✅ Running |
| sin-cloudflare | `delqhi/sin-cloudflare` | ✅ Running |
| sin-supabase | `delqhi/sin-supabase` | ✅ Running |
| sin-storage | `delqhi/sin-storage` | ✅ Running |
| sin-authenticator | `delqhi/sin-authenticator` | ✅ Running |
| sin-passwordmanager | `delqhi/sin-passwordmanager` | ✅ Running |
| sin-research | `delqhi/sin-research` | ✅ Running |
| sin-tiktok | `delqhi/sin-tiktok` | ✅ Running |
| sin-tiktok-shop | `delqhi/sin-tiktok-shop` | ✅ Running |
| sin-mindrift | `delqhi/sin-mindrift` | ✅ Running |

### Platform Agents (8) — easeeeclip Account

| Agent | HF Space | Status | Auth | Account |
|-------|----------|--------|------|---------|
| sin-reddit | `easeeeclip/sin-reddit` | ✅ RUNNING | ❌ Not logged in | easeeeclip (HF_API_9) |
| sin-discord | `easeeeclip/sin-discord` | ✅ RUNNING | ❌ Not logged in | easeeeclip (HF_API_9) |
| sin-youtube | `easeeeclip/sin-youtube` | ✅ RUNNING | ✅ 29 auth cookies | easeeeclip (HF_API_9) |
| sin-tiktok | `easeeeclip/sin-tiktok` | ✅ RUNNING | ⚠️ Visited, not logged in | easeeeclip (HF_API_9) |
| sin-medium | `easeeeclip/sin-medium` | ✅ RUNNING | ❌ Not logged in | easeeeclip (HF_API_9) |
| sin-instagram | `easeeeclip/sin-instagram` | ✅ RUNNING | ❌ Not logged in | easeeeclip (HF_API_9) |
| sin-x-twitter | `easeeeclip/sin-x-twitter` | ❌ RUNTIME_ERROR | ✅ 4 auth cookies | easeeeclip (HF_API_9) |
| sin-community | `easeeeclip/sin-community` | ✅ RUNNING | ✅ 5 auth cookies | easeeeclip (HF_API_9) |

> **Hinweis:** 8 Platform Agents erstellt am 2026-04-04 unter HF-Account `easeeeclip`. Token: `HF_API_9` in sin-passwordmanager. 7/8 Spaces RUNNING, x-twitter hat Launch Timeout (wird gefixt). Cookie-Auth via sin-platform-auth: 6/12 Plattformen eingeloggt im Chrome Profil.

### Apple A2A Fleet (12 Agenten)

| Agent | Zweck | MCP-Surface |
|-------|-------|-------------|
| SIN-Apple-Device-Control | App-Liste, App-Aktivierung, Screen Capture | AppleScript + System Events |
| SIN-Apple-Notifications | Local Notifications, Notification Center DB | `NSUserNotification` + SQLite |
| SIN-Apple-Calendar-Contacts | Kalender, Events, Kontakte | EventKit AppleScript |
| SIN-Apple-Notes | Notizen erstellen, suchen, auflisten | Notes.app AppleScript |
| SIN-Apple-Mobile | Device Discovery via `xcrun devicectl` / `idevice_id` | MobileDevice Bridge |
| SIN-Apple-Facetime | Call-State, Anruf starten/annehmen/beenden | FaceTime.app + Phone Automation |
| SIN-Apple-Mail | Mailbox, Inbox Summary, Drafts | Mail.app AppleScript |
| SIN-Apple-Reminders | Reminder-Listen, fällige Items, erstellen | Reminders.app AppleScript |
| SIN-Apple-Photos-Files | Recent Photos, Files, Finder Reveal | Photos.app + Finder AppleScript |
| SIN-Apple-Safari-WebKit | Tabs, URL öffnen, Front Tab Inspect | Safari AppleScript |
| SIN-Apple-System-Settings | Deep Links, Settings öffnen | System Settings AppleScript |
| SIN-Apple-Shortcuts | Shortcuts auflisten, Ordner, ausführen | Shortcuts.app AppleScript |

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

- [OpenSIN-Code Struktur](./opensin-code.md)
- [Architektur](./architecture.md)
- [Best Practices](./best-practices.md)
