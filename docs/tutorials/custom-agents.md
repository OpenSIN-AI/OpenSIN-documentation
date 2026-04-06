---
title: "Building Custom Agents"
---

# Building Custom Agents

Create your own A2A agent from scratch using the OpenSIN Agent SDK.

## Prerequisites

- Node.js 20+
- npm or pnpm
- GitHub account (for publishing)
- OpenSIN CLI installed

## Quick Start with Template

The fastest way to create a new agent:

```bash
# Clone the official template
gh repo create OpenSIN-AI/A2A-SIN-MyAgent \
  --template OpenSIN-AI/Template-A2A-SIN-Agent \
  --public

cd A2A-SIN-MyAgent
npm install
```

## Manual Setup

### 1. Initialize the Project

```bash
mkdir my-agent && cd my-agent
npm init -y
npm install @opensin/agent-sdk @opensin/sdk typescript
npx tsc --init
```

### 2. Define the Agent

Create `src/agent.ts`:

```typescript
import { AgentBuilder, ToolRegistry } from '@opensin/agent-sdk'

// Register custom tools
const tools = new ToolRegistry()

tools.register({
  name: 'analyze_code',
  description: 'Analyze code quality and suggest improvements',
  parameters: {
    type: 'object',
    properties: {
      filePath: { type: 'string', description: 'Path to the file to analyze' },
      checks: {
        type: 'array',
        items: { type: 'string' },
        description: 'Checks to run: complexity, style, security, performance',
      },
    },
    required: ['filePath'],
  },
  execute: async ({ filePath, checks }) => {
    // Your analysis logic here
    const results = await runAnalysis(filePath, checks)
    return { content: JSON.stringify(results, null, 2) }
  },
})

// Build the agent
const agent = AgentBuilder
  .create('sin-code-analyzer')
  .withDescription('Analyzes code quality across multiple dimensions')
  .withTools(tools)
  .withModel('openai/gpt-5.4')
  .withSystemPrompt(`You are a code quality analyzer. 
    Use the analyze_code tool to inspect files and provide actionable feedback.`)
  .build()

export default agent
```

### 3. Create the Agent Card

Create `.well-known/agent-card.json`:

```json
{
  "name": "SIN-Code-Analyzer",
  "version": "1.0.0",
  "description": "Analyzes code quality across complexity, style, security, and performance",
  "url": "https://code-analyzer.opensin.ai",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false,
    "stateTransitionHistory": true
  },
  "skills": [
    {
      "id": "analyze",
      "name": "Code Analysis",
      "description": "Run quality checks on source code files",
      "tags": ["code-quality", "analysis", "linting"]
    }
  ],
  "authentication": {
    "schemes": ["bearer"]
  },
  "defaultInputModes": ["text"],
  "defaultOutputModes": ["text"]
}
```

### 4. Add the CLI

Create `src/cli.ts`:

```typescript
import { createCLI } from '@opensin/agent-sdk'
import agent from './agent'

const cli = createCLI(agent, {
  name: 'sin-code-analyzer',
  version: '1.0.0',
  commands: {
    'print-card': () => agent.printCard(),
    'serve-mcp': () => agent.serveMCP(),
    'run-action': (action) => agent.runAction(JSON.parse(action)),
  },
})

cli.parse(process.argv)
```

### 5. Add MCP Server Support

Create `src/mcp.ts`:

```typescript
import { MCPServer } from '@opensin/agent-sdk'
import agent from './agent'

const server = new MCPServer(agent, {
  transport: 'stdio',  // or 'http'
})

server.start()
```

### 6. Build and Test

```bash
# Build
npm run build

# Test the agent card
node dist/src/cli.js print-card

# Test a health check
node dist/src/cli.js run-action '{"action":"agent.help"}'

# Start the MCP server
node dist/src/cli.js serve-mcp
```

## Agent Configuration Files

Every agent needs these files:

| File | Purpose |
|------|---------|
| `agent.json` | Agent metadata and configuration |
| `A2A-CARD.md` | Human-readable agent description |
| `AGENTS.md` | Agent behavior instructions |
| `.well-known/agent-card.json` | Machine-readable discovery card |
| `.well-known/agent.json` | Agent manifest |
| `mcp-config.json` | MCP server configuration |

## Registering with the Fleet

### 1. Add to OpenCode Config

Add your agent's MCP entry to `opencode.json`:

```json
{
  "mcpServers": {
    "sin-code-analyzer": {
      "command": "node",
      "args": ["/path/to/dist/src/cli.js", "serve-mcp"]
    }
  }
}
```

### 2. Set GitHub Topics

```bash
gh repo edit --add-topic opnsin-agent
gh repo edit --homepage "https://opensin.ai/agents/sin-code-analyzer"
```

### 3. Register Telegram Bot

Every agent needs its own Telegram bot for notifications:

```bash
# Register with BotFather, then:
sin-telegrambot register --token "YOUR_BOT_TOKEN" --name "sin-code-analyzer"
```

## Testing Checklist

Before marking your agent as ready:

- [ ] `npm run build` succeeds
- [ ] `print-card` outputs valid agent card JSON
- [ ] `run-action '{"action":"agent.help"}'` returns help text
- [ ] Health check action responds successfully
- [ ] MCP server starts and accepts connections
- [ ] Agent card at `/.well-known/agent-card.json` returns 200
- [ ] `/a2a/v1` endpoint exists and does not return 404
- [ ] GitHub topics include `opnsin-agent`
- [ ] Telegram bot registered and responsive
