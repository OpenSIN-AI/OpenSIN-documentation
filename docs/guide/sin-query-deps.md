# SIN Query Dependencies — Dependency Injection

> **OpenSIN's Query Dependencies** — Geklont aus Claude Code's query/deps.ts. Dependency Injection für Queries.

## Implementation

```python
from opensin.query import QueryDeps, ProductionDeps

# Production dependencies
deps = ProductionDeps(
    can_use_tool=can_use_tool_fn,
    tool_use_context=tool_context,
    get_app_state=get_app_state,
    set_app_state=set_app_state,
    mcp_clients=mcp_clients,
    agents=agents
)

# Use in query engine
engine = QueryEngine(config, deps)
```

## Dependency Types

| Dependency | Description |
|------------|-------------|
| `can_use_tool` | Tool permission check |
| `tool_use_context` | Tool execution context |
| `get_app_state` | App state getter |
| `set_app_state` | App state setter |
| `mcp_clients` | MCP client connections |
| `agents` | Available agents |

## Best Practices

1. **Inject dependencies** — Nicht global state nutzen
2. **Type-safe** — Dependencies typisieren
3. **Mock for testing** — Dependencies mocken
4. **Production defaults** — sinnvolle Defaults setzen
5. **Document interface** — Dependencies dokumentieren

## Next Steps

- [SIN Query Config](/guide/sin-query-config)
- [SIN Query Engine](/guide/sin-query-engine)
