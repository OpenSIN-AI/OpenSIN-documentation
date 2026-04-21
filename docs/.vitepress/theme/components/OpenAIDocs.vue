<script setup>
// OpenAIDocs.vue - 1:1 Pixel Perfect Clone for docs.opensin.ai/api
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
          <li>Modelle</li>
          <li>Preisgestaltung</li>
          <li>Bibliotheken</li>
          <li>Aktuellste Version: GPT-5.4</li>
          <li>Schnelle Beratung</li>
        </ul>
      </div>
      <div class="oad-sidebar__section">
        <h6>Kernkonzepte</h6>
        <ul>
          <li>Textgenerierung</li>
          <li>Codegenerierung</li>
          <li>Bilder und Visionen</li>
          <li>Audio und Sprache</li>
          <li>Strukturierte Ausgabe</li>
          <li>Funktionsaufruf</li>
          <li>Responses API</li>
          <li>Werkzeuge verwenden</li>
        </ul>
      </div>
      <div class="oad-sidebar__section">
        <h6>Agenten-SDK</h6>
        <ul>
          <li>Überblick</li>
        </ul>
      </div>
    </aside>

    <!-- Content Area -->
    <main class="oad-main">
      <header class="oad-header">
        <h1>API-Plattform</h1>
      </header>

      <!-- Schnellstart Card -->
      <section class="oad-schnellstart">
        <div class="oad-schnellstart__body">
          <h3>Entwickler-Schnellstart</h3>
          <p>Stellen Sie Ihre erste API-Anfrage in wenigen Minuten. Lernen Sie die Grundlagen der OpenSIN-Plattform kennen.</p>
          <div class="oad-schnellstart__actions">
            <button class="oa-btn oa-btn--black">Los geht's!</button>
            <button class="oa-btn oa-btn--grey">API-Schlüssel erstellen</button>
          </div>
        </div>
        <div class="oad-code">
          <div class="oad-code__header">
            <span>Javascript</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          </div>
          <pre><code><span class="c-k">import</span> OpenAI <span class="c-k">from</span> <span class="c-s">"opensin"</span>;
<span class="c-k">const</span> client = <span class="c-k">new</span> OpenAI();

<span class="c-k">const</span> response = <span class="c-k">await</span> client.responses.create({
  model: <span class="c-s">"gpt-5.4"</span>,
  input: <span class="c-s">"Write a short bedtime story about a unicorn."</span>
});

console.log(response.output_text);</code></pre>
        </div>
      </section>

      <!-- Pfade erstellen -->
      <section class="oad-section">
        <h2 class="oad-section__title">Pfade erstellen</h2>
        <div class="oad-path-grid">
          <div class="oad-path-card">
            <h4>Responses API</h4>
            <p>Stellen Sie direkte Modellanfragen für Text, strukturierte Ausgaben, Werkzeuge und multimodale Arbeitsabläufe.</p>
            <span class="oad-path-card__link">Beginnen wir mit den Antworten ↗</span>
          </div>
          <div class="oad-path-card">
            <h4>Agenten-SDK</h4>
            <p>Entwickeln Sie Code-First-Agenten, die Tools, Übergaben, Genehmigungen, Tracing und containerbasierte Ausführung orchestrieren.</p>
            <span class="oad-path-card__link">Beginnen Sie mit dem Agents SDK. ↗</span>
          </div>
        </div>
      </section>

      <!-- Modelle -->
      <section class="oad-section">
        <div class="oad-section__header">
          <h2 class="oad-section__title">Modelle</h2>
          <a href="#" class="oa-link">Alle anzeigen</a>
        </div>
        <p class="oad-section__subtitle">Für komplexe Schlussfolgerungen und Codierungen empfiehlt sich gpt-5.4, für Workloads mit geringerer Latenz und niedrigeren Kosten hingegen gpt-5.4-mini und gpt-5.4-nano.</p>
        
        <div class="oad-model-grid">
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--pollen">
              <span>gpt-5.4</span>
            </div>
            <div class="oad-model-card__body">
              <h5>GPT-5.4 <span class="badge">Neu</span></h5>
              <p>Optimale Intelligenz im großen Maßstab für agentenbasierte, Codierungs- und professionelle Arbeitsabläufe</p>
            </div>
          </div>
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--rose">
              <span>gpt-5.4-mini</span>
            </div>
            <div class="oad-model-card__body">
              <h5>GPT-5.4 mini <span class="badge">Neu</span></h5>
              <p>Unser bisher leistungsstärkstes Mini-Modell für Programmierung, Computernutzung und Subagenten</p>
            </div>
          </div>
          <div class="oad-model-card">
            <div class="oad-model-card__img oad-model-card__img--ocean">
              <span>gpt-5.4-nano</span>
            </div>
            <div class="oad-model-card__body">
              <h5>GPT-5.4 nano <span class="badge">Neu</span></h5>
              <p>Unser günstigstes Modell der GPT-5.4-Klasse für einfache Aufgaben mit hohem Volumen</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Building Grid -->
      <section class="oad-section">
        <h2 class="oad-section__title">Beginnen Sie mit dem Bauen</h2>
        <div class="oad-building-grid">
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
             <div>
               <h6>Text lesen und generieren</h6>
               <p>Verwenden Sie die API, um ein Modell abzufragen und Text zu generieren.</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
             <div>
               <h6>Nutzen Sie die Bildverarbeitungsfunktionen eines Modells.</h6>
               <p>Ermöglichen Sie Modellen, Bilder in Ihrer Anwendung anzuzeigen und zu analysieren.</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
             <div>
               <h6>Bilder als Ausgabe generieren ↗</h6>
               <p>Bilder mit GPT erstellen Bild 1</p>
             </div>
           </div>
           <div class="oad-building-item">
             <div class="oad-building-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg></div>
             <div>
               <h6>Apps mit Audio erstellen</h6>
               <p>Analysieren, transkribieren und generieren Sie Audio mit API-Endpunkten.</p>
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
