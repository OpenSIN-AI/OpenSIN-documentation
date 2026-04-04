# Architecture Overview

## Overview

OpenSIN is built with a modular, scalable architecture that enables autonomous agent-to-agent communication.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐ │
│  │ Web App  │  │ CLI      │  │ API      │  │ Integrations│ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬──────┘ │
└───────┼─────────────┼─────────────┼────────────────┼────────┘
        │             │             │                │
        └─────────────┴──────┬──────┴────────────────┘
                             │
                    ┌────────▼────────┐
                    │   A2A Router    │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
  ┌─────▼──────┐  ┌─────────▼────────┐  ┌───────▼───────┐
  │  Agents    │  │   Teams          │  │  MCP Servers  │
  │  (100+)    │  │  (18 teams)      │  │  (64+)        │
  └────────────┘  └──────────────────┘  └───────────────┘
```

## Core Components

### Agent Layer
- Individual agents with specific capabilities
- Each agent has its own model and system prompt
- Agents communicate via A2A protocol

### Team Layer
- Teams coordinate multiple agents
- Orchestrators determine workflow strategy
- Teams handle task delegation and completion

### A2A Protocol Layer
- Standardized agent-to-agent communication
- Message routing and delivery
- Authentication and authorization

### MCP Server Layer
- External tool and service integration
- Standardized tool interfaces
- Extensible plugin architecture

## Next Steps

- [Core Architecture](/architecture/core) — Detailed architecture
- [A2A Protocol](/architecture/a2a) — A2A protocol specification
- [Security](/architecture/security) — Security architecture
