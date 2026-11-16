# E389a1 — exact full-Selmer Chebotarev density and strict-Sha isolation

Date: 2026-11-16. Status: conditional elementary theorem; independent exact local p=5 arithmetic. This document neither proves global Sha finiteness nor the archimedean BSD leading-term identity.

## 1. Theorem (exact prescribed-selector density)

Let E/Q be an elliptic curve, p>=5 a good prime with Gal(Q(E[p])/Q)=GL_2(F_p). Let S=Sel(E[p]/Q), dimension s, and choose an F_p-basis c_1,...,c_s. For each index i there is a Chebotarev set of good primes q distinct from p with:

- q=1 (mod p), a_q(E)=2 (mod p);
- E(F_q)/pE(F_q) has F_p-dimension 1;
- localization of c_j at q is zero for every j != i;
- localization of c_i at q is nonzero.

**The natural density of this entire Frobenius selection event is exactly 1/p^(s+1).**

Here "entire" means the conjugacy-invariant event defined by the zero/nonzero pattern, NOT a single specified scalar in an arbitrarily fixed local quotient. In particular for s=2 the exact density is 1/p^3, not a universal 1/p^4. For s=2+t it is 1/p^(3+t).

### Proof

Put V=E[p] and K=Q(E[p]). Sah's lemma with central scalar 2I gives H^1(GL_2(F_p),V)=0. Restriction of an F_p-basis of S to G_K is therefore linearly independent in Hom(G_K,V). The image U of the combined homomorphism G_K -> V^s is GL_2(F_p)-stable. As V is absolutely irreducible and End_GL2(V)=F_p, every proper submodule of V^s admits a nonzero GL_2-equivariant projection V^s -> V annihilating it. That would give a linear relation among the restricted cocycles. Hence U=V^s.

Let L/K be the resulting Galois extension. The exact sequence
1 -> V^s -> Gal(L/Q) -> GL_2(F_p) -> 1
suffices: a splitting is NOT needed for this proof. Every fiber above a fixed A in GL_2 has exactly p^(2s) elements, and the V^s-kernel moves the cocycle values by arbitrary translations.

For any nonidentity unipotent A in GL_2(F_p), W_A=V/(A-I)V is 1-dimensional. At unramified good primes with Frobenius projection A, H^1_unr(Q_q,V) is W_A, and the localization of each c_j is its translation coordinate in this quotient. The map V^s -> W_A^s is surjective with all fibers of cardinality p^s, so precisely (p-1)*p^s elements above each A realize the motif (0,...,0,nonzero,0,...,0) with sole nonzero coordinate i.

There are p^2-1 nonidentity unipotents, and
|GL_2(F_p)|=(p^2-1)*p*(p-1).
The event is conjugacy-invariant (simultaneous change of quotient basis preserves its zero pattern), hence Chebotarev applies. Its density is

  ((p^2-1)*(p-1)*p^s) / (|GL_2(F_p)|*p^(2s))
    = 1/p^(s+1).

For these A, det(A)=1 and tr(A)=2. Thus q=1 mod p, a_q=2 mod p, and dim W_A=1 as required. QED.

## 2. Application to rank-two E389a1: exact isolation of the strict kernel

Assume E(Q)=Z P + Z Q, torsion=0, and choose distinct p-admissible q_1,q_2 such that the 2x2 MW localization matrix is invertible. Then the Kummer exact sequence and local linear algebra give

  Sel(E[p]/Q) = <P,Q>_(F_p) ⊕ K_p,
  K_p=ker(loc_q1 ⊕ loc_q2) ≅ Sha(E/Q)[p].

Set t=dim_Fp K_p and s=2+t. Pick a basis c_1,...,c_t of K_p and apply the preceding theorem with basis (P,Q,c_1,...,c_t). For each i we obtain auxiliary r_i with loc_{r_i}(P)=loc_{r_i}(Q)=0, loc_{r_i}(c_i) !=0 and loc_{r_i}(c_j)=0 (j!=i). Over suitable one-dimensional local target bases, localization at q_1,q_2,r_1,...,r_t is the block matrix diag(A_MW,I_t). It is invertible.

This gives a quantitative isolation theorem for *every* hypothetical Sha[p] basis, without assuming Sha[p]=0.

**Sharp boundary:** It does NOT eliminate any of those classes. A Kato/Euler-system reciprocity identity or independent strict-Selmer calculation must impose an additional global vanishing equation. Merely producing positive-density detecting primes, or an invertible MW 2x2 matrix, cannot yield the desired all-p triviality.

## 3. Independent concrete E389a1 witness at p=5

Use E:y^2+y=x^3+x^2-2x, P=(-1,1), Q=(0,-1). Direct exact group computations at two good primes give:

- q=61: #E(F_61)=70, a_61=-8, (70/5)P=(51,21) != O, (70/5)Q=O.
- q=251: #E(F_251)=230, a_251=22, (230/5)P=O, (230/5)Q=(62,95) != O.

Both q are 1 mod 5 and 5 exactly divides each group order. Consequently E(F_q)/5 is 1-dimensional at each prime. The MW localization matrix on the ordered primes (61,251) and basis (P,Q) is *diagonal with nonzero diagonal entries* after choosing local generators.

This only witnesses MW separation, not Sha[5]-triviality (already separately certified in earlier research). The exact program is verification/bsd389_full_selmer_chebotarev_density_and_p5_axis_gate.py.

## 4. Exact obstruction remaining

To turn this into an annihilation theorem, a new GLOBAL constraint on K_p is required. No global annihilator is constructed by this density calculation. Specifically neither the count 1/p^(s+1) nor the existence of q_1,q_2,r_i implies s=2. The effect of the selector theorem is to rule out the weaker explanation that possible Sha classes are undetectable by admissible prime localizations.

Previous underpinning: paper/bsd389_strict_selmer_chebotarev_detection_and_norm_projection_no_go_2026-11-05.md.
