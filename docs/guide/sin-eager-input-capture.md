# SIN Eager Input Capture — Zero-Loss Startup

> **OpenSIN's Eager Input** — Geklont aus Claude Code. Captured Keystrokes bevor die TUI rendert.

## Das Problem

Während des Startup (1-2 Sekunden) gehen Keystrokes verloren weil die TUI noch nicht ready ist.

## Die Lösung: Eager Input Capture

```python
from opensin.ui import EagerInputCapture

capture = EagerInputCapture()

# Startet sofort — noch vor TUI Render
capture.start()

# ... TUI rendert ...

# Alle Keystrokes die während Startup eingegeben wurden
# sind jetzt verfügbar
pending_input = capture.drain()
await tui.process_input(pending_input)
```

## Implementation

```python
class EagerInputCapture:
    def __init__(self):
        self._buffer = []
        self._active = False
    
    def start(self):
        """Startet Input Capture — noch vor TUI."""
        self._active = True
        # Platform-spezifischer raw input capture
        self._setup_raw_input()
    
    def _setup_raw_input(self):
        """Setup raw input capture."""
        import sys
        import tty
        import termios
        
        # Save terminal settings
        self._old_settings = termios.tcgetattr(sys.stdin)
        # Set raw mode
        tty.setraw(sys.stdin.fileno())
        # Start reading
        asyncio.create_task(self._read_input())
    
    async def _read_input(self):
        """Liest Input im Hintergrund."""
        while self._active:
            char = await asyncio.get_event_loop().run_in_executor(
                None, sys.stdin.read, 1
            )
            self._buffer.append(char)
    
    def drain(self) -> str:
        """Gibt alle gecaptured Keystrokes zurück."""
        input_str = ''.join(self._buffer)
        self._buffer.clear()
        return input_str
    
    def stop(self):
        """Stoppt Input Capture."""
        self._active = False
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._old_settings)
```

## Performance Impact

| Scenario | Lost Keystrokes | User Experience |
|----------|----------------|-----------------|
| Ohne Capture | 3-5 | Frustrating |
| Mit Capture | 0 | Seamless |

## Best Practices

1. **Start early** — Vor allem anderen starten
2. **Drain after TUI** — Nach TUI Render auslesen
3. **Platform-specific** — Raw input pro Platform
4. **Clean shutdown** — Terminal Settings restoren

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN Scroll Drain](/guide/sin-scroll-drain)
