# Events API

## Overview

Events API reference for OpenSIN agents and teams.

## Agent Events

### `message`

Emitted when a message is received.

```javascript
agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
  await agent.respond('Response');
});
```

### `error`

Emitted when an error occurs.

```javascript
agent.on('error', async (error) => {
  console.error('Agent error:', error);
});
```

### `start` / `stop`

Emitted when the agent starts or stops.

## Team Events

### `task-start` / `task-complete` / `task-error`

Emitted when tasks start, complete, or fail.

### `team-complete`

Emitted when all tasks are complete.

## Next Steps
- [Message API](/api/message)
- [Orchestrator API](/api/orchestrator)
