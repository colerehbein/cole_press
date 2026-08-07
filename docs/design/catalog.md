# Academic Brutalism — Design Token & Class Catalog (cole.press)

> Source: `_brutalist.scss` + `brutalist-light.scss` + `brutalist-dark.scss`
> Ported from the IPIP Repository design system.

## 1. Design tokens (CSS custom properties)

Defined in `:root` in each theme file. Light values in `brutalist-light.scss`, dark values in `brutalist-dark.scss`.

| Token | Light | Dark | Purpose |
|---|---|---|---|
| `--color-bg` | `#ffffff` | `#1a1a1a` | Page background |
| `--color-surface` | `#ffffff` | `#242424` | Card/container surfaces |
| `--color-primary` | `#0000ee` | `#6b9eff` | Links, focus, primary buttons, badges (palette-switchable) |
| `--color-primary-hover` | `#551a8b` | `#a78bfa` | Hover/visited |
| `--color-primary-light` | `#f5f5f5` | `#2a2a2a` | Tint backgrounds (abstract box, badges) |
| `--color-text` | `#000000` | `#f0f0f0` | Body text |
| `--color-text-secondary` | `#333333` | `#d0d0d0` | Secondary text |
| `--color-muted` | `#666666` | `#999999` | Labels, metadata |
| `--color-border` | `#000000` | `#777777` | All borders |
| `--color-border-hover` | `#000000` | `#999999` | — |
| `--color-border-light` | `#e5e5e5` | `#383838` | Interior hairlines |
| `--color-positive` | `#006600` | `#4ade80` | Positive/success text |
| `--color-negative` | `#cc0000` | `#ff6b6b` | Errors/negative |
| `--color-accent` | `#0000ee` | `#6b9eff` | Accent (follows palette) |
| `--color-focus-ring` | color-mix(primary 15%, transparent) | same | Focus ring |
| `--color-hover-bg` | `#f8fafc` | `#2a2a2a` | Row/card hover |
| `--color-code-bg` | `#f1f5f9` | `#2e2e2e` | Inline code + code blocks |
| `--color-warning-bg/border/text` | `#fef3c7`/`#f59e0b`/`#92400e` | `#2a1a00`/`#b45309`/`#fbbf24` | Warning callouts |
| `--color-error-bg/border` | `#fef2f2`/`#fecaca` | `#2e0d0d`/`#7f1d1d` | Error callouts |
| `--color-clinical*` | `#8b0000` family | `#ff8a8a` family | Clinical content (CV) |
| `--radius` / `--radius-lg` | `0px` | `0px` | Zero everywhere |
| `--shadow-sm/md/lg` | `none` | `none` | — |
| `--transition` | `0ms` | `0ms` | — |
| `--font-mono` | Anonymous Pro stack | same | Code, dates, data |
| `--swatch-*` | per-palette hexes | per-palette hexes | Navbar picker swatch colors |
| `--rainbow-1..6` | `#cc0000…#0e7490` | `#ff6b6b…#22d3ee` | Link-cycle hues (palette-only) — see "Rainbow link theming" |

Bootstrap runtime zeroing (also in `:root`): `--bs-border-radius: 0`, `--bs-box-shadow: none` (+sm/lg).

## 2. Typography

| Pattern | Spec |
|---|---|
| Body | `"Helvetica Neue", Helvetica, Arial, sans-serif`, `line-height: 1.6`, antialiased |
| h1 (page title) | `2rem`, 700, `-0.02em` |
| h2 | `1.5rem`, 700, `-0.02em` |
| h3 (sections) | `1.125rem`, 700, uppercase, `0.05em`, `border-bottom: 1px` |
| `.home-title` | `2.5rem`, 700, `-0.03em`, `line-height: 1.1` |
| `.home-kicker` | `0.7rem`, 700, uppercase, `0.08em`, muted |
| Nav links / labels | `0.85rem`, 600, uppercase, `0.05em` |
| `.home-sidebar-title` | `0.72rem`, 700, uppercase, `0.08em`, bottom border |
| Meta/small | `0.75–0.85rem`, muted |
| Inline `code` | mono, `0.8125em`, `--color-code-bg`, radius `4px` (allowed) |
| Data/numbers | mono, `0.72–0.85rem` |

## 3. Components

### Header / navbar (Quarto re-skin)
- `#quarto-header` — surface background; `::after` = the 4px rainbow stripe (hard-stop `linear-gradient`).
- `.navbar` — surface bg, `border-bottom: 2px solid var(--color-text)`.
- `.navbar-brand` — uppercase, `1.125rem`, 700, `0.05em`.
- `.navbar .nav-link` — uppercase, `0.85rem`, 600; hover = primary color + 2px primary underline; active = 2px text-color underline.
- `.navbar-toggler` — 1px border, 0 radius (mobile).
- `.quarto-color-scheme-toggle` — bare muted button.
- `.palette-picker` / `.palette-swatch` — 6 square 14px swatches (rainbow = hard-stop striped gradient), active = 2px outline; hidden ≤640px.

### Footer (`page-footer` → `.nav-footer`)
Top border 1px; links uppercase `0.8rem`, 700, underlined; muted text.

### Buttons
- `.btn` — 1px border, 0 radius, surface bg; hover: primary border/color + `--color-primary-light` bg.
- `.btn-primary` — primary bg, white text; hover: primary-hover.
- `.btn-sm` — `0.8rem`, `0.3rem 0.75rem`.

### Cards
- `.card` — 1px border, 0 radius, no shadow, `1.25rem 1.5rem` padding; hover `translateY(-1px)` (instant).
- `.card-grid` — `repeat(auto-fill, minmax(280px, 1fr))`, gap 1rem.
- `.project-card-title` / `.project-card-body` / `.project-card-links` — card internals (Projects page).

### Badges
- `.badge` — pill (`100px` radius — the allowed exception), `--color-primary-light` bg, primary text, uppercase `0.6875rem`/600.

### Tables
- `.table` — collapsed borders, th uppercase `0.6875rem` with 2px bottom border, td `0.625rem 1rem` padding + 1px borders, row hover `--color-hover-bg`.

### Forms
- Inputs/selects/textareas — 1px border, 0 radius, surface bg; focus: primary border + `0 0 0 3px var(--color-focus-ring)`.
- `.quick-search-form` / `.quick-search-input` / `.quick-search-btn` — newsletter: shared-border input + inverted GO button (text-color bg, bg-color text).

### Callouts
- `.callout` — 3px left border, 0 radius, no shadow; `.callout-warning` / `.callout-danger` use warning/error tokens.

### Timeline (About page)
- `.ipip-timeline-line` — 2px left spine, `2.25rem` padding-left.
- `.ipip-timeline-item` — hairline bottom border.
- `.ipip-timeline-dot` — 8px solid black square on the spine.
- `.ipip-timeline-year` — mono uppercase `0.75rem`/700/`0.12em`, muted.
- `.ipip-timeline-title` — `1.0625rem`/700.
- `.ipip-timeline-desc` — `0.9375rem`, secondary, `line-height: 1.65`.
- `.ipip-timeline-tag` — 1px border, uppercase `0.7rem`.

### Directory list (home index + CV)
- `.directory-list` — 1px top+bottom borders.
- `.directory-entry` — grid `180px 1fr` (stacks ≤768px), `1rem 0` padding, hairline separators.
- `.directory-term` — semibold; link = primary, underlined.
- `.directory-desc` — secondary color.

### CV entries
- `.cv-entry` — grid `220px 1fr` (stacks ≤640px), hairline separators.
- `.cv-role` — 700. `.cv-org` — secondary. `.cv-detail` — secondary, `0.9rem`.
- `.cv-meta` — mono uppercase `0.72rem` muted date line.

### Home page
- `.home-container` — `1040px` max-width, centered.
- `.home-layout` — grid `1fr 280px`, 2px top border; stacks ≤640px (sidebar loses left border, gains top border).
- `.home-abstract` — 1px border, `--color-primary-light` bg.
- `.home-meta` — muted `0.8rem`.
- `.home-start-hint` — 1px border; `.home-start-hint-label` inverted (text-color bg, bg-color text); `.home-start-hint-body` `0.85rem`.
- `.home-section-title` — `1.25rem`, `0.03em`.
- `.home-sidebar-section` / `.home-sidebar-title` — sidebar blocks.
- `.instrument-links` — sidebar link list (`.link-label` = mono muted label).
- `.changelog-list` / `.changelog-entry` — "Currently" rows (`auto 1fr` grid).

### Blog listing (Quarto re-skin)
- `.quarto-listing .quarto-post` — `1rem 0` padding, hairline bottom border (`!important` — Quarto's client-side listing CSS otherwise wins the cascade).
- `.quarto-listing .quarto-post .thumbnail` — hidden (text-only blog).
- `.listing-title` — `1.125rem`/700, primary underlined link.
- `.listing-date` — mono uppercase muted.
- `.listing-description` — secondary.
- `.listing-categories .listing-category` — pill badges (primary-light bg, primary text).
- `.quarto-listing-category .category` — filter buttons: 1px border, 0 radius; active = primary-light bg + primary text.
- `.quarto-listing-category-title` — uppercase `0.72rem` muted.

### Quarto chrome
- `.quarto-title-block h1` — `2rem`, `-0.02em`.
- `.toc` — uppercase `0.72rem` header, secondary links, active primary.
- `.pagination .page-link` — 0 radius, 1px borders; active = inverted (text-color bg).
- `.skip-link` — off-screen until focused (a11y).
- Global `:focus-visible` — `2px solid var(--color-primary)`, offset 2px.
- `.visually-hidden` — screen-reader-only utility.

### Misc
- `.empty-state-page` — centered muted placeholder.
- `.error` — negative color on error-bg with error-border.
- `::selection` — primary bg, bg-color text.

### Photo gallery (Portfolio)
- `.photo-grid` — `repeat(auto-fill, minmax(240px, 1fr))`, gap 1rem.
- `.photo-frame` — 1px border, 0 radius, square (`aspect-ratio: 1 / 1`), centered content, `overflow: hidden`.
- `.photo-placeholder` — mono uppercase muted label inside an empty frame.
- Adding photos: drop images in `portfolio/photos/` and replace a placeholder with `<figure class="photo-frame"><img src="photos/…" alt="…" loading="lazy"></figure>`.

## 3.5 Rainbow link theming (default palette)

When `[data-palette="rainbow"]` is active, links alternate through `--rainbow-1..6` (red › orange › green › blue › purple › teal) across:

- `.directory-list .directory-entry .directory-term a` — home index, portfolio writing, 404
- `.instrument-links li a` — home sidebar Links
- `.quarto-post .listing-title a` — blog post titles

Rules use **enumerated `:nth-child(1)` … `:nth-child(24)`** (cycle length 6) — do NOT use `an+b` formulas like `6n+1`: this build's CSS minifier rewrites `6n+1` → `7n`, which selects the wrong children. Rainbow links keep their hue on hover/visited; nav, footer, dropdown, prose links, and buttons keep the base single accent. Selecting any solid palette overrides the rainbow site-wide.

## 4. Responsive breakpoints

| Breakpoint | Effect |
|---|---|
| ≤768px | `.directory-entry` stacks to one column |
| ≤640px | `.home-layout` single column, sidebar reflows, `.cv-entry` stacks, palette picker hidden |
| ≤420px | `.home-title` → `2rem`, `.card` padding reduced |

## 5. Invariants (violating any of these is a bug)

1. Zero radius (exceptions: `.badge`, `code`).
2. Zero shadows. 3. Zero transitions.
4. Colors from tokens only — no hardcoded hexes in components.
5. 2px borders only for structural emphasis.
6. Headings: negative tracking. Labels: uppercase + positive tracking.
7. Palette changes accent colors ONLY — never borders or surfaces.
8. Rainbow stripe is the only multicolor element.
