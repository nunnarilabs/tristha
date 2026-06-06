# Spec — UPI Collect Request (stage this in Google Drive)

**Feature:** A payee raises a UPI **collect request**; the payer approves or declines.

## Requirements
- R1: Payee can raise a collect request to a valid VPA for an amount between ₹1 and ₹1,00,000.
- R2: The request must carry a note (max 50 characters) and an expiry (default 30 minutes, max 24 hours).
- R3: The payer receives a notification and can **approve** (with UPI PIN) or **decline**.
- R4: On approval, funds move from payer to payee and both get a confirmation with a UPI reference ID.
- R5: If the payer does not act before expiry, the request auto-expires and cannot be approved afterwards.
- R6: A payer can decline; the payee is notified with status "Declined".
- R7: Duplicate collect requests (same payer, payee, amount) within 60 seconds must be prevented.
- R8: Amount must be numeric and positive; reject invalid amounts.

## Notes
- Channel: UPI app.
- Security: approval requires UPI PIN; never log the PIN.
