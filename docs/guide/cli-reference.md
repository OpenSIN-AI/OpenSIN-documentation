# CLI Reference

Complete reference for the OpenSIN command-line interface.

## Installation

```bash
pip install opensin-cli
# or
npm install -g @opensin/cli
```

## Commands

### Agent Management

```bash
# Create a new agent
opensin agent create <name> [options]

# List all agents
opensin agent list

# Get agent details
opensin agent get <name>

# Update agent configuration
opensin agent update <name> [options]

# Delete an agent
opensin agent delete <name>

# Test an agent
opensin agent test <name> --prompt "Hello"

# View agent logs
opensin agent logs <name> [--tail 100]
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--model` | LLM model to use | gpt-4 |
| `--system-prompt` | System prompt | "" |
| `--temperature` | Temperature (0-2) | 0.7 |
| `--max-tokens` | Maximum tokens | 4000 |
| `--memory` | Enable memory | true |
| `--tools` | Comma-separated tools | "" |

### Team Management

```bash
# Create a new team
opensin team create <name> [options]

# List all teams
opensin team list

# Add agent to team
opensin team add <team> <agent>

# Remove agent from team
opensin team remove <team> <agent>

# Execute team task
opensin team exec <team> --task "Research AI trends"

# View team status
opensin team status <team>
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--strategy` | Execution strategy | sequential |
| `--max-iterations` | Max iterations | 10 |
| `--timeout` | Timeout in seconds | 300 |

### A2A Protocol

```bash
# Get agent card
opensin a2a card <agent-url>

# Send A2A message
opensin a2a send <agent-url> --type request --data '{"task": "Research"}'

# List A2A connections
opensin a2a connections

# Test A2A connectivity
opensin a2a ping <agent-url>
```

### Deployment

```bash
# Deploy to HF Spaces
opensin deploy hf [options]

# Deploy to Docker
opensin deploy docker [options]

# Deploy to Kubernetes
opensin deploy k8s [options]

# Check deployment status
opensin deploy status

# Rollback deployment
opensin deploy rollback
```

### Monitoring

```bash
# View metrics
opensin metrics [--agent <name>] [--period 24h]

# View logs
opensin logs [--agent <name>] [--tail 100]

# View errors
opensin errors [--agent <name>] [--period 24h]

# Health check
opensin health
```

### Configuration

```bash
# Set configuration
opensin config set <key> <value>

# Get configuration
opensin config get <key>

# List all configuration
opensin config list

# Reset to defaults
opensin config reset
```

### Authentication

```bash
# Login
opensin auth login

# Logout
opensin auth logout

# Check auth status
opensin auth status

# Rotate API key
opensin auth rotate
```

## Global Options

| Option | Description |
|--------|-------------|
| `--help` | Show help |
| `--version` | Show version |
| `--verbose` | Enable verbose output |
| `--quiet` | Suppress output |
| `--config` | Config file path |
| `--api-key` | API key (overrides config) |
| `--base-url` | API base URL |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENSIN_API_KEY` | API key |
| `OPENSIN_BASE_URL` | API base URL |
| `OPENSIN_LOG_LEVEL` | Log level (debug, info, warn, error) |
| `OPENSIN_CONFIG_PATH` | Config file path |
| `OPENSIN_CACHE_DIR` | Cache directory |

## Examples

### Create and test an agent

```bash
# Create agent
opensin agent create researcher \
  --model gpt-4 \
  --system-prompt "You are an expert researcher." \
  --tools search,code_interpreter

# Test agent
opensin agent test researcher --prompt "What are the latest AI trends?"

# View logs
opensin agent logs researcher --tail 50
```

### Create and run a team

```bash
# Create team
opensin team create research-team --strategy sequential

# Add agents
opensin team add research-team researcher
opensin team add research-team writer
opensin team add research-team reviewer

# Execute task
opensin team exec research-team --task "Research and write about AI in 2026"
```

### Deploy to production

```bash
# Deploy
opensin deploy hf \
  --space my-opensin-app \
  --sdk gradio \
  --hardware cpu-basic

# Check status
opensin deploy status

# View logs
opensin logs --tail 100
```

## Next Steps

- [Getting Started](/guide/getting-started)
- [Installation](/guide/installation)
- [Quick Start](/guide/quick-start)
