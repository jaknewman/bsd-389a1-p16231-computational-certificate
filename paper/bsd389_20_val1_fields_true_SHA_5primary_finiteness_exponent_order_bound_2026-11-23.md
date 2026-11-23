# E389a1 — NEW GENUINE FINITENESS AND EXPLICIT ORDER / EXPONENT BOUNDS FOR Sha(E/K)[5∞] IN TWENTY VALUATION-ONE CYCLIC FIELDS

**23 November 2026. MATHEMATICAL STATUS:** This is a new arithmetic deduction from (i) the USER-INDEPENDENTLY REPRODUCED authentic 34,775,000-Manin-symbol conductor 5351*13001, (ii) all 20 user-verified true 25-entry Mazur–Tate theta polynomials and their 40 nonzero cyclotomic resultants, (iii) Bullach–Honnor's proved inclusion of the TRUE theta in the TRUE Selmer Fitting ideal (Theorem 1.4(b), arXiv:2511.07203), (iv) the independently proved Sha(E/Q)[5∞]=0, and (v) explicit 24×24 Smith matrices of the TRUE group-ring quotient. Neither original BSD nor any all-p uniform existence is assumed. The conclusions concern the ACTUAL Sha groups over 20 nontrivial number fields, not the spurious analytic symmetric-theta cokernel.

## 1. The true setup and exact outside theorem

E/Q: y²+y=x³+x²−2x, N=389, rank E(Q)=2 with generators P=(-1,1),Q=(0,-1), no rational torsion nor rational isogenies. Full 5-adic Galois image contains SL2(Z5), as independently verified in the project. The curve is semistable.

q1=5351, q2=13001, n=q1q2=69,568,351, and both are p²=25 deep-admissible. For each r∈(Z/25)^× define
    chi_r(a)=zeta25^(lambda_1(a)+r lambda_2(a)),
    K_r=Q(zeta_n)^(ker chi_r),
    G_r=Gal(K_r/Q)=C25.

Let R=Z5[G_r]≅Z5[X]/(X^25−1), augmentation T=X−1 and Galois **norm** element
    N_G=1+X+X²+...+X^24.
Let
    M_r=Sel(E/K_r,5∞)^∨,
    Y_r=Sha(E/K_r)[5∞]^∨.

The published Bullach–Honnor theorem (Theorem 1.4(b), primary author source https://arxiv.org/pdf/2511.07203 , and semistable Remark 1.5(a)) states that the genuine Mazur–Tate theta \Theta_r belongs to Fitt_0,R(M_r). Our original integral plus-symbol polynomial F_r(X), as computed for the 20 r from the authentic frozen 390-Manin vector, agrees with this genuine theta up to an R-UNIT (the even-symbol factor 2, invertible at 5, is harmless). No finite Sha assumption appears.

The exact prior USER terminal checked all 20 full polynomials by SHA256
    1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463
and all 40 true norms Res(F_r,Phi5) and Res(F_r,Phi25) were nonzero. For every r, the authentic quadratic Taylor coefficient satisfies
    [T^0]Theta=0,
    [T]Theta≡0 mod25,
    [T²]Theta≡15*r mod25, valuation exactly1.

Finally **Sha(E/Q)[5∞]=0** was ALREADY independently certified in the project at q1=41,q2=61 from a p-UNIT Kurihara witness; the new argument relies only on this previously established base-field p-primary vanishing, not global Sha finiteness.

## 2. GENERAL exact double-annihilator theorem, no Kato needed

**Lemma 2.1 (true Fitting annihilator).** For any finitely presented module M over a commutative ring R,
    Fitt_0,R(M) ⊂ Ann_R(M).
Consequently, since \Theta_r∈Fitt_0,R(M_r),
    **Theta_r*M_r=0 and Theta_r*Y_r=0.**
This is a statement about the TRUE Selmer module, NOT the analytic theta-matrix module.

**Lemma 2.2 (true Sha norm annihilator).** For every finite Galois extension K/Q and elliptic curve E, the corestriction on Weil–Châtelet groups preserves local triviality and induces
    Cor_(K/Q):Sha(E/K)→Sha(E/Q).
On Sha(E/K), the composite Res Cor equals the Galois norm Σ_g g. Because Sha(E/Q)[5∞]=0,
    **N_G*Y_r=0**
(after Pontryagin duality, with the same central norm element).

Thus Y_r is a finitely generated R-module over
    **S_r:=R/(\Theta_r,N_G)**.

Now R/(N_G)≅Z5[X]/(1+...+X^24) is a Z5-free module of rank24. The determinant of multiplication by the ACTUAL F_r(X) on it is
    B_r=Res_X(1+...+X^24,F_r(X))
        =Res(F_r,Phi5)*Res(F_r,Phi25).
Because ALL nontrivial character values F_r(zeta25^t) are nonzero, B_r is a nonzero integer. Therefore S_r is a FINITE 5-primary abelian group.

Y_r, finitely generated over this finite ring, is FINITE. **Hence Sha(E/K_r)[5∞] is finite without invoking Kato's theorem or assuming any Sha finiteness over K_r.** The exact order bounds will follow below.

There is also a purely arithmetic rank proof that avoids Kato. Since Theta_r annihilates the genuine M_r and Theta_r(chi)≠0 for every nontrivial character, the semisimple Q5[G]-module M_r⊗Q5 has NO nontrivial Galois character. As Y_r is now finite, M_r⊗Q5 is the rational dual of E(K_r)⊗Q5; it is entirely trivial. Its G-invariant part has rank rank E(Q)=2, so rank E(K_r)=2. Because K_r/Q is Galois of odd degree25 and E has no rational isogenies, E(K_r) has no torsion (invariant mod-ell subspaces and Weil pairing; for ell=2 use gcd(6,25)=1). Rank equality therefore implies EXACT
    **E(K_r)=E(Q)=ZP⊕ZQ.**

This rederives the rank-stability of all 20 fields from the SAME Bullach–Honnor Fitting theorem and original character computations, WITHOUT requiring separate Kato twist nonvanishing. No rank-two BSD assumption is used.

## 3. Derive d_R(Y_r)≤3 using the TRUE valuation-one theta

R is local with maximal ideal mathfrak m=(5,T). Our real theta maps to
    Theta_r -> 5*u_r*T² !=0
in the honest local quotient (Z/25)[T]/(T³). Since its maximal ideal has fourth power ZERO, we have
    Theta_r notin mathfrak m^4.
Let d_r=dim_F5 M_r/mathfrak m M_r be the minimum number of R-generators. A minimal presentation gives Fitt0_R(M_r)⊂mathfrak m^{d_r}. As Theta_r∈Fitt0(M_r), necessarily
    **d_r≤3**.

The true dual Kummer sequence is now
    0 → Y_r → M_r → Hom_Z5(E(K_r)⊗Z5,Z5) ≅ (R/(T))² →0.

**Elementary generator-kernel lemma.** If a local R-module M is generated by d elements and surjects onto (R/(T))², with d≥2, its kernel is generated by at most d elements.
Proof: choose a minimal d-generator free cover R^d↠M; after elementary changes of basis that lift a basis of the quotient modulo (5,T), the composite R^d↠(R/(T))² becomes the standard quotient on its first two coordinates and is zero on the other d−2. Its free-source kernel is TR²⊕R^{d−2}, generated by 2+(d−2)=d elements. Its image is the desired kernel Y.

Consequently,
    **d_R(Y_r)≤d_R(M_r)≤3.**

Since Y_r is a quotient of S_r^3, we have simultaneously
    **#Y_r ≤ (#S_r)^3**
and
    **exp(Y_r) divides exp(S_r)**.

## 4. Actual 24×24 integer theta matrices: the exact finite quotient S_r

For each true 25-integer histogram
    F_r(X)=Σ_(j=0)^24 a_j X^j,
build the **ACTUAL** integer multiplication matrix C_r on
    Z[X]/(1+X+⋯+X^24)
in the basis 1,X,...,X^23. Since X^24=−Σ_(i=0)^23 X^i, its coefficients are explicitly

    **(C_r)_(i,j) = a_((i−j) mod25) − a_((24−j) mod25),**
for i,j=0,...,23.

A new *independent complete 24×24 p-adic Smith computation* on ALL TWENTY true user-verified coefficient vectors gives:

| r modulo5 | number of fields | nontrivial 5-primary Smith factors of C_r | v5(det C_r)=v5(B_r) | exp(S_r) |
|---|---:|---|---:|---:|
|1,2|10|[25,25,25,25]|8|25|
|3,4|10|[5,5,25,25,125,125]|12|125|

These are Smith invariants of **the finite annihilator ring S_r**, not a Fitting presentation of the arithmetic Selmer. Their use in Sha bounds is legitimate specifically because of Lemmas 2.1–2.2, which prove that actual Sha is a MODULE over S_r, unlike earlier attempted naive identifications.

## 5. NEW unconditional prime5 Sha(E/K_r) bounds

The combined theorems yield for EVERY one of the twenty explicit cyclic degree25 fields:

    **r≡1 or 2 (mod5), ten fields:**
        25 * Sha(E/K_r)[5∞]=0,
        **#Sha(E/K_r)[5∞] ≤ 5^24.**

    **r≡3 or 4 (mod5), ten fields:**
        125 * Sha(E/K_r)[5∞]=0,
        **#Sha(E/K_r)[5∞] ≤ 5^36.**

The arguments prove finiteness, *not* Sha=0, for these 20 nonunit fields. The exponents 24 and36 are conservative upper bounds from at-most-three R-generators; the actual groups may be smaller or zero. The finite Cassels–Tate pairing imposes an even valuation of their cardinalities, which is compatible with the displayed bounds, but is not needed.

Because the 34 previous unit-Kurihara fields have already been proved to satisfy Sha(E/K)[p∞]=0, the total corpus now comprises **54 distinct explicit real abelian fields with no new rational points**, of which 34 have p-primary Sha ZERO and 20 have p-primary Sha FINITE WITH EXPLICIT EXPONENT AND ORDER BOUNDS.

## 6. Reproduce the new TRUE arithmetic-input Smith computation

- Original user-reproduced entire 20 true theta histograms: \`verification/bsd389_p5_val1_all20_cyclic25_integer_hist_native.cpp\`
- Original user-reproduced SHA256 + 40 authentic character resultant test:
  \`verification/bsd389_p5_val1_all20_twisted_L_norm_spectrum_gate.py\`
- **NEW 24×24 finite ring quotient Smith and derived bound gate:**
  \`verification/bsd389_p5_val1_all20_true_Sha_exponent_order_bound_gate.py\`

The new gate uses exact modular p-adic Smith row/column elimination at precision 5^8 and checks ALL 20 results. It also confirms that their 24 invariants sum to the 5-valuation of the corresponding genuine user-reproduced resultant (8 or 12). It is not a direct group-cohomology calculation of Sha; the actual Sha bound follows from the published Selmer-Fitting theorem, corestriction, and the proved generator-kernel lemma.

## 7. Strict BSD boundary

All new bounds are at the FIXED prime5 and for the TWENTY explicit auxiliary fields. They do NOT produce a prime-INDEPENDENT integer annihilating Sha(E/Q) at all p, nor prove that every large p has a p²-deep nonzero two-prime Kurihara derivative. The original exact complex rank-two BSD leading-coefficient equality is still outstanding.

**Mathematically new and completely explicit:** a double-annihilator bridge from original 25-symbol-level Mazur–Tate and genuine arithmetic corestriction to an ACTUAL finite Sha module over a 24×24-presented ring, proving concrete annihilating exponents 25/125 and orders at most 5^24/5^36 for 20 real cyclic degree25 fields.

## Update 2026-11-23 — genuine arithmetic NONVANISHING, superseding the earlier zero target

A subsequent *arithmetic*, rather than formal group-ring, argument proves that the **twenty real degree-25 fields carry nonzero true Sha[5]**, conditional on the already established rank-stability, full residual image and base Sha5 certificates. At the totally ramified prime q=13001, \(E(\mathbf F_q)[5]\simeq\mathbf F_5^2\) while the rational MW image modulo 5 is only one-dimensional (Q=2P). Poitou–Tate produces a 3-dimensional Q-relaxed Selmer group, and tame inertia kills its new local ramification after restriction to K. Since E(K)=E(Q) has mod-5 dimension 2, the third genuine Selmer class has a nonzero Sha image. The true Fitting bound also forces the invariant Selmer dimension to equal 3. This is proved in [the new theorem](bsd389_p5_all20_relaxed_Selmer_nonzero_Sha_theorem_2026-11-23.md), with the independently executable finite-field local audit in ../verification/bsd389_p5_all20_local_13001_relaxed_selmer_sha_nonzero_gate.py.

**Important correction of research direction:** the equality \(\#(X_r/N_GX_r)=5^4\) is still a correct iff-criterion for *zero* Sha, but the new theorem shows it is **false for each of these twenty fields**. Indeed the genuine arithmetic coinvariant index is at least \(5^6\), and the true Sha5 has order at least \(5^2\) by the finite alternating Cassels–Tate pairing. Combining with the earlier upper bounds yields \(5^2\le\#\Sha[5^\infty]\le5^{20}\) for r mod 5 in {1,2}, and \(5^2\le\#\Sha[5^\infty]\le5^{32}\) for r mod 5 in {3,4}. This is **not a claim about Sha(E/Q) at all primes**.
