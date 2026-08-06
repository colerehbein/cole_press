# AI Agent Instructions

> **Canonical reference for AI coding assistants working on this repository.**
> This file is read by Codex, Claude, Copilot, Cursor, and other AI tools.
> For humans: [SITE-GUIDE.md](SITE-GUIDE.md) covers day-to-day content updates.

## Project Overview

**Repository:** `cole_press`  
**Website:** [https://cole.press](https://cole.press)  
**Type:** Personal website/blog built with Quarto  
**Owner:** Cole Rehbein

A personal site for a crisis counselor and clinical psychology researcher — audience: mental-health professionals and clients. The design is **Academic Brutalism** (ported from the IPIP Repository design system): white/off-white surfaces, pure black borders, zero radius/shadows/transitions, Helvetica Neue body text, uppercase labels, monospace only for data — plus two flourishes: a switchable **accent palette** (5 colors) and a **rainbow stripe** under the header.

## Tech Stack

| Component   | Version | Purpose                                     |
| ----------- | ------- | ------------------------------------------- |
| **Quarto**  | ≥1.7.31 | Static site generator (Markdown → HTML)     |
| **R**       | ≥4.5.1  | Code execution in `.qmd` files              |
| **SCSS**    | -       | Theming (light/dark modes)                  |
| **LaTeX**   | TinyTeX | PDF CV generation via `quarto-cv` extension |
| **Netlify** | -       | Deployment platform                         |

## Directory Structure

```
cole_press/
├── _quarto.yml              # Main Quarto configuration
├── index.qmd                # Home page (kicker, abstract, directory index, sidebar)
├── about.qmd                # About page (prose + career timeline)
├── research.qmd             # Research page (thesis, review, EEG, methods)
├── projects.qmd             # Projects showcase (card grid)
├── 404.qmd                  # Custom not-found page (renders 404.html)
├── portfolio/
│   ├── index.qmd            # Portfolio landing (Photos + Writing cards)
│   ├── photos.qmd           # Photo gallery grid
│   └── writing.qmd          # Writing index (essays, journalism, academic)
├── blog/
│   ├── index.qmd            # Blog listing + RSS feed (feed: true → /blog/index.xml)
│   ├── _metadata.yml        # Shared front matter for blog pages
│   └── posts/               # Posts: YYYY-MM-DD-slug.qmd
├── cv/
│   ├── index.qmd            # Web CV page (links both PDFs)
│   ├── full-cv.qmd          # Full CV source → cole-rehbein-cv.pdf
│   └── resume.qmd           # One-page résumé source → cole-rehbein-resume.pdf
├── brutalist-light.scss     # Light theme: tokens + Bootstrap bridge + palettes
├── brutalist-dark.scss      # Dark theme: tokens + Bootstrap bridge + palettes
├── _brutalist.scss          # SHARED component layer (imported by BOTH themes)
├── _fonts.scss              # Font face definitions (Anonymous Pro)
├── fonts/                   # Self-hosted WOFF2 font files
├── og-image.png             # 1200×630 Open Graph social card
├── _includes/
│   ├── preload-fonts.html   # Font preloading for performance
│   ├── accent-palette.html  # Palette boot script + navbar picker JS
│   ├── portfolio-nav.html   # Portfolio navbar: click-navigates on desktop, dropdown on hover
│   └── home-no-title.html   # Hides Quarto title block on the home page
├── _extensions/
│   ├── mps9506/quarto-cv/   # CV PDF extension (LaTeX-based)
│   └── quarto-ext/fontawesome/  # FontAwesome icons shortcode
├── docs/design/
│   ├── README.md            # Design system overview + principles
│   └── catalog.md           # Complete token + class catalog
├── SITE-GUIDE.md            # Human-facing how-to guide
├── .devcontainer/           # VS Code / Codespaces dev container
├── .github/workflows/
│   ├── deploy.yml           # Netlify deployment (main branch)
│   └── quarto.yml           # PR render check
├── Makefile                 # Build commands
├── setup.sh                 # Manual environment setup script
├── package.json             # npm deps (Netlify Quarto plugin)
├── DESCRIPTION              # R package dependencies
├── _redirects               # Netlify redirect rules (see "Redirects & Domains")
└── netlify.toml             # Netlify deployment config
```

## Key Files

| File                     | Purpose                                          |
| ------------------------ | ------------------------------------------------ |
| `_quarto.yml`            | Site configuration: navigation, themes, metadata |
| `brutalist-light.scss`   | Light tokens + Bootstrap bridge + accent palettes |
| `brutalist-dark.scss`    | Dark tokens + Bootstrap bridge + accent palettes |
| `_brutalist.scss`        | ALL component CSS — shared by both themes, never duplicated |
| `blog/index.qmd`         | Blog listing page; `feed: true` generates RSS at `/blog/index.xml` |
| `cv/full-cv.qmd`         | Full CV source (PDF via quarto-cv)               |
| `cv/resume.qmd`          | One-page résumé source (PDF via quarto-cv)       |
| `_includes/accent-palette.html` | Accent palette persistence + navbar picker  |
| `SITE-GUIDE.md`          | How to update content, palettes, fonts, deploy   |
| `docs/design/catalog.md` | Design token + class catalog                     |

## Build Commands

```bash
# Quick commands via Makefile
make preview    # Start local dev server with live reload
make build      # Render site to _site/
make setup      # Install R packages and TinyTeX
make clean      # Remove generated files

# Direct Quarto commands
quarto preview  # Dev server at http://localhost:4200
quarto render   # Generate static HTML to _site/
```

## Development Workflow

1. **Edit content:** Modify `.qmd` files (Quarto Markdown)
2. **Preview:** Run `make preview` or `quarto preview`
3. **Test:** Verify changes in browser at `localhost:4200` (both light/dark, all palettes)
4. **Commit:** Push to `main` triggers auto-deploy to Netlify

## Coding Conventions

### Quarto/Markdown

- Use Quarto shortcodes for icons: `{{< fa icon-name >}}`
- Front matter in YAML at top of `.qmd` files
- R code chunks use `{r}` fenced blocks
- **Raw HTML in `.qmd` files must be unindented to column 0** — pandoc turns indented `<dt>`/`<dd>`/`<p>` lines into escaped code blocks
- Never add page-scoped `<style>` blocks to `.qmd` files — component styles go in `_brutalist.scss`
- `include-in-header` at the document level (e.g. `index.qmd` hiding the title block) is the only accepted per-page CSS

### SCSS/Styling — Academic Brutalism

- **Invariants:** zero `border-radius` (exceptions: `.badge` pill, inline `code` 4px); zero `box-shadow`; zero `transition`; borders are `var(--color-border)` (1px containers, 2px structural emphasis)
- **Tokens only:** components use `var(--color-*)` custom properties — never hardcode colors
- **Architecture:** tokens live in the theme files (`brutalist-*.scss`); ALL component CSS lives in `_brutalist.scss`, imported by both themes — light and dark can never drift
- Accent palettes (`[data-palette="..."]` blocks) override only `--color-primary`/`--color-primary-hover`/`--color-accent`/`--color-focus-ring`; palette blocks are defined per theme (light values in the light file, dark in the dark file)
- The rainbow stripe (`#quarto-header::after`) is the only multicolor element — fixed colors, never per-palette
- Body font: Helvetica Neue system stack; mono: Anonymous Pro (self-hosted in `fonts/`)
- Headings use NEGATIVE tracking; uppercase labels use POSITIVE tracking
- Hovers exist but are instant (no transitions)
- Palette values live in **both** theme files — when adding a palette, update both + `_includes/accent-palette.html` + `--swatch-*` tokens

### File Naming

- Content pages: `kebab-case.qmd`
- SCSS partials: `_name.scss`
- Extensions: Located in `_extensions/`

## Extensions

### quarto-cv (mps9506/quarto-cv)

- Generates PDF CVs using LaTeX
- Requires TinyTeX or system LaTeX installation
- Config in `_extensions/mps9506/quarto-cv/`

### fontawesome (quarto-ext/fontawesome)

- Icon shortcode: `{{< fa brands github >}}`
- Supports Font Awesome 6 icons
- Config in `_extensions/quarto-ext/fontawesome/`

## Dependencies

### R Packages (from DESCRIPTION)

- `knitr` - Code chunk execution
- `rmarkdown` - Document rendering

### System Libraries (for R package compilation)

- `libcurl4-openssl-dev`
- `libssl-dev`
- `libxml2-dev`

### npm (from package.json)

- `@quarto/netlify-plugin-quarto` - Netlify integration

## CI/CD

- **Main branch push:** Triggers full render and Netlify deploy
- **Pull requests:** Render check with artifact upload
- Workflows in `.github/workflows/`
- Both workflows set `tinytex: true` in the Quarto setup step — required for the CV/résumé PDFs (`quarto-cv-pdf` format) to render in CI; removing it breaks `quarto render` on `cv/full-cv.qmd`

## Redirects & Domains

`_redirects` (copied into `_site/` at render time) defines Netlify rules:

- `https://blog.cole.press/* → https://cole.press/blog/:splat` (301) — subdomain shortcut to the in-site blog. **Requires `blog.cole.press` to be attached as a domain alias in the cole.press Netlify site's dashboard**; until then the rule never fires.
- Legacy `.html` URLs (`/index.html`, `/about.html`, `/projects.html`, `/cv/index.html`) 301 to their clean URLs.

## Output

- Generated site: `_site/` directory
- Excluded from git (see `.gitignore`)
- Deployed to Netlify automatically

## Common Tasks for AI Agents

### Adding a new blog post

1. Create `blog/posts/YYYY-MM-DD-slug.qmd` with YAML front matter
2. Include `title`, `description`, `author`, `date`, `categories` in front matter
3. Write content in Quarto Markdown
4. The listing page and RSS feed (`/blog/index.xml`) update automatically on render — no extra config needed

### Modifying the theme

1. Token values (light/dark colors): edit `brutalist-light.scss` / `brutalist-dark.scss` only
2. Component styles: edit `_brutalist.scss` only (never a theme file)
3. Adding an accent palette: both theme files (light+dark values) + `--swatch-*` tokens + `_includes/accent-palette.html` registration
4. Font changes: `$font-family-*` in both theme files + `_fonts.scss` + `_includes/preload-fonts.html`

### Adding a new page

1. Create `new-page.qmd` at root
2. Add navigation entry in `_quarto.yml` under `navbar`

### Testing changes

1. Run `make preview` to start dev server
2. Changes hot-reload automatically
3. Check both light and dark themes AND multiple accent palettes (navbar swatches)
4. Check mobile (<640px: sidebar stacks, grid collapses)

---

_This file is designed to be read by AI coding assistants. For human contributors, see [SITE-GUIDE.md](SITE-GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md)._
