# SIN Stop Hooks — Agent Completion Control

> **OpenSIN's Stop Hooks** — Geklont aus Claude Code's stopHooks.ts. Kontrolle wann Agenten stoppen dürfen.

## Implementation

```python
from opensin.hooks import StopHooks

stop_hooks = StopHooks(
    hooks=[
        {"type": "command", "command": "python3 hooks/sin_loop.py"},
        {"type": "function", "function": check_completion}
    ]
)

# Handle stop attempt
result = await stop_hooks.handle_stop(agent_response)
if not result.allow_stop:
    print("Agent must continue working")
```

## Stop Hook Types

| Type | Description | Use Case |
|------|-------------|----------|
| Command | External script | SIN Loop |
| Function | Python callback | Custom logic |
| Agent | Forked subagent | Complex evaluation |

## SIN Loop Integration

```python
# Stop Hook für SIN Loop
async def sin_loop_hook(response: str) -> StopResult:
    completion_keywords = ["done", "complete", "finished"]
    is_complete = any(kw in response.lower() for kw in completion_keywords)
    
    return StopResult(
        allow_stop=is_complete,
        message="Task not complete, continue working" if not is_complete else ""
    )
```

## Best Practices

1. **Fast evaluation** — Stop Hooks sollten schnell sein
2. **Clear criteria** — Klare Kriterien für Completion
3. **Max iterations** — Endlosschleifen verhindern
4. **User override** — User kann Stop erzwingen
5. **Log decisions** — Stop-Entscheidungen loggen

## Next Steps

- [SIN Loop](/guide/sin-loop)
- [SIN Hook System](/guide/sin-hook-system)
