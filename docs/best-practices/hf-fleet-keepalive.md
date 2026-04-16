---
title: Ultimate HF Fleet Keep-Alive & Persistence Protocol
description: How Hugging Face Spaces must stay awake, preserve state, and avoid accidental data loss.
---

# Ultimate HF Fleet Keep-Alive & Persistence Protocol

> **RULE:** A Hugging Face Free VM is disposable by default. If you do not actively keep it warm and persist critical state, you are building on sand.

---

## 1. Why This Exists

HF Spaces on free tiers can sleep. Sleep means:
- memory is gone
- in-flight sessions die
- temporary files vanish
- browser/auth state may be lost

Therefore every meaningful HF-hosted agent must have:
1. a keep-alive strategy
2. a persistence strategy
3. a recovery strategy

---

## 2. Keep-Alive Strategy

### Canonical pattern
Use a centralized scheduler (n8n on OCI VM) that pings every active HF Space health endpoint on a fixed interval.

### Why centralized
A decentralized “each agent pings itself” model is fragile and harder to audit.
The OCI scheduler is stable, visible, and cheap.

### Recommended interval
Every ~45 minutes for free-tier sleep prevention, unless platform behavior changes.

---

## 3. Persistence Strategy

Never rely on the HF VM filesystem for important long-lived state.
Use one of:
- Hugging Face Dataset as persistence store
- Supabase / remote DB for structured state
- Git repository for durable text/config state

### Typical persisted items
- auth/session bundles
- queue checkpoints
- agent state snapshots
- generated artifacts requiring recovery

---

## 4. Recovery Strategy

On restart, the agent should:
1. restore persisted state
2. verify auth/session validity
3. resume pending jobs safely
4. emit a recovery log/heartbeat

### Why
Without a recovery path, every HF restart becomes hidden data loss.

---

## 5. What Must Never Be Local-Only

Do **not** leave only on the HF filesystem:
- browser auth you cannot cheaply recreate
- workflow queue state
- issue mapping state
- important logs or evidence
- generated outputs the user depends on

---

## 6. Health Endpoint Requirement

Every HF-hosted service should expose a lightweight health endpoint such as:
- `/health`
- `/status`
- a tiny JSON heartbeat route

This is what the keep-alive scheduler pings and what operators use for status checks.

---

## 7. Operational Checklist

- [ ] health endpoint exists
- [ ] n8n keep-alive poller includes the Space URL
- [ ] important state is persisted remotely
- [ ] restart flow restores state
- [ ] recovery produces observable logs

---

## 8. Final Rule

**HF Spaces are excellent workers, but terrible memory.**
Treat them like resumable executors, not durable homes.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **HF Keep-Alive** | 0.0 | JEDER HF Space braucht Ping |
| **Session-Backup** | 0.0 | Hugging Face Dataset als Storage |
