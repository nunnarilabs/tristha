# Task 1 — Answer Key (TRAINER ONLY)

Verified with a reference implementation. Use it to score each model.

| Txn | Card | INR amt | Decision | Code | Reason |
|---|---|---|---|---|---|
| T1 | A | 20,000 | Approved | 00 | All checks pass |
| T2 | D | 5,000 | Declined | 14 | Invalid card number (Luhn) |
| T3 | F | 5,000 | Declined | 43 | Card stolen |
| T4 | G | 5,000 | Declined | 54 | Card expired (03/2025) |
| T5 | E | 8,400 | Declined | 62 | International (USD) txn on intl-blocked card |
| T6 | H | 5,000 | Declined | 57 | Debit not permitted |
| T7 | A | 35,000 | Declined | 61 | Over ECOM limit (35,000 > 30,000) |
| T8 | B | 50,000 | Approved | 00 | POS limit = 50,000 (not over); ACC1 cum 20k→70k; bal 80k→30k |
| T9 | A | 20,000 | Declined | 61 | **Account daily cap**: 70,000 + 20,000 = 90,000 > 80,000 (balance was fine — trap) |
| T10 | B | (REV T8) | Processed | REV | Restore ACC1 bal +50,000 → 80,000; cum 70k→20k; remove B's velocity + approved-count |
| T11 | A | 20,000 | Approved | 00 | cum 20k→40k; ACC1 bal 80k→60k |
| T12 | C | 5,000 | Approved | 00 | ACC2 bal 40k→35k; C count 1 |
| T13 | C | 5,000 | Approved | 00 | ACC2 bal 35k→30k; C count 2 |
| T14 | C | 5,000 | Approved | 00 | ACC2 bal 30k→25k; C count 3 |
| T15 | C | 5,000 | Declined | 65 | **Velocity**: 3 approved (10:00,10:10,10:20) in last 60 min (balance fine — trap) |
| T16 | C | 30,240 | Declined | 61 | **FX over limit**: USD 360 × 84 = ₹30,240 > ₹30,000 ECOM limit (trap) |
| T17 | C | 30,000 | Declined | 51 | Velocity now OK (only 10:20 in window) & cap OK, but balance 25,000 < 30,000 |

**Final state:** ACC1 balance **₹60,000** · ACC2 balance **₹25,000** · approved-count today — **CARD-A = 2**, **CARD-B = 0** (T8 reversed), **CARD-C = 3**.

## The traps that separate the models

1. **T9 — daily cap vs balance (61, not 00/51).** ACC1's *balance* (₹30,000) would cover ₹20,000, so a money-only model approves it. Correct: the **account daily cap** is hit first (70k+20k>80k) → 61. Requires tracking the shared-account cumulative across CARD-A *and* CARD-B.
2. **T10 reversal effects.** The reversal must restore balance, **reduce the cumulative** (so later txns fit), **and** remove T8 from velocity/approved-count. Models often restore the balance but forget the cumulative or the count → everything downstream drifts.
3. **T15 — rolling-window velocity (65).** Three approvals at 10:00/10:10/10:20 are all within 60 min of 10:30 → 65, even though balance is fine. Models that count "per day" loosely, or include declined T-attempts, get this wrong.
4. **T16 — FX crossing a limit (61).** USD 360 *looks* small but converts to **₹30,240**, just over the ₹30,000 ECOM limit. Models that skip conversion, or round wrong, approve it.
5. **T17 — window has moved (51, not 65).** By 11:10 only the 10:20 approval is still inside the 60-min window (10:00 and 10:10 have aged out), so velocity is fine — the real reason is **insufficient balance** (25,000 < 30,000). Tests whether the model re-evaluates the window, not just reuses T15's conclusion.
6. **Shared-account bookkeeping throughout.** ACC1 balance must track 100k → (T1) 80k → (T8) 30k → (T10 rev) 80k → (T11) 60k, with cumulative moving 0→20k→70k→20k→40k. CARD-A and CARD-B both touch it.
7. **Boundaries:** T8 POS amount = 50,000 (= limit, allowed); T17 = 30,000 (= POS limit, allowed) so it must fall through to the balance check.

## Observed results (from a real run — use these as your live narration)

- **Haiku 4.5 — ~13/17, and revealingly unreliable.** Got the obvious declines (T2–T6) and T15 velocity, but **failed every interacting case**: T7 (missed the ECOM per-txn limit, approved ₹35,000), T9 (missed the daily cap), T11 (false velocity decline of a valid txn), T16 (missed the FX-over-limit, approved ₹30,240). Worse, its state went **negative** — ACC1 −₹25,000, ACC2 −₹5,240 — *impossible balances*, and the final summary was entirely wrong.
- **Sonnet 4.6 — 17/17, perfect**, including the strictly-after window logic on T16/T17 and all traps.
- **Opus — 17/17, and it self-corrected live.** Initially slipped on T9 and T16, visibly caught itself ("…wait"), reworked them, and landed correct.
- **Opus + Extended Thinking — 17/17**, cleanest and fastest, with the reasoning done up front.

> **The two best teaching moments:**
> 1. **Haiku's negative balances** — not just wrong codes but *impossible states*. Visceral proof of "don't hand complex money logic to the cheapest model."
> 2. **Opus catching its own errors mid-answer** — perfect lead-in to Extended Thinking: "when it reasons out loud it self-corrects; turn Extended Thinking on and it does that internally, before answering."

> Behaviour is probabilistic — a given model may do better or worse on the day. **That variance is itself the point:** for high-stakes payment logic, use a stronger model, make it show its reasoning, and **always verify**. If a model surprises you (e.g. Haiku aces it once), pivot to: "would you trust it on 50 transactions with no answer key? That's why we verify."
