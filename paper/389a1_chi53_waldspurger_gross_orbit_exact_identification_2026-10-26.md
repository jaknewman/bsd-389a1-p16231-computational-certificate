# 389a1, conductor-53 order-nine period: finite CM orbit => adelic toric period

Date: 2026-10-26. **Status:** source-level conditional theorem tying the user-run quaternionic Stage 8, 14, 22, 23, 29, and 30 statements to an authentic Waldspurger period. This document is a mathematical proof of the abstract bridge *when its exact integral and local intersection inputs hold*, rather than another numerical spot-check. It does not formalize the Sage code or independently rerun the archived original Stage 29 assertions.

## Setup

Take E=389a1, f_E in S_2(Gamma_0(389)), K=Q(sqrt(-3)), and O=O_53=Z+53 O_K. The discriminant of O is -3*53²=-8427. Let B/Q be the definite quaternion algebra ramified exactly at 389 and infinity, and R a maximal order (level 389). Sage's `BrandtModule(389)` classifies right-R ideal classes I_i, i=0,...,32. Their varying **left** orders R_i=O_left(I_i) are the orders holding the CM embeddings.

Write theta in O with theta²-theta+2107=0. An element q_i in R_i of trace 1 and norm 2107 defines iota_i:K->B via theta|->q_i. The **critical optimality requirement**, not merely q_i in R_i, is

`iota_i(K) intersect R_i = iota_i(O_53)`.

This is exactly what Stage 29's local-53 intersection computation says for the initial embedding, while its other-prime support control says all other local intersections are maximal. The initial embedding therefore defines an **authentic Gross point of conductor 53**, not a point of conductor one re-labelled as conductor 53. (The source Stage 29 output and proof must be included in any final externally reproducible appendix.)

## Lemma 1: the Sage right-ideal action is the ring-class action

Let [I_i,iota_i] represent an oriented optimal embedding. Let l=(19,theta-2) be the invertible O_53 prime ideal over 19. Because 19 is prime to 53*389 and splits in K, l has norm 19 and conjugate ideal lbar satisfying l*lbar=(19). Locally at 19, l corresponds to a primitive one-dimensional eigensummand for theta modulo 19, and the cyclic right-ideal neighbor is represented by

`J_i = R_i*(q_i-2) + 19*R_i` (a LEFT R_i-ideal).

It has Z-lattice index 19² and reduced norm 19, consistent with the local ideal l. The quaternion conjugate `conj(J_i)` is a left `right_order(J_i)` / right R_i lattice, so the product `conj(J_i)*I_i` represents the **inverse class action** of l on the (right ideal, oriented embedding) CM point. Its opposite root 18 represents the inverse transition. This is exactly the algebraic operation specified in Stage 14 and Stage 22, not an analogy with Hecke action.

For each k=0,...,17, the archived witnesses alpha_k satisfy **equalities of actual rational right ideals**,

`alpha_k * conj(J_k)*I_k = I_(k+1)`

and of embeddings

`alpha_k*q_k*alpha_k^(-1)=q_(k+1)`;

the inverse-root transitions also satisfy exact reverse identities. Consequently the 18 ordered oriented pairs represent the orbit of the genuine Pic(O_53)-action, with generator [l] or its inverse depending on the chosen action side. The orientation ambiguity replaces chi by chi^-1 and possibly rotates the starting point, and therefore **cannot change whether a character-weighted sum is zero**.

## Lemma 2: the 18 points exhaust the ring-class orbit

`h(O_53)=18` by the ring-class number formula (h(O_K)=1, 53 inert, unit index=3). Stage 8 independently gave class order([l])=18. Stage 14 returned 18 distinct oriented pairs and closed after the eighteenth transport; Stage 22 confirmed 18 actual ideal/embedding transitions. Thus, regardless of repeated **unoriented** ideal indices among the 33, these 18 oriented pairs are precisely the 18 Pic(O_53) points attached to the initial optimal embedding.

**Important:** Repeated Brandt class indices are permitted, since distinct oriented CM embeddings can map to the same quaternion ideal class. They must **not** be deduplicated in the toric sum.

## Lemma 3: evaluation of the genuine automorphic toric period

Stage 30 established that the 33-dimensional integral vector

`v=[0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0]`

is a simultaneous Hecke eigenvector matching E for primes through the weight-two Sturm bound 65, with a **one-dimensional** common eigenspace and the correct column/row convention. Thus its class-function realization phi on B^×\B_A,f^× / (A_Q,f^× Rhat^×) lies on the Jacquet–Langlands transfer of the newform f_E, up to a nonzero scalar. Stage 23 checked that the evaluated index convention coincides with the orbit and that all relevant mass weights equal one.

For the character chi9 of Pic(O_53) with chi9([l])=zeta9, the *actual global toric period* is

`T(phi,chi9)= integral_(K^× A_Q^× \ A_K^×) phi(iota(t)*g0)*chi9(t) dt`.

The local stabilizer of the chosen CM point in K_A,f^× is Q_A,f^×*Ohat_53^×, because the initial embedding is optimal. The class group quotient is Pic(O_53), finite of size 18. The integrand is right Rhat^×-invariant and chi9 is trivial on Ohat_53^×. All cosets have equal positive Haar measure. Therefore, for **one nonzero scalar C determined only by Haar conventions**,

`T(phi,chi9)= C * sum_(k=0)^17 v[index_k] * chi9([l])^(+/-k)`.

The sign ± records the harmless inverse-action convention. Changing the initial point multiplies the sum by a root of unity. A positive period normalization changes only C. Since the orbit's 18 evaluations are rational and v is real, the ± choices are Galois conjugate and vanish simultaneously.

This is an identity from the **definition** of Gross points and the quotient by the CM stabilizer; it is not an additional fitted normalization. In particular no conjectural local Waldspurger factor is inserted into the finite toric sum.

## Exact nonzero value

Stage 23 produced the ordered 18 evaluations:

`[0,0,-1,0,0,-1,-1,2,2,-1,-1,2,2,-1,-1,0,0,-1]`.

Their polynomial modulo X^9-1 is

`P(X)=-1-X+X²+2X³-X⁴-2X⁵-X⁶+2X⁷+X⁸`.

Exact cyclotomic arithmetic gives

`P(X) mod Phi9(X) = -3X^5-3X^4+3X^3-3X`

and

`Norm_Q(zeta9)/Q(P(zeta9))=Res(Phi9,P)=729=3^6 != 0`.

Consequently `T(phi,chi9) != 0` **under the exact optimality, class-action and Hecke eigenvector identifications of Lemmas 1–3**. Note that P(zeta3)=0: an auxiliary order-three character would NOT work.

## Global Waldspurger nonvanishing: local factors do not need individual evaluation

Waldspurger's theorem (for the transferred cuspidal representation of E on B^×) implies

`T(phi,chi9) != 0 => L(1/2, BC(pi_E) tensor chi9) != 0`,

equivalently the elliptic-curve normalization `L(E/K,chi9,1) != 0`. This is the **nonvanishing implication** in the theorem: the global identity relating |T|² to central L-value times local factors forces the central L-value nonzero whenever T is nonzero. One does **not** need a separate calculation of each local proportionality constant or nonzero local factor to deduce this direction. The actual global period identification in Lemma 3 is indispensable.

Thus the only finite-input conditionality is the faithful Sage/stage realization of the optimal embedding and its 18 class actions, not any still-unmeasured analytic local factor.

Since independently bounded exact-rational central-series arithmetic gives `9/2 < L(E^(-3),1) < 23/5`, the full Castella–Hsieh auxiliary complex product is nonzero when the preceding authenticated quaternionic input gates are accepted:

`L(E^(-3),1) * L(E/K,chi9,1) != 0`.

At p=16231 the order-nine auxiliary character is also p-regular; this unlocks the published rank-two generalized-Kato converse only under all its remaining explicitly stated ordinary/residual and local hypotheses, and still does **not** prove a uniform mod-p Sha vanishing theorem.

## Critical external-audit caveat and archival source

This paper is the *missing abstract adelic-identification argument*, not a formal verification of the original Sage Stage 8/14/22/23/29/30 machine executions. An outside reviewer must be able to inspect the complete Stage 29 local-53 intersection proof (R_i∩K=O53), exact Stage 22 quaternion ideal witnesses and Stage 30 Hecke eigenspace transcript; those are user-run and partially stored outside the current GitHub repository. Until those finite inputs are placed in the public repository, the claimed Rankin L nonvanishing remains a **conditional computer-assisted assertion** rather than an end-to-end independently reproducible certified result.

## Primary literature

- The authentic CM/Gross point class-group parametrization and toric periods: Chida–Hsieh, *Special values of anticyclotomic L-functions for modular forms*, https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf (Gross-point definition and explicit period equation).
- The nonvanishing implication in Waldspurger's formula: https://www.math.columbia.edu/~chaoli/doc/GanGrossPrasad.html
- Sage Brandt module's exact right-ideal/double-class conventions: https://doc.sagemath.org/html/en/reference/modfrm/sage/modular/quatalg/brandt.html
- [Previously archived period and twist](389a1_twist_minus3_exact_L1_and_chi53_order9_correction_2026-10-26.md).

## One-fraction replacement for the Stage 29 local-optimality gate

Here the maximal-order intersection statement can be certified without running another 53-adic Smith-normal-form pipeline. Given any of the archived actual quaternion embeddings `q_i` with `q_i²-q_i+2107=0`, set

`omega_i=(q_i-27)/53`. Then `omega_i²+omega_i+1=0`, hence the maximal quadratic integer ring is `O_K=Z[omega_i]` and the conductor-53 suborder is `O_53=Z[q_i]`. An order in K containing O_53 must have conductor dividing 53; since 53 is prime, the *only* possible overorders are O_53 itself and O_K. Therefore

`R_i intersect iota_i(K)=iota_i(O_53)  iff  omega_i notin R_i`.

Because the 33 Sage right ideal representatives' left orders are explicit rational quaternion lattices, `omega_i notin R_i` is equivalent to **at least one nonintegral coefficient** in its coordinates relative to an integral Z-basis of R_i; the denominators can only be 1 or 53. The new exact Sage script [chi53_optimal_embedding_one_fraction_criterion.py](../verification/chi53_optimal_embedding_one_fraction_criterion.py) performs this check on all 18 actual stage14 embeddings. It is **CODE READY, NOT EXECUTED** at the time of this addendum; its full PASS is the sole new calculation needed to replace reliance on the longer Stage 29 local argument in an externally auditable archive.

Once this gate passes, Lemmas 1–3, the already user-executed Stage 22 right-ideal identities, Stage 23 mass/eigenvector/orbit evaluation, and Stage 30 Sturm eigenspace check identify the actual toric integral at conductor 53 with a nonzero multiple of `P(zeta9)`. The global **one-direction** Waldspurger implication then gives nonzero Rankin central L-value **without** computing a list of local Waldspurger constants. The remaining risk is faithful execution/provenance and applicability of the cited automorphic theorem, not a missing infinite sum.

Do not mark this new optimality shortcut executed until the user provides the new Sage log.