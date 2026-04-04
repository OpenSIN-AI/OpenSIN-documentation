# Agent Data Pipeline

Build data pipelines with OpenSIN agents.

## Pipeline Architecture

```
Source → Ingest → Transform → Analyze → Output
```

## Data Sources

| Source | Agent | Description |
|--------|-------|-------------|
| Database | `DatabaseAgent` | SQL/NoSQL queries |
| API | `APIAgent` | REST/GraphQL APIs |
| Files | `FileAgent` | CSV, JSON, Parquet |
| Stream | `StreamAgent` | Kafka, Kinesis |
| Web | `WebScraperAgent` | Web scraping |

## Pipeline Definition

```python
from opensin.pipeline import DataPipeline

pipeline = DataPipeline(
    name="sales-analysis",
    stages=[
        {
            "name": "ingest",
            "agent": DatabaseAgent(query="SELECT * FROM sales"),
            "output": "raw_data"
        },
        {
            "name": "clean",
            "agent": DataCleaningAgent(rules=cleaning_rules),
            "input": "raw_data",
            "output": "clean_data"
        },
        {
            "name": "analyze",
            "agent": AnalysisAgent(metrics=["revenue", "growth"]),
            "input": "clean_data",
            "output": "analysis"
        },
        {
            "name": "report",
            "agent": ReportAgent(template="sales_report"),
            "input": "analysis",
            "output": "final_report"
        }
    ]
)

result = await pipeline.execute()
```

## Real-time Pipeline

```python
from opensin.pipeline import StreamPipeline

stream = StreamPipeline(
    name="log-analysis",
    source=KafkaSource(topic="application-logs"),
    agents=[
        EnrichmentAgent(),
        ClassificationAgent(),
        AlertAgent()
    ],
    sink=DashboardSink()
)

await stream.start()
```

## Data Transformation

```python
from opensin.pipeline import TransformAgent

transformer = TransformAgent(
    rules=[
        {"type": "clean", "fields": ["name", "email"]},
        {"type": "normalize", "field": "phone"},
        {"type": "enrich", "source": "external_api"},
        {"type": "validate", "schema": "user_schema"}
    ]
)

result = await transformer.execute(data)
```

## Error Handling

```python
from opensin.pipeline import ErrorHandling

error_handler = ErrorHandling(
    strategy="dead_letter",
    max_retries=3,
    retry_delay=60,
    dead_letter_queue="failed_records"
)

pipeline.set_error_handler(error_handler)
```

## Monitoring

```python
from opensin.pipeline import PipelineMonitor

monitor = PipelineMonitor(pipeline)

# Track metrics
monitor.track("records_processed")
monitor.track("records_failed")
monitor.track("pipeline_duration")

# Alert on failures
monitor.alert_on("records_failed", threshold=100)
```

## Best Practices

1. **Idempotent stages** — Safe to re-run
2. **Checkpoint progress** — Resume from last checkpoint
3. **Monitor data quality** — Track data quality metrics
4. **Handle failures** — Dead letter queue for failed records
5. **Scale horizontally** — Auto-scale based on data volume

## Next Steps

- [Data Pipeline Guide](/guide/data-pipelines)
- [n8n Workflows](/guide/n8n-workflows)
