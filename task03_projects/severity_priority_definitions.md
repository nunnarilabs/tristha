# Severity & Priority Definitions (Tristha standard)

## Severity (impact of the defect)
- **S1 — Critical:** Money movement is wrong, data loss/corruption, security breach, or the
  core function is completely unusable. Example: double debit, wrong beneficiary credited.
- **S2 — High:** Major function fails or a key limit/validation is not enforced, but a
  workaround exists. Example: daily limit not enforced.
- **S3 — Medium:** Function works but with incorrect/secondary behaviour. Example: confirmation
  SMS not sent though transfer succeeds.
- **S4 — Low:** Cosmetic, minor UI/text, or trivial issue with no functional impact.

## Priority (how soon to fix)
- **P1 — Immediate:** Blocks release / production-impacting. Fix now.
- **P2 — High:** Fix in current cycle.
- **P3 — Medium:** Fix when capacity allows.
- **P4 — Low:** Backlog.

> Severity is about impact; priority is about urgency. A cosmetic issue on the login page of a
> public banking portal can be S4 but P1. Always set both, with a one-line reason.
