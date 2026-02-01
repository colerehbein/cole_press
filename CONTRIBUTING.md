# Contributing to cole_press

Thank you for your interest in contributing to cole.press! This guide covers how to set up your development environment and make changes.

## Quick Start

### Using Dev Container (Recommended)

1. Open the repository in VS Code
2. When prompted, click "Reopen in Container"
3. Wait for the container to build (includes Quarto, R, TinyTeX)
4. Run `make preview` to start the dev server

### Manual Setup

```bash
# Install dependencies (Ubuntu/Debian)
./setup.sh

# Install R packages
make setup

# Start development server
make preview
```

## Development Workflow

1. **Make changes** to `.qmd` files or SCSS themes
2. **Preview** with `make preview` (auto-reloads)
3. **Verify** changes in browser at `http://localhost:4200`
4. **Commit** and push to create a PR

## Project Structure

```
cole_press/
├── *.qmd                    # Content pages
├── _quarto.yml              # Site configuration
├── monospatial-light.scss   # Light theme
├── monospatial-dark.scss    # Dark theme
├── _fonts.scss              # Font definitions
├── fonts/                   # WOFF2 font files
├── _extensions/             # Quarto extensions
└── _site/                   # Generated output (git-ignored)
```

## Common Tasks

### Adding a Blog Post

1. Create a new file in `posts/` (create directory if needed):

   ```bash
   touch posts/my-new-post.qmd
   ```

2. Add front matter:

   ```yaml
   ---
   title: "My New Post"
   description: "A brief description"
   date: 2026-02-01
   categories: [tech, ai]
   ---
   ```

3. Write content using Quarto Markdown

4. Preview: `make preview`

### Adding a New Page

1. Create a `.qmd` file at the root:

   ```bash
   touch new-page.qmd
   ```

2. Add front matter:

   ```yaml
   ---
   title: "New Page"
   description: "Page description"
   ---
   ```

3. Add to navigation in `_quarto.yml`:
   ```yaml
   navbar:
     left:
       - text: "New Page"
         href: new-page.qmd
   ```

### Modifying Themes

**Light theme:** Edit `monospatial-light.scss`  
**Dark theme:** Edit `monospatial-dark.scss`  
**Fonts:** Edit `_fonts.scss`

The design uses a terminal/CLI-inspired aesthetic with:

- Monospace typography (Anonymous Pro)
- Clean, minimal colors
- Box-drawing characters for borders

### Using Icons

Use the FontAwesome extension:

```markdown
{{< fa brands github >}} # Brand icons
{{< fa solid envelope >}} # Solid icons
{{< fa regular star >}} # Regular icons
```

### Adding R Code

Use fenced code blocks with options:

````markdown
```{r}
#| label: my-analysis
#| echo: false
#| warning: false

library(dplyr)
data %>% summarize(mean = mean(value))
```
````

## Available Commands

| Command        | Description                      |
| -------------- | -------------------------------- |
| `make preview` | Start dev server with hot reload |
| `make build`   | Render site to `_site/`          |
| `make setup`   | Install R packages and TinyTeX   |
| `make clean`   | Remove generated files           |
| `make help`    | Show all available commands      |

## Code Style

### Quarto/Markdown

- Use Quarto shortcodes for icons (`{{< fa >}}`)
- Include descriptive front matter
- Use semantic section headers

### SCSS

- Follow existing naming conventions
- Use CSS custom properties for colors
- Mobile-first responsive design
- Maintain terminal-inspired aesthetic

### General

- Keep commits focused and atomic
- Write descriptive commit messages
- Test changes locally before pushing

## Testing

Before submitting changes:

1. Run `make preview` and verify in browser
2. Check both light and dark themes
3. Test on mobile viewport sizes
4. Ensure `make build` completes without errors

## CI/CD

- **Pull requests:** Automatic render check via GitHub Actions
- **Main branch:** Auto-deploy to Netlify

## Need Help?

- Check [AGENTS.md](AGENTS.md) for technical reference
- Review existing `.qmd` files for examples
- See [Quarto documentation](https://quarto.org/docs/)

---

_For AI agents: see [AGENTS.md](AGENTS.md) for machine-readable project documentation._
