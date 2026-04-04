# SIN System Prompt Builder — Dynamic Prompt Construction

> **OpenSIN's System Prompt Builder** — Geklont aus Claude Code's systemPromptType.ts, queryContext.ts. Dynamische Prompt-Erstellung.

## Implementation

```python
from opensin.prompt import SystemPromptBuilder

builder = SystemPromptBuilder(
    base_prompt=base_prompt,
    user_context=user_context,
    system_context=system_context,
    tools=tools,
    agents=agents,
    mcp_servers=mcp_servers,
    latches=active_latches
)

# Build system prompt
system_prompt = await builder.build()
```

## Prompt Parts

| Part | Description |
|------|-------------|
| Base Prompt | Core agent instructions |
| User Context | User-specific info |
| System Context | System configuration |
| Tool Definitions | Available tools |
| Agent Definitions | Available agents |
| MCP Servers | Connected MCP servers |
| Latches | Active feature latches |

## Fetch System Prompt Parts

```python
from opensin.prompt import fetch_system_prompt_parts

parts = await fetch_system_prompt_parts(
    include_tools=True,
    include_agents=True,
    include_mcp=True,
    include_latches=True
)
```

## Best Practices

1. **Modular** — Prompt in Teile aufbauen
2. **Cache** — Prompt-Teile cachen
3. **Dynamic** — Basierend auf Kontext anpassen
4. **Validate** — Prompt auf Gültigkeit prüfen
5. **Monitor** — Prompt-Größe tracken

## Next Steps

- [SIN ReAct Loop](/guide/sin-react-loop)
- [SIN Query Engine](/guide/sin-query-engine)
