---
title: Software 3.0 & Neural-Bus Doctrine
description: The architectural doctrine for evented, agentic, issue-centric, bus-driven OpenSIN systems.
---

# Software 3.0 & Neural-Bus Doctrine

> **RULE:** We are not building isolated apps anymore. We are building an evented organism: agents, workflows, repos, UI surfaces, and operators connected through explicit signals, issue state, and recoverable automation.

---

## 1. What “Software 3.0” Means Here

Software 3.0 in OpenSIN means:
- issue-centric work, not hidden local intention
- agentic execution, not single-process heroics
- event-driven coordination, not brittle manual chaining
- observable state, not invisible automation
- modular capabilities, not monolithic dependency traps

The “Neural Bus” is the idea that meaningful state changes propagate through the ecosystem like signals in a nervous system.

---

## 2. The Bus Is Conceptual and Concrete

It is **conceptual** because it describes how all parts of the fleet should think about coordination.
It is **concrete** because it appears in:
- GitHub issues and PRs
- n8n workflows
- agent events and heartbeats
- webhooks
- notifications
- dashboards and logs

---

## 3. Event-Centric Thinking

Design systems around meaningful events:
- issue created
- task dispatched
- agent started
- agent completed
- workflow failed
- deployment published
- alert raised
- approval granted

### Why
Polling disconnected state everywhere creates lag, duplication, and confusion. Events compress coordination.

---

## 4. State Must Be Recoverable

Any important workflow should be resumable from durable state:
- issue state
- repo state
- workflow execution history
- persisted task/session identifiers
- logs/evidence

### Why
If a VM restarts or an agent dies, the system should resume from signal history, not human memory.

---

## 5. Human Operator as High-Privilege Node

The operator is part of the bus, but should not be used as glue for routine work.
Escalate only when:
- permissions are truly required
- destructive approval is needed
- a real blocker survives automation

### Why
The user is the final authority, not the default transport layer.

---

## 6. What the Neural-Bus Rejects

- hidden local-only state
- undocumented side channels
- one-off scripts with no tracker link
- manual handoffs that should be evented
- “done” messages with no durable artifact

---

## 7. Architecture Consequences

A proper Neural-Bus system implies:
- issue-first execution
- branch/PR traceability
- workflow/agent status visibility
- durable evidence
- explicit contracts between modules
- bounded retries and escalation

---

## 8. Final Rule

**Software 3.0 is software that can think in public, recover from interruption, and coordinate through evidence instead of hope.**
If the system depends on one human remembering what happened, it is not Software 3.0.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Self-Hosted** | 0.0 | OCI VM — KEINE Cloud-Dienste |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
