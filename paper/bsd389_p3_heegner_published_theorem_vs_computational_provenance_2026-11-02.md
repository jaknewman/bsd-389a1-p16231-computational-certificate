# E389a1 at p=3 — rigorous implications and published Heegner provenance

**Date:** 2026-11-02. This is a source-critical ledger, not an independent recomputation of Kolyvagin derivative.

## Definitive arithmetic preflight

The user's Sage 10.9 `verification/bsd389_heegner_stein_p3_preflight.sage` execution passed (all printed gates and exit code 0), checking `E=389a1`, `N=389`, fundamental discriminant `D=-7`, `389` split in K, `c=41` and `ell=5` inert, `a_41=-3`, `3 | gcd(a_41,42)`, and `#E(F_5)=9`. See [authenticated transcript as user-provided text](../results/bsd389_heegner_p3_preflight_USER_PASS_2026-11-02.md).

## Published theorem / table

William Stein, *Heegner Points on Rank Two Elliptic Curves* (preliminary October 2009), <https://wstein.org/misc/sagedays18_papers/stein-heegner_points_on_rank_two_elliptic_curves.pdf>.

- Theorem 2.7 (printed page 5, PDF page index 4) says a nonzero local derived Heegner point `z_{c,sigma,ell}`, with MW rank exactly two and `q=p` prime, implies `Sha(E/Q)[p]=0`.
- Table 3.2 (printed page 9, PDF page index 8) row `389a1 | -7 | 3 | 5` lists `c=41,59,83,587` as examples with `z != 0`.
- Warning just before the table (printed page 7, PDF index 6) identifies nonrigorous pairs due to `p` dividing modular degree as `(389a1,5), (571b1,3), (655a1,3), (681c1,3), (997c1,3)`. The pair `(389a1,3)` is **not** listed.
- The paper states the residual `GL_2(F_p)` condition for its cases and assumes analytic rank two and analytic rank one of the appropriate quadratic twist. These need to be recorded when citing Theorem 2.7 as a formal deduction.

**Conditional source-based result:** accepting the correct computed nonzero class in Stein's table and all standing hypotheses, `Sha(E/Q)[3]=0`. For a p-primary torsion group, vanishing of p-torsion entails vanishing of the entire p-primary component, so `Sha(E/Q)[3^infinity]=0`. This step does not suppose global finiteness.

**Provenance caution:** this is NOT the user's independent full quaternionic derivative replay. Reproducing the class would require actual Brandt/Heegner/Kolyvagin operators and orientation normalizations, not just Kronecker symbols and point counts.

## Separate source and caution

Dimitar Jetchev, Kristin Lauter, William Stein, *Explicit Heegner points: Kolyvagin's conjecture and non-trivial elements in the Shafarevich-Tate group*, <https://wstein.org/papers/kolyconj/paper/jetchev-lauter-stein-kolyconj.pdf>. This work uses a different computational approach involving ring-class Heegner points. The authors explicitly note that the practical computations in its examples were **not made provably correct by a height-bound implementation** (Remark 2). Do not silently replace the specific 2009 Stein quaternionic table witness with computations from this different source and call them independently certified.

## Why generic Sage isn't the shortcut

The official Sage documentation `EllipticCurve('389a1').three_selmer_rank()` delegates to Magma (`optional: magma`), whereas `selmer_rank()` is the 2-Selmer rank. Thus without Magma or a new explicit 3-descent implementation, running stock Sage alone does not automatically produce an independently checked 3-Selmer certificate. The Sage `Sha.p_primary_bound(3)` documented rank-zero restriction excludes this rank-two curve.

## Global limit

Even if Sha[3∞]=0 is accepted and combined with Sage-certified Sha[p∞]=0 at p=5,7,11,13,107, these remain finitely many primes and do not prove uniform finite support of Sha or the complex BSD leading-term identity.
