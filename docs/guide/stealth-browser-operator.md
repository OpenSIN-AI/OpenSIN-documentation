# Stealth Browser Operator

Autonomer Browser-Operator mit Videoaufzeichnung, TTS-Vertonung und FFmpeg-Watermarking.

> **Installiert unter:** `~/.config/opencode/skills/stealth-browser-operator/SKILL.md`

## Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                    Stealth Browser Operator                   │
├────────────┬──────────────┬──────────────┬──────────────────┤
│ Phase 1    │ Phase 2      │ Phase 3      │ Phase 4          │
│ Proxy +    │ Browser      │ TTS +        │ FFmpeg           │
│ Browser    │ Navigation   │ Voiceover    │ Watermarking     │
│ Recording  │ + Recording  │ Generation   │ + Merge          │
└────────────┴──────────────┴──────────────┴──────────────────┘
```

## Installation

### 1. Abhängigkeiten

```bash
# Browser-Automatisierung
pip3 install --break-system-packages browser-use[video]

# TTS-Sprachausgabe (Microsoft Neural Voices, kostenlos)
pip3 install --break-system-packages edge-tts

# FFmpeg (bereits installiert via Homebrew)
brew install ffmpeg  # Falls noch nicht vorhanden
```

### 2. Verzeichnisstruktur

```
~/.config/opencode/
├── skills/
│   └── stealth-browser-operator/
│       └── SKILL.md              # Handlungsanweisung für Agenten
└── tools/
    ├── browser-recorder.py        # Browser-Automatisierung + Video
    ├── tts-generator.py           # Text-to-Speech (edge-tts/Kokoro)
    ├── video-processor.py         # FFmpeg Post-Production
    └── master-operator.py         # Alles-in-Einem Pipeline
```

## Quick Start

### Einzel-Befehl (Master Pipeline)

```bash
python3 ~/.config/opencode/tools/master-operator.py \
  --url "https://my.opensin.ai" \
  --task "Gehe zu Settings und aktiviere Dark Mode" \
  --tts-text "Ich zeige dir jetzt die Einstellungen von OpenSIN AI" \
  --logo "/Users/jeremy/dev/OpenSIN-documentation/docs/public/logo.png" \
  --text-overlay "OpenSIN AI — Settings Tutorial" \
  --output-dir "./recordings/$(date +%Y%m%d_%H%M%S)" \
  --chrome-profile "Default"
```

### Einzelne Phasen

**Phase 1: Browser-Recording**
```bash
python3 ~/.config/opencode/tools/browser-recorder.py \
  --url "https://example.com" \
  --task "Klicke auf Login, navigiere zu Dashboard" \
  --output-dir "./recordings" \
  --profile "Default"
```

**Phase 2: TTS-Vertonung**
```bash
python3 ~/.config/opencode/tools/tts-generator.py \
  --text "Willkommen bei OpenSIN AI" \
  --output "./recordings/voiceover.mp3" \
  --voice "de-DE-KatjaNeural"
```

**Phase 3: FFmpeg Post-Production**
```bash
python3 ~/.config/opencode/tools/video-processor.py \
  --input-video "./recordings/recording.mp4" \
  --audio "./recordings/voiceover.mp3" \
  --output "./recordings/final.mp4" \
  --logo "/path/to/logo.png" \
  --text "OpenSIN AI Demo"
```

## Verfügbare deutsche Stimmen

| Stimme | Geschlecht | Stil |
|--------|-----------|------|
| `de-DE-KatjaNeural` | Weiblich | Natürlich (EMPFOHLEN) |
| `de-DE-ConradNeural` | Männlich | Professionell |
| `de-DE-BerndNeural` | Männlich | Tief |
| `de-DE-ChristophNeural` | Männlich | Professionell |
| `de-DE-AmalaNeural` | Weiblich | Warm |
| `de-DE-ElkeNeural` | Weiblich | Freundlich |
| `de-DE-KlausNeural` | Männlich | Seriös |
| `de-DE-MajaNeural` | Weiblich | Sanft |

Alle 15 Stimmen: `python3 ~/.config/opencode/tools/tts-generator.py --list-voices`

## Output-Struktur

```
recordings/<DATUM_UHRZEIT>/
├── recording.mp4          # Roh-Aufnahme
├── screenshots/           # Screenshots pro Schritt
├── voiceover.mp3          # TTS-Audio
├── final.mp4              # Fertiges Video mit Wasserzeichen
├── pipeline-metadata.json # Vollständige Pipeline-Metadaten
└── metadata.json          # Browser-Session-Metadaten
```

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Vision-Gate** | -7.0 | KEINE Browser-Aktion ohne Screenshot + Vision-Check |
| **DevTools-First** | -1.0 | JEDER CSS-Selektor via DevTools verifizieren |
| **Technologie-Souveränität** | -2.0 | nodriver + Chrome Profil — Playwright/etc. verboten |
| **Bun-Only** | -1.5 | `bun install` — npm/pnpm verboten |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/browser-automation)
