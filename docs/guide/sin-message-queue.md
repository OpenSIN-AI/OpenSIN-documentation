# SIN Message Queue — Command Priority System

> **OpenSIN's Message Queue** — Geklont aus Claude Code's messageQueueManager.ts. Priorisierte Command-Verarbeitung.

## Architecture

```
User Input → Message Queue → Priority Sort → Process → Remove from Queue
```

## Queue Implementation

```python
from opensin.queue import MessageQueue

queue = MessageQueue(
    max_size=100,
    priority_levels=5
)

# Command mit Priority hinzufügen
await queue.add(
    command="/review",
    priority=1,  # 1 = highest
    content="Review the current PR"
)

# Commands nach Priority sortiert abrufen
commands = await queue.get_commands_by_max_priority()
```

## Priority System

| Priority | Level | Example |
|----------|-------|---------|
| 1 | Critical | /stop, /abort |
| 2 | High | /review, /fix |
| 3 | Medium | /explain, /search |
| 4 | Low | /help, /config |
| 5 | Background | /dream, /summarize |

## Slash Command Detection

```python
from opensin.queue import is_slash_command

def is_slash_command(message: str) -> bool:
    """Prüft ob Nachricht ein Slash Command ist."""
    return message.strip().startswith('/')

# Remove from queue after processing
await queue.remove(command_id)
```

## Command Lifecycle

```python
from opensin.queue import notify_command_lifecycle

# Notify lifecycle events
await notify_command_lifecycle("start", command_id)
await notify_command_lifecycle("complete", command_id)
await notify_command_lifecycle("error", command_id, error=error)
```

## Best Practices

1. **Priority-based processing** — Wichtige Commands zuerst
2. **Max queue size** — Verhindert unbounded growth
3. **Lifecycle notifications** — Track Command-Status
4. **Slash command detection** — Erkennne Commands in Messages
5. **Remove after processing** — Clean up processed Commands

## Next Steps

- [SIN Commands](/guide/sin-commands)
- [SIN ReAct Loop](/guide/sin-react-loop)
