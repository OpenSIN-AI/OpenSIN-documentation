# 🚀 Phase 7 Features: Autonomous PR & CI/CD

> **Status:** Implemented in Sprint 3 (Issue #42)

Phase 7 introduces the ability for Antigravity Rotator agents to **autonomously draft, create, and merge Pull Requests** directly from Issue specifications, while continuously monitoring CI/CD pipelines (GitHub Actions).

## 1. GitHub CLI Agent (`src/github_agent.py`)

A programmatic Python wrapper around the `gh` CLI. It manages authentication, formatting, and data parsing natively using JSON.

### Key Capabilities
- **Issues & PRs**: Fetch rich metadata about GitHub Issues and Pull Requests.
- **Mergeability Check**: Check for merge conflicts directly via `gh`.
- **Merge Engine**: Perform standard `gh pr merge --squash/merge/rebase` dynamically.

---

## 2. Autonomous PR Engine (`src/autonomous_pr.py`)

The brain behind the automated code integration flow.

### Key Capabilities
- **AI-Drafted PRs**: Fetches git diff stats and the original Issue context, then uses `opencode run` (LLM via open-source integration) to auto-draft a professional, conventional-commit formatted Pull Request.
- **Merge Strategy Engine**: Decides whether to `squash`, `merge`, or `rebase` based on:
    - Branch commit count.
    - Presence of merge conflicts.
    - Impact (number of files changed).

### Usage Examples

```python
from src.autonomous_pr import AutonomousPREngine

engine = AutonomousPREngine()

# Automatically draft and create PR from Issue #42
url = engine.create_autonomous_pr(
    issue_number=42,
    head_branch="feat/phase-7-autonomous-pr",
    base_branch="main"
)
print(f"Created PR: {url}")

# Evaluate and Merge
decision = engine.evaluate_merge_strategy(pr_number=101)
if decision.can_merge:
    engine.agent.merge_pr(101, strategy=decision.strategy)
```

---

## 3. CI/CD Monitor (`src/ci_cd.py`)

No more merging broken code. The CI/CD Monitor acts as a blocking gate to ensure that GitHub Actions finish successfully.

### Key Capabilities
- **Status Polling**: `wait_for_checks()` actively polls the GitHub Actions run status using `gh pr checks`.
- **Failure Detection**: Instantly detects `FAILURE`, `CANCELLED`, or `TIMED_OUT` conclusions and aborts the integration process.

---

## 4. CLI Commands

Full CLI access to Phase 7 features inside `main.py`:

```bash
# Autonomously create a PR for Issue #42
python3 -m main github pr-create 42 feat/phase-7-autonomous-pr

# Evaluate and merge a PR with CI checking
python3 -m main github pr-merge 101

# Watch the CI run
python3 -m main github ci-watch 101 --timeout 1200
```

---
**Branding**: OpenSIN / sincode
