# LinkedIn / Career Content - Master Source of Truth

> This is the single source of truth for William Pooley's professional narrative.
> LinkedIn, resume, and website all derive from this file. Update here first, then sync.
>
> **Positioning:** Backend software engineer with distributed-systems depth, leveraging
> Azure-scale experience (ex-Microsoft) as a differentiator. Targeting senior backend SWE
> roles at top engineering orgs (Amazon, SpaceX, etc.).
>
> **`[FILL]`** markers = high-value spots where a real metric would strengthen the line.
> Replace with a number if you have one; otherwise we can soften the phrasing.

---

## Headline (LinkedIn - 220 char max)

**Primary (recommended):**
> Senior Software Engineer @ DentaQuest (Sun Life) · Ex-Microsoft Azure | Backend & Distributed Systems - .NET, APIs, FHIR Interoperability

**Alternates:**
> Backend Software Engineer | Ex-Microsoft Azure API Management | Distributed Systems, .NET, Cloud-Scale APIs

> Senior Software Engineer - Backend & APIs at scale | Built GraphQL GA for Azure API Management | .NET / C# / Azure

---

## About / Summary

> Backend software engineer with 10+ years building the systems that move data and money at scale - from cloud platform services used by enterprises worldwide to federal healthcare interoperability infrastructure.
>
> At Microsoft, I helped ship GraphQL support to General Availability in Azure API Management - owning the passthrough proxy, WebSocket subscription support for real-time traffic, and the telemetry and SDK surfaces that made it production-ready. I also kept the compute fleet behind customer API gateways healthy and observable through on-call rotations and fleet-wide monitoring.
>
> Today, as a Senior Software Engineer at DentaQuest (a Sun Life company), I lead the architecture and delivery of our CMS interoperability compliance program across two federal mandates (CMS-9115 and CMS-0057-F). I designed a custom FHIR Façade in ASP.NET Core that queries our claims database in real time - eliminating ETL lag entirely - and built the SMART-on-FHIR auth flow (Okta, consent management, an Azure Function authorization proxy) for Patient Access. I also automated our appeals workflow end to end, cutting review time by ~70%.
>
> I care about clean service boundaries, real-time data paths over brittle batch jobs, observability you can trust, and shipping things that survive contact with production. I'm strongest in .NET / C#, SQL Server, and the Azure platform, and I'm comfortable owning a feature from architecture through GA and on-call.
>

---

## Experience

### DentaQuest (a Sun Life company) - Senior Software Engineer
*Apr 2023 – Present · Remote*

- Lead architect and engineer for DentaQuest's CMS interoperability compliance program across two federal mandates (CMS-9115, CMS-0057-F), driving on-time delivery ahead of the Jan 1, 2027 deadline.
- Architected a custom FHIR Façade in ASP.NET Core that queries the in-house claims SQL Server in real time (Firely .NET SDK + Dapper), replacing the Azure FHIR Server and **eliminating ETL lag** for compliance data.
- Technical lead for Patient Access API (CMS-9115): designed the full SMART-on-FHIR authentication flow - custom Authorization Proxy (Azure Function), Patient Picker app, Okta integration, and consent management in the Member Portal.
- Designed and specified Provider Access, Payer-to-Payer, Prior Authorization (Da Vinci CRD/DTR/PAS/CDex), and Bulk Data APIs; authored the functional requirements used across all engineering teams.
- Built end-to-end appeals workflow automation that **reduced appeal review time ~70%**, integrating the customer-service platform directly with the claims system and auto-generating decision letters from structured claim data - replacing a fully manual copy/paste-and-handtype process.
- Drove cross-team execution across claims, member portal, identity, infrastructure, and integration teams; used agentic AI tooling to accelerate FHIR server development velocity.

### Microsoft - Senior Software Engineer
*Sep 2021 – Mar 2023 · Austin, TX*

- Led the General Availability release of GraphQL support in Azure API Management (APIM), working with the core engineering team across telemetry, docs, and SDK surfaces.
- Owned the GraphQL **passthrough** implementation, enabling APIM to proxy GraphQL requests to backend services with full query forwarding.
- Designed and implemented **WebSocket subscription support** in the passthrough path, enabling real-time GraphQL subscription traffic through APIM.
- Contributed synthetic GraphQL-to-Cosmos DB resolver scaffolding (completed by the team after my transition); extended the Azure PowerShell libraries so customers could manage GraphQL APIs via scripting/automation.
- Instrumented end-to-end telemetry across the GraphQL feature for observability and GA operational readiness.
- Maintained health and compliance of the compute fleet running customer API gateways: monitoring-agent startup, fleet-wide heartbeat telemetry, agent version currency, and **on-call incident response**.

### Driscoll Health Plan - Data Integrity Analyst III
*Apr 2018 – Sep 2021 · Corpus Christi, TX*

- Built a Blazor Server-Side PWA for administrative control of application extracts and delivered web reports surfacing data discrepancies across systems (incl. MPF provider records).
- Developed C# applications to pull and categorize claim data for HHSC Financial Statistical Reports and provider Explanation-of-Payment documents.
- Built C#/SQL pipelines pulling provider data from the credentialing system to generate Enrollment Broker (P-Files) and Claims Transaction System extracts, plus various provider/claim/member extracts for third-party vendors and HHSC contractors.

### Sunoco - Senior Software Developer
*Mar 2014 – Mar 2018 · Corpus Christi, TX*

- Built and managed a C# application ingesting daily transaction-log XML from **700 retail store computers** into a central SQL Server for operational and accounting reporting.
- Managed an iOS/Objective-C employee learning-management app that captured assessment results to a local SQLite DB and synced to a central server.
- Created operational reports from sales and time-clock data using SQL and SSRS.

### Regency Nursing & Rehabilitation Centers - Database Administrator
*Oct 2011 – Feb 2014 · Victoria, TX*

- SQL Server administration: maintenance plans, backups, and SSRS reporting (Long-Term Care analytics, HR, Employee Self-Service, OIG Exclusion).
- Supported Microsoft Dynamics GP, American HealthTech LTC, and Kronos; provided application and desktop support.

---

## Skills (LinkedIn - pin top 3, list ~25–30)

**Pin these 3 (most searched for backend roles):**
1. C# / .NET
2. Distributed Systems
3. Microservices / APIs

**Full list:**
C#, .NET / ASP.NET Core, Microservices, RESTful APIs, GraphQL, WebSockets, Distributed Systems, System Design, Azure, Azure API Management, Azure Functions, SQL Server, Dapper, Entity Framework, Data Pipelines / ETL, Observability & Telemetry, On-Call / Incident Response, FHIR / Healthcare Interoperability, SMART on FHIR, OAuth / OIDC (Okta), Blazor, React, JavaScript, CI/CD, SSRS / Reporting, Software Architecture

---

## Featured / Projects (link these in the Featured section)

- **Simple Planner** - Firebase/React day planner with debounced three-way binding over a websocket connection. https://planner.wpooley.com/
- **Cyberpunk Timer** - Standup timer built in client-side Blazor/C# on WebAssembly. https://deltamaze.github.io/CyberPunkTimer/
- **Privacy Screen** - Chrome extension that reveals page content only on hover, with whitelist/blacklist modes. (Chrome Web Store)

---

## Education & Certifications

- **B.S. Computer Science**, University of Houston–Victoria - *Summa Cum Laude*, Dec 2011
- Epic: Chronicles Database Programmer (2019), Caboodle Development (2018), Caboodle-Clarity Development (2018)
- ITIL Foundation - IT Service Management

---

## Sync checklist (when this doc changes)

- [ ] LinkedIn: headline, About, current role bullets, skills, Featured links
- [ ] resume.html → re-export `assets/wpooley_resume.pdf`
- [ ] index.html: About paragraph ("currently working at Microsoft" is **wrong** - now DentaQuest), tagline

## Notes / open questions

- **Microsoft "Senior" title:** confirm exact title - was it "Senior Software Engineer" or "Software Engineer II"? (matters for resume accuracy)
- **Metrics to add if available:** scale of Azure APIM GraphQL usage (customers/requests), DentaQuest claims volume / # members served, appeals volume processed.
- **DentaQuest vs Driscoll** confirmed as separate jobs; timeline is clean and gap-free.
