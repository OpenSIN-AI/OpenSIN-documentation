# SIN Session Storage — Persistent Session Data

> **OpenSIN's Session Storage** — Geklont aus Claude Code's sessionStorage.ts. Persistente Session-Daten.

## Implementation

```python
from opensin.session import SessionStorage

storage = SessionStorage(
    backend="filesystem",  # or "database", "redis"
    path=".sin/sessions",
    ttl=86400 * 30  # 30 days
)

# Store session data
await storage.save(session_id, {
    "messages": messages,
    "usage": usage,
    "cost": cost,
    "metadata": metadata
})

# Load session data
data = await storage.load(session_id)

# Record transcript
await storage.record_transcript(session_id, transcript)
```

## Transcript Recording

```python
async def record_transcript(session_id: str, transcript: list[Message]):
    """Speichert Session-Transkript."""
    await storage.save(f"{session_id}/transcript.json", transcript)
```

## Content Replacement Tracking

```python
async def record_content_replacement(session_id: str, old: str, new: str):
    """Trackt Content-Ersetzungen."""
    await storage.append(f"{session_id}/replacements.json", {
        "old": old,
        "new": new,
        "timestamp": time.time()
    })
```

## Best Practices

1. **Persist important data** — Messages, Usage, Cost speichern
2. **TTL** — Alte Sessions automatisch löschen
3. **Compress** — Große Transcripts komprimieren
4. **Secure** — Sensible Daten verschlüsseln
5. **Backup** — Regelmäßige Backups erstellen

## Next Steps

- [SIN Session Memory](/guide/sin-session-memory)
- [SIN File History](/guide/sin-file-history)
