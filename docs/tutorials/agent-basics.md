# Tutorial: Agent Basics

## Duration: 30 minutes
## Difficulty: Beginner

## What You'll Learn
- How to create an agent
- How to configure agent capabilities
- How to handle messages
- How to deploy an agent

## Prerequisites
- Node.js 18+
- npm or yarn
- Basic JavaScript knowledge

## Step 1: Setup Project

```bash
mkdir my-agent
cd my-agent
npm init -y
npm install @opensin/core
```

## Step 2: Create Agent

```javascript
// index.js
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'my-first-agent',
  description: 'My first OpenSIN agent',
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

## Step 3: Run Agent

```bash
node index.js
```

## Step 4: Test Agent

```bash
curl -X POST http://localhost:3000/api/message \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello!"}'
```

## Expected Output

```json
{
  "response": "You said: Hello!",
  "agent": "my-first-agent",
  "timestamp": "2026-04-04T04:00:00Z"
}
```

## Next Steps
- [Tutorial: Multi-Agent Collaboration](multi-agent.md)
- [Integration: Telegram Bot](../integrations/telegram.md)
