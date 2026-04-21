<script setup>
/**
 * OpenAIDocs.vue - Branded with OpenSIN Green
 * Billion Dollar Restoration & Content Filling
 */
</script>

<template>
  <div class="oad-layout">
    <!-- Sidebar -->
    <aside class="oad-sidebar">
      <div class="oad-sidebar__section">
        <h6>Los geht's!</h6>
        <ul>
          <li class="is-active">Überblick</li>
          <li>Schnellstart</li>
          <li>Agenten-Modelle</li>
          <li>API-Referenz</li>
          <li>Bibliotheken</li>
          <li>OpenCode CLI</li>
          <li>Neural-Bus Core</li>
        </ul>
      </div>
      <div class="oad-sidebar__section">
        <h6>Kernkonzepte</h6>
        <ul>
          <li>Neural-Bus Relay</li>
          <li>A2A Kommunikation</li>
          <li>Behavioral Biometrics</li>
          <li>Stealth Browsing</li>
          <li>Strukturierte A2A-Daten</li>
          <li>Tool-Orchestrierung</li>
          <li>Relay API</li>
          <li>OpenSIN Skills</li>
        </ul>
      </div>
      <div class="oad-sidebar__section">
        <h6>OpenSIN SDK</h6>
        <ul>
          <li>Übersicht</li>
          <li>Python SDK</li>
          <li>TypeScript SDK</li>
        </ul>
      </div>
    </aside>

    <!-- Content Area -->
    <main class="oad-main">
      <header class="oad-header">
        <h1>Neural-Bus API</h1>
      </header>

      <!-- Schnellstart Card -->
      <section class="oad-schnellstart">
        <div class="oad-schnellstart__body">
          <h3>Entwickler-Schnellstart</h3>
          <p>Senden Sie Ihre erste A2A-Anfrage in wenigen Sekunden. Orchestrieren Sie autonome Flotten über den OpenSIN Neural-Bus.</p>
          <div class="oad-schnellstart__actions">
            <button class="oa-btn oa-btn--black">Jetzt starten</button>
            <button class="oa-btn oa-btn--grey">API-Dashboard</button>
          </div>
        </div>
        <div class="oad-code">
          <div class="oad-code__header">
            <span>Javascript / Node.js</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          </div>
          <pre><code><span class="c-k">import</span> { OpenSIN } <span class="c-k">from</span> <span class="c-s">"@opensin/sdk"</span>;
<span class="c-k">const</span> sin = <span class="c-k">new</span> OpenSIN();

<span class="c-k">const</span> task = <span class="c-k">await</span> sin.fleet.dispatch({
  agent: <span class="c-s">"core-executor-01"</span>,
  input: <span class="c-s">"Build a dashboard for A2A monitoring"</span>,
  priority: <span class="c-s">"high"</span>
});

console.log(task.status);</code></pre>
        </div>
      </section>

      <!-- Pfade erstellen -->
      <section class="oad-section">
        <h2 class="oad-section__title">Integrationen bauen</h2>
        <div class="oad-path-grid">
          <div class="oad-path-card">
            <h4>Neural-Bus Relay</h4>
            <p>Echtzeit-Event-Streaming für Agenten-Kommunikation. Hohe Durchsatzraten und geringe Latenz.</p>
            <span class="oad-path-card__link">Relay-Dokumentation lesen ↗</span>
          </div>
          <div class="oad-path-card">
            <h4>OpenCode SDK</h4>
            <p>Entwickeln Sie eigene Agenten mit nativem Zugriff auf das Global-Brain und den Neural-Bus.</p>
            <span class="oad-path-card__link">SDK-Referenz öffnen ↗</span>
          </div>
        </div>
      </section>

      <!-- Modelle -->
      <section class="oad-section">
        <div class="oad-section__header">
          <h2 class="oad-section__title">Agenten-Modelle</h2>
          <a href="/guide/agent-discovery" class="oa-link">Alle anzeigen</a>
        </div>
        <p class="oad-section__subtitle">Wählen Sie das passende Basis-Modell für Ihre Agenten-Instanzen. Von leichtgewichtigen Task-Runnern bis hin zu komplexen Reasoning-Nodes.</p>
        
        <div class="oad-model-grid">
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--green">
              <span>sin-core</span>
            </div>
            <div class="oad-model-card__body">
              <h5>SIN Core 1.0 <span class="badge">Standard</span></h5>
              <p>Optimiert für komplexe multi-agenten Orchestrierung und langfristige Task-Planung.</p>
            </div>
          </div>
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--blue">
              <span>sin-fast</span>
            </div>
            <div class="oad-model-card__body">
              <h5>SIN Fast-Link <span class="badge">Speed</span></h5>
              <p>Unser reaktionsschnellstes Modell für einfache Tool-Calls und schnelles Daten-Relaying.</p>
            </div>
          </div>
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--orange">
              <span>sin-stealth</span>
            </div>
            <div class="oad-model-card__body">
              <h5>SIN Stealth-Ops <span class="badge">Security</span></h5>
              <p>Spezialisiert auf Behavioral Biometrics und Umgehung von Bot-Detection-Systemen.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Building Grid -->
      <section class="oad-section">
        <h2 class="oad-section__title">OpenSIN Ökosystem</h2>
        <div class="oad-building-grid">
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
             <div>
               <h6>A2A Kommunikation</h6>
               <p>Lassen Sie Ihre Agenten direkt miteinander sprechen und Aufgaben delegieren.</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
             <div>
               <h6>Behavioral Analytics</h6>
               <p>Integrieren Sie menschliche Interaktionsmuster in Ihre automatisierten Abläufe.</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
             <div>
               <h6>Stealth Vision ↗</h6>
               <p>KI-gestützte Bildanalyse ohne Spuren im Web-Traffic zu hinterlassen.</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00cc88" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg></div>
             <div>
               <h6>Voice Fleet Control</h6>
               <p>Steuern Sie Ihre Agenten-Flotte per Sprachbefehl über verschlüsselte A2A-Kanäle.</p>
             </div>
           </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
.oad-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
  background: #ffffff;
}

.oad-sidebar {
  padding: 40px 24px;
  background: #f9f9f9;
  border-right: 1px solid #e5e5e7;
}

.oad-sidebar__section {
  margin-bottom: 32px;
}

.oad-sidebar h6 {
  font-size: 13px;
  font-weight: 600;
  color: #1d1d1f;
  margin-bottom: 12px;
  padding-left: 12px;
}

.oad-sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.oad-sidebar li {
  padding: 8px 12px;
  font-size: 14px;
  color: #6e6e73;
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.oad-sidebar li:hover {
  color: #00cc88;
  background: rgba(0, 204, 136, 0.05);
}

.oad-sidebar li.is-active {
  color: #000000;
  background: #e5e5e7;
  font-weight: 500;
}

.oad-main {
  padding: 48px 60px;
  max-width: 1000px;
}

.oad-header h1 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 40px;
}

.oad-schnellstart {
  display: flex;
  background: #f5f5f7;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 60px;
}

.oad-schnellstart__body {
  flex: 1;
  padding: 40px;
}

.oad-schnellstart h3 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 16px;
}

.oad-schnellstart p {
  font-size: 16px;
  color: #6e6e73;
  line-height: 1.5;
  margin-bottom: 32px;
}

.oad-schnellstart__actions {
  display: flex;
  gap: 12px;
}

.oa-btn {
  padding: 10px 20px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.2s ease;
}

.oa-btn--black {
  background: #000000;
  color: #ffffff;
}

.oa-btn--black:hover {
  background: #333333;
}

.oa-btn--grey {
  background: #e5e5e7;
  color: #000000;
}

.oad-code {
  flex: 1.2;
  background: #000000;
  color: #ffffff;
  padding: 24px;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  position: relative;
}

.oad-code__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #86868b;
  margin-bottom: 16px;
}

.oad-code pre { margin: 0; }
.c-k { color: #00cc88; } /* Changed to Green */
.c-s { color: #8ec5fc; }

.oad-section {
  margin-bottom: 80px;
}

.oad-section__title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
}

.oad-section__subtitle {
  font-size: 15px;
  color: #6e6e73;
  margin-bottom: 32px;
  line-height: 1.5;
}

.oad-path-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.oad-path-card {
  padding: 32px;
  border: 1px solid #e5e5e7;
  border-radius: 12px;
  transition: all 0.2s ease;
}

.oad-path-card:hover {
  border-color: #00cc88;
  box-shadow: 0 4px 12px rgba(0, 204, 136, 0.08);
}

.oad-path-card h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
}

.oad-path-card p {
  font-size: 14px;
  color: #6e6e73;
  line-height: 1.5;
  margin-bottom: 24px;
}

.oad-path-card__link {
  font-size: 14px;
  font-weight: 600;
  color: #00cc88;
}

.oad-model-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.oad-model-card__img {
  height: 180px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 16px;
}

.oad-model-card__img--green { background: linear-gradient(135deg, #008060 0%, #00cc88 100%); }
.oad-model-card__img--blue { background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); }
.oad-model-card__img--orange { background: linear-gradient(135deg, #008060 0%, #00ffaa 100%); }

.oad-model-card h5 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.badge {
  background: #e8f5e9;
  color: #2e7d32;
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}

.oad-model-card p {
  font-size: 13px;
  color: #6e6e73;
  line-height: 1.4;
}

.oad-building-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.oad-building-item {
  display: flex;
  gap: 16px;
}

.oad-building-item__icon {
  width: 40px;
  height: 40px;
  background: #f5f5f7;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.oad-building-item h6 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
}

.oad-building-item p {
  font-size: 13px;
  color: #6e6e73;
  line-height: 1.4;
}
</style>

<style scoped>
.oad-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
  background: #ffffff;
}

.oad-sidebar {
  padding: 40px 24px;
  background: #f9f9f9;
  border-right: 1px solid #e5e5e7;
}

.oad-sidebar__section {
  margin-bottom: 32px;
}

.oad-sidebar h6 {
  font-size: 13px;
  font-weight: 600;
  color: #1d1d1f;
  margin-bottom: 12px;
  padding-left: 12px;
}

.oad-sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.oad-sidebar li {
  padding: 8px 12px;
  font-size: 14px;
  color: #6e6e73;
  cursor: pointer;
  border-radius: 6px;
}

.oad-sidebar li:hover {
  color: #000000;
  background: #f0f0f2;
}

.oad-sidebar li.is-active {
  color: #000000;
  background: #e5e5e7;
  font-weight: 500;
}

.oad-main {
  padding: 48px 60px;
  max-width: 1000px;
}

.oad-header h1 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 40px;
}

.oad-schnellstart {
  display: flex;
  background: #f5f5f7;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 60px;
}

.oad-schnellstart__body {
  flex: 1;
  padding: 40px;
}

.oad-schnellstart h3 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 16px;
}

.oad-schnellstart p {
  font-size: 16px;
  color: #6e6e73;
  line-height: 1.5;
  margin-bottom: 32px;
}

.oad-schnellstart__actions {
  display: flex;
  gap: 12px;
}

.oa-btn {
  padding: 10px 20px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
}

.oa-btn--black {
  background: #000000;
  color: #ffffff;
}

.oa-btn--grey {
  background: #e5e5e7;
  color: #000000;
}

.oad-code {
  flex: 1.2;
  background: #000000;
  color: #ffffff;
  padding: 24px;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  position: relative;
}

.oad-code__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #86868b;
  margin-bottom: 16px;
}

.oad-code pre { margin: 0; }
.c-k { color: #d19a66; }
.c-s { color: #98c379; }

.oad-section {
  margin-bottom: 80px;
}

.oad-section__title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
}

.oad-section__subtitle {
  font-size: 15px;
  color: #6e6e73;
  margin-bottom: 32px;
  line-height: 1.5;
}

.oad-path-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.oad-path-card {
  padding: 32px;
  border: 1px solid #e5e5e7;
  border-radius: 12px;
}

.oad-path-card h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
}

.oad-path-card p {
  font-size: 14px;
  color: #6e6e73;
  line-height: 1.5;
  margin-bottom: 24px;
}

.oad-path-card__link {
  font-size: 14px;
  font-weight: 600;
  color: #000000;
}

.oad-model-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.oad-model-card__img {
  height: 180px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 16px;
}

.oad-model-card__img--pollen { background: linear-gradient(135deg, #fceabb 0%, #f8b500 100%); }
.oad-model-card__img--rose { background: linear-gradient(135deg, #f8ceec 0%, #a88beb 100%); }
.oad-model-card__img--ocean { background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); }

.oad-model-card h5 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.badge {
  background: #e8f5e9;
  color: #2e7d32;
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}

.oad-model-card p {
  font-size: 13px;
  color: #6e6e73;
  line-height: 1.4;
}

.oad-building-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.oad-building-item {
  display: flex;
  gap: 16px;
}

.oad-building-item__icon {
  width: 40px;
  height: 40px;
  background: #f5f5f7;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1d1d1f;
}

.oad-building-item h6 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
}

.oad-building-item p {
  font-size: 13px;
  color: #6e6e73;
  line-height: 1.4;
}
</style>
