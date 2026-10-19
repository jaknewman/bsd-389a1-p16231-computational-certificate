# 389a1: p-primary Sha trivial for p = 5, 7, 11, 13 — PASS

Date: 2026-10-19. Researcher's actual terminal output on IONOS, SageMath 10.9, with `EXIT_STATUS=0`.

```text
SHA_PRIMARY_BOUND p=5 exponent=0
SHA_PRIMARY_BOUND p=7 exponent=0
SHA_PRIMARY_BOUND p=11 exponent=0
SHA_PRIMARY_BOUND p=13 exponent=0
BSD389_SHA_SMALL_PRIMES_TRIVIAL_PASS
EXIT_STATUS=0
```

## Theorem applied

SageMath `E.sha().p_primary_bound(p)` returns a **provable exponent e** satisfying `#Sha(E/Q)[p^infinity] <= p^e` when its documented hypotheses are satisfied. Rank 2 is supported for primes >3. All four calls succeeded and returned `e=0`. Hence, for this precise curve,

`Sha(389a1/Q)[p^infinity] = 0` for `p=5,7,11,13`.

This is separate from the independent 2-descent certificate `Sha[2^infinity]=0`, and the conditional computer-assisted `p=16231` certificate.

## Remaining limits and next work

The calculation does **not** establish `Sha(E/Q)=0`, its global finiteness, or exact complex BSD leading-term equality.

In Sage's current implementation the special `p=3` branch is restricted to rank 0; the present rank-2 curve is not eligible. A 3-Selmer computation could instead use Sage's `E.three_selmer_rank()`, documented as **optional Magma-only**; no availability of a Magma license should be assumed.

Do not infer global finiteness from separate p-primary finiteness proofs, even if achieved for every prime individually, without a uniform support bound or separate global theorem.

References:
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/sha_tate.html
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html
- [2-primary certificate](full_BSD_sha_2_primary_TRIVIAL_PASS_2026-10-19.md)
