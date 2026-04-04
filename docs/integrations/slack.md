# Integration: Slack

## Duration: 20 minutes
## Difficulty: Beginner

## Prerequisites
- Slack Bot Token
- OpenSIN installed

## Step 1: Create Slack Agent

```javascript
import { SlackAgent } from '@opensin/integrations/slack';

const agent = new SlackAgent({
  token: process.env.SLACK_BOT_TOKEN,
  name: 'my-slack-bot',
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
SLACK_BOT_TOKEN=your_token node index.js
```

## Step 3: Test Bot

Send a message to your bot on Slack.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Integration: Signal](signal.md)
- [Integration: Matrix](matrix.md)
