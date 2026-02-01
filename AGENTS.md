# AI Agent Instructions

> **Canonical reference for AI coding assistants working on this repository.**
> This file is read by Codex, Claude, Copilot, Cursor, and other AI tools.

## Project Overview

**Repository:** `cole_press`  
**Website:** [https://cole.press](https://cole.press)  
**Type:** Personal website/blog built with Quarto  
**Owner:** Cole Rehbein  

A personal site featuring writings, projects, and experiments covering tech, AI, psychology, and politics. The design uses a distinctive terminal/neofetch-inspired aesthetic with monospace typography.

## Tech Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| **Quarto** | ≥1.7.31 | Static site generator (Markdown → HTML) |
| **R** | ≥4.5.1 | Code execution in `.qmd` files |
| **SCSS** | - | Theming (light/dark modes) |
| **LaTeX** | TinyTeX | PDF CV generation via `quarto-cv` extension |
| **Netlify** | - | Deployment platform |

## Directory Structure

```
cole_press/
├── _quarto.yml              # Main Quarto configuration
├── index.qmd                # Home page (terminal/neofetch style)
├── about.qmd                # About page
├── projects.qmd             # Projects showcase
├── monospatial-light.scss   # Light theme (primary)
├── monospatial-dark.scss    # Dark theme
├── _fonts.scss              # Font face definitions (Anonymous Pro)
├── fonts/                   # Self-hosted WOFF2 font files
├── _includes/
│   └── preload-fonts.html   # Font preloading for performance
├── _extensions/
│   ├── mps9506/quarto-cv/   # CV PDF extension (LaTeX-based)
│   └── quarto-ext/fontawesome/  # FontAwesome icons shortcode
├── .devcontainer/           # VS Code / Codespaces dev container
├── .github/workflows/
│   ├── deploy.yml           # Netlify deployment (main branch)
│   └── quarto.yml           # PR render check
├── Makefile                 # Build commands
├── setup.sh                 # Manual environment setup script
├── package.json             # npm deps (Netlify Quarto plugin)
├── DESCRIPTION              # R package dependencies
└── netlify.toml             # Netlify deployment config
```

## Key Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Site configuration: navigation, themes, metadata |
| `monospatial-light.scss` | Main theme (1300+ lines, terminal-inspired) |
| `monospatial-dark.scss` | Dark mode overrides |
| `_fonts.scss` | `@font-face` definitions for Anonymous Pro |
| `DESCRIPTION` | R dependencies: `knitr`, `rmarkdown` |

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
3. **Test:** Verify changes in browser at `localhost:4200`
4. **Commit:** Push to `main` triggers auto-deploy to Netlify

## Coding Conventions

### Quarto/Markdown
- Use Quarto shortcodes for icons: `{{< fa icon-name >}}`
- Front matter in YAML at top of `.qmd` files
- R code chunks use `{r}` fenced blocks
- Prefer semantic HTML classes over inline styles

### SCSS/Styling
- Design aesthetic: **Terminal/CLI-inspired, monospace typography**
- Primary font: `Anonymous Pro` (self-hosted in `fonts/`)
- Colors defined as CSS custom properties in theme files
- Light theme is primary; dark theme overrides specific values
- Mobile-first responsive design

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

## Output

- Generated site: `_site/` directory
- Excluded from git (see `.gitignore`)
- Deployed to Netlify automatically

## Common Tasks for AI Agents

### Adding a new blog post
1. Create `posts/new-post.qmd` with YAML front matter
2. Include `title`, `date`, `categories` in front matter
3. Write content in Quarto Markdown

### Modifying the theme
1. Edit `monospatial-light.scss` for light mode
2. Edit `monospatial-dark.scss` for dark mode overrides
3. Font changes go in `_fonts.scss`

### Adding a new page
1. Create `new-page.qmd` at root
2. Add navigation entry in `_quarto.yml` under `navbar`

### Testing changes
1. Run `make preview` to start dev server
2. Changes hot-reload automatically
3. Check both light and dark themes

---

*This file is designed to be read by AI coding assistants. For human contributors, see [CONTRIBUTING.md](CONTRIBUTING.md).*
