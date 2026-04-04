# SIN Tool Orchestration — StreamingToolExecutor

> **OpenSIN's Tool Orchestration** — Geklont aus Claude Code's StreamingToolExecutor.ts und toolOrchestration.ts. Parallele Tool-Ausführung.

## Architecture

```
API Response → Parse Tool Uses → Group by Type → Execute in Parallel
                                                    ↓
                                              Collect Results
                                                    ↓
                                              Build Messages
```

## StreamingToolExecutor

```python
from opensin.tools import StreamingToolExecutor

executor = StreamingToolExecutor(
    max_concurrent=5,
    timeout=30,
    retry_on_failure=True
)

# Führt Tools parallel aus mit Streaming
async for result in executor.execute(tool_uses):
    yield result
```

## Tool Orchestration

```python
from opensin.tools import run_tools

async def run_tools(
    tool_uses: list[ToolUse],
    tools: Tools,
    can_use_tool: CanUseToolFn,
    tool_use_context: ToolUseContext
) -> list[Message]:
    """Führt Tools aus und gibt Result-Nachrichten zurück."""
    
    # Gruppiere Tools nach Typ für parallele Ausführung
    grouped = group_tools_by_type(tool_uses)
    
    results = []
    for group in grouped:
        # Führe Gruppe parallel aus
        group_results = await asyncio.gather(*[
            execute_single_tool(tool, tools, can_use_tool, tool_use_context)
            for tool in group
        ])
        results.extend(group_results)
    
    return build_tool_result_messages(results)
```

## Parallel Tool Execution

```python
async def execute_parallel_tools(
    tools: list[ToolUse],
    max_concurrent: int = 5
) -> list[ToolResult]:
    """Führt Tools parallel aus mit Concurrency-Limit."""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def execute_with_semaphore(tool: ToolUse) -> ToolResult:
        async with semaphore:
            return await tool.execute()
    
    tasks = [execute_with_semaphore(tool) for tool in tools]
    return await asyncio.gather(*tasks)
```

## Tool Result Budget

```python
from opensin.tools import apply_tool_result_budget

def apply_tool_result_budget(
    tool_results: list[ToolResult],
    max_tokens: int = 50000
) -> list[ToolResult]:
    """Begrenzt Tool-Result-Tokens."""
    total_tokens = sum(r.token_count for r in tool_results)
    
    if total_tokens <= max_tokens:
        return tool_results
    
    # Truncate largest results first
    sorted_results = sorted(tool_results, key=lambda r: -r.token_count)
    truncated = []
    remaining_budget = max_tokens
    
    for result in sorted_results:
        if result.token_count <= remaining_budget:
            truncated.append(result)
            remaining_budget -= result.token_count
        else:
            truncated.append(result.truncate(remaining_budget))
            remaining_budget = 0
    
    return truncated
```

## Tool Grouping

```python
def group_tools_by_type(tool_uses: list[ToolUse]) -> list[list[ToolUse]]:
    """Gruppiert Tools nach Typ für parallele Ausführung."""
    groups = {}
    for tool_use in tool_uses:
        tool_type = tool_use.tool_type
        if tool_type not in groups:
            groups[tool_type] = []
        groups[tool_type].append(tool_use)
    
    # Read-only Tools können parallel ausgeführt werden
    # Schreib-Tools sollten sequentiell ausgeführt werden
    parallel_groups = []
    for tool_type, tools in groups.items():
        if is_read_only_tool(tool_type):
            parallel_groups.append(tools)  # Parallel
        else:
            for tool in tools:
                parallel_groups.append([tool])  # Sequentiell
    
    return parallel_groups
```

## Best Practices

1. **Parallel wo möglich** — Read-only Tools parallel ausführen
2. **Concurrency Limit** — Max 5 parallele Tools
3. **Result Budget** — Tool-Results auf max Tokens begrenzen
4. **Error Handling** — Einzelne Tool-Fehler ignorieren
5. **Streaming** — Tool-Results streamen für bessere UX

## Next Steps

- [SIN Tool System](/guide/sin-tool-system)
- [SIN ReAct Loop](/guide/sin-react-loop)
