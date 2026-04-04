# SIN Shell Utilities — Shell Command Helpers

> **OpenSIN's Shell Utilities** — Geklont aus Claude Code's Shell.ts. Shell-Command-Hilfsfunktionen.

## Implementation

```python
from opensin.shell import Shell

shell = Shell(
    cwd="/path/to/project",
    timeout=30,
    max_output_size=10000
)

# Execute command
result = await shell.execute("git status")
print(result.stdout)
print(result.stderr)
print(result.exit_code)
```

## CWD Management

```python
from opensin.shell import setCwd, getCwd

# Set working directory
setCwd("/new/path")

# Get current working directory
cwd = getCwd()
```

## Output Handling

```python
# Truncate large output
if len(result.stdout) > max_output_size:
    result.stdout = result.stdout[:max_output_size] + "\n... [truncated]"
```

## Best Practices

1. **Set timeout** — Immer Timeout setzen
2. **Limit output** — Große Outputs abschneiden
3. **Track cwd** — Working directory tracken
4. **Handle errors** — Exit codes prüfen
5. **Sanitize input** — Command-Input validieren

## Next Steps

- [SIN Tool System](/guide/sin-tool-system)
- [SIN Sandbox](/guide/sin-sandbox)
