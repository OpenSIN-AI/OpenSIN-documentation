import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'OpenSIN Documentation',
  description: 'OpenSIN-AI — Autonomous AI Agent Ecosystem',
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/docs/guide/getting-started' },
      { text: 'API', link: '/docs/api/' },
      { text: 'Plugins', link: '/docs/plugins/registry' },
      { text: 'Fleet', link: '/docs/fleet/overview' },
      { text: 'Tutorials', link: '/docs/tutorials/first-agent' },
    ],
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Getting Started', link: '/docs/guide/getting-started' },
          { text: 'Installation', link: '/docs/guide/installation' },
          { text: 'Quick Start', link: '/docs/guide/quick-start' },
          { text: 'Agent Basics', link: '/docs/guide/agent-basics' },
          { text: 'MCP Integration', link: '/docs/guide/mcp-integration' },
          { text: 'A2A Protocol', link: '/docs/guide/a2a-protocol' },
          { text: 'Plugin System', link: '/docs/guide/plugin-system' },
          { text: 'Team Orchestration', link: '/docs/guide/team-orchestration' },
          { text: 'Deployment', link: '/docs/guide/deployment' },
          { text: 'Monitoring', link: '/docs/guide/monitoring' },
          { text: 'Scaling', link: '/docs/guide/scaling' },
          { text: 'Troubleshooting', link: '/docs/guide/troubleshooting' },
          { text: 'Changelog', link: '/docs/guide/changelog' },
          { text: 'OpenSIN Code', link: '/docs/guide/opensin-code' },
          { text: 'OpenSIN-AI CLI (Rust)', link: '/docs/guide/opensin-ai-cli' },
          { text: 'OpenSIN-AI Code (Python)', link: '/docs/guide/opensin-ai-code' },
          { text: 'Rust Engine', link: '/docs/guide/opensin-code-rust-engine' },
          { text: 'OpenSIN-AI Platform', link: '/docs/guide/opensin-ai-platform' },
          { text: 'Agent Features vs Competitors', link: '/docs/guide/opensin-ai-agent-features' },
        ],
      },
      {
        text: 'API',
        items: [
          { text: 'Overview', link: '/docs/api/overview' },
          { text: 'Agent API', link: '/docs/api/agent' },
          { text: 'A2A API', link: '/docs/api/a2a' },
          { text: 'Team API', link: '/docs/api/team' },
        ],
      },
      {
        text: 'Architecture',
        items: [
          { text: 'Overview', link: '/docs/architecture/overview' },
          { text: 'Core', link: '/docs/architecture/core' },
          { text: 'A2A', link: '/docs/architecture/a2a' },
          { text: 'Security', link: '/docs/architecture/security' },
        ],
      },
      {
        text: 'Plugins',
        items: [
          { text: 'Registry', link: '/docs/plugins/registry' },
          { text: 'Context Pruning', link: '/docs/plugins/context-pruning' },
          { text: 'Envsitter', link: '/docs/plugins/envsitter' },
          { text: 'Handoff', link: '/docs/plugins/handoff' },
          { text: 'Safety Net', link: '/docs/plugins/safety-net' },
          { text: 'Context Analysis', link: '/docs/plugins/context-analysis' },
          { text: 'Agent Memory', link: '/docs/plugins/agent-memory' },
        ],
      },
      {
        text: 'SDK',
        items: [
          { text: 'Overview', link: '/docs/sdk/overview' },
          { text: 'Agent Loop', link: '/docs/sdk/agent-loop' },
          { text: 'Context Management', link: '/docs/sdk/context-management' },
          { text: 'Hooks', link: '/docs/sdk/hooks' },
          { text: 'Memory', link: '/docs/sdk/memory' },
          { text: 'Model Routing', link: '/docs/sdk/model-routing' },
          { text: 'Parallel Execution', link: '/docs/sdk/parallel-execution' },
          { text: 'Safety', link: '/docs/sdk/safety' },
        ],
      },
      {
        text: 'Fleet',
        items: [
          { text: 'Overview', link: '/docs/fleet/overview' },
        ],
      },
      {
        text: 'Governance',
        items: [
          { text: 'Overview', link: '/docs/governance/overview' },
          { text: 'Zeus', link: '/docs/governance/zeus' },
          { text: 'Hermes', link: '/docs/governance/hermes' },
        ],
      },
      {
        text: 'Migrations',
        items: [
          { text: 'Overview', link: '/docs/migrations/overview' },
        ],
      },
      {
        text: 'Tutorials',
        items: [
          { text: 'First Agent', link: '/docs/tutorials/first-agent' },
          { text: 'Plugin Development', link: '/docs/tutorials/plugin-development' },
          { text: 'A2A Communication', link: '/docs/tutorials/a2a-communication' },
        ],
      },
      {
        text: 'Examples',
        items: [
          { text: 'Hello World', link: '/docs/examples/hello-world' },
          { text: 'Multi-Agent', link: '/docs/examples/multi-agent' },
          { text: 'Telegram Bot', link: '/docs/examples/telegram-bot' },
          { text: 'Dual Auth Rotators', link: '/docs/examples/dual-auth-rotators' },
        ],
      },
      {
        text: 'Best Practices',
        items: [
          { text: 'Agent Design', link: '/docs/best-practices/agent-design' },
          { text: 'Performance', link: '/docs/best-practices/performance' },
          { text: 'Security', link: '/docs/best-practices/security' },
        ],
      },
      {
        text: 'Bridges',
        items: [
          { text: 'Chrome Extension', link: '/docs/bridges/chrome-extension' },
          { text: 'OpenSIN Bridge', link: '/docs/bridges/opensin-bridge-overview' },
        ],
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
  },
});
