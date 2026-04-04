# SIN Hook System — 20+ Event-Driven Hooks

> **OpenSIN's Hook System** — Geklont aus 5022 Zeilen Claude Code Hook Engine. Das umfassendste Automation-System für AI Agenten.

## Hook Events (20+)

| Event | Wann | Use Case |
|-------|------|----------|
| `SessionStart` | Session beginnt | Projekt laden, Context setzen |
| `SessionEnd` | Session endet | Memory speichern, Cleanup |
| `Setup` | Initialisierung | Environment prüfen |
| `UserPromptSubmit` | User sendet Prompt | Prompt validieren, erweitern |
| `PreToolUse` | VOR Tool-Ausführung | Security Check, Input modifizieren |
| `PostToolUse` | NACH Tool-Ausführung | Ergebnis validieren, loggen |
| `PostToolUseFailure` | Tool fehlgeschlagen | Retry, Fallback |
| `SubagentStart` | Subagent startet | Context injizieren |
| `SubagentStop` | Subagent fertig | Ergebnis sammeln |
| `PreCompact` | VOR Context Compaction | Wichtige Infos sichern |
| `PostCompact` | NACH Context Compaction | Kompaktierung prüfen |
| `PermissionDenied` | Permission verweigert | Alternative vorschlagen |
| `PermissionRequest` | Permission benötigt | Auto-entscheiden |
| `Elicitation` | MCP benötigt Input | Strukturierte Eingabe |
| `CwdChanged` | Verzeichnis gewechselt | Neue SIN.md laden |
| `FileChanged` | Datei geändert | Auto-reload, Re-analyze |
| `Notification` | Benachrichtigung | Filtern, priorisieren |
| `Stop` | Agent will stoppen | Iteration erzwingen (SIN Loop) |
| `StopFailure` | Turn fehlgeschlagen | Recovery |
| `TeammateIdle` | Teammate inaktiv | Task zuweisen |

## 5 Hook Execution Modes

### 1. Shell Command Hooks

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
    ]
  }
}
```

**Hook Input (stdin):**
```json
{
  "session_id": "uuid",
  "tool_name": "Edit",
  "tool_input": {"file_path": "src/main.py"},
  "context": {"branch": "main", "cwd": "/path"}
}
```

**Hook Output (stdout):**
```json
{
  "continue": true,
  "systemMessage": "⚠️ Kritische Datei. Bitte teste sorgfältig.",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {"file_path": "src/main.py"}
  }
}
```

**Exit Codes:**
- `0` = Operation erlauben
- `2` = Operation blockieren (nur PreToolUse)

### 2. HTTP Hooks

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "http",
            "url": "https://your-server.com/hook",
            "method": "POST",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### 3. Function Hooks (Callback)

```python
from opensin.hooks import HookRegistry

registry = HookRegistry()

@registry.on("PreToolUse", matcher="Edit|Write")
async def security_check(event):
    if is_dangerous(event.tool_input):
        return {
            "continue": False,
            "systemMessage": "🚫 Blockiert: Gefährliche Operation!"
        }
    return {"continue": True}
```

### 4. Agent Hooks (Forked Subagent)

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "agent",
            "agent": "sin-loop-agent",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 5. Prompt Hooks (Interactive)

```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Bash(sudo *)",
        "hooks": [
          {
            "type": "prompt",
            "message": "⚠️ sudo Command! Fortfahren?",
            "options": ["Allow", "Deny", "Allow for session"]
          }
        ]
      }
    ]
  }
}
```

## Map-Based Session Hooks (O(1) Performance)

```python
from opensin.hooks import SessionHookStore

# Map statt Record für O(1) Operationen unter hoher Parallelität
# Wichtig bei: N parallele Agents feuern N addHook calls im selben Tick
store = SessionHookStore()

# O(1) add — kein Kopieren der wachsenden Map
store.set(session_id, hook)

# Skippt alle ~30 Store Listener wenn sich nichts ändert
store.update_if_changed(session_id, new_hook)
```

## Frontmatter Hooks (Agent-Scoped)

```markdown
---
name: code-reviewer
hooks:
  - event: PreToolUse
    matcher: "Edit"
    command: python3 hooks/review_check.py
  - event: PostToolUse
    matcher: "Bash"
    command: python3 hooks/log_command.py
---

You are a code reviewer...
```

## Async Hook Protocol

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 hooks/slow_check.py",
            "async": true,
            "asyncTimeout": 60
          }
        ]
      }
    ]
  }
}
```

## Hook Matcher Patterns

| Pattern | Bedeutung |
|---------|-----------|
| `Edit\|Write` | Edit ODER Write |
| `Bash(git *)` | Alle git Commands |
| `Bash(npm publish:*)` | npm publish mit Args |
| `mcp__servername` | MCP Server Tools |
| `.*` | Alle (Catch-all) |

## Best Practices

1. **Hooks schnell halten** — Timeout nach 10s
2. **Idempotent** — Mehrfachaufruf = gleiches Ergebnis
3. **Fehlertolerant** — Hook Crash ≠ System Crash
4. **Map-based Store** — O(1) für parallele Agents
5. **Frontmatter Hooks** — Agent-spezifische Hooks

## Next Steps

- [SIN Loop](/guide/sin-loop)
- [SIN Plugins](/guide/sin-plugins)
- [SIN Permissions](/guide/sin-permission-system)
