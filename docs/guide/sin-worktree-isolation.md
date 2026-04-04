# SIN Worktree Isolation — Safe Parallel Agent Execution

> **OpenSIN's Worktree System** — Geklont aus Claude Code's AgentTool.tsx. Isolierte git Worktrees für sichere parallele Agenten.

## Architektur

```
Main Repo (main branch)
├── Worktree 1 (feature-a) → Agent 1 arbeitet isoliert
├── Worktree 2 (feature-b) → Agent 2 arbeitet isoliert
└── Worktree 3 (feature-c) → Agent 3 arbeitet isoliert
```

## Worktree erstellen

```python
from opensin.worktree import WorktreeManager

wtm = WorktreeManager(repo_path="/path/to/repo")

# Erstelle isolierten Worktree
worktree = await wtm.create(
    branch="feature-branch",
    path="/tmp/worktree-abc123",
    sparse_checkout=False  # Optional: nur bestimmte Pfade
)

# Agent im Worktree ausführen
agent = Agent(name="isolated-agent", cwd=worktree.path)
result = await agent.execute(task)

# Auto-Commit und Cleanup
if worktree.has_changes:
    commit = await worktree.commit("Agent: implemented feature")
    print(f"Changes committed: {commit.hash}")
else:
    await worktree.cleanup()  # Keine Änderungen → Worktree löschen
```

## Worktree Main Repo Path Resolution

```python
# Erkennt git Worktrees beim Init
# Und erlaubt Schreibzugriff auf Main Repo's .git Verzeichnis
# Für index.lock Operationen

class WorktreeDetector:
    def detect(self, path: str) -> Optional[WorktreeInfo]:
        if self.is_worktree(path):
            main_git_dir = self.resolve_main_repo_git_dir(path)
            return WorktreeInfo(
                worktree_path=path,
                main_git_dir=main_git_dir,
                allowed_paths=[main_git_dir, path]
            )
```

## Sparse Checkout für große Monorepos

```python
# Nur bestimmte Pfade im Worktree checkouten
# Spart Speicher und Zeit bei großen Repos

worktree = await wtm.create(
    branch="sparse-feature",
    path="/tmp/sparse-worktree",
    sparse_checkout=True,
    sparse_paths=["src/api/**", "tests/api/**"]
)
```

## Worktree Lifecycle

```python
# 1. Erstellen
worktree = await wtm.create(branch="feature", path="/tmp/wt")

# 2. Agent arbeitet
agent = Agent(cwd=worktree.path)
result = await agent.execute(task)

# 3. Änderungen prüfen
if worktree.has_changes:
    # 4a. Commit erstellen
    commit = await worktree.commit("Agent changes")
    
    # 5a. Optional: PR erstellen
    pr = await worktree.create_pr(title="Agent: implemented feature")
else:
    # 4b. Cleanup wenn keine Änderungen
    await worktree.cleanup()
```

## Best Practices

1. **Isolation** — Jeder Agent in eigenem Worktree
2. **Auto-Commit** — Änderungen automatisch committen
3. **Auto-Cleanup** — Worktrees ohne Änderungen löschen
4. **Sparse Checkout** — Nur nötige Pfade für große Repos
5. **Main Repo Resolution** — .git Zugriff für index.lock

## Next Steps

- [SIN Fork Subagent](/guide/sin-fork-subagent)
- [SIN Subagents](/guide/sin-subagents)
