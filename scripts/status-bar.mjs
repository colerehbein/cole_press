#!/usr/bin/env node
/**
 * status-bar.mjs — builds _status.qmd: the NOW bar at the top of every blog
 * post (wired in via blog/posts/_metadata.yml include-before-body).
 *
 * Auto rows, fetched fresh at build time:
 *   dateline  Albuquerque local time at render
 *   weather   Open-Meteo (no API key)
 *   building  colerehbein's own repos, most recently pushed first
 *
 * Manual rows, edited by hand in status.yml:
 *   reading / listening / sitting / cats
 *
 * Fails soft: any fetch error keeps the previous _status.qmd and exits 0 —
 * a flaky network must never break the site deploy.
 */
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const ROOT = new URL("..", import.meta.url).pathname;
const OUT = `${ROOT}_status.qmd`;
const STATUS = `${ROOT}status.yml`;
const LAT = 35.0844;
const LON = -106.6504;

function esc(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// Minimal reader for status.yml: flat `key: value` lines, quoted or plain.
function readStatus() {
  const out = {};
  if (!existsSync(STATUS)) return out;
  for (const raw of readFileSync(STATUS, "utf8").split("\n")) {
    const line = raw.trim();
    if (!line || line.startsWith("#")) continue;
    const m = line.match(/^([a-z_]+):\s*(.*)$/);
    if (!m) continue;
    let v = m[2].trim();
    if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
      v = v.slice(1, -1);
    }
    out[m[1]] = v;
  }
  return out;
}

async function getJSON(url, ms = 8000) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), ms);
  try {
    const headers = { "User-Agent": "cole.press status-bar" };
    if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
    const res = await fetch(url, { headers, signal: ctrl.signal });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } finally {
    clearTimeout(timer);
  }
}

// WMO weather interpretation codes -> short phrases
const WMO = {
  0: "clear", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
  45: "fog", 48: "freezing fog",
  51: "light drizzle", 53: "drizzle", 55: "heavy drizzle",
  56: "freezing drizzle", 57: "freezing drizzle",
  61: "light rain", 63: "rain", 65: "heavy rain",
  66: "freezing rain", 67: "freezing rain",
  71: "light snow", 73: "snow", 75: "heavy snow", 77: "snow grains",
  80: "light showers", 81: "showers", 82: "heavy showers",
  85: "snow showers", 86: "snow showers",
  95: "thunderstorm", 96: "thunderstorm with hail", 99: "thunderstorm with hail",
};

function dateline() {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Denver",
    weekday: "short", day: "2-digit", month: "short", year: "numeric",
    hour: "2-digit", minute: "2-digit", hour12: false, timeZoneName: "short",
  }).formatToParts(new Date());
  const p = Object.fromEntries(parts.map((x) => [x.type, x.value]));
  return `${p.weekday} ${p.day} ${p.month} ${p.year} · ${p.hour}:${p.minute} ${p.timeZoneName}`.toUpperCase();
}

async function fetchWeather() {
  const url =
    `https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LON}` +
    `&current=temperature_2m,weather_code,wind_speed_10m` +
    `&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone=America%2FDenver`;
  const j = await getJSON(url);
  const c = j.current;
  const cond = WMO[c.weather_code] ?? "no data";
  return `Albuquerque · ${Math.round(c.temperature_2m)}°F · ${cond} · wind ${Math.round(c.wind_speed_10m)} mph`;
}

async function fetchBuilding(n = 3) {
  const j = await getJSON("https://api.github.com/users/colerehbein/repos?sort=pushed&per_page=10");
  return (Array.isArray(j) ? j : [])
    .filter((r) => !r.fork && !r.archived)
    .slice(0, n)
    .map((r) => ({ name: r.name, url: r.html_url }));
}

async function main() {
  const manual = readStatus();
  const rows = [];

  try {
    rows.push(["Weather", esc(await fetchWeather())]);
  } catch (e) {
    console.error(`weather fetch failed: ${e.message}`);
  }

  for (const [key, label] of [
    ["reading", "Reading"],
    ["listening", "Listening"],
    ["sitting", "Sitting"],
    ["cats", "Cats"],
  ]) {
    if (manual[key]) rows.push([label, esc(manual[key])]);
  }

  try {
    const repos = await fetchBuilding();
    if (repos.length) {
      rows.push(["Building", repos.map((r) => `<a href="${esc(r.url)}">${esc(r.name)}</a>`).join(" · ")]);
    }
  } catch (e) {
    console.error(`github fetch failed: ${e.message}`);
  }

  if (!rows.length) {
    console.error("no rows could be built; leaving the existing _status.qmd in place");
    process.exit(0);
  }

  const rowHtml = rows
    .map(([label, value]) => `<div class="post-now-row"><dt>${label}</dt><dd>${value}</dd></div>`)
    .join("\n");

  const html = `<div class="post-now">
<div class="post-now-head"><span class="post-now-label">Now</span><span class="post-now-time">${esc(dateline())}</span></div>
<dl class="post-now-rows">
${rowHtml}
</dl>
</div>`;

  writeFileSync(OUT, html + "\n");
  console.log(`wrote ${OUT} (${rows.length} rows)`);
}

main();
