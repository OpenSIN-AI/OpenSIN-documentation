# SIN Parallel Prefetch — Hidden Latency Behind User Typing

> **OpenSIN's Parallel Prefetch** — Geklont aus Claude Code. Lädt Context im Hintergrund während User tippt.

## Das Problem

Context Loading (SIN.md, Memory, System Context) dauert 200-500ms → spürbare Verzögerung.

## Die Lösung: Parallel Prefetch nach erstem Render

```python
from opensin.context import ParallelPrefetcher

prefetcher = ParallelPrefetcher()

# Nach erstem Render — User tippt bereits
await prefetcher.start_all([
    prefetch_user_context,      # ~100ms
    prefetch_system_context,    # ~150ms
    prefetch_tips,              # ~50ms
    prefetch_file_counts,       # ~100ms
])

# Context ist ready bevor User erste Nachricht abschickt
```

## Implementation

```python
class ParallelPrefetcher:
    def __init__(self):
        self._tasks = []
        self._results = {}
    
    async def start_all(self, prefetches: list[Callable]):
        """Startet alle Prefetches parallel."""
        self._tasks = [
            asyncio.create_task(self._run_prefetch(p))
            for p in prefetches
        ]
    
    async def _run_prefetch(self, prefetch: Callable):
        """Führt einzelnen Prefetch aus."""
        name = prefetch.__name__
        try:
            self._results[name] = await prefetch()
        except Exception as e:
            self._results[name] = None
    
    async def get_result(self, name: str):
        """Wartet auf spezifischen Prefetch."""
        for task in self._tasks:
            if task.get_name() == name:
                return await task
        return self._results.get(name)
    
    async def wait_all(self):
        """Wartet auf alle Prefetches."""
        await asyncio.gather(*self._tasks)
    
    @property
    def results(self) -> dict:
        return self._results.copy()
```

## Performance Impact

| Scenario | Context Load Time | Perceived Latency |
|----------|------------------|-------------------|
| Sequential | 400ms | 400ms |
| Parallel Prefetch | 400ms | 0ms (hidden behind typing) |

## Prefetch Items

| Item | Duration | Priority |
|------|----------|----------|
| User Context | ~100ms | High |
| System Context | ~150ms | High |
| Tips | ~50ms | Medium |
| File Counts | ~100ms | Low |
| Memory Index | ~200ms | High |
| Plugin List | ~50ms | Medium |

## Best Practices

1. **After first render** — User tippt bereits
2. **Parallel execution** — Alle gleichzeitig
3. **Error tolerance** — Einzelne Failures ok
4. **Cache results** — Nicht doppelt laden

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN Eager Input](/guide/sin-eager-input-capture)
