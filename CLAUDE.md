# Claude Instructions

> **Claude-specific guidance for this repository.**
> For complete project context, see [AGENTS.md](AGENTS.md).

## Project Summary

This is a Quarto-based personal website at [cole.press](https://cole.press) with a terminal/CLI-inspired design aesthetic. Built with Quarto + R + SCSS, deployed to Netlify.

## Quick Reference

```bash
make preview    # Start dev server
make build      # Render site
make setup      # Install dependencies
make clean      # Remove generated files
```

## Key Context

- **Quarto version:** 1.7.31+
- **R version:** 4.5.1+
- **Design:** Terminal-inspired, monospace (Anonymous Pro font)
- **Output:** Static HTML in `_site/`

## Claude-Specific Guidelines

### Response Style

- Be concise and direct
- Prefer code examples over lengthy explanations
- When editing SCSS, maintain the terminal/CLI aesthetic

### Quarto Conventions

- Use shortcodes for icons: `{{< fa icon-name >}}`
- Front matter uses YAML syntax
- R code chunks: ` ```{r} `

### File Modifications

- Content: Edit `.qmd` files directly
- Styling: Edit `monospatial-light.scss` (primary) or `monospatial-dark.scss` (dark overrides)
- Config: Edit `_quarto.yml` for site-wide settings

### Testing Changes

Always recommend running `make preview` or `quarto preview` to verify changes before committing.

### Common Patterns

**Adding an icon:**

```markdown
{{< fa brands github >}} GitHub
{{< fa solid envelope >}} Email
```

**R code chunk:**

````markdown
```{r}
#| label: example
#| echo: false
summary(data)
```
````

**New page front matter:**

```yaml
---
title: "Page Title"
description: "Brief description"
---
```

## Files to Know

| File                     | When to reference       |
| ------------------------ | ----------------------- |
| `_quarto.yml`            | Site config, navigation |
| `monospatial-light.scss` | Theme colors, layout    |
| `DESCRIPTION`            | R package dependencies  |
| `Makefile`               | Available commands      |

## Do Not

- Modify files in `_extensions/` unless specifically requested
- Suggest `npm install` for site rendering (npm is only for Netlify plugin)
- Recommend full TeX Live (use TinyTeX via `quarto install tinytex`)

---

_See [AGENTS.md](AGENTS.md) for complete project documentation._
