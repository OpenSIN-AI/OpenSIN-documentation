---
title: Ultimate Testing & Verification Protocol
description: The mandatory proof-of-work testing doctrine for OpenSIN agents, SDK modules, web apps, and infrastructure.
---

# Ultimate Testing & Verification Protocol

> **ABSOLUTE RULE:** Nothing is done until reality proves it. A green-looking diff, a persuasive explanation, or a static code review is **not** evidence. The only valid proof is a successful real execution with logs, output, screenshots, or trace artifacts.

---

## 1. The 100% Test-Proof Mandate

### WHAT
Every change must be verified by a real execution path appropriate to the change:
- code path → unit/integration/runtime test
- UI path → browser verification + screenshot
- API path → real request/response check
- workflow path → real run in n8n / queue / webhook
- deploy path → live URL check

### WHY
Large autonomous systems fail most often at runtime boundaries: imports, environment variables, asset paths, auth, network, browser state, race conditions. These are invisible to “looks correct” reasoning.

### WHY NOT OTHERWISE
If you allow agents to declare success from code inspection alone, the fleet fills with half-fixes and ceremonial patches that collapse on first contact with production.

### DEPENDENCIES
This rule directly depends on:
- the absolute no-assumptions mandate
- GitLab LogCenter for evidence retention
- browser automation tooling for UI proof
- issue tracking for public incident memory

### CONSEQUENCES
Any task closed without proof is invalid. The fix must be reopened and retested.

---

## 2. Testing Pyramid, Reinterpreted for Agents

Traditional pyramids still matter, but in agentic systems the top matters more than people think because orchestration, tool-calling, and remote systems are where most failures live.

```text
              ┌───────────────────────────────┐
              │  LIVE / DEPLOY VERIFICATION   │
              │  real URL, webhook, session   │
              └───────────────────────────────┘
                    ┌─────────────────────┐
                    │  E2E / WORKFLOW     │
                    │  browser + API + DB │
                    └─────────────────────┘
                 ┌──────────────────────────┐
                 │  INTEGRATION / CONTRACT  │
                 │  adapters, MCP, A2A, n8n │
                 └──────────────────────────┘
               ┌──────────────────────────────┐
               │  UNIT / SYMBOL-LEVEL LOGIC   │
               │  pure functions, transforms  │
               └──────────────────────────────┘
```

### Practical interpretation
- **Unit tests** protect transformations and pure logic.
- **Integration tests** protect boundaries between modules and tools.
- **E2E tests** prove the user story.
- **Live verification** proves the deployment actually reflects the code.

---

## 3. Required Test Types by Change Class

| Change Type | Minimum Required Proof |
|---|---|
| Pure utility / parser | unit tests + one representative CLI or runtime call |
| SDK module / shared package | unit + integration + consumer build check |
| MCP / adapter / plugin | contract test + real tool invocation |
| n8n workflow | test execution + node output verification |
| Website UI | browser load + critical flow + screenshot |
| Deployment / infra | live endpoint health check + artifact evidence |
| Auth / permissions | explicit success + explicit denial test |

---

## 4. Mandatory Testing Behavior for Agents

### 4.1 Before editing
The agent must identify:
- what can break
- what proof would actually prove correctness
- what existing validation command the repo already uses

### 4.2 During editing
The agent should test incrementally after meaningful milestones, not only at the end.

### 4.3 Before claiming done
The agent must provide:
1. command(s) run
2. exact outcome
3. what those outcomes prove
4. what remains unproven

If something remains unproven, the task is not done.

---

## 5. Browser Verification Requirements

For any UI change, the following is mandatory:
- page loads with no fatal error
- key visible elements confirmed
- important interactions clicked
- screenshot captured for success state
- screenshot captured for failure state if any issue appears
- console errors checked if behavior is suspicious

### Why this matters
UI regressions often hide in CSS, hydration, route loading, or event wiring. A passing build proves almost nothing about visible correctness.

---

## 6. Workflow / n8n Verification Requirements

For any workflow change, the agent must verify:
- trigger fires
- downstream nodes receive expected shape
- side effects occur (issue created, message sent, file written, etc.)
- failure path is visible and understandable
- execution history is inspectable

### Required evidence
- execution ID or screenshot/log of execution
- output payload snippet
- confirmation of the side effect in the target system

---

## 7. Contract Testing for Shared Systems

When multiple repos consume the same module (`@opensin/ui`, MCP contracts, shared adapters), test the provider and at least one consumer.

### Why
A shared package can be valid in isolation but broken in consumer resolution, bundling, CSS order, or type exports.

### Minimum proof for shared packages
- package builds
- consumer app installs/links it
- consumer app build passes
- one visible consumer behavior proves integration

---

## 8. False Success Anti-Patterns

Reject all of these:
- “TypeScript compiles, so it works.”
- “The code looks correct.”
- “The component renders in theory.”
- “The webhook should fire.”
- “It passed once locally without logs.”
- “The PR is small so tests are unnecessary.”

Each of those is not proof. Each is just hope.

---

## 9. Required Artifact Retention

All meaningful verification should leave artifacts when possible:
- screenshots
- execution logs
- terminal output
- PR comments
- issue updates
- deployment URLs

When the project is covered by GitLab LogCenter, upload artifacts there instead of leaving them only in `/tmp`.

---

## 10. Recommended Validation Checklist Before Merge

- [ ] Repo-native lint/build/type checks pass
- [ ] Runtime proof exists
- [ ] Browser proof exists if UI changed
- [ ] Workflow proof exists if automation changed
- [ ] Shared consumer proof exists if package changed
- [ ] Failure path was considered
- [ ] Evidence retained in logs / screenshots / issue / PR

---

## 11. Example Verification Statements

### Good
- `npm run build` passed, proving the package and app bundle compile end-to-end.
- Browser loaded `https://blog.opensin.ai` and displayed the shared header/footer; screenshot saved.
- n8n execution `2200` completed successfully and wrote the markdown file to the blog repo.

### Bad
- “Looks fine now.”
- “Should be good.”
- “Probably fixed.”

---

## 12. Final Rule

**Testing is not a cleanup step. It is the proof layer of engineering.**
If proof is absent, the work is absent.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus
