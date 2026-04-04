# Phase 3: Advanced Capabilities

Phase 3 adds inline code completions, AI-powered code actions, and the Agent Marketplace.

## 3.1 Inline Chat / Completions

AI-powered ghost-text code completions triggered at the cursor position.

### Trigger Methods

| Method | Shortcut | Context |
|--------|----------|---------|
| Keyboard | `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Win/Linux) | Editor text focus |
| Auto | Registered as `InlineCompletionItemProvider` | All file patterns (`**`) |

### How It Works

1. Captures the code prefix from start of file to cursor position
2. Sends to AI with instruction: "Complete the code at cursor position. Return ONLY the completion (max 5 lines)"
3. Displays the suggestion as ghost text inline completion
4. Falls back gracefully on errors (returns null)

### Implementation

```typescript
// inlineChat.ts
class InlineChatProvider implements vscode.InlineCompletionItemProvider {
    bridge = new SinCodeBridge();

    async provideInlineCompletionItems(document, position, _context, _token) {
        const prefix = document.getText(
            new vscode.Range(new vscode.Position(0, 0), position)
        );
        try {
            let suggestion = '';
            await this.bridge.call(
                `Complete the code at cursor position. Return ONLY the completion (max 5 lines):\n\n${prefix}`,
                'code',
                (chunk) => { suggestion += chunk; }
            );
            const trimmed = suggestion.trim();
            if (!trimmed) return null;
            return [new vscode.InlineCompletionItem(trimmed)];
        } catch {
            return null; // Graceful fallback
        }
    }
}
```

### Registration

```typescript
context.subscriptions.push(
    vscode.languages.registerInlineCompletionItemProvider(
        { pattern: '**' },
        inlineController
    )
);
```

## 3.2 AI Code Actions

Context-aware code actions available via the lightbulb (💡) menu and command palette.

### Available Actions

| Action | Kind | Trigger | Mode | Command ID |
|--------|------|---------|------|------------|
| 🔮 **Fix error** | QuickFix | On diagnostic errors | Debug | `sincode.fixError` |
| 🤖 **Refactor selection** | Refactor | Always available | Code | `sincode.refactorSelection` |
| 📖 **Explain code** | Refactor | Always available | Ask | `sincode.explainCode` |
| ✅ **Generate tests** | Refactor | Always available | Code | `sincode.generateTests` |

### Fix Error

**Trigger:** Appears when a diagnostic error is present at the cursor.

**Flow:**
1. Reads the diagnostic message and selected code
2. Sends to AI in Debug mode: "Fix this error in the code below..."
3. Returns only the fixed code (no explanation)
4. Applies as a workspace edit replacing the selected range

**Prompt Template:**
```
Fix this error in the code below:

Error: <diagnostic.message>

Code:
<selectedCode>

Return ONLY the fixed code, no explanation:
```

### Refactor Selection

**Trigger:** Always available on any selected code.

**Flow:**
1. Sends selected code to AI in Code mode
2. Requests cleaner, more maintainable code following best practices
3. Applies the refactored code as a workspace edit

**Prompt Template:**
```
Refactor this code to be cleaner, more maintainable, and follow best practices:

<selectedCode>

Return ONLY the refactored code, no explanation:
```

### Explain Code

**Trigger:** Always available on any selected code.

**Flow:**
1. Sends selected code to AI in Ask mode
2. Opens a side panel webview with the explanation
3. Renders with basic HTML formatting

**Prompt Template:**
```
Explain what this code does in simple terms:

<selectedCode>
```

### Generate Tests

**Trigger:** Always available on any selected code.

**Flow:**
1. Sends selected code to AI in Code mode
2. Generates unit tests
3. Creates a new `.test.` file alongside the original
4. Opens the test file in the editor

**Prompt Template:**
```
Generate unit tests for this code:

<selectedCode>

Return ONLY the test code, no explanation:
```

**File Naming:** `original.ts` → `original.test.ts`

## 3.3 Agent Marketplace

A built-in webview panel for discovering and installing specialized SIN agents.

### Opening the Marketplace

| Method | Shortcut |
|--------|----------|
| Keyboard | `Cmd+Shift+M` (Mac) / `Ctrl+Shift+M` (Win/Linux) |
| Command Palette | `SIN Code: Open SIN Agent Marketplace` |
| Sidebar Chat | Click "Open Marketplace" button |

### Available Agents

| Agent | Category | Icon | Version | Commands |
|-------|----------|------|---------|----------|
| **SIN-Explorer** | Analysis | 🔍 | 1.0.0 | `explore.codebase`, `explore.patterns` |
| **SIN-Librarian** | Research | 📚 | 1.0.0 | `librarian.search`, `librarian.docs` |
| **SIN-Oracle** | Intelligence | 🔮 | 1.0.0 | `oracle.architect`, `oracle.debug` |
| **SIN-Artistry** | Creative | 🎨 | 1.0.0 | `artistry.solve`, `artistry.design` |
| **SIN-Frontend** | Development | 🎭 | 1.0.0 | `frontend.design`, `frontend.react` |
| **SIN-Vision-Colab** | Vision | 👁️ | 1.0.0 | `vision.record`, `vision.analyze` |

### UI Layout

```
┌──────────────────────────────────────────────────────────┐
│ 🤖 SIN Agent Marketplace          [3 / 6 installed]      │
├──────────────────────────────────────────────────────────┤
│ [Analysis] [Research] [Intelligence] [Creative] [Dev]... │
├──────────────────────────────────────────────────────────┤
│ ┌─────────────────┐  ┌─────────────────┐                 │
│ │ 🔍 SIN-Explorer │  │ 📚 SIN-Librarian│                 │
│ │ v1.0.0          │  │ v1.0.0          │                 │
│ │ [Analysis]      │  │ [Research]      │                 │
│ │ Codebase analy..│  │ Documentation.. │                 │
│ │ [✓ Installed]   │  │ [Install]       │                 │
│ │ [Remove]        │  │                 │                 │
│ └─────────────────┘  └─────────────────┘                 │
│ ┌─────────────────┐  ┌─────────────────┐                 │
│ │ 🔮 SIN-Oracle   │  │ 🎨 SIN-Artistry │                 │
│ │ v1.0.0          │  │ v1.0.0          │                 │
│ │ [Intelligence]  │  │ [Creative]      │                 │
│ │ Architecture... │  │ Creative prob.. │                 │
│ │ [Install]       │  │ [Install]       │                 │
│ └─────────────────┘  └─────────────────┘                 │
└──────────────────────────────────────────────────────────┘
```

### Features

- **Category filtering** — Toggle buttons filter agents by category
- **Install/Remove** — One-click install and remove with status tracking
- **Installed count badge** — Shows `X / Y installed` in header
- **Version display** — Each agent shows its version number
- **Responsive grid layout** — Adapts to panel width using CSS Grid
- **VS Code theme colors** — Uses native CSS variables for seamless integration

### Installation Behavior

Currently, installation is tracked in-memory within the session:
```typescript
case 'install':
    const agent = this.agents.find(a => a.id === message.agentId);
    if (agent) {
        agent.installed = true;
        vscode.window.showInformationMessage(`📦 Installed ${agent.name}!`);
        this.panel.webview.html = this.getHtml(); // Re-render
    }
```

**Note:** Future versions will persist installation state and integrate with the actual agent provisioning system.
