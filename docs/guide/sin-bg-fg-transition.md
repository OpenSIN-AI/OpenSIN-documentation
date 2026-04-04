# SIN Background↔Foreground Transition

> **OpenSIN's Agent Transition** — Geklont aus Claude Code's AgentTool.tsx. Sync Agents können mid-execution zu Background wechseln.

## Architektur

```
Foreground Agent → backgroundAll() → Cleanup → Background Agent → Output File → Monitor
```

## Background-to-Foreground Transition

```python
from opensin.subagent import BackgroundAgent, ForegroundAgent

# Starte als Foreground Agent
fg_agent = ForegroundAgent(
    name="researcher",
    task="Research AI trends and write a report"
)

# ... Agent arbeitet ...

# Mid-execution zu Background wechseln
bg_agent = await fg_agent.background_all(
    output_file="research_output.md",
    progress_interval=30  # Alle 30s Progress update
)

# Progress monitoren
async for progress in bg_agent.watch_progress():
    print(f"Progress: {progress.percentage}%")

# Wenn fertig → zurück zu Foreground
fg_agent = await bg_agent.transition_to_foreground()
result = await fg_agent.continue_execution()
```

## Background Agent Lifecycle

```python
class BackgroundAgent:
    async def start(self):
        # 1. MCP Connections cleanup
        await self.cleanup_mcp_connections()
        
        # 2. Session Hooks cleanup
        await self.cleanup_session_hooks()
        
        # 3. Independent progress tracking
        self.progress_tracker = ProgressTracker()
        
        # 4. Start execution
        await self.execute()
    
    async def watch_progress(self):
        """Stream Progress Updates."""
        while self.is_running:
            yield self.progress_tracker.get_update()
            await asyncio.sleep(self.progress_interval)
```

## Output File Monitoring

```python
from opensin.subagent import OutputFileMonitor

monitor = OutputFileMonitor(
    path="research_output.md",
    poll_interval=5  # Alle 5s prüfen
)

async for change in monitor.watch():
    print(f"File updated: {change.size} bytes")
    print(f"New content: {change.added_content}")
```

## Best Practices

1. **Cleanup MCP** — Connections vor Backgrounding schließen
2. **Cleanup Hooks** — Session Hooks aufräumen
3. **Independent Progress** — Eigenes Progress Tracking
4. **Output File** — Ergebnisse in Datei schreiben
5. **Graceful Transition** — Sauber zwischen Foreground/Background wechseln

## Next Steps

- [SIN Subagents](/guide/sin-subagents)
- [SIN Fork Subagent](/guide/sin-fork-subagent)
