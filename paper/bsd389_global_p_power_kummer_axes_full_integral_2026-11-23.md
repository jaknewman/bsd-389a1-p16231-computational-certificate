# Uniform p^k-integral Kummer-axis selectors: density exactly p^{-3k}

**23 November 2026. New rigorous ALL-DEPTH theorem for the two rational MW generators of E=389a1.** This strengthens the full-mod-p-Selmer selector theorem by giving an **INVERTIBLE p^k-ADIC localization matrix**, not merely an invertible mod-p matrix. Applies at every p>=5 with full p-adic Galois image, hence all sufficiently large p for this non-CM curve. It does not assert a nonzero Kurihara two-prime derivative or full Sha finiteness.

## 1. Statement

E:y²+y=x³+x²−2x, with the saturated rational MW basis P=(-1,1), Q=(0,-1), rank2, torsion0. Let p>=5 with Gal(Q(E[p^k])/Q)=GL2(Z/p^k) for every k>=1, and fix a depth k>=1.

Then there are **two** infinite Chebotarev sets Q_P(p,k) and Q_Q(p,k), EACH of **exact natural density 1/p^(3k)**, such that every q in either set satisfies:

  q!=p,389; q≡1 modp^k; a_q(E)≡2 modp^k;
  E(Q_q)/p^k E(Q_q) ≅ Z/p^kZ (a cyclic group of full order p^k).

Moreover:
- for q in Q_P, loc_q(P) is a GENERATOR of this cyclic group and loc_q(Q)=0 modp^k;
- for q in Q_Q, loc_q(P)=0 modp^k and loc_q(Q) is a GENERATOR.

Choose distinct q_P∈Q_P and q_Q∈Q_Q. The resulting rational Mordell–Weil Kummer localization is

  E(Q)/p^k E(Q)=(Z/p^k)^2
   → E(Q_{q_P})/p^k ⊕ E(Q_{q_Q})/p^k=(Z/p^k)^2

and, after choosing the two local generators, has diagonal matrix diag(u,v) with u,v∈(Z/p^k)^×. Thus

  **det(localization) ∈ (Z/p^k)^×**,

and the two-prime local detector is an exact isomorphism on the saturated rational MW lattice **at arbitrary depth**, with no assumption on Sha.

For k=2, each axis set has natural density **1/p^6**; q_P,q_Q can be taken with both Kurihara local moduli divisible by p².

## 2. Full p^k-Kummer image over the p^k-division field

Set R=Z/p^kZ, T=E[p^k]≈R², V=E[p]≈Fp² and K_k=Q(T). Choose p^k-division points R_P,R_Q with p^k R_P=P and p^k R_Q=Q. Restriction of the global Kummer cocycles to G_{K_k} yields a continuous homomorphism

    c=(c_P,c_Q):G_{K_k} → T⊕T.

Its image H is an R-submodule of T² and stable under the natural G_k=GL2(R) action. We prove **H=T²**, without assuming any global Sha result.

The natural R-linear surjection T→V is multiplication by p^(k−1). Under this map, the p^k-Kummer cocycles c_P,c_Q map exactly to the ordinary mod-p Kummer cocycles of the rational P,Q (because p·(p^(k−1)R_P)=P).

As in the companion full-Selmer proof, Sah's lemma gives

    H¹(G_k,V)=0:

the central element 2I∈G_k acts by 2 on V, and (2−1)=1 is invertible. Restriction H¹(Q,V)→H¹(K_k,V) is therefore injective. Since P,Q are an integral MW basis, their mod-p Kummer classes are Fp-independent and remain so after restriction.

The joint mod-p restricted cocycle image Hbar⊂V² is a G_k-stable submodule. V is absolutely simple for GL2(Fp) and End_G(V)=Fp. Any proper submodule Hbar of V² has a nontrivial equivariant quotient onto V, yielding a nontrivial Fp-linear relation between the two restricted Kummer cocycles. This contradicts independence; hence

    Hbar = V².

But Hbar is also the image of H under T²→T²/pT²≈V². Therefore

    H + p T² = T².

Applying Nakayama over the local Artinian ring R to the finite module T²/H yields

    **H = T²**.

This proves the complete additive p^k-Kummer extension:

    1 → (E[p^k])² → Gal(L_k/Q) → GL2(R) → 1

where L_k=Q(E[p^k],p^(−k)P,p^(−k)Q), no splitting assumed. Note this argument is stronger than just H modp=V²: it establishes all p^k-precision translations.

## 3. Local algebra for Frobenius U at EXACT p^k precision

Fix U=[[1,1],[0,1]] over R. As proved in the preceding note, its centralizer in GL2(R) has cardinality

    |Cent(U)| = p^(2k−1)(p−1),

so the conjugacy class of U has density

    1/[p^(2k−1)(p−1)].

For good q with Frobenius A conjugate to U modulo p^k,

    det A ≡ q ≡1 (mod p^k),
    tr A ≡ a_q(E) ≡2 (mod p^k).

The unramified local cohomology and local Kummer quotient at q are

    E(Q_q)/p^k E(Q_q)
      ≅ H¹_unr(Q_q,T)
      ≅ T/(A−1)T
      ≅ R,

because (U−1)T=R·e1 and the quotient is the free line R·e2. Hence q has local p-power torsion with a cyclic quotient of **exact order p^k**, not just p-rank one.

Above fixed A in Gal(L_k/Q), every lift differs by an independently arbitrary vector of T², by §2. Under reduction to the two local cyclic quotients R⊕R these vectors give independent uniform coordinates.

An *axis-P unit event* is
    loc_q(P)∈R^×,  loc_q(Q)=0.
There are |R^×| = p^(k−1)(p−1) favorable quotient pairs among |R|²=p^(2k) possible pairs. The conditional frequency is

    p^(k−1)(p−1)/p^(2k)=(p−1)/p^(k+1).

Multiplying by the full U-conjugacy density gives

    1/[p^(2k−1)(p−1)] · (p−1)/p^(k+1)
      = **1/p^(3k)**.

The same proof holds for the axis-Q event. Each is invariant under Galois conjugation (unit vs zero is preserved by automorphisms of the cyclic local target). Chebotarev gives the **exact natural** densities.

The two sets are disjoint, each positive-density, so distinct q_P,q_Q can be chosen. They make the MW localization diagonal with unit diagonal entries mod p^k.

## 4. Comparison with the weaker full-Selmer mod-p theorem

The companion note \`paper/bsd389_global_deep_kummer_full_selmer_axis_density_2026-11-23.md\` proves an event of exact density p^{-(2k+s−1)} for ANY basis element of the *mod-p* full Selmer group, where s=dim Sel(E[p]). It detects all Sha classes but only measures the local images modulo p.

The present stronger theorem works for the **two rational MW generators** and gives unit/zero local conditions modulo p^k, at density p^{-3k}. It does NOT assume Sel(E[p^k]) is free over Z/p^k (this could fail if Sha[p^k] contributes cyclic groups of differing exponents).

The ordinary rank2 MW image is free over R because the basis is saturated globally; this is the exact hypothesis used in §2.

## 5. New exact p^k strict-Selmer description of Sha at TWO deep auxiliary primes

The two prime sets just proved give an integral identification at the WHOLE p^k torsion level, not only mod p.

Let S_k=Sel(Q,E[p^k]) and L_k=E(Q_{q_P})/p^k ⊕ E(Q_{q_Q})/p^k ≅ R², with q_P,q_Q chosen from the P/Q axis sets.

The Kummer exact sequence at p^k reads

    0 → E(Q)/p^kE(Q)≈R² → S_k → Sha(E/Q)[p^k] → 0.

Let λ:S_k→L_k be the pair of localizations. The previous theorem proves λ restricts to an **isomorphism** on the embedded MW quotient. Hence λ has an R-linear section arising from the MW basis, and

    S_k ≅ R² ⊕ ker(λ).

For any class x∈Sha[p^k], choose a lift \tilde x∈S_k, then subtract the UNIQUE rational MW class y∈R² whose localization equals λ(\tilde x). The difference \tilde x−y lies in ker λ and depends ONLY on x (different choices of lift differ by MW and cancel identically). This constructs a canonical isomorphism relative to the chosen q_P,q_Q:

    **Sha(E/Q)[p^k] ≅
       ker( Sel(Q,E[p^k]) →
            E(Q_{q_P})/p^k ⊕ E(Q_{q_Q})/p^k ).**

No finite-primary-Sha assumption is used.

This is a concrete uniform **two-deep-prime strict Selmer model**, at arbitrary integral precision. Its kernel need NOT vanish: an arbitrary hypothetical Sha[p^k] is faithfully retained. In particular, Poitou–Tate and the existence of these q's alone cannot force it to be zero. An additional authentic rank-two Euler-system/Kurihara reciprocity identity must annihilate this strict kernel.

## 6. Boundary and implication for the global BSD program

This proves that for every sufficiently large p, the putative high-depth Kurihara auxiliary primes can be chosen to have an **integral determinant-one type MW localization** modulo p^k for arbitrary k. Thus no hidden local \(p^k\)-denominator or failure of MW local saturation is an obstacle to constructing TWO good auxiliary primes.

**However:** the true Kurihara number \tildeδ_{q_Pq_Q} depends on weighted modular-symbol/Kato-derived global information. Its valuation is NOT determined by local MW localization. The theorem does NOT imply
    v_p(\tildeδ_{q_Pq_Q})<=1,
and does NOT prove Sha[p]=0 or global BSD. The missing step is a genuine integral global reciprocity/determinantal comparison relating a derived Euler-system class to this local MW determinant.

This distinction is essential: if Sha[p] has positive dimension, these same local MW selectors exist, and their joint localization kernel inside Sel(E[p]) is exactly the Sha[p] component after choosing the splitting; there is no contradiction.

**Published external inputs:** Serre open image theorem, Serre p-adic lifting for p>=5 (https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html), Sah central-element lemma (elementary proof above), and Chebotarev density theorem. All other finite group/Kummer linear algebra is written explicitly here. The companion verification script is \`verification/bsd389_global_p_power_kummer_axes_density_gate.py\`.

**Scope:** a theorem proving exact deep \`p^k\` local MW-axis saturation, NOT the all-p Sha annihilator or exact complex BSD.
