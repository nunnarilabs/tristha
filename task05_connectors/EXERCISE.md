# Task 5 — Connectors under a Project

**Goal:** let Claude reach live systems — Google Drive, ClickUp, Gmail — from inside a Project,
so it works from the source instead of pasted text.

> Connectors are enabled in Settings → Connectors (Claude Desktop / claude.ai). For BFSI,
> only connect **approved, non-production / sandbox** accounts with safe sample data.
> Claude inherits *your* permissions — it sees only what your account can see.

## Setup (once)
1. In your "Tristha Test Case Generator" Project, open **Connectors** and enable:
   **Google Drive**, **ClickUp**, **Gmail**.
2. Stage the sample content first:
   - Upload the two files in `gdrive_files_to_stage/` to a Google Drive folder named
     **"Tristha Demo Specs"**.
   - In ClickUp, create a list **"Demo Defects"** and add 3–4 tasks (you can copy rows from
     `../task04_artifacts/defects_export.csv`).
   - In Gmail, have a sample thread (or send yourself one) titled **"UAT Status — Demo Bank"**.

## Exercise A — Google Drive
> "From my Drive folder 'Tristha Demo Specs', read the UPI collect-request spec and generate
> test scenarios for it using our standard."
→ Claude fetches the file from Drive — no copy-paste.

## Exercise B — ClickUp
> "Look at the 'Demo Defects' list in ClickUp. Summarise by severity, flag any S1, and draft a
> one-line status for each open item."
→ Claude reads your live task list.

## Exercise C — Gmail
> "Find the 'UAT Status — Demo Bank' email thread and draft a concise, professional reply with
> today's progress: 18 tests executed, 15 passed, 2 S1 defects open, go/no-go on Friday."
→ Claude drafts a reply grounded in the thread. **It drafts; you send.**

## Discuss
- Connectors turn Claude from "answers questions" into "works with your actual tools".
- Security: admin-approved, permission-scoped, never connect production client data without sign-off.

## BFSI relevance
Read the spec from Confluence/Drive, pull defects from your tracker, draft the client email —
all without leaving Claude or copy-pasting sensitive content around.
