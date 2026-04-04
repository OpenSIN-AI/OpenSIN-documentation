# 🏗️ Architektur & Repositories

Die Architektur von **OpenSIN** ist zu 100% modular, leicht verständlich und auf Enterprise-Niveau (aber Open Source!) gebaut.

Wir betreiben **130+ Git-Repositories**, die nahtlos ineinandergreifen.

---

## 📐 Gesamtarchitektur

```
┌──────────────────────────────────────────────────────────────────┐
│                         OpenSIN Ecosystem                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────┐    ┌────────────┐    ┌──────────────────────┐   │
│  │  Frontend  │    │  Backend   │    │   OpenSIN-Code CLI   │   │
│  │  (OpenSIN) │◄──►│ (Supabase) │◄──►│   (opencode + OMOC)  │   │
│  │ a2a.delqhi │    │  Auth/DB   │    │   SIN-Stack + MCPs   │   │
│  └────────────┘    └────────────┘    └──────────┬───────────┘   │
│                                                  │               │
│                                   ┌──────────────┴──────────┐   │
│                                   │   A2A Agent Fleet       │   │
│                                   │   (130+ Agenten)        │   │
│                                   │                         │   │
│                                   │ ┌─────┐ ┌─────┐ ┌─────┐ │   │
│                                   │ │Infra│ │Teams│ │Apple│ │   │
│                                   │ └─────┘ └─────┘ └─────┘ │   │
│                                   │ ┌─────┐ ┌─────┐ ┌─────┐ │   │
│                                   │ │Sec  │ │Code │ │Social│ │   │
│                                   │ └─────┘ └─────┘ └─────┘ │   │
│                                   └─────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Automation & Infrastructure                  │   │
│  │  Auth Rotator · OMOC Swarm · SIN-Terminal · LaunchAgents │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 💻 1. Das Frontend (Die User-Oberfläche)

*   [**OpenSIN-AI/OpenSIN**](https://github.com/OpenSIN-AI/OpenSIN)
    *   **Zweck:** Das User Dashboard / Web-Oberfläche.
    *   **URL:** Aktuell `a2a.delqhi.com`, wird zu `chat.opensin.ai`.
    *   **Deployment:** Vercel (Custom Domain `a2a.delqhi.com` mit SSL).
    *   **Besonderheit:** Komplett Open Source. Zeigt alle A2A-Agenten mit Status, Cards und Endpoints.

## ⚙️ 2. Das Backend (Daten & Kontrolle)

*   [**OpenSIN-AI/OpenSIN-backend**](https://github.com/OpenSIN-AI/OpenSIN-backend)
    *   **Zweck:** Die Datenbank (Supabase), Authentifizierung und das Fleet-Management der Open-Source-Version.
    *   **Installations-Bootstrapper:** `curl -fsSL https://raw.githubusercontent.com/OpenSIN-AI/OpenSIN-backend/main/install.sh | bash`
*   **MyOpenSIN (Closed Repo)**
    *   **Zweck:** Die Abo-Version von OpenSIN mit exklusiven Features für Enterprise-Kunden.
    *   **Zugang:** Nur für autorisierte Team-Mitglieder. Der Quellcode ist nicht öffentlich.
    *   **Features:** Erweiterte Agent-Teams, Premium-MCPs, erweiterte Analytics und Prioritäts-Support.
    *   **Marktplatz-Integration:** Direkt verknüpft mit `website-my.opensin.ai` für den Kauf und die Verwaltung von Abo-Paketen.

## 🌐 3. Die Websites (Marktplatz & Landing Pages)

*   [**OpenSIN-AI/website-opensin.ai**](https://github.com/OpenSIN-AI/website-opensin.ai)
    *   **Zweck:** Die offizielle Landingpage für die Open-Source-Version.
*   [**OpenSIN-AI/website-my.opensin.ai**](https://github.com/OpenSIN-AI/website-my.opensin.ai)
    *   **Zweck:** Die Abo-Modell-Website (MyOpenSIN).
    *   **Marktplatz:** Endnutzer kaufen hier modulare A2A-Teams (z. B. `Team-SIN-Google` für 3,99 €/Monat, `Team-SIN-BugBounty` für 16 €/Monat) oder nutzen kostenlose Teams (z. B. `Team-SIN-Apple`).
    *   **Design-Standard:** Enterprise-Niveau im selben Stil wie die Open-Source-Website.

## 🛠️ 4. Der Motor (Die CLI & Agenten)

*   [**OpenSIN-AI/OpenSIN-Code**](https://github.com/OpenSIN-AI/OpenSIN-Code)
    *   **Zweck:** `opencode` CLI + der gesamte SIN-Stack.
    *   **Inhalt:** Eigene Plugins (`SIN-Plugins`), originale Plugins (`OC-Plugins`), MCP-Server (`MCPs`), Tools (`Tools`), Skills (`Skills`), Watcher und Wrapper.
    *   **Dokumentationspflicht:** *Alles* in diesem Verzeichnis erhält eine eigene, visuelle Markdown-Datei! Siehe dazu [Die OpenSIN-Code Struktur](./opensin-code.md).

## 🤖 5. A2A Agent Fleet

Das A2A Fleet besteht aus 130+ Agenten in 8 Kategorien. 19 Structural Agents sind live auf Hugging Face Spaces deployed.

*   **Infrastructure (6):** SIN-Server, SIN-Cloudflare, SIN-Supabase, SIN-Storage, SIN-Authenticator, SIN-PasswordManager
*   **Teams (8):** SIN-Team-Orchestrator, SIN-Team-Social, SIN-Team-Google-Apps, SIN-Team-Shop, SIN-Team-Company, SIN-Team-Worker, SIN-Team-Creator, SIN-Team-Marketing
*   **Apple (13):** Device-Control, Notifications, Calendar/Contacts, Notes, Mobile, FaceTime, Mail, Reminders, Photos/Files, Safari/WebKit, System Settings, Shortcuts, iMessage
*   **Security (16):** Recon, Fuzz, Audit, Web, Network, Mobile, Auth, Crypto, Social, Cloud, AI, Malware, IoT, Forensics, RedTeam, Exploit
*   **Code (6):** Security, DevOps, DataScience, AI, Database, Integration
*   **Social/Comms (25+):** X/Twitter, Reddit, Discord, YouTube, TikTok, Instagram, LinkedIn, Telegram, WhatsApp, Signal, Google-Chat, Email + weitere
*   **Legal/Finance (8):** Tax, Contract, Compliance, Evidence, Damages, ClaimWriter, Paragraph, Summary
*   **Specialized (10+):** BugBounty, Research, N8N, GitHub-Action, Stripe, Patents + weitere

→ Siehe [A2A Fleet Dokumentation](./a2a-fleet.md) für Details.

## 🔄 6. Automation & Auth Rotator

Zwei autonome Systeme rotieren Model-Quotas automatisch:

*   **openAntigravity-auth-rotator:** Rotiert Google Workspace Accounts bei Antigravity-Quota-Erschöpfung (Claude + Gemini)
    *   → [Auth Rotator Dokumentation](./auth-rotator.md)
*   **opencodex-auth-rotator:** Rotiert OpenAI Accounts bei GPT-Quota-Erschöpfung
    *   → [Auth Rotator Dokumentation](./auth-rotator.md)

## 🎯 7. OMOC Swarm & OpenCode

OMOC (Oh My OpenCode) ist der Swarm Coordinator für Multi-Agent-Delegation:

*   **Globale Konfiguration:** `~/.config/opencode/opencode.json` + `oh-my-opencode.json`
*   **Swarm Plugin:** `~/.config/opencode/plugins/omoc-swarm.ts`
*   **A2A MCP-Integration:** Alle kanonischen Agenten sind als MCP-Server registriert
*   **SIN-Terminal:** Orchestriert sichtbare macOS-Terminals und delegiert an parallele OpenCode-Sessions

→ Siehe [OMOC Swarm Dokumentation](./omoc-swarm.md) für Details.

## 📚 8. Die Community & Docs

*   [**OpenSIN-AI/documentation**](https://github.com/OpenSIN-AI/OpenSIN-documentation)
    *   **Zweck:** *Genau das, was du gerade liest!* Internes Onboarding, Quereinsteiger-Hilfen, Team-Manuals.
*   [**OpenSIN-AI/global-dev-docs-standard**](https://github.com/OpenSIN-AI/global-dev-docs-standard)
    *   **Zweck:** Unser weltweiter Standard für Dokumentation. Jedes Repo muss diesem Standard folgen.
*   [**OpenSIN-AI/OpenSIN-Marketing-Strategy**](https://github.com/OpenSIN-AI/OpenSIN-Marketing-Strategy)
    *   **Zweck:** Marketing-Diskussionen, Release-Planung etc. (Findet hauptsächlich über [GitHub Discussions](https://github.com/orgs/OpenSIN-AI/discussions) statt).

## 🖥️ 9. Desktop App & VS Code Extension

*   **Desktop App:** Geführter lokaler Einstiegspunkt mit Install-Manager, Dashboard und Doc-Browser
    *   → [Desktop App Dokumentation](./desktop-app.md)
*   **VS Code Extension (SIN Code):** Agentic AI Coding Assistant mit Sidebar Chat, Swarm Coordinator, Buddy Gamification und Agent Marketplace
    *   → [VS Code Extension Dokumentation](./opensin-vscode-extension/README.md)

---

> **Ein Bild sagt mehr als tausend Worte:** Verlinke bei jeder Architektur-Diskussion oder einem neuen PR direkt auf visuelle Flowcharts oder kurze Video-Erklärungen, damit jedes Teammitglied sofort versteht, wo die Neuerung platziert ist!
