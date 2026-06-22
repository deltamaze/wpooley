# wpooley.com — Requirements & Strategy

> Top-level **strategy and goals** for the personal website and its embedded projects.
> **Specific feature details for each project live in individual spec files under
> [`docs/specs/`](./specs/)** — this document stays at the strategy level and points there.

## Purpose

A personal site at **wpooley.com** that serves as a living portfolio for a backend
software engineer. Beyond a static résumé, the site hosts **working example projects
built directly in this repository** to demonstrate hands-on engineering across the
stack — backend services, cloud architecture, and clean front-end work.

This repository is **open source on purpose**: it doubles as evidence of how I work,
including **spec-driven development with agentic AI tooling**. Specs come first
(`docs/specs/`), implementation follows, and the two stay in sync.

## Goals

1. **Showcase real engineering, not just claims.** Replace externally-hosted legacy
   demos with projects that live in this codebase and can be read, run, and reviewed.
2. **Demonstrate backend + cloud depth.** At least one project should exercise a real
   cloud backend (API gateway → compute → datastore) with a documented architecture.
3. **Demonstrate spec-driven development.** Every project ships with a spec in
   `docs/specs/` written before/alongside the code.
4. **Keep the front end clean and fast.** Lightweight, framework-light, fast-loading,
   mobile-friendly.
5. **Stay current and accurate.** Site content reflects the present (current role:
   Senior Software Engineer at DentaQuest); single source of truth for career narrative
   is [`main_content.md`](./main_content.md).

## Non-Goals (for now)

- No heavy SPA framework for the main site unless a project specifically warrants it.
- No infrastructure-as-code in v1 of the cloud project (manual AWS console setup is
  acceptable to start; see project spec). IaC is a documented future enhancement.
- No paid hosting requirement for the main site (currently GitHub Pages; migrating to
  AWS S3 + CloudFront on the free tier).

## Strategy

The portfolio is built around a deliberate progression of project types, each chosen to
demonstrate a different competency to a backend-focused hiring audience:

1. **Front-end fundamentals** — a clean, dependency-free vanilla JS project (Cyberpunk
   Timer rebuild) proving solid front-end engineering without leaning on a framework.
2. **Reusable full-stack cloud architecture** — a serverless ranking pipeline
   (API Gateway → Lambda → DynamoDB + nightly ingestion) applied to **two different
   domains** (restaurants, books). Shipping the same well-factored pattern twice shows
   architectural reuse and judgment, not just one-off scripts.
3. **Spec-driven, AI-assisted workflow** — every project is specced before it's built,
   and the specs live in the repo so the *process* is itself a portfolio artifact.

Detailed, per-project requirements (functional behavior, data model, open questions)
are intentionally **not** in this file — they live in each project's spec under
[`docs/specs/`](./specs/).

## Ranking Principles (shared across ranking projects)

These apply to both the restaurant and book ranking projects:

- **Minimum-reviews floor.** When sorting by rating, exclude items below a review-count
  threshold (**default ≥ 100 reviews**). Sorting purely by star rating surfaces brand-new
  items with a perfect score off a handful of reviews; the floor filters that noise out
  and produces rankings that reflect established popularity. The threshold should be a
  configurable constant.
- **Movement over time.** Rankings record historical snapshots so the dashboard can show
  whether an item is trending up or down (arrow + colored delta), not just a static list.

## Planned Projects

| Project | Spec | Theme | Status |
|---|---|---|---|
| Cyberpunk Timer (rebuild) | [`specs/cyberpunktimer.md`](./specs/cyberpunktimer.md) | Vanilla front-end, in-repo | Planned |
| Corpus Christi Restaurant Rankings | [`specs/restaurantrankings.md`](./specs/restaurantrankings.md) | Full-stack AWS backend + dashboard | Planned |
| Book Rankings | [`specs/bookrankings.md`](./specs/bookrankings.md) | Same AWS pattern, books domain | Planned |

## Constraints & Principles

- **Open source.** No secrets in the repo. Cloud secrets via **AWS Secrets Manager**.
- **Legal/ToS-clean data sources.** Portfolio projects must not rely on scraping or
  data use that violates a provider's Terms of Service (see restaurant spec open
  question).
- **Reproducible.** Manual setup steps must be documented so the project can be
  rebuilt from this repo.
- **Cost-aware.** Prefer free-tier-friendly cloud usage.

## Open Decisions (tracked in specs)

- AWS hosting & CI/CD foundation (replacing GitHub Pages) → [`specs/aws_infrastructure.md`](./specs/aws_infrastructure.md)
- Main site technology stack & navigation pattern → [`specs/mainsite.md`](./specs/mainsite.md)
- Restaurant data source (ToS-clean) → [`specs/restaurantrankings.md`](./specs/restaurantrankings.md)
- Book data source (ToS-clean) → [`specs/bookrankings.md`](./specs/bookrankings.md)
