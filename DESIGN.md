# DESIGN.md - Canonical OpenSIN Docs Design System

## Visual Identity
White-first, OpenAI-inspired content surfaces with disciplined dark-mode parity. OpenSIN Green is the primary accent and docs.opensin.ai is the visual baseline for all other surfaces.

## Colors
- **Background**: `#ffffff`
- **Elevated Surface**: `#f9fafb`
- **Primary Surface**: `#f3f4f6`
- **Primary Accent**: `#00cc88`
- **Secondary Accent**: `#00ffaa`
- **Success**: `#00cc88`
- **Text Primary**: `#111827`
- **Text Secondary**: `#4b5563`
- **Border**: `#e5e7eb`

## Typography
- **Font Family**: `Inter`, `system-ui`, `sans-serif`
- **Monospace**: `JetBrains Mono`, `Fira Code`, monospace
- **Scale**:
  - Display: 72px / 100
  - Heading: 28px / 700
  - Body: 16px / 400
  - Code: 14px / 500

## UI Components
- **Buttons**:
   - Primary: green fill, white text, compact 8px radius baseline
   - Secondary: transparent with subtle border
- **Cards**:
   - Background: `#ffffff` or `#f9fafb`
   - Border: `1px solid #e5e7eb`
   - Radius: `12px`–`18px`
- **Navigation**:
   - Sticky light bar with blur
   - Compact spacing
   - Green active state

## Icon Contract
- SVG icons must render with `display: block`
- Use rounded stroke caps and joins
- Icon wrappers should be centered, square, and visually quiet
- Feature/icon surfaces should not feel broken, clipped, or oversized

## Layout Principles
- White stacked sections with breathable spacing
- Large hero copy with simple supporting text
- Content should feel premium, minimal, and calm
- The `/api/` subpage defines the canonical docs subpage pattern

## Effects
- Soft green accent glow near heroes and CTAs
- Subtle hover lift on cards
- Fast, crisp transitions (150–200ms)
