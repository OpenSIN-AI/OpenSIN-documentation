import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'OpenSIN Docs',
  description: 'Official documentation for OpenSIN — the world\'s most comprehensive AI agent system',
  base: '/',
  lang: 'en-US',
  lastUpdated: true,
  cleanUrls: true,

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
        {
          text: 'Getting Started',
          items: [
            { text: 'Introduction', link: '/guide/getting-started' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Quick Start', link: '/guide/quick-start' },
            { text: 'Core Concepts', link: '/guide/core-concepts' },
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
            { text: 'Migration Guide', link: '/guide/migration' },
            { text: 'Changelog', link: '/guide/changelog' },
          ],
        },
        {
          text: 'Advanced',
          items: [
            { text: 'Advanced Agent Patterns', link: '/guide/advanced-agent-patterns' },
            { text: 'Security Hardening', link: '/guide/security-hardening' },
            { text: 'Performance Optimization', link: '/guide/performance-optimization' },
            { text: 'Developer Onboarding', link: '/guide/developer-onboarding' },
            { text: 'Troubleshooting & FAQ', link: '/guide/troubleshooting-faq' },
          ],
        },
        {
          text: 'Reference',
          items: [
            { text: 'Master Reference', link: '/guide/master-reference' },
            { text: 'Repository Catalog', link: '/guide/repository-catalog' },
            { text: 'Issue Phases', link: '/guide/issue-phases' },
            { text: 'Phase 5 Integration', link: '/guide/phase-5-integration' },
            { text: 'Testing Environment', link: '/guide/testing-environment' },
            { text: 'Refactor Backlog', link: '/guide/refactor-backlog' },
          ],
        },
      ],
      '/api/': [
        {
          text: 'API Reference',
          items: [
            { text: 'Overview', link: '/api/overview' },
            { text: 'Agent API', link: '/api/agent' },
            { text: 'Team API', link: '/api/team' },
            { text: 'A2A Protocol', link: '/api/a2a' },
            { text: 'Message API', link: '/api/message' },
            { text: 'Events API', link: '/api/events' },
            { text: 'Orchestrator API', link: '/api/orchestrator' },
            { text: 'MCP API', link: '/api/mcp' },
          ],
        },
      ],
      '/tutorials/': [
        {
          text: 'Tutorials',
          items: [
            { text: 'Agent Basics', link: '/tutorials/agent-basics' },
            { text: 'Multi-Agent Teams', link: '/tutorials/multi-agent' },
            { text: 'Custom Agents', link: '/tutorials/custom-agents' },
            { text: 'Advanced Orchestration', link: '/tutorials/advanced-orchestration' },
            { text: 'Telegram Bot', link: '/tutorials/telegram-bot' },
            { text: 'Discord Bot', link: '/tutorials/discord-bot' },
            { text: 'Deployment', link: '/tutorials/deployment' },
          ],
        },
      ],
      '/integrations/': [
        {
          text: 'Messaging Integrations',
          items: [
            { text: 'Telegram', link: '/integrations/telegram' },
            { text: 'Discord', link: '/integrations/discord' },
            { text: 'WhatsApp', link: '/integrations/whatsapp' },
            { text: 'Slack', link: '/integrations/slack' },
            { text: 'Signal', link: '/integrations/signal' },
            { text: 'Matrix', link: '/integrations/matrix' },
          ],
        },
        {
          text: 'Platform Integrations',
          items: [
            { text: 'Platform Auth', link: '/integrations/platform-auth' },
            { text: 'Auth Rotator', link: '/integrations/auth-rotator' },
            { text: 'ACP Protocol', link: '/integrations/acp-protocol' },
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
            { text: 'Scalability', link: '/architecture/scalability' },
            { text: 'Deep Dive', link: '/architecture/deep-dive' },
            { text: 'Chatroom Matrix', link: '/architecture/chatroom-matrix' },
          ],
        },
      ],
      '/best-practices/': [
        {
          text: 'Best Practices',
          items: [
            { text: 'Overview', link: '/best-practices/overview' },
            { text: 'Agent Design', link: '/best-practices/agent-design' },
            { text: 'Security', link: '/best-practices/security' },
            { text: 'Performance', link: '/best-practices/performance' },
            { text: 'Testing', link: '/best-practices/testing' },
          ],
        },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'Hello World', link: '/examples/hello-world' },
            { text: 'Multi-Agent Team', link: '/examples/multi-agent' },
            { text: 'Telegram Bot', link: '/examples/telegram-bot' },
            { text: 'Discord Bot', link: '/examples/discord-bot' },
            { text: 'Custom Agents', link: '/examples/custom-agents' },
            { text: 'Real-World Use Cases', link: '/examples/use-cases' },
          ],
        },
      ],
      '/platform/': [
        {
          text: 'Platform',
          items: [
            { text: 'Overview', link: '/platform/overview' },
            { text: 'OpenSIN Code', link: '/platform/code' },
            { text: 'Packages', link: '/platform/packages' },
            { text: 'Desktop App', link: '/platform/desktop-app' },
            { text: 'SIN Terminal', link: '/platform/sin-terminal' },
            { text: 'Plugins & MCP Skills', link: '/platform/plugins-mcp-skills' },
            { text: 'MyOpenSIN', link: '/platform/myopensin' },
            { text: 'Setup Complete', link: '/platform/setup-complete' },
          ],
        },
      ],
      '/agents/': [
        {
          text: 'Agents',
          items: [
            { text: 'Marketing Agents', link: '/agents/marketing-agents' },
            { text: 'A2A Fleet', link: '/agents/fleet' },
            { text: 'OMOC Swarm', link: '/agents/omoc-swarm' },
            { text: 'Agents Window', link: '/agents/agents-window' },
          ],
        },
      ],
      '/ops/': [
        {
          text: 'Operations',
          items: [
            { text: 'n8n CI/CD', link: '/ops/n8n-cicd' },
            { text: 'n8n Setup', link: '/ops/n8n-setup' },
            { text: 'HF Spaces Deployment', link: '/deployment/hf-spaces' },
            { text: 'HF Keepalive', link: '/ops/hf-keepalive' },
            { text: 'HF Space Monitoring', link: '/ops/hf-space-monitoring' },
            { text: 'HF Space Crisis', link: '/ops/hf-space-crisis' },
            { text: 'LaunchAgents', link: '/ops/launchagents' },
            { text: 'Fleet Status Report', link: '/ops/fleet-status-report' },
            { text: 'OMOC Swarm Bugs', link: '/ops/omoc-swarm-bugs' },
            { text: 'Session Report', link: '/ops/session-report-2026-04-04' },
          ],
        },
      ],
      '/community/': [
        {
          text: 'Community',
          items: [
            { text: 'Guidelines', link: '/community/guidelines' },
            { text: 'Onboarding', link: '/community/onboarding' },
            { text: 'Competitive Analysis', link: '/community/competitive-analysis' },
            { text: 'Blog Posts', link: '/community/blog-posts' },
            { text: 'Blog Post Rules', link: '/community/blog-post-rules' },
            { text: 'Alpha Scorecard', link: '/community/alpha-scorecard' },
          ],
        },
      ],
      '/governance/': [
        {
          text: 'Governance',
          items: [
            { text: 'Code of Conduct', link: '/governance/code-of-conduct' },
            { text: 'Contributing', link: '/governance/contributing' },
            { text: 'Security', link: '/governance/SECURITY' },
            { text: 'Core Principles', link: '/governance/core-principles' },
            { text: 'Onboarding Community', link: '/governance/onboarding-community' },
            { text: 'Governance & Marketing', link: '/governance/governance-marketing' },
          ],
        },
      ],
      '/vscode-extension/': [
        {
          text: 'VSCode Extension',
          items: [
            { text: 'Overview', link: '/vscode-extension/' },
            { text: 'Installation', link: '/vscode-extension/setup/installation' },
            { text: 'Architecture', link: '/vscode-extension/architecture/overview' },
            { text: 'Core Assistant', link: '/vscode-extension/features/phase1-core-assistant' },
            { text: 'Intelligence Layer', link: '/vscode-extension/features/phase2-intelligence-layer' },
            { text: 'Advanced Capabilities', link: '/vscode-extension/features/phase3-advanced-capabilities' },
            { text: 'API Overview', link: '/vscode-extension/api/' },
            { text: 'CLI Bridge', link: '/vscode-extension/api/cli-bridge' },
            { text: 'LSP Provider', link: '/vscode-extension/api/lsp-provider' },
            { text: 'Internal APIs', link: '/vscode-extension/api/internal-apis' },
            { text: 'Contributing', link: '/vscode-extension/contributing/guide' },
            { text: 'Troubleshooting', link: '/vscode-extension/troubleshooting/guide' },
            { text: 'Changelog', link: '/vscode-extension/changelog' },
          ],
        },
      ],
      '/bridges/': [
        {
          text: 'Bridges',
          items: [
            { text: 'SIN Chatroom', link: '/bridges/sin-chatroom' },
          ],
        },
      ],
      '/infrastructure/': [
        {
          text: 'Infrastructure',
          items: [
            { text: 'Overview', link: '/infrastructure/overview' },
          ],
        },
      ],
      '/guides/': [
        {
          text: 'Guides',
          items: [
            { text: 'Simone MCP Guide', link: '/guides/simone-mcp-guide' },
            { text: 'Opencode Config', link: '/guides/opencode-config' },
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
