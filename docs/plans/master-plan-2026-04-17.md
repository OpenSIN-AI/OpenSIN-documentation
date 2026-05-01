# Plan: OpenSIN Fleet — Open Issues Resolution Master Plan

**Mode:** plan-and-execute
**Created:** 2026-04-17
**Version:** 1
**Status:** in-progress

---

## Outcomes (OKRs)

**Objective:** Resolve all 14+ open issues, publish governance baseline, stabilize auth pool, ensure fleet-wide consistency.

**Key Results:**

- KR1: Antigravity pool stable (0 "no accounts" errors) — from broken to 100% working
- KR2: All 3 SSOT repos have complete governance artifacts — from 0/3 to 3/3
- KR3: Qwen auth handles non-JSON OAuth responses — from broken to working
- KR4: All 6 new coder repos fully registered with governance — from incomplete to complete
- KR5: MODAL_BASE_URL enforced in bootstrap — from missing to 100% enforced
- KR6: No `npm`/`bunx` usage anywhere in fleet — purge all legacy patterns

---

## Current State

### Strengths

- OCI VM hardening complete (BUG-OCI-001 — 5-layer protection stack deployed)
- 21 teams registered in `oh-my-sin.json` (including new `team-coding-agents`)
- `my-sin-coding-agents.json` created and pushed
- All 3 SSOT repos have BUG-OCI-001 knowledge propagated
- Global brain has BUG-OCI-001 entry in `brain/global/knowledge.json`
- BUN is the only package manager in active use

### Weaknesses

- No governance artifacts (`governance/`, `platforms/`, `n8n-workflows/`, `docs/03_ops/`) in ANY of the 3 SSOT repos
- Antigravity refresh-token pool unstable — subagents fail mid-flight
- Qwen OAuth callback handler crashes on non-JSON responses
- Fresh installs missing `MODAL_BASE_URL` → direct Modal API calls instead of OCI proxy
- Stale OpenCode model metadata on existing installs

### Critical Gaps

- All 3 repos (`upgraded-opencode-stack`, `Infra-SIN-Dev-Setup`, `global-brain`) missing mandatory governance files
- `sovereign-repo-governance` skill mandates `governance/repo-governance.json`, `pr-watcher.json`, `coder-dispatch-matrix.json`, `platforms/registry.json`, `n8n-workflows/inbound-intake.json`, `docs/03_ops/inbound-intake.md`, `scripts/watch-pr-feedback.sh`
- Antigravity pool has no preflight check before delegating to background subagents

---

## Decisions

| Decision                                                  | Rationale                                                             | Alternatives                                                 | Owner          |
| --------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------ | -------------- |
| Publish governance baseline BEFORE stack updates          | PR-Watcher rules must be in place before code changes land            | Do stack update first (REJECTED — breaks governance)         | developer-boss |
| Antigravity preflight as first auth task                  | Pool exhaustion blocks ALL downstream delegation                      | Fix pool first then preflight (REJECTED — will re-break)     | developer-boss |
| Use `oh-my-sin.json` as source of truth for team registry | Already the canonical roster, my-sin-coding-agents.json references it | Separate registry (REJECTED — duplication)                   | developer-boss |
| Deploy governance to upgraded-opencode-stack first        | Most critical — all agents pull from here                             | Parallel deploy to all 3 (REJECTED — need template from one) | developer-boss |

---

## Assumptions

| Assumption                                        | Confidence | Validation Method                                    |
| ------------------------------------------------- | ---------- | ---------------------------------------------------- |
| sin-sync will succeed after governance changes    | 0.85       | Test on OCI VM after changes                         |
| sovereign-repo-governance templates are complete  | 0.90       | Review template files before deployment              |
| Antigravity pool API (Port 8090) is reachable     | 0.95       | curl to `http://92.5.60.87:8090/health`              |
| Qwen OAuth endpoint still returns form-urlencoded | 0.70       | Test with live OAuth flow                            |
| All 6 new coder repos are реально deployed        | 0.80       | Check each repo for `agent.json` and running service |

---

## Phases

### Phase 1: Auth & Pool Stabilization — CRITICAL

- [ ] **P1-T1: Fix Antigravity refresh-token pool (#27)**
  - Effort: P=3h, R=2h, O=1h
  - Dependencies: None
  - Owner: A2A-SIN-Code-Plugin
  - Validation: Subagent spawning works without "no accounts configured" error. Test: spawn 3 parallel subagents, none fail with auth error.

- [ ] **P1-T2: Add Antigravity pool preflight check (#28)**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: [P1-T1]
  - Owner: A2A-SIN-Code-Plugin
  - Validation: Preflight returns healthy status before delegation. Test: invoke preflight when pool is empty → returns explicit "INSUFFICIENT" with rotation trigger.

- [ ] **P1-T3: Fix MODAL_BASE_URL bootstrap injection (#6)**
  - Effort: P=1h, R=30m, O=15m
  - Dependencies: None
  - Owner: A2A-SIN-Code-Command
  - Validation: Fresh `bun install` on new machine has `MODAL_BASE_URL=http://92.5.60.87:4100/modal/v1` in `~/.config/opencode/opencode.env`.

- [ ] **P1-T4: Fix Qwen auth non-JSON OAuth response handling (#23)**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: None
  - Owner: A2A-SIN-Code-Plugin
  - Validation: Qwen login completes successfully even when OAuth provider returns `text/html` or `application/x-www-form-urlencoded`. Test: trigger Qwen OAuth flow with HTML error page fallback.

---

### Phase 2: Governance Baseline Publishing — HIGH

- [ ] **P2-T1: Publish sovereign-repo-governance baseline in upgraded-opencode-stack (#26)**
  - Effort: P=4h, R=2h, O=1h
  - Dependencies: None
  - Owner: developer-boss
  - Validation: `governance/` contains all 7 required files, all valid JSON, `docs/03_ops/inbound-intake.md` exists and describes the intake flow, `scripts/watch-pr-feedback.sh` is executable.

- [ ] **P2-T2: Add governance/ to Infra-SIN-Dev-Setup**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: [P2-T1] (need template from upgraded-opencode-stack)
  - Owner: developer-boss
  - Validation: `governance/repo-governance.json` exists and valid, references OCI VM services correctly.

- [ ] **P2-T3: Add governance/ to global-brain**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: [P2-T2]
  - Owner: developer-boss
  - Validation: `governance/repo-governance.json` exists and valid, `platforms/registry.json` references Box.com and OCI VM.

---

### Phase 3: Stack Update & Cleanup — MEDIUM

- [ ] **P3-T1: Update upgraded-opencode-stack — purge outdated patterns (#22)**
  - Effort: P=3h, R=2h, O=1h
  - Dependencies: [P2-T1]
  - Owner: developer-boss
  - Validation: `grep -r "npm install\|bunx\|npm run" . --include="*.md" --include="*.json" | grep -v node_modules` returns empty. All package.json scripts use `bun run`.

- [ ] **P3-T2: Upgraded OpenCode stack sync via sin-sync (#21)**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: [P3-T1]
  - Owner: developer-boss
  - Validation: `sin-sync` completes without errors, all 3 machines (Mac, OCI VM, HF VMs) show consistent opencode config.

- [ ] **P3-T3: Fix stale OpenCode model metadata on existing installs (#5)**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: None
  - Owner: A2A-SIN-Code-Command
  - Validation: After cache flush, `opencode providers list` shows correct model routing for all providers.

---

### Phase 4: Documentation & Skills — MEDIUM

- [ ] **P4-T1: Document Antigravity pool recovery playbook (#29)**
  - Effort: P=2h, R=1h, O=30m
  - Dependencies: [P1-T1]
  - Owner: developer-boss
  - Validation: Recovery steps documented in `global-brain/brain/global/knowledge.json` and `docs/guides/antigravity-recovery.md`.

- [ ] **P4-T2: Repair /gen-thumbnail (#7, #8)**
  - Effort: P=3h, R=2h, O=1h
  - Dependencies: None
  - Owner: A2A-SIN-Code-Frontend
  - Validation: `/gen-thumbnail prompt` produces a valid 16:9 thumbnail image via Antigravity image generation.

- [ ] **P4-T3: Create /3d-web skill (#18)**
  - Effort: P=4h, R=2h, O=1h
  - Dependencies: None
  - Owner: A2A-SIN-Code-Frontend
  - Validation: `/3d-web $ARGUMENTS` skill exists and produces a runnable pipeline using nvidia-3d-forge patterns.

---

### Phase 5: Complex Epics — OPTIONAL (defer if blocked)

- [ ] **P5-T1: Multi-Agent Boardroom epics (#11-#17)**
  - Effort: P=8h, R=4h, O=2h
  - Dependencies: [P1-T2]
  - Owner: A2A-SIN-Zeus
  - Validation: Boardroom sessions successfully orchestrate multiple agents with session pool context.

- [ ] **P5-T2: OMOC swarm/dispatch architecture fix (#4)**
  - Effort: P=6h, R=3h, O=1h
  - Dependencies: [P5-T1]
  - Owner: A2A-SIN-Zeus
  - Validation: Dispatch handles 10+ concurrent agent calls without race conditions or deadlocks.

---

## Dependency Graph

```
P1-T1 (Auth Pool) ──┬──► P1-T2 (Preflight) ──► P5-T1 (Boardroom) ──► P5-T2 (OMOC)
                    │
P1-T1 ─────────────┼──────────────────────────► P4-T1 (Recovery Docs)
                    │
P1-T1 ─────────────┴──► P1-T4 (Qwen Auth) ────► (standalone)
P1-T3 (MODAL_BASE_URL) ──► (standalone)
P2-T1 (Governance UOS) ──► P3-T1 (Stack Update) ──► P3-T2 (sin-sync)
P2-T1 ────────────────────► P2-T2 (Infra Governance) ──► P2-T3 (global-brain Gov)
P3-T3 (Stale Metadata) ──► (standalone)
P4-T2 (gen-thumbnail) ──► (standalone)
P4-T3 (3d-web skill) ──► (standalone)
```

**Critical Path:** P1-T1 → P1-T2 → P5-T1 → P5-T2 (unless deferred)

---

## Risk Register

| ID  | Risk                                                 | Likelihood | Impact | Score | Mitigation                                                             | Owner               | Status     |
| --- | ---------------------------------------------------- | ---------- | ------ | ----- | ---------------------------------------------------------------------- | ------------------- | ---------- |
| R1  | Antigravity pool exhaustion during Phase 1 execution | 0.4        | 9      | 36    | Run P1-T1 first; if exhausted, trigger Token Factory before proceeding | A2A-SIN-Code-Plugin | identified |
| R2  | sin-sync breaks fleet alignment across Mac/OCI/HF    | 0.3        | 8      | 24    | Test on OCI VM first; if broken, revert opencode.json from git         | developer-boss      | identified |
| R3  | Governance templates are incomplete/wrong            | 0.3        | 6      | 18    | Use sovereign-repo-governance skill canonical templates                | developer-boss      | identified |
| R4  | Qwen OAuth endpoint changes response format          | 0.5        | 5      | 25    | Robust content-type detection with multiple fallbacks                  | A2A-SIN-Code-Plugin | identified |
| R5  | New coder repos not actually deployed                | 0.4        | 7      | 28    | Check each repo's `/.well-known/agent-card.json` before claiming done  | developer-boss      | identified |

**Overall Risk Score: 24 (LOW-MEDIUM)**

---

## Rollback Plan

- **Trigger:** Any Phase 1 task leaves auth broken (subagents can't get tokens)
- **Action:**
  1. `git checkout HEAD~1 -- oh-my-sin.json opencode.json` to revert config changes
  2. `killall opencode; opencode &` to restart with old config
  3. Report to `A2A-SIN-TelegramBot` with error details
- **Max Loss:** 2h of work (Phase 1 tasks only)

---

## Done Criteria

- [ ] Phase 1 (Critical): All 4 auth/pool tasks pass validation
- [ ] Phase 2 (Governance): All 3 repos have `governance/` with 7 required files
- [ ] Phase 3 (Stack): No `npm`/`bunx` found, sin-sync succeeds, model metadata clean
- [ ] Phase 4 (Docs/Skills): Antigravity recovery documented, /gen-thumbnail works, /3d-web exists
- [ ] Phase 5 (Epics): Explicitly deferred OR completed with validated boardroom sessions
- [ ] All GitHub issues closed or deferred with reason logged
- [ ] No regressions in existing working functionality

---

## Approval Gates

- [ ] Tech Lead (self-approval as developer-boss acting autonomously)
- [ ] All Phase 1 validations pass without errors
- [ ] No "no accounts configured" errors during execution

---

## Metrics

| Metric            | Value                |
| ----------------- | -------------------- |
| Planned Duration  | 40h                  |
| Confidence 50%    | 35h                  |
| Confidence 85%    | 52h                  |
| Confidence 95%    | 68h                  |
| Scope Creep Count | 0 (Phase 5 deferred) |
| Replan Count      | 0                    |

---

## Version History

| Version | Date       | Changes                                  |
| ------- | ---------- | ---------------------------------------- |
| 1       | 2026-04-17 | Initial plan — 14 issues across 5 phases |
