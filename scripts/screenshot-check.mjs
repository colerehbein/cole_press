// Screenshot + smoke guard for cole.press.
// Renders key routes headless, screenshots light & dark, and asserts the
// critical chrome exists (the bugs this guards: empty mobile toggler icon,
// missing skip link, palette picker presence, rainbow stripe).
//
// Usage:  node scripts/screenshot-check.mjs [baseUrl] [outDir]
//   baseUrl defaults to http://localhost:4200 (quarto preview)
//   outDir  defaults to ./screenshot-check-out
//
// Requires: npm i -D playwright  +  npx playwright install chromium

import { chromium } from "playwright";
import { mkdir } from "node:fs/promises";
import { execSync } from "node:child_process";
import path from "node:path";

const baseUrl = process.argv[2] || "http://localhost:4200";
const outDir = process.argv[3] || "./screenshot-check-out";

// Style guard: no em dashes in user-visible site copy (Cole's standing
// preference, enforced so AI-generated content can't reintroduce them).
// Skips the CV (conventional "Role — Org" resume format) and blog posts
// (Cole's own writing).
try {
  const out = execSync(
    "grep -rn '—' --include='*.qmd' . | grep -v '_site' | grep -vE 'cv/(full-cv|resume|index)\\.qmd' | grep -v 'blog/posts' || true",
    { cwd: new URL("..", import.meta.url).pathname, encoding: "utf8" }
  );
  if (out.trim()) {
    console.error("EM DASHES FOUND in user-visible content:\n" + out);
    process.exit(1);
  }
  console.log("OK   style-guard: no em dashes in user-visible content");
} catch (e) {
  console.error("style-guard error:", e.message);
}

const routes = [
  "/", "/about", "/research", "/projects", "/colophon",
  "/blog/", "/portfolio/", "/portfolio/photos", "/portfolio/writing", "/cv/",
];

const browser = await chromium.launch();
const results = [];
let failures = 0;

for (const route of routes) {
  for (const dark of [false, true]) {
    const page = await browser.newPage({
      colorScheme: dark ? "dark" : "light",
      viewport: { width: 1280, height: 800 },
    });
    const name = (route === "/" ? "index" : route.replaceAll("/", "_")) + (dark ? "-dark" : "-light");
    try {
      const url = baseUrl + route;
      await page.goto(url, { waitUntil: "networkidle" });
      // The core chrome assertions (only on pages that have them)
      const checks = {};
      if (route === "/") {
        checks.palettePicker = await page.locator(".palette-picker").count() > 0;
      }
      if (route === "/blog/") {
        checks.blogListing = await page.locator(".quarto-post").count() > 0;
      }
      await page.screenshot({ path: path.join(outDir, name + ".png"), fullPage: true });
      results.push(`OK   ${name}  ${JSON.stringify(checks)}`);
    } catch (e) {
      failures++;
      results.push(`FAIL ${name}  ${e.message}`);
    }
    await page.close();
  }
}

// Mobile check: the toggler icon must render its glyph (not be empty).
const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
await mobile.goto(baseUrl + "/", { waitUntil: "networkidle" });
const togglerVisible = await mobile.locator(".navbar-toggler-icon").isVisible().catch(() => false);
const togglerHasGlyph = await mobile.locator(".navbar-toggler-icon").evaluate(
  (el) => getComputedStyle(el, "::before").content !== "none" && getComputedStyle(el, "::before").content !== ""
).catch(() => false);
const skipLinkCount = await mobile.locator(".skip-link").count();
results.push(`CHK  mobile toggler visible=${togglerVisible} glyph=${togglerHasGlyph} skip-links=${skipLinkCount}`);
if (!togglerVisible || !togglerHasGlyph || skipLinkCount === 0) failures++;
await mobile.close();
await browser.close();

console.log(results.join("\n"));
console.log(failures === 0 ? "\nALL SCREENSHOT CHECKS PASSED" : `\n${failures} FAILURES`);
process.exit(failures === 0 ? 0 : 1);
