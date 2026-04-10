---
title: Ultimate Plugin Development Doctrine
description: Rules for building plugins that are clear, safe, observable, and fleet-compatible.
---

# Ultimate Plugin Development Doctrine

> **RULE:** A plugin is not allowed to be clever in private. It must be explicit in capability, predictable in side effects, and documented in behavior.

---

## 1. Plugin Purpose

A plugin should exist only when it creates a reusable capability boundary.
Do not create plugins for trivial wrapper vanity.

---

## 2. Plugin Contracts

Every plugin must define clearly:
- what it exposes
- what it depends on
- what permissions it needs
- what inputs are accepted
- what outputs are guaranteed

---

## 3. Safety Rules

Plugins must:
- avoid hidden credential usage
- avoid destructive defaults
- surface useful errors
- respect operator confirmation gates

---

## 4. Maintainability Rules

A plugin that nobody can debug is a trap.
Document lifecycle, failure modes, expected env, and integration points.

---

## 5. Final Rule

**Plugins should compress complexity for the rest of the fleet, not relocate it into a dark corner.**

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus
