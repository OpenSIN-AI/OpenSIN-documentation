---
name: nvidia-3d-forge
description: Build production-grade 3D assets as an image-to-3D or text-to-3D pipeline with OpenUSD/USDZ outputs, topology and PBR quality gates, and validation handoff.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/nvidia-3d-forge` and mirrored for OpenCode CLI usage.

# NVIDIA 3D Forge

Generate reproducible 3D assets through hosted NVIDIA NIM APIs, then gate outputs with deterministic similarity and mesh-quality checks.

## Quick Start

```bash
python3 "$HOME/.config/opencode/skills/nvidia-3d-forge/scripts/forge_3d_asset.py" \
  --prompt "futuristic round mascot with dark face panel, cyan eyes, thin limbs" \
  --reference-image /absolute/path/reference.png \
  --quality-preset cinema \
  --best-of 6 \
  --max-rounds 2 \
  --out-dir /absolute/path/output/nvidia-3d-forge
```

## Core Workflow

1. Ingest prompt and optional reference image.
2. Derive a compact TRELLIS-safe prompt from the reference image (`reference_prompt_openai_compat.py`).
3. Generate multiple hosted TRELLIS candidates with deterministic seed/CFG-step sweeps.
4. Render probe images (`usdrecord`) and compute similarity (`similarity_rank.py`).
5. Rank candidates by weighted quality score and select best output.
6. Export run artifacts:
   - `manifest.json`
   - `asset.glb` (or `asset.stl`)
   - `preview_3d.html`
   - `open_preview_3d.sh`
   - `open_preview_3d_chrome_clean.sh`

## Hosted Contract Rules

- Hosted endpoint: `https://ai.api.nvidia.com/v1/genai/microsoft/trellis`
- API key env: `NVIDIA_API_KEY`
- Prompt max length: 77 chars (TRELLIS request schema)
- `mode=image` caveat on hosted preview endpoint:
  - accepts documented `data:image/png;example_id,{0..3}` tokens
  - raw user image data URLs may return `422`
- Skill behavior for `--input-mode auto` with a user reference image:
  - auto-switches to text mode and uses reference-driven prompt adaptation

See exact contract notes in `references/contracts.md`.

## Presets

- `fast`: lowest latency, fewer candidates
- `balanced`: moderate search and quality
- `cinema`: strongest candidate sweep for fidelity

## Validation and Quality Gates

- Geometry gate (optional `trimesh`): faces/vertices/extents/flatness
- Visual gate: deterministic similarity rank (dhash + edge + histogram)
- Optional multimodal visual grader: `vision_similarity_openai_compat.py`

## Artifacts and Reproducibility

Each run writes a full decision trace to `manifest.json` including:

- prompt adaptation details
- per-candidate payload summary
- per-candidate quality metrics
- selected candidate rationale

## Resource Map

- `scripts/forge_3d_asset.py`: main hosted pipeline orchestrator
- `scripts/reference_prompt_openai_compat.py`: reference image -> compact TRELLIS prompt
- `scripts/similarity_rank.py`: deterministic visual similarity score
- `scripts/vision_similarity_openai_compat.py`: optional multimodal + local hybrid scorer
- `references/contracts.md`: verified API contract notes and constraints
