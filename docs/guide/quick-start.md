---
title: Quick Start
description: Build your first OpenSIN agent in 5 minutes
---

# Quick Start

Build your first OpenSIN agent in 5 minutes.

## Step 1: Create an Agent

```bash
opensin agent create researcher \
  --model gpt-4 \
  --system-prompt "You are an expert researcher. Research topics thoroughly." \
  --tools web_search,summarizer
```

## Step 2: Test Your Agent

```bash
opensin agent test researcher --prompt "What are the latest AI trends in 2026?"
```

## Step 3: Create a Team

```bash
opensin team create research-team \
  --agents researcher,writer,reviewer \
  --strategy sequential
```

## Step 4: Execute a Team Task

```bash
opensin team exec research-team \
  --task "Research AI trends and write a comprehensive report"
```

## What's Next?

- [Agent Basics](/guide/agent-basics) — Learn agent fundamentals
- [Team Orchestration](/guide/team-orchestration) — Coordinate multiple agents
- [A2A Protocol](/guide/a2a-protocol) — Agent-to-Agent communication
