# Agent Basics

OpenSIN agents are autonomous AI entities that can process inputs, make decisions, and produce outputs using LLMs and tools.

## Creating an Agent

```bash
bun start  # then type your query in the REPL
```

## Agent Configuration

- **name** — Unique identifier for the agent
- **model** — LLM model to use (`openai/gpt-5.4`, `openai/gpt-5.4-mini`, `google/antigravity-claude-sonnet-4-6`, etc.)
- **system_prompt** — Instructions that define the agent's behavior
- **temperature** — Controls randomness (0.0-2.0)
- **max_tokens** — Maximum tokens per response
- **tools** — List of tools the agent can use

## Testing an Agent

```bash
# The agent loop runs automatically
```

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [A2A Protocol](/guide/a2a-protocol)
- [MCP Integration](/guide/mcp-integration)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht** | -200.0 | SELBST MACHEN via `create-a2a-sin-agent` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/a2a-communication)
