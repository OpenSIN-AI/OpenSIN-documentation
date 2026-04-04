# Core Concepts

## Overview

OpenSIN is built around several core concepts that enable autonomous agent-to-agent communication.

## Agents

Agents are the fundamental building blocks of OpenSIN. Each agent has:
- **Name**: Unique identifier
- **Capabilities**: What the agent can do
- **Model**: The AI model it uses
- **System Prompt**: Instructions that guide behavior

```javascript
const agent = new Agent({
  name: 'researcher',
  capabilities: ['research', 'analyze'],
  model: 'openrouter/qwen/qwen3.6-plus:free',
  systemPrompt: 'You are a research assistant.'
});
```

## Teams

Teams are collections of agents that work together to accomplish complex tasks.

```javascript
const team = new Team({
  name: 'content-team',
  agents: [researcher, writer, editor],
  orchestrator: 'sequential'
});
```

## A2A Protocol

The Agent-to-Agent (A2A) protocol enables agents to communicate directly with each other.

```javascript
// Agent A sends message to Agent B
await agentA.sendTo(agentB, {
  type: 'request',
  task: 'Research AI trends',
  priority: 'high'
});
```

## MCP Integration

Model Context Protocol (MCP) enables agents to use external tools and services.

```javascript
const agent = new Agent({
  name: 'web-agent',
  mcpServers: ['web-search', 'web-scrape']
});
```

## Orchestration

Orchestration determines how agents coordinate their work:
- **Sequential**: Agents work one after another
- **Parallel**: Agents work simultaneously
- **Hierarchical**: A manager agent delegates tasks

## Next Steps

- [Agent Basics](/guide/agent-basics) — Deep dive into agents
- [Team Orchestration](/guide/team-orchestration) — Learn about team coordination
- [A2A Protocol](/guide/a2a-protocol) — Learn about agent-to-agent communication
