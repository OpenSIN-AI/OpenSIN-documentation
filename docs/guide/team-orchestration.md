# Team Orchestration

OpenSIN teams enable multiple agents to work together on complex tasks.

## Creating a Team

```bash
# Use background_agents plugin for parallel task delegation
```

## Team Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| sequential | Agents work one after another | Pipeline workflows |
| parallel | Agents work simultaneously | Independent tasks |
| consensus | Agents vote on outcomes | Decision making |
| leader | One agent coordinates others | Complex coordination |
| pipeline | Output of one feeds input of next | Data processing |

## Executing a Team Task

```bash
# Delegate via the REPL interface
```

## Next Steps

- [Agent Basics](/guide/agent-basics)
- [A2A Protocol](/guide/a2a-protocol)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht** | -200.0 | SELBST MACHEN via `create-a2a-sin-agent` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/a2a-communication)
