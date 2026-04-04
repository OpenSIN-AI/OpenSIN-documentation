# Troubleshooting Guide

## Common Issues

### Extension Not Loading

**Symptom:** SIN Code icon doesn't appear in the activity bar.

**Diagnosis:**
1. Open VS Code → Help → Toggle Developer Tools → Console
2. Look for `SIN Code VS Code extension is now active!`

**Solutions:**
- Restart VS Code completely
- Check if extension is disabled: Extensions view → search "SIN Code" → Enable
- Verify VS Code version >= 1.85.0: `code --version`

---

### "opencode: command not found"

**Symptom:** Chat shows error: `spawn opencode ENOENT`

**Diagnosis:**
```bash
which opencode
# If nothing returns, opencode is not in PATH
```

**Solutions:**
1. Install opencode CLI following the OpenSIN setup guide
2. Ensure opencode is in your PATH:
   ```bash
   echo $PATH
   # Should include the directory containing opencode
   ```
3. For macOS, if using a shell manager (nvm, fnm), ensure the shell profile is loaded
4. Restart VS Code after installing opencode

---

### No Models Available

**Symptom:** Model selector shows empty list or only fallback models.

**Diagnosis:**
```bash
opencode config list-models --format json
# Should return a JSON array of model IDs
```

**Solutions:**
1. Verify `~/.config/opencode/opencode.json` exists and is valid JSON
2. Check that providers are configured correctly
3. The extension falls back to these models if discovery fails:
   - `opencode/qwen3.6-plus-free`
   - `google/antigravity-gemini-3.1-pro`
   - `google/antigravity-claude-sonnet-4-6`

---

### Streaming Responses Not Working

**Symptom:** Chat sends prompt but no response appears, or response appears all at once.

**Diagnosis:**
1. Check the VS Code Developer Tools Console for errors
2. Verify opencode CLI works manually:
   ```bash
   opencode run "Hello" --format json
   ```

**Solutions:**
- Ensure opencode CLI supports `--format json` flag
- Check that the JSON output includes `{"type": "text", "part": {"text": "..."}}` events
- Verify no firewall is blocking the CLI process

---

### simone-mcp Symbol Extraction Fails

**Symptom:** LSP context shows no symbols, or `simone-mcp` errors in console.

**Diagnosis:**
```bash
simone-mcp symbols --file /path/to/file.ts --format json
# Should return JSON array of symbols
```

**Solutions:**
- This is **optional** — the extension works without simone-mcp
- Install simone-mcp if you want symbol extraction
- Check that simone-mcp is in your PATH

---

### BUDDY Not Showing in Status Bar

**Symptom:** No `🤖 Buddy Lv.1` in the right status bar.

**Solutions:**
1. Right-click the status bar → ensure "SIN Code" items are checked
2. Restart VS Code
3. Check that the extension activated successfully

---

### Inline Completions Not Working

**Symptom:** `Cmd+Shift+I` does nothing.

**Diagnosis:**
1. Verify the keybinding is registered: `Cmd+Shift+P` → "Preferences: Open Keyboard Shortcuts" → search "sincode"
2. Check that `editorTextFocus` context is active (cursor must be in editor)

**Solutions:**
- Ensure cursor is in an editor (not terminal, not sidebar)
- Check for keybinding conflicts with other extensions
- Verify opencode CLI is accessible

---

### Code Actions Not Appearing

**Symptom:** Lightbulb (💡) doesn't show SIN Code actions.

**Solutions:**
1. Select some text in the editor first
2. For "Fix Error" — there must be a diagnostic error at the cursor
3. Check that the extension is active
4. Try `Cmd+Shift+P` → `SIN Code: Fix Error` directly

---

### Memory Files Not Loading

**Symptom:** Memory context is empty in prompts.

**Diagnosis:**
1. Check that memory files exist in workspace root:
   ```bash
   ls AGENTS.md SIN-MEMORY.md CLAUDE.md .sincode-memory.md
   ```
2. Verify the workspace root is correctly detected

**Solutions:**
- Place memory files in the workspace root (first folder in workspace)
- Files are case-sensitive: `AGENTS.md` not `agents.md`
- Restart VS Code after adding memory files

---

### Auto Test Runner Not Triggering

**Symptom:** Saving a `.test.ts` file doesn't run tests.

**Solutions:**
1. Verify the file name contains `.test.` or `.spec.`
2. Check that `npm test` is configured in your `package.json`
3. Look for the "SIN Code Test Runner" terminal

---

### Agent Marketplace Not Opening

**Symptom:** `Cmd+Shift+M` does nothing.

**Solutions:**
1. Try Command Palette → `SIN Code: Open SIN Agent Marketplace`
2. Check for keybinding conflicts
3. Verify the extension is active

---

### Proactive Mode Not Analyzing

**Symptom:** Saving files doesn't trigger background analysis.

**Solutions:**
1. Ensure Proactive mode (⚡) is selected
2. Check the status bar mode indicator
3. Verify opencode CLI is accessible

---

## Debug Mode

### Enable Extension Logging

The extension logs to the VS Code Developer Tools Console:
1. `Cmd+Shift+P` → `Developer: Toggle Developer Tools`
2. Go to the Console tab
3. Look for `SIN Code` prefixed messages

### Check CLI Bridge Output

When a prompt is sent, the extension spawns `opencode run`. You can verify this manually:
```bash
opencode run "Test message" --format json --mode=code
```

### Check Process Status

If the extension seems stuck:
1. Check for hanging opencode processes:
   ```bash
   ps aux | grep opencode
   ```
2. Kill any stuck processes:
   ```bash
   killall opencode
   ```
3. The extension's cancel button sends SIGTERM to the active process

---

## Performance Tips

| Issue | Solution |
|-------|----------|
| Slow response streaming | Use a faster model (check `opencode config list-models`) |
| High memory usage | Close unused webview panels (Marketplace, Explain panels) |
| Slow activation | Ensure workspace has few memory files |
| Laggy inline completions | Inline completions spawn a new CLI process per trigger — use sparingly |

---

## Known Limitations

| Limitation | Status | Workaround |
|------------|--------|------------|
| Marketplace install is in-memory only | Known | State resets on VS Code restart |
| No persistent chat history | Known | Use memory files for context persistence |
| Single workspace support | Known | Only first workspace folder is used for memory scanning |
| No multi-file diff for code actions | Known | Code actions replace selection only |
| Buddy XP doesn't persist | Known | XP resets on VS Code restart |

---

## Getting Help

| Channel | Link |
|---------|------|
| **GitHub Issues** | [OpenSIN-AI/OpenSIN-Code/issues](https://github.com/OpenSIN-AI/OpenSIN-Code/issues) |
| **Marketplace Q&A** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=opensin.opensin-vscode) |
| **Documentation** | [OpenSIN Docs](https://github.com/OpenSIN-AI/Global-Dev-Docs-Standard) |

### Reporting a Bug

When reporting an issue, include:

1. **VS Code version:** `code --version`
2. **Extension version:** Check Extensions view → SIN Code → version number
3. **opencode version:** `opencode --version`
4. **Error messages:** From VS Code Developer Tools Console
5. **Steps to reproduce:** Exact steps to trigger the issue
6. **Expected vs actual behavior:** What you expected vs what happened
