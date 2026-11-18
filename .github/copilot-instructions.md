# GitHub Copilot Instructions

> **Copilot-specific guidance for this repository.**
> For complete project context, see [AGENTS.md](../AGENTS.md).

## Project Context

This is **cole_press**, a Quarto-based personal website at [cole.press](https://cole.press).

**Tech stack:** Quarto 1.7.31 + SCSS + LaTeX (for the CV PDFs; zero R chunks in the site)  
**Design:** Academic Brutalism (pure black borders, zero radius/shadows/transitions; Helvetica Neue prose, Anonymous Pro for data)

## Build Commands

```bash
make preview    # Dev server with hot reload
make build      # Render to _site/
make setup      # Install TinyTeX
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

::: {.callout-note}
Quarto callout (styled by the shared component layer).
:::
````

````

### SCSS Theme Variables

The theme uses CSS custom properties. Key variables in `brutalist-light.scss`:

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
- The site has zero R chunks: no `{r}` blocks

### When completing `.scss` files:

- Helvetica Neue for prose; Anonymous Pro (mono) reserved for data, dates, code
- Academic Brutalism tokens (`var(--color-*)` only; zero radius/shadows/transitions)
- Follow mobile-first responsive patterns

### When completing `_quarto.yml`:

- Follow Quarto YAML schema
- Navigation items need `text` and `href`
- Theme specified under `format: html: theme:`

## Key Files

- `_quarto.yml` - Site configuration
- `brutalist-light.scss` - Light theme tokens + palettes
- `brutalist-dark.scss` - Dark theme tokens + palettes
- `_brutalist.scss` - Shared component layer (both themes)
- `_fonts.scss` - Font face definitions

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
