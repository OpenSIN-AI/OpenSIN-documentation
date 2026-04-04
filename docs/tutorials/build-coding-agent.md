# Tutorial: Build a Coding Assistant Agent

Create an AI coding assistant that understands your codebase.

## What You'll Build

A coding agent that:
- Understands your codebase structure
- Answers code-related questions
- Generates code snippets
- Reviews pull requests
- Suggests improvements

## Step 1: Setup

```bash
mkdir coding-agent && cd coding-agent
opensin init
```

## Step 2: Index Your Codebase

```python
from opensin import CodebaseIndexer

indexer = CodebaseIndexer(
    root_path="./my-project",
    include=["*.py", "*.js", "*.ts", "*.md"],
    exclude=["node_modules", ".git", "__pycache__", "dist"]
)

await indexer.index()
print(f"Indexed {indexer.file_count} files")
```

## Step 3: Create the Coding Agent

```python
from opensin import Agent

coding_agent = Agent(
    name="coding-assistant",
    model="gpt-4",
    system_prompt="""You are an expert coding assistant.

Your capabilities:
- Answer questions about the codebase
- Generate code snippets
- Review code for bugs and improvements
- Explain complex code sections
- Suggest refactoring opportunities

Rules:
- Always reference actual file paths
- Provide complete, working code
- Explain your reasoning
- Suggest tests for new code""",
    tools=["codebase_search", "file_read", "file_write", "terminal"]
)
```

## Step 4: Connect to VSCode

```python
# The agent can now answer questions about your codebase
response = await coding_agent.send(
    "How does authentication work in this project?"
)

# Generate code
response = await coding_agent.send(
    "Create a function to validate email addresses"
)

# Review code
response = await coding_agent.send(
    "Review this code for bugs:\n" + code_snippet
)
```

## Step 5: Add PR Review

```python
from opensin.integrations import GitHub

github = GitHub(app_id="...", private_key="...")

@github.on("pull_request.opened")
async def review_pr(event):
    diff = await github.get_pr_diff(event.pr_number)
    review = await coding_agent.send(f"Review this PR:\n{diff}")
    await github.post_review(event.pr_number, review.content)
```

## Next Steps

- [Plugin Development](/guide/plugin-development)
- [GitHub Integration](/integrations/github)
