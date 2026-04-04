# 🖥️ OpenSIN Desktop App

Die OpenSIN Desktop App ist der geführte lokale Einstiegspunkt für Nutzer, die nicht am ersten Tag die gesamte Fleet-Architektur lernen müssen. Sie bündelt Installation, Dokumentation und Runtime in einer einzigen, benutzerfreundlichen Oberfläche.

## 📋 Aktueller Stand

- Der Desktop-App-Pfad ist in aktiver Entwicklung
- Der Shell-Installer bootstrapt bereits das Repository und die lokale Umgebung
- Die Desktop App konzentriert sich darauf, das System einfacher startbar, durchsuchbar und vertrauenswürdig zu machen

## 🎯 Was die App leisten soll

Die Desktop App soll drei Kernfragen schnell beantworten:

1. **Was ist OpenSIN?** – Eine kurze, verständliche Einführung in die A2A-Plattform
2. **Wie installiere/starte ich es?** – Ein-Klick-Installation mit dem bestehenden Bootstrapper
3. **Was mache ich als Nächstes?** – Geführte Next Steps: CLI starten, erstes Team erstellen, Docs lesen

## 🚀 Installationspfad

Der aktuelle Installations-Bootstrapper liegt im Backend-Repository:

```bash
curl -fsSL https://raw.githubusercontent.com/OpenSIN-AI/OpenSIN-backend/main/install.sh | bash
```

Dieser Weg ist der schnellste, um das lokale Repository, die Konfiguration und die Basis-Tooling-Umgebung vor dem vollständigen Desktop-Erlebnis vorzubereiten.

### Was der Installer macht

1. Klont `OpenSIN-Code` Repository
2. Installiert `opencode` CLI via Upstream-Sync
3. Erstellt `~/.config/opencode/` Verzeichnis mit Standard-Konfiguration
4. Installiert Node.js Dependencies (`npm install`)
5. Richtet OMOC Swarm Plugin ein
6. Verifiziert Installation mit `opencode --version`

## 🏗️ Architektur

```
┌─────────────────────────────────────────────────┐
│         OpenSIN Desktop App (Tauri)             │
├─────────────────────────────────────────────────┤
│  ┌───────────┐  ┌──────────┐  ┌──────────────┐ │
│  │ Dashboard │  │ Terminal │  │ Doc Browser  │ │
│  │           │  │          │  │              │ │
│  │ Teams     │  │ opencode │  │ Markdown     │ │
│  │ Agents    │  │ CLI      │  │ Renderer     │ │
│  │ Status    │  │ Session  │  │ Navigation   │ │
│  └─────┬─────┘  └────┬─────┘  └──────┬───────┘ │
├───────┴───────────────┴───────────────┴─────────┤
│              Tauri Core (Rust)                   │
│  ┌───────────────────────────────────────────┐  │
│  │  System Tray · Auto-Update · File System  │  │
│  │  Process Management · IPC Bridge          │  │
│  └───────────────────────────────────────────┘  │
├─────────────────────────────────────────────────┤
│         Install Bootstrapper                    │
│    (curl install.sh | bash)                     │
├─────────────────────────────────────────────────┤
│         Local Runtime Layer                     │
│   opencode CLI · SIN-Stack · MCPs · LaunchAgents│
└─────────────────────────────────────────────────┘
```

### Komponenten

| Komponente | Beschreibung | Tech |
|------------|--------------|------|
| **Dashboard** | Übersicht über installierte Teams, Agent-Status, Systemgesundheit | Tauri + Svelte/React |
| **Eingebetteter Terminal** | Direkter Zugriff auf die `opencode` CLI ohne externes Terminal | xterm.js + PTY |
| **Doc Browser** | Integrierte Ansicht der OpenSIN-Dokumentation | Markdown Renderer |
| **Install Manager** | GUI-Wrapper für den Shell-Bootstrapper mit Fortschrittsanzeige | Rust + Tauri Commands |
| **Team Hub** | Browse und installiere A2A-Teams aus dem Marktplatz | A2A Protocol |
| **System Tray** | Hintergrund-Status, Quick-Actions, Notifications | Tauri System Tray API |

## 💻 Technologie-Entscheidung: Tauri

| Framework | Vorteile | Nachteile |
|-----------|----------|-----------|
| **Electron** | Reifes Ökosystem, große Community | Höherer RAM-Verbrauch (~150MB+) |
| **Tauri** | Minimaler Footprint (~10MB), Rust-basiert, sicher | Jüngeres Ökosystem |
| **Neutralinojs** | Leichtgewichtig, kein Node.js | Begrenztere API |

**Entscheidung:** Tauri für minimalen Ressourcenverbrauch, da die App nah an der CLI arbeitet und kein schweres UI-Framework benötigt.

### Tauri Setup (für Entwickler)

```bash
# Rust installieren (falls nicht vorhanden)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Tauri CLI installieren
cargo install tauri-cli

# Projekt erstellen
mkdir opensin-desktop && cd opensin-desktop
npm create tauri-app

# Dependencies installieren
npm install

# Dev-Server starten
npm run tauri dev

# Production Build
npm run tauri build
```

### Tauri Konfiguration

```json
// tauri.conf.json
{
  "build": {
    "beforeBuildCommand": "npm run build",
    "beforeDevCommand": "npm run dev",
    "frontendDist": "../dist"
  },
  "app": {
    "windows": [{
      "title": "OpenSIN",
      "width": 1200,
      "height": 800,
      "resizable": true
    }]
  },
  "bundle": {
    "active": true,
    "targets": "all",
    "identifier": "ai.opensin.desktop",
    "icon": ["icons/32x32.png", "icons/128x128.png", "icons/icon.icns"]
  }
}
```

## 🗺️ Roadmap

### Phase 1: MVP (Aktuell)
- [x] Shell-Installer funktional
- [ ] Tauri Projekt-Grundgerüst
- [ ] Ein-Klick-Start für die CLI
- [ ] Integrierter Doc-Browser

### Phase 2: Integration
- [ ] Dashboard mit Agent-Status-Anzeige
- [ ] Team-Marktplatz-Browser
- [ ] Automatische Update-Prüfung
- [ ] Systemvoraussetzungs-Check

### Phase 3: Vollständige Erfahrung
- [ ] Visuelle Team-Konfiguration
- [ ] Echtzeit-Fleet-Übersicht
- [ ] Integriertes Debugging-Panel
- [ ] One-Click Bug Reports mit System-Info

## 🔗 Verknüpfte Dokumentation

- [Getting Started](./getting-started.md) – Ersteinrichtung
- [Architektur](./architecture.md) – Gesamtübersicht
- [OpenSIN-Code](./opensin-code.md) – CLI und SIN-Stack
- [LaunchAgents](./launchagents.md) – Hintergrund-Dienste
