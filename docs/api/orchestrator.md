# Orchestrator API

## Overview

Orchestrator API reference for coordinating agent teams.

## Creating an Orchestrator

```javascript
import { Orchestrator } from '@opensin/core';

const orchestrator = new Orchestrator({
  strategy: 'sequential',
  maxRetries: 3,
  timeout: 300000
});
```

## Orchestration Strategies

| Strategy | Description |
|----------|-------------|
| `sequential` | Agents work one after another |
| `parallel` | Agents work simultaneously |
| `hierarchical` | Manager agent delegates tasks |
| `dynamic` | Dynamic task assignment based on capabilities |

## Methods

### `assign(task: Task)`

Assign a task to the team.

### `cancel(taskId: string)`

Cancel a task.

### `status(taskId: string)`

Get task status.

## Next Steps
- [Team API](/api/team)
- [Events API](/api/events)
