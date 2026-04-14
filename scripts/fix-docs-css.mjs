/**
 * Post-build fix: Convert CSS preload to active stylesheets
 * VitePress generates <link rel="preload stylesheet"> which doesn't work in all browsers
 * This converts them to proper <link rel="stylesheet">
 */
import { readFileSync, writeFileSync, readdirSync, statSync } from 'fs';
import { join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const distDir = join(__dirname, '..', '.vitepress', 'dist');

function fixHtmlInDir(dir) {
  let fixed = 0;
  for (const file of readdirSync(dir)) {
    const fullPath = join(dir, file);
    const stat = statSync(fullPath);
    if (stat.isDirectory()) {
      fixed += fixHtmlInDir(fullPath);
    } else if (file.endsWith('.html')) {
      let content = readFileSync(fullPath, 'utf-8');
      content = content.replace(
        /<link rel="preload stylesheet" href="([^"]+)" as="style">/g,
        '<link rel="stylesheet" href="$1">'
      );
      writeFileSync(fullPath, content, 'utf-8');
      fixed++;
    }
  }
  return fixed;
}

console.log('Fixing CSS in:', distDir);
const count = fixHtmlInDir(distDir);
console.log('Fixed', count, 'HTML files');
