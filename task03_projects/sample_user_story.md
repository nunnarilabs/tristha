# Sample User Story — Fund Transfer (input for Task 3)

**Story (JIRA-style)**

*As a* retail banking customer
*I want to* transfer funds between my own accounts
*so that* I can move money without visiting a branch.

**Acceptance Criteria**
- AC-1: Source and destination accounts must both belong to the logged-in customer.
- AC-2: Transfer is blocked if the available balance is less than the transfer amount.
- AC-3: A per-customer daily transfer limit of ₹5,00,000 is enforced (cumulative across transfers).
- AC-4: Minimum transfer amount is ₹1; amounts must be positive and numeric.
- AC-5: On success, a confirmation SMS is sent to the registered mobile number.
- AC-6: Every transaction is logged with a timestamp and a unique reference ID.
- AC-7: The same request submitted twice within 10 seconds must not create two debits (idempotency).

**Notes**
- Channels: mobile app and net banking.
- Out of scope: third-party / external bank transfers (separate story).
