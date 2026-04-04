# SIN Query Engine — Core Conversation Engine

> **OpenSIN's QueryEngine** — Das Herzstück jedes OpenSIN Agenten. Verwaltet den kompletten Gesprächslebenszyklus.

## Architektur

```
User Input → QueryEngine.submitMessage() → Async Generator → LLM API → Tool Execution → Response
                  ↓                              ↓              ↓            ↓
           Message Store                  Stream Events   Tool Results  Compact
```

## QueryEngine Klasse

```python
from opensin.engine import QueryEngine

engine = QueryEngine(
    agent=agent,
    tools=tools,
    mcp_clients=mcp_clients,
    system_prompt=system_prompt,
    max_turns=10,
    max_budget_usd=1.00
)

# Jeder submitMessage() Startet eine neue Runde
async for event in engine.submit_message("Research AI trends"):
    if event.type == "tool_use":
        result = await execute_tool(event.tool_name, event.input)
        engine.submit_tool_result(event.tool_id, result)
    elif event.type == "assistant":
        print(event.content)
    elif event.type == "error":
        print(f"Error: {event.message}")
```

## Async Generator Pattern

```python
class QueryEngine:
    def __init__(self, config: QueryConfig):
        self.messages: list[Message] = config.initial_messages or []
        self.tools: Tools = config.tools
        self.abort_controller = AbortController()
        self.usage: Usage = Usage()
        self.cost_tracker = CostTracker()
        
    async def submit_message(self, content: str) -> AsyncGenerator[Event, None]:
        """Startet eine neue Gesprächsrunde."""
        # 1. User-Nachricht hinzufügen
        self.messages.append(UserMessage(content=content))
        
        # 2. System-Prompt zusammenbauen
        system_prompt = await self.build_system_prompt()
        
        # 3. ReAct Loop starten
        async for event in self.react_loop(system_prompt):
            yield event
            
            # 4. Token-Budget prüfen
            if self.cost_tracker.total > self.max_budget:
                yield ErrorEvent("Budget exceeded")
                break
                
            # 5. Max Turns prüfen
            if self.turn_count >= self.max_turns:
                yield ErrorEvent("Max turns reached")
                break
    
    async def react_loop(self, system_prompt: SystemPrompt) -> AsyncGenerator[Event, None]:
        """Der Haupt-ReAct-Loop: API Call → Tool Execution → Repeat."""
        while not self.should_stop():
            # API Call
            response = await self.call_api(system_prompt, self.messages)
            
            # Response verarbeiten
            for block in response.content:
                if block.type == "text":
                    yield AssistantEvent(content=block.text)
                    self.messages.append(AssistantMessage(block.text))
                    
                elif block.type == "tool_use":
                    yield ToolUseEvent(tool_name=block.name, input=block.input)
                    
                    # Tool ausführen
                    tool = self.tools.get(block.name)
                    result = await tool.execute(block.input)
                    
                    # Tool-Result speichern
                    self.messages.append(ToolResultMessage(block.id, result))
                    
            # Context Compaction wenn nötig
            if self.needs_compaction():
                await self.compact_context()
```

## Token Budget Tracking

```python
class TokenBudget:
    def __init__(self, max_tokens: int = 100000):
        self.max_tokens = max_tokens
        self.used_tokens = 0
        
    def check(self, estimated_tokens: int) -> bool:
        return self.used_tokens + estimated_tokens <= self.max_tokens
    
    def record(self, tokens: int):
        self.used_tokens += tokens
```

## Context Compaction

```python
async def compact_context(self):
    """Fasst alte Nachrichten zusammen wenn das Token-Limit erreicht wird."""
    if self.token_usage > self.compact_threshold:
        # Älteste Nachrichten zusammenfassen
        summary = await self.summarize(self.messages[:-5])
        
        # Zusammenfassung ersetzen
        self.messages = [
            SystemMessage(summary),
            *self.messages[-5:]  # Letzte 5 Nachrichten behalten
        ]
```

## Feature Flags (Dead Code Elimination)

```python
# Compile-time feature flags für verschiedene Build-Tiers
if feature("COORDINATOR_MODE"):
    from .coordinator import get_coordinator_context
else:
    def get_coordinator_context(): return {}

if feature("HISTORY_SNIP"):
    from .compact import snip_compact
else:
    snip_compact = None
```

## Best Practices

1. **Ein QueryEngine pro Conversation** — State persistiert über Runden
2. **Async Generator** — Stream Events in Echtzeit
3. **Token Budget** — Verhindert unerwartete Kosten
4. **Context Compaction** — Verhindert Token-Limit-Überschreitung
5. **Feature Flags** — Unterschiedliche Builds für verschiedene Tiers

## Next Steps

- [Agent Basics](/guide/agent-basics)
- [SIN Hooks](/guide/sin-hooks)
- [SIN Subagents](/guide/sin-subagents)
