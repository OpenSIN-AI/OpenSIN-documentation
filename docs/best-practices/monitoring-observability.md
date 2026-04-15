---
title: Ultimate Monitoring & Observability Doctrine
description: Mandatory visibility standards for agents, workflows, infrastructure, costs, and incidents across the OpenSIN fleet.
---

# Ultimate Monitoring & Observability Doctrine

> **RULE:** If the fleet cannot see it, the fleet cannot trust it. Monitoring is not decoration. It is the nervous system of autonomous engineering.

---

## 1. Core Principle

Every significant system must answer these questions at all times:
- Is it alive?
- Is it healthy?
- Is it producing value?
- Is it failing silently?
- Is it costing too much?
- Can we explain what happened after the fact?

If a subsystem cannot answer these, it is not production-ready.

---

## 2. Observability Layers

### 2.1 Agent layer
Track:
- active sessions
- error rate
- response latency
- model/tool availability
- background task state
- completion vs timeout vs cancellation

### 2.2 Workflow layer
Track:
- trigger frequency
- execution success/failure
- queue backlogs
- node-level bottlenecks
- side effect confirmation

### 2.3 Infrastructure layer
Track:
- CPU / memory / disk
- network health
- storage exhaustion risk
- process uptime
- HF Space sleep/restart behavior

### 2.4 Economic layer
Track:
- token usage
- hourly cost
- cost spikes per workflow / agent / model
- expensive retry loops

---

## 3. Mandatory Health Checks

Every production-capable component needs a health signal:
- websites → reachable URL / status check
- APIs → health endpoint or equivalent request
- workflows → last successful execution timestamp
- agents → last heartbeat / last activity
- MCP tools → list-tools / smoke-call success

### Why
A component that is “probably fine” is already a liability.

---

## 4. Logging Rules

### 4.1 Structured logs only where possible
Prefer machine-readable logs with fields for:
- timestamp
- component
- severity
- session/task/issue IDs
- action
- result
- error class

### 4.2 Redaction is mandatory
Never log raw secrets, tokens, passwords, or credentials. Log references, not secrets.

### 4.3 Log what matters
Log:
- starts
- finishes
- retries
- failures
- unusual paths
- external side effects
Do **not** drown the system in meaningless noise.

---

## 5. Alerting Rules

Alert only on things that require action.

### Critical alerts
- system down
- auth broken
- workflow repeatedly failing
- data loss risk
- billing/cost anomaly
- stuck queue / stuck retry loop

### Warning alerts
- degraded latency
- elevated error rate
- stale worker
- missed execution window

### Anti-pattern
Do not send alerts for every minor fluctuation. Alert fatigue blinds operators.

---

## 6. Evidence Preservation

Important incidents must preserve evidence:
- screenshots
- logs
- failing payloads
- URLs
- execution IDs
- commit/branch/issue references

Where Box Storage applies, upload there. `/tmp` is temporary, not authoritative.

---

## 7. Dashboards Must Be Operationally Useful

A good dashboard tells the operator what to do next.
A bad dashboard is just colorful guilt.

Minimum useful dashboard sections:
- overall fleet health
- current incidents
- recent failed executions
- hot repos / open blockers
- cost trends
- deployment state

---

## 8. Cost Observability

The fleet must watch for:
- runaway retries
- bad model routing
- needlessly expensive model selection
- repeated failed background tasks
- duplicate agents doing the same work

### Why
An autonomous system that does not watch cost becomes a denial-of-wallet attack against itself.

---

## 9. Silent Failure Prevention

Every important side effect must be checked downstream.
Examples:
- issue supposedly created → confirm issue URL exists
- blog supposedly published → confirm file exists and page resolves
- deploy supposedly finished → confirm URL and assets load
- agent supposedly completed → confirm result retrievable

Do not trust intermediate success messages over final reality.

---

## 10. Suggested Standard Metrics

| Area | Metric | Why it matters |
|---|---|---|
| Agents | active sessions | detects stalls and overload |
| Agents | error rate | reveals instability |
| Agents | avg / p95 latency | reveals slowdowns |
| Workflows | success rate | proves automation health |
| Workflows | execution age | detects dead pipelines |
| Infra | memory / disk | prevents crashes |
| Costs | hourly spend | prevents runaway economics |
| Product | live URL health | proves end-user reality |

---

## 11. Final Rule

**Monitoring is not for feeling informed. It is for enabling intervention.**
If a metric cannot drive a decision, rethink why you are collecting it.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Box.com Storage** | 0.0 | Logs zu Box.com hochladen |
| **Test-Beweis-Pflicht** | 0.0 | Monitoring MUSS echte Daten zeigen |
