# n8n Workflow Integration

Automate OpenSIN agent workflows with n8n.

## Overview

n8n provides a visual workflow builder to orchestrate OpenSIN agents, connect to external services, and automate complex processes.

## Setup

### 1. Install n8n

```bash
npm install n8n -g
n8n start
```

### 2. Configure OpenSIN Credentials

1. Open n8n at http://localhost:5678
2. Go to Credentials → Add Credential
3. Select "HTTP Request" or "Webhook"
4. Add your OpenSIN API key

### 3. Import OpenSIN Workflows

```bash
# Import pre-built workflows
n8n import:workflow --input=opensin-workflows.json
```

## Common Workflows

### 1. Agent Trigger → Process → Notify

```
[Webhook] → [OpenSIN Agent] → [Condition] → [Telegram/Discord/Slack]
```

**Use Case:** Receive a request, process with an agent, send response.

### 2. Scheduled Research Report

```
[Cron Schedule] → [Research Agent] → [Writer Agent] → [Email/Slack]
```

**Use Case:** Daily/weekly automated reports.

### 3. Multi-Agent Pipeline

```
[Trigger] → [Agent 1: Research] → [Agent 2: Analyze] → [Agent 3: Write] → [Output]
```

**Use Case:** Complex multi-step processing.

### 4. Social Media Monitoring

```
[Social Media Trigger] → [Sentiment Agent] → [Response Agent] → [Post Response]
```

**Use Case:** Automated social media management.

## HTTP Request Node Configuration

### Send Message to Agent

```json
{
  "method": "POST",
  "url": "https://api.opensin.ai/v1/agents/{{agent_id}}/send",
  "headers": {
    "Authorization": "Bearer {{api_key}}",
    "Content-Type": "application/json"
  },
  "body": {
    "message": "{{ $json.input }}",
    "stream": false
  }
}
```

### Create Team

```json
{
  "method": "POST",
  "url": "https://api.opensin.ai/v1/teams",
  "headers": {
    "Authorization": "Bearer {{api_key}}",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "{{ $json.team_name }}",
    "agents": ["{{ $json.agent_ids }}"],
    "strategy": "sequential"
  }
}
```

### Execute Team Task

```json
{
  "method": "POST",
  "url": "https://api.opensin.ai/v1/teams/{{team_id}}/execute",
  "headers": {
    "Authorization": "Bearer {{api_key}}",
    "Content-Type": "application/json"
  },
  "body": {
    "task": "{{ $json.task }}",
    "max_iterations": 10
  }
}
```

## Webhook Integration

### Receive Agent Events

1. Add Webhook node
2. Set method to POST
3. Configure path: `/webhook/opensin`
4. Connect to processing nodes

### Send Agent Events to n8n

```bash
opensin webhook create \
  --url http://your-n8n:5678/webhook/opensin \
  --events agent.completed,agent.failed,team.completed
```

## Error Handling

### Retry Configuration

```json
{
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 60
}
```

### Error Workflow

```
[Main Workflow] → [Error Trigger] → [Error Handler] → [Notification]
```

## Best Practices

1. **Use credentials** — Store API keys in n8n credentials
2. **Add error handling** — Configure retry and error workflows
3. **Monitor execution** — Enable execution logging
4. **Use environment variables** — For configuration
5. **Version control** — Export workflows regularly

## Next Steps

- [n8n Setup](/ops/n8n-setup)
- [n8n CI/CD](/ops/n8n-cicd)
- [Webhooks & Events](/guide/webhooks-events)
