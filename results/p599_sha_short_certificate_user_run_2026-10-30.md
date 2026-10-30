# p599 short certificate: user-executed terminal transcript (2026-10-30)

> **Artifact mismatch uncovered after this transcript:** This was produced by the user's *local* `sha599_short_certificate.py` before synchronization; the local script was flagged as **DIVERGENT** from the one written to the GitHub repository. Treat the run as a local execution only. GitHub HEAD source reproduction is pending [issue #5](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/5). Do not infer that the current GitHub script has run successfully on Sage.

This transcript was provided by the user from their Sage environment on Ubuntu. It is recorded as **user-reported execution**, not a GitHub Actions run or an independent assistant execution on the same authentic data. The table is not checked into the repository.

```text
SHA599_SHORT_CERTIFICATE_START
LIFT_WEIGHT_IDENTITIES_PASS
MANIN_TABLE_SHA256 fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
P599_FINITE_PROGRESS 25000 / 179101 sec 0.2
P599_FINITE_PROGRESS 50000 / 179101 sec 0.37
P599_FINITE_PROGRESS 75000 / 179101 sec 0.54
P599_FINITE_PROGRESS 100000 / 179101 sec 0.7
P599_FINITE_PROGRESS 125000 / 179101 sec 0.86
P599_FINITE_PROGRESS 150000 / 179101 sec 1.02
P599_FINITE_PROGRESS 175000 / 179101 sec 1.21
P599_LEVEL_P2_INDEPENDENT_PASS C0 0 C1 0 C2 543 pairs 179101 edges 1924081 checksum 779927018
ANALYTIC_FROBENIUS_DERIVED F0_modp 571 F1_modp 0 kind HECKE_PLUS_PRECISION_LEMMA
PRECISION_NOTE alpha-adic O(alpha^-1): G_error in Zp, H_error in p^-1 Zp; Frobenius projection kills mod p
SAGE_ARITHMETIC_GATES_PASS rank 2 generators [(-1 : 1 : 1), (0 : -1 : 1)] surjective True regulator_0_modp 571 regulator_1_val 1
KATO_THEOREM_APPLICATION Stein-Wuthrich Algorithm 11.1; review mathematical note
BOUNDARY Does not execute p_primary_bound or compute the p^3 sum; theorem application depends on the stated exact algebraic lemmas
SHA599_SHORT_CERTIFICATE_FINISHED
```

## Interpretation

- FINITE LEVEL PASS: C2=543 modulo 599, independently corroborated by native C++.
- SAGE ARITHMETIC GATES PASS: certified rank, generators, surjectivity, regulator data.
- `ANALYTIC_FROBENIUS_DERIVED` is an algebraic reduction, **not an independent level p³ sum**.
- No direct `p_primary_bound(599)=0` output. The application to Sha[599^infinity] is **REVIEW-REQUIRED** pending the separate precision and theorem audit tracked in [Issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4).
