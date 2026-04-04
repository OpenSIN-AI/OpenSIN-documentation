# Jira Integration

Connect OpenSIN agents to Jira for automated project management.

## Overview

The Jira integration enables agents to:
- Automatically create and update issues
- Generate sprint reports
- Estimate story points
- Triage and prioritize backlog
- Generate status updates

## Setup

### 1. Create API Token

1. Go to [id.atlassian.com](https://id.atlassian.com)
2. Create API token
3. Note your Jira domain and email

### 2. Configure OpenSIN

```bash
opensin integration create jira \
  --domain your-company.atlassian.net \
  --email your-email@company.com \
  --api-token YOUR_API_TOKEN
```

## Agent Configuration

### Sprint Planning Agent

```python
from opensin import Agent
from opensin.integrations import Jira

jira = Jira(domain="...", email="...", api_token="...")

planner = Agent(
    name="sprint-planner",
    model="gpt-4",
    system_prompt="You are an expert scrum master. Plan sprints and estimate story points.",
    tools=["jira_backlog", "jira_sprint", "estimation"]
)
```

### Automated Issue Triage

```python
@jira.on("issue.created")
async def triage_issue(event):
    issue = await jira.get_issue(event.issue_id)
    classification = await planner.send(f"Classify: {issue.summary}\n{issue.description}")
    await jira.update_issue(event.issue_id, labels=classification.labels)
```

## Next Steps

- [Project Management](/guide/team-orchestration)
- [Automation Workflows](/guide/n8n-workflows)
