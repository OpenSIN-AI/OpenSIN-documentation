# SIN API Errors — Error Classification

> **OpenSIN's API Errors** — Geklont aus Claude Code's errors.ts. API-Fehlerklassifizierung.

## Error Types

| Error | HTTP Status | Retry? | Description |
|-------|------------|--------|-------------|
| `RateLimitError` | 429 | Yes | Rate limit exceeded |
| `ContextLengthError` | 400 | Yes | Prompt too long |
| `AuthenticationError` | 401 | No | Invalid API key |
| `ServerError` | 500 | Yes | Internal server error |
| `TimeoutError` | - | Yes | Request timeout |
| `MaxTokensError` | 400 | Yes | Max output tokens exceeded |

## Error Classification

```python
from opensin.errors import categorize_retryable_error

def categorize_retryable_error(error: Exception) -> ErrorCategory:
    """Klassifiziert Fehler für Retry-Entscheidung."""
    if isinstance(error, RateLimitError):
        return ErrorCategory.RETRYABLE
    elif isinstance(error, ContextLengthError):
        return ErrorCategory.COMPACT_AND_RETRY
    elif isinstance(error, AuthenticationError):
        return ErrorCategory.FATAL
    elif isinstance(error, ServerError):
        return ErrorCategory.RETRYABLE
    return ErrorCategory.UNKNOWN
```

## Prompt Too Long Handling

```python
PROMPT_TOO_LONG_ERROR_MESSAGE = "The prompt is too long for this model."

def is_prompt_too_long_message(error: str) -> bool:
    return PROMPT_TOO_LONG_ERROR_MESSAGE in error
```

## Best Practices

1. **Classify errors** — Retryable vs Fatal
2. **Retry with backoff** — Exponential backoff für retryable
3. **Compact on context error** — Context kompaktieren
4. **Alert on fatal** — Bei fatalen Fehlern alarmieren
5. **Log all errors** — Alle Fehler loggen

## Next Steps

- [SIN Error Handling](/guide/agent-error-handling)
- [SIN ReAct Loop](/guide/sin-react-loop)
