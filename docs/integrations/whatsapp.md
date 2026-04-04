# Integration: WhatsApp

## Step 1: Create WhatsApp Agent

```javascript
import { WhatsAppAgent } from '@opensin/integrations/whatsapp';

const agent = new WhatsAppAgent({
  phoneNumberId: process.env.WHATSAPP_PHONE_NUMBER_ID,
  accessToken: process.env.WHATSAPP_ACCESS_TOKEN,
  name: 'my-whatsapp-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Step 2: Run

```bash
WHATSAPP_PHONE_NUMBER_ID=your_id WHATSAPP_ACCESS_TOKEN=your_token node bot.js
```

## Next Steps
- [Slack](slack.md)
- [Signal](signal.md)
