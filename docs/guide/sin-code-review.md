# SIN Code Review Plugin

> **OpenSIN's Automated PR Review** — Parallele Code Review mit Confidence Scoring.

## Overview

Automatisiere Code Reviews mit spezialisierten Agenten die nur Issues mit hoher Confidence melden.

## Setup

```bash
sin plugin install code-review
```

## Review Agents

| Agent | Modell | Aufgabe |
|-------|--------|---------|
| CLAUDE.md Compliance | sonnet | Prüft SIN.md Regeln |
| Bug Detection | opus | Findet Bugs |
| Security Audit | opus | Security Review |
| Performance | sonnet | Performance Issues |
| Style Check | haiku | Code Style |

## Confidence Scoring

Jeder Issue bekommt einen Confidence Score (0-100):

```python
class ReviewIssue:
    file: str
    line: int
    message: str
    severity: str  # critical, warning, info
    confidence: int  # 0-100
    
    def should_report(self) -> bool:
        return self.confidence >= 80  # Nur hohe Confidence
```

## Review Workflow

```
[PR Opened] → [Get Diff] → [Parallel Review Agents] → [Collect Issues]
                                                          ↓
                                              [Filter: Confidence >= 80]
                                                          ↓
                                              [Post Review to PR]
```

## Beispiel Review Output

```markdown
# Code Review: PR #42

## Critical Issues (2)

### 1. SQL Injection Risk
- File: `src/api/users.py:45`
- Confidence: 95/100
- Fix: Use parameterized queries

### 2. Missing Auth Check
- File: `src/api/admin.py:12`
- Confidence: 92/100
- Fix: Add @require_admin decorator

## Warnings (3)

### 1. Unused Import
- File: `src/utils.py:3`
- Confidence: 100/100

## Info (5)
...
```

## GitHub Integration

```python
@github.on("pull_request.opened")
async def auto_review(event):
    diff = await github.get_pr_diff(event.pr_number)
    
    review = await CodeReviewPlugin().review(diff)
    
    if review.critical_issues:
        await github.post_review(event.pr_number, review.markdown)
        await github.request_changes(event.pr_number)
```

## Next Steps

- [SIN Feature Dev](/guide/sin-feature-dev)
- [GitHub Integration](/integrations/github)
