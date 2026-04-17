# Project 18 — SIN Fleet Compliance Board

> **Status Contract & Transition Rules**
> Version: 2026.04.17 | Issue: OpenSIN-documentation#117

## Purpose

Project 18 (`https://github.com/orgs/OpenSIN-AI/projects/18`) is the executive compliance board for the entire OpenSIN A2A fleet. It tracks sovereign repo governance rollout, HF fleet recovery, factory hardening, and dashboard route provisioning.

This document defines the **fail-closed status semantics** — what each status means, when transitions are allowed, and what evidence is required to move between states.

## Status Definitions

| Status | Meaning | Entry Criteria | Exit Criteria |
|--------|---------|----------------|---------------|
| **Backlog** | Identified but not yet planned | Issue exists with clear scope | Assigned to a wave/sprint |
| **Todo** | Planned for current wave, not started | Assigned, dependencies satisfied | Work begins (branch created) |
| **In Progress** | Active work underway | Branch exists, at least 1 commit pushed | PR opened OR blocked |
| **Blocked** | Cannot proceed due to external dependency | Blocker identified and documented in issue comment | Blocker resolved with evidence |
| **In Review** | PR open, awaiting merge | PR passes all required checks | PR merged to main |
| **Done** | Merged and verified | PR merged, post-merge verification passed | N/A (terminal state) |
| **Cancelled** | No longer needed | Justification posted in issue | N/A (terminal state) |

## Transition Rules (Fail-Closed)

### Rule 1: No Status Without Evidence

Every status transition MUST have a corresponding evidence artifact:

| Transition | Required Evidence |
|------------|-------------------|
| Backlog → Todo | Issue comment stating "Dependencies satisfied: [list]" |
| Todo → In Progress | Branch name posted in issue, first commit pushed |
| In Progress → In Review | PR URL posted in issue comment |
| In Progress → Blocked | Blocker issue URL + explanation posted |
| Blocked → In Progress | Blocker resolution evidence (commit, PR, or external proof) |
| In Review → Done | Merge commit SHA + post-merge verification result |
| Any → Cancelled | Justification comment explaining why |

### Rule 2: No Backward Transitions Without Incident

Moving an item backward (e.g., In Review → In Progress, Done → In Progress) requires:
1. An incident comment explaining what failed
2. A linked GitHub issue for the regression if applicable
3. Update to the master tracker (`global-brain#30`)

### Rule 3: Blocked Items Have Timeout

- Items in **Blocked** status for > 48 hours trigger a Telegram alert to the fleet operator
- Items in **Blocked** status for > 7 days trigger automatic escalation to `A2A-SIN-TelegramBot` → CEO channel
- The blocker issue MUST be actively worked — parking items in Blocked without progress is a protocol violation

### Rule 4: Done Requires Post-Merge Verification

An item is NOT Done just because the PR merged. Post-merge verification checklist:

- [ ] `bun run build` succeeds on main after merge
- [ ] Agent card parses correctly (if agent repo)
- [ ] No regression in fleet validator output
- [ ] Required files from `required-files.manifest.json` all present (if applicable)
- [ ] Public URL returns 200 (if route was added)

### Rule 5: Fail-Closed Default

If the status of an item cannot be determined (CI down, verification script missing, evidence unclear):
- The item is treated as **Blocked**
- A diagnostic comment is posted automatically
- The item does NOT move forward until the ambiguity is resolved

## Wave Structure

Project 18 items are organized into execution waves with explicit dependency ordering:

### Wave 0: Foundation (CURRENT)
- Template-SIN-Agent canonical manifest (#149, #147, #148)
- Governance contract templates (upgraded-opencode-stack#26)
- Project 18 status contract (this document, #117)

### Wave 1: Factory & Routes
- Factory template parity fix (OpenSIN-backend#1162, #1163)
- Dashboard route pages (OpenSIN-WebApp#8, #9)
- Governance adoption in docs (OpenSIN-documentation#116)

### Wave 2: Normalization & Recovery
- Per-repo normalization for 6 A2A-SIN-Code-* repos (Infra-SIN-Dev-Setup#24-#29)
- Backfill sync automation (Infra-SIN-Dev-Setup#30)
- HF fleet canary verification (OpenSIN-overview#18, #21)

### Wave 3: Rollout & Verification
- HF fleet fan-out (OpenSIN-overview#20, #22)
- Homepage URL rollout (OpenSIN-overview#19, Infra-SIN-Dev-Setup#31)
- Live route verification (OpenSIN-WebApp#10)
- E2E factory validation (OpenSIN-backend#1164)

### Wave 4: Compliance Close
- Fleet readiness summary (OpenSIN-overview#23)
- Master tracker close (global-brain#30)

## Automation Hooks

### Telegram Alerts

| Event | Channel | Bot |
|-------|---------|-----|
| Item blocked > 48h | fleet-alerts | sin-telegrambot |
| Item blocked > 7d | ceo-escalation | sin-telegrambot |
| Wave completed | fleet-status | sin-telegrambot |
| Regression detected | fleet-alerts | sin-telegrambot |

### GitHub Actions (Future)

When CI is available on Project 18 repos:
- Auto-move items from "In Review" → "Done" when PR merges
- Auto-move items to "Blocked" when required checks fail
- Auto-post verification results as issue comments

## Master Tracker

The master tracker for the entire rollout is `Delqhi/global-brain#30`. Every wave completion and every significant status change MUST be posted as a comment there.

## Compliance Verification

To verify a repo is fully compliant, run:

```bash
# Validate against canonical manifest
node scripts/validate-sin-a2a-fleet.mjs --repo OpenSIN-AI/<repo-name>

# Check all required files exist
jq -r '.requiredFiles[] | select(.failSeverity == "critical") | .path' required-files.manifest.json | \
  while read f; do
    gh api "repos/OpenSIN-AI/<repo-name>/contents/$f" --silent 2>/dev/null && echo "✅ $f" || echo "❌ $f MISSING"
  done
```

## References

- Master Tracker: [global-brain#30](https://github.com/Delqhi/global-brain/issues/30)
- Project Board: [Project 18](https://github.com/orgs/OpenSIN-AI/projects/18)
- Required Files Manifest: [Template-SIN-Agent/required-files.manifest.json](https://github.com/OpenSIN-AI/Template-SIN-Agent/blob/main/required-files.manifest.json)
- Repo Governance Contract: [Template-SIN-Agent/governance/repo-governance.json](https://github.com/OpenSIN-AI/Template-SIN-Agent/blob/main/governance/repo-governance.json)
