---
title: Quick Start
description: Build your first OpenSIN agent in 5 minutes
---

# Quick Start

Build your first OpenSIN agent in 5 minutes.

## Step 1: Start the CLI

```bash
cd OpenSIN-Code
npm start
```

## Step 2: Send Your First Query

The OpenSIN-Code CLI provides an interactive REPL. Simply type your query and the agent loop will execute:

```
> Research the latest AI trends in 2026
```

The agent will:
1. Analyze your query
2. Use available tools (web search, file read/write, bash)
3. Iterate until the task is complete
4. Return a structured response

## Step 3: Use Agent Delegation

For complex tasks, delegate to background agents:

```
> Create a research agent to analyze AI trends and write a report
```

## What's Next?

- [Agent Basics](/guide/agent-basics) — Learn agent fundamentals
- [Team Orchestration](/guide/team-orchestration) — Coordinate multiple agents
- [A2A Protocol](/guide/a2a-protocol) — Agent-to-Agent communication
