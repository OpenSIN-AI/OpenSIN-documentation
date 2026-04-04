# Example: Discord Bot

## Overview

Discord bot integration example.

## Code

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

## Running the Example

```bash
DISCORD_BOT_TOKEN=your_token node discord-bot.js
```

## Testing

Send a message to your bot on Discord.

## Expected Output

```
Received: Hello!
Responded: You said: Hello!
```

## Next Steps
- [Telegram Bot Example](telegram-bot.md)
- [Slack Example](../integrations/slack.md)
