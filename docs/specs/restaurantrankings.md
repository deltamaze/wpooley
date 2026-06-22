# Spec: Corpus Christi Restaurant Rankings

> Status: **PLACEHOLDER / DRAFT.** Captures intent; key data-source decision is OPEN.
> Parent goals: [`../requirements.md`](../requirements.md)
> Sibling project (shared architecture): [`bookrankings.md`](./bookrankings.md)

## Summary

A full-stack portfolio project: a **dashboard** that ranks Corpus Christi restaurants
and visualizes **movement in the rankings over time** (a restaurant trending up or
down), backed by a serverless **AWS** pipeline. Split cleanly into a front-end
dashboard and a backend API + nightly ingestion job.

This project exists to demonstrate backend + cloud architecture (API Gateway →
Lambda → DynamoDB) and a data pipeline, in addition to a polished front end.

## Architecture (intended)

```
                       ┌─────────────────────────────────────────┐
   Nightly schedule    │  Ingestion Lambda (scheduled)            │
   (EventBridge cron) ─▶│   fetch restaurant/review data          │
                       │   → write to DynamoDB                     │
                       └───────────────┬───────────────────────────┘
                                       │
                                  ┌────▼─────┐
                                  │ DynamoDB │  (restaurant + rankings history)
                                  └────┬─────┘
                                       │
   Frontend dashboard ──HTTP──▶ API Gateway ──▶ API Lambda ──▶ reads DynamoDB
   (in this repo / Pages)
```

- **Frontend:** dashboard (in-repo, served from main site / GitHub Pages) that calls
  the backend API and renders rankings.
- **API:** AWS API Gateway → Lambda → DynamoDB read. Returns current rankings +
  movement data to the frontend.
- **Ingestion:** a separate Lambda on a **nightly schedule** (EventBridge) that fetches
  restaurant data from the chosen source and writes/updates DynamoDB, recording
  historical snapshots so movement can be computed.
- **Datastore:** DynamoDB table(s) for current state + ranking history.

## Functional Requirements (draft — to expand)

- [ ] Dashboard shows current ranked list of Corpus Christi restaurants (top spot, etc.).
- [ ] Show **movement** vs. previous period: up/down arrow + a delta number, colored
      (e.g. green = up, red = down).
- [ ] Apply the **minimum-reviews floor** (see Ranking Principles below) so newly-listed
      restaurants with a couple of 5-star reviews don't dominate the rankings.
- [ ] Nightly refresh of underlying data.
- [ ] Reasonable handling of new/removed restaurants in the rankings.

## Ranking Principles

- **Minimum-reviews floor (shared with book rankings):** when sorting by rating, exclude
  items below a review-count threshold (default **≥ 100 reviews**). This removes super-new
  restaurants showing a perfect rating off only a handful of reviews.
  See `../requirements.md` → "Ranking Principles" for the shared rationale.

## Cloud / Ops Approach (v1)

- **Setup:** manual configuration in the AWS Console (copy/paste Lambda code, wire up
  API Gateway, DynamoDB, EventBridge schedule) — **no CloudFormation/IaC in v1**.
- **Secrets:** all credentials (API keys, etc.) stored in **AWS Secrets Manager** —
  never committed to this open-source repo.
- **Reproducibility:** manual setup steps to be documented in this spec (or a
  `SETUP.md`) so the stack can be rebuilt from scratch.
- **Cost:** stay within AWS free-tier limits where possible.

## ⚠️ OPEN DECISION — Data Source (must resolve before build)

The original idea included a **Google Maps review scraper** and/or the **Yelp API**.
Both have Terms-of-Service constraints that matter for a public, employer-facing repo:

- **Google Maps review scraping** violates Google's Terms of Service. Not advisable for
  a portfolio piece.
- **Yelp Fusion API** generally **prohibits storing/caching** their data in your own
  database, which conflicts with the DynamoDB-snapshot design.

Candidate ToS-clean approaches (pick one):

1. **Google Places API (official)** — paid but has a free tier; allowed usage; check
   data-retention terms (some fields have caching limits, IDs are cacheable).
2. **Seeded / static dataset** — curate a Corpus Christi restaurant dataset and simulate
   review/ranking changes. Fully clean; lets the engineering (pipeline + dashboard)
   shine without ToS risk. Good v1.
3. **Other licensed API** — research alternatives that permit storage.

➡️ **Decision needed.** Recommendation: start with option 2 (seeded data) to build the
full pipeline + dashboard ToS-cleanly, then optionally layer in an official API later.

## Open Questions

- Ranking metric: by rating, review count, a composite score?
- Movement window: night-over-night, weekly, configurable?
- How many restaurants in scope?
