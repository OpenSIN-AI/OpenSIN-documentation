import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN Docs',
  description: 'Official documentation for OpenSIN AI agent system',
  base: '/',
  cleanUrls: true,
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/getting-started' },
      { text: 'API', link: '/api/overview' },
      { text: 'Architecture', link: '/architecture/overview' },
      { text: 'Community', link: 'https://discord.gg/opensin' },
    ],
    sidebar: {
      '/guide/': [
        { text: 'Getting Started', link: '/guide/getting-started' },
        { text: 'Installation', link: '/guide/installation' },
        { text: 'Quick Start', link: '/guide/quick-start' },
      ],
      '/api/': [
        { text: 'Overview', link: '/api/overview' },
      ],
      '/architecture/': [
        { text: 'Overview', link: '/architecture/overview' },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI/OpenSIN-documentation' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
    search: { provider: 'local' },
    footer: {
      message: 'Released under the Apache 2.0 License.',
      copyright: 'Copyright 2026 OpenSIN-AI',
    },
  },
})
