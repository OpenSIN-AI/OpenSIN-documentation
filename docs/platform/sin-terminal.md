# 🖥️ SIN-Terminal Orchestrator

SIN-Terminal ist der macOS-Terminal-Orchestrator, der sichtbare iTerm2-Sessions verwaltet und Tasks an parallele OpenCode-Sessions delegiert.

## 🎯 Zweck

SIN-Terminal löst drei Probleme:

1. **Session-Management:** Erkennt und verwaltet alle offenen iTerm2-Sessions mit OpenCode-Instanzen
2. **Task-Delegation:** Verteilt Tasks auf mehrere parallele OpenCode-Sessions für maximale Produktivität
3. **State-Persistenz:** Speichert Session-States und stellt sie nach Neustarts wieder her

## 🏗️ Architektur

```
┌────────────────────────────────────────────────────────────┐
│                      SIN-Terminal                          │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │  iTerm2 API  │  │   Session    │  │  Task Dispatcher │ │
│  │  (AppleScript│←→│   Manager    │←→│  (Parallel/Queue)│ │
│  │   + TTY)     │  │              │  │                  │ │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘ │
│         │                 │                    │           │
│  ┌──────┴─────────────────┴────────────────────┴───────┐  │
│  │              iTerm2 Sessions (TTYs)                  │  │
│  │                                                      │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │  │
│  │  │Session 1 │ │Session 2 │ │Session 3 │ │SessionN│ │  │
│  │  │PID:81457 │ │PID:81492 │ │PID:81661 │ │PID:... │ │  │
│  │  │ttys078   │ │ttys079   │ │ttys080   │ │ttys... │ │  │
│  │  │opencode  │ │opencode  │ │opencode  │ │opencode│ │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

## 🔧 Kern-Komponenten

### 1. Session Discovery

Erkennt alle OpenCode-Sessions in iTerm2:

```python
# AppleScript: Alle iTerm2-Sessions scannen
tell application "iTerm2"
    set sessions to {}
    repeat with w in windows
        repeat with t in tabs of w
            repeat with s in sessions of t
                set end of sessions to {
                    name: name of s,
                    tty: tty of s,
                    contents: contents of s
                }
            end repeat
        end repeat
    end repeat
    return sessions
end tell
```

**Erkennungsmuster:**
- `opencode` im Prozessnamen
- `opencode -s <session_id>` für spezifische Sessions
- `opencode -m <model>` für modell-spezifische Sessions
- `opencode run "<command>"` für Headless-Execution

### 2. TTY-Kommunikation

Direkte Kommunikation mit iTerm2-Sessions über TTY-Devices:

```python
# "mach weiter" an spezifische Session senden
echo -e "mach weiter\r" > /dev/ttys078
```

**Wichtig:** macOS 26 blockiert `TIOCSTI` ioctl – AppleScript `write text` oder `/dev/tty` writes sind die einzigen Optionen.

### 3. Session State Management

| State | Beschreibung |
|-------|-------------|
| `active` | Session läuft, CPU > 0% |
| `idle` | Session läuft, CPU = 0%, wartet auf Input |
| `stuck` | Session zeigt Error-Pattern (Rate Limit, 401, 403, 404) |
| `dead` | Prozess nicht mehr vorhanden |

### 4. Task Dispatcher

Verteilt Tasks auf verfügbare Sessions:

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   Task      │────→│   Dispatcher │────→│   Session    │
│   Queue     │     │   (Round-    │     │   Selector   │
│             │     │    Robin)    │     │              │
└─────────────┘     └──────────────┘     └──────────────┘
```

**Dispatch-Strategien:**
- **Round Robin:** Gleichmäßige Verteilung auf alle aktiven Sessions
- **Least Loaded:** Session mit niedrigster CPU-Auslastung
- **Model-Specific:** Task an Session mit passendem Modell

## 📁 Konfigurationspfade

| Pfad | Zweck |
|------|-------|
| `~/.config/opencode/opencode.json` | Globale OpenCode-Konfiguration |
| `~/.config/opencode/oh-my-opencode.json` | OMOC Modell-Pinnings |
| `~/.config/opencode/mcp.json` | MCP-Server-Konfiguration |
| `/tmp/sin-terminal-state.json` | Runtime Session State |

## 🔗 Integration mit anderen Systemen

| System | Integration |
|--------|-------------|
| **Auth Rotator** | SIN-Terminal erkennt stuck Sessions → triggert Rotation → sendet "mach weiter" |
| **OMOC Swarm** | SIN-Terminal delegiert Swarm-Tasks an parallele Sessions |
| **LaunchAgents** | Watcher scannt iTerm2-Sessions → SIN-Terminal managed die Sessions |
| **OpenCode CLI** | SIN-Terminal startet/stopped/managed OpenCode-Instanzen |

## 🐛 Bekannte Probleme

| Problem | Lösung |
|---------|--------|
| AppleScript `write text` hängt bei 30+ offenen Tabs | Nur letzte 2000 Zeichen pro Session lesen, Timeout 20s |
| `TIOCSTI` ioctl blockiert auf macOS 26 | AppleScript `write text` oder `/dev/tty` writes nutzen |
| Session IDs ändern sich nach Neustart | Dynamische Erkennung via `opencode session list` + Window-Title-Matching |
| Zombie-Prozesse nach Force-Kill | `ps aux | grep opencode` + `kill -9` vor Neustart |
| Chrome Singleton-Locks nach Crash | `Singleton*`-Files im Profil-Verzeichnis löschen vor Chrome-Start |

## 🚀 Quickstart

```bash
# Alle OpenCode-Sessions auflisten
ps aux | grep opencode

# Session ID finden
opencode session list

# Neue Session mit spezifischem Modell starten
opencode -s <session_id> -m google/antigravity-claude-sonnet-4-6

# "mach weiter" an Session senden
osascript -e 'tell application "iTerm2" to tell the current session of current window to write text "mach weiter"'
```

## 🔗 Verknüpfte Dokumentation

- [OMOC Swarm](./omoc-swarm.md) – Multi-Agent-Delegation
- [Auth Rotator](./auth-rotator.md) – Automatische Session-Rotation
- [Best Practices](./best-practices.md) – Browser-Automatisierung & Sicherheit
