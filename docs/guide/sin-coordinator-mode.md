# SIN Coordinator Mode — Multi-Agent Coordination

> **OpenSIN's Coordinator Mode** — Geklont aus Claude Code's coordinatorMode.ts. Multi-Agenten-Koordination.

## Implementation

```python
from opensin.coordinator import CoordinatorMode

coordinator = CoordinatorMode(
    enabled=True,
    agents=["researcher", "writer", "reviewer"],
    strategy="sequential"
)

# Get coordinator user context
context = await coordinator.get_user_context(
    mcp_clients=mcp_clients,
    scratchpad_dir=scratchpad_dir
)
```

## Coordinator Features

| Feature | Description |
|---------|-------------|
| Agent Discovery | Verfügbare Agenten finden |
| Task Distribution | Tasks an Agenten verteilen |
| Progress Tracking | Fortschritt aller Agenten tracken |
| Result Aggregation | Ergebnisse aggregieren |
| Error Handling | Fehler in Agenten behandeln |

## Best Practices

1. **Clear roles** — Jeder Agent hat klare Rolle
2. **Task distribution** — Tasks gleichmäßig verteilen
3. **Progress tracking** — Fortschritt aller Agenten tracken
4. **Error handling** — Fehler in Agenten behandeln
5. **Result aggregation** — Ergebnisse aggregieren

## Next Steps

- [SIN Multi-Agent Types](/guide/sin-multi-agent-types)
- [SIN Team Orchestration](/guide/team-orchestration)
