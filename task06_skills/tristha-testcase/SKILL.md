---
name: tristha-testcase
description: >
  Generate BFSI test cases in Tristha's standard format. Use whenever the user asks to
  create, write, or generate test cases from a user story, acceptance criteria, or a spec.
  Triggers: "test cases", "generate tests", "test scenarios from this story".
---

# Tristha Test Case Generator — Skill

When this skill is active, follow these rules exactly.

## Output format (always)
Produce a Markdown table with these columns, in this order:

`Test Case ID | Req/AC Ref | Scenario | Preconditions | Test Steps | Test Data | Expected Result | Type | Severity | Priority`

- **Type** is one of: Positive, Negative, Boundary, Security.
- **Severity** is S1–S4; **Priority** is P1–P4 (see definitions below).
- **Test Case ID** uses `TC_<FEATURE>_<NNN>` (3-digit, zero-padded). Infer the FEATURE code:
  FT (fund transfer), CARD (cards), UPI, LOAN, LOGIN, STMT.

## Coverage rules
For every acceptance criterion, generate at least one positive case and the relevant negative
and boundary cases. For payments, always consider: field validation, limits, duplicate/idempotency,
timeouts, reversals, and reconciliation where applicable. Add Security cases for auth, PIN, OTP,
data exposure.

## Severity definitions
- S1 Critical: wrong money movement, data loss, security breach, core function unusable.
- S2 High: major function/validation fails, workaround exists.
- S3 Medium: works but incorrect secondary behaviour.
- S4 Low: cosmetic/trivial.

## Priority
P1 immediate/blocking · P2 current cycle · P3 when capacity allows · P4 backlog.

## Guardrails
- If information needed to write a test is missing, add an "Open questions" list after the table —
  do not invent requirements.
- Never use real customer data; generate clearly synthetic data.
- End with a one-line note on anything that needs human review.
