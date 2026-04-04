# 🧩 SIN-Plugins, MCPs, Skills & Tools

Übersicht aller Erweiterungskomponenten im OpenSIN-Code Ökosystem.

## 📂 Verzeichnisstruktur

Alle Komponenten leben im [OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) Repository:

```
OpenSIN-Code/
├── OC-Plugins/          # Originale OpenCode Plugins (Upstream)
├── SIN-Plugins/         # Eigene OpenSIN Plugins
├── Provider/            # OAuth-Provider-Plugins
├── MCPs/
│   └── SIN-MCPs/       # Eigene MCP-Server
├── Skills/
│   └── SIN-Skills/     # Eigene Skills
├── Tools/               # Ausführbare Agent-Tools
├── Watcher/             # Event-Überwachungsskripte
└── Wrapper/             # API-Kapselungen
```

## 🔌 SIN-Plugins

Plugins erweitern die `opencode` CLI um neue Fähigkeiten.

### OMOC Swarm Plugin

**Pfad:** `~/.config/opencode/plugins/omoc-swarm.ts`

**Zweck:** Multi-Agent-Delegation – verteilt Tasks an spezialisierte Agenten.

**Commands:**
| Command | Beschreibung |
|---------|-------------|
| `omoc-jam` | Brainstorming mit mehreren Agenten |
| `omoc-max` | Maximale Agenten-Parallelisierung |
| `swarm_discover` | Verfügbare Agenten finden |
| `swarm_create` | Neuen Agenten erstellen |
| `swarm_status` | Agenten-Status abfragen |
| `swarm_parallel` | Tasks parallel dispatchen |
| `swarm_send` | Task an spezifischen Agenten senden |
| `swarm_forget` | Agenten aus Swarm entfernen |

### SIN-Terminal Plugin

**Zweck:** iTerm2 Session Management und Task-Delegation.

**Features:**
- Erkennt alle OpenCode-Sessions in iTerm2
- Sendet "mach weiter" an stuck Sessions
- Verwaltet Session-States (active, idle, stuck, dead)

→ Siehe [SIN-Terminal Dokumentation](./sin-terminal.md)

## 🌐 MCPs (Model Context Protocols)

MCPs erweitern die KI-Fähigkeiten um externe Datenquellen und Dienste.

### Structural MCPs (Deployed on HF)

| MCP | HF Space | Zweck |
|-----|----------|-------|
| `sin-server` | `delqhi/sin-server` | Haupt-Server für A2A-Kommunikation |
| `sin-cloudflare` | `delqhi/sin-cloudflare` | Cloudflare-Management (DNS, Workers, R2) |
| `sin-supabase` | `delqhi/sin-supabase` | Supabase-DB-Operationen |
| `sin-storage` | `delqhi/sin-storage` | File-Storage-Operationen |
| `sin-authenticator` | `delqhi/sin-authenticator` | Auth-Token-Management |
| `sin-passwordmanager` | `delqhi/sin-passwordmanager` | Credential-Storage |

### MCP-Konfiguration

```json
// ~/.config/opencode/mcp.json
{
  "mcpServers": {
    "sin-server": {
      "command": "npx",
      "args": ["-y", "@opensin/a2a-sin-server"],
      "env": {
        "A2A_ENDPOINT": "https://sin-server.hf.space/a2a/v1"
      }
    },
    "sin-passwordmanager": {
      "command": "npx",
      "args": ["-y", "@opensin/a2a-sin-passwordmanager"],
      "env": {
        "A2A_ENDPOINT": "https://sin-passwordmanager.hf.space/a2a/v1"
      }
    }
  }
}
```

## 🎯 Skills

Skills definieren spezialisierte Fähigkeiten für bestimmte Aufgaben.

### SIN-Skills Kategorien

| Kategorie | Beispiele |
|-----------|-----------|
| **Code** | Code-Review, Bug-Fixing, Refactoring, Test-Generierung |
| **Architektur** | Architekturplanung, Design-Patterns, ADR-Erstellung |
| **Security** | Vulnerability-Scan, Penetration-Testing, Audit |
| **Documentation** | README-Generierung, API-Docs, Changelog |
| **Deployment** | HF-Space-Deploy, Docker-Build, CI/CD-Setup |

### Skill-Konfiguration

Skills werden in der OpenCode-Konfiguration registriert:

```json
// ~/.config/opencode/opencode.json
{
  "skills": [
    {
      "name": "code-review",
      "description": "Review code for quality, security, and best practices",
      "trigger": "review this code"
    },
    {
      "name": "bug-fix",
      "description": "Diagnose and fix bugs in the codebase",
      "trigger": "fix this bug"
    }
  ]
}
```

## 🛠️ Tools

Tools sind ausführbare Befehle, die Agenten während ihrer Arbeit aufrufen können.

### Tool-Typen

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| **Shell** | Bash-Befehle | `ls`, `grep`, `git status` |
| **API** | HTTP-Requests | REST-Calls zu A2A-Endpoints |
| **File** | Datei-Operationen | Lesen, Schreiben, Suchen |
| **Process** | Prozess-Management | Starten, Stoppen, Überwachen |

## 👁️ Watcher

Watcher überwachen Events und triggern automatisierte Aktionen.

### Watcher-Typen

| Watcher | Zweck | Trigger |
|---------|-------|---------|
| **PR-Watcher** | Überwacht Pull Requests | GitHub Webhook |
| **Deploy-Watcher** | Überwacht Deployment-Status | HF Space Health Check |
| **Quota-Watcher** | Überwacht Model-Quotas | iTerm2 Scrollback Scan |
| **File-Watcher** | Überwacht Dateiänderungen | FileSystem Events |

→ Siehe [LaunchAgents Dokumentation](./launchagents.md) für Watcher-Konfiguration

## 📦 Wrapper

Wrapper kapseln externe Aufrufe für konsistente und sichere API-Nutzung.

### Wrapper-Pattern

```typescript
// Beispiel: A2A API Wrapper
export class A2AWrapper {
  private baseUrl: string;

  constructor(agentSlug: string) {
    this.baseUrl = `https://${agentSlug}.hf.space/a2a/v1`;
  }

  async send(message: string): Promise<A2AResponse> {
    const response = await fetch(this.baseUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });
    return response.json();
  }

  async health(): Promise<boolean> {
    const response = await fetch(`${this.baseUrl}/health`);
    return response.ok;
  }
}
```

## 📝 Dokumentations-Pflicht

**Jedes Element MUSS eine eigene `README.md` haben mit:**

1. **Einleitungssatz** – Was macht dieses Tool?
2. **Screenshot/GIF** – Tool in Aktion
3. **Quickstart** – Installation + Aufruf-Befehl
4. **Konfiguration** – JSON/Env-Variablen
5. **Beispiel-Output** – Terminal-Screenshot

> **Tipp:** Mach direkt ein 15-sekündiges Bildschirmvideo, wie du den Befehl ausführst, und binde es in die Markdown-Datei ein.

## 🔗 Verknüpfte Dokumentation

- [OpenSIN-Code Struktur](./opensin-code.md) – Gesamtübersicht
- [OMOC Swarm](./omoc-swarm.md) – Multi-Agent-Delegation
- [A2A Fleet](./a2a-fleet.md) – Deployed Agents
- [Best Practices](./best-practices.md) – Entwicklungsstandards
