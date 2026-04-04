# Example: Discord Bot

## Code

```javascript
import { DiscordAgent } from '@opensin/integrations/discord';

const agent = new DiscordAgent({
  token: process.env.DISCORD_BOT_TOKEN,
  name: 'my-discord-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(`You said: ${msg.content}`);
});

await agent.start();
```

## Next Steps
- [Telegram Bot](telegram-bot.md)
- [Slack](../integrations/slack.md)
