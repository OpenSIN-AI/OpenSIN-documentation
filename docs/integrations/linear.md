# Linear Integration

Connect OpenSIN agents to Linear for issue tracking automation.

## Overview

The Linear integration enables agents to:
- Create and update issues
- Manage projects and roadmaps
- Track team velocity
- Generate status reports
- Automate issue triage

## Setup

```bash
opensin integration create linear \
  --api-key lin_api_YOUR_KEY \
  --webhook-secret YOUR_SECRET
```

## Agent Configuration

```python
from opensin import Agent
from opensin.integrations import Linear

linear = Linear(api_key="lin_api_...")

pm_agent = Agent(
    name="project-manager",
    model="gpt-4",
    system_prompt="You manage Linear issues and projects.",
    tools=["linear_create_issue", "linear_update_issue", "linear_generate_report"]
)
```

## Common Workflows

### Automated Issue Triage

```python
@linear.on("issue.created")
async def triage_issue(event):
    issue = await linear.get_issue(event.issue_id)
    classification = await pm_agent.send(f"Classify: {issue.title}\n{issue.description}")
    await linear.update_issue(event.issue_id, {
        "labels": classification.labels,
        "priority": classification.priority,
        "team": classification.team
    })
```

### Sprint Planning

```python
# Generate sprint plan
backlog = await linear.get_backlog(team_id)
plan = await pm_agent.send(f"Plan sprint from backlog: {backlog}")
await linear.create_sprint(plan)
```

## Next Steps

- [Project Management](/guide/team-orchestration)
- [n8n Workflows](/guide/n8n-workflows)
