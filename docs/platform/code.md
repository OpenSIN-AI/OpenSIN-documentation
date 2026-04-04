# 💻 OpenSIN-Code: Das Herzstück unserer KI-Flotte

Willkommen im Verzeichnis für **OpenSIN-Code**! Hier lebt unsere Kommandozeilen-Infrastruktur, die `opencode` CLI, und das gesamte **SIN-Stack** Ökosystem.

Dies ist die Basis für alle A2A (Agent-to-Agent) Teams, egal ob für unsere kostenlose Open-Source-Version oder die Enterprise-Abo-Pakete auf `website-my.opensin.ai`.

---

## 📂 Verzeichnisstruktur

Das Repository [**OpenSIN-Code**](https://github.com/OpenSIN-AI/OpenSIN-Code) ist streng modular aufgebaut. **Jedes Element bekommt seine eigene `README.md`** als ultimativen Quickstart für neue Team-Mitglieder!

### 1. Die CLI & Upstream Sync

| Pfad | Zweck | Wichtig |
|------|-------|---------|
| `OpenSIN-Code/readme.md` | Haupteinleitung, Setup, Befehle, Troubleshooting | Erster Anlaufpunkt |
| `OpenSIN-Code/OpenCode/` | Originale `opencode` CLI (Upstream) | **Niemals manuell ändern** – wird beim Sync überschrieben |
| `OpenSIN-Code/sync-upstream.sh` | Sync-Skript für Upstream-Updates | Zieht Updates ohne unsere Configs zu überschreiben |

**Upstream-Sync Workflow:**
```bash
cd OpenSIN-Code
./sync-upstream.sh
# Prüft auf neue opencode-Version, merged ohne unsere Configs zu überschreiben
```

### 2. Plugins & Provider

| Verzeichnis | Zweck | Beispiele |
|-------------|-------|-----------|
| `OC-Plugins/` | Originale OpenCode Plugins (von Upstream/awesome-opencode) | Community-Plugins, 1:1 übernommen |
| `SIN-Plugins/` | Unsere selbst erstellten OpenSIN Plugins | OMOC Swarm, SIN-Terminal, Auth-Integration |
| `Provider/` | OAuth-Provider-Plugins für LLM-Authentifizierung | Anthropic, OpenAI, Google, lokale Modelle |

**Plugin-Entwicklung:**
- Jedes Plugin hat eine eigene `README.md` mit Beschreibung, Konfiguration und Beispielen
- Plugins werden in `~/.config/opencode/plugins/` installiert
- SIN-Plugins nutzen das `@opensin/` Namespace-Prefix

### 3. A2A Bausteine (MCPs, Skills, Tools)

| Verzeichnis | Zweck | Beispiele |
|-------------|-------|-----------|
| `MCPs/` | Model Context Protocols – erweitern KI um externe Datenquellen/Dienste | SIN-MCPs, Community-MCPs, Database-MCPs |
| `Skills/` | Spezialisierte Fähigkeiten für bestimmte Aufgaben | Code-Review, Bug-Fixing, Architekturplanung |
| `Tools/` | Ausführbare Befehle, die Agenten während der Arbeit aufrufen | Shell-Commands, API-Calls, File-Operations |

**MCP-Konfiguration:**
```json
// ~/.config/opencode/mcp.json
{
  "mcpServers": {
    "sin-server": {
      "command": "npx",
      "args": ["-y", "@opensin/a2a-sin-server"],
      "env": { "A2A_ENDPOINT": "https://sin-server.hf.space/a2a/v1" }
    }
  }
}
```

### 4. Watcher & Wrapper

| Verzeichnis | Zweck | Beispiele |
|-------------|-------|-----------|
| `Watcher/` | Überwachen Dateiänderungen, PR-Events, Systemzustände | PR-Watcher, Deploy-Watcher, Quota-Watcher |
| `Wrapper/` | Kapselung externer Aufrufe für konsistente/sichere API-Nutzung | API-Wrapper, CLI-Wrapper, Auth-Wrapper |

**Watcher-Pattern:**
- Watcher laufen als Hintergrundprozesse (LaunchAgents auf macOS)
- Triggern automatisierte Aktionen bei erkannten Events
- Loggen alle Events für Audit-Zwecke (OpenSIN-Ledger)

### 5. OMOC Swarm Integration

| Komponente | Pfad | Zweck |
|------------|------|-------|
| Swarm Plugin | `~/.config/opencode/plugins/omoc-swarm.ts` | Multi-Agent-Delegation |
| OMOC Config | `~/.config/opencode/oh-my-opencode.json` | Modell-Pinnings pro Agent |
| Agent Instructions | `~/.config/opencode/AGENTS.md` | Globale Agent-Verhaltensregeln |

**Verfügbare Swarm Commands:**
| Command | Beschreibung |
|---------|-------------|
| `omoc-jam` | Brainstorming mit mehreren Agenten |
| `omoc-max` | Maximale Agenten-Parallelisierung |
| `swarm_discover` | Verfügbare Agenten finden |
| `swarm_create` | Neuen Agenten erstellen |
| `swarm_status` | Agenten-Status abfragen |
| `swarm_parallel` | Tasks parallel dispatchen |

---

## 📸 Dokumentations-Pflicht für OpenSIN-Code

Jedes neue Plugin, jeder Skill und jeder MCP-Server **muss** im jeweiligen Ordner eine eigene `README.md` besitzen.

**Was gehört in eine Plugin/Skill README?**
1. **Ein aussagekräftiges Bild oder GIF** direkt am Anfang.
2. Ein kurzer "Was macht dieses Tool?" Abschnitt (2-3 Sätze).
3. Ein "Quickstart" (Installations- und Aufruf-Befehl).
4. **Beispielhafte Nutzung** mit Screenshots des Terminal-Outputs!

> **Tipp:** Wenn du ein neues `SIN-Plugin` oder einen `SIN-Skill` baust, mach direkt ein 15-sekündiges Bildschirmvideo (z.B. mit Loom oder macOS Screen Recording), wie du den Befehl ausführst, und binde es in die Markdown-Datei ein. Das spart dem nächsten Entwickler Stunden an Einarbeitung!

## 🔗 Verknüpfte Dokumentation

- [OMOC Swarm](./omoc-swarm.md) – Multi-Agent-Delegation
- [SIN-Terminal](./sin-terminal.md) – iTerm2 Session Management
- [A2A Fleet](./a2a-fleet.md) – Agent-Übersicht
- [Best Practices](./best-practices.md) – Sicherheit & Testing
