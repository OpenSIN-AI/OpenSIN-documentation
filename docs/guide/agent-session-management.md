# Agent Session Management

Manage agent sessions for better user experiences.

## Session Lifecycle

```
Create → Active → Idle → Expire → Archive
```

## Session Creation

```python
from opensin.session import SessionManager

manager = SessionManager()

# Create session
session = await manager.create(
    agent="researcher",
    user_id="user_123",
    metadata={"source": "web", "project": "research"}
)

print(f"Session ID: {session.id}")
print(f"Expires at: {session.expires_at}")
```

## Session State

```python
# Save session state
await session.save_state({
    "context": current_context,
    "memory": agent.memory.entries,
    "variables": user_variables
})

# Restore session state
state = await session.restore_state()
agent.memory.entries = state["memory"]
```

## Session Persistence

```python
from opensin.session import SessionStore

store = SessionStore(
    backend="redis",  # or "database", "memory"
    ttl=3600,  # 1 hour
    max_sessions=10000
)

# Save session
await store.save(session)

# Load session
session = await store.load(session_id)

# Delete session
await store.delete(session_id)
```

## Session Management

```python
# List active sessions
sessions = await manager.list(user_id="user_123")

# Get session details
session = await manager.get(session_id)

# Update session
await manager.update(session_id, metadata={"status": "paused"})

# End session
await manager.end(session_id)

# Archive session
await manager.archive(session_id)
```

## Session Recovery

```python
# Recover interrupted session
recovered = await manager.recover(session_id)

# Resume from checkpoint
await session.resume_from_checkpoint(checkpoint_id)
```

## Session Analytics

```python
from opensin.session import SessionAnalytics

analytics = SessionAnalytics(manager)

# Get session metrics
metrics = await analytics.get_metrics(
    period="7d",
    group_by="agent"
)

print(f"Total sessions: {metrics.total_sessions}")
print(f"Avg duration: {metrics.avg_duration}min")
print(f"Avg messages: {metrics.avg_messages}")
print(f"Completion rate: {metrics.completion_rate}%")
```

## Best Practices

1. **Set appropriate TTL** — Balance between persistence and resource usage
2. **Save state regularly** — Don't lose user context
3. **Handle interruptions** — Allow session recovery
4. **Monitor usage** — Track session metrics
5. **Clean up old sessions** — Archive or delete expired sessions

## Next Steps

- [Memory Management](/guide/memory-management)
- [Agent Configuration](/guide/agent-configuration)
