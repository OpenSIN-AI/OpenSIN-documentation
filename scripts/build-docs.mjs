#!/usr/bin/env bun
import { build } from 'vitepress';
import { runWorktreeHygiene } from './worktree-hygiene.mjs';

await runWorktreeHygiene();
await build('docs');
