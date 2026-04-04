# Setup & Installation Guide

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **VS Code** | >= 1.85.0 | Required for WebviewView API |
| **opencode CLI** | Latest | Must be in PATH for all AI calls |
| **Node.js** | >= 18.x | Required for development/build |
| **simone-mcp** | Optional | For LSP symbol extraction |
| **TypeScript** | >= 5.3.3 | Dev dependency for compilation |

## Installation Methods

### Method 1: From VS Code Marketplace (Recommended)

1. Open VS Code
2. Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux) to open Extensions
3. Search for **"OpenSIN"** or **"SIN Code"**
4. Click **Install**

Or use the direct link: [marketplace.visualstudio.com/items?itemName=opensin.opensin-vscode](https://marketplace.visualstudio.com/items?itemName=opensin.opensin-vscode)

### Method 2: From .vsix Package

```bash
# Clone the repository
git clone git@github.com:OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code/kairos-vscode

# Install dependencies and compile
npm install
npm run compile

# Package the extension
npx vsce package --no-dependencies

# Install in VS Code
code --install-extension sincode-vscode-0.1.0.vsix
```

### Method 3: Development Mode (Side-loading)

```bash
# Clone the repository
git clone git@github.com:OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code/kairos-vscode

# Install dependencies
npm install

# Option A: Open in VS Code and press F5
code .
# Then press F5 to launch Extension Host

# Option B: Launch extension host directly
code --extensionDevelopmentPath=$PWD
```

## Post-Installation Verification

After installation, verify the extension is working:

1. **Check Activity Bar** — Look for the SIN Code icon in the left sidebar
2. **Open Sidebar** — Click the icon or run `Cmd+Shift+P` → `SIN Code: Start`
3. **Verify CLI Bridge** — Type a message in the chat and press Send
4. **Check Status Bar** — You should see:
   - Mode selector on the left: `$(symbol-misc) Code`
   - Model selector on the left: `$(symbol-constant) qwen3.6-plus`
   - BUDDY status on the right: `🤖 Buddy Lv.1`

## Configuration

### Global OpenCode Configuration

SIN Code uses the global OpenCode configuration at `~/.config/opencode/`. No extension-specific settings are required.

Available models are automatically fetched via:
```bash
opencode config list-models --format json
```

### Default Model

The extension defaults to `opencode/qwen3.6-plus-free`. Change it via:
- Status bar model selector (click to open Quick Pick)
- Command palette: `SIN Code: Select Model`

### Memory Files

Place any of these files in your workspace root for automatic context loading:

| File | Purpose |
|------|---------|
| `AGENTS.md` | Agent instructions and project conventions |
| `SIN-MEMORY.md` | Persistent session memory |
| `CLAUDE.md` | Compatibility with Claude Code projects |
| `.sincode-memory.md` | Hidden memory file |

## Troubleshooting Installation

| Issue | Solution |
|-------|----------|
| Extension not showing in sidebar | Restart VS Code after installation |
| "opencode: command not found" | Ensure `opencode` CLI is installed and in PATH |
| No models available | Run `opencode config list-models --format json` manually to verify |
| Webview not loading | Check VS Code version >= 1.85.0 |
| simone-mcp errors | Optional — extension works without it (graceful fallback) |
