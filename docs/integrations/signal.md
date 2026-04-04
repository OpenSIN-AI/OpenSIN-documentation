# Integration: Signal

## Step 1: Create Signal Agent

```javascript
import { SignalAgent } from '@opensin/integrations/signal';

const agent = new SignalAgent({
  signalCliPath: '/usr/bin/signal-cli',
  phoneNumber: '+1234567890',
  name: 'my-signal-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

await agent.start();
```

## Next Steps
- [Matrix](matrix.md)
- [IRC](irc.md)
