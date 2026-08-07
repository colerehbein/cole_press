#!/usr/bin/env bash
# cv-sync.sh — copy the canonical CV from the colerehbein/cv repo into this site.
#
# The GitHub repo https://github.com/colerehbein/cv is the source of truth for
# the full CV (private; holds the academic CV with auto-rendered publications).
# This script pulls its CV.qmd (+ csl + bibliographies) into cole_press/cv/ so
# the site's /cv/ page keeps building cole-rehbein-cv.pdf from the same source.
#
# Usage:
#   scripts/cv-sync.sh [SOURCE_DIR]     # SOURCE_DIR defaults to ../cv
#
# Workflow: edit cv repo -> make cv-sync -> quarto render -> push cole_press.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="${1:-$ROOT/../cv}"
DEST="$ROOT/cv"

if [ ! -f "$SOURCE/CV.qmd" ]; then
  echo "error: no CV.qmd found in $SOURCE"
  echo "Clone the CV repo first, e.g.: git clone git@github.com:colerehbein/cv.git ../cv"
  exit 1
fi

echo "Syncing canonical CV from $SOURCE -> $DEST"

cp "$SOURCE/CV.qmd" "$DEST/full-cv.qmd"
cp "$SOURCE"/apa-annotated-bibliography.csl "$DEST/" 2>/dev/null || true

mkdir -p "$DEST/references"
cp "$SOURCE"/references/*.bib "$DEST/references/" 2>/dev/null || true

# Ensure the site builds the PDF under the filename the /cv/ page links to
python3 - "$DEST/full-cv.qmd" <<'PY'
import sys
p = sys.argv[1]
s = open(p).read()
if "output-file:" not in s.split("---")[1]:
    s = s.replace("format:\n  quarto-cv-pdf: default",
                  "format:\n  quarto-cv-pdf:\n    output-file: cole-rehbein-cv.pdf")
    open(p, "w").write(s)
    print("  injected output-file: cole-rehbein-cv.pdf")
PY

echo "Done. Run 'quarto render' (or 'make build') next; commit the synced files."
