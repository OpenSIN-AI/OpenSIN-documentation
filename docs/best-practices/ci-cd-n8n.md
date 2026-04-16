---
title: Ultimate CI/CD via n8n & sin-github-action
description: Mandatory zero-billing delivery doctrine using OCI, n8n, and controlled automation instead of standard GitHub-hosted runners.
---

# Ultimate CI/CD via n8n & sin-github-action

> **RULE:** Standard GitHub-hosted Actions runners are banned for core OpenSIN delivery paths when the OCI+n8n zero-billing route exists.

---

## 1. Why This Exists

The fleet must keep delivery:
- cheap
- observable
- reproducible
- controllable
- integrated with our issue/dispatch model

n8n on OCI gives us exactly that.

---

## 2. Canonical Delivery Path

GitHub event → n8n workflow on OCI → controlled runner / scripts → artifacts / deploy / notifications

### Why
This keeps delivery inside our own automation backbone instead of outsourcing critical orchestration to an opaque hosted runner model.

---

## 3. What Belongs in CI/CD

- lint/build/test gates
- deployment packaging
- branch / PR checks
- release notes / notifications
- environment validation

---

## 4. What Must Be Avoided

- hidden runner behavior
- expensive unnecessary jobs
- duplicate workflows in GitHub and n8n doing the same thing
- deployment scripts that cannot be rerun safely

---

## 5. Required Properties

Every CI/CD flow should be:
- idempotent where possible
- visible in logs
- linked to issue/PR state
- fail-closed on missing secrets or invalid config
- able to notify operators on failure

---

## 6. Final Rule

**CI/CD is not “whatever makes the green checkmark appear.”**
It is controlled, observable delivery with minimal cost and maximal evidence.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **n8n OSS Only** | 0.0 | KEINE n8n Premium Features |
| **Self-Hosted CI/CD** | 0.0 | OCI VM — KEINE GitHub Actions Runner |
| **Bun-Only** | -1.5 | `bun install` / `bun run` |
