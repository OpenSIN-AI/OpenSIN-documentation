# Tutorial: Building a Telegram Bot

## Duration: 30 minutes
## Difficulty: Intermediate

## Step 1: Create Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the bot token

## Step 2: Install Dependencies

```bash
npm install @opensin/core @opensin/integrations/telegram
```

## Step 3: Create Bot Code

```javascript
import { TelegramAgent } from '@opensin/integrations/telegram';

const agent = new TelegramAgent({
  token: process.env.TELEGRAM_BOT_TOKEN,
  name: 'my-telegram-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(await processMessage(msg.text));
});

await agent.start();
```

## Step 4: Run Bot

```bash
TELEGRAM_BOT_TOKEN=your_token node bot.js
```

## Next Steps
- [Discord Bot](discord-bot.md)
- [WhatsApp Integration](../integrations/whatsapp.md)
