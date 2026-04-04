# Example: Multi-Agent Team

## Overview

Multi-agent collaboration example.

## Code

```javascript
import { Team, Agent } from '@opensin/core';

const researcher = new Agent({
  name: 'researcher',
  capabilities: ['research', 'analyze']
});

const writer = new Agent({
  name: 'writer',
  capabilities: ['write', 'edit']
});

const team = new Team({
  name: 'content-team',
  agents: [researcher, writer],
  orchestrator: 'sequential'
});

await team.assign({
  task: 'Write a blog post about AI',
  workflow: [
    { agent: 'researcher', task: 'Research AI' },
    { agent: 'writer', task: 'Write blog post' }
  ]
});
```

## Running the Example

```bash
node multi-agent.js
```

## Expected Output

```
Researcher: Found 10 relevant articles
Writer: Blog post complete!
Task completed: { title: "AI in 2026", content: "..." }
```

## Next Steps
- [Telegram Bot Example](telegram-bot.md)
- [Discord Bot Example](discord-bot.md)
