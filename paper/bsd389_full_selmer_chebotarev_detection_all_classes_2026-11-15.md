# Full Selmer Chebotarev detection for E=389a1: positive density for every extra Sha[p] direction

**2026-11-15**. A genuine uniform-in-p Galois-cohomological theorem for ALL independent mod-p Selmer classes, not just the rational points P,Q. Does not prove Sha vanishing, uniform Sha finiteness or complex BSD.

## Setup and exact joint Kummer-image theorem

E/Q: y²+y=x³+x²−2x, with proved saturated E(Q)=Z P⊕Z Q, P=(-1,1),Q=(0,-1). Fix p≥5 with surjective ρ_{E,p}:G_Q→GL₂(Fp). Put V=E[p], F=Q(E[p]), Γ=GL₂(Fp), and S_p=Sel_p(E/Q), with finite Fp dimension m=2+dim_Fp Sha(E/Q)[p].

**Theorem 1.** For ANY Fp-linearly independent classes c₁,...,c_r in H¹(Q,V), the restrictions h_i to G_F define a finite Galois extension M/F with

**Gal(M/F)=V^r**,

and M/Q is Galois, with [M:F]=p^{2r}. In particular this applies to a BASIS OF THE ENTIRE p-SELmer group, including ANY extra Sha[p] lifts, with no Sha finiteness assumption.

**Proof.** The central element −I∈Γ acts as −1 on V, and p odd, so Sah's lemma gives H¹(Γ,V)=0. Inflation–restriction injects H¹(Q,V)→Hom(G_F,V)^Γ. The h_i are therefore Fp-linearly independent. Their joint image H⊆V^r is Γ-stable. The Γ-module V is absolutely irreducible with End_Γ(V)=Fp. The semisimple Γ-module V^r has the property that if H⊊V^r is proper, then a nonzero Γ-map V^r/H→V exists. Composing gives a nonzero Γ-hom V^r→V vanishing on H; by Schur this is ∑λ_i projection_i with λ_i∈Fp. Therefore ∑λ_i h_i=0, contradiction. Hence H=V^r. Γ-invariance makes M/Q Galois. QED.

## Exact local Chebotarev density and Sha-only detection

A nonidentity unipotent element g∈Γ has det(g)=1, tr(g)=2 and dim_Fp V/(g−1)V=1. There are exactly p²−1 such elements. Their rational prime density is (p²−1)/|GL₂(Fp)|=1/[p(p−1)]. For q∤389p with Frob_q of this type, the good local Kummer line E(Q_q)/p is identified with V/(g−1)V.

Over each lift of g in Gal(M/Q), the full translation kernel V^r varies the r Kummer local values independently over the r coordinates of (V/(g−1)V)^r≈Fp^r. This is uniform even if the full extension M/Q does NOT split over Γ. The simultaneous property "coordinate j nonzero and all other r−1 coordinates zero" is invariant under conjugation (nonzero scalar change of the common local line). Its conditional fraction is (p−1)/p^r. Chebotarev gives its EXACT ABSOLUTE prime density

**δ_{p,r,j}=(p−1)/p^r·1/[p(p−1)]=1/p^{r+1}.**

When Sha[p]≠0, choose r=3 with c₁=P,c₂=Q,c₃=s a lift of a nonzero Sha[p] class. There are infinitely many such q (density precisely **1/p⁴**) for which loc_q(P)=loc_q(Q)=0 but loc_q(s)≠0. These primes distinguish ANY individual extra Sha direction from MW, rather than annihilating it.

## The exact minimum number of one-dimensional auxiliary localization gates

Apply Theorem 1 to a BASIS c₁,...,c_m of S_p. For each j, Chebotarev permits a distinct prime q_j whose localization vanishes on all c_i except c_j, on which it is nonzero. The m×m full Selmer localization matrix at q₁,...,q_m is diagonal invertible, so
  Sel_p(E/Q) → ⊕_{j=1}^{m}E(Q_{q_j})/pE(Q_{q_j})
is an isomorphism. Conversely fewer than m one-dimensional target lines cannot contain an injective image of a dimension-m Fp space.

Defining N_p^det as the MINIMUM number of allowed nontrivial-unipotent good auxiliary primes whose localization map is injective on THE FULL Sel_p, we have the exact unconditional formula

**N_p^det=dim_Fp Sel_p(E/Q)=2+dim_Fp Sha(E/Q)[p].**

Serre's open image theorem for the non-CM E389a1 makes this valid at ALL sufficiently large p. This theorem is non-effective as to the least q_j and does NOT evaluate m without an independent computation of the full Selmer group.

## Experimental sanity audit (real finite GL₂ enumeration)

A dependency-free Python verifier enumerated ALL p⁴ matrices over Fp at p=5,7,11, found respectively p²−1=24,48,120 nonidentity unipotents, and enumerated r=2,3,4 quotient coordinate patterns. It confirms δ_{p,r}=1/p^{r+1} exactly by Fraction arithmetic. The exact assistant-executed source is:

verification/bsd389_full_selmer_frobenius_detection.py
SHA256 fa4f7c9b71683506d0d1f9d75eae85950eccf54f9e94b351d53761adc7df2741.

**Vital limitation.** Chebotarev can isolate Sha classes if they exist; the theorem does not FORCE Sha[p]=0, and does not yield the needed 2-factor **unit Kurihara derivative**. The minimal full Selmer localization count is NOT the minimum auxiliary degree of a nonzero Kolyvagin derivative. Conflating the two would assume the missing Euler-system primitivity. No new claims about the exact complex BSD coefficient.

This strengthens the earlier PR #16 two-MW-point version and PR #20 two-point joint Kummer image, without repeating their p-adic numeric gates.
