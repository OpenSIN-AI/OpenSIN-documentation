/**
 * OpenSIN Brand Guidelines — Enterprise Brand System
 *
 * Defines the complete visual and verbal identity for OpenSIN AI.
 * All generated media (images, videos, blog posts, social content)
 * MUST follow these guidelines for brand consistency.
 *
 * Based on analysis of OpenSIN-website brand colors and enterprise
 * AI company best practices (2026).
 */

export const OPENSIN_BRAND = {
  // ── Brand Name ────────────────────────────────────────────────
  name: 'OpenSIN',
  fullName: 'OpenSIN AI',
  tagline: 'Enterprise AI Agent Platform',
  description: 'OpenSIN is a multi-billion dollar enterprise AI platform that orchestrates specialized AI agents for code generation, media creation, research, and automation.',

  // ── Logo ──────────────────────────────────────────────────────
  logo: {
    path: '/Users/jeremy/dev/OpenSIN-website/public/logo.png',
    size: { width: 512, height: 512 },
    format: 'PNG',
    // Logo placement rules
    placement: {
      // Blog header: top-left corner, 8% of width
      blogHeader: { position: 'top-left', sizePercent: 8, padding: '2%' },
      // Video: top-right corner, 5% of width, semi-transparent
      video: { position: 'top-right', sizePercent: 5, opacity: 0.8, padding: '3%' },
      // Social media: bottom-right corner, 6% of width
      social: { position: 'bottom-right', sizePercent: 6, padding: '2%' },
      // End card: center, 15% of width
      endCard: { position: 'center', sizePercent: 15 },
    },
  },

  // ── Color Palette ─────────────────────────────────────────────
  colors: {
    // Primary
    primary: '#00bb7f',      // OpenSIN Green — main brand color
    primaryDark: '#004e3b',   // Dark green — backgrounds, depth
    primaryLight: '#05df72',  // Light green — highlights, accents

    // Secondary
    secondary: '#10b981',     // Tailwind emerald — supporting elements
    accent: '#ff2357',        // Hot pink/red — CTAs, alerts, emphasis
    accentOrange: '#fe6e00',  // Orange — secondary accent

    // Neutrals
    black: '#000000',
    darkest: '#09090b',       // Primary background
    dark: '#18181b',          // Secondary background
    darkGray: '#27272a',      // Cards, panels
    gray: '#808080',          // Body text on dark
    lightGray: '#d4d4d8',     // Subtle elements
    white: '#ffffff',

    // Tech accents
    techBlue: '#54a2ff',      // Data streams, connections
    techPurple: '#3080ff',    // AI/ML elements
    techGold: '#f99c00',      // Premium features
    techGoldDark: '#edb200',  // Gold accents
  },

  // ── Typography ────────────────────────────────────────────────
  typography: {
    // Primary font family (used across all media)
    fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    // Monospace for code
    monoFont: '"JetBrains Mono", "Fira Code", "SF Mono", monospace',

    // Blog/Article
    blog: {
      h1: { size: '3rem', weight: 800, lineHeight: 1.1, letterSpacing: '-0.02em' },
      h2: { size: '2rem', weight: 700, lineHeight: 1.2, letterSpacing: '-0.01em' },
      h3: { size: '1.5rem', weight: 600, lineHeight: 1.3 },
      body: { size: '1.125rem', weight: 400, lineHeight: 1.7 },
      caption: { size: '0.875rem', weight: 400, lineHeight: 1.5, color: '#808080' },
    },

    // Video subtitles/captions
    video: {
      subtitle: { size: '1.5rem', weight: 600, fontFamily: 'Inter', color: '#ffffff', textShadow: '0 2px 4px rgba(0,0,0,0.8)', backgroundColor: 'rgba(0,0,0,0.6)', padding: '8px 16px', borderRadius: '8px' },
      title: { size: '2.5rem', weight: 800, fontFamily: 'Inter', color: '#ffffff' },
      cta: { size: '1.25rem', weight: 600, fontFamily: 'Inter', color: '#00bb7f' },
    },

    // Social media
    social: {
      headline: { size: '2rem', weight: 800, fontFamily: 'Inter' },
      body: { size: '1rem', weight: 400, fontFamily: 'Inter' },
    },
  },

  // ── Visual Style ──────────────────────────────────────────────
  visualStyle: {
    // Overall aesthetic
    aesthetic: 'Dark, futuristic, enterprise-grade, clean, premium',
    mood: 'Professional, innovative, trustworthy, powerful',

    // Background patterns
    backgrounds: [
      'Dark gradient (#09090b → #18181b)',
      'Neural network connections (subtle, low opacity)',
      'Data stream lines (animated for video, static for images)',
      'Geometric grid patterns (very subtle)',
    ],

    // Image generation prompts — ALWAYS include these
    imagePromptSuffix:
      '. Dark background with deep blue and purple gradients. Clean, modern, enterprise-grade design. Professional tech aesthetic. OpenSIN brand colors: green (#00bb7f), dark (#09090b), accent red (#ff2357). No text in image — text will be added in post-production. 16:9 aspect ratio.',

    // Video generation prompts — ALWAYS include these
    videoPromptSuffix:
      '. Dark futuristic interface with glowing data streams. Neural network nodes pulse with green (#00bb7f) and blue (#54a2ff) light. Professional tech aesthetic, photorealistic, cinematic lighting, 16:9 aspect ratio. No text in video — text and subtitles will be added in post-production.',

    // What to NEVER generate
    prohibited: [
      'No generic stock photo aesthetics',
      'No cartoon or illustration style (unless specifically requested)',
      'No bright/cheerful colors — keep dark and premium',
      'No text embedded in generated images/videos',
      'No watermarks other than OpenSIN logo',
      'No competitor brand elements',
    ],
  },

  // ── Brand Voice ───────────────────────────────────────────────
  voice: {
    tone: 'Direct, premium, confident, technical but accessible',
    personality: 'Authoritative yet approachable — like a senior engineer who can explain complex things simply',
    language: 'English (primary), German (secondary)',

    // Message hierarchy for all content
    messageHierarchy: {
      // 1. Hook — grab attention in first 3 seconds/lines
      hook: 'Lead with the most impactful benefit or insight',
      // 2. Promise — what OpenSIN delivers
      promise: 'Clear value proposition — what problem we solve',
      // 3. Proof — evidence, metrics, demonstrations
      proof: 'Show, don\'t tell — demos, metrics, testimonials',
      // 4. CTA — clear next step
      cta: 'Single, clear call-to-action — never more than one',
    },

    // Tone by channel
    channelTone: {
      blog: 'In-depth, technical, authoritative, with practical examples',
      twitter: 'Punchy, insight-driven, data-backed, thread format',
      youtube: 'Professional, demo-focused, clear narration',
      linkedin: 'Business-focused, ROI-driven, enterprise language',
      instagram: 'Visual-first, behind-the-scenes, team culture',
      tiktok: 'Fast-paced, trend-aware, educational entertainment',
    },

    // Words to USE
    preferredWords: [
      'enterprise', 'orchestrate', 'autonomous', 'specialized',
      'production-grade', 'scalable', 'intelligent', 'workflow',
      'agent', 'swarm', 'pipeline', 'infrastructure',
    ],

    // Words to AVOID
    bannedWords: [
      'magic', 'revolutionary', 'game-changing', 'disrupt',
      'cutting-edge', 'next-gen', 'unprecedented',
    ],
  },

  // ── Video Packaging Rules ─────────────────────────────────────
  videoPackaging: {
    // TTS Voice settings
    tts: {
      provider: 'gemini-2.5-flash-native-audio-latest', // or ElevenLabs
      voice: 'professional-male-deep', // or 'professional-female-clear'
      language: 'en-US',
      speed: 1.0,
      pitch: 0.0,
      style: 'narration', // narration, conversational, energetic
    },

    // Subtitle style
    subtitles: {
      style: 'modern-minimal', // modern-minimal, bold-highlight, karaoke
      position: 'bottom-center',
      maxLineLength: 42,
      maxLines: 2,
      highlightColor: '#00bb7f', // Green highlight for key words
      animation: 'word-by-word', // word-by-word, line-by-line, fade
      fontFamily: 'Inter',
      fontWeight: 600,
    },

    // End card
    endCard: {
      duration: 3, // seconds
      background: '#09090b',
      logo: 'center',
      tagline: 'OpenSIN AI — Enterprise Agent Platform',
      cta: 'Visit opensin.ai',
      socialHandles: '@OpenSIN_AI',
    },

    // Intro bumper (optional, for YouTube)
    introBumper: {
      duration: 2,
      animation: 'logo-reveal',
      sound: 'subtle-whoosh',
    },

    // Background music
    bgm: {
      style: 'ambient-electronic', // ambient-electronic, lofi-tech, cinematic
      volume: 0.15, // 15% of narration volume
      fadeIn: 2,
      fadeOut: 3,
    },
  },

  // ── Content Pipeline ──────────────────────────────────────────
  pipeline: {
    steps: [
      '1. BRIEF — Define audience, key message, channel, format',
      '2. SCRIPT — Write narration script with message hierarchy',
      '3. GENERATE — Create raw media (images/video) with brand prompts',
      '4. TTS — Generate voice narration from script',
      '5. SUBTITLES — Generate timed subtitles from narration',
      '6. PACKAGE — Add logo, end card, BGM, color grade',
      '7. REVIEW — Check against brand guidelines',
      '8. PUBLISH — Export in platform-specific formats',
    ],
    qualityChecks: [
      'Logo visible and correctly placed',
      'Brand colors used consistently',
      'Typography matches brand guidelines',
      'Message hierarchy followed (Hook → Promise → Proof → CTA)',
      'No banned words used',
      'Tone matches channel requirements',
      'Subtitles readable and properly timed',
      'Audio levels balanced (narration > BGM)',
      'End card includes logo + CTA',
    ],
  },
} as const

export type OpenSINBrand = typeof OPENSIN_BRAND
