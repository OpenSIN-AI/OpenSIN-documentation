# API Reference: CLI Bridge

## SinCodeBridge

**File:** `src/cliBridge.ts` (compiled to `out/cliBridge.js`)

The `SinCodeBridge` class is the mandatory communication layer between the VS Code extension and the `opencode` CLI. It implements the Priority -2.5 rule: all LLM calls MUST go through `opencode run --format json`.

### Class Definition

```typescript
class SinCodeBridge {
    activeProcess: ChildProcess | null;

    call(prompt: string, mode: string, onData: (chunk: string) => void): Promise<void>;
    cancel(): void;
    getAvailableModels(): Promise<string[]>;
}
```

### Methods

#### `call(prompt, mode, onData)`

Sends a prompt to the `opencode` CLI and streams the response.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | `string` | The full prompt (includes mode, context, memory, user input) |
| `mode` | `string` | Agent mode ID: `architect`, `code`, `debug`, `ask`, `proactive` |
| `onData` | `(chunk: string) => void` | Callback for each streamed text chunk |

**Returns:** `Promise<void>` — Resolves when the CLI process exits with code 0.

**Spawned Command:**
```bash
opencode run "<prompt>" --format json --mode=<mode>
```

The `--mode` flag is only added when mode is not `code` (the default).

**Stream Parsing:**
```typescript
process.stdout.on('data', (data) => {
    const lines = data.toString().split('\n');
    for (const line of lines) {
        if (!line.trim()) continue;
        try {
            const parsed = JSON.parse(line);
            if (parsed.type === 'text' && parsed.part?.text) {
                onData(parsed.part.text);
            }
        } catch (e) {
            // Ignore non-JSON lines
        }
    }
});
```

**Error Handling:**
- `stderr` is forwarded to `onData` with `[stderr]` prefix
- Non-zero exit code rejects with `Error: sin-code CLI exited with code ${code}`
- Spawn errors reject with the original error object

#### `cancel()`

Kills the currently active CLI process.

**Implementation:**
```typescript
cancel() {
    if (this.activeProcess) {
        this.activeProcess.kill('SIGTERM');
        this.activeProcess = null;
    }
}
```

**Usage:** Called when the user clicks the "Stop" button in the chat UI.

#### `getAvailableModels()`

Fetches available models from the `opencode` configuration.

**Returns:** `Promise<string[]>` — Array of model identifiers.

**Spawned Command:**
```bash
opencode config list-models --format json
```

**Fallback Models:**
If the command fails or returns invalid JSON, returns:
```typescript
['opencode/qwen3.6-plus-free', 'google/antigravity-gemini-3.1-pro', 'google/antigravity-claude-sonnet-4-6']
```

### JSON Event Format

The `opencode` CLI streams JSON events, one per line:

```json
{"type": "text", "part": {"text": "Hello, "}}
{"type": "text", "part": {"text": "I can help with that."}}
{"type": "thinking", "part": {"text": "Analyzing the code..."}}
```

The bridge only extracts `type: "text"` events. Other event types are silently ignored.

### Usage Examples

**Basic Chat Call:**
```typescript
const bridge = new SinCodeBridge();
let response = '';
await bridge.call(
    '[Mode: You are SIN Code in Code Mode...]\n\nUser: Write a hello world',
    'code',
    (chunk) => { response += chunk; }
);
console.log(response); // "Hello, world!"
```

**With Mode Flag:**
```typescript
await bridge.call(
    '[Mode: You are SIN Code in Debug Mode...]\n\nUser: Fix this error',
    'debug',
    (chunk) => { console.log(chunk); }
);
// Spawns: opencode run "..." --format json --mode=debug
```

**Cancellation:**
```typescript
// Start a call
const promise = bridge.call(longPrompt, 'code', onData);

// Cancel it
bridge.cancel();
// The promise will reject with an error
```
