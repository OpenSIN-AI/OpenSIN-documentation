# OpenSIN Documentation Repair Log

## 🐛 BUG-001: Button Hover Shape Loss (FIXED 2026-04-16)

**Symptom:** Buttons lose their 8px border-radius upon mouseover/hover, reverting to default pill or sharp shapes.
**Root Cause:** The CSS `:hover` state for `.VPButton` in VitePress was not inheriting the `!important` border-radius from the base class.
**Fix:** Explicitly defined `border-radius: 8px !important` on both `.VPButton` and `.VPButton:hover`.
**Evidence:** [Image 1] from user session.

**Permanent contract:**
- Homepage CTA buttons must stay compact and premium.
- Hover must preserve shape, color contrast, and spacing.
- Future CSS changes must treat button hover as protected UI state.

---

## ⚖️ Mandates for Future Agents

1. **DO NOT** remove the 8px border-radius from buttons.
2. **ALWAYS** test hover states before deploying.
3. **DOCUMENT** every visual fix in this file.
