# Spec: Resume Page (src/resume.html)

> Status: **ACTIVE / IMPLEMENTED** (`/resume.html`).
> Parent goals: [`../requirements.md`](../requirements.md)
> Content source of truth: [`../main_content.md`](../main_content.md)

## Summary

A standalone, one-page résumé at `wpooley.com/resume.html`. Renders cleanly on screen and
exports to a crisp single-page PDF via the browser's native print dialog. Linked from the
main site's nav and About section (replacing the old static `src/assets/wpooley_resume.pdf`).

## Design Principle — Standalone Styling (important)

**The résumé's visual style is intentionally decoupled from the main site.**

- The **main site** is getting a totally new design — an old-school **terminal / Warhammer**
  aesthetic (think green CRT terminal, possibly an **amber/orange** accent — *to be
  determined* in [`mainsite.md`](./mainsite.md)).
- The **résumé must NOT follow that theme.** It must read like a professional document
  (think Word/Google Doc): **white background, neutral fonts, conservative colors.** This
  is what hiring managers and ATS expect, and a terminal theme would undercut it.
- `src/resume.html` therefore carries its **own self-contained styles** (embedded `<style>`),
  with no dependency on `src/index.css`. Changing the site theme must not affect the résumé.

## Current Implementation

- **Layout:** two columns — experience (main) + skills/education/certifications (sidebar);
  full-width header with name, title, and contact line.
- **Type:** Calibri-led neutral sans stack (Word-document feel).
- **Accent:** classic Office-navy `#1f4e79`, exposed as a single CSS variable `--accent`
  so the whole sheet can be re-accented in one edit. (Amber alternative noted below.)
- **Export:** "Download PDF" button calls `window.print()`; an `@media print` block hides
  the toolbar and constrains output to one US-Letter page.
- **Contact location:** Corpus Christi, TX.

## Accent Decision

- **Chosen:** Office-navy `#1f4e79` — professional, neutral, prints well.
- **Considered:** amber/orange (to mirror the future mainsite). Rejected for the résumé
  because it conflicts with the conservative "looks like a Word doc" requirement. Amber is
  reserved for the mainsite.
- **To switch accents:** change the `--accent` variable in `src/resume.html` (e.g. amber
  `#b5651d`). One-line change.

## Open / Future

- Decide whether to delete or regenerate the legacy `src/assets/wpooley_resume.pdf` (currently
  unlinked but still in repo).
- Confirm preferred contact email (`contact@wpooley.com` vs `wcpooley@gmail.com`).
- Keep content in sync with `main_content.md` whenever experience changes.
