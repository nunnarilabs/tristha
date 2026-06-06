# Task 2 — Research & Web Search

**Goal:** feel the difference between Claude answering from memory vs. Claude *researching* the live web with sources.

## Step A — Ask without web (baseline)
Turn web search OFF (or just ask plainly) and run:

> "What are the current ISO 20022 migration deadlines for cross-border payments, and what changed most recently?"

Notice: Claude may answer from training data, may be out of date, and won't cite live sources. Point this out.

## Step B — Same question WITH web search
Turn web search ON and run the same prompt. Notice it now fetches current pages and cites them.

## Step C — Use Claude Research (deep, multi-source)
Run the full research brief below. This fans out across many sources and returns a structured, cited report.

> **Research brief.** You are briefing a BFSI QA practice. Research the **current (2026) state of ISO 20022 migration for payments** (cross-border via SWIFT, and any India/RTGS context). Produce:
> 1. A 5-line executive summary of where things stand now.
> 2. Key dates/milestones still ahead.
> 3. **Seven concrete testing implications for a payments QA team** — what new fields, validations, or message flows we must test (e.g., structured remittance data, enhanced party data, character-set rules).
> 4. Three risks if testing is inadequate.
> 5. A short list of authoritative sources with links.
> Use only information you can find and cite. Where sources disagree or are unclear, say so.

## What to compare / discuss
- **No web:** confident but possibly stale, no citations.
- **Web search:** current, cited, quick.
- **Research:** broader, multi-source, structured — best for a briefing you'd actually send.

## BFSI relevance
This is exactly how a test lead can get up to speed on a regulatory or standards change (ISO 20022, UPI feature releases, RBI circulars) before scoping a test effort — in minutes, with sources to verify.

> Optional swap-in topics if you prefer: "UPI new features and limits in 2026 and their testing implications" or "RBI's latest guidelines on digital payment security testing."
