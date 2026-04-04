# Integration: Telegram

## Duration: 20 minutes
## Difficulty: Beginner

## Prerequisites
- Telegram Bot Token (from @BotFather)
- OpenSIN installed

## Step 1: Create Telegram Agent

```javascript
import { TelegramAgent } from '@opensin/integrations/telegram';

const agent = new TelegramAgent({
  token: process.env.TELEGRAM_BOT_TOKEN,
  name: 'my-telegram-bot',
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
TELEGRAM_BOT_TOKEN=your_token node index.js
```

## Step 3: Test Bot

Send a message to your bot on Telegram.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Discord Integration](discord.md)
- [WhatsApp Integration](whatsapp.md)
