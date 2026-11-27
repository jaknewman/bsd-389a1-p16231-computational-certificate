# BSD 389a1 — research evidence intake (27 November 2026)

This directory archives evidence from the November 26–27 investigation **without changing the previously certified baseline**.

**STATUS: DRAFT / UNDER INDEPENDENT AUDIT. Full BSD is NOT proved.**

## What is stored

* `notes/`: preserved investigation notes. A note's title or assertion of “proof” is **not** independently validated by its inclusion here.
* `data/ordinary_p2_5_to_1999.csv`: reported exact modular-symbol coefficients for 297 good ordinary primes below 2000. Source computation was performed by in-session C++ and partially cross-checked with Python; preserve it as reported computations, not a theorem for all primes.
* `verification/bsd389_selmer3.m`: script for the full 3-Selmer calculation. Its output `#Sel_3=9` was **supplied by the user** in the conversation, not independently reproduced in this import.
* `verification/pfaffian_permutation_audit.py`: finite check demonstrating that an artificially antisymmetrized Kurihara matrix does not produce a canonical pfaffian.

## Strongest reported mathematical inputs

1. Curve: `[0,1,1,-2,0]`, conductor 389, proved MW rank 2, trivial rational torsion.
2. User's Magma execution reported `ThreeSelmerGroup(E)` invariants `[3,3]`; with a certified rank-two MW basis this implies `Sha(E/Q)[3^infinity]=0`.
3. Kurihara two-prime unit witnesses were calculated at selected primes; conclusions involving Kim's results require exact normalization and theorem-hypothesis auditing.
4. The 390-element integral modular-symbol table and p-adic cyclotomic jets were reported with reproducible scripts in the source archives. Correct comparison with the ordinary or multiplicative `p`-adic L-function **requires a separate normalization audit**.
5. In particular, the claimed implications `Sha[389^infinity]=0` and `Sha[p^infinity]=0` for all 297 ordinary primes below 2000 remain **under independent mathematical and software review** here. They are not promoted to established theorems by this import.

## Review gates before merging to main

- [ ] Reproduce the integral 390-edge table with Sage/eclib and confirm the Néron period normalization.
- [ ] Run and independently review the 3-Selmer transcript and the Magma version.
- [ ] Recompute at least a representative sample of each Kurihara batch and check Kim's precise definitions.
- [ ] Audit the tame-character projection and distribution/stabilization factors in the cyclotomic p-adic L-function.
- [ ] Verify the applicability and direction of all characteristic-ideal divisibilities (Kato/Wuthrich), and Greenberg's no-finite-submodule theorem.
- [ ] Reproduce and peer-review the p=389 exceptional-zero argument.
- [ ] Do not assert a proof of full BSD without an independent global argument and archimedean comparison.

The original program archives are not included in this first text/data intake; their SHA256 references are in `ARCHIVE_MANIFEST.md`. Import all source code/logs before merge.
