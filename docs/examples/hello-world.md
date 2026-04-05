---
title: Hello World Example
description: Your first OpenSIN agent
---

# Hello World Example

Create your first OpenSIN agent in 5 minutes.

## Prerequisites

```bash
pip install opensin-cli
```

## Step 1: Create an Agent

```bash
opensin agent create hello-agent \
  --model gpt-4 \
  --system-prompt "You are a friendly assistant. Respond with enthusiasm!"
```

## Step 2: Test Your Agent

```bash
opensin agent test hello-agent --prompt "Hello, world!"
```

## Step 3: Send a Message

```bash
opensin agent send hello-agent "What can you do?"
```

## Expected Output

```
Agent: hello-agent
Response: Hello! I'm your friendly OpenSIN assistant! I can help you with research, writing, coding, and much more. What would you like to explore today?
Tokens used: 45
Cost: $0.00135
Duration: 1.2s
```

## Next Steps

- [Multi-Agent Example](/examples/multi-agent)
- [Telegram Bot Example](/examples/telegram-bot)
