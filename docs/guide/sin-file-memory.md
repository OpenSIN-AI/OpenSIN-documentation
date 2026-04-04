# SIN File-Based Memory — Persistent Agent Memory

> **OpenSIN's Memory System** — Geklont aus Claude Code's memdir.ts. Index + Topic Files für skalierbares Gedächtnis.

## Architektur

```
MEMORY.md (Index, max 200 lines, 25KB)
├── → logs/2026/04/2026-04-04.md (Daily Log)
├── → topics/user-preferences.md (Topic File)
├── → topics/project-architecture.md (Topic File)
└── → topics/api-patterns.md (Topic File)
```

## Two-Step Memory Saving

```python
from opensin.memory import MemoryManager

memory = MemoryManager(root_path=".sin/memory")

# Step 1: Topic File schreiben
await memory.write_topic(
    name="user-preferences",
    type="user",
    content="User prefers Python over JavaScript. Uses dark theme."
)

# Step 2: Pointer zu MEMORY.md hinzufügen
await memory.add_to_index(
    topic="user-preferences",
    description="User coding preferences and settings"
)
```

## Memory Types

| Type | Beschreibung | Beispiel |
|------|-------------|----------|
| `user` | Benutzer-Informationen | Name, Präferenzen |
| `feedback` | Feedback zu Agenten | "War zu ausführlich" |
| `project` | Projekt-Wissen | Architektur, Patterns |
| `reference` | Referenz-Material | API Docs, Best Practices |

## Assistant Daily Log Mode

```python
from opensin.memory import DailyLog

log = DailyLog(base_path=".sin/memory/logs")

# Append zu datums-basierter Log-Datei
await log.append(
    date="2026-04-04",
    entry="Discussed API design with user. Decided on REST over GraphQL."
)

# Nightly /dream: Logs zu Topic Files destillieren
await log.distill_to_topics()
```

## Session Memory Auto-Extraction

```python
from opensin.memory import SessionMemory

session_memory = SessionMemory(
    agent=agent,
    trigger_tokens=50000,  # Nach 50K Tokens
    trigger_tool_calls=20  # ODER nach 20 Tool Calls
)

# Automatische Extraktion wenn Thresholds erreicht
await session_memory.check_and_extract()
```

## Content Truncation with Warnings

```python
# MEMORY.md wird bei 200 lines oder 25KB gekappt
# Mit Warning die dem Modell sagt welches Limit feuerte

if memory.index_lines > 200:
    memory.truncate(max_lines=200)
    memory.add_warning("⚠️ Index capped at 200 lines. Oldest entries removed.")
    
if memory.index_size > 25000:
    memory.truncate(max_bytes=25000)
    memory.add_warning("⚠️ Index capped at 25KB. Oldest entries removed.")
```

## SIN.md Auto-Discovery

```python
from opensin.memory import SINMdLoader

loader = SINMdLoader(root_path="/path/to/project")

# Lädt alle SIN.md Dateien im Projekt-Hierarchie
sin_files = await loader.discover()

# Kombiniert relevante SIN.md Dateien basierend auf CWD
context = await loader.load_for_cwd("/path/to/project/src/api")
```

## Best Practices

1. **Two-Step Pattern** — Topic File → Index Pointer
2. **Daily Logs** — Für lange Sessions statt live Index
3. **Auto-Extraction** — Session Memory automatisch extrahieren
4. **Truncation Warnings** — Modell über Limits informieren
5. **SIN.md Hierarchie** — Projekt-Kontext auto-laden

## Next Steps

- [Memory Management](/guide/memory-management)
- [SIN.md System](/guide/sin-md-system)
