# Agent Prompt Engineering

Master the art of writing effective prompts for OpenSIN agents.

## Prompt Structure

```
[Role] + [Context] + [Task] + [Constraints] + [Output Format]
```

## Role Definition

```python
# Bad
system_prompt = "You are a helpful assistant."

# Good
system_prompt = """You are a senior software engineer with 15+ years of experience in Python, distributed systems, and cloud architecture.

Your expertise:
- Python best practices and design patterns
- Microservices architecture
- AWS/GCP cloud services
- Database optimization
- Security best practices"""
```

## Context Setting

```python
# Include relevant context
context = f"""Project: {project_name}
Tech Stack: {tech_stack}
Current Task: {current_task}
Recent Changes: {recent_commits}"""
```

## Task Specification

```python
# Specific and actionable
task = """Your task:
1. Review the code changes in the PR
2. Identify any bugs or security issues
3. Suggest improvements for performance
4. Check for adherence to project coding standards

Focus areas:
- Error handling
- Input validation
- Database queries
- API response formats"""
```

## Output Format

```python
# Structured output
output_format = """Respond in this format:

## Summary
Brief overview of findings

## Issues Found
1. [Severity] Issue description (file:line)
   - Fix: suggested fix

## Recommendations
1. Specific improvement suggestion

## Score
Overall code quality: X/10"""
```

## Advanced Techniques

### Few-Shot Prompting

```python
prompt = """Classify the sentiment of these reviews:

Review: "Great product, love it!"
Sentiment: Positive

Review: "Terrible experience, waste of money"
Sentiment: Negative

Review: "It's okay, nothing special"
Sentiment: Neutral

Review: "{user_review}"
Sentiment:"""
```

### Chain of Thought

```python
prompt = """Solve this step by step:

1. First, understand the problem
2. Identify the key components
3. Consider possible approaches
4. Choose the best approach
5. Implement the solution

Problem: {problem}"""
```

### Self-Correction

```python
prompt = """Write the solution, then review your own work:

## Solution
[your solution]

## Self-Review
- Are there any bugs?
- Is this efficient?
- Can this be improved?
- Are there edge cases?

## Improved Solution
[revised solution if needed]"""
```

## Prompt Testing

```python
from opensin import PromptTester

tester = PromptTester(agent)

# Test prompt variations
results = await tester.test_variations(
    base_prompt="Classify this text: {text}",
    variations=[
        "Classify the sentiment: {text}",
        "What is the sentiment of: {text}",
        "Analyze sentiment: {text}",
    ],
    test_data=test_texts
)

print(f"Best prompt: {results.best_prompt}")
print(f"Accuracy: {results.best_accuracy}%")
```

## Best Practices

1. **Be specific** — Vague prompts get vague results
2. **Include examples** — Show, don't just tell
3. **Define output format** — Specify exactly what you want
4. **Set constraints** — Limit scope and behavior
5. **Test variations** — A/B test different prompts
6. **Iterate** — Refine prompts based on results
7. **Version prompts** — Track prompt changes

## Next Steps

- [Agent Configuration](/guide/agent-configuration)
- [Agent Evaluation](/guide/agent-evaluation)
