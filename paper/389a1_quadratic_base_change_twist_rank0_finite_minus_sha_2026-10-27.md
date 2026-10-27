# 389a1: a genuinely uniform theorem for the anti-invariant Sha over K=Q(sqrt(-3))

**Date:** 2026-10-27. **Status:** mathematical consequence (rank-zero Kolyvagin + quadratic descent) of the project's independently checked exact-rational proof that `L(E^(-3),1)>9/2`. Proves a *uniform finite arithmetic defect only for the quadratic anti-invariant summand*, not finiteness of Sha(389a1/Q) nor global BSD.

## 1. Fixed setup and certified nonvanishing

Let `E: y²+y=x³+x²−2x` over Q, minimal discriminant +389, conductor 389, Mordell–Weil rank 2 and analytic rank 2. Put `d=-3`, `K=Q(sqrt(d))` with `G=Gal(K/Q)=<tau>`, and let `E^d` be the quadratic twist.

The exact-rational Dirichlet series code `verification/bsd389_twist_minus3_exact_rational_positive.py` computes the newform coefficients up to n=100 from Hasse point counts and the Hecke recurrences, applies the functional equation of the twist with conductor 3501 and sign +1, bounds each exponential with rational Taylor polynomials and the entire remainder with a provable Hasse tail. The resulting certified inequalities are

`9/2 < L(E^(-3),1) < 23/5`.

The assistant independently reimplemented and ran the exact same mathematical rational-interval algorithm locally in this turn, recovering the exact interval diagnostics `[4.524769101826934,4.574549787573269]` and verifying both rational endpoint inequalities. The original archived Sage auxiliary code is separate and is not needed for this rank-zero consequence.

Therefore the theorem of Kolyvagin for modular elliptic curves of analytic rank zero implies

`rank E^(-3)(Q)=0` and `Sha(E^(-3)/Q) is finite`.

## 2. The odd-primary quadratic Sha splitting (unconditional group theorem)

**Theorem.** For every **odd** rational prime ell, after choosing an identification `E^(-3)⊗K ≅ E⊗K`, there is an isomorphism of ell-primary groups

`Sha(E/K)[ell^infinity] ≅ Sha(E/Q)[ell^infinity] ⊕ Sha(E^(-3)/Q)[ell^infinity]`.

The first summand is the +1 eigenspace of tau, the second summand is the −1 eigenspace. The isomorphism is canonical up to the chosen quadratic twist identification, as is the G-action convention.

**Proof.** For each global and local Galois cohomology group, restriction and corestriction satisfy `cor∘res=[K:Q]=2`; similarly `res∘cor=1+tau` on the K-side. On ell-primary torsion with ell odd, multiplication by 2 is invertible. Thus restriction identifies the ell-primary part of H¹(Q,E) with the tau-invariants in H¹(K,E), and the same statement holds simultaneously for each local K_v/Q_v by Shapiro/inflation-restriction; the kernels/cokernels of descent are annihilated by 2. Since restriction and corestriction respect the local-triviality defining conditions, they induce an isomorphism on Sha ell-primary components. For the anti-invariants use the quadratic twist identification E^(-3)(K)≅E(K) carrying the downstairs Galois descent action to the negative eigenspace. The direct sum is given by idempotents `e_±=(1±tau)/2` acting on ell-primary torsion. QED.

**Corollary.** For all odd ell,

`Sha(E/K)[ell^infinity]^(-) ≅ Sha(E^(-3)/Q)[ell^infinity]`,

and every such minus component is finite. Since `Sha(E^(-3)/Q)` is itself finite, there is a **single fixed nonzero integer**

`D_- = #Sha(E^(-3)/Q)`

such that for every odd ell, its anti-invariant Pontryagin dual `X_{ell,-}` satisfies

`D_- ∈ Fitt_{0,Z_ell}(X_{ell,-})`.

In particular, `Sha(E/K)[ell^infinity]^(-)=0` for every odd `ell ∤ D_-`. This is a **genuine existential uniform Fitting integer for the minus component**—a proof of its existence, albeit not an explicit numerical computation of D_-.

The **plus component** is precisely `Sha(E/Q)[ell^infinity]`. No divisibility or annihilator relation from `D_-` to that plus component has been proved, and none follows merely from the quadratic decomposition. It is therefore **incorrect** to use `D_-`, the period norm 729, or the nonzero ring-class Rankin value to conclude that Sha(E/Q) is finite.

## 3. Selmer coranks and local extension evidence

Since rank E^(-3)(Q)=0, the standard quadratic Mordell–Weil decomposition over Q for odd ell gives

`E(K) ⊗ Z_ell ≅ (E(Q)⊗Z_ell)^(+) ⊕ (E^(-3)(Q)⊗Z_ell)^(-)`

as G-eigenspaces, so rank E(K)=2. The anti-invariant rational p-Selmer space for E/K has dimension 0, while the plus eigenspace has dimension `2+corank_Zp Sha(E/Q)[p^infinity]`. The rank-two obstruction is therefore **entirely in the plus eigenspace** for each odd p.

The central *ring-class* twisted value `L(E/K,chi9,1) !=0`, conditionally inferred from the quaternionic Gross orbit and Waldspurger, is a different Rankin L-function from the **trivial-character** base-change L(E/K,s)=L(E,s)L(E^(-3),s). The latter has analytic order 2, not 0, because L(E,s) has order 2 and the twist has order 0. Thus one cannot invoke rank-zero Kolyvagin on E/K merely because an order-nine auxiliary Rankin value is nonzero.

## 4. Exact implication for the search for an all-prime Fitting integer

We have produced by a *proved rank-zero theorem* an existential integer D_- bounding all odd anti-invariant finite Sha defects. The missing all-prime integer D_+ is equivalent to finiteness of the original Sha(E/Q) at all primes (see the project's equivalence note). The quadratic twist construction does not descend that plus-side bound. A genuine rank-two integral Euler-system/Fitting comparison theorem for the plus part remains to be supplied.

**Status:** ✓ odd-primary quadratic decomposition proved; ✓ rank-zero twist Sha finiteness follows from exact positive L-value and Kolyvagin; ✓ existential uniform D_- for anti-invariant Sha; ✗ no uniform D_+; ✗ no new proof of global Sha(E/Q) finiteness or BSD.

## Sources

- User project exact-rational positivity verifier: [verification/bsd389_twist_minus3_exact_rational_positive.py](../verification/bsd389_twist_minus3_exact_rational_positive.py).
- Sage documented rank-zero Kolyvagin and Sha finiteness: https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html
- Galois restriction-corestriction, quadratic twisting and Shapiro's lemma: standard Serre *Galois Cohomology*, Chapters I–II.
- [All-prime uniform Fitting integer equivalence and its limits](389a1_uniform_integer_fitting_equivalent_to_sha_finiteness_2026-10-26.md).
- [Original rank-two order-nine Gross nonvanishing analysis](389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md).
