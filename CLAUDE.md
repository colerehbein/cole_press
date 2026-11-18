# Claude Instructions

> **Claude-specific guidance for this repository.**
> For complete project context, see [AGENTS.md](AGENTS.md).

## Project Summary

This is a Quarto-based personal website at [cole.press](https://cole.press) with an **Academic Brutalism** design. Built with Quarto + SCSS, deployed to Netlify.

## Quick Reference

```bash
make preview    # Start dev server
make build      # Refresh the NOW bar + render site
make setup      # Install TinyTeX (CV PDFs)
make clean      # Remove generated files
```

## Key Context

- **Quarto version:** 1.7.31+
- **Design:** Academic Brutalism — pure black borders, zero radius/shadows/transitions; Helvetica Neue prose, Anonymous Pro (mono) for data
- **Theme layer:** tokens in `brutalist-light.scss` / `brutalist-dark.scss`; ALL component CSS in `_brutalist.scss`
- **Output:** Static HTML in `_site/`
- **No R chunks anywhere** — the site is pure Markdown + HTML + SCSS

## Response Style

- Be concise and direct
- Prefer code examples over lengthy explanations
- When editing SCSS, maintain the Academic Brutalism invariants (tokens only, zero radius/shadows/transitions)

## Quarto Conventions

- Use shortcodes for icons: `{{< fa icon-name >}}`
- Front matter uses YAML syntax
- Raw HTML in `.qmd` must be unindented to column 0 (pandoc escapes indented blocks)

## File Modifications

- Content: Edit `.qmd` files directly
- Styling: tokens in `brutalist-light.scss` / `brutalist-dark.scss`; components in `_brutalist.scss` (never put component CSS in a theme file)
- Config: Edit `_quarto.yml` for site-wide settings

## Testing Changes

Always recommend running `make preview` or `quarto preview` to verify changes before committing.

## Files to Know

| File                     | When to reference       |
| ------------------------ | ----------------------- |
| `_quarto.yml`            | Site config, navigation |
| `brutalist-light.scss`   | Light theme tokens      |
| `brutalist-dark.scss`    | Dark theme tokens       |
| `_brutalist.scss`        | Component styles        |
| `Makefile`               | Available commands      |

## Do Not

- Modify files in `_extensions/` unless specifically requested
- Suggest `npm install` for site rendering (npm is only for Netlify plugin)
- Recommend full TeX Live (use TinyTeX via `quarto install tinytex`)
- Rewrite Cole's own writing (blog essays, CV prose)

---

_See [AGENTS.md](AGENTS.md) for complete project documentation._
