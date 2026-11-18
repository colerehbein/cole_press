#!/usr/bin/env python3
"""
og-image.py — regenerates og-image.png (the 1200x630 social card) from the
site's public copy. Layout is Academic Brutalism: white card, black frame,
big name, hard rule, one description line, footer line, and the deliberately
garish five-color header stripe at the bottom.

Usage: python3 scripts/og-image.py   (writes og-image.png in the repo root)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NEUE = "/System/Library/Fonts/HelveticaNeue.ttc"

NAME_1 = "Cole Rehbein"
NAME_2 = "MS, LMHC"
DESC = (
    "Crisis clinician and psychotherapist (LMHC) on the 988 Suicide & Crisis "
    "Lifeline network, and clinical psychology researcher studying behavioral "
    "treatments for depression."
)
FOOTER_A = "ALBUQUERQUE, NM · "
FOOTER_B = "COLE.PRESS"

# The header stripe is deliberately its own garish five-color set
# (see _brutalist.scss, #quarto-header::after): fixed, never per-palette.
STRIPE = ["#ff6b6b", "#f8e71c", "#00c9a7", "#4dabf7", "#a66dd4"]

INK = "#000000"
GRAY = "#555555"
LINK = "#0000ee"


def tracked(draw, xy, text, font, fill, spacing=0.0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + spacing
    return x


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)

    f_name = ImageFont.truetype(NEUE, 112, index=1)
    f_desc = ImageFont.truetype(NEUE, 26, index=0)
    f_foot = ImageFont.truetype(NEUE, 15, index=1)

    # Frame
    d.rectangle([18, 18, W - 18, H - 22], outline=INK, width=3)

    # Name, stacked and scaled to fill the frame
    d.text((52, 58), NAME_1, font=f_name, fill=INK)
    d.text((52, 174), NAME_2, font=f_name, fill=INK)

    # Hard rule
    d.rectangle([56, 328, 236, 340], fill=INK)

    # Description
    y = 366
    for line in wrap(DESC, f_desc, W - 112):
        d.text((56, y), line, font=f_desc, fill=INK)
        y += 37

    # Footer line (tracked uppercase, link part in accent blue + underlined)
    fx = tracked(d, (56, H - 55), FOOTER_A, f_foot, GRAY, spacing=2.0)
    tracked(d, (fx, H - 55), FOOTER_B, f_foot, LINK, spacing=2.0)
    d.rectangle([fx, H - 38, fx + f_foot.getlength(FOOTER_B) + 2.0 * len(FOOTER_B), H - 37], fill=LINK)

    # Rainbow stripe
    seg = W / len(STRIPE)
    for i, c in enumerate(STRIPE):
        d.rectangle([i * seg, H - 14, (i + 1) * seg, H], fill=c)

    import os
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "og-image.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
