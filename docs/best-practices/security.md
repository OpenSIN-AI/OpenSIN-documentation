---
title: Ultimate Security & Trust Boundary Doctrine
description: Mandatory rules for secrets, auth, permissions, operator trust, and fail-closed behavior.
---

# Ultimate Security & Trust Boundary Doctrine

> **RULE:** Security in OpenSIN is not a checklist item. It is the discipline of deciding what the system is allowed to trust, what it is never allowed to expose, and how it must fail when trust is uncertain.

---

## 1. Trust Boundaries Must Be Explicit

Every system must know:

- what input is trusted
- what input is untrusted
- what credentials it may access
- what side effects require confirmation
- what should fail closed instead of fail open

If these boundaries are implicit, they will be violated.

---

## 2. Secret Handling Rules

### Never do

- hardcode secrets
- commit secrets
- print secrets in logs
- pass secrets through screenshots or issue bodies
- leave secrets in temporary scripts or throwaway files

### Always do

- keep secrets in env vars / credential stores / approved secret surfaces
- redact logs
- rotate leaked tokens immediately
- prefer least privilege

### Why

A leaked secret is not “just a mistake.” It is an attacker invitation.

---

## 3. Confirmation Gates

Actions that are destructive, security-sensitive, identity-sensitive, or billing-sensitive require explicit confirmation unless the operator has clearly delegated that authority.

Examples:

- deleting data
- rotating production credentials
- changing auth rules
- binding domains
- making billing-affecting API changes

### Why

Autonomy without permission gates becomes self-sabotage.

---

## 4. Fail-Closed by Default

When validation is missing, signatures are absent, auth is unclear, or required config is incomplete, the system must refuse activation.

### Why

Fail-open behavior turns uncertainty into compromise.

---

## 5. Scope & Least Privilege

Every token, credential, and integration should have only the permissions it actually needs.

### Anti-patterns

- one global god-token for everything
- sharing admin credentials across unrelated agents
- reusing powerful tokens in docs/tests/examples

---

## 6. Security Logging

Security-relevant events must be visible without exposing the secret itself:

- auth failures
- permission denials
- suspicious retries
- unexpected environment mismatch
- token rotation events

Log the event, not the credential.

---

## 7. Browser / UI Security Implications

Browser automation often crosses powerful trust boundaries:

- admin consoles
- OAuth approvals
- dashboards with billing power

Therefore profile selection, permissions, and evidence capture are part of security, not just convenience.

---

## 8. Documentation Security Rule

Docs may explain secret flow, but must not contain real secrets, token-shaped values, or copy-pasteable privileged credentials.

### Why

A markdown file in Git is forever unless cleaned aggressively.

---

## 9. Final Rule

**Security is the discipline of protecting trust, not the performance of looking careful.**
If the system cannot explain why it trusts an action, it should not perform it.

---

_Last updated:_ 2026-04-10  
_Status:_ **ACTIVE & MANDATORY**  
_Maintainer:_ sin-zeus

---

## Relevante Mandate

| Mandat               | Priority | Regel                             |
| -------------------- | -------- | --------------------------------- |
| **Antigravity-Only** | -10.0    | KEIN gemini-api Provider          |
| **Annahmen-Verbot**  | -5.0     | KEINE Diagnose ohne Beweis        |
| **Box.com Storage**  | 0.0      | Alle Logs zu Box.com, nicht lokal |
