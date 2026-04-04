# SIN Session Memory — Auto-Extraction via Forked Subagent

> **OpenSIN's Session Memory** — Geklont aus Claude Code's sessionMemory.ts. Automatische Extraktion von Session-Zusammenfassungen.

## Architektur

```
Session läuft → Token Threshold erreicht → Forked Subagent extrahiert Summary → Session Memory File
```

## Threshold-Based Triggering

```python
from opensin.memory import SessionMemory

session_memory = SessionMemory(
    agent=agent,
    trigger_tokens=50000,      # Nach 50K Tokens
    trigger_tool_calls=20,     # ODER nach 20 Tool Calls
    no_active_tool_use=True    # Nur wenn kein Tool aktiv
)

# Prüfe ob Extraktion nötig
if session_memory.should_extract():
    await session_memory.extract_summary()
```

## Forked Subagent Extraction

```python
from opensin.subagent import ForkSubagent

class SessionMemory:
    async def extract_summary(self):
        """Extrahiert Session-Zusammenfassung via Forked Subagent."""
        # Forked Subagent nutzt gleichen Prompt Prefix → Cache Hit!
        fork = ForkSubagent(
            parent=self.agent,
            task="Zusammenfassen der wichtigsten Erkenntnisse dieser Session",
            cache_prefix=True
        )
        
        summary = await fork.execute()
        
        # Speichere in Session Memory File
        await self.save_session_summary(summary)
```

## Sequential Wrapper

```python
from opensin.memory import SequentialWrapper

# Verhindert parallele Extraktionen
wrapper = SequentialWrapper(session_memory.extract_summary)

# Nur eine Extraktion zur Zeit
await wrapper.run()  # Blockiert wenn bereits laufend
```

## Session Memory File Format

```markdown
# Session Summary — 2026-04-04

## Key Decisions
- Decided on REST API over GraphQL
- Chose PostgreSQL as database
- Implemented JWT authentication

## Code Changes
- Created `src/api/` directory
- Added user authentication module
- Set up database migrations

## Open Questions
- Need to decide on caching strategy
- Rate limiting approach TBD

## Next Steps
- Implement caching layer
- Add rate limiting
- Write API documentation
```

## Best Practices

1. **Threshold Triggering** — Nicht zu oft extrahieren
2. **Forked Subagent** — Gleicher Prefix für Cache Hits
3. **Sequential Wrapper** — Keine parallelen Extraktionen
4. **Structured Format** — Maschinenlesbar + menschlich lesbar
5. **Session-Scoped** — Jede Session hat eigenes Memory File

## Next Steps

- [SIN File Memory](/guide/sin-file-memory)
- [SIN Fork Subagent](/guide/sin-fork-subagent)
