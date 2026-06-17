# Design Cleanup Implementation Plan

**Goal:** Trim the noise, keep the signal. Remove behavioral gimmicks (typewriter, redundant prompts) and unused CSS while preserving all terminal visual identity (color picker, neofetch, terminal windows, rainbow navbar, monospace, glow).

---

## Step 1: Remove redundant hover JS from index.qmd

**Lines 252–267.** These set inline `transform` and `boxShadow` on hover — but the CSS already handles this with `.project-item:hover`, etc. The JS overrides the CSS transitions and is redundant.

**Remove:**
```js
    // Enhanced hover effects with smooth transitions
    const interactiveElements = document.querySelectorAll('.project-item, .thought-item, .newsletter-box');
    interactiveElements.forEach(el => {
        el.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        
        el.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
            this.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)';
        });
        el.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '';
        });
    });
```

## Step 2: Remove typewriter animation JS from index.qmd

**Lines 269–346.** This is the IntersectionObserver that types text letter-by-letter, plus the fade-in animation setup, plus the 3-second fallback timer. All of it goes.

**Remove:**
- The `cliPrompts` querySelectorAll and `completedPrompts` Set
- The `typewriterObserver` IntersectionObserver (lines 273–321)
- The `cliPrompts.forEach` observer setup (lines 323–331)  
- The `sections` fade-in opacity setup (lines 324–331)
- The 3-second fallback timeout (lines 333–346)

**After removal, what remains in the JS block (lines 252+):**
Just the newsletter form handler, ASCII cursor blink, and theme switcher. These three start at what was line 348.

## Step 3: Remove 3 CLI prompt banners from index.qmd

Three section-separator prompts are being removed. Their content is repetitive and clutters the page. The neofetch CLI prompt stays.

### Prompt before skills (lines 63–66 → remove 4 lines)
```
                              ← blank line
::: cli-prompt
<span class="text-terminal-primary">cole@press:~$</span> <code class="text-glow">cat skills.json | jq '.expertise' && ls -la ~/projects/</code>
:::
```

### Prompt before git activity (lines 105–108 → remove 4 lines)
```
                              ← blank line
::: cli-prompt
<span class="text-terminal-primary">cole@press:~$</span> <code class="text-glow">git log --oneline --graph | head -10</code>
:::
```

### Prompt before thoughts (lines 156–159 → remove 4 lines)
```
                              ← blank line
::: cli-prompt
<span class="text-terminal-primary">cole@press:~$</span> <code class="text-glow">cat thoughts/latest.txt</code>
:::
```

## Step 4: Remove unused CSS from monospatial-light.scss

The explore agent confirmed 27 classes have SCSS definitions but are never referenced in any `.qmd` or `.html` file. Remove these blocks:

### 4a. `.terminal-header` (lines 570–588)
The old terminal header class. Not used. `.cli-prompt` and `.terminal-window-large` serve this role now.

### 4b. `.hero-section-compact` (lines 591–667)
Includes `.hero-title`, `.terminal-subtitle` (the container, not `terminal-subtitle-text`), `.hero-actions-compact`. All unused.

### 4c. `.main-content-compact` (lines 670–674)
Unused layout class.

### 4d. `.terminal-prompt` (lines 677–687)
Unused. The actual prompt class is `.cli-prompt`.

### 4e. `.skills-terminal` (lines 689–705)
Unused. Skills are now in `.skills-json` inside `.skills-and-projects`.

### 4f. `.section-title-compact` (lines 708–727)
Unused section title styling.

### 4g. `.nav-grid-compact` + `.nav-card-terminal` (lines 965–978)
Unused navigation grid.

### 4h. `.activity-section-compact` + `.github-terminal` (lines 981–1030)
Unused activity/github section. Git activity now uses `.git-activity` directly.

### 4i. `.insights-matrix` + `.insight-terminal` (lines 1033–1070)
Unused insights section.

### 4j. `.connect-terminal` + `.newsletter-terminal` + `.social-terminal` (lines 1073–1177)
Unused. The connect section now uses `.connect-sidebar`.

### 4k. `.ascii-footer` (lines 1180–1193)
Unused. The footer is `.cli-footer`.

### 4l. `.terminal-dense` (lines 1477–1494)
Unused terminal content class.

### 4m. `.log-stream` (lines 1497–1539)
Unused log entry class.

### 4n. `.man-page` (lines 1542–1594)
Unused man-page layout.

### 4o. `.glow-pulse` utility classes (lines 1600–1611)
`.glow-pulse`, `.glow-pulse-green`, `.glow-pulse-purple` — these are defined as CSS classes but never used in markup. The mixins they reference (`@include glow-pulse`) stay since they're called internally.

### 4p. `.hover-lift` utility classes (lines 1612–1618)
`.hover-lift`, `.hover-lift-sm` — unused utility classes.

### 4q. `.ambient-effects-enabled` (lines 1635–1646)
Unused parent modifier class that gates scanline/glow effects.

### 4r. Matrix rain animation (lines 1677–1692)
`.matrix-rain` keyframes and class — unused.

### 4s. `.cli-header` (lines 1697–1711)
Unused. The actual CLI section headers are `.cli-prompt`.

### 4t. Also remove the `.terminal-window` grouping with `.terminal-window-large`...
Wait — `.terminal-window` is defined grouped with `.terminal-window-large` at lines 730–791. Only `.terminal-window-large` is used. But since they share a definition, we should split them: keep `.terminal-window-large` as a solo selector, drop `.terminal-window`.

Actually, for safety: just leave `.terminal-window` in the selector but remove the comma — make it `.terminal-window-large { ... }` only.

### Summary of lines to remove from monospatial-light.scss:
- 570–588: `.terminal-header`
- 591–667: `.hero-section-compact` (and children)
- 670–674: `.main-content-compact`
- 677–687: `.terminal-prompt`
- 689–705: `.skills-terminal`
- 708–727: `.section-title-compact`
- 965–978: `.nav-grid-compact`
- 981–1030: `.activity-section-compact`
- 1033–1070: `.insights-matrix`
- 1073–1177: `.connect-terminal`
- 1180–1193: `.ascii-footer`
- 1477–1494: `.terminal-dense`
- 1497–1539: `.log-stream`
- 1542–1594: `.man-page`
- 1600–1611: `.glow-pulse` utilities
- 1612–1618: `.hover-lift` utilities
- 1635–1646: `.ambient-effects-enabled`
- 1677–1692: `.matrix-rain`
- 1697–1711: `.cli-header`
- Fix line 730: change `.terminal-window,` to just `.terminal-window-large` (since `.terminal-window` is unused, but they share a block)

**Also check:** any responsive/breakpoint references to removed classes. The `@media (max-width: 768px)` at line 1291 references `.hero-section-compact` (line 1292), `.main-content-compact` (line 1306), `.nav-grid-compact` (line 1310), `.connect-terminal` (line 1315), `.insights-matrix` (line 1319). Remove those media query blocks too.

## Step 5: Fix monospatial-dark.scss

Remove duplicate terminal theme color definitions (lines 77–124). These are already defined in `monospatial-light.scss` and Quarto compiles them together.

**Remove:**
```scss
// CSS Custom Properties for Dynamic Theming (Terminal Colors)
:root {
  --terminal-primary: #c4b5fd;
  ...
}
[data-terminal-theme="green"] { ... }
[data-terminal-theme="amber"] { ... }
[data-terminal-theme="cyan"] { ... }
[data-terminal-theme="lavender"] { ... }
[data-terminal-theme="white"] { ... }
```

## Step 6: Increase whitespace between homepage sections

In `monospatial-light.scss`, adjust these spacing values for a more open, "manuscript/editorial" feel:

- `.neofetch-style` margin-bottom: change `$spacing-3` to `$spacing-6` (line 1721)
- `.skills-and-projects` margin-bottom: change `$spacing-4` to `$spacing-6` (line 1794)
- `.git-activity` margin-bottom: change `$spacing-4` to `$spacing-6` (line 1900)
- `.thoughts-section` margin-bottom: change `$spacing-4` to `$spacing-6` (line 1951)
- `.homepage-with-sidebar` gap: change `$spacing-6` to `$spacing-8` (line 2218)

## Step 7: Build and verify

```bash
make build    # or: quarto render
```

Check:
- Homepage renders all sections immediately (no fade-in delay)
- No typewriter animation on CLI prompts
- Three CLI prompt separators are gone
- Color picker still works
- Neofetch layout still intact
- Terminal windows on About/Projects pages still render
- Rainbow navbar border still present
- Glow effects still work
- Light/dark mode toggle still works
- No console errors
