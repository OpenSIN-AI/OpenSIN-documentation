# SIN Query Transitions — State Machine

> **OpenSIN's Query Transitions** — Geklont aus Claude Code's query/transitions.ts. State Machine für Query-Flow.

## Implementation

```python
from opensin.query import Terminal, Continue

class QueryStateMachine:
    def __init__(self):
        self.state = "idle"
    
    async def transition(self, event: str) -> Union[Terminal, Continue]:
        if event == "tool_use":
            return Continue(tool_execution)
        elif event == "error":
            return Terminal(error_message)
        elif event == "complete":
            return Terminal(complete_message)
        return Continue()
```

## Transition Types

| Type | Description |
|------|-------------|
| `Continue` | Query continues |
| `Terminal` | Query ends |

## Best Practices

1. **Clear states** — Zustände klar definieren
2. **Handle all transitions** — Alle Übergänge behandeln
3. **Error handling** — Fehler-Zustände behandeln
4. **Logging** — Zustandsänderungen loggen
5. **Testing** — State Machine testen

## Next Steps

- [SIN Query Config](/guide/sin-query-config)
- [SIN ReAct Loop](/guide/sin-react-loop)
