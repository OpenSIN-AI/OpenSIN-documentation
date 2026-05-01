# A2A Protocol

The Agent-to-Agent (A2A) protocol enables direct communication between OpenSIN agents.

## Overview

A2A allows agents to:

- Send messages to each other
- Request information or actions
- Share context and state
- Coordinate complex workflows

## Message Types

| Type         | Description                   |
| ------------ | ----------------------------- |
| request      | Request information or action |
| response     | Response to a request         |
| notification | One-way notification          |
| error        | Error message                 |

## Using A2A

```bash
opensin a2a send --from agent1 --to agent2 --message "Research AI trends"
```

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [MCP Integration](/guide/mcp-integration)
