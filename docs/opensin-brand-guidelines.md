# 🎨 OpenSIN Brand Guidelines

**Version:** 1.0  
**Last Updated:** 2026-04-04  
**Status:** Enterprise Standard

---

## 🏷️ Brand Identity

| Property | Value |
|----------|-------|
| **Name** | OpenSIN AI |
| **Tagline** | Enterprise AI Agent Platform |
| **Description** | Multi-billion dollar enterprise AI platform that orchestrates specialized AI agents for code generation, media creation, research, and automation |
| **Tone** | Direct, premium, confident, technical but accessible |
| **Personality** | Authoritative yet approachable — like a senior engineer who explains complex things simply |

---

## 🎨 Color Palette

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **OpenSIN Green** | `#00bb7f` | Main brand color, CTAs, highlights |
| **Dark Green** | `#004e3b` | Backgrounds, depth |
| **Light Green** | `#05df72` | Highlights, accents |

### Secondary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Emerald** | `#10b981` | Supporting elements |
| **Hot Red** | `#ff2357` | CTAs, alerts, emphasis |
| **Orange** | `#fe6e00` | Secondary accent |

### Neutral Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Black** | `#000000` | Pure black |
| **Darkest** | `#09090b` | Primary background |
| **Dark** | `#18181b` | Secondary background |
| **Dark Gray** | `#27272a` | Cards, panels |
| **Gray** | `#808080` | Body text on dark |
| **Light Gray** | `#d4d4d8` | Subtle elements |
| **White** | `#ffffff` | Text on dark |

### Tech Accents
| Color | Hex | Usage |
|-------|-----|-------|
| **Tech Blue** | `#54a2ff` | Data streams, connections |
| **Tech Purple** | `#3080ff` | AI/ML elements |
| **Tech Gold** | `#f99c00` | Premium features |

---

## 🔤 Typography

- **Primary Font:** Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
- **Monospace:** "JetBrains Mono", "Fira Code", "SF Mono", monospace

### Blog/Article
| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 | 3rem | 800 | 1.1 |
| H2 | 2rem | 700 | 1.2 |
| H3 | 1.5rem | 600 | 1.3 |
| Body | 1.125rem | 400 | 1.7 |
| Caption | 0.875rem | 400 | 1.5 |

### Video Subtitles
| Element | Size | Weight | Style |
|---------|------|--------|-------|
| Subtitle | 1.5rem | 600 | White text, dark bg, 8px radius |
| Title | 2.5rem | 800 | White text |
| CTA | 1.25rem | 600 | Green (#00bb7f) |

---

## 🖼️ Logo

- **File:** `logo.png` (512x512 PNG)
- **Location:** `/Users/jeremy/dev/OpenSIN-website/public/logo.png`

### Logo Placement Rules
| Channel | Position | Size | Padding |
|---------|----------|------|---------|
| Blog Header | Top-left | 8% of width | 2% |
| Video | Top-right | 5% of width | 3% |
| Social Media | Bottom-right | 6% of width | 2% |
| End Card | Center | 15% of width | — |

---

##  Brand Voice

### Message Hierarchy (MUST follow in all content)
1. **HOOK** — Grab attention in first 3 seconds/lines
2. **PROMISE** — What OpenSIN delivers
3. **PROOF** — Evidence, metrics, demonstrations
4. **CTA** — Single, clear call-to-action

### Preferred Words
`enterprise`, `orchestrate`, `autonomous`, `specialized`, `production-grade`, `scalable`, `intelligent`, `workflow`, `agent`, `swarm`, `pipeline`, `infrastructure`

### Banned Words
`magic`, `revolutionary`, `game-changing`, `disrupt`, `cutting-edge`, `next-gen`, `unprecedented`

### Tone by Channel
| Channel | Tone |
|---------|------|
| Blog | In-depth, technical, authoritative, practical examples |
| Twitter | Punchy, insight-driven, data-backed, thread format |
| YouTube | Professional, demo-focused, clear narration |
| LinkedIn | Business-focused, ROI-driven, enterprise language |
| Instagram | Visual-first, behind-the-scenes, team culture |
| TikTok | Fast-paced, trend-aware, educational entertainment |

---

## 🎬 Video Packaging

### TTS Voice
- **Provider:** Gemini 2.5 Flash Preview TTS
- **Voice:** Aoede (professional, clear)
- **Language:** en-US
- **Speed:** 1.0x

### Subtitle Style
- **Style:** Modern minimal
- **Position:** Bottom-center
- **Max Length:** 42 chars per line, 2 lines max
- **Highlight Color:** Green (#00bb7f)
- **Animation:** Word-by-word
- **Font:** Inter, 600 weight

### End Card
- **Duration:** 3 seconds
- **Background:** #09090b
- **Logo:** Center
- **Tagline:** "OpenSIN AI — Enterprise Agent Platform"
- **CTA:** "Visit opensin.ai"

### Background Music
- **Style:** Ambient electronic
- **Volume:** 15% of narration
- **Fade In:** 2 seconds
- **Fade Out:** 3 seconds

---

## 🎨 Visual Style

### Aesthetic
- Dark, futuristic, enterprise-grade, clean, premium
- Neural network connections (subtle, low opacity)
- Data stream lines (animated for video, static for images)
- Geometric grid patterns (very subtle)

### Image Generation Prompt Suffix (ALWAYS append)
```
. Dark background with deep blue and purple gradients. Clean, modern, enterprise-grade design. Professional tech aesthetic. OpenSIN brand colors: green (#00bb7f), dark (#09090b), accent red (#ff2357). No text in image. 16:9 aspect ratio.
```

### Video Generation Prompt Suffix (ALWAYS append)
```
. Dark futuristic interface with glowing data streams. Neural network nodes pulse with green (#00bb7f) and blue (#54a2ff) light. Professional tech aesthetic, photorealistic, cinematic lighting, 16:9 aspect ratio. No text in video.
```

### Prohibited
- ❌ Generic stock photo aesthetics
- ❌ Cartoon or illustration style (unless specifically requested)
- ❌ Bright/cheerful colors — keep dark and premium
- ❌ Text embedded in generated images/videos
- ❌ Watermarks other than OpenSIN logo
- ❌ Competitor brand elements

---

## 🔄 Content Pipeline

1. **BRIEF** — Define audience, key message, channel, format
2. **SCRIPT** — Write narration following message hierarchy
3. **GENERATE** — Create raw media with brand prompts
4. **TTS** — Generate voice narration from script
5. **SUBTITLES** — Generate timed SRT subtitles
6. **PACKAGE** — Add logo, end card, BGM, color grade
7. **REVIEW** — Check against brand guidelines
8. **PUBLISH** — Export in platform-specific formats

### Quality Checklist
- [ ] Logo visible and correctly placed
- [ ] Brand colors used consistently
- [ ] Typography matches brand guidelines
- [ ] Message hierarchy followed (Hook → Promise → Proof → CTA)
- [ ] No banned words used
- [ ] Tone matches channel requirements
- [ ] Subtitles readable and properly timed
- [ ] Audio levels balanced (narration > BGM)
- [ ] End card includes logo + CTA

---

## 🔗 Related Docs

- [A2A SIN Agents](./a2a-sin-agents.md)
- [OpenSIN-Code Overview](./opensin-code.md)
- [Bug Library](./bugs.md)
- [Runbooks](./runbooks.md)
