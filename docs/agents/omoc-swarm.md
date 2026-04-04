# 🎯 OMOC Swarm & OpenCode Konfiguration

OMOC (Oh My OpenCode) ist der Swarm Coordinator, der Aufgaben an spezialisierte Agenten delegiert und Modell-Routing steuert.

## 🏗️ Architektur

```
┌─────────────────────────────────────────────────────────┐
│                    OpenCode CLI                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐ │
│  │   OMOC       │  │   Swarm      │  │   A2A MCP     │ │
│  │ (Coordinator)│←→│  (Plugin)    │←→│   (Fleet)     │ │
│  │              │  │              │  │               │ │
│  │ Prompt →     │  │ discover     │  │ sin-server    │ │
│  │ Delegate →   │  │ create       │  │ sin-terminal  │ │
│  │ Aggregate ←  │  │ status       │  │ sin-frontend  │ │
│  │              │  │ parallel     │  │ ... (130+)    │ │
│  │              │  │ jam          │  │               │ │
│  └──────────────┘  └──────────────┘  └───────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## 📁 Kanonische Konfigurationspfade

| Pfad | Zweck |
|------|-------|
| `~/.config/opencode/opencode.json` | Globale OpenCode-Konfiguration (Default Agent, Commands, Plugins) |
| `~/.config/opencode/oh-my-opencode.json` | OMOC Modell-Pinnings pro Agent |
| `~/.config/opencode/mcp.json` | Globale MCP-Server-Konfiguration |
| `~/.config/opencode/plugins/omoc-swarm.ts` | Globales Swarm Plugin |
| `~/.config/opencode/AGENTS.md` | Globale Agent Instructions |
| `.opencode/opencode.json` (Repo) | Repo-spezifische OpenCode-Konfiguration |

## 🧠 Swarm Commands

| Command | Beschreibung |
|---------|-------------|
| `omoc-jam` | Brainstorming-Modus mit mehreren Agenten |
| `omoc-max` | Maximale Agenten-Parallelisierung |
| `swarm_discover` | Verfügbare Agenten finden |
| `swarm_create` | Neuen Agenten erstellen |
| `swarm_status` | Agenten-Status abfragen |
| `swarm_parallel` | Tasks parallel dispatchen |
| `swarm_send` | Task an spezifischen Agenten senden |
| `swarm_forget` | Agenten aus Swarm entfernen |

## 🤖 Agent-Modell-Pinnings

| Agent | Modell | Zweck |
|-------|--------|-------|
| `omoc` | Gemini 3.1 Pro | Swarm Coordinator |
| `build` | Claude Sonnet 4.6 (Antigravity) | Code-Generierung |
| `general` | Claude Sonnet 4.6 (Antigravity) | Allgemeine Tasks |
| `Sisyphus (Ultraworker)` | Claude Sonnet 4.6 (Antigravity) | Heavy computation |
| `Prometheus (Planner)` | Claude Opus 4.6 Thinking | Architektur-Planung |

## ⚠️ Bekannte Probleme

| Problem | Lösung |
|---------|--------|
| OMOC hardcoded edit/coder phase auf `agent: "build"` | Fixed: nutzt jetzt `wt.agent` für dynamische Zuordnung |
| Naming Mismatch: `Sisyphus (Ultraworker)` vs `Fast-Ultraworker` | Fixed: Alias-kompatible Namen in `opencode.json` |
| `gemini-3.1-pro` → 404 | Fixed: Plugin resolved zu `gemini-3.1-pro-low` |
| Stale `rateLimitResetTimes` Einträge erzwingen falschen Header-Style | Fixed: Einträge manuell löschen |
| Singleton-Regel: Nur `~/.config/opencode/opencode.json` und `oh-my-opencode.json` erlaubt | Repo-/`~/.opencode`-Duplikate entfernen |

## 🔗 Verknüpfte Dokumentation

- [A2A Fleet](./a2a-fleet.md)
- [Auth Rotator](./auth-rotator.md)
- [OpenSIN-Code Struktur](./opensin-code.md)
