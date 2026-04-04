# Tutorial: Building a Discord Bot

## Duration: 30 minutes
## Difficulty: Intermediate

## Step 1: Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Create a bot and copy the token
4. Invite bot to your server

## Step 2: Install Dependencies

```bash
npm install @opensin/core @opensin/integrations/discord
```

## Step 3: Create Bot Code

```javascript
import { DiscordAgent } from '@opensin/integrations/discord';

const agent = new DiscordAgent({
  token: process.env.DISCORD_BOT_TOKEN,
  name: 'my-discord-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(await processMessage(msg.content));
});

await agent.start();
```

## Next Steps
- [Telegram Bot](telegram-bot.md)
- [Slack Integration](../integrations/slack.md)
