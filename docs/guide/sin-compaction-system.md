# SIN Compaction System — Context Management

> **OpenSIN's Compaction System** — Geklont aus Claude Code's compact.ts, snipCompact.ts, reactiveCompact.ts. Verhindert Token-Limit-Überschreitung.

## Compaction Strategies

| Strategy | Description | When |
|----------|-------------|------|
| `auto_compact` | Automatische Zusammenfassung | Token-Warnung |
| `reactive_compact` | Reaktive Kompaktierung | Prompt zu lang |
| `micro_compact` | Mini-Zusammenfassung | Alle 10 Turns |
| `snip_compact` | Snip-basierte Kompaktierung | HISTORY_SNIP Feature |
| `context_collapse` | Vollständiger Kollaps | CONTEXT_COLLAPSE Feature |

## Auto Compaction

```python
from opensin.compaction import AutoCompactor

compactor = AutoCompactor(
    warning_threshold=0.8,    # 80% des Kontexts
    circuit_breaker_limit=3,  # Max 3 fehlgeschlagene Kompaktierungen
    summarizer_model="gpt-3.5-turbo"  # Schnelles Modell
)

# Prüfe ob Kompaktierung nötig
state = compactor.calculate_token_warning_state(messages)
if state.needs_compaction:
    messages = await compactor.compact(messages)
```

## Reactive Compact

```python
from opensin.compaction import ReactiveCompactor

compactor = ReactiveCompactor(
    max_output_tokens=16384,
    recovery_limit=3
)

# Wenn Prompt zu lang → reaktiv kompaktieren
try:
    response = await api.call(messages)
except ContextLengthError:
    messages = await compactor.reactive_compact(messages)
    response = await api.call(messages)
```

## Micro Compact

```python
from opensin.compaction import MicroCompactor

compactor = MicroCompactor(
    interval=10,  # Alle 10 Turns
    boundary_message="--- Micro-compact boundary ---"
)

# Fügt Boundary-Nachricht alle N Turns ein
if self.turn_count % compactor.interval == 0:
    messages.append(compactor.create_boundary_message())
```

## Snip Compact (HISTORY_SNIP)

```python
from opensin.compaction import SnipCompactor

compactor = SnipCompactor(
    snip_boundary_detector=snip_boundary_detector,
    replay_handler=replay_handler
)

# Erkennt Snip-Grenzen und replayed bei Bedarf
for message in messages:
    snip_result = compactor.check_snip_boundary(message)
    if snip_result:
        replayed = replay_handler.replay(snip_result)
        yield replayed
```

## Build Post-Compact Messages

```python
async def build_post_compact_messages(
    messages: list[Message],
    compact_boundary: int
) -> list[Message]:
    """Buildet Nachrichten nach Kompaktierung."""
    # Behalte Boundary-Nachricht
    boundary = messages[compact_boundary]
    
    # Behalte letzte Nachrichten
    recent = messages[compact_boundary + 1:]
    
    # Zusammenfassung als System-Nachricht
    summary = await summarize(messages[:compact_boundary])
    
    return [
        SystemMessage(f"Previous conversation summary: {summary}"),
        boundary,
        *recent
    ]
```

## Token Warning State

```python
class TokenWarningState:
    def __init__(self):
        self.is_warning = False
        self.is_error = False
        self.compact_boundary_index = None
        self.micro_compact_boundary_index = None
    
    @property
    def needs_compaction(self) -> bool:
        return self.is_warning or self.is_error
```

## Circuit Breaker

```python
class CompactionCircuitBreaker:
    def __init__(self, max_failures: int = 3):
        self.max_failures = max_failures
        self.failure_count = 0
    
    def record_failure(self):
        self.failure_count += 1
    
    def is_open(self) -> bool:
        return self.failure_count >= self.max_failures
    
    def reset(self):
        self.failure_count = 0
```

## Best Practices

1. **Auto Compact** — Standard für die meisten Use Cases
2. **Reactive Compact** — Fallback bei Prompt zu lang
3. **Micro Compact** — Regelmäßige Mini-Kompaktierungen
4. **Circuit Breaker** — Verhindert Endlos-Kompaktierung
5. **Summarizer Model** — Günstiges Modell für Zusammenfassung

## Next Steps

- [SIN ReAct Loop](/guide/sin-react-loop)
- [SIN Query Engine](/guide/sin-query-engine)
