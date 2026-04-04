# Developer Onboarding Guide

Welcome to the OpenSIN developer community! This guide will help you get started contributing to OpenSIN.

## Prerequisites

Before you begin, make sure you have:

- **Python 3.10+** installed
- **Git** installed and configured
- **GitHub account** with access to the OpenSIN-AI organization
- **Basic understanding** of AI agents and LLMs
- **Familiarity** with async Python programming

## Step 1: Join the Organization

1. Accept the invitation to [OpenSIN-AI](https://github.com/OpenSIN-AI)
2. Join our [Discord server](https://discord.gg/opensin)
3. Introduce yourself in the `#introductions` channel

## Step 2: Clone the Repository

```bash
# Clone the documentation repo
git clone https://github.com/OpenSIN-AI/OpenSIN-documentation.git
cd OpenSIN-documentation

# Clone the main OpenSIN repo
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN

# Clone the backend (private)
git clone git@github.com:OpenSIN-AI/OpenSIN-backend.git
```

## Step 3: Set Up Your Development Environment

### Install Dependencies

```bash
cd OpenSIN
pip install -r requirements.txt
pip install -e .
```

### Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Run Tests

```bash
pytest tests/
```

## Step 4: Understand the Architecture

OpenSIN consists of several key components:

| Component | Description | Repository |
|-----------|-------------|------------|
| **OpenSIN** | Free version, community showcase | [OpenSIN](https://github.com/OpenSIN-AI/OpenSIN) |
| **OpenSIN-backend** | All proprietary code, services, agents | [OpenSIN-backend](https://github.com/OpenSIN-AI/OpenSIN-backend) |
| **Documentation** | This documentation site | [OpenSIN-documentation](https://github.com/OpenSIN-AI/OpenSIN-documentation) |
| **A2A Agents** | Individual agent implementations | Various `A2A-SIN-*` repos |

### Key Concepts

- **Agents**: Individual AI agents with specific capabilities
- **Teams**: Groups of agents working together
- **A2A Protocol**: Agent-to-Agent communication protocol
- **MCP**: Model Context Protocol for tool integration
- **Orchestrator**: Central coordination system

## Step 5: Read Essential Documentation

Before making contributions, read these documents:

1. [Core Principles](/governance/core-principles) — Our guiding principles
2. [Architecture Overview](/architecture/overview) — System architecture
3. [A2A Protocol](/guide/a2a-protocol) — How agents communicate
4. [Security Guide](/governance/SECURITY) — Security best practices
5. [Contributing Guide](/governance/contributing) — How to contribute

## Step 6: Make Your First Contribution

### Find an Issue

1. Browse [OpenSIN issues](https://github.com/OpenSIN-AI/OpenSIN/issues)
2. Look for `good first issue` labels
3. Comment on the issue to claim it

### Create a Branch

```bash
git checkout -b feat/your-feature-name
```

### Make Changes

1. Write code following our [coding standards](/governance/contributing)
2. Add tests for new functionality
3. Update documentation

### Submit a Pull Request

```bash
git add .
git commit -m "feat: your feature description"
git push origin feat/your-feature-name
```

Then create a PR on GitHub.

## Development Workflow

### Branch Naming

- `feat/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation changes
- `refactor/` — Code refactoring
- `test/` — Test additions
- `chore/` — Maintenance tasks

### Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Code Review

All PRs require:
- At least one approval
- Passing CI checks
- Updated documentation
- Test coverage for new code

## Communication Channels

| Channel | Purpose |
|---------|---------|
| [Discord](https://discord.gg/opensin) | Real-time chat |
| [GitHub Discussions](https://github.com/orgs/OpenSIN-AI/discussions) | Ideas and questions |
| [GitHub Issues](https://github.com/OpenSIN-AI/OpenSIN/issues) | Bugs and tasks |
| Email | Urgent matters |

## Resources

- [API Reference](/api/overview) — Complete API docs
- [Tutorials](/tutorials/agent-basics) — Step-by-step guides
- [Examples](/examples/hello-world) — Code examples
- [Best Practices](/best-practices/overview) — Coding standards
- [Troubleshooting](/guide/troubleshooting) — Common issues

## Next Steps

1. Set up your development environment
2. Read the essential documentation
3. Find an issue to work on
4. Make your first pull request
5. Join the community discussions

Welcome to OpenSIN!
