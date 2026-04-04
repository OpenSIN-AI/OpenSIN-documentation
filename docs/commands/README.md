# ⌨️ OpenCode Commands — Documentation

> **Stand:** 2026-04-04 | **Total Commands:** 25+ | **Status:** ✅ All documented

## Overview

OpenCode Commands sind spezialisierte Befehle die bestimmte Workflows auslösen.

## Built-in Commands

| Command | Scope | Purpose |
|---------|-------|---------|
| [`/cancel-ralph`](./cancel-ralph.md) | builtin | Cancel active Ralph Loop |
| [`/handoff`](./handoff.md) | builtin | Create a detailed context summary for continuing work in a new session |
| [`/init-deep`](./init-deep.md) | builtin | Initialize hierarchical AGENTS.md knowledge base |
| [`/ralph-loop`](./ralph-loop.md) | builtin | Start self-referential development loop until completion |
| [`/refactor`](./refactor.md) | builtin | Intelligent refactoring with LSP, AST-grep, architecture analysis, codemap, and TDD verification |
| [`/start-work`](./start-work.md) | builtin | Start Sisyphus work session from Prometheus plan |
| [`/stop-continuation`](./stop-continuation.md) | builtin | Stop all continuation mechanisms (ralph loop, todo continuation, boulder) |
| [`/ulw-loop`](./ulw-loop.md) | builtin | Start ultrawork loop - continues until completion with ultrawork mode |

## Plugin Commands (Vercel)

| Command | Purpose |
|---------|---------|
| [`/vercel-plugin:ai-gateway`](./vercel-plugin-ai-gateway.md) | AI Gateway configuration |
| [`/vercel-plugin:ai-sdk`](./vercel-plugin-ai-sdk.md) | Vercel AI SDK guidance |
| [`/vercel-plugin:auth`](./vercel-plugin-auth.md) | Authentication setup (Clerk, Descope, Auth0) |
| [`/vercel-plugin:bootstrap`](./vercel-plugin-bootstrap.md) | Bootstrap project with Vercel resources |
| [`/vercel-plugin:chat-sdk`](./vercel-plugin-chat-sdk.md) | Chat SDK for multi-platform bots |
| [`/vercel-plugin:deploy`](./vercel-plugin-deploy.md) | Deploy to Vercel (preview or production) |
| [`/vercel-plugin:env`](./vercel-plugin-env.md) | Manage environment variables |
| [`/vercel-plugin:investigation-mode`](./vercel-plugin-investigation-mode.md) | Debugging coordinator |
| [`/vercel-plugin:marketplace`](./vercel-plugin-marketplace.md) | Marketplace integrations guidance |
| [`/vercel-plugin:n8n`](./vercel-plugin-n8n.md) | n8n workflow management |
| [`/vercel-plugin:nextjs`](./vercel-plugin-nextjs.md) | Next.js App Router guidance |
| [`/vercel-plugin:observability`](./vercel-plugin-observability.md) | Drains, analytics, monitoring guidance |
| [`/vercel-plugin:shadcn`](./vercel-plugin-shadcn.md) | shadcn/ui component guidance |
| [`/vercel-plugin:status`](./vercel-plugin-status.md) | Show Vercel project status |
| [`/vercel-plugin:vercel-agent`](./vercel-plugin-vercel-agent.md) | AI-powered code review and debugging |
| [`/vercel-plugin:vercel-functions`](./vercel-plugin-vercel-functions.md) | Serverless/Edge Functions guidance |
| [`/vercel-plugin:vercel-storage`](./vercel-plugin-vercel-storage.md) | Blob, Edge Config, Neon, Upstash guidance |
| [`/vercel-plugin:workflow`](./vercel-plugin-workflow.md) | Workflow DevKit guidance |

## Usage

Commands werden in OpenCode Sessions aufgerufen:

```
/check-plan-done
/vercel-plugin:deploy prod
```

---

*Last updated: 2026-04-04 by SIN-Zeus*