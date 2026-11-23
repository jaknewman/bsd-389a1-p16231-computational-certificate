# Published 5003-prime range and independently reconstructed p599 integer Manin moment — assistant execution

**Date:** 23 November 2026. This is an exact computational log summary, NOT a proof of an unverified analytic signed normalization or the full BSD identity.

## Finite prime range (using published Stein–Wuthrich Theorem 12.3)

Independent prime sieve in the assistant's runtime:

```text
PRIMES_5_LE_P_LT_48859 = 5022
EXCLUDED_SUPERSINGULAR_AND_BAD_AND_P16231 = 19
GOOD_ORDINARY_P_GE5_THEOREM_12_3_COVERED = 5003
PLUS_ARCHIVED_P107_CERTIFICATE = 5004
GOOD_PRIMES_NOT_YET_COVERED = 17
```

The published theorem itself is not rerun. It shows `Sha[p]=0` at all its covered primes; hence also `Sha[p∞]=0`.

## p599 independent 390 Manin reconstruction

The 390-entry source is the separate archived integer-Manin vector under `proof/p599-signed-main-conjecture-unit-closure-2026-11-15`, file `verification/bsd389_p599_independent_integral_390_moment_20261115.py`. The assistant independently fetched this source and used a **new JavaScript Euclidean continued-fraction accumulator**, not the original Python code, to visit the complete range `a=1,...,(599²−1)/2`, skipping nonunits. Direct reported output:

```json
{
  "source": "independent integral Manin vector 390 from user's repository branch",
  "input_length": 390,
  "half_representatives": 179101,
  "C0": 0,
  "C1": 0,
  "C2": 543,
  "seconds": 0.583,
  "independent_js_implementation": true,
  "signed_minus_mod_p": 28
}
```

The `28` is **only** the arithmetic scalar `-543/2 mod599`; confirming its identification with the actual Pollack `L^-_{599}` coefficient in the **same normalization as Burungale–Skinner–Tian–Wan Theorem 1.3** remains a separate required analytic/source audit.

An independent Python standard-library script with the full 390-digit source embedded is now committed as
`verification/bsd389_5003_ordinary_and_p599_integer_manin_gate_20261123.py`; it reconstructs the range and the p599 C2. Its arithmetic is validated by the JS execution, but the newly committed file itself has NOT been separately run on the user's Ubuntu machine.

Full precise theorem/normalization status:
`paper/bsd389_5003_ordinary_p599_signed_unit_reduction_2026-11-23.md`.

**No unconditional p599 Sha-vanishing claim at this stage. No p-uniform finite support or exact complex BSD.**
