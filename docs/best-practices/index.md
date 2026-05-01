---
title: "Best Practices"
---

# Best Practices

This section is the rulebook for building, operating, debugging, and scaling the OpenSIN fleet.
It is not a loose suggestion shelf. It is the operational memory of the system.

## Core Mandates

| Document                                                 | Focus                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Agent Design](/best-practices/agent-design)             | Ultimate fleet mandates, no-silo rules, self-healing, test-proof culture |
| [Code Quality](/best-practices/code-quality)             | Extreme commenting mandate, anti-AI-slop, review discipline              |
| [Error Handling](/best-practices/error-handling)         | Immediate bug registry, no-assumptions, self-healing escalation          |
| [Browser Automation](/best-practices/browser-automation) | DevTools-first, anti-bot bypass, Chrome profile law                      |
| [A2A Communication](/best-practices/a2a-communication)   | Pure agentic paradigm, inbound governance, opencode-only LLM usage       |

## System Reliability & Execution

| Document                                                               | Focus                                                       |
| ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Testing](/best-practices/testing)                                     | Runtime proof, workflow validation, UI/browser verification |
| [Monitoring & Observability](/best-practices/monitoring-observability) | Health, metrics, evidence retention, alert usefulness       |
| [Team Orchestration](/best-practices/team-orchestration)               | Parallel vs sequential work, retries, specialist routing    |
| [HF Fleet Keep-Alive](/best-practices/hf-fleet-keepalive)              | Hugging Face wake strategy, persistence, recovery           |
| [CI/CD mit n8n + sin-github-action](/best-practices/ci-cd-n8n)         | Zero-billing CI via OCI + n8n                               |

## Advanced / Specialized

| Document                                                            | Focus                                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [MCP Integration](/best-practices/mcp-integration)                  | MCP transport, safety, integration patterns                                   |
| [Plugin Development](/best-practices/plugin-development)            | Plugin architecture and extension rules                                       |
| [Performance](/best-practices/performance)                          | Cost, model routing, latency, efficiency                                      |
| [Security](/best-practices/security)                                | Secrets, auth boundaries, operator trust                                      |
| [Software 3.0: Neural-Bus](/best-practices/software-3.0-neural-bus) | Higher-level architecture doctrine                                            |
| [SEO Pipeline](/best-practices/seo-pipeline)                        | Proof-of-work blog publishing pipeline                                        |
| [**Simone MCP + PCPM** ⭐ PFLICHT](/best-practices/simone-mcp-pcpm) | Semantic code intelligence + cross-session memory — mandatory for every agent |

## Before You Call Something “Done”

- [ ] issue exists and matches the work
- [ ] code is commented with WHAT / WHY / WHY NOT / CONSEQUENCES
- [ ] repo-native checks pass
- [ ] runtime proof exists
- [ ] screenshots/logs exist where relevant
- [ ] docs updated if architecture or workflow changed
- [ ] remaining risk is clearly stated

## Final Reminder

The OpenSIN fleet is allowed to move fast **only because** it is forced to leave evidence, structure, and recoverable knowledge behind.
Without that, autonomy becomes chaos.
