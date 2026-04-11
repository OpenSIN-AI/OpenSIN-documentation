---
title: Ultimate MCP Integration Doctrine
description: Mandatory patterns for connecting, validating, routing, and safeguarding MCP tools in the OpenSIN ecosystem.
---

# Ultimate MCP Integration Doctrine

> **RULE:** MCPs are force multipliers only when they are explicit, validated, and observable. A mysterious MCP is worse than no MCP.

---

## 1. What MCP Integration Must Achieve

An MCP integration must make these clear:
- what tools it exposes
- how it authenticates
- how it is started / reached
- what project problems it solves
- what failure modes it introduces

---

## 2. Prefer Explicit Discovery

Always verify live tool availability rather than trusting stale documentation.

### Why
MCP servers drift. Installed tools change. Old docs lie.

---

## 3. Startup & Reachability

For each MCP, document:
- startup mode (stdio / streamable HTTP / daemon)
- host/port if relevant
- health-check method
- required env vars / credentials

If you cannot prove reachability, you cannot rely on the MCP.

---

## 4. Security Requirements

MCP integrations must never silently inherit dangerous credentials or broad trust they do not need.
Scope access tightly.
Redact outputs where sensitive.

---

## 5. Tool Selection Discipline

Use an MCP only when it is the correct abstraction.
Do not route simple local work through a remote MCP just to look sophisticated.
Do not avoid an MCP when it is clearly the canonical path.

---

## 6. Failure Handling

When MCP calls fail, capture:
- tool name
- target MCP
- parameters shape
- error class
- whether retry is safe

Do not hide MCP instability behind vague “tool failed” messages.

---

## 7. Final Rule

**An MCP must reduce uncertainty, not increase it.**
If it adds magical hidden behavior, document and constrain it before trusting it.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus
