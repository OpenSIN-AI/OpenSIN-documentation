# 💎 MyOpenSIN (Enterprise / Abo-Version)

MyOpenSIN ist die kommerzielle Abo-Version von OpenSIN mit exklusiven Features für Enterprise-Kunden.

## 📋 Überblick

| Aspekt | OpenSIN (Open Source) | MyOpenSIN (Abo) |
|--------|----------------------|-----------------|
| **Preis** | Kostenlos | Modular ab 3,99 €/Monat |
| **Code** | Open Source (MIT) | Closed Source |
| **Agent-Teams** | Basis-Teams | Premium-Teams + Custom |
| **MCPs** | Community MCPs | Premium MCPs |
| **Support** | Community (Discussions) | Prioritäts-Support |
| **Analytics** | Basis | Erweitert |
| **Deployment** | Selbst (HF Spaces) | Managed |

## 🛒 Marktplatz-Modell

Endnutzer kaufen modulare A2A-Teams auf `website-my.opensin.ai`:

| Team | Preis | Inhalt |
|------|-------|--------|
| **Team-SIN-Google** | 3,99 €/Monat | Google Workspace Integration (Gmail, Drive, Calendar, Docs) |
| **Team-SIN-Apple** | Kostenlos | Apple-Integration (iMessage, Calendar, Notes, Reminders) |
| **Team-SIN-BugBounty** | 16 €/Monat | Security-Testing (Recon, Fuzz, Audit, Web, Network) |
| **Team-SIN-Social** | 9,99 €/Monat | Social Media Management (X, Reddit, Discord, YouTube, TikTok) |
| **Team-SIN-DevOps** | 12 €/Monat | DevOps-Automation (CI/CD, Docker, Cloud, Monitoring) |
| **Team-SIN-Creator** | 7,99 €/Monat | Content Creation (Text, Bild, Video, Audio) |
| **Team-SIN-Company** | 29,99 €/Monat | Full Enterprise Suite (alle Teams + Custom Agents) |

## 🏗️ Architektur

```
┌──────────────────────────────────────────────────────────────┐
│                        MyOpenSIN                              │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────┐    ┌─────────────────┐                  │
│  │ website-my.     │    │   MyOpenSIN     │                  │
│  │ opensin.ai      │    │   Backend       │                  │
│  │ (Marktplatz)    │◄──►│   (Closed)      │                  │
│  │                 │    │                 │                  │
│  │ - Team-Kauf     │    │ - Abo-Verwaltung│                  │
│  │ - Preis-Modelle │    │ - Billing       │                  │
│  │ - Dashboard     │    │ - Team-Provision│                  │
│  └─────────────────┘    └────────┬────────┘                  │
│                                  │                            │
│                     ┌────────────┴────────────┐              │
│                     │   Premium A2A Fleet     │              │
│                     │                         │              │
│                     │ ┌─────────────────────┐ │              │
│                     │ │ Premium MCPs        │ │              │
│                     │ │ Erweiterte Agenten  │ │              │
│                     │ │ Custom Integrations │ │              │
│                     │ │ Analytics Engine    │ │              │
│                     │ └─────────────────────┘ │              │
│                     └─────────────────────────┘              │
└──────────────────────────────────────────────────────────────┘
```

## 🔗 Integration mit Open Source

MyOpenSIN baut auf dem Open-Source-Fundament auf:

| Open-Source-Komponente | MyOpenSIN-Erweiterung |
|------------------------|----------------------|
| OpenSIN-Code CLI | Premium-Modelle (GPT-4, Claude Opus) |
| A2A Fleet (Basis) | Premium-Teams mit erweiterten Fähigkeiten |
| Community MCPs | Proprietäre MCPs für Enterprise-Integrationen |
| OpenSIN Dashboard | Erweiterte Analytics + Team-Management |
| Auth Rotator | Managed Token-Rotation (kein Setup nötig) |

## 🎯 Zielgruppen

| Zielgruppe | Empfohlenes Paket |
|------------|------------------|
| **Einzelentwickler** | Team-SIN-Google (3,99 €) oder Team-SIN-Apple (gratis) |
| **Small Teams (2-10)** | Team-SIN-DevOps (12 €) + Team-SIN-Creator (7,99 €) |
| **Security-Firmen** | Team-SIN-BugBounty (16 €) |
| **Marketing-Agenturen** | Team-SIN-Social (9,99 €) + Team-SIN-Creator (7,99 €) |
| **Enterprise (10+)** | Team-SIN-Company (29,99 €) |

## 📈 Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| 1 | Marktplatz-Website live | ✅ Live |
| 2 | Stripe-Integration | ✅ Live |
| 3 | Team-Provisioning (automatisch) | 🟡 In Entwicklung |
| 4 | Custom Agent Builder | 🟡 Geplant |
| 5 | Enterprise SSO | 🔴 Geplant |
| 6 | SLA-Garantien | 🔴 Geplant |

## 🔗 Verknüpfte Dokumentation

- [Architektur](./architecture.md) – Gesamtübersicht
- [A2A Fleet](./a2a-fleet.md) – Verfügbare Agent-Teams
- [Getting Started](./getting-started.md) – Open-Source-Einstieg
