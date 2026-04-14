# 🏷️ Naming Conventions & SSOT

## The Ultimate SSOT
Before modifying any code or reading further, you must be aware of the **[OpenSIN-overview](https://github.com/OpenSIN-AI/OpenSIN-overview)** repository. It is the Single Source of Truth for the entire organization.

## Strict Naming Schema
To prevent architectural chaos, every repository in the OpenSIN-AI organization **MUST** follow this strict naming schema:

`[Type]-SIN-[Name]`

### Valid Types:
- `Team-SIN-*` (Orchestrators, Hubs, Managers. E.g., `Team-SIN-Legal`)
- `A2A-SIN-*` (Worker Agents that execute tasks. E.g., `A2A-SIN-ClaimWriter`)
- `MCP-SIN-*` (Model Context Protocol Servers / Tools. E.g., `MCP-SIN-Browser`)
- `CLI-SIN-*` (Command Line Interfaces / Terminals. E.g., `CLI-SIN-Code`)
- `Template-SIN-*` (Blueprints for the forge scripts)
