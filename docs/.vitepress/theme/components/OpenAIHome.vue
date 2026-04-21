<script setup>
// OpenAIHome.vue - 1:1 Pixel Perfect Clone for docs.opensin.ai
</script>

<template>
  <div class="oa-container">
    <!-- Hero Section -->
    <section class="oa-hero">
      <h1 class="oa-hero__title">OpenSIN für Entwickler</h1>
      <p class="oa-hero__subtitle">
        Dokumente und Ressourcen, die Ihnen helfen, mit, für und auf OpenSIN
        zu entwickeln.
      </p>
    </section>

    <!-- Announcement Bar -->
    <div class="oa-announcement">
      <div class="oa-announcement__card">
        <div class="oa-announcement__icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        </div>
        <div class="oa-announcement__content">
          <strong>Neu: Sandbox-Agenten im Agenten-SDK</strong>
          <span>Agenten in containerbasierten Umgebungen mit Dateien, Befehlen, Fähigkeiten, Snapshots und Speicher ausführen.</span>
        </div>
        <div class="oa-announcement__arrow">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
      </div>
    </div>

    <!-- Top Grid -->
    <div class="oa-top-grid">
      <div class="oa-card oa-card--simple">
        <div class="oa-card__icon-top">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
        </div>
        <h3>API-Plattform</h3>
        <p>Nutzen Sie unsere APIs und Modelle, um Ihre eigenen KI-Erlebnisse zu entwickeln.</p>
      </div>

      <div class="oa-card oa-card--gradient">
        <div class="oa-card__icon-top oa-card__icon-top--white">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <h3>Kodex</h3>
        <p>Mit unserem Codierungsagenten können Sie schneller entwickeln und veröffentlichen – überall dort, wo Sie arbeiten.</p>
      </div>

      <div class="oa-card oa-card--simple">
        <div class="oa-card__icon-top">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        </div>
        <h3>Apps SDK</h3>
        <p>Erweitern Sie ChatGPT mit Ihren Anwendungen, die auf dem Model Context Protocol aufbauen.</p>
      </div>
    </div>

    <!-- Recommended Section -->
    <section class="oa-section">
      <div class="oa-section__header">
        <h2 class="oa-section__title">Empfohlen</h2>
      </div>
      <div class="oa-recommended">
        <div class="oa-recommended__content">
          <!-- Empfohlen Cards Grid (Left side in image is just text title, right side is cards) -->
          <!-- Actually Image 2 shows "Empfohlen" as a grid with large images -->
        </div>
        <div class="oa-recommended__grid">
          <div class="oa-image-card">
            <div class="oa-image-card__img oa-image-card__img--blue">
               <svg width="40" height="40" viewBox="0 0 24 24" fill="white" style="opacity: 0.5"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            </div>
            <div class="oa-image-card__body">
              <h4>Beispiele für das Apps SDK</h4>
              <div class="oa-image-card__meta">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                <span>Code</span>
                <span>•</span>
                <span>6. Oktober 2025</span>
              </div>
            </div>
          </div>
          <div class="oa-image-card">
            <div class="oa-image-card__img oa-image-card__img--light-blue">
               <svg width="40" height="40" viewBox="0 0 24 24" fill="white" style="opacity: 0.5"><circle cx="12" cy="12" r="10"></circle></svg>
            </div>
            <div class="oa-image-card__body">
              <h4>ChatKit-Starter-App</h4>
              <div class="oa-image-card__meta">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                <span>Code</span>
                <span>•</span>
                <span>6. Oktober 2025</span>
              </div>
            </div>
          </div>
          <div class="oa-image-card">
            <div class="oa-image-card__img oa-image-card__img--orange">
               <svg width="40" height="40" viewBox="0 0 24 24" fill="white" style="opacity: 0.5"><rect x="3" y="4" width="18" height="16" rx="2"></rect><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            </div>
            <div class="oa-image-card__body">
              <h4>Agentic Commerce Protocol</h4>
              <div class="oa-image-card__meta">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                <span>Führung</span>
                <span>•</span>
                <span>29. September 2025</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Latest Section -->
    <section class="oa-section">
      <div class="oa-section__header">
        <h2 class="oa-section__title">Letzte</h2>
        <a href="#" class="oa-link">Alle anzeigen</a>
      </div>
      <div class="oa-latest-grid">
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--purple">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Sora 2 Prompting Guide</h5>
            <p>Kochbuch zur Erstellung effektiver Video-Instrumente für die Sora 2-Generation.</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
               <span>Kochbuch</span>
            </div>
          </div>
        </div>
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--purple">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Codex-Leitfaden für Gesprächsanregungen</h5>
            <p>Codex-Modelle erweitern die Grenzen von Intelligenz und Effizienz und unser empfohlenes agentenbasiertes...</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
               <span>Kochbuch</span>
            </div>
          </div>
        </div>
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--yellow">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Wir stellen die Codex-App vor.</h5>
            <p>Sehen Sie die Codex-App in Aktion und erfahren Sie, wie sie Ihnen hilft, schneller zu entwickeln und zu liefern.</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
               <span>Video</span>
            </div>
          </div>
        </div>
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--yellow">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Codex in JetBrains IDEs</h5>
            <p>Wie man Codex in JetBrains IDEs wie Rider, IntelliJ, PyCharm und WebStorm verwendet.</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
               <span>Video</span>
            </div>
          </div>
        </div>
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--orange">
             <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Docs MCP</h5>
            <p>Suchen und lesen Sie die Entwicklerdokumentation von OpenAI direkt in Ihrem Editor mithilfe von MCP.</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
               <span>Führung</span>
            </div>
          </div>
        </div>
        <div class="oa-list-item">
          <div class="oa-list-item__icon oa-list-item__icon--purple">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <div class="oa-list-item__body">
            <h5>Gpt-image-1.5 Prompting Guide</h5>
            <p>Anleitung zur zuverlässigen Bildgenerierung mit gpt-image-1.5.</p>
            <div class="oa-image-card__meta">
               <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
               <span>Kochbuch</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Explore Section -->
    <section class="oa-section">
      <div class="oa-section__header">
        <h2 class="oa-section__title">Erkunden</h2>
      </div>
      <div class="oa-explore-grid">
        <div class="oa-explore-card oa-explore-card--blog">
          <div class="oa-explore-card__icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg>
          </div>
          <span class="oa-explore-card__label">Blog</span>
        </div>
        <div class="oa-explore-card oa-explore-card--resources">
          <div class="oa-explore-card__icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"></path><path d="M4 6v12c0 1.1.9 2 2 2h14v-4"></path><path d="M18 12a2 2 0 0 0-2 2c0 1.1.9 2 2 2h4v-4h-4z"></path></svg>
          </div>
          <span class="oa-explore-card__label">Ressourcen</span>
        </div>
        <div class="oa-explore-card oa-explore-card--cookbook">
          <div class="oa-explore-card__icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <span class="oa-explore-card__label">Kochbuch</span>
        </div>
      </div>
    </section>

    <!-- Footer Icons Section -->
    <div class="oa-footer-grid">
      <div class="oa-footer-item">
        <div class="oa-footer-item__icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="3"></circle></svg>
        </div>
        <h6>Hilfezentrum</h6>
        <p>Häufig gestellte Fragen zu Konto und Abrechnung</p>
      </div>
      <div class="oa-footer-item">
        <div class="oa-footer-item__icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        </div>
        <h6>Entwicklerforum</h6>
        <p>Diskutieren Sie Themen mit anderen Entwicklern</p>
      </div>
      <div class="oa-footer-item">
        <div class="oa-footer-item__icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </div>
        <h6>OpenSIN für Startups</h6>
        <p>Ressourcen für ambitionierte Gründer, die mit OpenSIN entwickeln</p>
      </div>
      <div class="oa-footer-item">
        <div class="oa-footer-item__icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
        </div>
        <h6>Status</h6>
        <p>Überprüfen Sie den Status der OpenSIN-Dienste</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.oa-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 24px 100px;
  background: #ffffff;
  color: #000000;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.oa-hero {
  text-align: center;
  margin-bottom: 60px;
}

.oa-hero__title {
  font-size: 48px;
  font-weight: 500;
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}

.oa-hero__subtitle {
  font-size: 18px;
  color: #6e6e73;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.5;
}

.oa-announcement {
  margin-bottom: 32px;
}

.oa-announcement__card {
  display: flex;
  align-items: center;
  padding: 16px 24px;
  background: #ffffff;
  border: 1px solid #e5e5e7;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.oa-announcement__card:hover {
  background: #f5f5f7;
}

.oa-announcement__icon {
  margin-right: 16px;
  color: #1d1d1f;
}

.oa-announcement__content {
  flex: 1;
  font-size: 14px;
  line-height: 1.4;
}

.oa-announcement__content strong {
  display: block;
  font-weight: 600;
  margin-bottom: 2px;
}

.oa-announcement__content span {
  color: #6e6e73;
}

.oa-announcement__arrow {
  margin-left: 16px;
  color: #86868b;
}

.oa-top-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 60px;
}

.oa-card {
  padding: 32px;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.oa-card--simple {
  background: #f5f5f7;
  border: 1px solid transparent;
}

.oa-card--simple:hover {
  background: #e5e5e7;
}

.oa-card--gradient {
  background: linear-gradient(135deg, #a88beb 0%, #f8ceec 100%);
  color: #ffffff;
}

.oa-card--gradient:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}

.oa-card__icon-top {
  margin-bottom: 24px;
  color: #1d1d1f;
}

.oa-card__icon-top--white {
  color: #ffffff;
}

.oa-card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 12px;
}

.oa-card p {
  font-size: 15px;
  line-height: 1.5;
  opacity: 0.9;
}

.oa-card--simple p {
  color: #6e6e73;
}

.oa-section {
  margin-bottom: 80px;
}

.oa-section__header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 24px;
}

.oa-section__title {
  font-size: 24px;
  font-weight: 600;
}

.oa-link {
  font-size: 14px;
  color: #0066cc;
  text-decoration: none;
}

.oa-recommended {
  display: flex;
  gap: 40px;
}

.oa-recommended__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  flex: 1;
}

.oa-image-card {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e5e5e7;
  transition: transform 0.2s ease;
  cursor: pointer;
}

.oa-image-card:hover {
  transform: translateY(-4px);
}

.oa-image-card__img {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.oa-image-card__img--blue { background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%); }
.oa-image-card__img--light-blue { background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); }
.oa-image-card__img--orange { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }

.oa-image-card__body {
  padding: 20px;
}

.oa-image-card__body h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
}

.oa-image-card__meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #86868b;
}

.oa-latest-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.oa-list-item {
  display: flex;
  gap: 20px;
}

.oa-list-item__icon {
  width: 48px;
  height: 48px;
  min-width: 48px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.oa-list-item__icon--purple { background: #9b51e0; }
.oa-list-item__icon--yellow { background: #f2c94c; }
.oa-list-item__icon--orange { background: #f2994a; }

.oa-list-item__body h5 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
}

.oa-list-item__body p {
  font-size: 13px;
  color: #6e6e73;
  margin-bottom: 8px;
  line-height: 1.4;
}

.oa-explore-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.oa-explore-card {
  height: 240px;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 32px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s ease;
}

.oa-explore-card:hover {
  transform: scale(1.02);
}

.oa-explore-card--blog { background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); }
.oa-explore-card--resources { background: linear-gradient(135deg, #cfd9df 0%, #e2ebf0 100%); }
.oa-explore-card--cookbook { background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%); }

.oa-explore-card__icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #ffffff;
  width: 64px;
  height: 64px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.oa-explore-card__label {
  font-size: 18px;
  font-weight: 600;
  color: #1d1d1f;
}

.oa-footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  border-top: 1px solid #e5e5e7;
  padding-top: 60px;
}

.oa-footer-item {
  text-align: center;
}

.oa-footer-item__icon {
  margin: 0 auto 16px;
  color: #1d1d1f;
}

.oa-footer-item h6 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 8px;
}

.oa-footer-item p {
  font-size: 13px;
  color: #6e6e73;
  line-height: 1.4;
}
</style>
