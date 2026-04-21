---
title: "Sovereign Security Mandate"
description: "Zero-Trust and Auth-Broker standards for the OpenSIN ecosystem."
---

# Sovereign Security Mandate

In the OpenSIN-AI ecosystem, security is not a feature; it is the foundation. We operate on a **Zero-Trust** model between agents.

## 1. The Auth-Broker Pattern
Agents never hold long-lived credentials. All access to sensitive APIs (NIM, Groq, Stripe) must be brokered through the [Passwordmanager](/guide/passwordmanager).

## 2. Evidence-First Auditing
Every destructive action (Write, Delete, Execute) must be logged with a pre-action screenshot and a post-action confirmation published to the Neural-Bus.

## 3. Sandboxing & Scoping
- **FileSystem:** Agents are restricted to the project root unless explicitly authorized by the Operator.
- **Network:** Outbound calls to unverified domains are blocked by the default proxy.

## 4. Secret Redaction
All audit logs and Telegram notifications must pass through the Redaction-Engine to prevent leak of API keys or PII.

---

## ⚖️ Enforcement

Non-compliant agents will be immediately disconnected from the Neural-Bus and moved to a quarantine branch for audit.

→ [View Full Security Specs](/architecture/security)
