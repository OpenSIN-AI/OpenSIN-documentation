# Data Pipeline Guide

Build data processing pipelines with OpenSIN agents.

## Overview

OpenSIN agents can process, transform, and analyze data at scale using pipeline patterns.

## Pipeline Patterns

### ETL Pipeline

```python
from opensin import Pipeline

etl_pipeline = Pipeline([
    ExtractAgent(source="database"),     # Extract data
    TransformAgent(rules=cleaning_rules), # Transform data
    LoadAgent(destination="warehouse"),  # Load data
])

await etl_pipeline.execute()
```

### Analysis Pipeline

```python
analysis_pipeline = Pipeline([
    DataIngestionAgent(),      # Load raw data
    DataCleaningAgent(),       # Clean and normalize
    StatisticalAgent(),        # Run statistical analysis
    VisualizationAgent(),      # Generate charts
    ReportAgent(),             # Write narrative report
])

result = await analysis_pipeline.execute({
    "data_source": "sales_data",
    "period": "Q1 2026"
})
```

### Real-time Pipeline

```python
from opensin import StreamPipeline

stream = StreamPipeline(
    source=KafkaSource(topic="events"),
    agents=[
        EnrichmentAgent(),
        ClassificationAgent(),
        AlertAgent(),
    ],
    sink=DashboardSink()
)

await stream.start()
```

## Data Sources

| Source | Agent | Description |
|--------|-------|-------------|
| Database | `DatabaseAgent` | SQL/NoSQL queries |
| API | `APIAgent` | REST/GraphQL APIs |
| Files | `FileAgent` | CSV, JSON, Parquet |
| Stream | `StreamAgent` | Kafka, Kinesis |
| Web | `WebScraperAgent` | Web scraping |

## Data Transformations

```python
from opensin import TransformAgent

transformer = TransformAgent(
    rules=[
        {"type": "clean", "fields": ["name", "email"]},
        {"type": "normalize", "field": "phone"},
        {"type": "enrich", "source": "external_api"},
        {"type": "validate", "schema": "user_schema"},
    ]
)

result = await transformer.execute(data)
```

## Best Practices

1. **Idempotent** — Pipelines can run multiple times safely
2. **Checkpointing** — Resume from last checkpoint on failure
3. **Monitoring** — Track data quality metrics
4. **Error handling** — Dead letter queue for failed records
5. **Scaling** — Auto-scale based on data volume

## Next Steps

- [n8n Workflows](/guide/n8n-workflows)
- [Real-World Use Cases](/examples/use-cases)
