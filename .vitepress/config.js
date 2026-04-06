import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN Docs',
  description: 'Official documentation for OpenSIN — the world\'s most comprehensive autonomous AI agent ecosystem',
  base: '/',
  lang: 'en-US',
  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true,
  sitemap: {
    hostname: 'https://docs.opensin.ai',
  },
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#10b981' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: 'en' }],
    ['meta', { property: 'og:title', content: 'OpenSIN Documentation — AI Agent Ecosystem' }],
    ['meta', { property: 'og:description', content: 'Official documentation for OpenSIN — 100+ autonomous AI agents, 18 specialized teams, A2A protocol' }],
    ['meta', { property: 'og:site_name', content: 'OpenSIN Docs' }],
    ['meta', { property: 'og:image', content: 'https://docs.opensin.ai/og-image.png' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:site', content: '@OpenSIN_AI' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
  ],
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: 'Guide', link: '/guide/getting-started' },
      { text: 'API', link: '/api/overview' },
      { text: 'SDK', link: '/sdk/overview' },
      { text: 'Tutorials', link: '/tutorials/agent-basics' },
      { text: 'Bridge', link: '/bridges/opensin-bridge-overview' },
      { text: 'Architecture', link: '/architecture/overview' },
      { text: 'opensin.ai', link: 'https://opensin.ai' },
      { text: 'Community', link: 'https://discord.gg/opensin' },
    ],
    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Introduction', link: '/guide/getting-started' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Quick Start', link: '/guide/quick-start' },
          ],
        },
        {
          text: 'Core Guides',
          items: [
            { text: 'Agent Basics', link: '/guide/agent-basics' },
            { text: 'Team Orchestration', link: '/guide/team-orchestration' },
            { text: 'A2A Protocol', link: '/guide/a2a-protocol' },
            { text: 'MCP Integration', link: '/guide/mcp-integration' },
          ],
        },
        {
          text: 'Operations',
          items: [
            { text: 'Deployment', link: '/guide/deployment' },
            { text: 'Monitoring', link: '/guide/monitoring' },
            { text: 'Scaling', link: '/guide/scaling' },
            { text: 'Troubleshooting', link: '/guide/troubleshooting' },
            { text: 'Changelog', link: '/guide/changelog' },
          ],
        },
      ],
      '/sdk/': [
        {
          text: 'SDK Reference',
          items: [
            { text: 'Overview', link: '/sdk/overview' },
            { text: 'Agent Loop', link: '/sdk/agent-loop' },
            { text: 'Tool System', link: '/sdk/tool-system' },
            { text: 'Model Routing', link: '/sdk/model-routing' },
            { text: 'Memory Manager', link: '/sdk/memory' },
            { text: 'Context Management', link: '/sdk/context-management' },
            { text: 'Safety & Permissions', link: '/sdk/safety' },
            { text: 'Session Persistence', link: '/sdk/sessions' },
            { text: 'Hooks & Lifecycle', link: '/sdk/hooks' },
            { text: 'Parallel Execution', link: '/sdk/parallel-execution' },
            { text: 'Usage & Pricing', link: '/sdk/usage-pricing' },
          ],
        },
      ],
      '/plugins/': [
        {
          text: 'Plugins',
          items: [
            { text: 'Plugin Registry', link: '/plugins/registry' },
          ],
        },
      ],
      '/api/': [
        {
          text: 'API Reference',
          items: [
            { text: 'Overview', link: '/api/overview' },
            { text: 'Agent API', link: '/api/agent' },
            { text: 'A2A API', link: '/api/a2a' },
            { text: 'Team API', link: '/api/team' },
          ],
        },
      ],
      '/tutorials/': [
        {
          text: 'Tutorials',
          items: [
            { text: 'Agent Basics', link: '/tutorials/agent-basics' },
            { text: 'Custom Agents', link: '/tutorials/custom-agents' },
            { text: 'Multi-Agent Systems', link: '/tutorials/multi-agent' },
            { text: 'Advanced Orchestration', link: '/tutorials/advanced-orchestration' },
          ],
        },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'Hello World', link: '/examples/hello-world' },
            { text: 'Multi-Agent', link: '/examples/multi-agent' },
            { text: 'Telegram Bot', link: '/examples/telegram-bot' },
          ],
        },
      ],
      '/architecture/': [
        {
          text: 'Architecture',
          items: [
            { text: 'Overview', link: '/architecture/overview' },
            { text: 'Core Architecture', link: '/architecture/core' },
            { text: 'A2A Protocol', link: '/architecture/a2a' },
            { text: 'Security', link: '/architecture/security' },
          ],
        },
      ],
      '/bridges/': [
        {
          text: 'OpenSIN Bridge',
          items: [
            { text: 'Overview', link: '/bridges/opensin-bridge-overview' },
            { text: 'Chrome Extension', link: '/bridges/chrome-extension' },
          ],
        },
      ],
      '/best-practices/': [
        {
          text: 'Best Practices',
          items: [
            { text: 'Agent Design', link: '/best-practices/agent-design' },
            { text: 'Performance', link: '/best-practices/performance' },
            { text: 'Security', link: '/best-practices/security' },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI/OpenSIN-documentation' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: 'Search',
                buttonAriaLabel: 'Search documentation',
              },
              modal: {
                noResultsText: 'No results found',
                resetButtonTitle: 'Reset search',
                footer: {
                  selectText: 'to select',
                  navigateText: 'to navigate',
                  closeText: 'to close',
                },
              },
            },
          },
        },
      },
    },
    editLink: {
      pattern: 'https://github.com/OpenSIN-AI/OpenSIN-documentation/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },
    lastUpdated: {
      text: 'Last updated',
      formatOptions: {
        dateStyle: 'full',
      },
    },
    footer: {
      message: 'Released under the Apache 2.0 License.',
      copyright: 'Copyright © 2026 OpenSIN-AI',
    },
  },
  markdown: {
    lineNumbers: true,
  },
})
