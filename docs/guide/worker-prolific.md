# A2A-SIN-Worker-Prolific v7.3

Autonomous Prolific survey worker. Connects via CDP to local Chrome, scans for studies, fills surveys using Groq Vision (FREE), and submits them automatically.

## Architecture

```
+---------------------------------------------------------+
|                MAC (100% LOCAL)                          |
|                                                         |
|  Chrome (Default Profile)  <--CDP--> Worker v7.3        |
|  + OpenSIN Bridge v4.0.0   Port 9335  (Python)          |
|  + Prolific Session                                     |
|                                  - Groq Vision FREE     |
|                                  - Dual-Key Rotation    |
|                                  - Human Emulation      |
|                                  - Full Submit Pipeline |
+---------------------------------------------------------+
```

## Components

| Class | Lines | Purpose |
|-------|-------|---------|
| `CDPClient` | ~300 | Direct Chrome DevTools Protocol |
| `GroqVision` | ~80 | Free vision AI with dual-key rotation and 3-model fallback |
| `HumanEmulator` | ~150 | Anti-detection: human-like typing, clicking, scrolling |
| `ProlificWorker` | ~1100 | Full lifecycle: login, scan, reserve, fill, submit, repeat |

## Study Submission Pipeline

The complete Prolific study lifecycle discovered and verified via live CDP testing:

1. Click study card on `/studies` list
2. Click "Take part" / "Reserve" button
3. Click "Open study in new window" (with popup blocker bypass)
4. Complete or visit external survey
5. Click "I'm finished"
6. Click "I didn't receive a completion code" (NOCODE path)
7. Click "Yes, I understand"
8. Study shows "Awaiting review"

### Edge Cases

**Auto-complete studies**: Some screening studies show "Thank you!" immediately without submission buttons. Detected via heading text and treated as completed.

**Popup blocker**: When the "Open study" button doesn't open a new tab, the external URL is extracted from page links and navigated to directly.

**Stuck in-progress studies**: 3-state FSM detects and clears studies stuck from previous sessions.

## Groq Vision (FREE)

Two API keys from gcloud Secret Manager with automatic rotation on 429 rate limits.

3-model fallback chain:
1. `meta-llama/llama-4-scout-17b-16e-instruct`
2. `meta-llama/llama-3.2-90b-vision-preview`
3. `meta-llama/llama-3.2-11b-vision-preview`

## Quick Start

```bash
# Start Chrome with CDP
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9335 \
  --user-data-dir="/Users/$USER/Library/Application Support/Google/Chrome/Default"

# Run worker
pip install websockets
python3 src/worker_v7.py
```

## Credentials

All secrets loaded from gcloud Secret Manager (`artificial-biometrics` project):
- `spm-prolific_email`
- `spm-prolific_password`
- `spm-groq_api_key_1`
- `spm-groq_api_key_2`

## Repository

[OpenSIN-AI/A2A-SIN-Worker-Prolific](https://github.com/OpenSIN-AI/A2A-SIN-Worker-Prolific)

## Version History

| Version | Changes |
|---------|---------|
| v7.0 | Direct CDP + Groq Vision + Human Emulation + gcloud secrets |
| v7.1 | Auth0 login fix, real Prolific DOM selectors |
| v7.2 | 3-state in-progress study FSM |
| v7.3 | Full submission pipeline, dual-key rotation, popup bypass, auto-complete detection |
