# Real-Time Agent Systems

Build agents that respond in real-time to events and streams.

## Overview

Real-time agents process events as they happen, enabling:
- Live monitoring and alerting
- Real-time data processing
- Instant response to user actions
- Stream processing and analysis

## Event-Driven Agents

```python
from opensin import EventAgent

agent = EventAgent(
    name="monitor",
    model="gpt-3.5-turbo",  # Fast model for real-time
    system_prompt="Monitor events and alert on anomalies.",
    tools=["alert", "log", "dashboard_update"]
)

# Subscribe to events
agent.subscribe("system.cpu_high")
agent.subscribe("system.memory_high")
agent.subscribe("app.error")

# Handle events
@agent.on_event
async def handle_event(event):
    if event.severity == "critical":
        await agent.tools.alert.send(
            channel="#alerts",
            message=f"🚨 {event.type}: {event.message}"
        )
```

## Stream Processing

```python
from opensin import StreamAgent

agent = StreamAgent(
    name="log-analyzer",
    model="gpt-3.5-turbo",
    system_prompt="Analyze log streams for patterns."
)

# Connect to stream
stream = agent.connect_stream(
    source="kafka",
    topic="application-logs",
    batch_size=100,
    window_seconds=60
)

# Process in real-time
async for batch in stream:
    analysis = await agent.analyze(batch)
    if analysis.anomaly_detected:
        await agent.alert(analysis)
```

## WebSocket Agents

```python
from opensin import WebSocketAgent

agent = WebSocketAgent(
    name="live-assistant",
    model="gpt-4",
    system_prompt="Provide real-time assistance."
)

# Handle WebSocket connections
@agent.on_connection
async def handle_connection(ws):
    async for message in ws:
        response = await agent.process(message)
        await ws.send(response)
```

## Performance Optimization

### Low Latency

```python
agent = Agent(
    name="real-time",
    model="gpt-3.5-turbo",  # Fast model
    temperature=0.1,  # Deterministic
    max_tokens=500,  # Short responses
    streaming=True,  # Stream output
    timeout=5  # 5 second timeout
)
```

### Batch Processing

```python
# Process events in batches
batch_processor = BatchProcessor(
    batch_size=50,
    window_seconds=10,
    agent=analysis_agent
)

async for batch in event_stream:
    results = await batch_processor.process(batch)
    await output_stream.send(results)
```

## Best Practices

1. **Use fast models** — GPT-3.5-turbo or Haiku for real-time
2. **Set timeouts** — Prevent blocking
3. **Stream responses** — Faster perceived latency
4. **Batch when possible** — Reduce API calls
5. **Monitor latency** — Track p99 response times

## Next Steps

- [Webhooks & Events](/guide/webhooks-events)
- [Performance Optimization](/guide/performance-optimization)
