---
title: Ultimate Browser Automation & Anti-Bot Bypass
description: The mandatory protocols for web interactions, DevTools-first coding, and evading bot detection.
---

# Ultimate Browser Automation & Anti-Bot Bypass

> **Mandate:** Web interaction work must stay inside the approved OpenSIN browser stack. Use `webauto-nodriver-mcp`, attached Chrome profiles, and verified selectors; do not improvise with legacy browser frameworks or guessed DOM targets.

## At a glance

| Area | Standard |
|---|---|
| Allowed tooling | `webauto-nodriver-mcp`, `nodriver`, Chrome DevTools Protocol, `curl_cffi` when TLS impersonation is explicitly required |
| Required proof | DevTools verification, screenshot + vision check after every action, runtime artifacts for failures |
| Forbidden | Playwright, Puppeteer, Selenium, Camoufox, temporary clean profiles, blind selector guesses |

## 1. Technology sovereignty mandate

### What
All web interactions, logins, CAPTCHA handling, and scraping tasks must run through `webauto-nodriver-mcp`, `nodriver`, CDP, or `curl_cffi` when the task specifically needs TLS spoofing.

### Why
`nodriver` attaches to a real Chrome session and reuses genuine cookies, history, and session state. That keeps the interaction close to human browsing behavior and preserves the trust already built into the profile.

### Why not otherwise
Playwright, Puppeteer, Selenium, and similar stacks expose browser automation fingerprints immediately. They also break the shared Chrome-profile workflow the rest of the fleet depends on.

### Dependencies
- `webauto-nodriver-mcp` for browser control
- the Chrome profile rule for authenticated and trusted sessions
- the vision-gate mandate for post-action verification

### Consequences
- Shipping `bun add playwright` or a similar stack is a protocol violation
- Burning trusted sessions or getting the project flagged by Cloudflare destroys future automation capacity

## 2. DevTools-first workflow

### What
Before every click, form fill, or selector change, inspect the live DOM and verify the exact target in DevTools.

1. Check the Elements tab for the real `id`, `class`, and `data-*` attributes.
2. Validate the selector in Console with `document.querySelector(...)`; if it returns `null`, stop.
3. Confirm visibility with checks such as `element.offsetParent !== null` and `window.getComputedStyle(el)`.
4. Read Console errors before triggering the action.

### Why
Modern React/Vue/SPAs generate transient classes, overlays, and delayed elements. Guessing selectors from memory creates flaky scripts that only work under lucky timing.

### Why not otherwise
Blind automation turns recoverable page-state issues into retries, timeouts, and noisy failures. A selector that is not validated against the live DOM is not ready for production use.

### Dependencies
This workflow depends on screenshot capture, console evidence, and explicit failure logging when a selector cannot be proven.

### Consequences
- Unverified selectors are treated as protocol violations
- Empty clicks waste compute, stall flows, and obscure the real page failure

## 3. Chrome profile discipline

### What
Automation must run inside the documented Chrome profiles for the task. Never switch bot-sensitive work to an empty or temporary profile.

| Profile | Example use | Rule |
|---|---|---|
| Business/admin profile | Workspace or admin-console operations | Keep separated from personal and general agent work |
| Default / general profile | Standard agent browsing and known trusted sessions | Do not reuse for admin-only tasks |
| Specialized profile | Bug bounty, freelancing, or target-specific tasks | Reserve it for the documented workflow only |

### Why
Profile separation protects privileged sessions and preserves the trust cookies required for hard targets.

### Why not otherwise
A fresh profile starts without trust history and is far more likely to trigger anti-bot systems immediately.

### Dependencies
One live Chrome instance should own one profile directory at a time. If a profile is already active, attach to the existing session instead of trying to force a second writer onto the same profile.

### Consequences
Cross-contaminating profiles or wiping trusted state is a long-lived operational failure, not a small local mistake.

## 4. Anti-bot defense layers

### What
For bot-sensitive or revenue-critical flows, keep all five layers aligned:

1. **IP reputation** — avoid exposing raw datacenter IPs when the target requires higher trust.
2. **TLS fingerprint** — use native browser traffic or `curl_cffi` where transport impersonation matters.
3. **Browser fingerprint** — stay in visible, real-profile Chrome sessions.
4. **Behavioral signals** — pace input like a human, not a benchmark script.
5. **Challenge persistence** — preserve reusable cookies and session state.

### Why
Hard targets evaluate transport, browser, behavior, and prior trust together. Failing only one layer can still burn the session.

## Verification checklist

- [ ] Approved browser tooling was used end-to-end
- [ ] Every selector was verified against the live DOM before use
- [ ] The correct Chrome profile was documented or reused
- [ ] Screenshot + vision evidence exists after each critical action
- [ ] Bot-sensitive steps use realistic pacing and preserve session state

## Related docs

- [Best-Practice Page Pattern](/best-practices/page-pattern)
- [Testing](/best-practices/testing)
- [Agent Design](/best-practices/agent-design)

---

*Last updated:* 2026-04-21  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Vision-Gate** | -7.0 | KEINE Web-Aktion ohne Screenshot + Vision-Check |
| **DevTools-First** | -1.0 | JEDER CSS-Selektor via DevTools verifizieren |
| **Technologie-Souveränität** | -2.0 | nodriver + Chrome Profil — Playwright/etc. verboten |
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm verboten |
