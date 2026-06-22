# Spec: Book Rankings

> Status: **PLACEHOLDER / DRAFT.** Captures intent; key data-source decision is OPEN.
> Parent goals: [`../requirements.md`](../requirements.md)
> Sibling project (shared architecture): [`restaurantrankings.md`](./restaurantrankings.md)

## Summary

A full-stack portfolio project that ranks **books** by popularity/rating and visualizes
**movement in the rankings over time**, backed by the same serverless **AWS** pattern as
the restaurant rankings project. Dashboard shows the most popular books and whether each
is trending up or down.

This is intentionally a **second application of the same architecture** (API Gateway →
Lambda → DynamoDB + nightly ingestion) in a different domain — demonstrating a reusable,
well-factored backend pattern.

## Architecture (intended)

Same shape as [`restaurantrankings.md`](./restaurantrankings.md):

```
   Nightly schedule (EventBridge) ─▶ Ingestion Lambda ─▶ DynamoDB (books + rankings history)
   Frontend dashboard ──HTTP──▶ API Gateway ─▶ API Lambda ─▶ reads DynamoDB
```

## Functional Requirements (draft — to expand)

- [ ] Dashboard shows a ranked list of the most popular books.
- [ ] Show **movement** vs. previous period: up/down arrow + colored delta number
      (green = up, red = down).
- [ ] Apply the **minimum-reviews floor** (see Ranking Principles below) to avoid
      books with very few reviews dominating by rating.
- [ ] Nightly refresh of underlying data.

## Ranking Principles

- **Minimum-reviews floor (shared with restaurant rankings):** when sorting by rating,
  exclude items below a review-count threshold (default **≥ 100 reviews**). This filters
  out brand-new books that show a perfect rating off only a handful of reviews.
  See `../requirements.md` → "Ranking Principles" for the shared rationale.

## Cloud / Ops Approach (v1)

Identical to the restaurant project: manual AWS Console setup (no IaC in v1), secrets in
AWS Secrets Manager, document manual steps for reproducibility, stay free-tier-friendly.

## ⚠️ OPEN DECISION — Data Source (must resolve before build)

The original idea was to **scrape Goodreads** review data. Constraints for a public,
employer-facing repo:

- **Goodreads** retired its public API (Amazon-owned) and **scraping it violates their
  Terms of Service.** Not advisable for a portfolio piece.

Candidate ToS-clean approaches (pick one):

1. **Open Library API / data dumps** (openlibrary.org) — genuinely open data, bulk
   downloads permitted. Strong, clean default for books.
2. **Google Books API** — official, free tier; check data-retention terms.
3. **Seeded / static dataset** with simulated rating changes — fully clean; lets the
   pipeline + dashboard engineering shine. Good v1.

➡️ **Decision needed.** Recommendation: **Open Library** as the real source (it's open),
falling back to a seeded dataset if needed to demonstrate movement over time.

## Open Questions

- Ranking metric: rating, number of ratings, a composite popularity score?
- Scope: all books, a genre, a curated list, bestsellers?
- Movement window: nightly, weekly, configurable?
