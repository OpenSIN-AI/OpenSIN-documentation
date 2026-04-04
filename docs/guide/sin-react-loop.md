# SIN ReAct Loop — Core Agent Execution Engine

> **OpenSIN's ReAct Loop** — Geklont aus Claude Code's query.ts. Der zentrale Ausführungsloop für alle Agenten.

## Architektur

```
User Input → System Prompt → API Call → Parse Response
                                      ↓
                              ┌──── Tool Use? ────┐
                              ↓                   ↓
                         Text Output         Execute Tool
                              ↓                   ↓
                        Yield Event        Tool Result → API Call
                                              ↓
                                        Continue Loop
```

## Implementation

```python
from opensin.engine import ReActLoop

loop = ReActLoop(
    agent=agent,
    system_prompt=system_prompt,
    tools=tools,
    max_turns=50,
    max_tokens=100000
)

async for event in loop.run(user_input):
    if event.type == "tool_use":
        result = await execute_tool(event.tool_name, event.input)
        loop.submit_tool_result(event.tool_id, result)
    elif event.type == "text":
        print(event.content)
    elif event.type == "error":
        print(f"Error: {event.message}")
        break
```

## Token Budget Tracking

```python
class TokenBudget:
    def __init__(self, max_tokens: int = 100000):
        self.max_tokens = max_tokens
        self.used_tokens = 0
        self.continuation_count = 0
    
    def check(self, estimated: int) -> bool:
        return self.used_tokens + estimated <= self.max_tokens
    
    def record(self, tokens: int):
        self.used_tokens += tokens
    
    def needs_continuation(self) -> bool:
        return self.used_tokens > self.max_tokens * 0.9
```

## Context Compaction

```python
async def compact_context(self, messages: list[Message]) -> list[Message]:
    """Fasst alte Nachrichten zusammen wenn Token-Limit erreicht."""
    if self.token_count(messages) > self.compact_threshold:
        # Letzte 5 Nachrichten behalten
        recent = messages[-5:]
        
        # Ältere zusammenfassen
        summary = await self.summarize(messages[:-5])
        
        return [SystemMessage(summary)] + recent
    return messages
```

## Tool Execution Pipeline

```python
async def execute_tool(self, tool_name: str, tool_input: dict) -> ToolResult:
    """Führt Tool aus mit Hook-Integration."""
    # PreToolUse Hooks
    for hook in self.hooks.get("PreToolUse", []):
        result = await hook.run(tool_name, tool_input)
        if not result.continue_:
            return ToolResult(error=result.systemMessage)
    
    # Tool ausführen
    tool = self.tools.get(tool_name)
    result = await tool.execute(tool_input)
    
    # PostToolUse Hooks
    for hook in self.hooks.get("PostToolUse", []):
        await hook.run(tool_name, result)
    
    return result
```

## Error Recovery

```python
async def handle_error(self, error: Exception) -> Optional[Message]:
    """Behandelt API-Fehler mit Recovery-Strategien."""
    if isinstance(error, ContextLengthError):
        # Context kompaktieren und retry
        self.messages = await self.compact_context(self.messages)
        return await self.retry_api_call()
    
    elif isinstance(error, RateLimitError):
        # Warten und retry
        await asyncio.sleep(error.retry_after)
        return await self.retry_api_call()
    
    elif isinstance(error, MaxTokensError):
        # Max 3 Recovery-Versuche
        if self.recovery_count < 3:
            self.recovery_count += 1
            return await self.retry_with_higher_limit()
    
    return None
```

## Best Practices

1. **Async Generator** — Stream Events in Echtzeit
2. **Token Budget** — Verhindert unerwartete Kosten
3. **Context Compaction** — Verhindert Token-Limit-Überschreitung
4. **Error Recovery** — Automatische Fehlerbehebung
5. **Hook Integration** — Pre/Post Tool Execution Hooks

## Next Steps

- [SIN Query Engine](/guide/sin-query-engine)
- [SIN Hook System](/guide/sin-hook-system)
