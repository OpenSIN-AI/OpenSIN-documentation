# Phase 2: Intelligence Layer

Phase 2 adds multi-agent orchestration, gamification, automated testing, and file context management.

## 2.1 Swarm Coordinator

Dispatch parallel tasks to specialized oh-my-opencode agents via the `opencode` CLI.

### Available Agents

| Agent | ID | Icon | Purpose |
|-------|-----|------|---------|
| **Explore** | `explore` | 🔍 | Codebase patterns, file structures, ast-grep analysis |
| **Librarian** | `librarian` | 📚 | Documentation research, GitHub examples, best-practice lookup |
| **Oracle** | `oracle` | 🔮 | Architecture guidance, debugging, complex logic solving |
| **Artistry** | `artistry` | 🎨 | Creative problem solving, non-conventional approaches |

### Dispatching a Single Task

1. Command palette: `SIN Code: Dispatch Agent`
2. Select an agent from the Quick Pick
3. Enter the task prompt
4. Progress notification shows dispatch status

### CLI Command Format

```bash
opencode run "Task: <prompt>\nAgent Type: <agentType>\nExecute this task and return the result." --format json --agent <agentType>
```

### Parallel Swarm Dispatch

The `dispatchSwarm()` method runs multiple agents simultaneously:

```typescript
const results = await Promise.allSettled([
  swarmCoordinator.dispatchTask('explore', 'Analyze codebase structure'),
  swarmCoordinator.dispatchTask('librarian', 'Find React best practices'),
  swarmCoordinator.dispatchTask('oracle', 'Review architecture'),
]);
```

### Task Tracking

Each task gets a unique ID and status:
```typescript
{
  id: "task_1712145600000_abc123def",
  agent: "explore",
  prompt: "Analyze codebase structure",
  status: "running" | "completed" | "failed",
  result?: string
}
```

### Buddy XP Reward

Successful swarm task completion earns **+20 XP**.

## 2.2 BUDDY Gamification System

A pet companion in your status bar that reacts to your coding activity.

### Status Bar Display

```
🤖 Buddy Lv.1
```

Click for detailed tooltip:
```
BUDDY Status:
Mood: happy
Level: 1
XP: 45
Last: Success: Response generated
```

### XP Reward Table

| Event | XP Gain | Emoji | Trigger |
|-------|---------|-------|---------|
| Commit pushed | +25 XP | 🚀 | `.git/HEAD` file change detected |
| Swarm task completed | +20 XP | ✅ | `dispatchTask()` resolves successfully |
| Response generated | +10 XP | 😊 | AI response completes |
| Tests passed | +15 XP | ✅ | Auto test runner succeeds |
| File added to context | +5 XP | 📎 | `addFileToContext()` called |
| Background analysis | +5 XP | 🔍 | Proactive mode analysis completes |
| Error/failure | 0 XP | 😢/💥 | Any operation fails |

### Leveling System

Each level requires `level × 100` XP:

| Level | XP Required | Cumulative XP |
|-------|-------------|---------------|
| 1 | 100 | 100 |
| 2 | 200 | 300 |
| 3 | 300 | 600 |
| 4 | 400 | 1000 |
| 5 | 500 | 1500 |

On level-up:
```
🎉 BUDDY leveled up to 2!
```

### Mood System

| Mood | Emoji | Trigger |
|------|-------|---------|
| `neutral` | 🤖 | Default state |
| `happy` | 😊 | Successful action |
| `excited` | 🎉 | Level up |
| `sad` | 😢 | Failed action |
| `sleeping` | 😴 | (Reserved for future idle mode) |

**Auto-decay:** Moods decay back to `neutral` after 30 seconds.

### Git Commit Detection

Watches `.git/HEAD` for changes using `FileSystemWatcher`:
```typescript
const gitWatcher = vscode.workspace.createFileSystemWatcher(
  new vscode.RelativePattern(workspaceRoot, '.git/HEAD')
);
gitWatcher.onDidChange(() => { buddySystem.onCommit(); });
```

## 2.3 Auto Test Runner

Automatically runs tests when test files are saved.

### Trigger

Fires on `onDidSaveTextDocument` when the saved file contains:
- `.test.` in the filename (e.g., `utils.test.ts`)
- `.spec.` in the filename (e.g., `utils.spec.ts`)

### Behavior

1. Creates a terminal named "SIN Code Test Runner"
2. Runs `cd <test-file-dir> && npm test || echo "TESTS_FAILED"`
3. Shows the terminal output

### Terminal Command

```bash
cd /path/to/project && npm test || echo "TESTS_FAILED"
```

## 2.4 File Context Management

Add any open file to the conversation context.

### Methods

- **Command Palette:** `SIN Code: Add File to Context`
- **Editor Context Menu:** Right-click → `Add File to SIN Code Context`

### Implementation

```typescript
// From extension.ts
context.subscriptions.push(vscode.commands.registerCommand('sincode.addFileToContext', async () => {
    const editor = vscode.window.activeTextEditor;
    if (editor) {
        provider.addFileToContext(editor.document.uri.fsPath);
        buddySystem.onActionSuccess('File added to context', 5);
        vscode.window.showInformationMessage(`Added ${editor.document.fileName} to SIN Code context`);
    }
}));
```

### Context Menu Integration

Registered in `package.json`:
```json
"menus": {
    "editor/context": [
        {
            "command": "sincode.addFileToContext",
            "group": "navigation"
        }
    ]
}
```
