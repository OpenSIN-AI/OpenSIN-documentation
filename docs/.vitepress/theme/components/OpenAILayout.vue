<script setup>
import { computed, inject } from 'vue'
import { useData } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

const { Layout } = DefaultTheme
const { frontmatter, isDark, theme } = useData()

const toggleAppearance = inject('toggle-appearance', () => {
  isDark.value = !isDark.value
})

const themeTitle = computed(() =>
  isDark.value
    ? theme.value.lightModeSwitchTitle || 'Switch to light theme'
    : theme.value.darkModeSwitchTitle || 'Switch to dark theme',
)

const navLinks = [
  { label: 'Home', href: '/', chevron: false },
  { label: 'API', href: '/api/', chevron: true },
  { label: 'OpenSIN Code', href: '/guide/opensin-code', chevron: true },
  { label: 'Chat', href: 'https://chat.opensin.ai', chevron: true },
  { label: 'Resources', href: '/guide/getting-started', chevron: true },
]

const footerLinks = [
  {
    icon: 'help',
    title: 'Help center',
    description: 'Frequently asked questions about account and billing',
    href: 'https://help.opensin.ai/',
  },
  {
    icon: 'forum',
    title: 'Developer forum',
    description: 'Discuss topics with other developers',
    href: 'https://community.opensin.ai/',
  },
  {
    icon: 'startups',
    title: 'OpenSIN for startups',
    description: 'Resources for ambitious founders building with OpenSIN',
    href: 'https://opensin.ai/startups',
  },
  {
    icon: 'status',
    title: 'Status',
    description: 'Check the status of OpenSIN services',
    href: 'https://status.opensin.ai/',
  },
]
</script>

<template>
  <Layout v-if="frontmatter.layout !== 'openai-home' && frontmatter.layout !== 'openai-docs'">
    <template #nav-bar-content-before />
  </Layout>

  <div v-else class="opensin-theme">
    <header class="oa-nav">
      <div class="oa-nav__container">
        <a href="/" class="oa-brand" aria-label="OpenSIN Developers home">
          <img src="/logo.svg" alt="OpenSIN Developers" class="oa-brand__logo" />
        </a>

        <nav class="oa-nav__links" aria-label="Primary navigation">
          <a v-for="link in navLinks" :key="link.label" :href="link.href">
            {{ link.label }}
            <span v-if="link.chevron" class="oa-nav__chevron" aria-hidden="true">▾</span>
          </a>
        </nav>

        <div class="oa-nav__actions">
          <button type="button" class="oa-nav__search" aria-label="Search docs">
            <span>Start searching</span>
            <span class="oa-nav__search-icon" aria-hidden="true">⌕</span>
          </button>

          <a href="https://chat.opensin.ai" class="oa-nav__cta">API Dashboard</a>

          <button
            type="button"
            class="oa-nav__theme"
            :aria-label="themeTitle"
            :title="themeTitle"
            :aria-pressed="isDark"
            @click="toggleAppearance"
          >
            <svg v-if="!isDark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <circle cx="12" cy="12" r="4.5" />
              <path d="M12 3.5v2" />
              <path d="M12 18.5v2" />
              <path d="M3.5 12h2" />
              <path d="M18.5 12h2" />
              <path d="M5.9 5.9l1.4 1.4" />
              <path d="M16.7 16.7l1.4 1.4" />
              <path d="M16.7 7.3l1.4-1.4" />
              <path d="M5.9 18.1l1.4-1.4" />
            </svg>
            <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M15.5 18.2A7.2 7.2 0 0 1 6.8 8.1c.6-.8 1.3-1.5 2.1-2.1a7.2 7.2 0 0 0 6.6 12.2Z" />
              <path d="M15.8 6.2h.01" />
              <path d="M18.5 8.7h.01" />
              <path d="M18.5 4.8h.01" />
            </svg>
          </button>
        </div>
      </div>
    </header>

    <main class="oa-main-content">
      <Content />
    </main>

    <footer class="oa-footer">
      <div class="oa-footer__container">
        <div class="oa-footer__grid">
          <a v-for="item in footerLinks" :key="item.title" :href="item.href" class="oa-footer__section">
            <span class="oa-footer__icon" aria-hidden="true">
              <svg v-if="item.icon === 'help'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <circle cx="12" cy="12" r="8.5" />
                <path d="M9.6 9.4a2.5 2.5 0 1 1 4.1 2c-.8.7-1.5 1-1.9 1.7-.1.2-.2.5-.2.9" />
                <circle cx="12" cy="17" r="0.75" fill="currentColor" stroke="none" />
              </svg>
              <svg v-else-if="item.icon === 'forum'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <circle cx="8" cy="9" r="2.2" />
                <circle cx="16" cy="9" r="2.2" />
                <path d="M4.5 18c.7-2.6 2.8-4 5.5-4s4.8 1.4 5.5 4" />
                <path d="M11 18c.5-2.2 2.1-3.3 4.4-3.3 1.2 0 2.2.3 3 .9" />
              </svg>
              <svg v-else-if="item.icon === 'startups'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <path d="M12 3l1.7 4.9L19 9.6l-5.3 1.8L12 16.4l-1.7-5L5 9.6l5.3-1.7L12 3z" />
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <path d="M4 13a8 8 0 0 1 16 0" />
                <path d="M7 13a5 5 0 0 1 10 0" />
                <path d="M10 13a2 2 0 0 1 4 0" />
                <circle cx="12" cy="16.5" r="1" fill="currentColor" stroke="none" />
              </svg>
            </span>
            <h4>{{ item.title }}</h4>
            <p>{{ item.description }}</p>
          </a>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
.opensin-theme {
  min-height: 100vh;
  background: #fff;
  color: #111827;
}

.oa-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.96);
  border-bottom: 1px solid #e5e7eb;
  backdrop-filter: blur(12px);
}

.oa-nav__container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 16px 40px;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 24px;
}

.oa-brand {
  display: inline-flex;
  align-items: center;
  gap: 0;
  color: #111827;
  text-decoration: none;
  white-space: nowrap;
  flex: 0 0 auto;
}

.oa-brand__logo {
  width: 160px;
  height: 17px;
  display: block;
}

.oa-nav__links {
  display: inline-flex;
  align-items: center;
  gap: 22px;
  justify-content: center;
  min-width: 0;
}

.oa-nav__links a {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #374151;
  text-decoration: none;
  font-size: 0.92rem;
  font-weight: 500;
}

.oa-nav__chevron {
  color: #9ca3af;
  font-size: 0.72rem;
  transform: translateY(1px);
}

.oa-nav__links a:hover {
  color: #111827;
}

.oa-nav__actions {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-self: end;
}

.oa-nav__search {
  width: 218px;
  min-height: 38px;
  padding: 0 14px;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 999px;
  border: 1px solid #e5e7eb;
  background: #ffffff;
  color: #6b7280;
  font-size: 0.92rem;
  font-weight: 500;
}

.oa-nav__search-icon {
  color: #9ca3af;
  font-size: 1rem;
  line-height: 1;
}

.oa-nav__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 999px;
  background: #111111;
  color: #ffffff;
  text-decoration: none;
  font-size: 0.92rem;
  font-weight: 600;
}

.oa-nav__cta::after {
  content: '↗';
  margin-left: 8px;
  font-size: 0.9rem;
  line-height: 1;
}

.oa-nav__theme {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background: #ffffff;
  color: #111827;
  cursor: pointer;
  transition: background-color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

.oa-nav__theme:hover {
  border-color: #d1d5db;
  background: #f9fafb;
  transform: translateY(-1px);
}

.oa-nav__theme svg {
  width: 16px;
  height: 16px;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.oa-nav__cta:hover {
  background: #2a2a2a;
}

.dark .oa-nav {
  background: rgba(10, 10, 10, 0.9);
  border-bottom-color: rgba(255, 255, 255, 0.08);
}

.dark .oa-nav__links a,
.dark .oa-nav__search,
.dark .oa-nav__theme,
.dark .oa-nav__cta,
.dark .oa-footer__section h4,
.dark .oa-footer__section p,
.dark .oa-footer__icon,
.dark .oa-brand {
  color: #ececf1;
}

.dark .oa-nav__search,
.dark .oa-nav__theme {
  background: #111111;
  border-color: #2a2a2a;
}

.dark .oa-nav__cta {
  background: #ececf1;
  color: #0a0a0a;
}

.dark .oa-nav__cta:hover {
  background: #ffffff;
}

.dark .oa-footer {
  background: #0a0a0a;
  border-top-color: rgba(255, 255, 255, 0.08);
}

.dark .oa-footer__section p {
  color: #9ca3af;
}

.oa-main-content {
  padding-top: 0;
}

.oa-footer {
  background: #ffffff;
  padding: 56px 0 32px;
  border-top: 1px solid #e5e7eb;
}

.oa-footer__container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 40px;
}

.oa-footer__grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 28px;
}

.oa-footer__section {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  text-decoration: none;
  color: inherit;
}

.oa-footer__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  margin-bottom: 14px;
  color: #111827;
}

.oa-footer__icon svg {
  width: 24px;
  height: 24px;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.oa-footer__section h4 {
  margin: 0 0 8px;
  color: #111827;
  font-size: 1rem;
  line-height: 1.3;
  font-weight: 600;
}

.oa-footer__section p {
  margin: 0;
  color: #6b7280;
  font-size: 0.88rem;
  line-height: 1.45;
}

@media (max-width: 1024px) {
  .oa-nav__container {
    display: flex;
    flex-wrap: wrap;
  }

  .oa-nav__links {
    order: 3;
    width: 100%;
  }

  .oa-nav__actions {
    margin-left: auto;
  }
}

@media (max-width: 860px) {
  .oa-nav__search {
    width: min(100%, 180px);
  }

  .oa-footer__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .oa-nav__container,
  .oa-footer__container {
    padding-left: 20px;
    padding-right: 20px;
  }

  .oa-nav__actions {
    width: 100%;
    flex-direction: column;
    align-items: stretch;
  }

  .oa-nav__search,
  .oa-nav__cta,
  .oa-nav__theme {
    width: 100%;
  }

  .oa-footer__grid {
    grid-template-columns: 1fr;
  }
}
</style>
