<script setup>
const sidebarSections = [
  {
    title: 'Get started',
    links: [
      { title: 'Overview', href: '/api/overview' },
      { title: 'Quickstart', href: '/guide/getting-started' },
      { title: 'Models', href: '/api/overview' },
      { title: 'Pricing', href: '/guide/changelog' },
      { title: 'Libraries', href: '/guide/opensin-code' },
      { title: 'Latest: OpenSIN Code', href: '/guide/whats-new' },
      { title: 'Prompt guidance', href: '/guide/opensin-code' },
    ],
  },
  {
    title: 'Core concepts',
    links: [
      { title: 'Text generation', href: '/guide/opensin-code' },
      { title: 'Code generation', href: '/guide/opensin-code' },
      { title: 'Images and vision', href: '/guide/agent-basics' },
      { title: 'Audio and speech', href: '/guide/mcp-integration' },
      { title: 'Structured output', href: '/api/overview' },
      { title: 'Function calling', href: '/api/a2a' },
      { title: 'OpenSIN API', href: '/api/overview' },
      { title: 'Using tools', href: '/guide/opensin-code' },
    ],
  },
  {
    title: 'OpenSIN Code',
    links: [
      { title: 'Overview', href: '/guide/opensin-code' },
      { title: 'Quickstart', href: '/guide/getting-started' },
      { title: 'Agent definitions', href: '/guide/agent-basics' },
      { title: 'Models and providers', href: '/api/agent' },
      { title: 'Running agents', href: '/guide/team-orchestration' },
      { title: 'Sandbox agents', href: '/guide/stealth-browser-operator' },
      { title: 'Orchestration', href: '/api/team' },
      { title: 'Guardrails', href: '/best-practices/security' },
      { title: 'Results and state', href: '/guide/mcp-integration' },
      { title: 'Integrations and observability', href: '/guide/monitoring' },
      { title: 'Evaluate agent workflows', href: '/best-practices/testing' },
      { title: 'Voice agents', href: '/guide/whats-new' },
    ],
  },
  {
    title: 'Tools',
    links: [
      { title: 'Web search', href: '/guide/mcp-integration' },
      { title: 'MCP and Connectors', href: '/guide/mcp-integration' },
      { title: 'Skills', href: '/guide/opensin-code' },
      { title: 'Shell', href: '/guide/opensin-code' },
      { title: 'Computer use', href: '/guide/opensin-code' },
      { title: 'File search', href: '/guide/mcp-integration' },
      { title: 'Retrieval', href: '/guide/mcp-integration' },
      { title: 'Tool search', href: '/guide/opensin-code' },
    ],
  },
  {
    title: 'Run and scale',
    links: [
      { title: 'Conversation state', href: '/guide/agent-basics' },
      { title: 'Background mode', href: '/guide/opensin-code' },
      { title: 'Streaming', href: '/guide/opensin-code' },
      { title: 'WebSocket mode', href: '/guide/opensin-code' },
      { title: 'Webhooks', href: '/guide/mcp-integration' },
      { title: 'File inputs', href: '/guide/getting-started' },
      { title: 'Prompting', href: '/guide/opensin-code' },
      { title: 'Reasoning', href: '/guide/opensin-code' },
    ],
  },
  {
    title: 'Evaluation',
    links: [
      { title: 'Getting started', href: '/best-practices/testing' },
      { title: 'Working with evals', href: '/best-practices/testing' },
      { title: 'Prompt optimizer', href: '/best-practices/performance' },
      { title: 'External models', href: '/best-practices/performance' },
      { title: 'Best practices', href: '/best-practices/testing' },
    ],
  },
  {
    title: 'Realtime API',
    links: [
      { title: 'Overview', href: '/guide/mcp-integration' },
      { title: 'WebRTC', href: '/guide/mcp-integration' },
      { title: 'WebSocket', href: '/guide/mcp-integration' },
      { title: 'SIP', href: '/guide/mcp-integration' },
      { title: 'Using realtime models', href: '/guide/opensin-code' },
      { title: 'Managing conversations', href: '/guide/agent-basics' },
      { title: 'MCP servers', href: '/guide/mcp-integration' },
      { title: 'Webhooks and server-side controls', href: '/guide/mcp-integration' },
      { title: 'Managing costs', href: '/best-practices/performance' },
      { title: 'Realtime transcription', href: '/guide/opensin-code' },
      { title: 'Voice agents', href: '/guide/whats-new' },
    ],
  },
  {
    title: 'Model optimization',
    links: [
      { title: 'Optimization cycle', href: '/best-practices/performance' },
      { title: 'Supervised fine-tuning', href: '/guide/opensin-code' },
      { title: 'Vision fine-tuning', href: '/guide/agent-basics' },
      { title: 'Direct preference optimization', href: '/best-practices/performance' },
      { title: 'Reinforcement fine-tuning', href: '/best-practices/performance' },
      { title: 'RFT use cases', href: '/best-practices/performance' },
      { title: 'Best practices', href: '/best-practices/performance' },
      { title: 'Graders', href: '/best-practices/testing' },
    ],
  },
  {
    title: 'Specialized models',
    links: [
      { title: 'Image generation', href: '/guide/opensin-code' },
      { title: 'Video generation', href: '/guide/whats-new' },
      { title: 'Text to speech', href: '/guide/opensin-code' },
      { title: 'Speech to text', href: '/guide/opensin-code' },
      { title: 'Deep research', href: '/guide/whats-new' },
      { title: 'Embeddings', href: '/guide/opensin-code' },
      { title: 'Moderation', href: '/best-practices/security' },
    ],
  },
  {
    title: 'Going live',
    links: [
      { title: 'Production best practices', href: '/best-practices/performance' },
      { title: 'Deployment checklist', href: '/guide/deployment' },
      { title: 'Latency optimization', href: '/best-practices/performance' },
      { title: 'Cost optimization', href: '/best-practices/performance' },
      { title: 'Accuracy optimization', href: '/best-practices/performance' },
      { title: 'Safety best practices', href: '/best-practices/security' },
      { title: 'Safety checks', href: '/best-practices/security' },
      { title: 'Cybersecurity checks', href: '/best-practices/security' },
    ],
  },
  {
    title: 'Legacy APIs',
    links: [
      { title: 'Assistants API', href: '/guide/opensin-code' },
      { title: 'Migration guide', href: '/guide/opensin-code' },
      { title: 'Deep dive', href: '/guide/opensin-code' },
      { title: 'Tools', href: '/guide/opensin-code' },
    ],
  },
  {
    title: 'Resources',
    links: [
      { title: 'Terms and policies', href: 'https://opensin.ai/policies', external: true },
      { title: 'Changelog', href: '/guide/changelog' },
      { title: 'Your data', href: '/governance/overview' },
      { title: 'Permissions', href: '/governance/overview' },
      { title: 'Rate limits', href: '/guide/opensin-code' },
      { title: 'Deprecations', href: '/guide/changelog' },
      { title: 'Developer mode', href: '/guide/opensin-code' },
    ],
  },
]

const quickstartSamples = [
  {
    id: 'shell',
    label: 'Shell',
    code: `bun add @opensin/sdk`,
  },
  {
    id: 'js',
    label: 'JavaScript',
    code: `import { AgentLoop } from '@opensin/sdk';

const loop = new AgentLoop();
const response = await loop.run('Write a short bedtime story about a unicorn.');

console.log(response.outputText);`,
  },
  {
    id: 'python',
    label: 'Python',
    code: `from opensin_ouroboros import AgentLoop

loop = AgentLoop()
response = loop.run('Write a short bedtime story about a unicorn.')

print(response.output_text)`,
  },
  {
    id: 'csharp',
    label: 'C#',
    code: `using OpenSIN.SDK;

var client = new OpenSINClient();
var response = client.CreateResponse("Write a short bedtime story about a unicorn.");

Console.WriteLine(response.OutputText);`,
  },
]

const buildPaths = [
  {
    title: 'OpenSIN API',
    description: 'Make direct platform requests for text, structured output, tools, and multimodal workflows.',
    href: '/api/overview',
    cta: 'Start with OpenSIN API',
  },
  {
    title: 'OpenSIN Code',
    description: 'Build code-first agents that orchestrate tools, handoffs, approvals, tracing, and container-based execution.',
    href: '/guide/opensin-code',
    cta: 'Start with OpenSIN Code',
  },
]

const models = [
  {
    title: 'OpenSIN API',
    badge: 'New',
    description: 'Primary surface for text, tools, and multimodal workflows.',
    href: '/api/overview',
  },
  {
    title: 'OpenSIN Agents',
    badge: '',
    description: 'Code-first agent orchestration with handoffs and tracing.',
    href: '/api/overview',
  },
  {
    title: 'OpenSIN Mini',
    badge: '',
    description: 'Lower-latency execution for lightweight tasks and subagents.',
    href: '/api/overview',
  },
]

const startBuilding = [
  {
    title: 'Read and generate text',
    description: 'Use the API to prompt a model and generate text.',
    href: '/guide/opensin-code',
    image: 'https://cdn.openai.com/devhub/resources/guide-2.png',
    icon: 'book',
  },
  {
    title: "Use a model's vision capabilities",
    description: 'Allow models to see and analyze images in your application.',
    href: '/guide/agent-basics',
    image: 'https://cdn.openai.com/devhub/resources/guide-3.png',
    icon: 'image',
  },
  {
    title: 'Generate images as output',
    description: 'Create images with OpenSIN image models.',
    href: '/guide/opensin-code',
    image: 'https://cdn.openai.com/devhub/resources/code-2.png',
    icon: 'spark',
  },
  {
    title: 'Build apps with audio',
    description: 'Analyze, transcribe, and generate audio with API endpoints.',
    href: '/guide/mcp-integration',
    image: 'https://cdn.openai.com/devhub/resources/video-2.png',
    icon: 'monitor',
  },
  {
    title: 'Build agentic applications',
    description: 'Use the API to build agents that use tools and computers.',
    href: '/guide/team-orchestration',
    image: 'https://cdn.openai.com/devhub/resources/code-3.png',
    icon: 'chat',
  },
  {
    title: 'Achieve complex tasks with reasoning',
    description: 'Use reasoning models to carry out complex tasks.',
    href: '/best-practices/performance',
    image: 'https://cdn.openai.com/devhub/resources/video-1.png',
    icon: 'spark',
  },
  {
    title: 'Get structured data from models',
    description: 'Use Structured Outputs to get model responses that adhere to a JSON schema.',
    href: '/api/overview',
    image: 'https://cdn.openai.com/devhub/resources/guide-4.png',
    icon: 'book',
  },
  {
    title: 'Tailor to your use case',
    description: 'Adjust our models to perform specifically for your use case with fine-tuning, evals, and distillation.',
    href: '/best-practices/performance',
    image: 'https://cdn.openai.com/devhub/resources/cookbook-4.png',
    icon: 'spark',
  },
]
</script>

<template>
  <div class="oa-page">
    <div class="oa-container">
      <aside class="oa-sidebar" aria-label="Documentation navigation">
        <div class="oa-sidebar__search">
          <span>Search docs</span>
          <small>opensin code agents mcp memory</small>
        </div>

        <div v-for="section in sidebarSections" :key="section.title" class="oa-sidebar__section">
          <p class="oa-sidebar__label">{{ section.title }}</p>
          <a
            v-for="link in section.links"
            :key="link.title"
            class="oa-sidebar__link"
            :class="{ 'oa-sidebar__link--external': link.external }"
            :href="link.href"
            :target="link.external ? '_blank' : undefined"
            :rel="link.external ? 'noreferrer' : undefined"
          >
            {{ link.title }}
          </a>
        </div>
      </aside>

      <main class="oa-main">
        <header class="oa-hero">
          <h1>OpenSIN API Platform Documentation</h1>
        </header>

        <section class="oa-quickstart">
          <div class="oa-quickstart__copy">
            <p class="oa-kicker">Developer quickstart</p>
            <h2>Make your first API request in minutes.</h2>
            <p>
              Learn the basics of the OpenSIN platform with the same calm, high-signal layout used by the reference experience.
            </p>

            <div class="oa-actions">
              <a class="oa-button oa-button--primary" href="/api/overview">Get started</a>
              <a class="oa-button oa-button--secondary" href="https://chat.opensin.ai">Create API key</a>
            </div>
          </div>

          <div class="oa-snippet-grid" aria-label="Quickstart code examples">
            <article v-for="sample in quickstartSamples" :key="sample.id" class="oa-snippet">
              <div class="oa-snippet__bar">
                <span>{{ sample.label }}</span>
                <span>Copy</span>
              </div>
              <pre><code>{{ sample.code }}</code></pre>
            </article>
          </div>
        </section>

        <section class="oa-section">
          <div class="oa-section-header">
            <h2 class="oa-section-title">Build paths</h2>
          </div>

          <div class="oa-build-grid">
            <a v-for="path in buildPaths" :key="path.title" :href="path.href" class="oa-build-card oa-card--link">
              <h3>{{ path.title }}</h3>
              <p>{{ path.description }}</p>
              <span class="oa-card__cta">{{ path.cta }}</span>
            </a>
          </div>
        </section>

        <section class="oa-section">
          <div class="oa-section-header">
            <h2 class="oa-section-title">Models</h2>
            <a class="oa-view-all" href="/api/overview">View all</a>
          </div>

          <p class="oa-section-subtitle">
            Start with OpenSIN API for complex workflows, or choose OpenSIN mini for lower-latency, lower-cost workloads.
          </p>

          <div class="oa-model-grid">
            <a v-for="model in models" :key="model.title" :href="model.href" class="oa-model-card">
              <span v-if="model.badge" class="oa-model-card__badge">{{ model.badge }}</span>
              <span class="oa-model-card__title">{{ model.title }}</span>
              <span class="oa-model-card__desc">{{ model.description }}</span>
            </a>
          </div>
        </section>

        <section class="oa-section">
          <div class="oa-section-header">
            <h2 class="oa-section-title">Start building</h2>
          </div>

          <div class="oa-start-grid">
            <a v-for="card in startBuilding" :key="card.title" :href="card.href" class="oa-start-card">
              <div class="oa-start-card__media">
                <img :src="card.image" :alt="card.title" />
                <span class="oa-start-card__badge">
                  <CardIcon :name="card.icon" variant="explore" />
                </span>
              </div>
              <div class="oa-start-card__body">
                <h3>{{ card.title }}</h3>
                <p>{{ card.description }}</p>
              </div>
            </a>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>
.oa-page {
  min-height: 100vh;
  background: var(--oa-bg);
  color: var(--oa-text-primary);
}

.oa-container {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 262px minmax(0, 1fr);
}

.oa-sidebar {
  position: sticky;
  top: 72px;
  align-self: start;
  max-height: calc(100vh - 72px);
  overflow: auto;
  padding: 28px 18px 40px;
  border-right: 1px solid var(--oa-border);
  background: var(--oa-bg);
}

.oa-sidebar__search {
  padding: 14px 14px 16px;
  margin-bottom: 24px;
  border: 1px solid var(--oa-border);
  border-radius: 16px;
  background: var(--oa-bg);
}

.oa-sidebar__search span {
  display: block;
  margin-bottom: 6px;
  color: var(--oa-text-primary);
  font-size: 0.92rem;
  font-weight: 600;
}

.oa-sidebar__search small {
  display: block;
  color: var(--oa-text-secondary);
  font-size: 0.8rem;
  line-height: 1.45;
}

.oa-sidebar__section + .oa-sidebar__section {
  margin-top: 24px;
}

.oa-sidebar__label,
.oa-kicker {
  margin: 0 0 12px;
  color: var(--oa-text-primary);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0;
}

.oa-sidebar__link {
  display: block;
  padding: 8px 12px;
  border-radius: 10px;
  color: var(--oa-text-secondary);
  font-size: 0.92rem;
  line-height: 1.35;
  text-decoration: none;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.oa-sidebar__link:hover {
  color: var(--oa-text-primary);
  background: var(--oa-accent-soft);
}

.oa-sidebar__link--external::after {
  content: '↗';
  margin-left: 6px;
  font-size: 0.75rem;
  color: var(--oa-text-muted);
}

.oa-main {
  padding: 34px 50px 82px;
}

.oa-hero {
  max-width: 860px;
  margin-bottom: 18px;
}

.oa-hero h1 {
  margin: 0;
  color: var(--oa-text-primary);
  font-size: clamp(2.8rem, 4vw, 3.8rem);
  line-height: 0.96;
  letter-spacing: -0.06em;
  font-weight: 700;
}

.oa-quickstart {
  display: grid;
  grid-template-columns: minmax(0, 0.88fr) minmax(0, 1.12fr);
  gap: 24px;
  margin-bottom: 36px;
}

.oa-quickstart__copy h2,
.oa-section-title,
.oa-build-card h3,
.oa-model-card__title,
.oa-start-card h3 {
  margin: 0;
  color: var(--oa-text-primary);
  letter-spacing: -0.04em;
}

.oa-quickstart__copy h2 {
  font-size: 1.95rem;
  line-height: 1.12;
}

.oa-quickstart__copy p,
.oa-build-card p,
.oa-model-card__desc,
.oa-start-card p,
.oa-section-subtitle {
  color: var(--oa-text-secondary);
  line-height: 1.65;
}

.oa-quickstart__copy p {
  margin: 12px 0 0;
  max-width: 60ch;
}

.oa-actions {
  display: flex;
  gap: 12px;
  margin-top: 20px;
}

.oa-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 700;
}

.oa-button--primary {
  background: var(--oa-accent);
  color: #ffffff;
}

.oa-button--secondary {
  background: var(--oa-hover);
  color: var(--oa-text-primary);
}

.oa-snippet-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

.oa-snippet {
  border-radius: 18px;
  overflow: hidden;
  background: #0d1117;
  color: #e6edf3;
  font-family: 'JetBrains Mono', monospace;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08);
}

.oa-snippet__bar {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  color: var(--oa-text-muted);
  font-size: 0.8rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.oa-snippet pre {
  margin: 0;
  padding: 16px 14px 18px;
  overflow-x: auto;
  font-size: 0.84rem;
  line-height: 1.58;
  white-space: pre;
}

.oa-section {
  margin-bottom: 40px;
}

.oa-section-header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 16px;
}

.oa-view-all {
  color: var(--oa-text-primary);
  font-weight: 700;
  text-decoration: none;
}

.oa-section-subtitle {
  margin: -4px 0 18px;
  max-width: 70ch;
}

.oa-build-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.oa-build-card {
  border: 0;
  border-radius: 16px;
  padding: 22px;
  background: var(--oa-hover);
  box-shadow: none;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-build-card:hover {
  transform: translateY(-2px);
  background: color-mix(in srgb, var(--oa-hover) 72%, var(--oa-bg));
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.oa-card--link {
  text-decoration: none;
  display: block;
}

.oa-card__cta {
  display: inline-flex;
  margin-top: 18px;
  color: var(--oa-text-primary);
  font-weight: 700;
}

.oa-model-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: 2px;
}

.oa-model-card {
  min-height: 172px;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  text-decoration: none;
  padding: 20px;
  border: 0;
  background: var(--oa-hover);
  box-shadow: none;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
}

.oa-model-card:hover {
  transform: translateY(-2px);
  background: color-mix(in srgb, var(--oa-hover) 72%, var(--oa-bg));
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.oa-model-card__badge {
  align-self: flex-start;
  display: inline-flex;
  padding: 4px 8px;
  border-radius: 999px;
  background: var(--oa-accent-soft);
  color: var(--oa-accent);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.oa-model-card__title {
  font-size: 1.45rem;
  line-height: 1.08;
}

.oa-model-card__desc {
  font-size: 0.92rem;
}

.oa-start-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.oa-start-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  border-radius: 16px;
  overflow: hidden;
  border: 0;
  background: transparent;
  box-shadow: none;
  transition: transform 0.2s ease;
}

.oa-start-card:hover {
  transform: translateY(-2px);
}

.oa-start-card__media {
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: linear-gradient(180deg, var(--oa-hover) 0%, var(--oa-bg) 100%);
  border-radius: 16px;
}

.oa-start-card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.oa-start-card__badge {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.oa-start-card__body {
  padding: 14px 0 0;
}

.oa-start-card h3 {
  font-size: 1.02rem;
  line-height: 1.28;
}

.oa-start-card p {
  margin: 6px 0 0;
  font-size: 0.92rem;
}

@media (max-width: 1100px) {
  .oa-container,
  .oa-quickstart,
  .oa-build-grid,
  .oa-model-grid,
  .oa-start-grid {
    grid-template-columns: 1fr;
  }

  .oa-sidebar {
    position: static;
    max-height: none;
    border-right: 0;
    border-bottom: 1px solid var(--oa-border);
  }

  .oa-main {
    padding: 28px 20px 72px;
  }
}

@media (max-width: 720px) {
  .oa-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .oa-button {
    width: 100%;
  }

  .oa-snippet-grid {
    grid-template-columns: 1fr;
  }
}

:global(.dark) .oa-page {
  background: var(--oa-bg);
  color: var(--oa-text-primary);
}

:global(.dark) .oa-sidebar {
  background: var(--oa-bg);
  border-right-color: var(--oa-border);
}

:global(.dark) .oa-sidebar__search,
:global(.dark) .oa-build-card,
:global(.dark) .oa-model-card,
:global(.dark) .oa-start-card {
  background: var(--oa-hover);
  border-color: var(--oa-border);
  box-shadow: none;
}

:global(.dark) .oa-sidebar__search span,
:global(.dark) .oa-hero h1,
:global(.dark) .oa-section-title,
:global(.dark) .oa-quickstart__copy h2,
:global(.dark) .oa-build-card h3,
:global(.dark) .oa-model-card__title,
:global(.dark) .oa-start-card h3 {
  color: var(--oa-text-primary);
}

:global(.dark) .oa-sidebar__search small,
:global(.dark) .oa-quickstart__copy p,
:global(.dark) .oa-build-card p,
:global(.dark) .oa-model-card__desc,
:global(.dark) .oa-start-card p,
:global(.dark) .oa-section-subtitle {
  color: var(--oa-text-secondary);
}

:global(.dark) .oa-sidebar__link,
:global(.dark) .oa-view-all {
  color: var(--oa-text-secondary);
}

:global(.dark) .oa-sidebar__link:hover,
:global(.dark) .oa-view-all:hover {
  color: var(--oa-text-primary);
  background: var(--oa-accent-soft);
}

:global(.dark) .oa-button--primary {
  background: var(--oa-accent);
  color: #ffffff;
}

:global(.dark) .oa-button--secondary {
  background: var(--oa-hover);
  color: var(--oa-text-primary);
  border: 1px solid var(--oa-border);
}

:global(.dark) .oa-snippet {
  background: #0d1117;
  color: #e6edf3;
}

:global(.dark) .oa-snippet__bar {
  color: var(--oa-text-muted);
  border-bottom-color: rgba(255, 255, 255, 0.08);
}

:global(.dark) .oa-model-card__badge {
  background: var(--oa-accent-soft);
  color: #9ecbff;
}

:global(.dark) .oa-start-card__media,
:global(.dark) .oa-start-card__badge {
  background: linear-gradient(180deg, var(--oa-hover) 0%, var(--oa-bg) 100%);
}
</style>
