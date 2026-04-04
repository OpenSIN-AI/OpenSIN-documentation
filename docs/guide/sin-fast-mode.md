# SIN Fast Mode — Low-Latency Execution

> **OpenSIN's Fast Mode** — Geklont aus Claude Code's fastMode.ts. Reduzierte Latenz für schnelle Tasks.

## Implementation

```python
from opensin.fastmode import FastMode

fast_mode = FastMode(
    enabled=False,  # Default aus
    model_override="gpt-3.5-turbo",  # Schnelleres Modell
    max_tokens_override=1000,  # Weniger Tokens
    skip_compaction=True  # Keine Kompaktierung
)

# Aktivieren
await fast_mode.enable()

# Status prüfen
if fast_mode.is_enabled:
    print("Fast mode active")
```

## Fast Mode Effects

| Setting | Normal | Fast Mode |
|---------|--------|-----------|
| Model | gpt-4 | gpt-3.5-turbo |
| Max Tokens | 4000 | 1000 |
| Compaction | Enabled | Disabled |
| Tool Search | Enabled | Disabled |
| Memory | Full | Minimal |

## Sticky Latch Integration

```python
# Fast Mode als Sticky Latch
# Einmal aktiviert, bleibt es für ganze Session an
# Verhindert Prompt Cache Busts

await latch.activate("fast_mode")
# Alle folgenden Requests nutzen denselben System Prompt
# → Maximale Cache Hits!
```

## Best Practices

1. **Use for simple tasks** — Nur für einfache Tasks aktivieren
2. **Sticky activation** — Einmal an = immer an
3. **Monitor quality** — Qualität im Fast Mode prüfen
4. **User control** — User kann Fast Mode togglen
5. **Cost savings** — Fast Mode spart Kosten

## Next Steps

- [SIN Sticky Latches](/guide/sin-sticky-latches)
- [Cost Optimization](/guide/agent-cost-optimization)
