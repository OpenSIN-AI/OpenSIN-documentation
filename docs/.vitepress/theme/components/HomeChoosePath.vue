<template>
  <section class="home-choose-path">
    <div class="home-choose-path__eyebrow">Start with the right entry point</div>
    <h2 class="home-choose-path__title">Choose Your Path</h2>
    <p class="home-choose-path__lede">
      The homepage contract protects exactly two cards here: one for operators and one for builders.
    </p>

    <div class="home-choose-path__grid">
      <a
        v-for="card in cards"
        :key="card.title"
        :href="card.href"
        class="home-choose-path__card"
        :class="{ 'is-highlight': card.highlight }"
      >
        <div class="home-choose-path__label">{{ card.label }}</div>
        <div class="home-choose-path__heading">
          {{ card.title }}
          <span class="home-choose-path__arrow">→</span>
        </div>
        <div class="home-choose-path__description">{{ card.description }}</div>
      </a>
    </div>
  </section>
</template>

<script setup lang="ts">
/**
 * Homepage contract note:
 * - Keep this array at exactly 2 entries unless issue #141 is formally replaced.
 * - Styling intentionally consumes the shared homepage tokens from custom.css so
 *   hero/features/path/topic cards feel like one surface system across themes.
 */
const cards = [
  {
    title: 'User Documentation',
    description: 'Learn the operator path, daily workflows, and the shortest route to a productive OpenSIN fleet.',
    href: '/guide/getting-started',
    label: 'Operate',
    highlight: true,
  },
  {
    title: 'Developer Documentation',
    description: 'Build plugins, compose A2A agents, and ship integrations without leaving the existing docs contract.',
    href: '/sdk/overview',
    label: 'Build',
    highlight: false,
  },
]
</script>

<style scoped>
.home-choose-path {
  margin-top: 3.5rem;
}

.home-choose-path__eyebrow {
  margin-bottom: 0.7rem;
  color: var(--opensin-home-accent-text);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.home-choose-path__title {
  margin: 0;
  font-size: clamp(1.75rem, 2.8vw, 2.2rem);
  font-weight: 800;
  letter-spacing: -0.04em;
}

.home-choose-path__lede {
  max-width: 42rem;
  margin: 0.85rem 0 1.5rem;
  color: var(--vp-c-text-2);
  font-size: 1rem;
  line-height: 1.65;
}

.home-choose-path__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.home-choose-path__card {
  display: block;
  padding: 1.3rem 1.3rem 1.4rem;
  border-radius: 20px;
  border: 1px solid var(--opensin-home-card-border);
  background: var(--opensin-home-card-bg);
  box-shadow: var(--opensin-home-card-shadow);
  text-decoration: none;
  transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
}

.home-choose-path__card:hover {
  transform: translateY(-3px);
  border-color: var(--opensin-home-card-border-strong);
  box-shadow: var(--opensin-home-card-shadow-hover);
}

.home-choose-path__card.is-highlight {
  background: var(--opensin-home-card-bg-highlight);
}

.home-choose-path__label {
  display: inline-flex;
  align-items: center;
  min-height: 1.7rem;
  margin-bottom: 0.95rem;
  padding: 0.2rem 0.65rem;
  border-radius: 999px;
  background: var(--opensin-home-pill-bg);
  color: var(--opensin-home-accent-text);
  font-size: 0.77rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.home-choose-path__heading {
  color: var(--vp-c-text-1);
  font-size: 1.16rem;
  font-weight: 750;
  line-height: 1.3;
}

.home-choose-path__description {
  margin-top: 0.55rem;
  color: var(--vp-c-text-2);
  font-size: 0.98rem;
  line-height: 1.6;
}

.home-choose-path__arrow {
  margin-left: 0.4rem;
  color: var(--opensin-home-accent-text);
}

@media (max-width: 720px) {
  .home-choose-path {
    margin-top: 3rem;
  }

  .home-choose-path__grid {
    grid-template-columns: 1fr;
  }
}
</style>
