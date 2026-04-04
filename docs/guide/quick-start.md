# Quick Start

Get started with OpenSIN in 5 minutes.

## Step 1: Install OpenSIN

```bash
npm install @opensin/core
```

## Step 2: Create Your First Agent

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'my-first-agent',
  capabilities: ['greet', 'answer'],
  model: 'openrouter/qwen/qwen3.6-plus:free',
  systemPrompt: 'You are a helpful assistant.'
});

agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Step 3: Send a Message

```javascript
const response = await agent.send('Hello!');
console.log(response);
// Output: { text: "You said: Hello!", agent: "my-first-agent" }
```

## Step 4: Create a Team

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
  task: 'Write a blog post about AI agents',
  workflow: [
    { agent: 'researcher', task: 'Research AI agents' },
    { agent: 'writer', task: 'Write blog post' }
  ]
});
```

## Next Steps

- [Core Concepts](/guide/core-concepts) — Learn the fundamentals
- [Agent Basics](/guide/agent-basics) — Deep dive into agents
- [Examples](/examples/hello-world) — Ready-to-use examples
