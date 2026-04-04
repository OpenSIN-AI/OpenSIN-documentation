# Tutorial: Building a Telegram Bot

## Duration: 30 minutes
## Difficulty: Intermediate

## What You'll Learn
- How to create a Telegram bot
- How to integrate with OpenSIN
- How to handle Telegram messages
- How to deploy the bot

## Prerequisites
- Telegram account
- Node.js 18+
- OpenSIN installed

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
  console.log('Received:', msg.text);
  const response = await processMessage(msg.text);
  await agent.respond(response);
});

await agent.start();
```

## Step 4: Run Bot

```bash
TELEGRAM_BOT_TOKEN=your_token node bot.js
```

## Step 5: Test Bot

Send a message to your bot on Telegram.

## Expected Output

```
Received: Hello!
Responded: Hello! How can I help you?
```

## Next Steps
- [Tutorial: Discord Bot](discord-bot.md)
- [Integration: WhatsApp](../integrations/whatsapp.md)
