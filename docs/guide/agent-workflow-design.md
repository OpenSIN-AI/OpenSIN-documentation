# Agent Workflow Design

Design effective workflows for AI agents.

## Workflow Patterns

### 1. Linear Workflow

```
Input → Process → Output
```

```python
from opensin.workflow import LinearWorkflow

workflow = LinearWorkflow([
    {"agent": "ingest", "action": "load_data"},
    {"agent": "process", "action": "transform"},
    {"agent": "output", "action": "generate_report"}
])

result = await workflow.execute(input_data)
```

### 2. Branching Workflow

```
         → Path A →
Input →             → Merge → Output
         → Path B →
```

```python
from opensin.workflow import BranchingWorkflow

workflow = BranchingWorkflow(
    branches={
        "code": coding_workflow,
        "research": research_workflow,
        "writing": writing_workflow
    },
    router=router_agent
)

result = await workflow.execute(input)
```

### 3. Looping Workflow

```
Input → Process → Check → (if not done) → Process → ...
                              ↓ (done)
                            Output
```

```python
from opensin.workflow import LoopingWorkflow

workflow = LoopingWorkflow(
    agent=refinement_agent,
    condition=lambda x: x.quality < 0.9,
    max_iterations=10
)

result = await workflow.execute(draft)
```

### 4. Parallel Workflow

```
Input → [Task A] →
        [Task B] → Merge → Output
        [Task C] →
```

```python
from opensin.workflow import ParallelWorkflow

workflow = ParallelWorkflow([
    {"agent": "researcher_a", "task": "Research topic A"},
    {"agent": "researcher_b", "task": "Research topic B"},
    {"agent": "researcher_c", "task": "Research topic C"},
])

results = await workflow.execute()
```

## Workflow Visualization

```python
from opensin.workflow import WorkflowVisualizer

visualizer = WorkflowVisualizer()

# Generate diagram
diagram = await visualizer.generate(workflow, format="mermaid")
print(diagram)

# Export
await visualizer.export(workflow, format="png", path="workflow.png")
```

## Workflow Testing

```python
from opensin.workflow import WorkflowTester

tester = WorkflowTester(workflow)

# Test with sample data
results = await tester.test(sample_inputs)

print(f"Success rate: {results.success_rate}%")
print(f"Avg duration: {results.avg_duration}s")
print(f"Failed steps: {results.failed_steps}")
```

## Best Practices

1. **Start simple** — Begin with linear workflows
2. **Add complexity gradually** — Only add branches/loops when needed
3. **Test thoroughly** — Test each path independently
4. **Monitor execution** — Track workflow metrics
5. **Handle failures** — Define fallback paths
6. **Document workflows** — Keep diagrams up to date

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [Orchestration Patterns](/guide/agent-orchestration-patterns)
