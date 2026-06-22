# CLAUDE.md

## What this project is

This repository is **wpooley.com** — the personal website and portfolio of William
Pooley, a backend software engineer. It is **open source on purpose**: alongside the
site itself, it hosts working example projects and demonstrates **spec-driven
development with agentic AI tooling** (specs are written first, implementation follows,
and the two stay in sync).

## How this repo is organized

- **Specs come first.** High-level strategy lives in [`docs/requirements.md`](docs/requirements.md);
  per-project/feature details live in individual spec files under
  [`docs/specs/`](docs/specs/).
- The site shell is vanilla HTML/CSS/JS, now under [`src/`](src/) (`src/index.html`,
  `src/index.css`, `src/index.js`). Hosting is moving to AWS (S3 + CloudFront, free
  tier); the legacy GitHub Pages setup (`src/CNAME`) is being retired.
- Career narrative source of truth: [`docs/main_content.md`](docs/main_content.md).

## Working agreement

- **Read the spec before implementing.** For any feature/project, consult its spec in
  `docs/specs/` (and `docs/requirements.md` for overall goals/constraints) first.
- **Update specs alongside code.** If behavior changes, update the spec in the same pass.
- **No secrets in the repo.** It's public; cloud secrets go in AWS Secrets Manager.
- **ToS-clean data sources only** for portfolio projects (no scraping that violates a
  provider's Terms of Service).

➡️ See [`docs/requirements.md`](docs/requirements.md) for the full strategy and goals.
