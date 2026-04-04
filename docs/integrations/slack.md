# Integration: Slack

## Step 1: Create Slack Agent

```javascript
import { SlackAgent } from '@opensin/integrations/slack';

const agent = new SlackAgent({
  token: process.env.SLACK_BOT_TOKEN,
  name: 'my-slack-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Next Steps
- [Signal](signal.md)
- [Matrix](matrix.md)
