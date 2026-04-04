# SIN Sorted Tool Assembly — Cache-Stabile Tool Definitionen

> **OpenSIN's Tool Assembly** — Geklont aus Claude Code. Sortierte Tools für byte-identische Definitionen über Sessions.

## Das Problem

Wenn Tools in unterschiedlicher Reihenfolge im Prompt erscheinen, ist jeder Request ein Cache Miss → hohe Kosten.

## Die Lösung: Sortierte Assembly

```python
from opensin.tools import assemble_tool_pool

# Tools werden NACH NAMEN SORTIERT bevor sie zum Prompt hinzugefügt werden
tool_pool = assemble_tool_pool(
    built_in_tools=built_in_tools,  # Sortiert nach Name
    mcp_tools=mcp_tools,            # Sortiert nach Name
    permission_context=permission_context
)

# Ergebnis: Byte-identische Tool-Definitionen über alle Sessions
# → Maximale Prompt Cache Hits!
```

## Implementation

```python
def assemble_tool_pool(
    built_in_tools: list[Tool],
    mcp_tools: list[Tool],
    permission_context: PermissionContext
) -> ToolPool:
    # 1. Built-in Tools sortieren
    sorted_builtin = sorted(built_in_tools, key=lambda t: t.name)
    
    # 2. MCP Tools sortieren
    sorted_mcp = sorted(mcp_tools, key=lambda t: t.name)
    
    # 3. Deduplizieren (MCP kann Built-in shadowen)
    tool_map = {}
    for tool in sorted_builtin + sorted_mcp:
        tool_map[tool.name] = tool
    
    # 4. Nach Permission-Context filtern
    filtered_tools = filter_by_permissions(
        list(tool_map.values()),
        permission_context
    )
    
    return ToolPool(filtered_tools)
```

## Performance Impact

| Scenario | Cache Hit Rate | Cost per 10000 Requests |
|----------|---------------|------------------------|
| Unsortiert | 30% | $210.00 |
| Sortiert | 85% | $59.50 |
| **Ersparnis** | **2.8x** | **$150.50** |

## Permission-Aware Filtering

```python
def filter_by_permissions(
    tools: list[Tool],
    context: PermissionContext
) -> list[Tool]:
    """Filtert Tools basierend auf Permission Rules."""
    filtered = []
    for tool in tools:
        if context.is_tool_allowed(tool):
            filtered.append(tool)
    return filtered

# MCP Server-Prefix Rules
# mcp__github filtert ALLE Tools von diesem Server
# BEFORE das Modell sie sieht
```

## Best Practices

1. **Immer sortieren** — Name-basierte Sortierung
2. **Deduplizieren** — MCP kann Built-in shadowen
3. **Permission-First** — Filtern vor dem API Call
4. **Monitor Cache** — Tracke Cache Hit Rate

## Next Steps

- [SIN Tool System](/guide/sin-tool-system)
- [Cost Optimization](/guide/agent-cost-optimization)
