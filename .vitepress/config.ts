import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN Documentation',
  description: 'Official documentation for OpenSIN - The first Agent-to-Agent (A2A) network',
  base: '/',
  lastUpdated: true,
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: 'Guide', link: '/guide/getting-started' },
      { text: 'API Reference', link: '/api/overview' },
      { text: 'Tutorials', link: '/tutorials/agent-basics' },
      { text: 'Integrations', link: '/integrations/telegram' },
      { text: 'Architecture', link: '/architecture/overview' },
      { text: 'Examples', link: '/examples/hello-world' },
      { text: 'Best Practices', link: '/best-practices/agent-design' }
    ],
    sidebar: {
      '/guide/': [
        { text: 'Getting Started', link: '/guide/getting-started' },
        { text: 'Installation', link: '/guide/installation' },
        { text: 'Quick Start', link: '/guide/quick-start' },
        { text: 'Core Concepts', link: '/guide/core-concepts' },
        { text: 'Agent Basics', link: '/guide/agent-basics' },
        { text: 'Team Orchestration', link: '/guide/team-orchestration' },
        { text: 'A2A Protocol', link: '/guide/a2a-protocol' },
        { text: 'MCP Integration', link: '/guide/mcp-integration' },
        { text: 'Deployment', link: '/guide/deployment' }
      ],
      '/api/': [
        { text: 'API Overview', link: '/api/overview' },
        { text: 'Agent API', link: '/api/agent' },
        { text: 'Team API', link: '/api/team' },
        { text: 'A2A API', link: '/api/a2a' },
        { text: 'MCP API', link: '/api/mcp' },
        { text: 'Message API', link: '/api/message' },
        { text: 'Events API', link: '/api/events' }
      ],
      '/tutorials/': [
        { text: 'Agent Basics', link: '/tutorials/agent-basics' },
        { text: 'Multi-Agent Collaboration', link: '/tutorials/multi-agent' },
        { text: 'Custom Agents', link: '/tutorials/custom-agents' },
        { text: 'Advanced Orchestration', link: '/tutorials/advanced-orchestration' }
      ],
      '/integrations/': [
        { text: 'Telegram', link: '/integrations/telegram' },
        { text: 'Discord', link: '/integrations/discord' },
        { text: 'WhatsApp', link: '/integrations/whatsapp' },
        { text: 'Slack', link: '/integrations/slack' },
        { text: 'Signal', link: '/integrations/signal' },
        { text: 'Matrix', link: '/integrations/matrix' }
      ],
      '/architecture/': [
        { text: 'Architecture Overview', link: '/architecture/overview' },
        { text: 'Core Architecture', link: '/architecture/core' },
        { text: 'A2A Protocol', link: '/architecture/a2a' },
        { text: 'Security', link: '/architecture/security' },
        { text: 'Scalability', link: '/architecture/scalability' }
      ],
      '/examples/': [
        { text: 'Hello World', link: '/examples/hello-world' },
        { text: 'Multi-Agent Team', link: '/examples/multi-agent' },
        { text: 'Telegram Bot', link: '/examples/telegram-bot' },
        { text: 'Discord Bot', link: '/examples/discord-bot' }
      ],
      '/best-practices/': [
        { text: 'Agent Design', link: '/best-practices/agent-design' },
        { text: 'Security', link: '/best-practices/security' },
        { text: 'Performance', link: '/best-practices/performance' },
        { text: 'Testing', link: '/best-practices/testing' }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI/OpenSIN' },
      { icon: 'discord', link: 'https://discord.gg/opensin' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026 OpenSIN-AI'
    }
  }
})
