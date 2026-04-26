<script setup>
const featuredLead = {
  title: 'Introducing the OpenSIN Code app',
  meta: 'Video February 2, 2026',
  href: '/guide/opensin-code',
  image: 'https://cdn.openai.com/devhub/resources/video-1.png',
}

const featuredCards = [
  {
    title: 'OpenSIN Apps SDK examples',
    meta: 'Code October 6, 2025',
    href: '/guide/opensin-code',
    image: 'https://cdn.openai.com/devhub/resources/code-2.png',
  },
  {
    title: 'OpenSIN ChatKit starter app',
    meta: 'Code October 6, 2025',
    href: '/guide/opensin-code',
    image: 'https://cdn.openai.com/devhub/resources/code-3.png',
  },
  {
    title: 'OpenSIN A2A Protocol',
    meta: 'Guide September 29, 2025',
    href: '/guide/a2a-protocol',
    image: 'https://cdn.openai.com/devhub/resources/guide-4.png',
  },
]

const latestCards = [
  {
    title: 'OpenSIN Code Prompting Guide',
    meta: 'Kochbuch',
    description: 'Kochbuch zur Erstellung effektiver Video-Instrumente für die OpenSIN Code-Generation.',
    href: '/guide/opensin-code',
    tone: 'violet',
    icon: 'book',
  },
  {
    title: 'OpenSIN-Leitfaden für Gesprächsagenten',
    meta: 'Kochbuch',
    description: 'OpenSIN-Modelle erweitern die Grenzen von Intelligenz und Effizienz und unser empfohlenes agentenbasiertes Setup.',
    href: '/guide/team-orchestration',
    tone: 'gold',
    icon: 'chat',
  },
  {
    title: 'Wir stellen die OpenSIN-Code-App vor',
    meta: 'Video',
    description: 'Sehen Sie die OpenSIN Code-App in Aktion und erfahren Sie, wie sie Ihnen hilft, schneller zu entwickeln und zu liefern.',
    href: '/guide/opensin-code',
    tone: 'orange',
    icon: 'terminal',
  },
  {
    title: 'OpenSIN in JetBrains IDEs',
    meta: 'Video',
    description: 'Wie man OpenSIN in JetBrains IDEs wie Rider, IntelliJ, PyCharm und WebStorm verwendet.',
    href: '/guide/opensin-code',
    tone: 'sky',
    icon: 'monitor',
  },
  {
    title: 'Docs MCP',
    meta: 'Führung',
    description: 'Suchen und lesen Sie die Entwicklerdokumentation von OpenSIN direkt in Ihrem Editor mithilfe von MCP.',
    href: '/guide/mcp-integration',
    tone: 'mint',
    icon: 'search',
  },
  {
    title: 'OpenSIN Image-1.5 Prompting Guide',
    meta: 'Kochbuch',
    description: 'Anleitung zu zuverlässiger Bilderzeugung mit OpenSIN Image-1.5.',
    href: '/guide/opensin-code',
    tone: 'lavender',
    icon: 'image',
  },
]

const exploreCards = [
  {
    title: 'Blog',
    href: 'https://blog.opensin.ai',
    tone: 'violet',
    icon: 'spark',
  },
  {
    title: 'Ressourcen',
    href: '/guide/getting-started',
    tone: 'sky',
    icon: 'gift',
  },
  {
    title: 'Kochbuch',
    href: '/examples/hello-world',
    tone: 'mint',
    icon: 'book',
  },
]
</script>

<template>
  <div class="oa-page">
    <div class="oa-container">
      <section class="oa-hero">
        <h1 class="oa-hero__title">OpenSIN for developers</h1>
        <p class="oa-hero__subtitle">
          Docs and resources to help you build with, for, and on OpenSIN.
        </p>
      </section>

      <a class="oa-promo" href="/api/overview">
        <div class="oa-promo__media">
            <img
            src="https://developers.openai.com/images/api/models/icons/gpt-5.5.png"
            alt="OpenSIN sandbox agents"
          />
        </div>
        <div class="oa-promo__body">
          <span class="oa-promo__eyebrow">New</span>
          <h2 class="oa-promo__title">Sandbox agents in the OpenSIN Agents SDK</h2>
          <p class="oa-promo__description">
            Run agents in container-based environments with files, commands, skills, snapshots, and memory.
          </p>
        </div>
        <span class="oa-promo__arrow" aria-hidden="true">›</span>
      </a>

      <div class="oa-grid oa-grid--3">
        <a class="oa-tile" href="/api/">
          <span class="oa-tile__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <rect x="3" y="3" width="18" height="18" rx="3" />
              <path d="M3 9h18" />
              <path d="M9 21V9" />
            </svg>
          </span>
          <h3>OpenSIN Platform</h3>
          <p>Use OpenSIN APIs and models to build your own AI experiences.</p>
        </a>

        <a class="oa-tile" href="/guide/opensin-code">
          <span class="oa-tile__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M8 6 2 12l6 6" />
              <path d="m16 6 6 6-6 6" />
            </svg>
          </span>
          <h3>OpenSIN Code</h3>
          <p>Build and ship faster with OpenSIN Code — everywhere you work.</p>
        </a>

        <a class="oa-tile" href="/guide/a2a-protocol">
          <span class="oa-tile__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <rect x="3" y="3" width="7" height="7" rx="1.5" />
              <rect x="14" y="3" width="7" height="7" rx="1.5" />
              <rect x="14" y="14" width="7" height="7" rx="1.5" />
              <rect x="3" y="14" width="7" height="7" rx="1.5" />
            </svg>
          </span>
          <h3>OpenSIN Apps SDK</h3>
          <p>Extend OpenSIN surfaces with your apps built on top of the Model Context Protocol.</p>
        </a>
      </div>

      <section class="oa-section">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Featured</h2>
        </div>

        <a class="oa-featured-lead" :href="featuredLead.href">
          <div class="oa-featured-lead__media">
            <img :src="featuredLead.image" :alt="featuredLead.title" />
          </div>
          <div class="oa-featured-lead__body">
            <h3>{{ featuredLead.title }}</h3>
            <p>{{ featuredLead.meta }}</p>
          </div>
        </a>

        <div class="oa-featured-grid">
          <a v-for="card in featuredCards" :key="card.title" :href="card.href" class="oa-featured-card">
            <div class="oa-featured-card__media">
              <img :src="card.image" :alt="card.title" />
            </div>
            <div class="oa-featured-card__body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.meta }}</p>
            </div>
          </a>
        </div>
      </section>

      <section class="oa-section">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Latest</h2>
          <a href="/guide/getting-started" class="oa-view-all">View all</a>
        </div>

        <div class="oa-latest-grid">
          <a v-for="card in latestCards" :key="card.title" :href="card.href" class="oa-latest-card">
            <div :class="['oa-latest-card__media', `oa-latest-card__media--${card.tone}`]">
              <CardIcon :name="card.icon" variant="latest" />
            </div>
            <div class="oa-latest-card__body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
              <span class="oa-latest-card__meta">{{ card.meta }}</span>
            </div>
          </a>
        </div>
      </section>

      <section class="oa-section oa-section--explore">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Explore</h2>
        </div>

        <div class="oa-explore-grid">
          <a v-for="card in exploreCards" :key="card.title" :href="card.href" class="oa-explore-card">
            <div :class="['oa-explore-card__media', `oa-explore-card__media--${card.tone}`]">
              <CardIcon :name="card.icon" variant="explore" />
            </div>
            <h3>{{ card.title }}</h3>
          </a>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.oa-page {
  min-height: 100vh;
  background: #ffffff;
  color: #111827;
}

.oa-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 40px 96px;
}

.oa-hero {
  padding: 56px 0 26px;
  text-align: center;
}

.oa-hero__title {
  margin: 0;
  color: #111827;
  font-size: clamp(3rem, 6vw, 4.6rem);
  line-height: 0.96;
  letter-spacing: -0.06em;
  font-weight: 700;
}

.oa-hero__subtitle {
  margin: 16px auto 0;
  max-width: 680px;
  color: #4b5563;
  font-size: 1.05rem;
  line-height: 1.65;
}

.oa-promo {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 20px 22px;
  margin: 0 auto 28px;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  background: #ffffff;
  text-decoration: none;
  color: inherit;
  box-shadow: none;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-promo:hover {
  transform: translateY(-1px);
  border-color: #d1d5db;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.oa-promo__media {
  flex: 0 0 72px;
  width: 72px;
  height: 72px;
  border-radius: 14px;
  overflow: hidden;
  background: #f9fafb;
  border: none;
}

.oa-promo__media img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 8px;
  display: block;
}

.oa-promo__body {
  min-width: 0;
}

.oa-promo__arrow {
  margin-left: auto;
  color: #6b7280;
  font-size: 2rem;
  line-height: 1;
  font-weight: 300;
}

.oa-promo__eyebrow {
  display: inline-flex;
  align-items: center;
  margin-bottom: 10px;
  padding: 4px 10px;
  border-radius: 999px;
  background: #f3f4f6;
  color: #111827;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.oa-promo__title {
  margin: 0;
  color: #111827;
  font-size: 1.4rem;
  line-height: 1.2;
  letter-spacing: -0.03em;
  font-weight: 700;
}

.oa-promo__description {
  margin: 10px 0 0;
  color: #4b5563;
  font-size: 0.98rem;
  line-height: 1.55;
}

.oa-grid {
  display: grid;
  gap: 20px;
}

.oa-grid--3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.oa-tile {
  display: flex;
  flex-direction: column;
  min-height: 168px;
  padding: 24px;
  border: 0;
  border-radius: 18px;
  background: #f9fafb;
  text-decoration: none;
  color: inherit;
  box-shadow: none;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-tile:hover {
  transform: translateY(-2px);
  background: #f3f4f6;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.oa-tile__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  margin-bottom: 18px;
  border-radius: 12px;
  background: transparent;
  color: #111827;
}

.oa-tile__icon svg {
  width: 22px;
  height: 22px;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-width: 1.6;
}

.oa-tile h3 {
  margin: 0;
  color: #111827;
  font-size: 1.12rem;
  line-height: 1.25;
  letter-spacing: -0.02em;
  font-weight: 700;
}

.oa-tile p {
  margin: 10px 0 0;
  color: #4b5563;
  font-size: 0.96rem;
  line-height: 1.55;
}

.oa-section {
  margin-top: 72px;
}

.oa-section-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 28px;
}

.oa-section-title {
  margin: 0;
  color: #111827;
  font-size: 1.55rem;
  line-height: 1.1;
  letter-spacing: -0.03em;
  font-weight: 700;
}

.oa-view-all {
  color: #6b7280;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 600;
}

.oa-view-all:hover {
  color: #111827;
}

.oa-featured-lead {
  display: grid;
  grid-template-columns: minmax(0, 1.3fr) minmax(280px, 0.9fr);
  gap: 20px;
  margin-bottom: 22px;
  padding: 16px;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  background: #ffffff;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-featured-lead:hover {
  transform: translateY(-2px);
  border-color: #e5e7eb;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.05);
}

.oa-featured-lead__media,
.oa-featured-card__media,
.oa-latest-card__media,
.oa-explore-card__media {
  overflow: hidden;
  border-radius: 16px;
  background: linear-gradient(180deg, #f9fafb 0%, #ffffff 100%);
  border: 1px solid #eef2f7;
}

.oa-featured-lead__media {
  min-height: 240px;
}

.oa-featured-lead__media img,
.oa-featured-card__media img,
.oa-latest-card__media img,
.oa-explore-card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.oa-featured-lead__body {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 6px 4px 6px 0;
}

.oa-featured-lead__body h3,
.oa-featured-card__body h3,
.oa-latest-card__body h3 {
  margin: 0;
  color: #111827;
  line-height: 1.25;
  letter-spacing: -0.02em;
  font-weight: 700;
}

.oa-featured-lead__body h3 {
  font-size: 1.25rem;
}

.oa-featured-lead__body p,
.oa-featured-card__body p,
.oa-latest-card__body p {
  margin: 8px 0 0;
  color: #6b7280;
  font-size: 0.95rem;
  line-height: 1.5;
}

.oa-featured-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.oa-featured-card,
.oa-latest-card,
.oa-explore-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-featured-card {
  padding: 0;
  border: 0;
  border-radius: 18px;
  background: transparent;
  box-shadow: none;
  overflow: visible;
}

.oa-featured-card:hover,
.oa-latest-card:hover,
.oa-explore-card:hover {
  transform: translateY(-2px);
}

.oa-featured-card:hover {
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.oa-featured-card__media {
  aspect-ratio: 16 / 10;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: none;
}

.oa-featured-card__body {
  padding: 16px 18px 18px;
}

.oa-featured-card__body h3 {
  font-size: 1rem;
}

.oa-featured-card__body p {
  margin-top: 6px;
  font-size: 0.85rem;
}

.oa-latest-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 28px 44px;
}

.oa-latest-card {
  display: grid;
  grid-template-columns: 112px minmax(0, 1fr);
  gap: 16px;
  align-items: start;
  padding: 0;
  border: 0;
  background: transparent;
  box-shadow: none;
  overflow: visible;
}

.oa-latest-card:hover {
  transform: translateY(-2px);
}

.oa-latest-card__media {
  width: 112px;
  height: 112px;
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
  box-shadow: none;
}

.oa-latest-card__media--violet {
  background: linear-gradient(135deg, #c4b5fd 0%, #93c5fd 100%);
}

.oa-latest-card__media--gold {
  background: linear-gradient(135deg, #fde68a 0%, #f59e0b 100%);
}

.oa-latest-card__media--orange {
  background: linear-gradient(135deg, #fdba74 0%, #fb7185 100%);
}

.oa-latest-card__media--sky {
  background: linear-gradient(135deg, #bfdbfe 0%, #7dd3fc 100%);
}

.oa-latest-card__media--mint {
  background: linear-gradient(135deg, #a7f3d0 0%, #86efac 100%);
}

.oa-latest-card__media--lavender {
  background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
}

.oa-latest-card__body {
  padding: 6px 0 0;
}

.oa-latest-card__body h3 {
  font-size: 1rem;
}

.oa-latest-card__meta {
  display: inline-flex;
  margin-top: 12px;
  color: #9ca3af;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0;
}

.oa-section--explore {
  margin-top: 68px;
}

.oa-explore-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.oa-explore-card {
  padding: 0;
  border: 0;
  border-radius: 0;
  background: transparent;
  box-shadow: none;
  overflow: visible;
}

.oa-explore-card:hover {
  transform: translateY(-2px);
}

.oa-explore-card__media {
  aspect-ratio: 4 / 5;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  box-shadow: none;
}

.oa-explore-card__media--violet {
  background: linear-gradient(135deg, #c4b5fd 0%, #93c5fd 100%);
}

.oa-explore-card__media--sky {
  background: linear-gradient(135deg, #dbeafe 0%, #bae6fd 100%);
}

.oa-explore-card__media--mint {
  background: linear-gradient(135deg, #a7f3d0 0%, #93c5fd 100%);
}

.oa-explore-card h3 {
  margin: 0;
  padding: 14px 0 0;
  color: #111827;
  font-size: 1rem;
  line-height: 1.25;
  letter-spacing: -0.02em;
  font-weight: 700;
}

@media (max-width: 980px) {
  .oa-grid--3,
  .oa-featured-grid,
  .oa-explore-grid {
    grid-template-columns: 1fr;
  }

  .oa-latest-grid,
  .oa-featured-lead {
    grid-template-columns: 1fr;
  }

  .oa-latest-card {
    grid-template-columns: 112px minmax(0, 1fr);
  }

  .oa-promo {
    flex-direction: column;
    align-items: flex-start;
  }

  .oa-promo__media {
    width: 100%;
    flex-basis: auto;
    aspect-ratio: 16 / 9;
    height: auto;
  }

  .oa-promo__arrow {
    margin-left: 0;
  }

  .oa-latest-card {
    grid-template-columns: 1fr;
  }

  .oa-latest-card__media {
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
  }
}

@media (min-width: 981px) and (max-width: 1200px) {
  .oa-latest-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .oa-container {
    padding: 0 20px 80px;
  }

  .oa-hero {
    padding-top: 40px;
  }

  .oa-section {
    margin-top: 56px;
  }

  .oa-promo,
  .oa-tile,
  .oa-featured-lead,
  .oa-featured-card,
  .oa-latest-card,
  .oa-explore-card {
    border-radius: 16px;
  }

  .oa-section-title {
    font-size: 1.3rem;
  }

  .oa-section-header {
    margin-bottom: 22px;
  }
}

:global(.dark) .oa-page {
  background: #0a0a0a;
  color: #ececf1;
}

:global(.dark) .oa-hero__title,
:global(.dark) .oa-section-title,
:global(.dark) .oa-featured-lead__body h3,
:global(.dark) .oa-featured-card__body h3,
:global(.dark) .oa-latest-card__body h3,
:global(.dark) .oa-explore-card h3,
:global(.dark) .oa-tile h3 {
  color: #ececf1;
}

:global(.dark) .oa-hero__subtitle,
:global(.dark) .oa-promo__description,
:global(.dark) .oa-tile p,
:global(.dark) .oa-featured-lead__body p,
:global(.dark) .oa-featured-card__body p,
:global(.dark) .oa-latest-card__body p {
  color: #c5c5d2;
}

:global(.dark) .oa-promo,
:global(.dark) .oa-tile,
:global(.dark) .oa-featured-lead,
:global(.dark) .oa-featured-card,
:global(.dark) .oa-latest-card,
:global(.dark) .oa-explore-card {
  background: #111111;
  border-color: #2a2a2a;
  box-shadow: none;
}

:global(.dark) .oa-promo__eyebrow {
  background: rgba(68, 147, 248, 0.14);
  color: #9ecbff;
}

:global(.dark) .oa-tile__icon {
  background: rgba(68, 147, 248, 0.14);
  color: #9ecbff;
}

:global(.dark) .oa-view-all {
  color: #c5c5d2;
}

:global(.dark) .oa-view-all:hover {
  color: #ffffff;
}

:global(.dark) .oa-latest-card__media,
:global(.dark) .oa-explore-card__media,
:global(.dark) .oa-featured-lead__media,
:global(.dark) .oa-featured-card__media {
  border-color: #2a2a2a;
  box-shadow: none;
}
</style>
