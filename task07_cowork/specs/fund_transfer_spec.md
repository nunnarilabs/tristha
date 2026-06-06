# Spec — Own-Account Fund Transfer

Customers transfer funds between their own accounts via app/net-banking.

## Requirements
- Source & destination must belong to the logged-in customer.
- Block if available balance < amount.
- Enforce per-customer daily limit ₹5,00,000 (cumulative).
- Minimum ₹1; amount positive and numeric.
- Confirmation SMS on success.
- Log every transaction with timestamp + unique reference ID.
- Idempotency: same request twice within 10s must not double-debit.
