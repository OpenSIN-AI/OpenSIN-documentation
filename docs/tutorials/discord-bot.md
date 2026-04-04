# Tutorial: Building a Discord Bot

## Duration: 30 minutes
## Difficulty: Intermediate

## What You'll Learn
- How to create a Discord bot
- How to integrate with OpenSIN
- How to handle Discord messages
- How to deploy the bot

## Prerequisites
- Discord account
- Node.js 18+
- OpenSIN installed

## Step 1: Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and create a bot
4. Copy the bot token
5. Invite bot to your server using OAuth2 URL generator

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
  console.log('Received:', msg.content);
  const response = await processMessage(msg.content);
  await agent.respond(response);
});

await agent.start();
```

## Step 4: Run Bot

```bash
DISCORD_BOT_TOKEN=your_token node bot.js
```

## Step 5: Test Bot

Send a message to your bot on Discord.

## Expected Output

```
Received: Hello!
Responded: Hello! How can I help you?
```

## Next Steps
- [Tutorial: Telegram Bot](telegram-bot.md)
- [Integration: Slack](../integrations/slack.md)
