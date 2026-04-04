# SIN Dump Prompts — Debug & Development

> **OpenSIN's Dump Prompts** — Geklont aus Claude Code's dumpPrompts.ts. System-Prompts debuggen und exportieren.

## Dump Implementation

```python
from opensin.debug import PromptDumper

dumper = PromptDumper(
    output_dir=".sin/debug/prompts",
    include_system_prompt=True,
    include_user_context=True,
    include_tool_definitions=True
)

# Dump aktuellen Prompt
await dumper.dump(
    session_id=session_id,
    messages=messages,
    system_prompt=system_prompt
)
```

## Output Format

```json
{
  "session_id": "abc123",
  "timestamp": "2026-04-04T10:00:00Z",
  "system_prompt": "...",
  "user_context": {"key": "value"},
  "tool_definitions": [...],
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "token_count": 4500
}
```

## Use Cases

1. **Debug** — System-Prompts inspizieren
2. **Development** — Prompt-Änderungen testen
3. **Audit** — Prompt-Historie nachvollziehen
4. **Optimization** — Token-Usage analysieren

## Best Practices

1. **Secure storage** — Prompts nicht öffentlich speichern
2. **Redact secrets** — API Keys und Secrets entfernen
3. **Limited retention** — Alte Dumps automatisch löschen
4. **Include metadata** — Session-ID, Timestamp, Token-Count

## Next Steps

- [SIN Debugging](/guide/agent-debugging)
- [SIN ReAct Loop](/guide/sin-react-loop)
