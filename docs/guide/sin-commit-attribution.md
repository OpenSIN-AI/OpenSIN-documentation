# SIN Commit Attribution — Code Change Tracking

> **OpenSIN's Commit Attribution** — Geklont aus Claude Code's commitAttribution.ts. Agenten-Code-Änderungen tracken.

## Implementation

```python
from opensin.git import CommitAttribution

attribution = CommitAttribution(
    repo_path="/path/to/repo",
    agent_name="coding-agent"
)

# Track commit
await attribution.track(
    commit_hash="abc123",
    agent_name="coding-agent",
    files_changed=["src/main.py", "tests/test_main.py"]
)

# Get attribution
stats = await attribution.get_stats()
print(f"Agent {stats.agent_name} changed {stats.files_changed} files")
```

## Attribution State

```python
class AttributionState:
    def __init__(self):
        self.commits = []
        self.files_changed = set()
        self.lines_added = 0
        self.lines_deleted = 0
```

## Best Practices

1. **Track all commits** — Alle Agent-Commits tracken
2. **Attribute correctly** — Richtigen Agenten zuordnen
3. **Generate reports** — Regelmäßige Reports erstellen
4. **Monitor quality** — Code-Qualität tracken
5. **Integrate with CI** — In CI/CD integrieren

## Next Steps

- [SIN File History](/guide/sin-file-history)
- [SIN Tool System](/guide/sin-tool-system)
