<template>
  <section class="home-related-topics">
    <h2 class="home-related-topics__title">Related topics</h2>
    <div class="home-related-topics__grid">
      <a v-for="card in cards" :key="card.title" :href="card.href" class="home-related-topics__card">
        <div class="home-related-topics__heading">
          {{ card.title }}
        </div>
        <div class="home-related-topics__description">{{ card.description }}</div>
      </a>
    </div>
  </section>
</template>

<script setup lang="ts">
/**
 * Homepage related-topics grid.
 * DO NOT replace with inline HTML in index.md again.
 * This component exists so the homepage can keep the premium surface-card look
 * without polluting markdown content with raw layout markup.
 */
const cards = [
  {
    title: 'Consumer docs',
    description: 'Guides, onboarding, and product help',
    href: '/guide/getting-started',
  },
  {
    title: 'Developer portal',
    description: 'APIs, SDKs, auth, and webhooks',
    href: 'https://developers.opensin.ai/docs/',
  },
  {
    title: 'MyOpenSIN',
    description: 'Plans, billing, and customer access',
    href: 'https://my.opensin.ai',
  },
  {
    title: 'Surface registry',
    description: 'Public, gated, and internal surface rules',
    href: '/governance/domain-registry',
  },
]
</script>

<style scoped>
.home-related-topics {
  margin-top: 3rem;
}

.home-related-topics__title {
  margin: 0 0 1rem;
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -0.03em;
}

.home-related-topics__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.home-related-topics__card {
  display: block;
  padding: 1.15rem 1.2rem;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: #141414;
  text-decoration: none;
  transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
}

.home-related-topics__card:hover {
  transform: translateY(-2px);
  border-color: rgba(0, 204, 136, 0.45);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.22);
}

.home-related-topics__heading {
  color: #f5f5f5;
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.home-related-topics__description {
  color: #8e8ea0;
  font-size: 0.95rem;
  line-height: 1.45;
}

:global(html:not(.dark)) .home-related-topics__card {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
}

:global(html:not(.dark)) .home-related-topics__heading {
  color: #0f172a;
}

:global(html:not(.dark)) .home-related-topics__description {
  color: #475569;
}

@media (max-width: 960px) {
  .home-related-topics__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .home-related-topics__grid {
    grid-template-columns: 1fr;
  }
}
</style>
