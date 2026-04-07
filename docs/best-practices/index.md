---
title: "Best Practices"
---

# Best Practices

Production-tested guidelines for building, deploying, and operating OpenSIN agents and infrastructure.

## Core Practices

| Document | Focus |
|----------|-------|
| [Agent Design](/best-practices/agent-design) | Single responsibility, model selection, system prompts |
| [Security](/best-practices/security) | Credential management, input validation, MCP security |
| [Performance](/best-practices/performance) | Model routing, context management, caching |

## Extended Practices

| Document | Focus |
|----------|-------|
| [Testing](/best-practices/testing) | Unit, integration, E2E testing strategies |
| [A2A Communication](/best-practices/a2a-communication) | Message design, reliability, security |
| [Plugin Development](/best-practices/plugin-development) | Plugin structure, commands, agents, skills, hooks |
| [MCP Integration](/best-practices/mcp-integration) | Transport selection, connection management, security |
| [Team Orchestration](/best-practices/team-orchestration) | Delegation strategies, retry, monitoring |
| [Error Handling](/best-practices/error-handling) | Error classification, retry patterns, recovery |
| [Monitoring & Observability](/best-practices/monitoring-observability) | Metrics, health checks, alerting, dashboards |
| [Code Quality](/best-practices/code-quality) | Code style, architecture, review standards |

## Quick Reference

### Before Deploying an Agent

- [ ] All secrets in environment variables (not hardcoded)
- [ ] Permission manager configured
- [ ] Error handling covers edge cases
- [ ] Tests pass with adequate coverage
- [ ] Logging configured with redaction
- [ ] Model routing optimized for cost
- [ ] A2A endpoints authenticated

### Before Merging Code

- [ ] ESLint passing
- [ ] TypeScript strict mode clean
- [ ] No `as any` or `@ts-ignore`
- [ ] Tests included
- [ ] Documentation updated
- [ ] Security review completed
