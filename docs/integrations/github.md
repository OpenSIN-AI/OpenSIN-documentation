# GitHub Integration

Connect OpenSIN agents to GitHub for automated code workflows.

## Overview

The GitHub integration enables agents to:
- Review pull requests automatically
- Create and manage issues
- Generate code from specifications
- Monitor repository activity
- Automate release workflows

## Setup

### 1. Create GitHub App

1. Go to GitHub Settings → Developer settings → GitHub Apps
2. Create new app with permissions:
   - Pull requests: Read & Write
   - Issues: Read & Write
   - Contents: Read & Write
   - Commit statuses: Read & Write
3. Install app on your repositories

### 2. Configure OpenSIN

```bash
opensin integration create github \
  --app-id YOUR_APP_ID \
  --private-key-path ~/.github/app-private-key.pem \
  --webhook-secret YOUR_WEBHOOK_SECRET
```

## Agent Configuration

### Code Review Agent

```python
from opensin import Agent
from opensin.integrations import GitHub

github = GitHub(app_id="...", private_key="...")

reviewer = Agent(
    name="code-reviewer",
    model="gpt-4",
    system_prompt="""You are an expert code reviewer. Review code for:
- Bugs and logic errors
- Security vulnerabilities
- Performance issues
- Code style and best practices
- Documentation quality""",
    tools=["github_pr_review", "code_analysis"]
)
```

### Automated PR Review

```python
@github.on("pull_request.opened")
async def review_pr(event):
    diff = await github.get_pr_diff(event.pr_number)
    review = await reviewer.send(f"Review this PR:\n{diff}")
    await github.post_review(event.pr_number, review.content)
```

## Webhook Events

| Event | Trigger |
|-------|---------|
| `pull_request.opened` | New PR created |
| `pull_request.synchronize` | PR updated |
| `pull_request.review_requested` | Review requested |
| `issue.opened` | New issue created |
| `push` | Code pushed |
| `release.published` | Release published |

## Workflows

### Automated Code Review

```
[PR Opened] → [Get Diff] → [Review Agent] → [Post Review] → [Comment on PR]
```

### Issue Triage

```
[Issue Opened] → [Classify Agent] → [Add Labels] → [Assign to Team]
```

### Release Notes Generation

```
[Release Tagged] → [Get Commits] → [Writer Agent] → [Create Release Notes]
```

## Next Steps

- [GitHub Actions Integration](/ops/n8n-cicd)
- [Code Review Agent](/examples/custom-agents)
- [Webhooks & Events](/guide/webhooks-events)
