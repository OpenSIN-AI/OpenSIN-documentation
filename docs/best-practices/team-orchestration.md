---
title: Ultimate Team Orchestration Doctrine
description: Mandatory patterns for delegation, sequencing, retries, specialist routing, and non-idle fleet behavior.
---

# Ultimate Team Orchestration Doctrine

> **RULE:** Never let the fleet idle when meaningful work exists, and never let multiple agents collide blindly on the same task without structure.

---

## 1. What Team Orchestration Actually Means

Team orchestration is not “start many agents and hope.”
It means:
- deciding which work can run in parallel
- deciding which work must wait on dependencies
- routing tasks to the correct specialist
- capturing progress in issues/trackers
- preventing duplicate/conflicting implementation
- escalating blockers instead of stalling silently

---

## 2. Canonical Routing Logic

### Use the right specialist
- **Explore** → local codebase/context analysis
- **Librarian** → best practices, docs, external guidance
- **Oracle** → architecture, implementation, hard debugging, conventional deep work
- **Frontend specialist** → all UI/UX/styling/design work

### Why
Misrouted tasks waste time, burn tokens, and produce low-quality output.

---

## 3. Parallel vs Sequential Work

### Parallel work is correct when:
- tasks do not mutate the same surface
- tasks only gather information
- tasks are independent implementation tracks

### Sequential work is required when:
- one task defines contracts another task consumes
- shared files would conflict
- architectural decisions must settle first
- irreversible actions depend on previous validation

### Anti-pattern
Running dependent tasks in parallel because it “feels faster” usually creates merge debt and rework.

---

## 4. Dependency Discipline

Every substantial task should know:
- what it depends on
- what depends on it
- what proof unlocks the next stage

Example:
- remote control API contract first
- channel adapters and streaming can begin in parallel, but must track API shape
- UI migrations can scaffold locally, but shared package contract must stabilize early

---

## 5. Non-Idle Fleet Rule

If there are open, actionable issues without an active dispatcher, dispatch immediately.
No unnecessary waiting for ceremony.
No “I’ll get to it later.”

### But also:
Do not manufacture fake activity. Busy-looking chaos is not orchestration.
Only dispatch work that has a real issue, a real branch, and real acceptance criteria.

---

## 6. Retry and Recovery Rules

When an agent stalls or fails:
1. identify whether it is a real blocker or a prompt/working-dir problem
2. salvage existing progress if possible
3. relaunch only the failed branch of work
4. keep issue/branch mapping explicit

### Why
Blindly restarting everything destroys context and causes duplicate work.

---

## 7. Required Progress Reporting

For meaningful long-running work, agents should report:
- current branch
- files created or modified
- blockers
- next step

Progress reports should reduce uncertainty, not add noise.

---

## 8. Issue-Centric Orchestration

GitHub is the source of truth for intent.
That means:
- work starts from issues
- branches map to issues
- progress is explainable through issue comments / PRs
- plans become visible artifacts, not private thoughts

Without issue-centric tracking, orchestration becomes invisible and un-auditable.

---

## 9. Merge Conflict Prevention

Prevent conflicts by:
- isolating branches per issue
- assigning ownership by surface
- sequencing shared-core changes carefully
- extracting contracts first
- not letting multiple agents “just touch the same area quickly”

---

## 10. Final Rule

**Orchestration quality is measured by throughput without confusion.**
If many agents are active but nobody can say who owns what, the system is failing.

---

*Last updated:* 2026-04-10  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **A2A-First** | -200.0 | Teams via A2A-Protokoll |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` |
