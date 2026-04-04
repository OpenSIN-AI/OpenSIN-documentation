# 🔗 SIN-Chatroom + Matrix + Messenger Bridges — Architektur-Plan

**Issue:** #625  
**Datum:** 2026-04-04  
**Status:** Planung abgeschlossen, Implementation bereit

---

## 1. IST-Zustand

### Vorhandene Repos (22)
| Repo | Typ | Status |
|------|-----|--------|
| A2A-SIN-Chatroom | Hub (docker-compose) | ✅ Code da, nicht deployed |
| A2A-SIN-Matrix | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Beeper | A2A Agent | ✅ Scaffolded |
| A2A-SIN-WhatsApp | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Telegram | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Signal | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Discord | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Teams | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Zoom | A2A Agent | ✅ Scaffolded |
| A2A-SIN-WebChat | A2A Agent | ✅ Scaffolded |
| A2A-SIN-IRC | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Feishu | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Google-Chat | A2A Agent | ✅ Scaffolded |
| A2A-SIN-LINE | A2A Agent | ✅ Scaffolded |
| A2A-SIN-Nostr | A2A Agent | ✅ Scaffolded |
| A2A-SIN-SMS | A2A Agent | ✅ Scaffolded |
| A2A-SIN-WeChat | A2A Agent | ✅ Scaffolded |
| A2A-SIN-BlueBubbles | A2A Agent | ✅ Scaffolded |
| A2A-SIN-iMessage | A2A Agent | ✅ Scaffolded |
| OpenSIN-TelegramBot-CLI | CLI Tool | ✅ Existiert |
| OpenSIN-Create-TelegramBot-Skill | Skill | ✅ Existiert |
| Template-A2A-SIN-TelegramBot | Template | ✅ Existiert |

### Chatroom docker-compose.yml (bestehend)
```
Services:
├── synapse (Matrix Homeserver) — Port 8008
├── element (Web Client) — Port 8080
├── whatsapp-bridge (mautrix-whatsapp)
├── telegram-bridge (mautrix-telegram)
├── signal-bridge (mautrix-signal)
├── discord-bridge (mautrix-discord)
├── slack-bridge (mautrix-slack)
├── instagram-bridge (mautrix-instagram)
├── irc-bridge (matrix-appservice-irc)
├── email-bridge (matrix-appservice-email)
└── cloudflared (Tunnel)
```

---

## 2. Ziel-Architektur

### 3-Schichten-Modell

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SCHICHT 1: USER INTERFACE                        │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ Element  │  │ Mobile   │  │ CLI      │  │ WebChat          │   │
│  │ Web:8080 │  │ Apps     │  │ Terminal │  │ Browser          │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │              │                 │              │
└───────┼──────────────┼──────────────┼─────────────────┼─────────────┘
        │              │              │                 │
        ▼              ▼              ▼                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    SCHICHT 2: MATRIX BACKBONE                       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Synapse Homeserver (chat.opensin.ai)            │  │
│  │  - User Management                                           │  │
│  │  - Room Management                                           │  │
│  │  - Federation                                                │  │
│  │  - End-to-End Encryption                                     │  │
│  └──────────────────────┬───────────────────────────────────────┘  │
│                         │                                           │
│  ┌──────────────────────┴───────────────────────────────────────┐  │
│  │              Bridge Layer (mautrix + appservices)            │  │
│  │  ┌────────┐ ┌────────┐ ┌───────┐ ┌────────┐ ┌────────────┐ │  │
│  │  │WhatsApp│ │Telegram│ │Signal │ │Discord │ │Instagram   │ │  │
│  │  └────────┘ └────────┘ └───────┘ └────────┘ └────────────┘ │  │
│  │  ┌────────┐ ┌──────┐ ┌─────┐ ┌────────┐ ┌──────────────┐ │  │
│  │  │Slack   │ │ IRC  │ │Email │ │iMessage│ │ BlueBubbles  │ │  │
│  │  └────────┘ └──────┘ └─────┘ └────────┘ └──────────────┘ │  │
│  │  ┌────────┐ ┌──────┐ ┌─────┐ ┌───────┐ ┌──────────────┐ │  │
│  │  │WeChat  │ │ LINE │ │SMS  │ │Nostr  │ │ Google-Chat  │ │  │
│  │  └────────┘ └──────┘ └─────┘ └───────┘ └──────────────┘ │  │
│  │  ┌────────┐ ┌──────┐ ┌─────┐ ┌───────┐                   │  │
│  │  │Teams   │ │ Zoom │ │Beeper│ │Feishu │                   │  │
│  │  └────────┘ └──────┘ └─────┘ └───────┘                   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────┬──────────────────────────────┘
                                       │ Matrix Client-Server API
                                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    SCHICHT 3: A2A AGENT LAYER                       │
│                                                                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                   │
│  │A2A-SIN     │  │A2A-SIN     │  │A2A-SIN     │  ← 18+ Agenten   │
│  │WhatsApp    │  │Telegram    │  │Discord     │     (separate     │
│  │Agent       │  │Agent       │  │Agent       │      Repos)        │
│  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘                   │
│        │               │               │                            │
│        └───────────────┼───────────────┘                            │
│                        ▼                                            │
│              ┌─────────────────┐                                    │
│              │  Supabase DB    │  ← Shared State                    │
│              │  92.5.60.87     │     - Messages                     │
│              │  :54321         │     - User Mappings                │
│              └────────┬────────┘     - Bridge Status               │
│                       │                                             │
│              ┌────────┴────────┐                                    │
│              │  n8n Workflows  │  ← Automation                     │
│              │  92.5.60.87     │     - Keep-Alive                  │
│              │  :5678          │     - Health Checks               │
│              └─────────────────┘     - Alerting                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Implementierungs-Phasen

### Phase 1: Matrix Server (Woche 1)
- [ ] OCI VM vorbereiten (92.5.60.87)
- [ ] Synapse Homeserver installieren + konfigurieren
- [ ] Domain `chat.opensin.ai` via Cloudflare DNS
- [ ] SSL/TLS mit Let's Encrypt
- [ ] Element Web Client deployen
- [ ] Admin User erstellen
- [ ] Federation mit öffentlichem Matrix aktivieren

### Phase 2: Bridges (Woche 2)
- [ ] Für jede Bridge: Registration File generieren
- [ ] Bridge Config mit Synapse verknüpfen
- [ ] Auth Tokens besorgen:
  - WhatsApp: Phone Number + QR Code Scan
  - Telegram: Bot Token von @BotFather
  - Signal: Phone Number + Verification Code
  - Discord: Bot Token + OAuth2
  - Slack: App Token + Bot Token
  - Instagram: Facebook App Credentials
  - iMessage: BlueBubbles Server auf Mac
- [ ] Test: User kann sich via jeder Bridge einloggen

### Phase 3: A2A Integration (Woche 3)
- [ ] Jeden Messenger-Agenten mit Matrix Room verbinden
- [ ] A2A Protocol: Agent ↔ Matrix Bridge Kommunikation
- [ ] Message Routing: Matrix Event → A2A Action → Response
- [ ] Supabase Schema für Bridge State
- [ ] Health Endpoint pro Bridge

### Phase 4: Deployment (Woche 4)
- [ ] docker-compose auf OCI VM deployen
- [ ] Cloudflare Tunnel konfigurieren
- [ ] HF Space Fallback erstellen
- [ ] Keep-Alive via n8n
- [ ] Monitoring Dashboard

### Phase 5: Testing (Woche 5)
- [ ] End-to-End Test pro Bridge
- [ ] Lasttest: 100 gleichzeitige Nachrichten
- [ ] Failover Test: Bridge down → Recovery
- [ ] Security Audit: E2E Encryption

---

## 4. Ressourcen

### OCI VM (92.5.60.87)
- CPU: 4 Core
- RAM: 24 GB
- Storage: 200 GB
- Bereits laufend: Supabase (:54321), n8n (:5678)

### Ports
| Service | Port | Protocol |
|---------|------|----------|
| Synapse | 8008 | HTTP |
| Synapse TLS | 8448 | HTTPS (Federation) |
| Element | 8080 | HTTP |
| WhatsApp Bridge | 29318 | HTTP |
| Telegram Bridge | 29319 | HTTP |
| Signal Bridge | 29320 | HTTP |
| Discord Bridge | 29321 | HTTP |
| Supabase | 54321 | HTTP |
| n8n | 5678 | HTTP |

### Domains
- `chat.opensin.ai` → Synapse + Element
- `a2a.delqhi.com` → A2A Endpoints
- Cloudflare Tunnel für Public Access

---

## 5. Risiken & Blocker

| Risiko | Impact | Lösung |
|--------|--------|--------|
| WhatsApp Bridge benötigt Phone Number | Medium | Dedizierte SIM Karte |
| iMessage Bridge benötigt Mac | Medium | BlueBubbles auf bestehendem Mac |
| Signal Bridge: Phone Verification | Low | Einmalige Verifikation |
| HF Space Rate Limit (20/Tag) | Low | OCI VM als Primary, HF als Fallback |
| Synapse Memory Usage | Medium | 24 GB RAM auf OCI VM ausreichend |
