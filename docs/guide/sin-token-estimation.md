# SIN Token Estimation — Accurate Token Counting

> **OpenSIN's Token Estimation** — Geklont aus Claude Code's tokens.ts. Präzise Token-Zählung für Context-Management.

## Token Counting Methods

| Method | Accuracy | Speed | Use Case |
|--------|----------|-------|----------|
| `exact_count` | 100% | Slow | API Calls |
| `estimate` | ~95% | Fast | Pre-flight checks |
| `quick_estimate` | ~85% | Very Fast | UI display |

## Token Count with Estimation

```python
from opensin.tokens import token_count_with_estimation

def token_count_with_estimation(
    messages: list[Message],
    model: str = "gpt-4"
) -> int:
    """Zählt Tokens mit Schätzung für nicht-cached Teile."""
    total = 0
    
    for message in messages:
        if message.cached:
            # Exakte Zählung für cached Messages
            total += exact_token_count(message)
        else:
            # Schätzung für nicht-cached Messages
            total += estimate_token_count(message)
    
    return total
```

## Context Tokens from Last Response

```python
from opensin.tokens import final_context_tokens_from_last_response

def final_context_tokens_from_last_response(
    messages: list[Message],
    last_response_tokens: int
) -> int:
    """Berechnet finale Context-Tokens nach letzter Response."""
    # Zählt Tokens aller Messages nach Compact-Boundary
    boundary_index = find_compact_boundary(messages)
    messages_after_boundary = messages[boundary_index + 1:]
    
    return (
        token_count_with_estimation(messages_after_boundary)
        + last_response_tokens
    )
```

## 200K Message Check

```python
from opensin.tokens import does_most_recent_assistant_message_exceed_200k

def does_most_recent_assistant_message_exceed_200k(
    messages: list[Message]
) -> bool:
    """Prüft ob letzte Assistant-Message > 200K Tokens."""
    for message in reversed(messages):
        if message.type == "assistant":
            return message.token_count > 200000
    return False
```

## Escalated Max Tokens

```python
# Max Tokens für verschiedene Szenarien
ESCALATED_MAX_TOKENS = 32768  # 32K für komplexe Tasks
DEFAULT_MAX_TOKENS = 4096     # 4K für normale Tasks
COMPACT_MAX_TOKENS = 1024     # 1K für Kompaktierung
```

## Token Budget Tracking

```python
from opensin.tokens import TokenBudgetTracker

tracker = TokenBudgetTracker(
    max_tokens=100000,
    warning_threshold=0.8
)

# Tracke Token-Usage
tracker.record_input(1500)
tracker.record_output(500)

# Prüfe ob Warning
if tracker.is_warning:
    print("⚠️ 80% des Token-Budgets erreicht")

# Prüfe ob Limit erreicht
if tracker.is_exceeded:
    print("🛑 Token-Budget überschritten")
```

## Best Practices

1. **Estimate first** — Schnelle Schätzung vor API Call
2. **Exact count for API** — Exakte Zählung für API Calls
3. **Track continuously** — Token-Usage kontinuierlich tracken
4. **Warning at 80%** — Warning bei 80% des Budgets
5. **Compact before limit** — Kompaktieren bevor Limit erreicht

## Next Steps

- [SIN ReAct Loop](/guide/sin-react-loop)
- [SIN Compaction System](/guide/sin-compaction-system)
