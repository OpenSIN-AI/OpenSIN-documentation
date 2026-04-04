# SIN Context Collapse — Advanced Context Management

> **OpenSIN's Context Collapse** — Geklont aus Claude Code's contextCollapse/index.ts. Fortgeschrittenes Context-Management.

## Implementation

```python
from opensin.collapse import ContextCollapse

collapse = ContextCollapse(
    enabled=True,
    strategy="aggressive",  # conservative, balanced, aggressive
    min_context_size=4000,
    max_context_size=100000
)

# Collapse context
collapsed = await collapse.collapse(messages)
```

## Collapse Strategies

| Strategy | Description | Context Retention |
|----------|-------------|-------------------|
| Conservative | Behalte mehr Kontext | 80% |
| Balanced | Ausgewogen | 60% |
| Aggressive | Maximale Kompression | 40% |

## Best Practices

1. **Choose strategy wisely** — Aggressive für lange Sessions
2. **Monitor quality** — Qualität nach Collapse prüfen
3. **Preserve key info** — Wichtige Infos immer behalten
4. **User control** — User kann Strategie wählen
5. **Track impact** — Impact auf Antwortqualität messen

## Next Steps

- [SIN Compaction System](/guide/sin-compaction-system)
- [SIN ReAct Loop](/guide/sin-react-loop)
