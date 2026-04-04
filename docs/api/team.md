# Team API

## Overview

The Team API provides the interface for creating and managing agent teams.

## Creating a Team

```javascript
import { Team, Agent, Orchestrator } from '@opensin/core';

const researcher = new Agent({ name: 'researcher', capabilities: ['research', 'analyze'] });
const writer = new Agent({ name: 'writer', capabilities: ['write', 'edit'] });
const editor = new Agent({ name: 'editor', capabilities: ['review', 'approve'] });

const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: new Orchestrator({
    strategy: 'sequential',
    maxRetries: 3,
    timeout: 300000
  })
});
```

## TeamOptions

| Property | Type | Description | Required |
|----------|------|-------------|----------|
| `name` | string | Team name | Yes |
| `agents` | Agent[] | Team agents | Yes |
| `orchestrator` | Orchestrator | Orchestration strategy | Yes |

## Methods

### `start()`

Start the team.

```javascript
await team.start();
```

### `stop()`

Stop the team.

```javascript
await team.stop();
```

### `assign(task: Task)`

Assign a task to the team.

```javascript
await team.assign({
  task: 'Write a blog post',
  workflow: [
    { agent: 'researcher', task: 'Research' },
    { agent: 'writer', task: 'Write' },
    { agent: 'editor', task: 'Review' }
  ]
});
```

### `cancel(taskId: string)`

Cancel a task.

```javascript
await team.cancel('task-id');
```

### `status(taskId: string)`

Get task status.

```javascript
const status = await team.status('task-id');
```

## Events

| Event | Description |
|-------|-------------|
| `task-start` | Emitted when a task starts |
| `task-complete` | Emitted when a task completes |
| `task-error` | Emitted when a task fails |
| `team-complete` | Emitted when all tasks are complete |

## Orchestration Strategies

### Sequential

Agents work one after another.

```javascript
const orchestrator = new Orchestrator({ strategy: 'sequential' });
```

### Parallel

Agents work simultaneously.

```javascript
const orchestrator = new Orchestrator({ strategy: 'parallel' });
```

### Hierarchical

A manager agent delegates tasks.

```javascript
const orchestrator = new Orchestrator({
  strategy: 'hierarchical',
  manager: 'manager-agent'
});
```

### Dynamic

Dynamic task assignment based on capabilities.

```javascript
const orchestrator = new Orchestrator({ strategy: 'dynamic' });
```

## Next Steps
- [Agent API](/api/agent)
- [Orchestrator API](/api/orchestrator)
- [Events API](/api/events)
