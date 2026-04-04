# SIN Scratchpad — Temporary Workspace

> **OpenSIN's Scratchpad** — Geklont aus Claude Code's scratchpad.ts. Temporärer Arbeitsbereich für Agenten.

## Implementation

```python
from opensin.scratchpad import Scratchpad

scratchpad = Scratchpad(
    base_path=".sin/scratchpad",
    max_size=100 * 1024 * 1024,  # 100MB
    ttl=86400  # 24 hours
)

# Create scratchpad file
path = await scratchpad.create("temp-analysis.txt")
await scratchpad.write(path, "Analysis results...")

# Read scratchpad
content = await scratchpad.read(path)

# Cleanup old files
await scratchpad.cleanup()
```

## Scratchpad Features

| Feature | Description |
|---------|-------------|
| Auto-cleanup | Alte Dateien automatisch löschen |
| Size limit | Max 100MB pro Session |
| TTL | 24 Stunden Lebensdauer |
| Session-scoped | Jede Session hat eigenen Scratchpad |
| Shared access | Agenten können Scratchpad teilen |

## Best Practices

1. **Auto-cleanup** — Alte Dateien automatisch löschen
2. **Size limits** — Max Größe pro Session
3. **Session-scoped** — Isolierte Scratchpads
4. **Shared when needed** — Explizites Sharing erlauben
5. **Monitor usage** — Scratchpad-Nutzung tracken

## Next Steps

- [SIN File History](/guide/sin-file-history)
- [SIN File State Cache](/guide/sin-file-state-cache)
