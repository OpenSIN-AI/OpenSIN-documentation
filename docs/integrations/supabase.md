# Supabase Integration

Connect OpenSIN agents to Supabase for database and auth services.

## Overview

The Supabase integration enables agents to:
- Query and update databases
- Store and retrieve files
- Manage user authentication
- Use real-time subscriptions
- Execute edge functions

## Setup

```bash
opensin integration create supabase \
  --url https://your-project.supabase.co \
  --service-role-key YOUR_SERVICE_ROLE_KEY
```

## Agent Configuration

### Database Agent

```python
from opensin import Agent
from opensin.integrations import Supabase

supabase = Supabase(url="...", key="...")

db_agent = Agent(
    name="data-analyst",
    model="gpt-4",
    system_prompt="You are a data analyst. Query databases and generate insights.",
    tools=["supabase_query", "data_analysis", "report_generation"]
)
```

### Query Example

```python
# Agent can query the database
result = await db_agent.send("How many users signed up this week?")
# Agent generates SQL, executes via Supabase, returns analysis
```

## Next Steps

- [Data Pipeline Guide](/guide/n8n-workflows)
- [Database Best Practices](/best-practices/performance)
