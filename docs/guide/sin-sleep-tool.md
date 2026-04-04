# SIN Sleep Tool — Proactive Agent Pausing

> **OpenSIN's Sleep Tool** — Geklont aus Claude Code's SleepTool. Agenten können proaktiv pausieren.

## Use Cases

| Use Case | Description |
|----------|-------------|
| Rate Limit | Warten bis Rate Limit zurückgesetzt |
| Resource Wait | Warten auf externe Ressource |
| Cooldown | Abkühlung nach intensiver Arbeit |
| Scheduled | Geplante Pause |

## Implementation

```python
from opensin.tools import SleepTool

sleep_tool = SleepTool(
    max_duration=300,  # Max 5 Minuten
    allowed_durations=[1, 5, 10, 30, 60, 120, 300]
)

# Agent kann Sleep anfordern
result = await sleep_tool.execute(duration=60)
# Agent pausiert für 60 Sekunden
```

## Sleep in ReAct Loop

```python
async def handle_sleep_in_loop(duration: int):
    """Behandelt Sleep im ReAct Loop."""
    if duration > max_allowed_sleep:
        raise ValueError(f"Sleep duration {duration} exceeds max {max_allowed_sleep}")
    
    await asyncio.sleep(duration)
    return ToolResult(content=f"Slept for {duration} seconds")
```

## Best Practices

1. **Max duration** — Immer Maximum setzen
2. **Allowed durations** — Nur bestimmte Dauern erlauben
3. **User notification** — User über Sleep informieren
4. **Abort support** — Sleep vom User abbrechbar machen

## Next Steps

- [SIN Tool System](/guide/sin-tool-system)
- [SIN ReAct Loop](/guide/sin-react-loop)
