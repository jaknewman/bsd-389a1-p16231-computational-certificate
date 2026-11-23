# 389a1 — user Ubuntu/Sage validation of genuine Hecke norm and diagonal Kurihara theorem

**Date:** 23 November 2026. **Status:** successfully run by the user on Ubuntu with the `sage` Conda environment; this is not an assistant-only synthetic test.

Invocation:
```bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only
python -u verification/bsd389_authentic_Hecke_norm_and_diagonal_Kurihara_quadratic.py
```

User's complete relevant stdout:

```text
AUTHENTIC_HECKE_CONDUCTOR_NORM_BOTH_DIRECTIONS_PASS 5 41 61 crosslogs (4, 4) old_single_quadratic (0, 0) projected_degree_0_to_6 ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0])
AUTHENTIC_DIAGONAL_QUADRATIC_EQUALS_KURIHARA_PASS 5 41 61 delta 4 diagonal_choices {(1, 1): 4, (1, 2): 3, (2, 3): 4} raw_M33 3 elapsed_seconds 0.01
AUTHENTIC_HECKE_CONDUCTOR_NORM_BOTH_DIRECTIONS_PASS 11 397 991 crosslogs (5, 9) old_single_quadratic (9, 9) projected_degree_0_to_6 ([0, 0, 0, 0, 6, 1, 7], [0, 0, 0, 0, 8, 7, 6])
AUTHENTIC_DIAGONAL_QUADRATIC_EQUALS_KURIHARA_PASS 11 397 991 delta 1 diagonal_choices {(1, 1): 1, (1, 2): 2, (2, 3): 6} raw_M33 2 elapsed_seconds 2.1
ALL_REAL_ONE_VARIABLE_DIAGONAL_QUADRATIC_AND_HECKE_NORM_TESTS_PASS
BOUNDARY_NO_UNIFORM_NONVANISHING_OR_GLOBAL_SHA_FINITENESS
```

The source at commit `0c233a4` evaluates actual modular symbols for all needed a/(q1q2), via the historically independently checked 390-entry Néron-normalized integer Manin vector. It tests the two **authentic Hecke norm projections** degree by degree through six, and three diagonal cyclic-group quotients. Distinct p5 and p11 known original eclib anchor values are reproduced.

These tests independently confirm the arithmetic finite-level statement
`[T²] diag(theta_{q1 q2}) = delta_{q1q2} mod p`
for the two specified pairs. The abstract theorem proof is:
`paper/bsd389_real_Hecke_norm_diagonal_quadratic_Kurihara_theorem_2026-11-23.md`.

**Limit:** the verified finite diagonal theta depends on the auxiliary conductor; it is not the fixed cyclotomic p-adic L function. This data does not prove the quadratic coefficient nonzero for all sufficiently large p, nor Sha global finiteness or exact complex BSD.
