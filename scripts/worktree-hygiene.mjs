#!/usr/bin/env bun
import { readdirSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = process.cwd();
const IGNORED = new Set(['node_modules', '.git', 'dist', '.vitepress', 'venv', '.opencode']);

function scan(dir, depth = 0) {
  if (depth > 3) return [];

  const hits = [];
  let entries;

  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch {
    return hits;
  }

  for (const entry of entries) {
    const full = join(dir, entry.name);

    if (entry.name === '.git') {
      if (dir !== ROOT) hits.push(full);
      continue;
    }

    if (IGNORED.has(entry.name)) continue;

    if (entry.isDirectory()) {
      hits.push(...scan(full, depth + 1));
    }
  }

  return hits;
}

export function runWorktreeHygiene() {
  const nested = scan(ROOT);

  if (nested.length > 0) {
    console.error('❌ Worktree/nested .git detected inside repository root:');
    nested.forEach((path) => console.error(`   - ${relative(ROOT, path)}`));
    console.error('\n⚠️  Worktrees must reside outside the repository root to prevent recursive scans, secret detector false positives, and VitePress watcher loops.');
    console.error('👉 Move worktrees to a sibling directory (e.g., ../OpenSIN-worktrees/) or run: git worktree prune');
    process.exit(1);
  }

  console.log('✅ Worktree hygiene check passed. No nested .git artifacts found.');
}

if (import.meta.main) {
  runWorktreeHygiene();
}
