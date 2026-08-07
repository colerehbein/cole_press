# Site User Guide — cole.press

A practical guide to updating, maintaining, and shipping this site. For AI agents working in this repo, see [AGENTS.md](./AGENTS.md); for the design system reference, see [docs/design](./docs/design/README.md).

---

## 1. What this site is

A personal website for Cole Rehbein — crisis counselor and clinical psychology researcher — built with **Quarto** and deployed to **Netlify**. Content lives in Markdown (`.qmd` files); a push to `main` on GitHub triggers a GitHub Action that renders the site and deploys it.

The design is **Academic Brutalism** (ported from the IPIP Repository design system): white/off-white surfaces, pure black borders, zero rounded corners, zero shadows, system sans-serif (Helvetica Neue), uppercase labels, monospace only for data/code — with two bits of personality: an **accent palette switcher** (5 colors) and a **rainbow stripe** under the header.

---

## 2. Quick start

```bash
make preview    # local dev server with live reload → http://localhost:4200
make build      # render the site to _site/
quarto render   # same as make build
```

To ship: commit your changes and push to `main`. The GitHub Action (`Build & Deploy to Netlify`) renders and deploys automatically. Check the run under the repo's **Actions** tab.

---

## 3. Site map

| URL | Source file | What it is |
|---|---|---|
| `/` | `index.qmd` | Home: kicker, title, abstract, directory index, sidebar |
| `/about` | `about.qmd` | About: prose + career timeline |
| `/research` | `research.qmd` | Research: thesis, systematic review, EEG work, methods, presentations |
| `/projects` | `projects.qmd` | Case-study cards |
| `/portfolio/` | `portfolio/index.qmd` | Portfolio landing: Photos + Writing cards |
| `/portfolio/photos` | `portfolio/photos.qmd` | Photo gallery (grid) |
| `/portfolio/writing` | `portfolio/writing.qmd` | Writing index: essays, journalism, academic papers |
| `/blog/` | `blog/index.qmd` + `blog/posts/*.qmd` | Essay listing + RSS feed (`/blog/index.xml`) |
| `/cv/` | `cv/index.qmd` | Web CV + PDF download buttons |
| `cv/cole-rehbein-cv.pdf` | `cv/full-cv.qmd` | Full CV PDF (LaTeX, built automatically) |
| `cv/cole-rehbein-resume.pdf` | `cv/resume.qmd` | One-page résumé PDF |

---

## 4. Common tasks

### 4.1 Add a blog post

1. Create `blog/posts/YYYY-MM-DD-slug.qmd` (e.g. `blog/posts/2026-08-05-brutalism.md`).
2. Front matter (required):

   ```yaml
   ---
   title: "Your title"
   description: "One sentence shown in the listing and RSS feed."
   author: "Cole Rehbein"
   date: 2026-08-05
   categories: [crisis work, research]
   ---
   ```

3. Write the post in plain Markdown.
4. The listing and RSS feed update automatically on the next render. Nothing else to do.

### 4.2 Edit the home page

`index.qmd` is mostly raw HTML with these classes (all styled by the theme — do not add inline styles):

- `.home-kicker` — the small uppercase line above the title
- `.home-title` — the big name
- `.home-abstract` — the bordered "Abstract:" box
- `.home-meta` — the muted credentials line
- `.home-start-hint` — the "First visit?" box
- `.directory-list` / `.directory-entry` / `.directory-term` / `.directory-desc` — the Directory Index rows
- `.home-sidebar-section` / `.home-sidebar-title` — sidebar blocks
- `.instrument-links` — the links list
- `.quick-search-form` / `.quick-search-input` / `.quick-search-btn` — the newsletter form (posts to Buttondown)
- `.changelog-list` / `.changelog-entry` — the "Currently" entries

**Note:** raw HTML in `.qmd` files must be **unindented to column 0** — pandoc turns indented `<dt>`/`<dd>`/`<p>` lines into escaped code blocks.

### 4.3 Edit About / Research / CV / Projects

All are Markdown + a few theme classes:

- **About** — plain Markdown; the timeline at the bottom uses `.ipip-timeline*` classes (see the section in `about.qmd` as a template).
- **Research** — thesis facts live in a Markdown table (rendered with the brutalist `.table` styles); the review and EEG studies use `.cv-entry` rows (same as CV). Update the thesis **Status** row when the manuscript moves.
- **Projects** — each project is a `.card` inside `.card-grid`. Copy an existing card block; status uses `.badge` pills.
- **CV** — each position is a `.cv-entry` (left column: `.cv-role` + `.cv-org`; right column: `.cv-detail` with an optional `.cv-meta` date line). PDF download buttons are `.btn btn-primary` / `.btn`.

### 4.4 Change the accent palette (or add one)

Palettes are defined per theme in `brutalist-light.scss` and `brutalist-dark.scss`:

```scss
[data-palette="violet"] {
  --color-primary: #7c3aed;        /* light theme */
  --color-primary-hover: #5b21b6;
  --color-accent: #7c3aed;
}
```

To add a palette:

1. Add a `[data-palette="name"]` block in **both** theme files (light values in the light file, dark values in the dark file).
2. Add a swatch color token `--swatch-name: ...` to the `:root` block of **both** theme files (this is the color shown in the navbar picker).
3. Register it in `_includes/accent-palette.html` (the `palettes` array + the `localStorage` allow-list in the boot script).
4. If it needs a `.palette-swatch[data-palette="name"]` background rule, add it in `_brutalist.scss`.

The picker saves to `localStorage["cole-palette"]`; the boot script in `_includes/accent-palette.html` applies it before paint so there's no flash.

### 4.5 Change fonts

- **Body font:** `$font-family-base` in both `brutalist-*.scss` files (currently the Helvetica Neue system stack).
- **Monospace (code, dates, data):** `$font-family-monospace` in both files + `--font-mono` token + `_fonts.scss` (`@font-face` for self-hosted Anonymous Pro in `fonts/`).
- **Font preloading:** `_includes/preload-fonts.html`.

### 4.6 Update the newsletter form

The form posts to Buttondown (`https://buttondown.com/api/emails/embed-subscribe/coler` in `index.qmd`). Change the email/subscribe ID there.

### 4.7 Add photos to the portfolio

1. Drop image files (JPG/PNG/WebP) into `portfolio/photos/`.
2. In `portfolio/photos.qmd`, replace a placeholder frame with:
   `<figure class="photo-frame"><img src="photos/your-photo.jpg" alt="Description" loading="lazy"></figure>`
   (paths are relative to `portfolio/`).
3. Add the folder to `resources` in `_quarto.yml` if Quarto doesn't copy it automatically (`resources: - portfolio/photos/`).

### 4.8 Update the CV (and how the CV repo works)

The full CV's **source of truth is the private GitHub repo [`colerehbein/cv`](https://github.com/colerehbein/cv)** (the academic CV with auto-rendered publications). The site keeps the PDF building inside this repo because `/cv/` is a page here.

Workflow to update the CV:

1. Edit `CV.qmd` in your local clone of `colerehbein/cv` (push it — it's the record).
2. `make cv-sync` in this repo — copies `CV.qmd`, the CSL, and `references/*.bib` into `cv/` (and pins `output-file: cole-rehbein-cv.pdf`).
3. `quarto render` (or `make build`), commit the synced `cv/` changes, push.

The one-page résumé (`cv/resume.qmd`) is site-owned and edited directly here — the CV repo has no résumé. `cv/index.qmd` (the web CV page) is also site-owned.

### 4.9 The navbar structure

Top navigation (`_quarto.yml` → `navbar`):

- **Home · About · Research ▾ · Blog · Portfolio ▾ · CV** (right: GitHub · X)
- **Research ▾** is a pure dropdown toggle (Research, Projects) — native Quarto `menu:`, no custom JS.
- **Portfolio ▾** (Overview, Photos, Writing) — clicking "Portfolio" itself navigates to `/portfolio/` on desktop (not native Quarto: `_includes/portfolio-nav.html` repoints the toggle's href and strips `data-bs-toggle` on desktop, while CSS hover/focus opens the menu). On mobile the native toggle stays and the Overview item appears.
- Both dropdowns use the shared brutalist `.dropdown-menu` styling in `_brutalist.scss` (square, black border, hover = primary-light).

### 4.9 The 404 page

`404.qmd` renders to `404.html`, which Netlify serves as the custom not-found page (Quarto picks it up automatically — no config needed). It uses the directory-list component and includes the 988 note.

---

## 5. How the theme is organized

```
brutalist-light.scss     # light tokens + Bootstrap bridge + palette blocks + imports
brutalist-dark.scss      # dark tokens + Bootstrap bridge + palette blocks + imports
_brutalist.scss          # ALL component CSS (shared by both themes — never drift)
_fonts.scss              # @font-face for Anonymous Pro
_includes/preload-fonts.html    # font preloading
_includes/accent-palette.html   # palette boot script + navbar picker JS
_includes/home-no-title.html    # hides the Quarto title block on the home page only
```

**The golden rule:** components live only in `_brutalist.scss` and use CSS custom properties (`var(--color-*)`). The two theme files define the token values (light vs dark) and nothing else. If a component needs a color, it uses a token — never a hardcoded hex. If a palette changes, only accent colors change; borders and surfaces never do.

Bootstrap bridge: each theme file sets SCSS vars (`$body-bg`, `$primary`, `$border-radius: 0`, …) and emits `:root { --bs-border-radius: 0; --bs-box-shadow: none; … }` to kill leftover Bootstrap rounding/shadows.

---

## 6. Design system cheat sheet

- **Radius:** 0 everywhere. Exceptions: `.badge` (100px pill), inline `code` (4px).
- **Shadows:** none. **Transitions:** none (hovers are instant).
- **Borders:** 1px = containers/rows; 2px = structural emphasis (header bottom, section-top rules, table headers); `--color-border-light` = interior hairlines.
- **Typography:** body = Helvetica Neue, `line-height: 1.6`; headings 700 weight with *negative* tracking (`-0.02em`); uppercase labels with *positive* tracking (`0.05em`+); mono (Anonymous Pro) for code, dates, data.
- **Links:** `--color-primary` (blue by default), underline in body text, `--color-primary-hover` (purple) on hover/visited. Nav links are not underlined — they get a 2px bottom border on hover instead.
- **Accent palettes:** Classic Blue, Violet, Green, Amber, Crimson — switchable from the navbar; persist across visits.
- **Rainbow stripe:** the 4px hard-stop striped bar under the header — the site's one decorative flourish. Colors are fixed (do not change per palette).
- **988 crisis note:** the bordered line in the footer center (`page-footer.center` in `_quarto.yml`) — appears on every page; styled via `.nav-footer .footer-items-center`.
- **Print:** a `@media print` block in `_brutalist.scss` strips the chrome (header, footer, picker, search, TOC) and keeps cards/entries together across page breaks.

Full component reference: [docs/design/catalog.md](./docs/design/catalog.md).

---

## 7. Build & deployment

- **Local:** `make preview` / `quarto render`.
- **CI:** two GitHub Actions on push to `main`:
  - `Build & Deploy to Netlify` — installs R, Quarto **with TinyTeX** (needed for the CV PDFs), renders, deploys `_site/` to Netlify.
  - `Quarto Render` — render check (also runs on PRs). Both workflows set `tinytex: true`; removing it breaks the CV PDF builds.
- **Netlify:** deploy happens via the Action (`nwtgck/actions-netlify`), not Netlify's own build. `netlify.toml` only sets headers.
- **Redirects:** `_redirects` (copied into `_site/`) — `blog.cole.press/*` 301s to `/blog/:splat` (needs the `blog.cole.press` domain alias attached to the cole.press Netlify site in the dashboard), and legacy `.html` URLs 301 to clean URLs.

---

## 8. Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| CI deploy fails at the render step | Check for a pandoc YAML error in a `.qmd` (e.g. invalid `listing:` options). `quarto render` locally reproduces it. |
| CI fails with "No TeX installation detected" | Someone removed `tinytex: true` from `.github/workflows/*.yml`. Re-add it. |
| CV PDFs are stale | PDFs build from `cv/full-cv.qmd` / `cv/resume.qmd` at render time. Change those files, not the PDFs. |
| Home page shows a big "Cole Rehbein" heading twice | The `.quarto-title-block` is hidden via `_includes/home-no-title.html` (referenced in `index.qmd` front matter). If you removed it, the title block reappears. |
| Escaped HTML (`&lt;dt&gt;` blocks visible as code) | Raw HTML in `.qmd` files must be unindented to column 0 (see §4.2). |
| Dark mode looks unstyled | Both themes import `_brutalist.scss`; if a new component was added only to one theme file, move it to `_brutalist.scss`. |
| Palette picker missing | `_includes/accent-palette.html` must be in `include-in-header` in `_quarto.yml`, and it mounts into `.quarto-navbar-tools` (Quarto's navbar tools container). |
| Blog listing rows have no separators | Quarto's client-side listing CSS can win the cascade; the `.quarto-listing .quarto-post` rules in `_brutalist.scss` use `!important` deliberately. Keep them. |
