# Example: Hello World

## Overview

Simple "Hello World" example using OpenSIN.

## Code

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'hello-world',
  capabilities: ['greet'],
  model: 'openrouter/qwen/qwen3.6-plus:free',
  systemPrompt: 'You are a friendly assistant.'
});

agent.on('message', async (msg) => {
  if (msg.text.toLowerCase().includes('hello')) {
    await agent.respond('Hello! How can I help you today?');
  } else {
    await agent.respond('You said: ' + msg.text);
  }
});

await agent.start();
```

## Running the Example

```bash
npm install @opensin/core
node hello-world.js
```

## Testing

```bash
curl -X POST http://localhost:3000/api/message \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello!"}'
```

## Expected Output

```json
{
  "response": "Hello! How can I help you today?",
  "agent": "hello-world",
  "timestamp": "2026-04-04T04:00:00Z"
}
```

## Next Steps
- [Multi-Agent Example](multi-agent.md)
- [Telegram Bot Example](telegram-bot.md)
