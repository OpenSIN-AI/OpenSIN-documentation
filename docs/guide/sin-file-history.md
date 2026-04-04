# SIN File History — Change Tracking

> **OpenSIN's File History** — Geklont aus Claude Code's fileHistory.ts. Verfolgt Dateiänderungen über Zeit.

## Implementation

```python
from opensin.filehistory import FileHistory

history = FileHistory(
    enabled=True,
    max_snapshots=100,
    snapshot_interval=300  # 5 minutes
)

# Create snapshot
await history.snapshot("src/main.py")

# Get history
changes = await history.get_history("src/main.py")
for change in changes:
    print(f"{change.timestamp}: {change.type}")
```

## Snapshot System

```python
class FileSnapshot:
    def __init__(self, path: str, content: str, timestamp: float):
        self.path = path
        self.content = content
        self.timestamp = timestamp
        self.hash = hashlib.md5(content.encode()).hexdigest()

class FileHistory:
    def __init__(self, max_snapshots: int = 100):
        self.snapshots: dict[str, list[FileSnapshot]] = {}
        self.max_snapshots = max_snapshots
    
    async def snapshot(self, path: str):
        """Erstellt Snapshot einer Datei."""
        content = await self.read_file(path)
        snapshot = FileSnapshot(path, content, time.time())
        
        if path not in self.snapshots:
            self.snapshots[path] = []
        
        self.snapshots[path].append(snapshot)
        
        # Limit snapshots
        if len(self.snapshots[path]) > self.max_snapshots:
            self.snapshots[path] = self.snapshots[path][-self.max_snapshots:]
```

## Change Detection

```python
async def detect_changes(self, path: str) -> list[FileChange]:
    """Erkennt Änderungen seit letztem Snapshot."""
    current_content = await self.read_file(path)
    snapshots = self.snapshots.get(path, [])
    
    if not snapshots:
        return []
    
    last_snapshot = snapshots[-1]
    if last_snapshot.hash != hashlib.md5(current_content.encode()).hexdigest():
        return [FileChange(
            path=path,
            type="modified",
            timestamp=time.time()
        )]
    
    return []
```

## Best Practices

1. **Enable by default** — File History sollte immer aktiv sein
2. **Limit snapshots** — Max 100 Snapshots pro Datei
3. **Regular snapshots** — Alle 5 Minuten oder bei Änderungen
4. **Cleanup old** — Alte Snapshots automatisch löschen
5. **Diff support** — Änderungen zwischen Snapshots anzeigen

## Next Steps

- [SIN File Memory](/guide/sin-file-memory)
- [SIN Debugging](/guide/agent-debugging)
