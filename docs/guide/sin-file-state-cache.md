# SIN File State Cache — Optimized File Reading

> **OpenSIN's File State Cache** — Geklont aus Claude Code's fileStateCache.ts. Cache für Datei-Zustände.

## Architecture

```
File Read → Check Cache → Hit: Return Cached → Miss: Read & Cache
```

## Implementation

```python
from opensin.cache import FileStateCache

cache = FileStateCache(
    max_size=1000,  # Max 1000 files
    ttl=3600,       # 1 hour TTL
    eviction_policy="lru"
)

# Read file with caching
content = await cache.read("src/main.py")

# Invalidate cache
await cache.invalidate("src/main.py")

# Clear all
await cache.clear()
```

## Clone File State Cache

```python
from opensin.cache import clone_file_state_cache

def clone_file_state_cache(source: FileStateCache) -> FileStateCache:
    """Klont File State Cache für Subagents."""
    cloned = FileStateCache(
        max_size=source.max_size,
        ttl=source.ttl,
        eviction_policy=source.eviction_policy
    )
    
    # Copy all entries
    for path, entry in source.entries.items():
        cloned.entries[path] = entry.copy()
    
    return cloned
```

## Cache Invalidation

```python
async def invalidate_on_change(self, path: str):
    """Invalidiert Cache wenn Datei sich ändert."""
    if await self.file_watcher.has_changed(path):
        await self.invalidate(path)
```

## Best Practices

1. **LRU eviction** — Least Recently Used zuerst entfernen
2. **TTL** — Time-to-live für alle Entries
3. **Watch files** — Automatische Invalidierung bei Änderungen
4. **Clone for subagents** — Jeder Subagent bekommt eigenen Cache
5. **Monitor hit rate** — Cache Hit Rate tracken

## Next Steps

- [SIN File History](/guide/sin-file-history)
- [Performance Optimization](/guide/performance-optimization)
