# API Reference: Internal Modules

## SwarmCoordinator

**File:** `src/swarmCoordinator.ts`

### Class Definition

```typescript
class SwarmCoordinator {
    activeTasks: Map<string, Task>;

    dispatchTask(agentType: string, prompt: string): Promise<string>;
    dispatchSwarm(tasks: { agent: string; prompt: string }[]): Promise<Task[]>;
    getActiveTasks(): Task[];
    cancelTask(taskId: string): void;
}
```

### Task Interface

```typescript
interface Task {
    id: string;       // Unique ID: task_<timestamp>_<random>
    agent: string;    // Agent type: explore, librarian, oracle, artistry
    prompt: string;   // Task description
    status: 'running' | 'completed' | 'failed';
    result?: string;  // Output from the agent
}
```

### Available Agents

```typescript
const AVAILABLE_AGENTS = [
    { id: 'explore', name: 'Explore', description: 'Codebase patterns, file structures, ast-grep', icon: '🔍' },
    { id: 'librarian', name: 'Librarian', description: 'Remote repos, official docs, GitHub examples', icon: '📚' },
    { id: 'oracle', name: 'Oracle', description: 'Conventional problems (architecture, debugging, complex logic)', icon: '🔮' },
    { id: 'artistry', name: 'Artistry', description: 'Non-conventional problems (different approach needed)', icon: '🎨' }
];
```

### CLI Command Format

```bash
opencode run "Task: <prompt>\nAgent Type: <agentType>\nExecute this task and return the result." --format json --agent <agentType>
```

---

## BuddySystem

**File:** `src/buddyGamification.ts`

### Class Definition

```typescript
class BuddySystem {
    state: BuddyState;
    statusBarItem: StatusBarItem;

    onActionSuccess(action: string, xpGain?: number): void;
    onActionFailure(action: string): void;
    onCommit(): void;
    onTestPass(): void;
    onTestFail(): void;
    onError(error: string): void;
    checkLevelUp(): void;
    scheduleMoodDecay(): void;
    updateDisplay(): void;
    getState(): BuddyState;
    dispose(): void;
}
```

### BuddyState Interface

```typescript
interface BuddyState {
    mood: 'neutral' | 'happy' | 'excited' | 'sad' | 'sleeping';
    level: number;
    xp: number;
    lastAction: string;
    emoji: string;
}
```

### XP Reward Values

| Method | XP | Emoji |
|--------|-----|-------|
| `onCommit()` | +25 | 🚀 |
| `onActionSuccess(action, 20)` | +20 | ✅ |
| `onTestPass()` | +15 | ✅ |
| `onActionSuccess(action, 10)` | +10 | 😊 |
| `onActionSuccess(action, 5)` | +5 | 📎/🔍 |
| `onActionFailure()` | 0 | 😢 |
| `onError()` | 0 | 💥 |

### Level Formula

```typescript
const xpNeeded = state.level * 100;
if (state.xp >= xpNeeded) {
    state.level++;
    state.xp -= xpNeeded;
    // Show notification
}
```

---

## MemoryConsolidation

**File:** `src/memoryConsolidation.ts`

### Class Definition

```typescript
class MemoryConsolidation {
    workspaceRoot: string;
    memoryFiles: string[];

    constructor(workspaceRoot: string);
    scanForMemoryFiles(): void;
    getConsolidatedMemory(): Promise<string>;
    appendMemory(entry: string): Promise<void>;
    startWatching(): FileSystemWatcher;
}
```

### Memory File Patterns

```typescript
const patterns = ['AGENTS.md', 'SIN-MEMORY.md', 'CLAUDE.md', '.sincode-memory.md'];
```

### File Watcher Pattern

```typescript
const watcher = vscode.workspace.createFileSystemWatcher(
    new vscode.RelativePattern(this.workspaceRoot, '**/{AGENTS.md,SIN-MEMORY.md,CLAUDE.md}')
);
```

---

## InlineChatProvider

**File:** `src/inlineChat.ts`

### Class Definition

```typescript
class InlineChatProvider implements vscode.InlineCompletionItemProvider {
    bridge: SinCodeBridge;

    provideInlineCompletionItems(
        document: TextDocument,
        position: Position,
        context: InlineCompletionContext,
        token: CancellationToken
    ): Promise<InlineCompletionItem[] | null>;

    dispose(): void;
}
```

### Completion Prompt Template

```
Complete the code at cursor position. Return ONLY the completion (max 5 lines):

<code from start of file to cursor>
```

---

## SINCodeActionProvider

**File:** `src/codeActions.ts`

### Class Definition

```typescript
class SINCodeActionProvider implements vscode.CodeActionProvider {
    bridge: SinCodeBridge;
    static providedCodeActionKinds: CodeActionKind[];

    provideCodeActions(
        document: TextDocument,
        range: Range | Selection,
        context: CodeActionContext,
        token: CancellationToken
    ): CodeAction[];
}
```

### Provided Action Kinds

```typescript
static providedCodeActionKinds = [
    vscode.CodeActionKind.QuickFix,
    vscode.CodeActionKind.Refactor
];
```

### Standalone Command Functions

| Function | Mode | Purpose |
|----------|------|---------|
| `fixError(document, diagnostic, range)` | `debug` | Fix diagnostic error |
| `refactorSelection(document, range)` | `code` | Refactor selected code |
| `explainCode(document, range)` | `ask` | Explain code in side panel |
| `generateTests(document, range)` | `code` | Generate unit tests |

### applyEdit Helper

```typescript
async function applyEdit(document, range, newText) {
    const edit = new vscode.WorkspaceEdit();
    edit.replace(document.uri, range, newText);
    await vscode.workspace.applyEdit(edit);
    vscode.window.showInformationMessage('✅ SIN Code applied the changes!');
}
```

---

## MarketplacePanel

**File:** `src/agentMarketplace.ts`

### Class Definition

```typescript
class MarketplacePanel {
    panel: WebviewPanel | undefined;
    agents: AgentInfo[];

    show(): void;
    getHtml(): string;
    dispose(): void;
}
```

### AgentInfo Interface

```typescript
interface AgentInfo {
    id: string;
    name: string;
    description: string;
    category: 'Analysis' | 'Research' | 'Intelligence' | 'Creative' | 'Development' | 'Vision';
    icon: string;
    version: string;
    installed: boolean;
    commands: string[];
}
```

### Webview Message Protocol

| Command | Payload | Action |
|---------|---------|--------|
| `install` | `{ agentId: string }` | Mark agent as installed, re-render |
| `remove` | `{ agentId: string }` | Mark agent as uninstalled, re-render |
| `close` | `{}` | Dispose the panel |
