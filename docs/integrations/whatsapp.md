# Integration: WhatsApp

## Duration: 25 minutes
## Difficulty: Intermediate

## Prerequisites
- WhatsApp Business API credentials
- OpenSIN installed

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
  console.log('Received:', msg.text);
  await agent.respond(`You said: ${msg.text}`);
});

await agent.start();
```

## Step 2: Run Agent

```bash
WHATSAPP_PHONE_NUMBER_ID=your_id \
WHATSAPP_ACCESS_TOKEN=your_token \
node index.js
```

## Step 3: Test Bot

Send a message to your WhatsApp number.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Slack Integration](slack.md)
- [Signal Integration](signal.md)
