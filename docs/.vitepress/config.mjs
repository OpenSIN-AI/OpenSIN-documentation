import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN API Platform Documentation',
  description: 'Guides and concepts for the OpenSIN API.',
  lang: 'en-US',
  ignoreDeadLinks: true,
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }],
    ['link', { rel: 'canonical', href: 'https://docs.opensin.ai/' }],
    ['meta', { property: 'og:title', content: 'OpenSIN API Platform Documentation' }],
    ['meta', { property: 'og:description', content: 'Guides and concepts for the OpenSIN API.' }],
    ['meta', { property: 'og:image', content: 'https://docs.opensin.ai/social-preview.svg' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:image', content: 'https://docs.opensin.ai/social-preview.svg' }],
  ],
  themeConfig: {
    siteTitle: 'OpenSIN Developers',
    logo: '/logo.svg',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'API', link: '/api/' },
      { text: 'OpenSIN Code', link: '/guide/opensin-code' },
      { text: 'Chat', link: 'https://chat.opensin.ai' },
      { text: 'Resources', link: '/guide/getting-started' },
    ],
    sidebar: {
      '/guide/': [
        {
          text: 'Guide',
          items: [
            { text: 'Getting Started', link: '/guide/getting-started' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Quick Start', link: '/guide/quick-start' },
            { text: 'Agent Basics', link: '/guide/agent-basics' },
            { text: 'MCP Integration', link: '/guide/mcp-integration' },
            { text: 'A2A Protocol', link: '/guide/a2a-protocol' },
            { text: 'Plugin System', link: '/guide/plugin-system' },
            { text: 'Team Orchestration', link: '/guide/team-orchestration' },
            { text: 'Deployment', link: '/guide/deployment' },
            { text: 'Monitoring', link: '/guide/monitoring' },
            { text: 'Scaling', link: '/guide/scaling' },
            { text: 'Troubleshooting', link: '/guide/troubleshooting' },
            { text: 'Dynamic Input Commands', link: '/guides/dynamic-input-commands' },
            { text: 'Changelog', link: '/guide/changelog' },
          ],
        },
      ],
      '/architecture/': [
        {
          text: 'Architecture',
          items: [
            { text: 'Overview', link: '/architecture/overview' },
            { text: 'Core', link: '/architecture/core' },
            { text: 'A2A', link: '/architecture/a2a' },
            { text: 'Security', link: '/architecture/security' },
            { text: 'Global Brain & Neural-Bus', link: '/architecture/global-brain-neural-bus' },
            { text: 'Hacker Bypass', link: '/architecture/hacker-bypass' },
          ],
        },
      ],
      '/api/': [
        {
          text: 'API',
          items: [
            { text: 'Overview', link: '/api/overview' },
            { text: 'Agent API', link: '/api/agent' },
            { text: 'A2A API', link: '/api/a2a' },
            { text: 'Team API', link: '/api/team' },
          ],
        },
      ],
      '/sdk/': [
        {
          text: 'SDK',
          items: [
            { text: 'Overview', link: '/sdk/overview' },
            { text: 'Agent Loop', link: '/sdk/agent-loop' },
            { text: 'Context Management', link: '/sdk/context-management' },
            { text: 'Hooks', link: '/sdk/hooks' },
            { text: 'Memory', link: '/sdk/memory' },
            { text: 'Model Routing', link: '/sdk/model-routing' },
            { text: 'Parallel Execution', link: '/sdk/parallel-execution' },
            { text: 'Safety', link: '/sdk/safety' },
            { text: 'Sessions', link: '/sdk/sessions' },
            { text: 'Tool System', link: '/sdk/tool-system' },
            { text: 'Usage & Pricing', link: '/sdk/usage-pricing' },
          ],
        },
      ],
      '/plugins/': [
        {
          text: 'Plugins',
          items: [
            { text: 'Registry', link: '/plugins/registry' },
            { text: 'Context Pruning', link: '/plugins/context-pruning' },
            { text: 'Envsitter', link: '/plugins/envsitter' },
            { text: 'Handoff', link: '/plugins/handoff' },
            { text: 'Safety Net', link: '/plugins/safety-net' },
            { text: 'Context Analysis', link: '/plugins/context-analysis' },
            { text: 'Agent Memory', link: '/plugins/agent-memory' },
            { text: 'MCP Servers', link: '/plugins/mcp-servers' },
            { text: 'Code Plugins', link: '/plugins/opensin-code-plugins' },
          ],
        },
      ],
      '/fleet/': [
        {
          text: 'Fleet',
          items: [
            { text: 'Fleet Overview', link: '/fleet/overview' },
          ],
        },
      ],
      '/governance/': [
        {
          text: 'Governance',
          items: [
            { text: 'Overview', link: '/governance/overview' },
            { text: 'Domain Registry', link: '/governance/domain-registry' },
            { text: 'Security Mandate', link: '/governance/security-mandate' },
            { text: 'Zeus', link: '/governance/zeus' },
            { text: 'Hermes', link: '/governance/hermes' },
            { text: 'Repo Health Check', link: '/governance/repo-health-check' },
          ],
        },
      ],
      '/tutorials/': [
        {
          text: 'Tutorials',
          items: [
            { text: 'First Agent', link: '/tutorials/first-agent' },
            { text: 'Plugin Development', link: '/tutorials/plugin-development' },
            { text: 'A2A Communication', link: '/tutorials/a2a-communication' },
            { text: 'Advanced Orchestration', link: '/tutorials/advanced-orchestration' },
          ],
        },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'Hello World', link: '/examples/hello-world' },
            { text: 'Multi-Agent Example', link: '/examples/multi-agent' },
            { text: 'Telegram Bot Example', link: '/examples/telegram-bot' },
            { text: 'Dual Auth Rotators', link: '/examples/dual-auth-rotators' },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
    footer: {
      message: 'Guides and concepts for the OpenSIN API.',
      copyright: 'Copyright © 2026 OpenSIN-AI',
    },
    search: {
      provider: 'local',
    },
  },
})
