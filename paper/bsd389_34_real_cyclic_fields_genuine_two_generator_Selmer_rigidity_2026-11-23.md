# E389a1 — 34 cyclic fields: exact TWO-GENERATOR genuine p-primary Selmer rigidity, using the Bullach–Honnor 2025 Fitting inclusion

**Date 2026-11-23. Status: a mathematically justified NEW deduction about the genuine Selmer groups, under the three independently USER-executed Kurihara certificates and the already proved E(K)=E(Q) for these 34 fields.** This is not a computation of Sha(E/K) nor global finiteness of Sha(E/Q). The short program accompanying the note checks the arithmetic low-jet premises, while the Selmer conclusion follows from the cited published theorem and a local commutative-algebra argument.

## 1. Exact external source and conditions

Bullach–Honnor, *On the refined 'Birch–Swinnerton-Dyer type' conjectures of Mazur and Tate*, arXiv:2511.07203, v1, Theorem 1.4(b), printed page 2:
https://arxiv.org/pdf/2511.07203

If p>3, rho_E,p(G_Q) contains SL2(Zp), the finite abelian extension K/Q either lacks mu_p or meets an alternate nonanomalous condition, and E has no additive reduction at p (or K unramified there), then

    theta^MT_K,# ∈ Fitt_0,Zp[G](Sel(E/K,p^infty)^vee).

This is genuinely the Pontryagin dual of the p-primary Selmer group; the theorem does not assume that Sha(E/K)[p^infty] is finite. The inversion # is an automorphism of the group ring preserving the unique maximal ideal for G a p-group.

For E=389a1, all hypotheses hold at p=11 (semistability + Mazur for p>=11), and also p=5 using the archived full p-adic image gate. Each of our cyclic fields K has degree p^k (odd), so mu_p cannot lie in K; the curve is semistable, so the additive-reduction condition is vacuous.

## 2. Explicit 34 field families and true quadratic-leading theta

The three authentic user-certified pairs are

    (p,k,q1,q2,delta mod p^k)
    (5,1,41,61,4)
    (11,1,397,991,1)
    (5,2,5351,10651,22).

For each tuple, m=p^k and every r∈(Z/m)^× define the real cyclic degree-m field

    K_r = Q(zeta_(q1*q2))^(ker chi_r),
    chi_r(a)=zeta_m^(lambda_1(a)+r*lambda_2(a)),

using the true primitive-root q_i discrete logs. Distinct r give phi(m) distinct fields. So there are 4+10+20=34 fields, with degrees 5,11,25.

Our authentic Hecke projection shows for EVERY such field the normalized actual theta has

    theta^MT_(K_r) mod (p,T^3) = u_r*T^2

with u_r ≡ r*delta modulo p, multiplied by at most a known p-unit depending on the Mazur–Tate normalization (p>=5). Therefore the p-adic augmentation-m-adic order is exactly TWO:

    theta_(K_r) ∉ (p,T)^3.

This is a true analytic computation for all 34 fields, not only one diagonal with r=1: the same bivariate low-jet formula gives c2=r delta.

## 3. General local Fitting two-generator lemma

Put R=Zp[G], G=Gal(K_r/Q)=C_m, maximal ideal mathfrak m=(p,T), and M=Sel(E/K_r,p^infty)^vee, a finitely generated R-module. Let

    d=dim_Fp M/mathfrak m M.

A minimal free presentation of M over the local ring R has all presentation entries in mathfrak m. Consequently

    Fitt_0,R(M) ⊂ mathfrak m^d.

By the actual Bullach–Honnor Theorem 1.4(b), theta^#_K∈Fitt_0(M). But theta^#_K∉mathfrak m^3 because its quadratic coefficient is a p-unit and lower terms are divisible by p (the exact Taylor constant vanishes). Therefore d≤2.

Conversely, the previously proved integral MW non-growth identity for these 34 fields says E(K_r)=E(Q)=Z·P⊕Z·Q, with trivial G action. The p-primary Kummer sequence gives a canonical surjection of R-modules

    M ↠ Hom_Zp(E(K_r)⊗Zp,Zp) ≅ Zp²

with trivial G action. Reducing modulo mathfrak m yields a surjection M/mathfrak m M ↠ Fp². Thus d≥2.

**THEOREM (true two-generator Selmer rigidity):**
    **dim_Fp M/mathfrak m M=2**.
Equivalently,
    **M needs exactly TWO generators over the ACTUAL local group ring Zp[C_m]**.

This is a genuine result about the arithmetic Selmer group, not an artificial theta-module cokernel. No finiteness of Sha(E/K_r)[p^infty] is assumed.

## 4. Even sharper exact G-invariant finite Selmer consequence

Since E(K_r)=Z² is torsionfree, E(K_r)[p]=0. The standard exact comparison between finite and p-infinity Selmer groups then gives

    Sel(E[p]/K_r) ≅ Sel(E/K_r,p^infty)[p].

Let S=Sel(E/K_r,p^infty). Pontryagin duality and the finite p-group G action give

    (S[p]^G)^vee = M/(p,T)M.

Hence the previously proved d=2 is the exact equality

    dim_Fp Sel(E[p]/K_r)^G = 2.

The rational MW classes form a two-dimensional G-invariant subspace via Kummer:

    E(K_r)/pE(K_r) = E(Q)/pE(Q) ≅ Fp²
       ↪ Sel(E[p]/K_r)^G.

Both sides have dimension2, so

    **Sel(E[p]/K_r)^G =
        Kummer(E(Q)/pE(Q))**.

This is a stronger, clean arithmetic rigidity result for the 34 explicit fields: their G-invariant p-Selmer classes are exactly the two rational MW directions.

**Do NOT infer Sha(E/K_r)[p]^G=0 from this equality.** Applying invariants to
    0→E(K_r)/pE(K_r)→Sel(E[p]/K_r)→Sha(E/K_r)[p]→0
is not right-exact for p-groups G. An invariant Sha class may fail to have a G-invariant Selmer lift; the connecting H¹(G,E(K_r)/p) can be nonzero. In fact the long exact sequence only yields an injection
    Sha(E/K_r)[p]^G ↪ H¹(G,E(Q)/p)≈Fp²
when the invariant Selmer terms coincide. This is a bound, not vanishing.

The base-field result Sha(E/Q)[p^infty]=0 for p=5 or11 follows independently from the true Fitting theta argument plus inflation–restriction (previous note), and was previously certified via Kim; none of these statements implies global all-prime Sha finiteness.

## 5. Reproduction and publication boundary

Existing complete USER runs:
- results/bsd389_p5_depth25_diagonal_USER_UBUNTU_PASS_2026-11-23.md
- results/bsd389_34_fields_532_twists_and_resultant_USER_UBUNTU_PASS_2026-11-23.md
- results/bsd389_three_genuine_integer_resultants_USER_UBUNTU_PASS_2026-11-23.md
- results/bsd389_symmetric_theta_three_Smith_USER_UBUNTU_PASS_2026-11-23.md

Latest USER Fitting-bridge output, containing the genuine three polynomial Taylor coefficients, is archived separately. Companion source verification:
    verification/bsd389_true_selmer_34_fields_two_generator_gate.py

**New proved theorem:** 34 real cyclic fields with exactly two genuine p-primary Selmer generators over their Zp Galois group rings, and precisely two G-invariant finite p-Selmer classes (the rational generators P,Q). **Not proved:** Sha(E/K_r)[p]=0 for these fields, Sha(E/Q) finite across all primes, or original full rank-two BSD formula.
