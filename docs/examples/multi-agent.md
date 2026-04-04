# Example: Multi-Agent Team

## Overview

Complete multi-agent team example with task orchestration.

## Code

```javascript
import { Team, Agent, Orchestrator } from '@opensin/core';

// Create agents
const researcher = new Agent({
  name: 'researcher',
  capabilities: ['research', 'analyze'],
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

const writer = new Agent({
  name: 'writer',
  capabilities: ['write', 'edit'],
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

const editor = new Agent({
  name: 'editor',
  capabilities: ['review', 'approve'],
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

// Create team
const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: new Orchestrator({
    strategy: 'sequential',
    timeout: 300000
  })
});

// Assign task
await team.assign({
  task: 'Write a comprehensive blog post about AI agents in 2026',
  workflow: [
    { agent: 'researcher', task: 'Research AI agents' },
    { agent: 'writer', task: 'Write blog post' },
    { agent: 'editor', task: 'Review and approve' }
  ]
});

// Monitor progress
team.on('task-complete', (result) => {
  console.log(`Task completed: ${result.agent}`);
});

team.on('team-complete', (result) => {
  console.log('Team completed all tasks!');
  console.log(result);
});

await team.start();
```

## Expected Output

```
Task completed: researcher
Task completed: writer
Task completed: editor
Team completed all tasks!
{ title: "AI Agents in 2026", content: "...", status: "approved" }
```

## Testing

```javascript
describe('Multi-Agent Team', () => {
  it('should complete tasks', async () => {
    const result = await team.assign({
      task: 'Test task',
      workflow: [
        { agent: 'researcher', task: 'Research' },
        { agent: 'writer', task: 'Write' }
      ]
    });
    expect(result.status).toBe('completed');
  });
});
```

## Next Steps
- [Custom Agents Example](custom-agents.md)
- [Telegram Bot Example](telegram-bot.md)
