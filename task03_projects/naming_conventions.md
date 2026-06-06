# Test Artefact Naming Conventions (Tristha standard)

## Test Case IDs
`TC_<FEATURE>_<NNN>` — three-digit, zero-padded, sequential per feature.
- Feature codes: `FT` Fund Transfer · `CARD` Card payments · `UPI` UPI · `LOAN` Loans/EMI ·
  `LOGIN` Authentication · `STMT` Statements.
- Examples: `TC_FT_001`, `TC_CARD_014`, `TC_UPI_007`.

## Defect IDs
`DEF_<FEATURE>_<NNN>` — e.g. `DEF_FT_003`.

## Test data labels
`TD_<FEATURE>_<type>` where type is `valid` | `boundary` | `negative` — e.g. `TD_CARD_boundary`.

## Versions
Documents use semantic versioning `vMAJOR.MINOR` — e.g. test strategy `v1.0`, `v1.1`.
