# Spec — Personal Loan EMI & Foreclosure

## Requirements
- EMI computed using reducing-balance method from principal, annual rate, and tenure (months).
- First EMI date is the 5th of the month following disbursement.
- Final installment adjusts for rounding so total repaid = principal + total interest.
- Interest accrual must be correct across leap years (use actual/365 or product rule as configured).
- Foreclosure allowed after 6 EMIs; foreclosure charge = 2% of **outstanding principal** (not original).
- Part-payment reduces outstanding principal and recomputes EMI or tenure per customer choice.
- All money values rounded to 2 decimals; no rupee should be lost or created across the schedule.
