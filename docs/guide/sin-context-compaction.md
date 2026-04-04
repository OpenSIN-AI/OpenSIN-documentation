# SIN Context Compaction

> **OpenSIN's Context Management** — Verhindere Token-Limits in langen Sessions.

## Overview

Context Compaction fasst lange Konversationen automatisch zusammen bevor das Token-Limit erreicht wird.

## Wie es funktioniert

```
Session startet
    ↓
Context wächst mit jeder Nachricht
    ↓
80% des Limits erreicht → Compaction Trigger
    ↓
Zusammenfassung erstellen
    ↓
Original durch Summary ersetzen
    ↓
Weiter im kompaktierten Context
```

## Compaction Strategien

| Strategie | Beschreibung | Use Case |
|-----------|-------------|----------|
| `summarize` | Fasse Conversation zusammen | Allgemeine Sessions |
| `truncate` | Schneide alte Nachrichten ab | Kurze Sessions |
| `selective` | Behalte wichtige Messages | Code Review Sessions |
| `hierarchical` | Multi-Level Summaries | Sehr lange Sessions |

## Konfiguration

```python
from opensin import Agent, ContextCompactor

agent = Agent(
    name="assistant",
    model="gpt-4",
    compaction=ContextCompactor(
        strategy="summarize",
        threshold=0.8,      # 80% des Limits
        max_compactions=3,  # Max 3 Compactions
        circuit_breaker=True  # Stop bei Endlosschleife
    )
)
```

## Circuit Breaker

Nach 3 fehlgeschlagenen Compactions wird der Circuit Breaker aktiviert:

```python
# Circuit Breaker verhindert Endlos-Compaction
if compaction_failures >= 3:
    # Session warnen und manuelles Eingreifen fordern
    await agent.notify("⚠️ Context zu komplex. Bitte neue Session starten.")
```

## Manual Compaction

```bash
# Manuell compactieren
/sin compact

# Compaction Status
/sin context
```

## Best Practices

1. **Threshold 0.8** — Früh genug compactieren
2. **Circuit Breaker** — Immer aktivieren
3. **Selective** — Wichtige Infos behalten
4. **Monitoring** — Compaction Events loggen

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN Subagents](/guide/sin-subagents)
