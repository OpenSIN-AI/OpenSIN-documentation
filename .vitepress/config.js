import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'OpenSIN Documentation',
  description: 'OpenSIN-AI — Autonomous AI Agent Ecosystem',
  srcDir: 'docs',
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/getting-started' },
      { text: 'API', link: '/api/' },
      { text: 'Architecture', link: '/architecture/overview' },
      { text: 'SDK', link: '/sdk/overview' },
      { text: 'Plugins', link: '/plugins/registry' },
      { text: 'Tutorials', link: '/tutorials/first-agent' },
      { text: 'Examples', link: '/examples/hello-world' },
    ],
    sidebar: [
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
          { text: 'Changelog', link: '/guide/changelog' },
          { text: 'OpenSIN Code', link: '/guide/opensin-code' },
          { text: 'OpenSIN-AI CLI (Rust)', link: '/guide/opensin-ai-cli' },
          { text: 'OpenSIN-AI Code (Python)', link: '/guide/opensin-ai-code' },
          { text: 'Rust Engine', link: '/guide/opensin-code-rust-engine' },
          { text: 'OpenSIN-AI Platform', link: '/guide/opensin-ai-platform' },
          { text: 'Agent Features vs Competitors', link: '/guide/opensin-ai-agent-features' },
        ],
      },
      {
        text: 'API',
        items: [
          { text: 'Overview', link: '/api/overview' },
          { text: 'Agent API', link: '/api/agent' },
          { text: 'A2A API', link: '/api/a2a' },
          { text: 'Team API', link: '/api/team' },
        ],
      },
      {
        text: 'Architecture',
        items: [
          { text: 'Overview', link: '/architecture/overview' },
          { text: 'Core', link: '/architecture/core' },
          { text: 'A2A', link: '/architecture/a2a' },
          { text: 'Security', link: '/architecture/security' },
          { text: 'Global Brain & Neural-Bus', link: '/architecture/global-brain-neural-bus' },
        ],
      },
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
        ],
      },
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
        ],
      },
      {
        text: 'Fleet',
        items: [
          { text: 'Overview', link: '/fleet/overview' },
        ],
      },
      {
        text: 'Governance',
        items: [
          { text: 'Overview', link: '/governance/overview' },
          { text: 'Zeus', link: '/governance/zeus' },
          { text: 'Hermes', link: '/governance/hermes' },
        ],
      },
      {
        text: 'Migrations',
        items: [
          { text: 'Overview', link: '/migrations/overview' },
        ],
      },
      {
        text: 'Tutorials',
        items: [
          { text: 'First Agent', link: '/tutorials/first-agent' },
          { text: 'Plugin Development', link: '/tutorials/plugin-development' },
          { text: 'A2A Communication', link: '/tutorials/a2a-communication' },
        ],
      },
      {
        text: 'Examples',
        items: [
          { text: 'Hello World', link: '/examples/hello-world' },
          { text: 'Multi-Agent', link: '/examples/multi-agent' },
          { text: 'Telegram Bot', link: '/examples/telegram-bot' },
          { text: 'Dual Auth Rotators', link: '/examples/dual-auth-rotators' },
        ],
      },
      {
        text: 'Best Practices',
        items: [
          { text: 'Agent Design', link: '/best-practices/agent-design' },
          { text: 'Performance', link: '/best-practices/performance' },
          { text: 'Security', link: '/best-practices/security' },
        ],
      },
      {
        text: 'Bridges',
        items: [
          { text: 'Chrome Extension', link: '/bridges/chrome-extension' },
          { text: 'OpenSIN Bridge', link: '/bridges/opensin-bridge-overview' },
        ],
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/OpenSIN-AI' },
      { icon: 'discord', link: 'https://discord.gg/opensin' },
    ],
  },
});
