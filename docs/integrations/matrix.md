# Integration: Matrix

## Step 1: Create Matrix Agent

```javascript
import { MatrixAgent } from '@opensin/integrations/matrix';

const agent = new MatrixAgent({
  homeserverUrl: 'https://matrix.org',
  accessToken: process.env.MATRIX_ACCESS_TOKEN,
  userId: '@bot:matrix.org',
  name: 'my-matrix-bot',
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

await agent.start();
```

## Next Steps
- [IRC](irc.md)
- [Best Practices](../best-practices/agent-design.md)
