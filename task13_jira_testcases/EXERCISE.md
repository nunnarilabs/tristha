# Task 13 — Jira → Test Cases (MCP connector)

**Goal:** connect Claude to Jira, pull a real user story from the source, and generate a
structured, review-ready test-case table — no copy-paste.

> Connectors are enabled in Settings → Connectors (Claude Desktop / claude.ai). For BFSI,
> connect only **approved, non-production / sandbox** accounts with synthetic data.
> Claude inherits *your* permissions — it sees only what your account can see.

## Setup (once)
1. In your **"Tristha Test Case Generator"** Project, open **Connectors** → enable the **Jira** (Atlassian) connector and sign in.
2. Sample data is already staged in the **`KAN` — "My Team"** project on `navaneethm.atlassian.net`:
   - **KAN-4** — `[Story]` Real-time card authorization for online card payments (7 acceptance criteria + non-functionals).
   - **KAN-5 … KAN-8** — four `[Defect]` items (S1–S3) linked to that story.
3. If you're using your own site, create one Task named like a user story with clear acceptance criteria, and note its key.

## Exercise A — Pull the story
> "Using the Jira connector, open issue **KAN-4** and show me the summary, the user story,
> and the acceptance criteria. Don't add anything yet."

→ Claude reads the live issue. Confirm it captured all 7 acceptance criteria + the non-functional notes.

## Exercise B — Generate test cases
> "You are a senior test analyst on a retail-banking program. From **KAN-4**, generate a
> structured test-case table covering every acceptance criterion. Include **positive, negative,
> boundary, and security/compliance** cases. Columns: *Test ID, Title, Type, Preconditions,
> Steps, Test Data, Expected Result, AC ref, Priority*. Use synthetic data only and mask any
> card numbers. Call out any acceptance criteria that are ambiguous or untestable as written."

→ Claude drafts the table grounded in the live story.

**What good looks like** (trainer check): coverage of all 7 ACs; explicit boundary cases on the
INR 2,00,000 limit (199,999 / 200,000 / 200,001 / 200,000.50); negative cases for codes 51 / 54 /
62; a security case for PAN masking (NFR); the fraud-lock case (3 declines → 4th attempt); and a
note that AC #1's "within 2 seconds" needs a performance test, not a functional one.

## Exercise C — Tighten & export
> "Trim to the 12 highest-value test cases for a smoke pass, then output as CSV I can import into
> our test management tool."

→ A focused, copy-paste-ready set.

## Stretch (read + write) — optional
> "Create the top 3 test cases back in Jira as sub-tasks under KAN-4, each with the steps and
> expected result in the description."

→ Demonstrates the connector writing back. **Claude drafts the create action; you confirm.**
Only do this on the sandbox project.

## Bonus — defect triage warm-up
> "Summarise the open `[Defect]` issues in the KAN project by severity, flag any S1, and draft a
> one-line UAT status for each."

→ Uses KAN-5…KAN-8. Good 2-minute lead-in if you have time.

## Discuss
- The connector turns Claude from "works on text you paste" into "works from the system of record" —
  the story can't drift out of sync because it's read live.
- Coverage is only as good as the acceptance criteria — Claude surfacing *untestable* ACs is a feature,
  not a failure.
- Security: admin-approved, permission-scoped, synthetic data; Claude drafts, a human reviews and owns
  every test case and every write-back.

## BFSI relevance
Requirement → test cases is the single biggest time sink for testing teams. Pulling the story straight
from Jira, generating coverage in your format, and (optionally) writing cases back closes the loop without
sensitive data ever leaving your approved tools.
