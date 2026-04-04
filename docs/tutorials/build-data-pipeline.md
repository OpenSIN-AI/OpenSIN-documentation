# Tutorial: Build an Automated Data Pipeline

Create a data pipeline that processes, analyzes, and reports on data automatically.

## What You'll Build

A data pipeline that:
- Ingests data from multiple sources
- Cleans and transforms data
- Runs statistical analysis
- Generates visualizations
- Creates narrative reports
- Sends reports via email/Slack

## Step 1: Setup

```bash
mkdir data-pipeline && cd data-pipeline
opensin init
pip install pandas numpy matplotlib
```

## Step 2: Create Pipeline Agents

```python
from opensin import Agent, Pipeline

# Data Ingestion Agent
ingestion = Agent(
    name="ingestion",
    model="gpt-4",
    system_prompt="Load and validate data from sources.",
    tools=["database_query", "api_fetch", "file_read"]
)

# Data Cleaning Agent
cleaning = Agent(
    name="cleaning",
    model="gpt-4",
    system_prompt="Clean and normalize data.",
    tools=["pandas_transform", "data_validation"]
)

# Analysis Agent
analysis = Agent(
    name="analysis",
    model="gpt-4",
    system_prompt="Analyze data and find insights.",
    tools=["statistical_analysis", "trend_detection"]
)

# Visualization Agent
visualization = Agent(
    name="visualization",
    model="gpt-4",
    system_prompt="Create charts and graphs.",
    tools=["matplotlib", "plotly"]
)

# Report Agent
reporting = Agent(
    name="reporting",
    model="gpt-4",
    system_prompt="Write narrative reports from data.",
    tools=["markdown_writer", "template_engine"]
)
```

## Step 3: Build the Pipeline

```python
pipeline = Pipeline([
    ingestion,
    cleaning,
    analysis,
    visualization,
    reporting
])
```

## Step 4: Execute Pipeline

```python
result = await pipeline.execute({
    "sources": {
        "database": "SELECT * FROM sales WHERE date > '2026-01-01'",
        "api": "https://api.example.com/metrics",
        "files": ["./data/q1.csv"]
    },
    "analysis_type": "comprehensive",
    "report_format": "markdown"
})

# Save report
with open("report.md", "w") as f:
    f.write(result.report)
```

## Step 5: Schedule Automated Runs

```python
from opensin import Scheduler

scheduler = Scheduler()

# Run every Monday at 9 AM
scheduler.add_cron(
    name="weekly-report",
    cron="0 9 * * 1",
    pipeline=pipeline,
    input={"sources": {...}}
)

await scheduler.start()
```

## Next Steps

- [Data Pipeline Guide](/guide/data-pipelines)
- [Real-World Use Cases](/examples/use-cases)
