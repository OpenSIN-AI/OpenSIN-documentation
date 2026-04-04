# Onboarding Guide

## Welcome to OpenSIN!

## Step 1: Join the Community

- [Discord](https://discord.gg/opensin)
- [Twitter/X](https://twitter.com/opensin_ai)
- [GitHub](https://github.com/OpenSIN-AI/OpenSIN)

## Step 2: Install

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
npm install
npm start
```

## Step 3: Run Your First Agent

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({ name: 'my-agent', capabilities: ['greet'], model: 'openrouter/qwen/qwen3.6-plus:free' });
agent.on('message', async (msg) => { await agent.respond('Hello!'); });
await agent.start();
```

## Step 4: Explore Documentation

- [Getting Started](/guide/getting-started)
- [Quick Start](/guide/quick-start)
- [API Reference](/api/overview)
- [Tutorials](/tutorials/agent-basics)

## Step 5: Contribute

- Read [Community Guidelines](guidelines.md)
- Find [good first issues](https://github.com/OpenSIN-AI/OpenSIN/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- Submit your first PR!

## Need Help?

- [Discord](https://discord.gg/opensin)
- [Email](mailto:support@opensin.ai)
