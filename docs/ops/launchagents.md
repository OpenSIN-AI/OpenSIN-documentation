# 🔔 LaunchAgents (Guard + Watcher)

LaunchAgents sind macOS-Systemdienste, die im Hintergrund laufen und die Auth-Rotation-Systeme steuern.

## 📐 Architektur

```
┌──────────────────────────────────────────────────────────────┐
│                      macOS LaunchAgents                       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────┐    ┌──────────────────────────┐ │
│  │  openAntigravity-       │    │  com.opencode.           │ │
│  │  ratelimit-watcher      │    │  auth-guard               │ │
│  │                         │    │                           │ │
│  │  Zweck:                 │    │  Zweck:                   │ │
│  │  Antigravity-Quota      │    │  OpenAI-Token             │ │
│  │  überwachen             │    │  überwachen               │ │
│  │                         │    │                           │ │
│  │  Trigger:               │    │  Trigger:                 │ │
│  │  Rate-Limit Pattern    │    │  Fehlender OpenAI-Key     │ │
│  │  in iTerm2 Scrollback   │    │  in auth.json             │ │
│  │                         │    │                           │ │
│  │  Aktion:                │    │  Aktion:                  │ │
│  │  Rotation triggern      │    │  Rotation triggern        │ │
│  └───────────┬─────────────┘    └───────────┬──────────────┘ │
│              │                              │                 │
│              └──────────────┬───────────────┘                 │
│                             │                                 │
│              ┌──────────────┴───────────────┐                 │
│              │   Auth Rotator (main.py)     │                 │
│              │   Browser-Automation         │                 │
│              │   Token Exchange             │                 │
│              │   Session Resume             │                 │
│              └──────────────────────────────┘                 │
└──────────────────────────────────────────────────────────────┘
```

## 📁 Projekt-Struktur

Das LaunchAgents-Projekt liegt separat vom Rotator-Code:

```
/Users/jeremy/dev/Opencode-LaunchAgents/
├── guard/
│   ├── __init__.py
│   ├── main.py              # Poll-Loop: check auth → rotate → send weiter
│   ├── check_auth.py        # Prüft auth.json auf "openai" Key
│   ├── run_rotator.py       # PID-based lock + Popen rotator
│   ├── wait_rotation.py     # Wartet auf Rotator-Exit
│   ├── iterm_list.py        # AppleScript: alle iTerm2 (window,tab) Paare
│   ├── iterm_read.py        # AppleScript: liest Tab-Inhalt
│   ├── iterm_send.py        # AppleScript: sendet Text an Tab
│   ├── find_stuck.py        # Findet Tabs mit Rate-Limit-Text
│   └── send_weiter.py       # Sendet "mach weiter" an stuck Tabs
├── watcher/
│   ├── __init__.py
│   ├── main.py              # Modularer Watcher Entry Point
│   ├── detect_scan.py       # Scannt iTerm2 Scrollback
│   ├── detect_openai.py     # OpenAI-spezifische Erkennung
│   ├── wtrigger_run.py      # Trigger Rotation mit Cooldown
│   └── watcher_config.py    # Patterns, Cooldowns, Lock-Files
├── com.opencode.auth-guard.plist
├── com.openAntigravity.ratelimit-watcher.plist
├── shortcuts/
│   └── opencode-shortcuts.lua  # Hammerspoon ⌘R→C / ⌘R→A
└── run-guard.sh              # Shim für LaunchAgent
```

## 🔧 LaunchAgent 1: openAntigravity-ratelimit-watcher

**Zweck:** Überwacht iTerm2 auf Antigravity-Model-Quota-Erschöpfung (Claude + Gemini).

**Plist:** `~/Library/LaunchAgents/com.openAntigravity.ratelimit-watcher.plist`

**Funktionsweise:**
1. Pollt alle 30 Sekunden iTerm2 Scrollback (letzte 2000 Zeichen pro Session)
2. Prüft gegen Error-Patterns (Rate Limit, 401, 403, 404, PERMISSION_DENIED)
3. Bei Match: Triggert Rotation via `orchestrator/run_rotate.py`
4. macOS Desktop Notification bei Start/Trigger/Error
5. 10-Minuten globaler Cooldown verhindert Re-Trigger

**Error-Patterns:**
```python
QUOTA_PATTERNS = [
    r"rate.?limit",
    r"over \d+% usage for",
    r"quota.*exceeded",
    r"usage limit has been reached",
]

MODEL_ERROR_PATTERNS = [
    r"Requested entity was not found",
    r"ProviderModelNotFoundError",
    r"Model not found:",
    r"PERMISSION_DENIED",
    r"authentication.*invalid",
    r"token has been invalidated",
]
```

**Log-File:** `/tmp/openAntigravity-watcher.log`

## 🔧 LaunchAgent 2: com.opencode.auth-guard

**Zweck:** Überwacht OpenAI-Token-Status und triggert Rotation bei fehlendem/abgelaufenem Token.

**Plist:** `~/Library/LaunchAgents/com.opencode.auth-guard.plist`

**Funktionsweise:**
1. Prüft alle 5 Minuten `auth.json` auf "openai" Key
2. Wenn fehlend: Triggert sofort Rotation (kein GPT-Test mehr!)
3. Wartet auf Rotator-Completion (PID-based lock)
4. Findet stuck iTerm2-Sessions
5. Sendet "mach weiter" an alle stuck Sessions

**Log-File:** `/tmp/opencodex-guard.log`

## 🎹 Hammerspoon Shortcuts

Globale Tastenkürzel zum manuellen Triggern der Rotator-Systeme:

| Shortcut | Aktion |
|----------|--------|
| `⌘R→C` | opencodex-auth-rotator starten |
| `⌘R→A` | openAntigravity-auth-rotator starten |

**Konfiguration:** `~/.hammerspoon/init.lua` + `~/dev/Opencode-LaunchAgents/shortcuts/opencode-shortcuts.lua`

## 🐛 Bekannte Probleme

| Problem | Lösung |
|---------|--------|
| Doppelte Watcher-Prozesse | `launchctl list | grep watcher` → überflüssige mit `launchctl unload` entfernen |
| Stale Lock-Files | `/tmp/openAntigravity-*.lock` manuell löschen |
| AppleScript Timeout bei 30+ Tabs | Nur letzte 2000 Zeichen lesen, Timeout 20s |
| LaunchAgent PATH eingeschränkt | Immer absolute Pfade nutzen (`/opt/homebrew/bin/python3.14`) |
| Cooldown zu kurz → Re-Trigger | 10 Minuten globaler Cooldown (`/tmp/openAntigravity-last-rotation.txt`) |
| Deutsche macOS Locale | AppleScript Variablennamen müssen lang sein (`aSess` nicht `aS`) |

## 🚀 Quickstart

```bash
# Watcher-Status prüfen
launchctl list | grep -E "opencode|openAntigravity"

# Watcher neustarten
launchctl unload ~/Library/LaunchAgents/com.openAntigravity.ratelimit-watcher.plist
launchctl load ~/Library/LaunchAgents/com.openAntigravity.ratelimit-watcher.plist

# Guard neustarten
launchctl unload ~/Library/LaunchAgents/com.opencode.auth-guard.plist
launchctl load ~/Library/LaunchAgents/com.opencode.auth-guard.plist

# Logs ansehen
tail -f /tmp/openAntigravity-watcher.log
tail -f /tmp/opencodex-guard.log

# Stale Locks entfernen
rm -f /tmp/openAntigravity-*.lock
rm -f /tmp/opencodex-*.lock
```

## 🔗 Verknüpfte Dokumentation

- [Auth Rotator](./auth-rotator.md) – Die Rotator-Systeme selbst
- [SIN-Terminal](./sin-terminal.md) – iTerm2 Session Management
- [Best Practices](./best-practices.md) – Browser-Automatisierung & Sicherheit
