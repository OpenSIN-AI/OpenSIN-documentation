# SIN Tool Result Budget — Output Token Control

> **OpenSIN's Tool Result Budget** — Geklont aus Claude Code's toolResultStorage.ts. Begrenzt Tool-Result-Tokens.

## Implementation

```python
from opensin.tools import ToolResultBudget

budget = ToolResultBudget(
    max_tokens=50000,
    per_tool_max=10000,
    truncation_strategy="tail"  # or "head", "middle"
)

# Apply budget to tool results
results = await budget.apply(tool_results)
```

## Truncation Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| `tail` | Schneide Ende ab | Logs, Output |
| `head` | Schneide Anfang ab | History |
| `middle` | Schneide Mitte ab | Long text |

## Best Practices

1. **Set limits** — Max Tokens pro Tool-Result
2. **Truncate gracefully** — Mit Hinweis auf Kürzung
3. **Preserve key info** — Wichtige Infos behalten
4. **Monitor usage** — Tool-Result-Usage tracken
5. **Adjust dynamically** — Budget basierend auf Kontext anpassen

## Next Steps

- [SIN Tool Orchestration](/guide/sin-tool-orchestration)
- [SIN Token Estimation](/guide/sin-token-estimation)
