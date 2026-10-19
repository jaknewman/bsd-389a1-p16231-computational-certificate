# Full BSD 389a1 — 2-primary Tate–Shafarevich triviality: PASS

**Date:** 2026-10-19. **Source:** user-provided terminal log, SageMath 10.9, IONOS Ubuntu. **Observed exit:** `EXIT_STATUS=0`.

## Original results

```text
MW_RANK 2
TORSION_ORDER 1
SELMER_2_PARI 2
SELMER_2_MWRANK 2
SHA_2_RANK 0
BSD389_SHA_2_PRIMARY_TRIVIAL_PASS
EXIT_STATUS=0
```

The two independently supplied 2-Selmer dimension computations agree (`pari` and `mwrank`) and coincide with the proven Mordell–Weil rank 2.

## Rigorous mathematical deduction

The standard Kummer sequence gives:

```text
0 → E(Q)/2E(Q) → Sel_2(E/Q) → Sha(E/Q)[2] → 0.
```

As `E(Q)` has rank 2 and trivial torsion, `E(Q)/2E(Q)` has dimension 2 over `F_2`. The 2-Selmer group also has dimension 2. Hence the final term has dimension zero: `Sha(E/Q)[2]=0`.

If a nonzero element had order `2^k`, multiplying by `2^(k-1)` would give a nonzero element of order 2, impossible. Thus

`Sha(389a1/Q)[2^infinity]=0`.

This exact algebraic conclusion does not depend on the p=16231 cyclotomic C01 computational bridge.

## Scope

The result eliminates the *entire 2-primary subgroup*, whether or not the full Tate–Shafarevich group is finite. It does not by itself exclude 3,5,7,... components, show finiteness of Sha, or prove the full BSD leading-coefficient identity.

Related: [Rigorous analytic rank-2 certificate](full_BSD_exact_analytic_rank2_PASS_2026-10-19.md); [Kato p=16231 arithmetic gate](kato389_sage10_9_terminal_pass_2026-10-19.md).
