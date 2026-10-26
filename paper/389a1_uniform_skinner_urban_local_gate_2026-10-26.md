# 389a1 — a uniform Skinner–Urban local gate, not uniform Sha vanishing

**Date:** 2026-10-26. This is a short mathematical deduction from the explicit Weierstrass equation and the version-pinned SageMath 10.9 `Sha.p_primary_order` criterion. No new large numerical computation or sampled regression is required.

## Exact local invariants

For `E: y²+y=x³+x²−2x`, take `(a1,a2,a3,a4,a6)=(0,1,1,-2,0)`. The standard Weierstrass quantities are

`b2=4, b4=-4, b6=1, b8=-3; c4=112, c6=-856; Delta_min=+389`.

**Important sign correction:** the discriminant is **positive +389**, not -389. This follows from `Delta=-b2² b8 -8 b4³ -27 b6² +9 b2 b4 b6=389`; an independent published Sage worked example for 389a records `factor(discriminant(E))=389` (William Stein, *Example: A curve of rank 2*, https://www.wstein.org/books/bsd/bsd/node30.html). The minimality follows because v_389(Delta)=1 (an integral Weierstrass change cannot lower the valuation by a positive multiple of 12), and v_389(c4)=0.

Thus E has multiplicative type I1 at 389. For its local Tate uniformization, `v_389(q_E)=v_389(Delta_min)=1` (true for split multiplicative over Q_389 and for the unramified splitting extension in the nonsplit case). The conductor is `N=389`, with 389 appearing to exact exponent 1.

## Uniform applicability proposition

**Proposition.** For every prime `ell>=5` with `ell != 389`, for which `E` has good ordinary reduction and the residual representation `rho_{E,ell}: Gal(Qbar/Q) -> GL2(F_ell)` is surjective, the extra local ramification hypothesis required by the Skinner–Urban branch of Sage 10.9 `E.sha().p_primary_order(ell)` is automatically satisfied.

**Proof.** In Sage 10.9 `src/sage/schemes/elliptic_curves/sha_tate.py`, the method first requires odd `ell`, `E.is_ordinary(ell)`, `N % ell != 0`, and `E.galois_representation().is_surjective(ell)`. It then loops over primes q with exponent one in the conductor and rejects the exact-order branch iff **all** such q satisfy `E.tate_curve(q).parameter().valuation() % ell == 0`. Here the set consists only of q=389 and its valuation is exactly 1. Since `1 % ell != 0`, the rejection condition is false at every eligible ell. The method proceeds directly to `self.p_primary_bound(ell)`; by Sage's documented Skinner–Urban criterion its returned exponent determines the exact ell-primary order. QED.

## What is and is not uniform

The **theorem applicability criterion** is uniform in ell. It reduces the good ordinary, residually-surjective ell-primary problem to evaluating the normalized leading term of the ell-adic L-function and regulator. **It does not imply `Sha[ell^infinity]=0` automatically**. It also does not cover supersingular ell, ell=389, or primes where the residual surjectivity hypothesis does not hold (and the odd-prime issue for ell=3 merits the separate Sage restrictions). Good ordinary primes need not be cofinite.

For the already numerically certified ell=16231, the two complete independent C01 global J sums, two complete n2 evaluations, two p-adic regulator algorithms, all exact Manin/Shapiro relations and six adversarial direct high-p Sage local moments yield the n3/regulator quotient a p-adic unit, conditional on the pinned analytic-bridge and source semantics. Therefore, under these verified gate assumptions, `p_primary_order(16231)=p_primary_bound(16231)=0` and `Sha(E/Q)[16231^infinity]=0` in the sense of a computer-assisted conditional finite-input theorem; neither Sage method has actually been run in its expensive full n3 implementation.

### Sources

- SageMath 10.9 source for `p_primary_order` and `p_primary_bound`: https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py
- William Stein's computation for this model, discriminant +389: https://www.wstein.org/books/bsd/bsd/node30.html
- [Minimal p=16231 primary proof and numerical dependencies](p16231_minimal_prime_primary_sha_certificate_2026-10-26.md).
