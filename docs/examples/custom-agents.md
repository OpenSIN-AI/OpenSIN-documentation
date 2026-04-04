# Example: Custom Agents

## Overview

Complete custom agent example with external API integration.

## Code

```typescript
import { Agent, Message, AgentOptions } from '@opensin/core';

interface CustomAgentOptions extends AgentOptions {
  apiKey: string;
  baseUrl: string;
}

export class CustomAgent extends Agent {
  private apiKey: string;
  private baseUrl: string;

  constructor(options: CustomAgentOptions) {
    super(options);
    this.apiKey = options.apiKey;
    this.baseUrl = options.baseUrl;
  }

  async processMessage(msg: Message): Promise<string> {
    const response = await fetch(`${this.baseUrl}/process`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: msg.text })
    });

    const data = await response.json();
    return data.response;
  }
}

// Usage
const agent = new CustomAgent({
  name: 'custom-agent',
  capabilities: ['custom-processing'],
  apiKey: process.env.API_KEY,
  baseUrl: 'https://api.example.com'
});

await agent.start();
```

## Testing

```javascript
describe('CustomAgent', () => {
  it('should process messages', async () => {
    const agent = new CustomAgent({
      name: 'test-agent',
      capabilities: ['test'],
      apiKey: 'test-key',
      baseUrl: 'https://test-api.example.com'
    });

    const response = await agent.processMessage({ text: 'Hello!' });
    expect(response).toBeDefined();
  });
});
```

## Next Steps
- [Multi-Agent Team Example](multi-agent.md)
- [Telegram Bot Example](telegram-bot.md)
