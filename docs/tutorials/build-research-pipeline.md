# Tutorial: Build an Automated Research Pipeline

Create a multi-agent research system that produces reports automatically.

## What You'll Build

A research pipeline with:
- Topic discovery and planning
- Web research with multiple sources
- Data analysis and synthesis
- Report generation with citations
- Quality review before publishing

## Step 1: Create Research Agents

```python
from opensin import Agent, Team, Pipeline

# Planner Agent
planner = Agent(
    name="planner",
    model="gpt-4",
    system_prompt="Create a research plan with specific questions to answer.",
    tools=["outline_generator"]
)

# Researcher Agents (parallel)
researchers = [
    Agent(name="researcher-tech", model="gpt-4",
          system_prompt="Research technical aspects.",
          tools=["web_search", "arxiv_search"]),
    Agent(name="researcher-market", model="gpt-4",
          system_prompt="Research market aspects.",
          tools=["web_search", "news_search"]),
    Agent(name="researcher-competitors", model="gpt-4",
          system_prompt="Research competitors.",
          tools=["web_search", "company_search"]),
]

# Analyst Agent
analyst = Agent(
    name="analyst",
    model="gpt-4",
    system_prompt="Analyze research findings and identify key insights.",
    tools=["data_analysis", "chart_generator"]
)

# Writer Agent
writer = Agent(
    name="writer",
    model="gpt-4",
    system_prompt="Write a comprehensive report with citations.",
    tools=["markdown_writer", "citation_formatter"]
)

# Reviewer Agent
reviewer = Agent(
    name="reviewer",
    model="gpt-4",
    system_prompt="Review the report for accuracy, completeness, and clarity.",
    tools=["fact_checker", "grammar_checker"]
)
```

## Step 2: Build the Pipeline

```python
research_pipeline = Pipeline([
    planner,           # Step 1: Create research plan
    researchers,       # Step 2: Parallel research
    analyst,           # Step 3: Analyze findings
    writer,            # Step 4: Write report
    reviewer,          # Step 5: Review and approve
])
```

## Step 3: Execute Research

```python
result = await research_pipeline.execute({
    "topic": "The Future of AI Agents in 2026",
    "depth": "comprehensive",
    "sources": 50,
    "format": "markdown"
})

print(result.report)
```

## Step 4: Schedule Automated Research

```python
from opensin import Scheduler

scheduler = Scheduler()

# Run research every Monday at 9 AM
scheduler.add_cron(
    name="weekly-research",
    cron="0 9 * * 1",
    pipeline=research_pipeline,
    input={"topic": "Weekly AI Industry Report"}
)

await scheduler.start()
```

## Next Steps

- [Real-World Use Cases](/examples/use-cases)
- [SIN Feature Dev Workflow](/guide/sin-feature-dev)
