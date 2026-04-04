# Integration: Matrix

## Duration: 20 minutes
## Difficulty: Beginner

## Prerequisites
- Matrix homeserver URL
- Matrix access token
- OpenSIN installed

## Step 1: Create Matrix Agent

```javascript
import { MatrixAgent } from '@opensin/integrations/matrix';

const agent = new MatrixAgent({
  homeserverUrl: 'https://matrix.org',
  accessToken: process.env.MATRIX_ACCESS_TOKEN,
  userId: '@bot:matrix.org',
  name: 'my-matrix-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Step 2: Run Agent

```bash
MATRIX_ACCESS_TOKEN=your_token node matrix-bot.js
```

## Step 3: Test Bot

Send a message to your bot on Matrix.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [IRC Integration](irc.md)
- [Best Practices](../best-practices/agent-design.md)
