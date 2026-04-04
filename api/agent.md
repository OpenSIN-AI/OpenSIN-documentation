# Agent API

## Overview

The Agent API provides the core interface for creating and managing AI agents.

## Creating an Agent

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'my-agent',
  description: 'A helpful assistant',
  capabilities: ['greet', 'answer', 'research'],
  model: 'openrouter/qwen/qwen3.6-plus:free',
  systemPrompt: 'You are a helpful assistant.',
  mcpServers: ['web-search', 'file-system'],
  rateLimit: {
    messagesPerMinute: 60,
    tokensPerMinute: 10000
  },
  logging: {
    level: 'info',
    destination: 'file',
    path: './logs/agent.log'
  }
});
```

## AgentOptions

| Property | Type | Description | Required |
|----------|------|-------------|----------|
| `name` | string | Unique agent identifier | Yes |
| `description` | string | Agent description | No |
| `capabilities` | string[] | What the agent can do | Yes |
| `model` | string | AI model to use | Yes |
| `systemPrompt` | string | Instructions for the agent | No |
| `mcpServers` | string[] | MCP servers to use | No |
| `rateLimit` | object | Rate limiting config | No |
| `logging` | object | Logging config | No |

## Methods

### `start()`

Start the agent.

```javascript
await agent.start();
```

### `stop()`

Stop the agent.

```javascript
await agent.stop();
```

### `send(message: string | Message)`

Send a message to the agent.

```javascript
const response = await agent.send('Hello!');
```

### `respond(message: string | Message)`

Respond to a message.

```javascript
await agent.respond('Hello back!');
```

### `on(event: string, handler: Function)`

Register an event handler.

```javascript
agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
  await agent.respond('Response');
});
```

## Events

| Event | Description |
|-------|-------------|
| `message` | Emitted when a message is received |
| `error` | Emitted when an error occurs |
| `start` | Emitted when the agent starts |
| `stop` | Emitted when the agent stops |
| `capability-ready` | Emitted when a capability is ready |

## Error Handling

```javascript
agent.on('error', async (error) => {
  console.error('Agent error:', error);
  await agent.respond({
    type: 'error',
    content: 'I encountered an error. Please try again.'
  });
});
```

## Next Steps
- [Team API](/api/team)
- [A2A API](/api/a2a)
- [Message API](/api/message)
