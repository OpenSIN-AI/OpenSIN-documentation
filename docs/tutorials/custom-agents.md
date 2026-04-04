# Tutorial: Custom Agents

## Duration: 60 minutes
## Difficulty: Advanced

## What You'll Learn
- How to create custom agent classes
- How to add custom capabilities
- How to integrate with external APIs

## Step 1: Create Custom Agent Class

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
      headers: { 'Authorization': `Bearer ${this.apiKey}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: msg.text })
    });
    const data = await response.json();
    return data.response;
  }
}
```

## Next Steps
- [Advanced Orchestration](advanced-orchestration.md)
- [Integration: Telegram](../integrations/telegram.md)
