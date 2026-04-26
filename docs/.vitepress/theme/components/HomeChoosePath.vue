<template>
  <section class="home-choose-path">
    <h2 class="home-choose-path__title">Choose Your Path</h2>
    <div class="home-choose-path__grid">
      <a href="/guide/getting-started" class="home-choose-path__card is-highlight">
        <div class="home-choose-path__heading">Consumer Documentation <span class="home-choose-path__arrow">→</span></div>
      <div class="home-choose-path__description">Guides, onboarding, and the quickest path to using OpenSIN.</div>
      </a>
      <a href="https://developers.opensin.ai/docs/" class="home-choose-path__card">
        <div class="home-choose-path__heading">Developer Documentation <span class="home-choose-path__arrow">→</span></div>
        <div class="home-choose-path__description">APIs, SDKs, auth, webhooks, and integration details live on the builder surface.</div>
      </a>
    </div>
  </section>
</template>

<style scoped>
.home-choose-path { margin-top: 2.75rem; }
.home-choose-path__title { margin: 0 0 1rem; font-size: 1.6rem; font-weight: 700; letter-spacing: -0.03em; }
.home-choose-path__grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }
.home-choose-path__card {
  display: block;
  padding: 1.25rem 1.25rem;
  border-radius: 14px;
  border: 1px solid #e5e7eb;
  background: #ffffff;
  text-decoration: none;
  transition: border-color .2s ease, transform .2s ease, box-shadow .2s ease;
}
.home-choose-path__card:hover { transform: translateY(-2px); border-color: rgba(9,105,218,.35); box-shadow: 0 16px 30px rgba(15,23,42,.08); }
.home-choose-path__heading { color:#111827; font-size:1.05rem; font-weight:700; margin-bottom:.35rem; }
.home-choose-path__description { color:#4b5563; font-size:.95rem; line-height:1.45; }
.home-choose-path__card.is-highlight { border-color: rgba(9,105,218,.35); }
.home-choose-path__card.is-highlight .home-choose-path__heading { color:#0969da; }
.home-choose-path__arrow { margin-left:.35rem; }
:global(html:not(.dark)) .home-choose-path__card { box-shadow:0 10px 24px rgba(15,23,42,.05); }
:global(html:not(.dark)) .home-choose-path__card.is-highlight { background: linear-gradient(180deg,#ffffff 0%,#f6f8fa 100%); border-color: rgba(9,105,218,.24); }
:global(html:not(.dark)) .home-choose-path__card.is-highlight .home-choose-path__heading { color:#0550ae; }
:global(.dark) .home-choose-path__card { background:#141414; border-color:#2a2a2a; }
:global(.dark) .home-choose-path__heading { color:#f5f5f5; }
:global(.dark) .home-choose-path__description { color:#a0a0a0; }
:global(.dark) .home-choose-path__card.is-highlight { border-color: rgba(68,147,248,.35); }
:global(.dark) .home-choose-path__card.is-highlight .home-choose-path__heading { color:#58a6ff; }
@media (max-width: 720px) { .home-choose-path__grid { grid-template-columns: 1fr; } }
</style>
