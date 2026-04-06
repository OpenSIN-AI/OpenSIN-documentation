# Quick Start

Get OpenCode running in under 5 minutes.

## Prerequisites

- Node.js 20+ (`brew install node`)
- Git configured with GitHub access

## Installation

```bash
# Install OpenCode CLI
curl -fsSL https://opencode.ai/install | bash

# Verify installation
opencode --version
```

## First Session

```bash
# Start OpenCode in your project
cd ~/my-project
opencode

# Or run with a direct message
opencode run "Create a REST API with Express"
```

## Using Agents

```bash
# List available agents
opencode agent list

# Create a new agent
opencode agent create researcher --model openai/gpt-5.4

# Run with a specific agent
opencode run --agent researcher "Research the latest AI trends"
```

## Using Plugins

```bash
# Install a plugin
opencode plugin oh-my-opencode

# Verify plugins
opencode plugin list
```

## Using MCPs

```bash
# Configure MCP servers
opencode mcp add filesystem --command npx -y @modelcontextprotocol/server-filesystem /path/to/dir

# List MCPs
opencode mcp list
```

## Essential Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/agents` | List and switch agents |
| `/models` | List and switch models |
| `/tools` | Show available tools |
| `/export` | Export session data |
| `/compact` | Compact conversation context |

## Next Steps

- [Installation Guide](./installation.md) — Detailed setup instructions
- [Agent Basics](./agent-basics.md) — Learn to use agents effectively
- [MCP Integration](./mcp-integration.md) — Connect external tools
- [Plugin System](./plugin-system.md) — Build custom plugins
