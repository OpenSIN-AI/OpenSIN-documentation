# Onboarding Guide

## Welcome to OpenSIN!

This guide will help you get started with OpenSIN.

## Step 1: Join the Community

- Join our [Discord server](https://discord.gg/opensin)
- Follow us on [Twitter/X](https://twitter.com/opensin_ai)
- Star us on [GitHub](https://github.com/OpenSIN-AI/OpenSIN)

## Step 2: Install OpenSIN

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
npm install
npm start
```

## Step 3: Run Your First Agent

```javascript
import { Agent } from '@opensin/core';

const agent = new Agent({
  name: 'my-first-agent',
  capabilities: ['greet'],
  model: 'openrouter/qwen/qwen3.6-plus:free'
});

agent.on('message', async (msg) => {
  await agent.respond('Hello!');
});

await agent.start();
```

## Step 4: Explore the Documentation

- [Getting Started](/guide/getting-started)
- [Quick Start](/guide/quick-start)
- [Core Concepts](/guide/core-concepts)
- [API Reference](/api/overview)
- [Tutorials](/tutorials/agent-basics)
- [Examples](/examples/hello-world)

## Step 5: Contribute

- Read our [Contributing Guide](guidelines.md)
- Find [good first issues](https://github.com/OpenSIN-AI/OpenSIN/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- Submit your first PR!

## Need Help?

- [GitHub Discussions](https://github.com/OpenSIN-AI/OpenSIN/discussions)
- [Discord](https://discord.gg/opensin)
- [Email](mailto:support@opensin.ai)

Welcome aboard! 🚀
