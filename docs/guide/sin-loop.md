# SIN Loop — Iterative Self-Correction

> **OpenSIN's Self-Improvement Loop** — Agenten iterieren automatisch bis der Task perfekt ist.

## Overview

SIN Loop verhindert dass Agenten zu früh aufhören. Ein Stop Hook blockiert das Beenden und fordert den Agenten auf weiterzuarbeiten.

## Wie es funktioniert

```
Agent arbeitet
    ↓
Agent will stoppen ("I'm done")
    ↓
Stop Hook feuert
    ↓
Prüfe: Ist Task wirklich fertig?
    ↓
NEIN → "Mache weiter!" → Agent arbeitet weiter
    ↓
JA → "Task abgeschlossen" → Session endet
```

## Konfiguration

### hooks.json

```json
{
  "hooks": {
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
    ]
  }
}
```

### sin_loop.py

```python
#!/usr/bin/env python3
"""SIN Loop: Iteriere bis Task wirklich fertig ist."""
import json
import sys

COMPLETION_KEYWORDS = [
    "task complete", "all done", "finished",
    "implementierung abgeschlossen", "fertig"
]

MAX_ITERATIONS = 10

def main():
    input_data = json.load(sys.stdin)
    response = input_data.get("agent_response", "").lower()
    iteration = input_data.get("iteration", 0)
    
    # Max Iterations prüfen
    if iteration >= MAX_ITERATIONS:
        print(json.dumps({
            "continue": True,
            "systemMessage": f"⚠️ Max {MAX_ITERATIONS} Iterationen erreicht."
        }))
        sys.exit(0)
    
    # Completion prüfen
    is_complete = any(kw in response for kw in COMPLETION_KEYWORDS)
    
    if not is_complete:
        print(json.dumps({
            "continue": False,
            "systemMessage": "🔄 Task ist noch nicht abgeschlossen. Mache weiter!"
        }))
        sys.exit(2)
    
    # Task fertig
    print(json.dumps({
        "continue": True,
        "systemMessage": f"✅ Task nach {iteration + 1} Iterationen abgeschlossen."
    }))
    sys.exit(0)

if __name__ == "__main__":
    main()
```

## Use Cases

| Use Case | Warum Loop? |
|----------|-------------|
| Code Refactoring | Agent hört oft zu früh auf |
| Bug Fixing | Mehrere Iterationen nötig |
| Testing | Tests schreiben → laufen lassen → fixen |
| Documentation | Vollständigkeit prüfen |

## Best Practices

1. **Max Iterations** — Immer setzen (verhindert Endlosschleife)
2. **Completion Detection** — Robuste Keywords
3. **Timeout** — Hook Timeout setzen
4. **Logging** — Jede Iteration loggen

## Next Steps

- [SIN Hooks](/guide/sin-hooks)
- [SIN Feature Dev](/guide/sin-feature-dev)
