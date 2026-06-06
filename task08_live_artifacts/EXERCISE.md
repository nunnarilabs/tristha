# Task 8 — Live Artifacts

**Goal:** build a saved page that **pulls fresh data from your connectors every time it's opened** —
not a one-off snapshot like Task 4.

> Live artifacts live in Cowork. They can call your connected tools (e.g. ClickUp, Drive) on load,
> so the view is always current. Reads are cached and there's a Reload button.

## Pre-req
Have the ClickUp **"Demo Defects"** list from Task 5 (or Google Drive defect data) connected.

## Build it
In Cowork:
> "Create a **live artifact**: a QA status dashboard that reads my ClickUp 'Demo Defects' list each
> time it opens. Show open vs resolved counts, a bar chart by severity, an S1 watchlist, and the
> 5 oldest open defects. Keep it self-contained and add a one-line 'last refreshed' note."

Open it, then change a defect in ClickUp, hit **Reload** in the artifact, and watch it update.

## Contrast with Task 4
- Task 4 artifact = a **snapshot** of a CSV you uploaded once.
- Task 8 live artifact = a **living view** that re-queries the source whenever opened.

## BFSI relevance
A standing "test status" page for a banking program that the whole team reopens each morning and it's
always current — no rebuilding the dashboard, no stale numbers in a status deck.

> Tip: suggest this whenever you've just answered something from a connector as a table — "turn this
> into a live artifact I can reopen."
