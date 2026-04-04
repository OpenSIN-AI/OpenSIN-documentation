# SIN Bare Git Repo Escape Prevention — Sandbox Security

> **OpenSIN's Git Escape Prevention** — Geklont aus Claude Code's sandbox-adapter.ts. Verhindert dass planted git repos die Sandbox escapen.

## Die Bedrohung

Ein Agent könnte versuchen, ein bare git repo zu erstellen um die Sandbox zu escapen:

```bash
# Gefährlich: Erstellt git Struktur die Sandbox umgehen könnte
mkdir -p .git/objects .git/refs .git/hooks
echo "ref: refs/heads/main" > .git/HEAD
```

## Die Lösung: Bare Git Repo Prevention

```python
from opensin.sandbox import GitEscapePrevention

prevention = GitEscapePrevention()

# GIT Directory Files die überwacht werden
GIT_FILES = ["HEAD", "objects", "refs", "hooks", "config"]

class GitEscapePrevention:
    def check_write(self, path: str, content: bytes, file_exists: bool):
        """Prüft ob Schreiboperation ein git repo erstellen könnte."""
        if self.is_git_file(path):
            if file_exists:
                # Bestehende git Files dürfen nicht modifiziert werden
                raise SecurityError("Cannot modify existing git files")
            else:
                # Neue git Files werden post-command gescrubt
                self.mark_for_scrubbing(path)
    
    def is_git_file(self, path: str) -> bool:
        """Prüft ob Datei zu einer git Struktur gehört."""
        parts = Path(path).parts
        return ".git" in parts or any(
            p in GIT_FILES for p in parts
        )
    
    def scrub_git_files(self, paths: list[str]):
        """Scrubbt neu erstellte git Files nach Command-Ausführung."""
        for path in paths:
            if self.is_git_file(path) and not self.file_existed_before(path):
                os.remove(path)
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

## Best Practices

1. **Immer aktiviert** — Git Escape Prevention sollte immer an sein
2. **Worktree Detection** — Main Repo .git Zugriff für index.lock erlauben
3. **Post-Command Scrubbing** — Neue git Files nach Ausführung löschen
4. **Existing File Protection** — Bestehende git Files nie modifizieren

## Next Steps

- [SIN Sandbox](/guide/sin-sandbox)
- [Security Hardening](/guide/security-hardening)
