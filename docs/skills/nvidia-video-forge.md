---
name: nvidia-video-forge
description: Create production-grade videos with hosted NVIDIA NIM/Cosmos APIs using a deterministic generation pipeline, multisource ingestion, chat-bridge judging, and strict QA gating.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/nvidia-video-forge` and mirrored for OpenCode CLI usage.

# NVIDIA Video Forge

Build videos as a reproducible pipeline with explicit run state, bridge artifacts, and resumable iterations.

## Pipeline Standard

1. Ingest all provided sources into `asset_graph.json` (image/video/audio/url/youtube/blog/product/person/overlay).
   - For YouTube, fetch metadata via Google API (service account / API key fallback) and extract source visual evidence (video + keyframes) when enabled.
2. Derive brand profile (`brand_profile.json`) and optional ASR storyboard (`asr_plan.json`).
3. Build prompt plan from user prompt + source context + brand constraints.
4. Generate multiple hosted NVIDIA candidates.
5. Judge candidates:
   - Default: `chat_bridge` (same chat session; no `codex exec`).
   - Optional: `nvidia_qa`, `openai_api`, `dual`.
6. Iterate until pass or budget reached (`--judge-max-iterations`, `--judge-max-minutes`).
7. Apply optional voice stage and overlay stage.
8. Export run artifacts (`manifest.json`, QA files, bridge files, final/rejected video, dashboard).

## Quick Start

Generate in default chat-bridge mode:

```bash
python3 scripts/video_forge.py generate \
  --prompt "Branded product reel with smooth camera motion" \
  --input-product-image /absolute/path/product.png \
  --input-person-image /absolute/path/person.jpg \
  --input-url https://example.com \
  --overlay-template world_news \
  --hosted \
  --api-key-env NVIDIA_API_KEY
```

Resume after judge response in same run:

```bash
python3 scripts/video_forge.py resume \
  --run-dir /absolute/path/output/nvidia-video-forge/<run-id> \
  --judge-response /absolute/path/judge_response.json
```

Debug ingestion only:

```bash
python3 scripts/video_forge.py ingest \
  --input-url https://example.com \
  --input-blog-url https://example.com/blog/post \
  --input-youtube-url https://www.youtube.com/watch?v=... \
  --out-dir /absolute/path/ingest-preview
```

## Execution Rules

- Hosted NVIDIA generation is mandatory (`--hosted`).
- Default judge is `chat_bridge`; this path writes bridge artifacts and exits with code `3` while waiting for `resume`.
- `chat_bridge` does not execute external judge tasks by itself.
- For YouTube visual judging, configure Google auth (`--google-service-account-json` and/or `GOOGLE_API_KEY`) and keep `--youtube-include-source-media` enabled (default).
- Keep contract fallback and endpoint profile fallback enabled unless strict debugging is needed.
- For NVCF exec routes, provide reference media or use text-capable routes.
- Preserve all run artifacts for reproducibility.

## Run State Machine

- `running`: candidate generation and QA loop in progress.
- `awaiting_judge`: bridge package emitted; run must be resumed with judge JSON.
- `completed`: final output accepted and written.
- `failed`: budget exhausted or all candidates rejected.

## Resource Map

- `scripts/video_forge.py`: main CLI orchestrator (`generate`, `resume`, `ingest`, `qa`, `voice`, `probe`).
- `scripts/source_adapters.py`: multisource normalization and crawling.
- `scripts/brand_profile.py`: brand extraction heuristics.
- `scripts/asr_pipeline.py`: audio timeline/storyboard planning.
- `scripts/overlay_engine.py`: FFmpeg overlay templates + file overlays.
- `scripts/video_judge_chat_bridge.py`: bridge request/schema/template generation + response normalization.
- `scripts/video_qa_gate_openai_compat.py`: strict QA gate.
- `references/cli.md`: CLI catalog and examples.
- `references/model-matrix.md`: judge/generation model routing notes.
- `references/troubleshooting.md`: failure modes and fixes.
