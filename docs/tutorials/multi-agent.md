# Tutorial: Multi-Agent Collaboration

## Duration: 45 minutes
## Difficulty: Intermediate

## What You'll Learn
- How to create agent teams
- How to configure orchestration
- How to handle task delegation
- How to monitor team performance

## Step 1: Create Agent Team

```javascript
import { Team, Agent, Orchestrator } from '@opensin/core';

const researcher = new Agent({ name: 'researcher', capabilities: ['research', 'analyze'] });
const writer = new Agent({ name: 'writer', capabilities: ['write', 'edit'] });
const editor = new Agent({ name: 'editor', capabilities: ['review', 'approve'] });

const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: new Orchestrator({ strategy: 'sequential', timeout: 300000 })
});

await team.start();
```

## Step 2: Assign Task

```javascript
await team.assign({
  task: 'Write a blog post about AI agents',
  workflow: [
    { agent: 'researcher', task: 'Research AI agents' },
    { agent: 'writer', task: 'Write blog post' },
    { agent: 'editor', task: 'Review and approve' }
  ]
});
```

## Step 3: Monitor Progress

```javascript
team.on('task-complete', (result) => {
  console.log(`Task completed: ${result.agent}`);
});

team.on('team-complete', (result) => {
  console.log('Team completed all tasks!');
});
```

## Next Steps
- [Custom Agents](custom-agents.md)
- [Advanced Orchestration](advanced-orchestration.md)
