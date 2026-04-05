import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN Docs',
  description: 'Official documentation for OpenSIN — the world\'s most comprehensive AI agent system',
  base: '/',
  lang: 'en-US',
  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true,
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#5f67ee' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: 'en' }],
    ['meta', { property: 'og:title', content: 'OpenSIN Documentation' }],
    ['meta', { property: 'og:description', content: 'Official documentation for OpenSIN AI agent system' }],
    ['meta', { property: 'og:site_name', content: 'OpenSIN Docs' }],
    ['meta', { property: 'og:image', content: 'https://docs.opensin.ai/og-image.png' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ],
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: 'Guide', link: '/guide/getting-started' },
      { text: 'API', link: '/api/overview' },
      { text: 'Tutorials', link: '/tutorials/agent-basics' },
      { text: 'Integrations', link: '/integrations/telegram' },
      { text: 'Architecture', link: '/architecture/overview' },
      { text: 'Community', link: 'https://discord.gg/opensin' },
    ],
    sidebar: {
      '/guide/': [
        { text: 'Getting Started', items: [
          { text: 'Introduction', link: '/guide/getting-started' },
          { text: 'Installation', link: '/guide/installation' },
          { text: 'Quick Start', link: '/guide/quick-start' },
        ]},
        { text: 'Core Guides', items: [
          { text: 'Agent Basics', link: '/guide/agent-basics' },
          { text: 'Team Orchestration', link: '/guide/team-orchestration' },
          { text: 'A2A Protocol', link: '/guide/a2a-protocol' },
          { text: 'MCP Integration', link: '/guide/mcp-integration' },
        ]},
        { text: 'Operations', items: [
          { text: 'Deployment', link: '/guide/deployment' },
          { text: 'Monitoring', link: '/guide/monitoring' },
          { text: 'Scaling', link: '/guide/scaling' },
          { text: 'Troubleshooting', link: '/guide/troubleshooting' },
          { text: 'Changelog', link: '/guide/changelog' },
        ]},
      ],
      '/api/': [
        { text: 'API Reference', items: [
          { text: 'Overview', link: '/api/overview' },
        ]},
      ],
      '/architecture/': [
        { text: 'Architecture', items: [
          { text: 'Overview', link: '/architecture/overview' },
        ]},
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI/OpenSIN-documentation' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
    search: {
      provider: 'local',
    },
    editLink: {
      pattern: 'https://github.com/OpenSIN-AI/OpenSIN-documentation/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },
    footer: {
      message: 'Released under the Apache 2.0 License.',
      copyright: 'Copyright © 2026 OpenSIN-AI',
    },
  },
})
