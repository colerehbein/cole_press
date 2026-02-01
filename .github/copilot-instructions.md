# GitHub Copilot Instructions

> **Copilot-specific guidance for this repository.**
> For complete project context, see [AGENTS.md](../AGENTS.md).

## Project Context

This is **cole_press**, a Quarto-based personal website at [cole.press](https://cole.press).

**Tech stack:** Quarto 1.7.31 + R 4.5.1 + SCSS + LaTeX (for CV)  
**Design:** Terminal/CLI-inspired with monospace typography (Anonymous Pro)

## Build Commands

```bash
make preview    # Dev server with hot reload
make build      # Render to _site/
make setup      # Install R deps + TinyTeX
make clean      # Remove generated files
```

## File Types

| Extension | Language        | Purpose        |
| --------- | --------------- | -------------- |
| `.qmd`    | Quarto Markdown | Content pages  |
| `.scss`   | SCSS            | Theming        |
| `.yml`    | YAML            | Configuration  |
| `.tex`    | LaTeX           | CV templates   |
| `.lua`    | Lua             | Quarto filters |

## Code Patterns

### Quarto Markdown (.qmd)

````markdown
---
title: "Page Title"
description: "Brief description"
date: 2026-02-01
categories: [tech, ai]
---

## Section Header

Content with {{< fa icon-name >}} icons.

```{r}
#| label: chunk-name
#| echo: false
# R code here
```
````

````

### SCSS Theme Variables

The theme uses CSS custom properties. Key variables in `monospatial-light.scss`:

```scss
// Colors are defined as CSS custom properties
$body-bg: #ffffff;
$body-color: #333333;
$link-color: #0066cc;
$code-bg: #f5f5f5;
$font-family-monospace: "Anonymous Pro", monospace;
````

### Quarto Config (\_quarto.yml)

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "cole.press"
  navbar:
    left:
      - text: "Home"
        href: index.qmd
```

## Copilot Suggestions

### When completing `.qmd` files:

- Use Quarto shortcodes: `{{< fa brands github >}}`
- Include YAML front matter with `title`, `date`, `description`
- Use fenced R code blocks with `{r}` and options via `#|` comments

### When completing `.scss` files:

- Maintain monospace typography (Anonymous Pro)
- Use terminal-inspired color schemes
- Follow mobile-first responsive patterns

### When completing `_quarto.yml`:

- Follow Quarto YAML schema
- Navigation items need `text` and `href`
- Theme specified under `format: html: theme:`

## Key Files

- `_quarto.yml` - Site configuration
- `monospatial-light.scss` - Primary theme (1300+ lines)
- `monospatial-dark.scss` - Dark mode overrides
- `_fonts.scss` - Font face definitions
- `DESCRIPTION` - R dependencies (knitr, rmarkdown)

## Extensions Available

- **fontawesome:** `{{< fa icon-name >}}` for icons
- **quarto-cv:** PDF CV generation (uses LaTeX)

## Testing

After making changes, verify with:

```bash
quarto preview  # or: make preview
```

---

_See [AGENTS.md](../AGENTS.md) for complete documentation._
