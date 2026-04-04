# SIN Sticky Header Latches — Prompt Cache Preservation

> **OpenSIN's Sticky Latches** — Geklont aus Claude Code. Einmal aktiviert, bleibt ein Feature für die ganze Session an → verhindert Prompt Cache Busts.

## Das Problem

Jedes Mal wenn du ein Feature an/ausschaltest, ändert sich der System Prompt → der gesamte Prompt Cache wird ungültig → hohe Kosten.

## Die Lösung: Sticky-On Latches

```python
from opensin.cache import StickyLatch

latch = StickyLatch()

# Einmal aktivieren → bleibt für ganze Session an
await latch.activate("fast_mode")

# Alle folgenden Requests nutzen denselben System Prompt
# → Maximale Cache Hits!

# Verfügbare Latches
latches = [
    "fast_mode",        # Schnelles Modell
    "afk_mode",         # AFK Modus
    "cache_editing",    # Cache Editing
    "thinking_clear",   # Thinking deaktivieren
]
```

## Cache Preservation Pattern

```python
class QueryEngine:
    def __init__(self):
        self.active_latches = set()
        
    async def submit_message(self, content: str):
        # System Prompt basiert auf aktiven Latches
        system_prompt = self.build_system_prompt(
            latches=self.active_latches
        )
        
        # Da sich Latches nicht ändern, ist der Prefix immer gleich
        # → Byte-identische API Requests → Maximale Cache Hits
        async for event in self.react_loop(system_prompt):
            yield event
```

## Implementation

```python
class StickyLatch:
    def __init__(self):
        self._active: set[str] = set()
    
    async def activate(self, latch: str):
        """Latch aktivieren — kann nicht deaktiviert werden."""
        self._active.add(latch)
        
    def is_active(self, latch: str) -> bool:
        return latch in self._active
    
    def get_active(self) -> frozenset[str]:
        return frozenset(self._active)
    
    def build_system_prompt(self, base_prompt: str) -> str:
        """Baue System Prompt basierend auf aktiven Latches."""
        parts = [base_prompt]
        
        if "fast_mode" in self._active:
            parts.append(FAST_MODE_PROMPT)
        if "afk_mode" in self._active:
            parts.append(AFK_MODE_PROMPT)
        if "cache_editing" in self._active:
            parts.append(CACHE_EDITING_PROMPT)
            
        return "\n\n".join(parts)
```

## Performance Impact

| Scenario | Cache Hit Rate | Cost per 100 Requests |
|----------|---------------|----------------------|
| Ohne Latches | 20% | $3.00 |
| Mit Latches | 80% | $0.60 |
| **Ersparnis** | **4x** | **$2.40** |

## Best Practices

1. **Früh aktivieren** — Latches vor dem ersten Request setzen
2. **Nicht deaktivieren** — Einmal an = immer an
3. **Wenige Latches** — Nur wirklich benötigte aktivieren
4. **Monitor Cache** — Tracke Cache Hit Rate

## Next Steps

- [Cost Optimization](/guide/agent-cost-optimization)
- [SIN Query Engine](/guide/sin-query-engine)
