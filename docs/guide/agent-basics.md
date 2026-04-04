# Agent Basics

## What is an Agent?

An agent is an autonomous AI entity that can:
- Receive and process messages
- Execute tasks using its capabilities
- Communicate with other agents via A2A protocol
- Use external tools via MCP servers

## Creating an Agent

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'my-agent',
  description: 'A helpful assistant',
  capabilities: ['greet', 'answer', 'research'],
  model: 'openrouter/qwen/qwen3.6-plus:free',
  systemPrompt: 'You are a helpful assistant.'
});
```

## Agent Configuration

| Property | Type | Description | Required |
|----------|------|-------------|----------|
| `name` | string | Unique agent identifier | Yes |
| `description` | string | Agent description | No |
| `capabilities` | string[] | What the agent can do | Yes |
| `model` | string | AI model to use | Yes |
| `systemPrompt` | string | Instructions for the agent | No |
| `mcpServers` | string[] | MCP servers to use | No |
| `rateLimit` | object | Rate limiting config | No |

## Handling Messages

```javascript
agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
  const response = await processMessage(msg.text);
  await agent.respond(response);
});
```

## Starting and Stopping

```javascript
// Start the agent
await agent.start();

// Stop the agent
await agent.stop();

// Check if agent is running
console.log(agent.isRunning); // true/false
```

## Next Steps
- [Team Orchestration](/guide/team-orchestration)
- [A2A Protocol](/guide/a2a-protocol)
