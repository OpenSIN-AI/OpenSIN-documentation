# Contributing Guide

## Getting Started

### Repository Location

The SIN Code VS Code Extension source lives in the `kairos-vscode/` directory of the [OpenSIN-AI/OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) repository.

```bash
git clone git@github.com:OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code/kairos-vscode
```

### Development Setup

```bash
# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch mode (auto-recompile on changes)
npm run watch

# Package for distribution
npm run package
```

### Running the Extension

**Option 1: Debug Launch (F5)**
1. Open the `kairos-vscode/` folder in VS Code
2. Press `F5` to launch the Extension Host
3. A new VS Code window opens with the extension loaded

**Option 2: Command Line**
```bash
code --extensionDevelopmentPath=$PWD
```

## Project Structure

```
kairos-vscode/
├── src/                    # TypeScript source files
│   ├── extension.ts        # Main entry point
│   ├── cliBridge.ts        # CLI communication layer
│   ├── modes.ts            # Agent mode definitions
│   ├── lspProvider.ts      # LSP diagnostics & symbols
│   ├── swarmCoordinator.ts # Multi-agent dispatch
│   ├── buddyGamification.ts# Gamification system
│   ├── memoryConsolidation.ts # Memory file watcher
│   ├── inlineChat.ts       # Inline completions
│   ├── codeActions.ts      # Code actions provider
│   └── agentMarketplace.ts # Marketplace webview
├── out/                    # Compiled JavaScript (gitignored)
├── media/                  # Static assets (icons, images)
├── package.json            # Extension manifest
├── tsconfig.json           # TypeScript config
└── CHANGELOG.md            # Version history
```

## Coding Standards

### TypeScript

- **Target:** ES2020
- **Module:** CommonJS (VS Code extension standard)
- **Strict mode:** Enabled
- **No external runtime dependencies** — Only `vscode` and `child_process`

### Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Classes | PascalCase | `SinCodeBridge`, `BuddySystem` |
| Functions | camelCase | `buildFullPrompt`, `dispatchTask` |
| Constants | UPPER_SNAKE_CASE | `AGENT_MODES`, `AVAILABLE_AGENTS` |
| Files | camelCase | `cliBridge.ts`, `modes.ts` |
| Commands | dot.case | `sincode.start`, `sincode.selectMode` |

### Code Style

- **No runtime dependencies** — The extension must work with zero npm packages at runtime
- **Graceful degradation** — All external CLI calls (opencode, simone-mcp) must have fallback behavior
- **Error handling** — Catch and display errors in the UI, never crash silently
- **Type safety** — Use TypeScript types for all interfaces

## Adding a New Feature

### 1. Define the Module

Create a new file in `src/`:
```typescript
// src/myFeature.ts
import * as vscode from 'vscode';

export class MyFeature {
    // Implementation
}
```

### 2. Register in extension.ts

```typescript
import { MyFeature } from './myFeature';

function activate(context: vscode.ExtensionContext) {
    const myFeature = new MyFeature();
    context.subscriptions.push(myFeature);

    context.subscriptions.push(
        vscode.commands.registerCommand('sincode.myFeature', () => {
            myFeature.doSomething();
        })
    );
}
```

### 3. Add Command to package.json

```json
"contributes": {
    "commands": [
        {
            "command": "sincode.myFeature",
            "title": "SIN Code: My Feature",
            "category": "SIN Code"
        }
    ]
}
```

### 4. Add Keybinding (Optional)

```json
"contributes": {
    "keybindings": [
        {
            "key": "ctrl+shift+x",
            "mac": "cmd+shift+x",
            "command": "sincode.myFeature",
            "when": "editorTextFocus"
        }
    ]
}
```

## Adding a New Agent Mode

Edit `src/modes.ts`:

```typescript
export const AGENT_MODES = [
    // ... existing modes
    {
        id: 'review',
        name: 'Review',
        description: 'Code review and quality assessment',
        systemPrompt: 'You are SIN Code in Review Mode. Focus on code quality, security, and best practices.',
        icon: '🔍'
    }
];
```

## Adding a New Swarm Agent

Edit `src/swarmCoordinator.ts`:

```typescript
export const AVAILABLE_AGENTS = [
    // ... existing agents
    {
        id: 'reviewer',
        name: 'Reviewer',
        description: 'Automated code review and quality assessment',
        icon: '🔍'
    }
];
```

## Adding a Marketplace Agent

Edit `src/agentMarketplace.ts`:

```typescript
const DEFAULT_AGENTS = [
    // ... existing agents
    {
        id: 'sin-reviewer',
        name: 'SIN-Reviewer',
        description: 'Automated code review and quality assessment',
        category: 'Analysis',
        icon: '🔍',
        version: '1.0.0',
        installed: false,
        commands: ['review.code', 'review.security']
    }
];
```

## Testing

### Manual Testing Checklist

- [ ] Extension activates without errors
- [ ] Sidebar chat opens and displays
- [ ] Mode switching works (all 5 modes)
- [ ] Model selector shows available models
- [ ] Chat sends prompts and receives streaming responses
- [ ] Cancel button stops running generation
- [ ] File context management works
- [ ] Swarm dispatch works for all 4 agents
- [ ] BUDDY status bar shows correct XP/level
- [ ] Git commit detection triggers XP reward
- [ ] Inline completions work (Cmd+Shift+I)
- [ ] Code actions appear in lightbulb menu
- [ ] Agent Marketplace opens and displays agents
- [ ] Memory files are loaded and watched

### Build Verification

```bash
npm run compile    # Should complete without errors
npm run package    # Should produce .vsix file
code --install-extension sincode-vscode-0.1.0.vsix  # Should install cleanly
```

## Pull Request Workflow

1. **Create a branch** from `main`
2. **Make changes** following the coding standards
3. **Compile and test** locally
4. **Update CHANGELOG.md** with your changes
5. **Submit PR** to `OpenSIN-AI/OpenSIN-Code`
6. **Address review feedback**

### Commit Message Format

```
feat(vscode): add inline chat completions
fix(vscode): handle missing opencode CLI gracefully
docs(vscode): update architecture diagram
chore(vscode): bump version to 0.2.0
```

## Release Process

1. Update `version` in `package.json`
2. Update `CHANGELOG.md` with new version entry
3. Run `npm run compile`
4. Run `npm run package`
5. Test the `.vsix` file
6. Publish to VS Code Marketplace
