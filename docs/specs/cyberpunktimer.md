# Spec: Cyberpunk Timer (Rebuild)

> Status: **PLACEHOLDER / DRAFT.** Captures intent; details to be expanded before build.
> Parent goals: [`../requirements.md`](../requirements.md)

## Summary

Rebuild the existing Cyberpunk Timer as an **in-repo project** using **vanilla
JavaScript / HTML / CSS** (no framework), with the help of agentic AI tooling.
Decommission the old externally-hosted Blazor/WASM version once the rebuild is live.

## Background

- Original: a standup-meeting timer built in client-side Blazor/C# on WebAssembly,
  hosted at `deltamaze.github.io/CyberPunkTimer`.
- Motivation (original): time daily standups and distribute the allotted time evenly
  across team members.

## Goals

- Reimplement core functionality in vanilla JS/HTML/CSS, living in this repository.
- Demonstrate clean, dependency-free front-end engineering.
- Retire the legacy hosted version (update/remove links on the main site).

## Functional Requirements (draft — to expand)

- [ ] Configure number of participants and total meeting time.
- [ ] Evenly distribute time per participant; advance through turns.
- [ ] Start / pause / reset; visual + (optional) audible turn transitions.
- [ ] "Cyberpunk" visual aesthetic (carry over the look/feel).

## Open Questions

- Persist settings between sessions (localStorage)? 
- Mobile layout requirements?
- Keep exact original feature set, or trim/expand?

## Notes

- This is a front-end-only project; no backend.
- Will live under the main site's navigation (see `mainsite.md` embedding decision).
