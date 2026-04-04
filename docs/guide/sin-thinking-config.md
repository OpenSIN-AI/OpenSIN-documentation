# SIN Thinking Configuration — Model Thinking Control

> **OpenSIN's Thinking Config** — Geklont aus Claude Code's thinking.ts. Kontrolle über Modell-Denkprozesse.

## Implementation

```python
from opensin.thinking import ThinkingConfig

thinking = ThinkingConfig(
    enabled=True,
    max_thinking_length=16384,  # 16K Tokens
    budget_tokens=10000,
    default_enabled=True
)

# Check if thinking should be enabled by default
if thinking.should_enable_by_default(model="claude-sonnet"):
    print("Thinking enabled for this model")
```

## Thinking Rules

1. Message mit thinking block muss query mit max_thinking_length > 0 haben
2. Thinking block darf nicht letzte Message im Block sein
3. Thinking blocks müssen für gesamte Assistant-Trajektorie erhalten bleiben

## Thinking Budget Tracking

```python
from opensin.thinking import ThinkingBudget

budget = ThinkingBudget(
    max_tokens=16384,
    warning_threshold=0.8
)

# Track thinking tokens
budget.record(thinking_tokens)

# Check if warning
if budget.is_warning:
    print("⚠️ 80% of thinking budget used")
```

## Best Practices

1. **Enable for complex tasks** — Thinking für komplexe Tasks aktivieren
2. **Budget control** — Max Tokens für Thinking setzen
3. **Preserve blocks** — Thinking blocks nicht löschen
4. **Monitor usage** — Thinking Token-Usage tracken
5. **Disable for simple** — Für simple Tasks deaktivieren

## Next Steps

- [SIN ReAct Loop](/guide/sin-react-loop)
- [SIN Token Estimation](/guide/sin-token-estimation)
