<script setup>
import { useData } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

const { Layout } = DefaultTheme
const { frontmatter } = useData()
</script>

<template>
  <Layout v-if="frontmatter.layout !== 'openai-home' && frontmatter.layout !== 'openai-docs'">
    <template #nav-bar-content-before>
       <!-- Custom Logo or Nav if needed -->
    </template>
  </Layout>

  <div v-else class="openai-theme">
    <!-- OpenAI Style Header Branded for OpenSIN -->
    <header class="oa-nav">
      <div class="oa-nav__container">
        <div class="oa-nav__left">
          <a href="/" class="oa-nav__logo">
             <img src="/logo.png" alt="OpenSIN" style="height: 24px; margin-right: 8px;" />
             <strong>Developers</strong>
          </a>
          <nav class="oa-nav__links">
            <a href="/">Heim</a>
            <div class="oa-nav__dropdown">API <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
            <div class="oa-nav__dropdown">OpenCode <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
            <div class="oa-nav__dropdown">Fleet <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
            <div class="oa-nav__dropdown">Ressourcen <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
          </nav>
        </div>
        <div class="oa-nav__right">
          <div class="oa-nav__search">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" placeholder="Suche starten" />
          </div>
          <a href="https://chat.opensin.ai" class="oa-nav__btn">Fleet-Dashboard ↗</a>
          <div class="oa-nav__mode">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="18.36" x2="5.64" y2="16.93"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="oa-main-content">
      <Content />
    </main>
  </div>
</template>

<style>
.openai-theme {
  background: #ffffff;
  color: #000000;
  min-height: 100vh;
}

.oa-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #ffffff;
  border-bottom: 1px solid #e5e5e7;
  padding: 12px 0;
}

.oa-nav__container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.oa-nav__left, .oa-nav__right {
  display: flex;
  align-items: center;
  gap: 32px;
}

.oa-nav__logo {
  font-size: 18px;
  text-decoration: none;
  color: #000000;
}

.oa-nav__links {
  display: flex;
  gap: 20px;
  font-size: 14px;
}

.oa-nav__links a, .oa-nav__dropdown {
  color: #6e6e73;
  text-decoration: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
}

.oa-nav__links a:hover, .oa-nav__dropdown:hover {
  color: #00cc88; /* OpenSIN Green */
}

.oa-nav__search {
  display: flex;
  align-items: center;
  background: #f5f5f7;
  border-radius: 8px;
  padding: 6px 12px;
  gap: 8px;
  width: 240px;
}

.oa-nav__search input {
  background: transparent;
  border: none;
  font-size: 14px;
  width: 100%;
  outline: none;
}

.oa-nav__btn {
  background: #000000;
  color: #ffffff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s ease;
}

.oa-nav__btn:hover {
  background: #00cc88;
}

.oa-nav__mode {
  color: #86868b;
  cursor: pointer;
}

.oa-nav__mode:hover {
  color: #00cc88;
}

.oa-main-content {
  /* Prevent VitePress default padding if needed */
}
</style>
