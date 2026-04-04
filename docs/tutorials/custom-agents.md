# Tutorial: Custom Agents

## Duration: 60 minutes
## Difficulty: Advanced

## What You'll Learn
- How to create custom agent classes
- How to add custom capabilities
- How to integrate with external APIs
- How to deploy custom agents

## Prerequisites
- Complete [Agent Basics](agent-basics.md)
- Node.js 18+
- TypeScript knowledge

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
    // Custom message processing logic
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
```

## Step 2: Add Custom Capabilities

```typescript
export class CustomAgent extends Agent {
  // ... constructor ...

  async customCapability(data: any): Promise<any> {
    // Implement custom capability
    return await this.processData(data);
  }

  private async processData(data: any): Promise<any> {
    // Custom data processing
    return processedData;
  }
}
```

## Step 3: Deploy Custom Agent

```bash
npm run build
npm run deploy
```

## Next Steps
- [Advanced Orchestration](advanced-orchestration.md)
- [Integration: Telegram Bot](../integrations/telegram.md)
