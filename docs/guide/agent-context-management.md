# Agent Context Management

Optimize context for better agent performance.

## Context Window

| Model | Context Window | Practical Limit |
|-------|---------------|-----------------|
| GPT-4 | 128K tokens | ~100K tokens |
| GPT-3.5 | 16K tokens | ~12K tokens |
| Claude Sonnet | 200K tokens | ~150K tokens |
| Claude Haiku | 200K tokens | ~150K tokens |
| Gemini Pro | 32K tokens | ~25K tokens |

## Context Budget

```python
from opensin.context import ContextBudget

budget = ContextBudget(
    total_tokens=8000,
    allocation={
        "system_prompt": 500,    # 6%
        "context": 3000,         # 38%
        "conversation": 2000,    # 25%
        "tools": 500,            # 6%
        "response": 2000,        # 25%
    }
)
```

## Context Optimization

### 1. Relevant Context Retrieval

```python
from opensin.context import ContextRetriever

retriever = ContextRetriever(
    strategy="semantic_search",  # or "keyword", "hybrid"
    top_k=5,
    relevance_threshold=0.7
)

context = await retriever.retrieve(query, knowledge_base)
```

### 2. Context Compression

```python
from opensin.context import ContextCompressor

compressor = ContextCompressor(
    strategy="summarize",  # or "extract", "hybrid"
    target_tokens=2000,
    preserve_key_facts=True
)

compressed = await compressor.compress(large_context)
```

### 3. Context Prioritization

```python
from opensin.context import ContextPrioritizer

prioritizer = ContextPrioritizer(
    weights={
        "recency": 0.3,
        "relevance": 0.4,
        "importance": 0.3
    }
)

prioritized = await prioritizer.rank(context_entries, query)
```

## Context Strategies

### Sliding Window

```python
# Keep most recent messages
agent.config.memory_strategy = "sliding_window"
agent.config.memory_max_tokens = 4000
```

### Summary

```python
# Summarize old messages
agent.config.memory_strategy = "summary"
agent.config.compact_threshold = 0.8
```

### Hybrid

```python
# Combine sliding window with vector search
agent.config.memory_strategy = "hybrid"
agent.config.memory_max_tokens = 8000
agent.config.vector_memory_enabled = True
```

## Context Monitoring

```python
from opensin.context import ContextMonitor

monitor = ContextMonitor(agent)

# Get context stats
stats = monitor.get_stats()
print(f"Tokens used: {stats.tokens_used}/{stats.tokens_total}")
print(f"Context fill: {stats.fill_percentage}%")
print(f"Messages: {stats.message_count}")
```

## Best Practices

1. **Budget context** — Allocate tokens wisely
2. **Retrieve relevant info** — Don't dump everything
3. **Compress when needed** — Summarize old context
4. **Monitor usage** — Track context fill percentage
5. **Test with limits** — Ensure agent works at max context

## Next Steps

- [Memory Management](/guide/memory-management)
- [Performance Optimization](/guide/performance-optimization)
CTXMGRT

cat > docs/guide/agent-tool-creation.md << 'TOOLCREATE'
# Agent Tool Creation

Build custom tools for OpenSIN agents.

## Tool Anatomy

```python
from opensin.tools import Tool

tool = Tool(
    name="web_search",
    description="Search the web for information",
    parameters={
        "query": {
            "type": "string",
            "description": "Search query",
            "required": True
        },
        "num_results": {
            "type": "integer",
            "description": "Number of results",
            "default": 5
        }
    },
    handler=web_search_handler
)
```

## Tool Handler

```python
async def web_search_handler(query: str, num_results: int = 5) -> dict:
    """Search the web and return results."""
    results = await search_engine.search(query, limit=num_results)
    return {
        "results": [
            {"title": r.title, "url": r.url, "snippet": r.snippet}
            for r in results
        ],
        "total": len(results)
    }
```

## Tool Registration

```python
# Register with agent
agent.register_tool(tool)

# Register multiple tools
agent.register_tools([tool1, tool2, tool3])

# Register from file
agent.register_tool_from_file("tools/web_search.py")
```

## Tool Testing

```python
from opensin.tools import ToolTester

tester = ToolTester(tool)

# Test with valid input
result = await tester.test({"query": "OpenSIN AI"})
assert result["total"] > 0

# Test with invalid input
result = await tester.test({"query": ""})
assert "error" in result
```

## Tool Categories

| Category | Examples |
|----------|----------|
| Web | Search, fetch, scrape |
| Code | Execute, analyze, debug |
| Data | Query, transform, visualize |
| Communication | Email, Slack, SMS |
| File | Read, write, search |
| Math | Calculate, statistics |
| Media | Image, audio, video |

## Best Practices

1. **Clear descriptions** — Help the agent understand when to use the tool
2. **Type-safe parameters** — Use JSON Schema for validation
3. **Error handling** — Return structured errors
4. **Timeouts** — Prevent hanging tool calls
5. **Rate limiting** — Protect external APIs
6. **Testing** — Test tools thoroughly before registering

## Next Steps

- [Plugin Development](/guide/plugin-development)
- [Agent Configuration](/guide/agent-configuration)
TOOLCREATE

echo "DONE: Created prompt injection defense, context management, tool creation docs"