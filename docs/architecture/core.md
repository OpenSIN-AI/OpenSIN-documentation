# Core Architecture

## Overview

Detailed architecture of OpenSIN core components.

## Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Core Components                         │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐ │
│  │ Agent    │  │ Team     │  │ A2A      │  │ MCP         │ │
│  │ Manager  │  │ Manager  │  │ Router   │  │ Manager     │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬──────┘ │
└───────┼─────────────┼─────────────┼────────────────┼────────┘
        │             │             │                │
        └─────────────┴──────┬──────┴────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Event Bus     │
                    └─────────────────┘
```

## Agent Manager

Responsible for:
- Creating and destroying agents
- Managing agent lifecycle
- Monitoring agent health

## Team Manager

Responsible for:
- Creating and managing teams
- Assigning tasks to teams
- Monitoring team performance

## A2A Router

Responsible for:
- Routing messages between agents
- Ensuring message delivery
- Handling message errors

## MCP Manager

Responsible for:
- Managing MCP servers
- Loading and unloading tools
- Monitoring tool health

## Next Steps
- [A2A Protocol](/architecture/a2a)
- [Security](/architecture/security)
