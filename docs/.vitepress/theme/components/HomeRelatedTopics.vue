<template>
  <section class="home-related-topics">
    <div class="home-related-topics__eyebrow">Cross-surface navigation</div>
    <h2 class="home-related-topics__title">Related topics</h2>
    <p class="home-related-topics__lede">
      Keep the ecosystem scan-friendly without changing the protected four-card section shape.
    </p>

    <div class="home-related-topics__grid">
      <a v-for="card in cards" :key="card.title" :href="card.href" class="home-related-topics__card">
        <div class="home-related-topics__label">{{ card.label }}</div>
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
 * - Keep this array at exactly 4 items while issue #141 is the active contract.
 * - This component exists so the homepage keeps a polished surface-card system
 *   without pushing raw layout HTML into docs/index.md.
 */
const cards = [
  {
    title: 'OpenSIN Marketing',
    description: 'Brand, discovery, and the public-facing narrative around the ecosystem.',
    href: 'https://opensin.ai',
    label: 'Surface',
  },
  {
    title: 'OpenSIN Marketplace',
    description: 'Plans, bundles, and commercial packaging for premium access.',
    href: 'https://my.opensin.ai',
    label: 'Commerce',
  },
  {
    title: 'OpenSIN Dashboard',
    description: 'Authenticated fleet control, chat, and the active operator workspace.',
    href: 'https://chat.opensin.ai',
    label: 'Control',
  },
  {
    title: 'Domain Registry',
    description: 'Verified public, gated, and internal surfaces kept in one canonical map.',
    href: '/governance/domain-registry',
    label: 'Governance',
  },
]
</script>

<style scoped>
.home-related-topics {
  margin-top: 3.25rem;
}

.home-related-topics__eyebrow {
  margin-bottom: 0.7rem;
  color: var(--opensin-home-accent-text);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.home-related-topics__title {
  margin: 0;
  font-size: clamp(1.75rem, 2.8vw, 2.2rem);
  font-weight: 800;
  letter-spacing: -0.04em;
}

.home-related-topics__lede {
  max-width: 42rem;
  margin: 0.85rem 0 1.5rem;
  color: var(--vp-c-text-2);
  font-size: 1rem;
  line-height: 1.65;
}

.home-related-topics__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.home-related-topics__card {
  display: block;
  padding: 1.2rem 1.2rem 1.3rem;
  border-radius: 20px;
  border: 1px solid var(--opensin-home-card-border);
  background: var(--opensin-home-card-bg);
  box-shadow: var(--opensin-home-card-shadow);
  text-decoration: none;
  transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
}

.home-related-topics__card:hover {
  transform: translateY(-3px);
  border-color: var(--opensin-home-card-border-strong);
  box-shadow: var(--opensin-home-card-shadow-hover);
}

.home-related-topics__label {
  display: inline-flex;
  align-items: center;
  min-height: 1.65rem;
  margin-bottom: 0.9rem;
  padding: 0.18rem 0.62rem;
  border-radius: 999px;
  background: var(--opensin-home-pill-bg);
  color: var(--opensin-home-accent-text);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.home-related-topics__heading {
  color: var(--vp-c-text-1);
  font-size: 1.08rem;
  font-weight: 750;
  margin-bottom: 0.35rem;
}

.home-related-topics__description {
  color: var(--vp-c-text-2);
  font-size: 0.97rem;
  line-height: 1.58;
}

@media (max-width: 640px) {
  .home-related-topics__grid {
    grid-template-columns: 1fr;
  }
}
</style>
