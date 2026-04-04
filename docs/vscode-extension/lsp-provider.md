# API Reference: LSP Provider

## LspProvider

**File:** `src/lspProvider.ts` (compiled to `out/lspProvider.js`)

The `LspProvider` class bridges VS Code's diagnostic API and the `simone-mcp` CLI to extract semantic context from the current editor state.

### Class Definition

```typescript
class LspProvider {
    getCurrentDiagnostics(): DiagnosticInfo[];
    getSymbolsInFile(): Promise<SymbolInfo[]>;
    getSemanticContext(): Promise<string>;
}
```

### Types

#### DiagnosticInfo

```typescript
interface DiagnosticInfo {
    file: string;       // Full file path
    severity: 'error' | 'warning' | 'info';
    message: string;    // Diagnostic message
    line: number;       // 0-based line number
    character: number;  // 0-based character position
}
```

#### SymbolInfo

```typescript
interface SymbolInfo {
    name: string;   // Symbol name (function, class, variable)
    kind: string;   // LSP symbol kind
    file: string;   // Full file path
    line: number;   // 0-based line number
}
```

### Methods

#### `getCurrentDiagnostics()`

Extracts diagnostics from VS Code's diagnostic API for the active editor.

**Returns:** `DiagnosticInfo[]` — Array of diagnostic information.

**Implementation:**
```typescript
getCurrentDiagnostics() {
    const editor = vscode.window.activeTextEditor;
    if (!editor) return [];
    const diagnostics = vscode.languages.getDiagnostics(editor.document.uri);
    return diagnostics.map(d => ({
        file: editor.document.fileName,
        severity: d.severity === vscode.DiagnosticSeverity.Error ? 'error' :
                  d.severity === vscode.DiagnosticSeverity.Warning ? 'warning' : 'info',
        message: d.message,
        line: d.range.start.line,
        character: d.range.start.character
    }));
}
```

**Source:** Uses `vscode.languages.getDiagnostics(uri)` which aggregates diagnostics from all registered diagnostic providers (TypeScript language server, ESLint, etc.).

#### `getSymbolsInFile()`

Extracts symbols from the current file using the `simone-mcp` CLI.

**Returns:** `Promise<SymbolInfo[]>` — Array of symbol information.

**Spawned Command:**
```bash
simone-mcp symbols --file <path> --format json
```

**Error Handling:**
- Returns empty array `[]` on spawn error
- Returns empty array `[]` on JSON parse error
- Graceful degradation — the extension works without simone-mcp

#### `getSemanticContext()`

Combines all semantic information into a single context string.

**Returns:** `Promise<string>` — Formatted context string for inclusion in prompts.

**Output Format:**
```
**Current File:** /Users/jeremy/dev/project/src/index.ts
**Cursor Word:** processData

**Diagnostics (2):**
- [ERROR] Line 15: Cannot find name 'foo'
- [WARNING] Line 22: Unused variable 'bar'

**Symbols in File:** processData, DataHandler, Config, init
```

**Components:**
1. **Current File** — Always included (full path)
2. **Cursor Word** — Included if cursor is on a word
3. **Diagnostics** — Up to 5 most relevant, included if any exist
4. **Symbols** — Comma-separated list, included if any exist

### Integration with Prompt Building

The LSP context is injected into every prompt via `buildFullPrompt()`:

```typescript
const lspContext = await this.lspProvider.getSemanticContext();
if (lspContext) {
    context += `\n\n[LSP Context]\n${lspContext}\n`;
}
```

### Dependencies

| Dependency | Purpose | Required |
|------------|---------|----------|
| `vscode.languages` | Diagnostic API | Yes (built-in) |
| `simone-mcp` CLI | Symbol extraction | No (graceful fallback) |
