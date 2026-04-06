import { describe, it, expect } from 'vitest';
import * as fs from 'fs';
import * as path from 'path';

describe('Documentation structure', () => {
  it('has required directories', () => {
    const dirs = ['docs', 'docs/guide', 'docs/api', 'public'];
    for (const dir of dirs) {
      expect(fs.existsSync(path.join(__dirname, '..', dir))).toBe(true);
    }
  });

  it('has LICENSE file', () => {
    expect(fs.existsSync(path.join(__dirname, '..', 'LICENSE'))).toBe(true);
  });

  it('has sitemap.xml', () => {
    expect(fs.existsSync(path.join(__dirname, '..', 'public', 'sitemap.xml'))).toBe(true);
  });

  it('has robots.txt', () => {
    expect(fs.existsSync(path.join(__dirname, '..', 'public', 'robots.txt'))).toBe(true);
  });

  it('has dependabot config', () => {
    expect(fs.existsSync(path.join(__dirname, '..', '.github', 'dependabot.yml'))).toBe(true);
  });

  it('has deploy workflow', () => {
    expect(fs.existsSync(path.join(__dirname, '..', '.github', 'workflows', 'deploy.yml'))).toBe(true);
  });
});
