# Example: Multi-Agent Team

## Code

```javascript
import { Team, Agent } from '@opensin/core';

const researcher = new Agent({ name: 'researcher', capabilities: ['research', 'analyze'] });
const writer = new Agent({ name: 'writer', capabilities: ['write', 'edit'] });

const team = new Team({ name: 'content-team', agents: [researcher, writer], orchestrator: 'sequential' });

await team.assign({
  task: 'Write a blog post',
  workflow: [
    { agent: 'researcher', task: 'Research' },
    { agent: 'writer', task: 'Write' }
  ]
});
```

## Next Steps
- [Hello World](hello-world.md)
- [Custom Agents](custom-agents.md)
