# SIN Hooks — Event-Driven Automation

> **OpenSIN's Hook System** — Automatisiere ALLES mit event-driven Hooks.

## Overview

SIN Hooks feuern bei jedem wichtigen Event. Hooks können Operationen blockieren, modifizieren oder erweitern.

## Hook Events (20+)

| Event | Wann | Use Case |
|-------|------|----------|
| `SessionStart` | Session beginnt | Projekt laden, Context setzen |
| `UserPromptSubmit` | User sendet Prompt | Prompt validieren, erweitern |
| `PreToolUse` | VOR Tool-Ausführung | Security Check, Input modifizieren |
| `PostToolUse` | NACH Tool-Ausführung | Ergebnis validieren, loggen |
| `PostToolUseFailure` | Tool fehlgeschlagen | Retry, Fallback |
| `Stop` | Agent will stoppen | Iteration erzwingen (SIN Loop) |
| `SubagentStart` | Subagent startet | Context injizieren |
| `SubagentStop` | Subagent fertig | Ergebnis sammeln |
| `FileChanged` | Datei geändert | Auto-reload, Re-analyze |
| `CwdChanged` | Verzeichnis gewechselt | Neue SIN.md laden |
| `SessionEnd` | Session endet | Memory speichern, Cleanup |

## Hook Konfiguration

### hooks.json

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${SIN_PLUGIN_ROOT}/hooks/security_check.py",
            "timeout": 10
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${SIN_PLUGIN_ROOT}/hooks/sin_loop.py",
            "timeout": 30
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command", 
            "command": "python3 ${SIN_PLUGIN_ROOT}/hooks/command_logger.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

## Hook Input (stdin)

```json
{
  "session_id": "uuid",
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "src/main.py",
    "old_string": "def old():",
    "new_string": "def new():"
  },
  "context": {
    "branch": "main",
    "cwd": "/path/to/project"
  }
}
```

## Hook Output (stdout)

```json
{
  "continue": true,
  "systemMessage": "⚠️ Du änderst eine kritische Datei. Bitte teste sorgfältig.",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "file_path": "src/main.py",
      "old_string": "def old():",
      "new_string": "def new():\n    # Added by hook"
    }
  }
}
```

## Exit Codes

| Code | Bedeutung |
|------|-----------|
| `0` | Operation erlauben |
| `2` | Operation blockieren (nur PreToolUse) |

## Beispiel: Security Check Hook

```python
#!/usr/bin/env python3
"""PreToolUse Hook: Blockiere gefährliche Operationen."""
import json
import sys

def main():
    # Input lesen
    input_data = json.load(sys.stdin)
    
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    
    # Gefährliche Patterns erkennen
    dangerous_files = [".env", "secrets.py", "credentials.json"]
    file_path = tool_input.get("file_path", "")
    
    for dangerous in dangerous_files:
        if dangerous in file_path:
            print(json.dumps({
                "continue": False,
                "systemMessage": f"🚫 BLOCKED: Änderung an {dangerous} ist nicht erlaubt!"
            }))
            sys.exit(2)
    
    # Alles OK
    print(json.dumps({
        "continue": True,
        "systemMessage": f"✅ Edit an {file_path} erlaubt."
    }))
    sys.exit(0)

if __name__ == "__main__":
    main()
```

## Beispiel: SIN Loop (Stop Hook)

```python
#!/usr/bin/env python3
"""Stop Hook: Iteriere bis Task fertig ist."""
import json
import sys

def main():
    input_data = json.load(sys.stdin)
    
    # Prüfe ob Task wirklich fertig ist
    completion_keywords = ["fertig", "done", "complete", "finished"]
    response = input_data.get("agent_response", "").lower()
    
    if not any(keyword in response for keyword in completion_keywords):
        # Task nicht fertig — weiter iterieren
        print(json.dumps({
            "continue": False,
            "systemMessage": "Task ist noch nicht abgeschlossen. Mache weiter!"
        }))
        sys.exit(2)
    
    # Task fertig
    print(json.dumps({
        "continue": True,
        "systemMessage": "✅ Task erfolgreich abgeschlossen."
    }))
    sys.exit(0)

if __name__ == "__main__":
    main()
```

## Hookify — Hooks ohne Code

Erstelle Hooks mit Markdown — kein Coding nötig:

```yaml
# hooks/rules.yaml
- name: "Keine Secrets committen"
  event: PreToolUse
  match: "Bash(git commit*)"
  check:
    type: regex
    pattern: "(password|secret|api_key|token)"
    scope: staged_files
  action: block
  message: "🚫 Secrets detected in staged files! Remove before committing."

- name: "Tests vor Commit"
  event: PreToolUse  
  match: "Bash(git commit*)"
  check:
    type: command
    command: "pytest tests/ -q"
  action: warn
  message: "⚠️ Tests failed! Trotzdem committen?"
```

## Best Practices

1. **Hooks schnell halten** — Timeout nach 10s
2. **Idempotent** — Mehrfachaufruf = gleiches Ergebnis
3. **Fehlertolerant** — Hook Crash ≠ System Crash
4. **Logging** — Logge alle Hook-Ausführungen
5. **Testing** — Teste Hooks isoliert

## Next Steps

- [Plugin System](/guide/sin-plugins)
- [SIN.md System](/guide/sin-md-system)
- [Permission System](/guide/sin-permissions)
