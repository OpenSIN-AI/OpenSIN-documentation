# SIN Query Configuration — Query Setup

> **OpenSIN's Query Config** — Geklont aus Claude Code's query/config.ts. Query-Konfiguration.

## Implementation

```python
from opensin.query import QueryConfig

config = QueryConfig(
    model="gpt-4",
    max_tokens=4000,
    temperature=0.7,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop_sequences=None,
    tools=tools,
    system_prompt=system_prompt
)

# Build query
query = QueryEngine(config)
```

## Query Dependencies

```python
from opensin.query import QueryDeps

deps = QueryDeps(
    can_use_tool=can_use_tool_fn,
    tool_use_context=tool_context,
    get_app_state=get_app_state,
    set_app_state=set_app_state
)
```

## Best Practices

1. **Validate config** — Config vor Query-Start validieren
2. **Set limits** — Max Tokens, Timeout setzen
3. **Include dependencies** — Alle Dependencies mitgeben
4. **Monitor usage** — Query-Usage tracken
5. **Handle errors** — Query-Fehler behandeln

## Next Steps

- [SIN Query Engine](/guide/sin-query-engine)
- [SIN ReAct Loop](/guide/sin-react-loop)
