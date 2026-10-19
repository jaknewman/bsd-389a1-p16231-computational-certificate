# Exact Manin–Shapiro export certificate — 2026-10-19

**Input:** original data archive `bsd389_donnees_certification.tar.gz`; SHA-256 `7a6eed49fbe1ea12ace7838f3aabacb9dcbb3cf6394893296b906ac10736298c`.

## Frozen input fingerprints

- Relation export `bsd389_tame_relation_export_p16231.json`: `9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8` **PASS**
- Generator scalar values `bsd389_tame_scalar_values_p16231.json`: `7724c8d730a370e3fdc403293b9fc23f6adad632ca39b53d8439a96f18dd0c7e` **PASS**
- Independent verification source `verify_full_original_export.py`: SHA-256 `31621d69f04771071bcf894f7651157d588c08854c3f934817688d57f49584ff`.

## Mathematical identity established exactly

For every one of the 390 matrices `G_i` and each export relation `(e,A,r)`, the independent verifier checked **over exact rational cusp divisors**:

`[G_i infinity]-[G_i 0] = sum_(e,A,r) e ([A^(-1) G_r infinity]-[A^(-1) G_r 0])`.

All **390/390** relations pass, **zero nonzero cusp coefficients**, using `fractions.Fraction`, not modular or floating-point arithmetic. This also verifies the specific `A` lifts used by C01. Therefore the identities survive application of *every* Shapiro representative `r_j`, since a matrix acts on exact cusp divisors.

Additional independent tests:

| Check | Outcome |
|---|---|
| Projective keys `P¹(Z/389Z)` | 390/390 bijective and correctly indexed |
| Selected generators | 67/67 distinct, exact matrices match |
| Relations `(e,A,r)` | 2,012/2,012, `det(A)=1`, `A in Gamma0(389)`, `e=±1`, generator targets valid |
| Exceptional coset `R_inf` | determinant +1, expected entries |
| Max matrix entry absolute value | 2,723; signed `__int128` bound proved |
| Scalar Manin `S/U` laws | 780/780 PASS |
| Rank of standard Manin relations | 325/390 over both GF(101) and GF(16231) |
| New rank after adding all exported identities | 325; **zero extra rank** |
| Elliptic torsion directions | generator labels 22, 60; scalar values both 0 |

The 65-dimensional quotient is consistent with two elliptic 2-torsion labels among 67 chosen representatives; it is not 67 independent untwisted homology dimensions.

## Historical C++ engine comparison using real input, not synthetic data

Byte-identical TSV outputs for original pairwise `contrib()` versus aggregated `V11` on eight disjoint/representative intervals:

```text
[0,16) PASS 158 rows
[16,48) PASS 857 rows E1=1
[16000,16032) PASS 1078 rows E0=1 E1=44
[16230,16246) PASS 314 rows E0=1 E1=13
[263429114,263429130) PASS 303 rows
[0,512) PASS 13698 rows E0=14 E1=272
[130000000,130000512) PASS 17532 rows E0=27 E1=494
[263428618,263429130) PASS 13907 rows E0=39 E1=344
```

All intervals use the original `export.json`, SHA-pinned above. They are **bounded independent checks**, not an all-pairs second run.

## Consequence and precise boundary

The exact cusp-divisor equations, Hecke two-moment covariance `M0(hD)=M0(D)`, `M1(hD)=-AB M0(D)+A² M1(D)`, and C++ source branching establish the **algebraic identification of the V11 *source algorithm* with the mathematical functional `J_ref`**, for all pairs. This is no longer just a sampled claim about the 390 exported Manin relations. The historical chain audit separately passed for 263,429,130 pairs, 514,511 chunks and 4,019 checkpoints, final hash `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.

Remaining caveats: historic executable/binary ↔ full source provenance and trusted machine execution are **not formally proved** merely by source SHA hashes and checkpoint hashes. This record also does not independently rerun all chunk mathematics; the full terminal first-moment contraction has separate V65 evidence. The arithmetic conclusion on `Sha[16231^infinity]` still requires a justified application of the proved upper-bound theorem in rank 2. No claim of exact `u_p=1` or full BSD is made.

The two full input JSON files are preserved in the user-supplied archive; this record publishes their identities but **does not falsely claim their complete bytes are already committed into Git**.
