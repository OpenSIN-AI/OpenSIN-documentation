# Example: Telegram Bot

## Code

```javascript
import { TelegramAgent } from '@opensin/integrations/telegram';

const agent = new TelegramAgent({
  token: process.env.TELEGRAM_BOT_TOKEN,
  name: 'my-telegram-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Next Steps
- [Discord Bot](discord-bot.md)
- [WhatsApp](../integrations/whatsapp.md)
