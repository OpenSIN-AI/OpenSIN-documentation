# Contributing to OpenSIN Documentation

## Code Quality Standards

### Pull Request Process
1. Create a feature branch from `main`
2. Make your changes
3. Run `npm run docs:build` to verify build passes
4. Submit PR with descriptive title and body
5. Wait for review before merging

### Documentation Standards
- Use Markdown with VitePress extensions
- Include code examples for all tutorials
- Keep language clear and concise
- Link to related pages

### File Structure
```
docs/
├── guide/          # User guides
├── api/            # API reference
├── architecture/   # Architecture docs
├── bridges/        # Bridge documentation
└── .vitepress/     # VitePress config
```

### Commit Messages
- `docs:` for documentation changes
- `feat:` for new features
- `fix:` for bug fixes
- `chore:` for maintenance

### Review Checklist
- [ ] Build passes (`npm run docs:build`)
- [ ] No broken links
- [ ] Code examples are tested
- [ ] Spelling and grammar checked
