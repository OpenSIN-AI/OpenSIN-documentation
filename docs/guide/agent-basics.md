# Agent Basics

OpenSIN agents are autonomous AI entities that can process inputs, make decisions, and produce outputs using LLMs and tools.

## Creating an Agent

```bash
npm start  # then type your query in the REPL
```

## Agent Configuration

- **name** — Unique identifier for the agent
- **model** — LLM model to use (gpt-4, gpt-3.5-turbo, claude-sonnet, etc.)
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
