# Tutorial: Multi-Agent Collaboration

## Duration: 45 minutes
## Difficulty: Intermediate

## What You'll Learn
- How to create agent teams
- How to configure orchestration
- How to handle task delegation
- How to monitor team performance

## Prerequisites
- Complete [Agent Basics](agent-basics.md)
- OpenSIN installed

## Step 1: Create Agent Team

```javascript
import { Team, Agent, Orchestrator } from '@opensin/core';

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

const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: new Orchestrator({
    strategy: 'sequential',
    timeout: 300000 // 5 minutes
  })
});

await team.start();
```

## Step 2: Assign Task

```javascript
await team.assign({
  task: 'Write a comprehensive blog post about AI agents in 2026',
  workflow: [
    { agent: 'researcher', task: 'Research AI agents' },
    { agent: 'writer', task: 'Write blog post' },
    { agent: 'editor', task: 'Review and approve' }
  ]
});
```

## Step 3: Monitor Progress

```javascript
team.on('task-start', (task) => {
  console.log(`Task started: ${task.agent} - ${task.task}`);
});

team.on('task-complete', (result) => {
  console.log(`Task completed: ${result.agent}`);
  console.log(`Result: ${result.output}`);
});

team.on('team-complete', (result) => {
  console.log('Team completed all tasks!');
  console.log(result);
});
```

## Expected Output

```
Task started: researcher - Research AI agents
Researcher: Found 15 relevant articles
Task completed: researcher
Task started: writer - Write blog post
Writer: Blog post complete!
Task completed: writer
Task started: editor - Review and approve
Editor: Approved with minor edits
Task completed: editor
Team completed all tasks!
{ title: "AI Agents in 2026", content: "...", status: "approved" }
```

## Next Steps
- [Integration: Telegram Bot](../integrations/telegram.md)
- [Best Practices](../best-practices/agent-design.md)
