# Spec: Main Website (wpooley.com)

> Status: **DRAFT — tech stack to be finalized.** See open questions.
> Parent goals: [`../requirements.md`](../requirements.md)

## Summary

The primary personal site. Hosts the About/résumé content plus links into the
in-repo example projects. Should stay lightweight and fast.

## Current State (as-is)

- **Stack:** Vanilla HTML / CSS / JS, under `src/` (`src/index.html`, `src/index.css`,
  `src/index.js`).
- **Hosting:** GitHub Pages, custom domain via `src/CNAME` (wpooley.com). _Migrating to
  AWS S3 + CloudFront (free tier); GitHub Pages being retired._
- **Navigation:** Single-page; nav links toggle visibility of `About` / `Projects` /
  `Contact` sections via `linkClicked()` (show/hide pattern, no router).
- **Icons/fonts:** Font Awesome (local `src/webfonts/`, `src/assets/all.min.css`).
- **Content issues to fix:** About paragraph says "currently working at Microsoft" —
  now inaccurate (current role is DentaQuest). Legacy projects link out to external
  hosts; these are to be replaced by in-repo projects.

## Target (to-be) — proposed, pending confirmation

- **Stack:** Keep **vanilla HTML/CSS/JS** for the shell (aligns with "framework-light"
  goal and with the Cyberpunk Timer rebuild being vanilla). Reconsider only if a
  project demands a framework.
- **Navigation pattern:** _OPEN QUESTION_ — keep the show/hide single-page approach, or
  move to real multi-page routes (e.g. `/`, `/projects/timer`, `/projects/restaurants`)?
  Multi-page (separate HTML files) tends to be cleaner for embedding distinct projects
  and is GitHub-Pages friendly.
- **Structure:** Each in-repo project gets its own page/route and pulls from its spec.
- **Visual design — NEW DIRECTION:** a **totally new design**, moving away from the current
  blue/white aesthetic. Inspiration: **old-school green CRT terminal / Warhammer-style
  interfaces** — monospace type, dark background, scanline/glow vibes. Accent color *TBD*
  (**green vs amber/orange**).
  - **Boundary:** this theme applies to the **main site only**. The résumé (`src/resume.html`)
    stays a clean white "Word doc" and must **not** inherit this theme — see
    [`resume.md`](./resume.md).

## Open Questions

1. **Navigation model:** single-page show/hide (current) vs. multi-page static routes?
2. **Accent color** for the terminal theme: green CRT vs amber/orange?
3. **Project embedding:** do projects live as sub-pages of the main site, or as
   self-contained sub-apps linked from a projects index?
4. **Build step:** stay build-less (raw files served by Pages) or introduce a minimal
   bundler? Default: build-less.

## Decisions (fill in as resolved)

- _TBD_
