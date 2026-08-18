#!/usr/bin/env python3
"""WCAG contrast audit for the Academic Brutalist theme (brutalist-light.scss /
brutalist-dark.scss + _brutalist.scss components).

Computes contrast ratios for every text/background pairing actually rendered
by the site: body/secondary/muted text, links (base + palette + rainbow),
buttons, badges, code, inverted labels, and the 3:1 non-text focus indicator.

Usage:  python3 contrast-audit.py
Exits non-zero if any check fails (handy for CI).
"""
import colorsys
import sys

def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb2hex(rgb):
    return '#%02x%02x%02x' % tuple(round(max(0, min(255, c))) for c in rgb)

def lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(rgb):
    r, g, b = rgb
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

def check(name, fg, bg, threshold=4.5):
    r = ratio(hex2rgb(fg) if isinstance(fg, str) else fg,
              hex2rgb(bg) if isinstance(bg, str) else bg)
    status = 'PASS' if r >= threshold else '**FAIL**'
    print(f'{status:8s} {r:5.2f}:1  {name:56s} fg={fg} bg={bg}')
    return r >= threshold

# ---------------------------------------------------------------------------
# Light theme tokens (brutalist-light.scss :root)
# ---------------------------------------------------------------------------
L_BG       = '#ffffff'
L_SURFACE  = '#ffffff'
L_TEXT     = '#000000'
L_SEC      = '#333333'
L_MUTED    = '#666666'
L_BORDER   = '#000000'
L_HAIR     = '#e5e5e5'
L_PRIMARY  = '#0000ee'
L_HOVER    = '#551a8b'
L_TINT     = '#f5f5f5'      # default --color-primary-light
L_CODE     = '#f1f5f9'
L_HOVERBG  = '#f8fafc'
L_RAINBOW  = ['#cc0000', '#b45309', '#006600', '#0a6ebd', '#6d28d9', '#0e7490']
L_TINTS    = {  # per-palette --color-primary-light (same keys as data-palette)
    'classic': '#eef0ff', 'violet': '#f3eeff', 'green': '#e9f5e9',
    'amber': '#fdf3e7', 'crimson': '#fdeeee',
}

# ---------------------------------------------------------------------------
# Dark theme tokens (brutalist-dark.scss :root)
# ---------------------------------------------------------------------------
D_BG       = '#1a1a1a'
D_SURFACE  = '#242424'
D_TEXT     = '#f0f0f0'
D_SEC      = '#d0d0d0'
D_MUTED    = '#999999'
D_BORDER   = '#777777'
D_HAIR     = '#383838'
D_PRIMARY  = '#6b9eff'
D_HOVER    = '#a78bfa'
D_TINT     = '#2a2a2a'      # default --color-primary-light
D_CODE     = '#2e2e2e'
D_HOVERBG  = '#2a2a2a'
D_RAINBOW  = ['#ff6b6b', '#fbbf24', '#4ade80', '#6b9eff', '#c084fc', '#22d3ee']
D_TINTS    = {
    'classic': '#25314d', 'violet': '#2d2540', 'green': '#14301f',
    'amber': '#3a2b06', 'crimson': '#3d1a1a',
}

# ---------------------------------------------------------------------------
ok = True

def audit(theme, BG, SURFACE, TEXT, SEC, MUTED, PRIMARY, HOVER, TINT, CODE,
          HOVERBG, RAINBOW, TINTS, label):
    global ok
    print(f'\n== {label} ==')
    # Core text
    ok &= check('body text on page',            TEXT, BG)
    ok &= check('secondary text on page',       SEC, BG)
    ok &= check('muted text on page',           MUTED, BG)
    ok &= check('muted text on surface',        MUTED, SURFACE)
    ok &= check('secondary text on surface',    SEC, SURFACE)
    # Links
    ok &= check('link (primary) on page',       PRIMARY, BG)
    ok &= check('link hover/visited on page',   HOVER, BG)
    ok &= check('link (primary) on tint (badge bg)', PRIMARY, TINT)
    ok &= check('link (primary) on surface',    PRIMARY, SURFACE)
    # Buttons (light: white on primary; dark: --color-bg on primary)
    if label == 'DARK THEME':
        ok &= check('btn-primary: bg on primary',   BG, PRIMARY)
        ok &= check('btn-primary hover: bg on hover', BG, HOVER)
    else:
        ok &= check('btn-primary: white on primary', '#ffffff', PRIMARY)
        ok &= check('btn-primary hover: white on hover', '#ffffff', HOVER)
    # Inverted labels (home-start-hint-label, quick-search-btn)
    ok &= check('inverted label: bg on text',   BG, TEXT)
    # Code / blockquote
    ok &= check('code text on code-bg',         TEXT, CODE)
    ok &= check('secondary text on code-bg (blockquote)', SEC, CODE)
    ok &= check('inline code on code-bg',       TEXT, CODE)
    # Footer / nav
    ok &= check('nav/footer link text on surface', TEXT, SURFACE)
    # Rainbow link hues on page bg
    print('  -- rainbow link hues --')
    for i, hue in enumerate(RAINBOW, 1):
        ok &= check(f'rainbow-{i} on page',     hue, BG)
    # Per-palette: primary on its own tint (badges under that palette)
    print('  -- per-palette badges (primary on palette tint) --')
    for name, tint in TINTS.items():
        ok &= check(f'{name} primary on {name} tint', PRIMARY, tint)

audit('LIGHT', L_BG, L_SURFACE, L_TEXT, L_SEC, L_MUTED, L_PRIMARY, L_HOVER,
      L_TINT, L_CODE, L_HOVERBG, L_RAINBOW, L_TINTS, 'LIGHT THEME')
audit('DARK', D_BG, D_SURFACE, D_TEXT, D_SEC, D_MUTED, D_PRIMARY, D_HOVER,
      D_TINT, D_CODE, D_HOVERBG, D_RAINBOW, D_TINTS, 'DARK THEME')

print('\n== FOCUS INDICATOR (3:1 non-text) ==')
ok &= check('light focus outline (primary) on page',   L_PRIMARY, L_BG, 3.0)
ok &= check('dark focus outline (primary) on page',    D_PRIMARY, D_BG, 3.0)

print('\n' + ('ALL CHECKS PASSED' if ok else 'FAILURES PRESENT'))
sys.exit(0 if ok else 1)
