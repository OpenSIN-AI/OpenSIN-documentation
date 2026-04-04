# Integration: Discord

## Duration: 20 minutes
## Difficulty: Beginner

## Prerequisites
- Discord Bot Token
- OpenSIN installed

## Step 1: Create Discord Agent

```javascript
import { DiscordAgent } from '@opensin/integrations/discord';

const agent = new DiscordAgent({
  token: process.env.DISCORD_BOT_TOKEN,
  name: 'my-discord-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  console.log('Received:', msg.content);
  await agent.respond(`You said: ${msg.content}`);
});

await agent.start();
```

## Step 2: Run Agent

```bash
DISCORD_BOT_TOKEN=your_token node index.js
```

## Step 3: Test Bot

Send a message to your bot on Discord.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Integration: WhatsApp](whatsapp.md)
- [Integration: Slack](slack.md)
