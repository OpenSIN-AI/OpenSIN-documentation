# Example: Telegram Bot

## Overview

Complete Telegram bot integration example.

## Code

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

## Running the Example

```bash
TELEGRAM_BOT_TOKEN=your_token node telegram-bot.js
```

## Testing

Send a message to your bot on Telegram.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Discord Bot Example](discord-bot.md)
- [WhatsApp Integration](../integrations/whatsapp.md)
