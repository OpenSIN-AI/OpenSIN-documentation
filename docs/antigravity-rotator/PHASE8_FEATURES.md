# 🚀 Phase 8 Features: Cross-Repo Intelligence

> **Status:** Implemented in Sprint 4 (Issue #44)

Phase 8 enables the Antigravity Rotator to act across repository boundaries, bringing true multi-repo intelligence to the A2A fleet. 

## 1. Cross-Repo Analyzer (`src/cross_repo.py`)

Using the existing `WorkspaceManager`, the `CrossRepoAnalyzer` parses Python Abstract Syntax Trees (AST) across all registered local repositories.

### Key Capabilities

- **Global Dependency Graph**: Generates a directed graph of all module imports linking multiple workspaces together.
- **Function Usage Locator**: Accurately finds all usages of a specific function or class across repos, eliminating the false positives commonly seen with regular expressions.
- **Breaking Change Detection**: Identifies cross-repository impact when modifying function signatures, highlighting call sites that need refactoring before integration.

### Usage Examples

```python
from src.cross_repo import CrossRepoAnalyzer

analyzer = CrossRepoAnalyzer()

# 1. Build a dependency graph across workspaces
graph = analyzer.build_dependency_graph()
print(graph.nodes)
print(graph.edges)

# 2. Find function usages globally
usages = analyzer.find_usages("deploy_agent")
for usage in usages:
    print(f"[{usage.repo_name}] {usage.file_path}:{usage.line_number} -> {usage.context}")

# 3. Detect breaking changes
risks = analyzer.detect_breaking_changes(usages, new_param_count=2)
for risk in risks:
    print(f"Risk at {risk['file']}: {risk['risk']}")
```

---

## 2. CLI Commands

The multi-repo commands are available under the `cross-repo` subcommand:

```bash
# Build the global AST dependency graph
python3 -m main cross-repo analyze-deps

# Output the dependency graph in JSON format
python3 -m main cross-repo analyze-deps --json

# Find all cross-repo calls to a specific function
python3 -m main cross-repo find-usages "deploy_agent"

# Output the usages in JSON format
python3 -m main cross-repo find-usages "setup_logging" --json
```

---
**Branding**: OpenSIN / sincode
