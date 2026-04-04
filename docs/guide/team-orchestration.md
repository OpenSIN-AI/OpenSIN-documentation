# Team Orchestration

## What is a Team?

A team is a collection of agents that work together to accomplish complex tasks.

## Creating a Team

```javascript
import { Team, Agent } from '@opensin/core';

const researcher = new Agent({ name: 'researcher', capabilities: ['research', 'analyze'] });
const writer = new Agent({ name: 'writer', capabilities: ['write', 'edit'] });
const editor = new Agent({ name: 'editor', capabilities: ['review', 'approve'] });

const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: 'sequential'
});
```

## Orchestration Strategies

### Sequential
Agents work one after another.

```javascript
const team = new Team({ orchestrator: 'sequential' });
```

### Parallel
Agents work simultaneously.

```javascript
const team = new Team({ orchestrator: 'parallel' });
```

### Hierarchical
A manager agent delegates tasks.

```javascript
const team = new Team({ orchestrator: 'hierarchical', manager: 'manager-agent' });
```

## Assigning Tasks

```javascript
await team.assign({
  task: 'Write a blog post',
  workflow: [
    { agent: 'researcher', task: 'Research topic' },
    { agent: 'writer', task: 'Write draft' },
    { agent: 'editor', task: 'Review and edit' }
  ]
});
```

## Monitoring Teams

```javascript
team.on('task-start', (task) => {
  console.log(`Task started: ${task.agent}`);
});

team.on('task-complete', (result) => {
  console.log(`Task completed: ${result.agent}`);
});

team.on('team-complete', (result) => {
  console.log('Team completed all tasks!');
});
```

## Next Steps
- [A2A Protocol](/guide/a2a-protocol)
- [MCP Integration](/guide/mcp-integration)
