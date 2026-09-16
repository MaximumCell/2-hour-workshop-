// Minimal Playwright REPL-ish driver for the reveal.js deck.
// Usage: node driver.mjs <command> [args...]
//
// Commands:
//   shot <out.png> [slideIndex]   Navigate (optionally to #/<slideIndex>) and screenshot.
//   next <out.png>                Press ArrowRight then screenshot.
//   goto <n> <out.png>            Jump to slide n (0-based) via URL hash, screenshot.
//   speaker <out.png>             Press 's' to open speaker notes popup, screenshot main window.
//   pdf <out.pdf>                 Load with ?print-pdf and save a browser PDF snapshot.
//   errors                        Print any page console errors seen during a full click-through.
//
// Requires the deck dev server already running at http://localhost:8000
// (see SKILL.md). Uses the Chromium build installed via
// `npx playwright install chromium`.

import { chromium } from "playwright";

const BASE = process.env.DECK_URL || "http://localhost:8000";
const [, , cmd, ...args] = process.argv;

async function withPage(fn) {
  const browser = await chromium.launch({ args: ["--no-sandbox"] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const errors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") errors.push(msg.text());
  });
  page.on("pageerror", (err) => errors.push(String(err)));
  try {
    await fn(page, errors);
  } finally {
    await browser.close();
  }
  return errors;
}

async function main() {
  if (cmd === "shot") {
    const [out, slide] = args;
    const errors = await withPage(async (page) => {
      const url = slide ? `${BASE}/#/${slide}` : BASE;
      await page.goto(url, { waitUntil: "load" });
      await page.waitForSelector(".reveal .slides section.present", { timeout: 10000 });
      await page.waitForTimeout(300); // let reveal.js finish layout/transition
      await page.screenshot({ path: out });
    });
    console.log(`saved ${out}`);
    if (errors.length) console.log("console errors:\n" + errors.join("\n"));
  } else if (cmd === "next") {
    const [out] = args;
    await withPage(async (page) => {
      await page.goto(BASE, { waitUntil: "load" });
      await page.waitForSelector(".reveal .slides section.present");
      await page.keyboard.press("ArrowRight");
      await page.waitForTimeout(400);
      await page.screenshot({ path: out });
    });
    console.log(`saved ${out}`);
  } else if (cmd === "goto") {
    const [n, out] = args;
    await withPage(async (page) => {
      await page.goto(`${BASE}/#/${n}`, { waitUntil: "load" });
      await page.waitForSelector(".reveal .slides section.present");
      await page.waitForTimeout(300);
      await page.screenshot({ path: out });
    });
    console.log(`saved ${out}`);
  } else if (cmd === "pdf") {
    const [out] = args;
    await withPage(async (page) => {
      await page.goto(`${BASE}/?print-pdf`, { waitUntil: "networkidle" });
      await page.waitForTimeout(1000);
      await page.pdf({ path: out, printBackground: true, width: "1280px", height: "720px" });
    });
    console.log(`saved ${out}`);
  } else if (cmd === "errors") {
    const errors = await withPage(async (page) => {
      await page.goto(BASE, { waitUntil: "load" });
      await page.waitForSelector(".reveal .slides section.present");
      for (let i = 0; i < 12; i++) {
        await page.keyboard.press("ArrowRight");
        await page.waitForTimeout(150);
      }
    });
    console.log(errors.length ? errors.join("\n") : "no console errors");
  } else {
    console.error("unknown command:", cmd);
    console.error("usage: node driver.mjs <shot|next|goto|pdf|errors> [args...]");
    process.exit(1);
  }
}

main();
