# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single self-contained static HTML page (`index.html`) — a personal site for Gal Matalon (QA/automation manager, founder of "המכללה לאוטומציה"). There is no build system, package manager, bundler, or test suite: `index.html` contains all CSS inline in a `<style>` block and has no JavaScript or external script dependencies (only a Google Fonts stylesheet link). Not a git repository.

## Structure

- `index.html` — the entire site (header nav, hero, about, experience timeline, skills, college promo section, education, footer). RTL Hebrew content (`dir="rtl" lang="he"`).
- `images/` — image assets (`gal5.jpg`, `logo.jpeg`, `גל מטלון - קורסי בדיקות תוכנה לכניסה להייטק QA.jpg`) referenced by `index.html` via **relative paths** (`images/...`). This folder must stay alongside `index.html`; moving the HTML file elsewhere requires moving `images/` with it (note one filename is Hebrew with spaces).
- `gal-matalon.pdf` — a LinkedIn profile export; source material for the bio/experience copy in the site, not a build input.

## Previewing changes

There's no dev server or build step — just open `index.html` in a browser. If verifying via the Playwright MCP browser tools, note that `file://` navigation is blocked by the sandbox; serve the directory over HTTP first, e.g.:

```
py -3 -m http.server 8791
```

then navigate to `http://localhost:8791/index.html`.

## Editing conventions already in the page

- Design tokens are CSS custom properties on `:root`, with dark-mode overrides duplicated for both `prefers-color-scheme: dark` and an explicit `[data-theme="dark"]` selector — keep both in sync when changing colors.
- Hebrew body copy uses "Heebo"/"IBM Plex Sans Hebrew"; Latin/numeric mono content (dates, phone numbers, tech tags) uses the `.mono` class with `direction:ltr` to keep it from reversing inside RTL flow.

## User preferences

- Gal's favorite color is blue (כחול).
