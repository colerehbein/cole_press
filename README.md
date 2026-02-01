# cole_press

[![Netlify Status](https://api.netlify.com/api/v1/badges/placeholder/deploy-status)](https://cole.press)

Personal website at [cole.press](https://cole.press) — writings, projects, and experiments covering tech, AI, psychology, and politics.

Built with **Quarto** + **R** + **SCSS** featuring a terminal/CLI-inspired design.

## Quick Start

### Option 1: Dev Container (Recommended)

1. Open in VS Code
2. Click "Reopen in Container" when prompted
3. Run `make preview`

### Option 2: Manual Setup

```bash
./setup.sh          # Install Quarto and R
make setup          # Install R packages and TinyTeX
make preview        # Start dev server
```

## Prerequisites

| Tool | Version | Installation |
|------|---------|--------------|
| Quarto | ≥1.7.31 | [quarto.org](https://quarto.org/docs/get-started/) |
| R | ≥4.5.1 | [r-project.org](https://www.r-project.org/) |
| TinyTeX | latest | `quarto install tinytex` |

**System libraries** (Ubuntu/Debian):
```bash
sudo apt-get install libcurl4-openssl-dev libssl-dev libxml2-dev
```

## Commands

```bash
make preview    # Dev server at localhost:4200 (hot reload)
make build      # Render site to _site/
make setup      # Install R packages + TinyTeX
make clean      # Remove generated files
make check      # Verify installation
make help       # Show all commands
```

## Project Structure

```
cole_press/
├── *.qmd                    # Content pages (Quarto Markdown)
├── _quarto.yml              # Site configuration
├── monospatial-light.scss   # Light theme (primary)
├── monospatial-dark.scss    # Dark theme
├── _fonts.scss              # Font definitions (Anonymous Pro)
├── _extensions/             # Quarto extensions (fontawesome, quarto-cv)
├── .devcontainer/           # VS Code dev container config
└── _site/                   # Generated output (git-ignored)
```

## Documentation

| Document | Purpose |
|----------|---------|
| [AGENTS.md](AGENTS.md) | AI agent reference (Codex, Claude, Copilot) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [CLAUDE.md](CLAUDE.md) | Claude-specific instructions |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | GitHub Copilot context |

## Tech Stack

- **[Quarto](https://quarto.org)** — Static site generator
- **[R](https://www.r-project.org)** — Code execution in documents
- **SCSS** — Custom theming with terminal-inspired design
- **[Netlify](https://netlify.com)** — Deployment and hosting
- **TinyTeX** — PDF CV generation via quarto-cv extension

## License

Content © Cole Rehbein. See individual files for specific licenses.
