# Spec: AWS Infrastructure & CI/CD

> Status: **DRAFT — for review.** Nothing built yet; this documents the action plan.
> Parent goals: [`../requirements.md`](../requirements.md)
> Related: [`mainsite.md`](./mainsite.md), [`restaurantrankings.md`](./restaurantrankings.md),
> [`bookrankings.md`](./bookrankings.md)

## Summary

Move hosting off GitHub Pages onto **AWS**, and stand up the cloud foundation the
portfolio projects will share. Two layers:

1. **Static site hosting** for the main site (`src/`) — S3 + CloudFront + ACM (TLS),
   custom domain `wpooley.com`.
2. **Serverless backend foundation** for the ranking projects — API Gateway → Lambda →
   DynamoDB, defined as Infrastructure-as-Code so the repo *is* the source of truth.

Everything is **codified (IaC) and deployed from GitHub Actions** — no click-ops, no
secrets committed, free-tier-friendly.

## Guiding constraints (from requirements.md)

- **Open source / public repo.** No secrets in the repo. No long-lived cloud keys
  anywhere we can avoid them.
- **Free-tier-friendly.** Expected traffic is a few hundred requests/month.
- **Reproducible.** The stack can be rebuilt from this repo via documented commands.
- **GitHub-native.** Stay on GitHub (public profile). CI/CD via **GitHub Actions**
  (not Azure DevOps — that's the day-job stack; this repo deliberately uses GH Actions).

## Authentication: GitHub OIDC, not stored keys (important)

> This is the main design decision to confirm.

The instinct is to create an AWS "service account" (IAM user) and paste its access
key + secret into GitHub Actions secrets. **We should not do that.** Static keys are
long-lived, leak-prone, and contradict the repo's "no secrets" principle.

Instead use **GitHub OIDC federation**:

- AWS trusts GitHub's OIDC identity provider. A GitHub Actions workflow requests a
  short-lived token and **assumes an IAM role** scoped to this repo (and optionally a
  specific branch/environment). No static credentials are stored — GitHub holds *nothing*
  secret; AWS holds only a role + trust policy.
- One-time manual setup in AWS: create the OIDC identity provider
  (`token.actions.githubusercontent.com`) and a deploy IAM role whose trust policy
  pins `repo:deltamaze/wpooley:*`.
- The workflow uses `aws-actions/configure-aws-credentials` with `role-to-assume` and
  `permission: id-token: write`.
- **App-level secrets** (3rd-party API keys for ingestion, etc.) live in **AWS Secrets
  Manager**, read by Lambdas at runtime — never in GitHub, never in the repo.

What GitHub *does* hold (non-secret config / variables, not secrets): the AWS account ID,
region, and role ARN — fine as repo **Variables**.

## Infrastructure-as-Code choice

**AWS SAM** as the primary tool. SAM is a superset of CloudFormation: it's purpose-built
for the serverless ranking projects (Lambda/API Gateway/DynamoDB) *and* can declare the
plain CloudFormation resources for static hosting (S3/CloudFront/ACM) in the same
template language. One tool, one mental model.

- _Alternative considered:_ AWS CDK (TypeScript). More expressive, but adds a build/synth
  step and a language dependency. SAM keeps it declarative and closer to raw CFN, which
  is easier to read in a portfolio context. **Default: SAM.** Revisit if templates get
  unwieldy.
- Static-site and backend infra likely split into **separate stacks** (different change
  cadence, different blast radius), both under an `infra/` (or `template.yaml` per
  project) layout — exact directory layout is an open question below.

## Target architecture

### Static site (main site)
```
Squarespace (registrar) -> NS delegate -> Route 53 (hosted zone, apex ALIAS) -> CloudFront (TLS via ACM in us-east-1) -> S3 (private, OAC)
```
- S3 bucket holds the contents of `src/` (private; served only through CloudFront via
  Origin Access Control).
- ACM certificate for `wpooley.com` must be in **us-east-1** (CloudFront requirement).
- **DNS (decided):** `wpooley.com` is registered at **Squarespace** (migrated from Google
  Domains). Keep registration there but **delegate DNS to a Route 53 hosted zone** (set
  Squarespace's nameservers to the Route 53 NS records). Reason: the **apex** domain must
  point at CloudFront, and Squarespace DNS can't ALIAS a bare apex to CloudFront — Route 53
  ALIAS records can. Cost: ~$0.50/mo for the hosted zone.

### Serverless backend (ranking projects — later phase)
```
EventBridge (nightly) -> Ingestion Lambda -> DynamoDB
API Gateway (HTTP API) -> Read Lambda -> DynamoDB -> dashboard (served from the static site)
```
- Shared pattern reused across restaurants + books (see those specs).
- Secrets (data-source API keys) from AWS Secrets Manager.

## CI/CD (GitHub Actions)

Per-push to `main` (and PR validation):

1. **Auth:** assume the deploy role via OIDC (no stored keys).
2. **Backend infra:** `sam build` + `sam deploy --no-confirm-changeset` for changed stacks.
3. **Site deploy:** `aws s3 sync src/ s3://<bucket>` then a **CloudFront invalidation**
   (`/*`) so the edge cache serves the new build.
4. (PRs) run `sam validate` / `cfn-lint` and a dry-run changeset; deploy only on `main`.

Workflows live in `.github/workflows/`. Start with a single environment (`prod`); add
a `staging` environment later only if warranted.

## Cost expectation (free-tier)

- **CloudFront:** always-free tier (1 TB egress + 10M requests/mo) — far above expected use.
- **S3:** pennies (free 12 months); tiny site.
- **Lambda / DynamoDB / API Gateway:** free-tier covers a few hundred calls/month easily.
- **ACM cert:** free. **Route 53:** ~$0.50/mo per hosted zone *if* used (avoidable).
- Net: effectively $0–$0.50/month.

## Action plan (phased)

- **Phase 0 — Decide (this spec).** Confirm OIDC-over-keys, SAM-over-CDK, DNS approach,
  repo layout. _← we are here._
- **Phase 1 — Static hosting.** Manual one-time: OIDC provider + deploy role. SAM stack
  for S3 + CloudFront + ACM. GH Actions workflow to sync `src/` + invalidate. Cut
  `wpooley.com` DNS over from GitHub Pages to CloudFront. Retire Pages + remove
  `src/CNAME`. Refresh `README.md`.
- **Phase 2 — Backend foundation.** SAM stack for the shared ranking pattern (API GW +
  Lambda + DynamoDB + EventBridge), Secrets Manager wiring. Build against one domain
  (restaurants) first.
- **Phase 3 — Reuse + harden.** Apply the pattern to books; add monitoring/alarms,
  least-privilege IAM review, optional staging env.

## Open questions

1. **One stack or many:** separate static-site and backend stacks (recommended) vs. a
   single monolithic template?
2. **CloudFront cache/SPA behavior:** custom error responses / routing rules needed once
   projects become sub-pages?
3. **MFA on root:** is MFA already enabled on the root user? (Recommended before going
   further — see decision below.)

## Decisions

- **DNS (resolved):** Registrar stays **Squarespace** (where `wpooley.com` landed after
  the Google Domains migration). **Delegate DNS to a Route 53 hosted zone** so the apex
  can ALIAS to CloudFront (Squarespace DNS can't ALIAS a bare apex). ~$0.50/mo (~$6/yr).
  Total domain+DNS ≈ ~$21/yr (Squarespace reg ~$15 + hosted zone ~$6). DNS records are
  managed in IaC (`AWS::Route53::HostedZone` + record sets); registration stays a manual
  console action.
  - _Considered & deferred — consolidate registration into Route 53:_ saves only ~$2/yr
    (.com ~$13 vs $15) and does **not** remove the hosted-zone fee (registering in Route 53
    auto-creates a billed hosted zone). Marginal; revisit only if consolidating providers.
  - _Considered & rejected — Cloudflare free DNS (apex flattening):_ would zero the $0.50/mo
    but moves DNS outside AWS/IaC, undercutting the all-in-AWS portfolio story.
- **IaC layout (resolved):** Use a top-level **`infra/`** directory (common convention),
  with **separate stacks** per concern (static site vs. backend) as `.yaml` templates
  inside it. Lambda/app source lives under `src/` (or per-project), kept distinct from
  `infra/`.
- **Account & identity (resolved):** Use the **existing personal AWS account**. Pipelines
  authenticate via **GitHub OIDC → least-privilege IAM deploy role** — never root, never
  static keys. Console review stays as **root for now** (solo account, simplicity), with
  two guardrails: **(a) enable MFA on root** if not already, and **(b)** consider an IAM
  admin user for day-to-day console use later. No existing OIDC provider — create one in
  Phase 1.
- **Auth model (proposed, pending build):** GitHub OIDC over stored keys — see
  [Authentication](#authentication-github-oidc-not-stored-keys-important).
- **IaC tool (proposed, pending build):** AWS SAM over CDK.
