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
agent.register_tool(tool)
agent.register_tools([tool1, tool2, tool3])
agent.register_tool_from_file("tools/web_search.py")
```

## Tool Testing

```python
from opensin.tools import ToolTester

tester = ToolTester(tool)
result = await tester.test({"query": "OpenSIN AI"})
assert result["total"] > 0
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

1. Clear descriptions — Help the agent understand when to use the tool
2. Type-safe parameters — Use JSON Schema for validation
3. Error handling — Return structured errors
4. Timeouts — Prevent hanging tool calls
5. Rate limiting — Protect external APIs
6. Testing — Test tools thoroughly before registering

## Next Steps

- [Plugin Development](/guide/plugin-development)
- [Agent Configuration](/guide/agent-configuration)
