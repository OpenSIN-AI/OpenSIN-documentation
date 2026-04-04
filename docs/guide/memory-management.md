# Memory Management Guide

Master agent memory for better context and persistence.

## Memory Types

| Type | Duration | Use Case |
|------|----------|----------|
| Session Memory | Single session | Conversation context |
| Persistent Memory | Across sessions | Long-term knowledge |
| Shared Memory | Team-wide | Shared context |
| Vector Memory | Semantic search | Relevant context retrieval |

## Session Memory

```python
from opensin import Agent

agent = Agent(
    name="assistant",
    memory_enabled=True,
    memory_max_tokens=8000,
    memory_strategy="sliding_window"
)

# Memory is automatically managed
await agent.send("My name is Alice")
response = await agent.send("What's my name?")  # "Alice"
```

## Persistent Memory

```python
from opensin import PersistentMemory

memory = PersistentMemory(
    path=".sin/memory/agent.json",
    max_entries=1000,
    ttl=86400  # 24 hours
)

# Store facts
memory.set("user_name", "Alice")
memory.set("preferences", {"theme": "dark"})

# Retrieve facts
name = memory.get("user_name")
```

## Vector Memory

```python
from opensin import VectorMemory

memory = VectorMemory(
    embedding_model="text-embedding-3-small",
    dimension=1536,
    max_entries=10000
)

# Store documents
memory.add("Python is a programming language", metadata={"type": "fact"})
memory.add("OpenSIN supports multiple LLMs", metadata={"type": "feature"})

# Search by relevance
results = memory.search("What programming languages are supported?")
```

## Memory Strategies

### Sliding Window

```python
# Keeps most recent messages, drops oldest
agent.config.memory_strategy = "sliding_window"
agent.config.memory_max_tokens = 8000
```

### Summary

```python
# Summarizes old messages
agent.config.memory_strategy = "summary"
agent.config.compact_threshold = 0.8
```

### Hybrid

```python
# Combines sliding window with vector search
agent.config.memory_strategy = "hybrid"
agent.config.memory_max_tokens = 16000
agent.config.vector_memory_enabled = True
```

## Memory Optimization

### Reduce Memory Usage

```python
# Compact memory
await agent.memory.compact()

# Clear old entries
await agent.memory.cleanup(max_age=3600)

# Remove irrelevant entries
await agent.memory.prune(threshold=0.3)
```

### Monitor Memory

```python
# Get memory stats
stats = agent.memory.stats()
print(f"Entries: {stats.entries}")
print(f"Tokens: {stats.tokens}")
print(f"Hit rate: {stats.hit_rate}%")
```

## Best Practices

1. **Set appropriate limits** — Don't let memory grow unbounded
2. **Use vector memory for large knowledge bases** — Better than linear search
3. **Compact regularly** — Prevent token limit issues
4. **Persist important facts** — Don't lose critical information
5. **Monitor memory usage** — Track memory stats

## Next Steps

- [Agent Configuration](/guide/agent-configuration)
- [Performance Optimization](/guide/performance-optimization)
