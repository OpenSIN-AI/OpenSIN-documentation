---
title: Agent Basics Tutorial
description: Learn the fundamentals of OpenSIN agents
---

# Agent Basics Tutorial

Learn how to create, configure, and use OpenSIN agents.

## Prerequisites

- OpenSIN CLI installed (`pip install opensin-cli`)
- API key configured

## Step 1: Create Your First Agent

```bash
opensin agent create researcher \
  --model gpt-4 \
  --system-prompt "You are an expert researcher. Research topics thoroughly and provide detailed reports." \
  --tools web_search,summarizer
```

## Step 2: Test Your Agent

```bash
opensin agent test researcher --prompt "What are the latest AI trends in 2026?"
```

## Step 3: Configure Agent Settings

```bash
# Update model
opensin agent update researcher --model claude-sonnet

# Update system prompt
opensin agent update researcher --system-prompt "New system prompt"

# Add tools
opensin agent update researcher --tools web_search,summarizer,code_interpreter
```

## Step 4: Use Your Agent

```bash
# Send a message
opensin agent send researcher "Research quantum computing"

# View agent logs
opensin agent logs researcher

# Check agent status
opensin agent status researcher
```

## Next Steps

- [Multi-Agent Teams](/tutorials/multi-agent)
- [Custom Agents](/tutorials/custom-agents)
