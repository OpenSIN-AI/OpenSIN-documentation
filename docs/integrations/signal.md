# Integration: Signal

## Duration: 25 minutes
## Difficulty: Intermediate

## Prerequisites
- Signal CLI installed
- OpenSIN installed

## Step 1: Create Signal Agent

```javascript
import { SignalAgent } from '@opensin/integrations/signal';

const agent = new SignalAgent({
  signalCliPath: '/usr/bin/signal-cli',
  phoneNumber: '+1234567890',
  name: 'my-signal-bot',
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
node signal-bot.js
```

## Step 3: Test Bot

Send a message to your Signal number.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Matrix Integration](matrix.md)
- [IRC Integration](irc.md)
