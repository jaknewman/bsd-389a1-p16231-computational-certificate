# BSD 389a1 — A concrete obstruction to naive pointwise MW-Kurihara reciprocity (8 November 2026)

**Scope:** Exact independent finite-field computation with a *pre-existing archived* Sage-normalized Kurihara zero. This rules out a broad pointwise inference from independence of local MW reductions to nonzero Kurihara values. The pair under discussion is NOT a pair of two nonidentity-unipotent Frobenius primes, so the narrower conjectural comparison remains UNTESTED.

## Fixed input and audited pair

E/Q: y²+y=x³+x²−2x, P=(-1,1), Q=(0,-1), p=7. The earlier Sage/eclib script `verification/bsd389_kurihara_hecke_dual_p7_regression.py`, independently checked in the project archive, records

    δ_(113*281) ≡ 0 (mod 7);
    δ_(113*673) ≡ 2 (mod 7).

These Kurihara values are **archived evidence, not recomputed in this check**. The two pairs are p-admissible in the sense of modular-symbol/Kurihara congruences.

The new standalone standard-library Python script `verification/bsd389_global_p7_q281_local_countertest_2026_11_08.py` independently enumerates the entire E(F_q) for q=113,281, calculates the group law and multiplication by 7, and tests all 49 combinations of the reductions of P,Q.

Results:

| q | a_q | #E(F_q) | #E(F_q)[7] | dim_F7 E(F_q)/7 |
|---|---:|---:|---:|---:|
| 113 | 9 | 105 | 7 | 1 |
| 281 | -12 | 294 | 49 | 2 |

Both q≡1 mod7 and a_q≡2≡q+1 mod7. For q=113, the local images of P,Q satisfy Q=3P in E(F_113)/7. For q=281, the [7]-multiple subgroup has exactly 6 elements. Exhaustively:

    aP+bQ ∈ 7E(F_281), for 0<=a,b<=6
      if and only if (a,b)=(0,0).

Therefore the exact reduction map

    span_F7(P,Q) --> E(F_281)/7E(F_281)

is an isomorphism of 2-dimensional F7-vector spaces. In particular a *single* 7-admissible auxiliary prime already separates both rational generators, even though the archived associated **two-prime** Kurihara number δ_(113*281) is zero.

### Exact logical consequence

The following broad assertion is FALSE for E389a1:

> For every Kurihara-admissible pair (q1,q2), if the combined local images of the two rational MW generators are independent, then δ_(q1q2) is a unit modulo p.

Witness (p,q1,q2)=(7,113,281): local independence holds (at q2 alone!), while δ=0 (from archival full-sum Sage/eclib certificate).

This is not merely a toy linear-algebra example; it is the actual arithmetic of E=389a1. But it is **NOT** a counterexample to the narrower statement for pairs with **both** mod-p Frobenius nonidentity unipotent and 1-dimensional local spaces: the q=281 Frobenius is the **IDENTITY** on E[7], as certified by #E(F_281)[7]=49. Thus this counter-test does not rule out *all* conceivable specially selected pairs or a more sophisticated Kato-derived reciprocity theorem.

The density of Frobenius identity among unipotent admissible matrices is only 1/p², making the distinction essential rather than cosmetic.

### Why the missing global reciprocity is substantive

Kummer detects the two rational-point directions in the finite local Selmer spaces, while Kurihara δ is a weighted global modular-symbol derivative of a cyclotomic zeta class. A nonzero local determinant is not, by itself, a nonzero value of the latter weighted sum. The archived zero and nonzero p7 pairs demonstrate the distinction.

Moreover, the finite local Bloch–Kato/Kummer condition at good q≠p is isotropic under the local Tate pairing: unramified classes pair trivially with one another. Any meaningful Euler-system reciprocity must therefore involve **singular/transverse** local classes or global derived zeta elements, not solely a pairing of the two rational-point finite localizations.

### Next genuinely open gate

For pairs with both mod-p Frobenii **nonidentity unipotent** and an invertible 2x2 rational-point localization matrix, determine whether any properly normalized Kato derivative can give a *unit* Kurihara value. One would need an independent integral finite-singular comparison that also controls the strict Selmer group, not just the MW subspace. Without this, neither Sha(E)[p]=0 uniformly nor full rank-two complex BSD follows.

## Audit status

- New finite-field E(F_113), E(F_281), 7-torsion and all-49-combination computations: independently EXECUTED, all PASS.
- δ_(113*281)=0, δ_(113*673)=2: **REUSED archived** authentic modular-symbol regression; not reproduced with Sage in this new run.
- Global all-p Sha support and exact complex BSD leading-term equality: **OPEN**.
