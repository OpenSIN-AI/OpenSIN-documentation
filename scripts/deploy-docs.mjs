#!/usr/bin/env bun
const deploy = Bun.spawnSync([
  './node_modules/.bin/wrangler',
  'pages',
  'deploy',
  'docs/.vitepress/dist',
  '--project-name',
  'opensin-docs',
  '--commit-dirty=true',
], {
  cwd: process.cwd(),
  stdout: 'inherit',
  stderr: 'inherit',
});

process.exit(deploy.exitCode ?? 1);
