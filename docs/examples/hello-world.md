# Example: Hello World

## Code

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({ name: 'hello-world', capabilities: ['greet'], model: 'openrouter/qwen/qwen3.6-plus:free' });

agent.on('message', async (msg) => {
  if (msg.text.toLowerCase().includes('hello')) {
    await agent.respond('Hello! How can I help you?');
  } else {
    await agent.respond('You said: ' + msg.text);
  }
});

await agent.start();
```

## Testing

```bash
curl -X POST http://localhost:3000/api/message -H "Content-Type: application/json" -d '{"text": "Hello!"}'
```

## Next Steps
- [Multi-Agent Team](multi-agent.md)
- [Telegram Bot](telegram-bot.md)
