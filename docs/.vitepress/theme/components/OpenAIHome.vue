<script setup>
/**
 * OpenAIHome.vue - Billion Dollar Restoration v2
 * Based on professional design audit.
 * Implements ResourceCard component and strict 8px spacing.
 */
</script>

<template>
  <div class="oa-page">
    <div class="oa-container">
      <!-- Hero Section -->
      <section class="oa-hero">
        <h1 class="oa-hero__title">OpenSIN für Entwickler</h1>
        <p class="oa-hero__subtitle">
          Dokumente und Ressourcen, die Ihnen helfen, mit der Neural-Bus API
          autonome Agenten-Flotten zu bauen und zu steuern.
        </p>
      </section>

      <!-- Announcement Bar -->
      <div class="oa-announcement">
        <a href="/guide/whats-new" class="oa-announcement-card">
          <div class="oa-ann-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <div class="oa-ann-content">
            <span class="oa-ann-tag">Neu</span>
            <span class="oa-ann-text">OpenSIN Core v2.0 Standard – Native n8n Integration & Stealth-Biometrics</span>
          </div>
          <div class="oa-ann-arrow">→</div>
        </a>
      </div>

      <!-- Main Feature Grid (Image 2 Top) -->
      <div class="oa-grid oa-grid--3">
        <a href="/api/" class="feature-tile feature-tile--light">
           <div class="feature-tile__icon">
             <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
           </div>
           <div class="feature-tile__body">
             <h3>Neural-Bus API</h3>
             <p>Nutzen Sie unsere APIs und Modelle, um Ihre eigenen KI-Erlebnisse zu entwickeln.</p>
           </div>
        </a>

        <a href="/guide/opensin-code" class="feature-tile feature-tile--gradient">
           <div class="feature-tile__icon feature-tile__icon--white">
             <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
           </div>
           <div class="feature-tile__body">
             <h3>OpenCode CLI</h3>
             <p>Der autonome Entwickler-Agent für dein Terminal. Schneller entwickeln und validieren.</p>
           </div>
        </a>

        <a href="/guide/a2a-protocol" class="feature-tile feature-tile--light">
           <div class="feature-tile__icon">
             <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
           </div>
           <div class="feature-tile__body">
             <h3>A2A Protocol</h3>
             <p>Standardisierte Protokolle für Agent-to-Agent Interaktionen auf dem Neural-Bus.</p>
           </div>
        </a>
      </div>

      <!-- Recommended Section -->
      <section class="oa-section">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Empfohlen</h2>
        </div>
        <div class="oa-grid oa-grid--3">
          <ResourceCard 
            title="Erste Schritte mit Kairos" 
            description="Lernen Sie, wie Sie hochperformante Agent-Loops mit Kairos orchestrieren." 
            link="/tutorials/agent-basics"
            meta="Tutorial"
            imageClass="bg-sin-blue"
          />
          <ResourceCard 
            title="Building Custom MCP Servers" 
            description="Eigene Datenquellen und Tools über das Model Context Protocol anbinden." 
            link="/best-practices/mcp-integration"
            meta="Entwicklung"
            imageClass="bg-sin-green"
          />
          <ResourceCard 
            title="Fleet Orchestration Patterns" 
            description="Best Practices für die Verwaltung von 100+ autonomen Agenten-Instanzen." 
            link="/guide/team-orchestration"
            meta="Führung"
            imageClass="bg-sin-orange"
          />
        </div>
      </section>

      <!-- Latest Section -->
      <section class="oa-section">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Letzte Updates</h2>
          <a href="/guide/changelog" class="oa-view-all">Alle anzeigen →</a>
        </div>
        <div class="oa-latest-list">
          <a href="/best-practices/browser-automation" class="latest-item">
            <div class="latest-item__icon latest-item__icon--green">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            </div>
            <div class="latest-item__content">
              <h4>Behavioral Biometrics Guide</h4>
              <p>Menschliches Verhalten simulieren für Stealth-Automatisierung.</p>
              <span class="latest-item__meta">Best Practices</span>
            </div>
          </a>
          <a href="/tutorials/ci-cd-n8n" class="latest-item">
            <div class="latest-item__icon latest-item__icon--green">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            </div>
            <div class="latest-item__content">
              <h4>n8n Workflow Automation</h4>
              <p>Verbinden Sie Agenten mit Enterprise Workflows.</p>
              <span class="latest-item__meta">Tutorial</span>
            </div>
          </a>
        </div>
      </section>

      <!-- Explore Blocks -->
      <section class="oa-section">
        <div class="oa-section-header">
          <h2 class="oa-section-title">Erkunden</h2>
        </div>
        <div class="oa-grid oa-grid--3">
          <a href="https://blog.opensin.ai" class="explore-block explore-block--blog">
             <div class="explore-block__icon">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path></svg>
             </div>
             <span>Engineering Blog</span>
          </a>
          <a href="/guide/getting-started" class="explore-block explore-block--resources">
             <div class="explore-block__icon">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"></path></svg>
             </div>
             <span>Onboarding Ressourcen</span>
          </a>
          <a href="/examples/hello-world" class="explore-block explore-block--cookbook">
             <div class="explore-block__icon">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg>
             </div>
             <span>OpenSIN Cookbook</span>
          </a>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.oa-page {
  background: #ffffff;
  min-height: 100vh;
  padding-bottom: 120px;
}

.oa-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

/* Hero Section */
.oa-hero {
  padding: 80px 0 64px;
  text-align: center;
}

.oa-hero__title {
  font-size: 3.5rem;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.04em;
  margin-bottom: 16px;
}

.oa-hero__subtitle {
  font-size: 1.25rem;
  color: #4b5563;
  max-width: 680px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Announcement Bar */
.oa-announcement {
  margin-bottom: 48px;
}

.oa-announcement-card {
  display: flex;
  align-items: center;
  padding: 12px 24px;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 99px;
  text-decoration: none;
  color: inherit;
  transition: all 0.2s ease;
  width: fit-content;
  margin: 0 auto;
}

.oa-announcement-card:hover {
  border-color: #00cc88;
  background: #f9fafb;
}

.oa-ann-tag {
  background: #ecfdf5;
  color: #059669;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 99px;
  margin-right: 12px;
  text-transform: uppercase;
}

.oa-ann-text {
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
}

.oa-ann-arrow {
  margin-left: 12px;
  color: #9ca3af;
}

/* Grids */
.oa-grid {
  display: grid;
  gap: 24px;
}

.oa-grid--3 {
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
}

/* Feature Tiles */
.feature-tile {
  padding: 40px;
  border-radius: 16px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
  height: 240px;
}

.feature-tile--light {
  background: #f9fafb;
  border: 1px solid #f3f4f6;
}

.feature-tile--light:hover {
  background: #f3f4f6;
  transform: translateY(-4px);
}

.feature-tile--gradient {
  background: linear-gradient(135deg, #008060 0%, #00cc88 100%);
  color: #ffffff;
}

.feature-tile--gradient:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 204, 136, 0.15);
}

.feature-tile__icon {
  margin-bottom: 32px;
  color: #111827;
}

.feature-tile__icon--white { color: #ffffff; }

.feature-tile h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: -0.02em;
}

.feature-tile p {
  font-size: 1rem;
  line-height: 1.5;
  opacity: 0.85;
}

/* Sections */
.oa-section {
  margin-top: 88px;
}

.oa-section-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 32px;
  padding-bottom: 16px;
  border-bottom: 1px solid #f3f4f6;
}

.oa-section-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
}

.oa-view-all {
  font-size: 0.9375rem;
  font-weight: 600;
  color: #00cc88;
  text-decoration: none;
}

/* Latest List */
.oa-latest-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 32px;
}

.latest-item {
  display: flex;
  gap: 24px;
  text-decoration: none;
  color: inherit;
  padding: 16px;
  border-radius: 12px;
  transition: background 0.2s ease;
}

.latest-item:hover {
  background: #f9fafb;
}

.latest-item__icon {
  width: 48px;
  height: 48px;
  background: #00cc88;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.latest-item__content h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 4px;
}

.latest-item__content p {
  font-size: 0.9375rem;
  color: #4b5563;
  margin-bottom: 8px;
}

.latest-item__meta {
  font-size: 0.75rem;
  font-weight: 600;
  color: #9ca3af;
  text-transform: uppercase;
}

/* Explore Blocks */
.explore-block {
  height: 200px;
  border-radius: 16px;
  background: #f9fafb;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 32px;
  text-decoration: none;
  color: #111827;
  font-weight: 600;
  font-size: 1.125rem;
  position: relative;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.explore-block:hover {
  border-color: #00cc88;
  background: #ffffff;
  box-shadow: 0 8px 24px rgba(0, 204, 136, 0.08);
  transform: scale(1.02);
}

.explore-block__icon {
  position: absolute;
  top: 32px;
  left: 32px;
  width: 48px;
  height: 48px;
  background: #ffffff;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

@media (max-width: 768px) {
  .oa-hero__title { font-size: 2.5rem; }
  .oa-container { padding: 0 24px; }
  .oa-latest-list { grid-template-columns: 1fr; }
}
</style>
