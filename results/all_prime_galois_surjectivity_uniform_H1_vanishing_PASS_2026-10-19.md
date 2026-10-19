# 389a1: all-prime residual surjectivity and uniform finite-image H¹-vanishing

**Date:** 2026-10-19. **Status:** an unconditional uniform theorem using Sage's *proved* non_surjective() specification and the user's successful SageMath 10.9 execution. Does **not** imply Sha(E/Q) finite or trivial.

## 1. Reproducible Sage output and precise API semantics

Researcher's actual log:

```text
BSD389_UNIFORM_MODP_EXCEPTION_SUPERSET []
BSD389_UNIFORM_MODP_SURJECTIVE_OUTSIDE_FINITE_SET_PASS
BOUNDARY: surjectivity does not imply Sha[p]=0
EXIT_STATUS=0
```

Invoked `E=EllipticCurve('389a1')`; `assert E.conductor()==389`; `assert not E.has_cm()`; `assert E.conductor().is_squarefree()`; `rho=E.galois_representation()`; `rho.non_surjective(A=1000)` yielded `[]`. No bound to prime indices: `A=1000` is a bound on the number of Frobenius traces used in a proof, **not** a bound on the primes to which the assertion applies.

The official Sage documentation explicitly states: **if a prime p is not in the list returned by non_surjective(), then its mod-p representation is provably surjective**. Therefore the empty result is a proved *all-prime* mathematical statement:

`For every prime l, Gal(Q(E[l])/Q) ≅ GL₂(F_l)`.

Primary source: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html

## 2. New uniform cohomological corollary

Let `V_l=E[l] ≅ F_l^2`, `L_l=Q(E[l])`, and `G_l=Gal(L_l/Q)=GL₂(F_l)`. Then

`H¹(G_l,V_l)=0` **for every prime l**.

### Proof for odd primes

For l odd, `z=-I` lies in the center of `G_l`. Let `c:G_l→V_l` be a 1-cocycle. Centrality and the cocycle identity give, for each `g∈G_l`,

`(z-1)c(g)=(g-1)c(z)`.

As `z-1=-2I` is invertible in `F_l`, put `v=(z-1)^{-1}c(z)`. Then `c(g)=(g-1)v`: every cocycle is a coboundary. Thus `H¹(G_l,V_l)=0`. This is the degree-one case of Sah's central-element lemma.

### Proof for l=2

`G_2=GL₂(F₂) ≅ S₃`. It has normal cyclic subgroup `C₃`, and the natural `F₂²` module `V₂` has `V₂^{C₃}=0` (an order-three matrix has irreducible polynomial `X²+X+1` over `F₂`). Since 3 is invertible in `F₂`, `H¹(C₃,V₂)=0`. Inflation–restriction for `C₃ ◁ S₃` gives

`0 → H¹(S₃/C₃,V₂^{C₃}) → H¹(S₃,V₂) → H¹(C₃,V₂)^{S₃/C₃}`,

both outside terms zero. So `H¹(G₂,V₂)=0` as well.

**Result:** exactly one theorem covers all primes, without enumerating them.

## 3. Why this DOES NOT show Sha[l]=0

Inflation–restriction for `1→G_{L_l}→G_Q→G_l→1` yields

`0→H¹(G_l,V_l)→H¹(G_Q,V_l)→H¹(G_{L_l},V_l)^{G_l}`.

Since the first H¹ is zero, restriction injects

`H¹(G_Q,V_l) ↪ Hom_cont(G_{L_l},V_l)^{G_l}`.

The right-hand side need not vanish. In particular, the Selmer group

`Sel_l(E/Q) ⊆ H¹(G_Q,V_l)`

can still contain classes arising from nontrivial `G_l`-equivariant homomorphisms from the Galois group of the division field. Local conditions matter.

The Kummer map sends the known free rank-two `E(Q)/lE(Q) ≅ F_l²` into the Selmer group. **To establish Sha[l]=0 uniformly, the missing theorem must prove there are no further locally admissible homomorphisms for all l outside a provably finite exceptional set**. Full residual image alone provides no such bound.

## 4. Recommended next proof obligation

Study the family of *everywhere locally restricted* modules

`Hom_{G_l}(G_{L_l},V_l)` subject to Selmer local conditions.

Seek a uniform higher-rank Euler/Kolyvagin-system or congruence theorem bounding the quotient by the two Kummer classes, with an **integer independent of l**. Merely replacing the Galois image by its full GL₂ at all primes does **not** furnish this integer.

This is meaningful provable progress in one hypothesis of potential higher-rank results, but **global Sha finiteness**, exact `#Sha`, and exact complex BSD leading-term formula remain OPEN.

## 5. Previously proved small-prime data (not uniformly extrapolated)

`Sha[l^∞]=0` proved for `l=2,3,5,7,11,13` using 2-/3-descent and Sage proved p-primary bounds. The 16231 result is a separate conditional computer-assisted p-adic certificate. Neither provides a uniform support bound.
