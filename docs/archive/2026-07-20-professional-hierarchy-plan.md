# cole.press professional-hierarchy overhaul — execution plan

> **ARCHIVED 2026-08-18.** This plan was executed and shipped (the July 2026
> professional-hierarchy overhaul). It lives here for provenance only. The
> theme files it names (`monospatial-light.scss` / `monospatial-dark.scss`)
> were renamed to `brutalist-light.scss` / `brutalist-dark.scss` in the
> Academic Brutalist redesign. Still-relevant follow-ups (CSP report-only,
> LinkedIn/photo assets) are tracked in SITE-GUIDE.md §8 and the repo backlog.

Date: 2026-07-20. Source: professional review of cole.press (accepted by owner; blog = Option A: merge into main site).

Positioning used everywhere: "Crisis counselor and clinical psychology researcher building reproducible tools for behavioral-health research, communication, and care."

## Swarm assignments (parallel, non-conflicting file ownership)

| # | Specialist | Files owned |
|---|-----------|-------------|
| 1 | Homepage_Specialist | `index.qmd` — hero + CTAs, proof cards, trimmed terminal, remove gh-stats chunk, a11y fixes |
| 2 | Projects_Specialist | `projects.qmd` — case studies (Problem/Role/Stack/Artifact/Status), specific repo links |
| 3 | CV_Specialist | `cv/index.qmd`, `cv/full-cv.qmd`, `cv/resume.qmd` — full web CV + PDF sources (may render its PDFs only) |
| 4 | BlogMerge_Specialist | `blog/index.qmd`, `blog/_metadata.yml`, `blog/posts/` — Option A merge (listing, RSS, shared theme) |
| 5 | Essay_Writer | `blog/posts/2026-07-20-crisis-work-mental-health-tech.qmd` — cornerstone essay |
| 6 | About_Specialist | `about.qmd` — professional resequencing |
| 7 | SiteConfig_Specialist | `_quarto.yml` — description, navbar aria-labels, OG/Twitter card metadata |
| 8 | Netlify_Specialist | `netlify.toml`, `_redirects` — security headers, font caching, drop blog proxy, .html 301s |
| 9 | SocialImage_Specialist | `og-image.png` — 1200×630 terminal-style social card |
| 10 | ContrastA11y_Specialist | `monospatial-light.scss`, `monospatial-dark.scss` — WCAG contrast, focus styles, .visually-hidden |
| 11 | GitHubProfile_Specialist | External: profile README, cv repo cleanup/privacy, macOSMoveTo README framing |

## Integration (orchestrator, after swarm)
- Run full `quarto render`; fix breakage; verify `/blog/` listing + RSS, `_site/_redirects`, OG image reference, PDF downloads (if LaTeX present).
- Report + manual follow-ups: pin repos / repo descriptions (GitHub UI), archive old blog repo + subdomain DNS, LinkedIn/photo (need owner's assets), CSP report-only, one-page résumé CI check.

## Deferred / not in scope
- Merging real posts (none exist), font subsetting, FA→SVG swap, photo/LinkedIn (assets needed), git commit/push/deploy (owner's call).
