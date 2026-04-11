# 🚀 Phase 2 Features: Collaboration, Test Generation & Visual Diff

Phase 2 adds developer workflow tooling that makes the rotator easier to evolve, review, and validate.

## 1. Live Collaboration (`src/live_collaboration.py`)

The collaboration module tracks shared editing sessions with revision history, conflict detection, and JSON persistence.

### Key Capabilities
- **Session Hub**: Manage multiple collaborative sessions at once.
- **Revision Tracking**: Every edit increments the session revision.
- **Conflict Detection**: Outdated edits are marked as conflicts.
- **History & Persistence**: Sessions can be saved to and loaded from JSON.

### Usage Example

```python
from src.live_collaboration import CollaborationHub, EditOperation

hub = CollaborationHub()
session = hub.create_session("docs", "alpha\nbeta\ngamma")
session.join("alice")
session.join("bob")

session.apply_edit(EditOperation("alice", 2, 2, "BETA", base_revision=0))
print(session.summary())
print(session.render_history())
```

---

## 2. Automated Test Generation (`src/testgen.py`)

The test generator scans Python source files and produces pytest smoke tests for public functions and classes.

### Key Capabilities
- **AST Discovery**: Finds public functions, classes, and methods.
- **Safe Sample Inputs**: Infers simple values from annotations and parameter names.
- **Pytest Output**: Generates runnable smoke tests.
- **Write Support**: Can write generated tests directly to disk.

### Usage Example

```python
from src.testgen import TestGenerator

generator = TestGenerator()
code = generator.generate_pytest("src/rotator.py")
print(code)
```

CLI:

```bash
python3 -m main generate-tests src/rotator.py -o tests/generated_rotator.py
```

---

## 3. Visual Diff Viewer (`src/visual_diff.py`)

The visual diff viewer renders side-by-side comparisons and unified diffs for rapid code review.

### Key Capabilities
- **Side-by-Side Diff**: Human-readable line comparison.
- **Unified Diff**: Standard patch-style output.
- **Impact Summary**: Reports churn and change ratio.
- **File or Text Input**: Works on strings or files.

### Usage Example

```python
from src.visual_diff import VisualDiffViewer

viewer = VisualDiffViewer()
report = viewer.compare_texts("alpha\nbeta", "alpha\nBETA")
print(viewer.render_side_by_side(report))
print(viewer.impact_summary(report))
```

CLI:

```bash
python3 -m main diff old.py new.py --mode side
```

---

## 🏗️ Phase 2 Architecture

```text
[ User / CLI ]
      |
      v
[ main.py ] --------------------------+
   |          |          |            |
   v          v          v            v
[ Collaboration ] [ TestGen ] [ Visual Diff ] [ Source Files ]
      |              |              |
      v              v              v
[ JSON Sessions ]  [ Pytest Code ] [ Review Output ]
```

## 🔧 Integration Guide

1. Use `TestGenerator` before committing changes to generate smoke tests from new modules.
2. Use `VisualDiffViewer` when comparing refactors or reviewing generated output.
3. Use `CollaborationHub` when multiple agents or editors need shared revision tracking.

---
**Branding**: OpenSIN / sincode
