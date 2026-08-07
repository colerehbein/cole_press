# Academic Brutalism — Design System (cole.press)

This site uses **Academic Brutalism**, ported from the [IPIP Repository](https://ipip.ipsyc.io) design system. Raw, unpolished, scientific: no rounded corners, no shadows, no transitions, pure black borders, system sans-serif, uppercase labels, monospace for data. The design signals seriousness — not a SaaS product, but a professional and clinical researcher's site.

## Documents

| Document | Purpose |
|---|---|
| [Catalog](./catalog.md) | Every token, class, and pattern with exact values. |
| [Site Guide](../../SITE-GUIDE.md) | How to update content (posts, pages, palettes, fonts). |

## Core principles

1. **No radius** — `--radius: 0px` everywhere. Exceptions: `.badge` pill (`100px`), inline `code` (`4px`).
2. **No shadows** — `--shadow-*: none` everywhere.
3. **No transitions** — `--transition: 0ms`. All hovers are instant.
4. **Pure black borders** — `--color-border: #000000` (light). 2px for structural emphasis, 1px for containers.
5. **Raw hyperlink blue** — `--color-primary: #0000ee` (light), switchable via accent palettes.
6. **Helvetica Neue** — system sans-serif; no web fonts for body text.
7. **Uppercase labels** — `text-transform: uppercase`, `letter-spacing: 0.05em+`.
8. **Monospace for data** — Anonymous Pro (self-hosted) for codes, dates, numbers.
9. **Off-white surfaces** — `#fcfcfc`/`#f5f5f5` for subtle box differentiation.
10. **Grid-heavy layouts** — CSS Grid with `minmax()` for card grids.
11. **Two allowed flourishes** — the accent palette switcher (6 options: a rainbow default + five solids) and the rainbow stripe under the header.
12. **Tokens only** — components use `var(--color-*)`; never hardcode colors that exist as tokens.

## Token quick reference

| Token | Light | Dark |
|---|---|---|
| `--color-bg` | `#ffffff` | `#1a1a1a` |
| `--color-surface` | `#ffffff` | `#242424` |
| `--color-primary` | `#0000ee` | `#6b9eff` |
| `--color-primary-hover` | `#551a8b` | `#a78bfa` |
| `--color-primary-light` | `#f5f5f5` | `#2a2a2a` |
| `--color-text` | `#000000` | `#f0f0f0` |
| `--color-text-secondary` | `#333333` | `#d0d0d0` |
| `--color-muted` | `#666666` | `#999999` |
| `--color-border` | `#000000` | `#777777` |
| `--color-border-light` | `#e5e5e5` | `#383838` |
| `--color-positive` / `--color-negative` | `#006600` / `#cc0000` | `#4ade80` / `#ff6b6b` |
| `--radius`, `--radius-lg` | `0px` | `0px` |
| `--shadow-*` | `none` | `none` |
| `--font-mono` | Anonymous Pro stack | same |

Semantic surfaces (`--color-hover-bg`, `--color-code-bg`, `--color-warning-*`, `--color-error-*`, `--color-clinical-*`, …) follow the IPIP dark/light sets — see the theme files for the full table.

## Accent palettes

Six palettes, switchable from the navbar (persisted in `localStorage["cole-palette"]`), **rainbow being the default**. Solid palettes override ONLY accent tokens (`--color-primary`, `--color-primary-hover`, `--color-accent`, `--color-focus-ring`). The rainbow palette does the same for its base accent, plus adds `--rainbow-1..6` which cycle across link lists/titles.

| Palette | Light primary / hover | Dark primary / hover |
|---|---|---|
| **rainbow** (default) | base `#0000ee` / `#551a8b`; links cycle `--rainbow-1..6` | base `#6b9eff` / `#a78bfa`; links cycle dark `--rainbow-1..6` |
| classic | `#0000ee` / `#551a8b` | `#6b9eff` / `#a78bfa` |
| violet | `#7c3aed` / `#5b21b6` | `#a78bfa` / `#c4b5fd` |
| green | `#006600` / `#004d00` | `#4ade80` / `#86efac` |
| amber | `#b45309` / `#92400e` | `#fbbf24` / `#fde68a` |
| crimson | `#cc0000` / `#990000` | `#ff6b6b` / `#fca5a5` |

### Rainbow link hues (`--rainbow-1..6`)

| Var | Hue | Light | Dark |
|---|---|---|---|
| `--rainbow-1` | red | `#cc0000` | `#ff6b6b` |
| `--rainbow-2` | orange | `#b45309` | `#fbbf24` |
| `--rainbow-3` | green | `#006600` | `#4ade80` |
| `--rainbow-4` | blue | `#0a6ebd` | `#6b9eff` |
| `--rainbow-5` | purple | `#6d28d9` | `#c084fc` |
| `--rainbow-6` | teal | `#0e7490` | `#22d3ee` |

Under rainbow, links in lists and post titles alternate through these hues (see "Rainbow link theming" in the catalog). Nav, footer, dropdown, prose links, and buttons keep the base single accent. Picking any solid palette switches everything to that one hue.

## Rainbow stripe

The one multicolor element on the site: a 4px full-width bar directly under the header, rendered as hard-stop stripes (flat segments, not a gradient blend) — `#ff6b6b #f8e71c #00c9a7 #4dabf7 #a66dd4`. Fixed colors in both themes; never per-palette.

## Architecture

- `brutalist-light.scss` / `brutalist-dark.scss` — tokens + Bootstrap SCSS bridge + palette blocks. **Only token values differ.**
- `_brutalist.scss` — every component rule, imported by both themes. Components use `var(--color-*)` only.
- `_includes/accent-palette.html` — boot script (no-flash) + navbar picker.
- `_includes/home-no-title.html` — hides the Quarto title block on `/`.

## Adding new components

1. Put the CSS in `_brutalist.scss` (never in a theme file, never inline in a `.qmd`).
2. Use design tokens (`var(--color-*)`) — no hardcoded colors.
3. Follow the invariants above (0 radius, no shadow, no transition).
4. Add a `/* ── Section Name ── */` header comment.
5. Document the class in `catalog.md`.
