# AWS Integration

Connect OpenSIN agents to AWS services.

## Overview

The AWS integration enables agents to:
- Deploy to EC2, Lambda, ECS
- Store data in S3, DynamoDB
- Process events with SQS, SNS, EventBridge
- Monitor with CloudWatch
- Manage infrastructure with CloudFormation

## Setup

```bash
opensin integration create aws \
  --access-key AKIA... \
  --secret-key YOUR_SECRET \
  --region us-east-1
```

## Agent Configuration

```python
from opensin import Agent
from opensin.integrations import AWS

aws = AWS(access_key="...", secret_key="...", region="us-east-1")

deploy_agent = Agent(
    name="aws-deployer",
    model="gpt-4",
    system_prompt="You deploy and manage AWS infrastructure.",
    tools=["aws_lambda_deploy", "aws_s3_upload", "aws_ecs_update"]
)
```

## Common Workflows

### Auto-Deploy to Lambda

```
[Code Pushed] → [Build] → [Deploy to Lambda] → [Run Tests] → [Update Alias]
```

### S3 Data Processing

```python
@aws.on("s3:ObjectCreated:*")
async def process_upload(event):
    await data_agent.send(f"New file uploaded: {event.key}")
    result = await data_agent.process(event.key)
    await aws.s3.put_object(Bucket="processed", Key=event.key, Body=result)
```

## Next Steps

- [Production Deployment](/guide/deployment-production)
- [Monitoring Guide](/guide/monitoring)
