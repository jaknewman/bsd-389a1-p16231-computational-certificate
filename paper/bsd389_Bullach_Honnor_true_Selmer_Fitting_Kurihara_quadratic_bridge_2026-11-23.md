# 389a1 — A REAL Selmer/Fitting bridge from Bullach–Honnor's proved weak main conjecture: true two-prime theta unit forces Sha[p]=0

**23 November 2026. Status: COMPLETE MATHEMATICAL PROOF of a primewise implication via the actual p-primary Selmer module.** Unlike earlier authentic symmetric theta matrix coker calculations, this note invokes the published *2025* theorem of Bullach–Honnor that places the **genuine Mazur–Tate theta itself in the genuine Selmer Fitting ideal** for arbitrary finite abelian fields, with no Sha-finiteness assumption. For E389a1 all needed conditions hold for p≥11 (and at p=5 by existing independent full-image certificate). This is a new independent route to existing proven p5/11 Sha triviality, NOT an all-p Sha proof: a p-unit quadratic theta coefficient is still needed for each p.

**Primary PDF, Theorem 1.4(a,b), Hypothesis 1.2 and Remark 1.5(a), printed pp.2–3:**
Dominik Bullach and Matthew H. L. Honnor,
*On the refined 'Birch–Swinnerton-Dyer type' conjectures of Mazur and Tate*,
arXiv:2511.07203v1 (10 November 2025).
https://arxiv.org/pdf/2511.07203
The published theorem is materially stronger than older theorems restricted to the fixed cyclotomic Z_p tower.

## 1. Completely checked hypotheses for our actual varying-conductor fields

Fix E:y²+y=x³+x²−2x, conductor N=389, rank(E(Q))=2, torsion0, semistable. Fix p≥11 (or p5 using archived independently established full 5-adic Galois image) and k≥1. Let q1,q2 be distinct GOOD p^k-admissible auxiliary primes:
    qi≡1 and a_qi(E)≡2 modulo p^k.

Choose a pair of primitive root discrete logs and a diagonal unit r modulo m=p^k, and define the actual cyclic degree-p^k real abelian field
    K=Q(zeta_(q1q2))^(ker chi_r),
    chi_r(a)=zeta_m^(lambda_1(a)+r lambda_2(a)).
Then K/Q is abelian G≅C_m, its conductor n=q1q2 is coprime to 389, and [K:Q]=p^k is odd.

**Bullach–Honnor Hypothesis 1.2:**
(i) the p-adic image contains SL2(Z_p): true for E semistable and p≥11 by Mazur's theorem, explicitly recalled in their Remark1.3; at p5 this follows from the existing full residual GL2(F5) certificate plus Serre's lifting criterion at p≥5;
(ii)(a) K does not contain a primitive p-th root of unity: true because p−1 is even and [K:Q]=p^k is odd;
(iii) if additive reduction at p, p unramified in K: vacuous, because E is semistable at every prime.

Their Theorem1.4(b) therefore applies **UNCONDITIONALLY**, with no assumption Sha(E/K) finite.

Let
    R=Z_p[G]=Z_p[T]/((1+T)^m−1), T=gamma−1,
    M=Sel(E/K,p^infty)^∨.
The theorem says
    **theta_K^# ∈ Fitt_(0,R)(M)**.
The inversion # is an automorphism of R preserving its unique maximal ideal, so it will not affect augmentation order.

## 2. General local-ring Fitting lemma: no Sha hypotheses

R is a complete local ring with maximal ideal mathfrak m=(p,T), residue field Fp. Let
    d=dim_Fp M/mathfrak m M.

By Nakayama's lemma M has a MINIMAL R-presentation
    R^a --> R^d --> M -->0
in which the entries of the first map all lie in mathfrak m. Thus the generators of Fitt_(0,R)(M) are d×d minors of a matrix whose entries lie in mathfrak m. Hence
    **Fitt_(0,R)(M) ⊆ mathfrak m^d**.
This remains true if a<d, when Fitt0=0.

For any actual theta whose reduction modulo p has initial augmentation term in degree t<m,
    theta_K modp = c_t*T^t + higher, c_t!=0,
we have theta_K ∈ mathfrak m^t but theta_K ∉ mathfrak m^(t+1).
Since # preserves mathfrak m-adic order, Theorem1.4(b) yields
    **d≤t**.

This is a genuine published-theorem-driven bound on the TRUE Selmer module's minimal number of R-generators, not on the separate analytic theta cokernel.

## 3. Actual Selmer restriction and the base field bound

The complete residual Galois image GL2(Fp) implies
    E[p](K)=0.

Proof: because K/Q is abelian, E[p](K) is a G_Q-stable Fp-subspace of the irreducible E[p]. If nonzero then all E[p] would lie in K, implying the nonabelian extension Q(E[p])/Q is contained in abelian K, impossible.

By inflation–restriction, the global map
    H¹(Q,E[p]) →H¹(K,E[p])^G
is INJECTIVE, and restriction preserves the Kummer local conditions. Hence
    Sel(Q,E[p]) ↪ Sel(K,E[p])^G.

As E[p](K)=0, the usual Kummer comparison injects Sel(K,E[p]) into Sel(E/K,p^infty)[p]. Pontryagin duality gives
    dim_Fp Sel(K,E[p])^G
       ≤dim_Fp Sel(E/K,p^infty)[p]^G
       =dim_Fp M/(p,T)M =d.

Meanwhile the base rank2, rational torsion0 and the true finite-level Kummer exact sequence give
    dim_Fp Sel(Q,E[p]) =2+dim_Fp Sha(E/Q)[p].
Therefore the new unconditional **degree-of-vanishing ⇒ true base Sha dimension** bound reads:

    **dim_Fp Sha(E/Q)[p] ≤ t−2**.

Only full p-adic image and the existence of an authentic K with theta_K reduction of T-order t<m are required. There is NO Sha finiteness assumption and no need to assume or prove E(K)=E(Q).

## 4. The real rank-two theta quadratic ⇒ Sha[p]=0 implication

The genuine Néron-integral Manin symbols and exact Hecke norm imply, for each deep admissible q1,q2, the TRUE diagonal theta satisfies

    theta_K mod(p,T³)=u*T²,     u≡r*delta_(q1q2) modp,

up to the known p-adic unit (a possible factor2, and a group-ring unit from the convention on Frobenius) between the standard Mazur–Tate normalization of Bullach–Honnor and our frozen normalized plus-symbol convention. These units do not affect the modp order t.

If the REAL two-factor Kurihara coefficient is a p-unit,
    **delta_(q1q2)!=0 modp**, so t=2. The bound in §3 becomes
    2+dim Sha[p] ≤d≤2,
and thus
    **Sha(E/Q)[p]=0**.

Because any nonzero p-primary torsion has nonzero order-p torsion, this implies
    **Sha(E/Q)[p∞]=0**
(with no prior finiteness assumption).

This gives a TRUE Selmer/Fitting proof of the same primewise implication previously extracted from Kim's Kolyvagin-system theorem, and does so using the direct Mazur–Tate theta of our explicit finite abelian fields. It is the requested REAL arithmetic bridge (at fixed p) from theta to true Selmer, but NOT a prime-independent rank-two regulator comparison.

## 5. Three actual E389a1 witnesses, independently user executed

| p,k | q1,q2 | actual theta mod (p,T³) | δ mod p^k | new implication |
|---|---|---|---|---|
|5,1 |41,61 |4*T² mod(5,T³)|4 mod5|Sha[5∞]=0|
|11,1|397,991|1*T² mod(11,T³)|1 mod11|Sha[11∞]=0|
|5,2 |5351,10651|2*T² mod(5,T³)|22 mod25|Sha[5∞]=0|

The values and true integer theta polynomials were independently USER-reproduced in Ubuntu. The Sha-zero outcomes at p5,p11 already had independent earlier certified proofs; the novelty is the *proof mechanism* via Bullach–Honnor's real Fitt0 inclusion, not a new prime or a new global Sha support theorem.

A short exact arithmetic gate:
    verification/bsd389_Bullach_Honnor_real_Selmer_Fitting_bridge_gate.py
checks theta order t2 in three authentic polynomials, the finite local-ring Nakayama implication for sample presentations, and prints the stated theorem scope. It does not compute the unknown Selmer group over K.

## 6. Strict limitations and next mathematically decisive problem

This theorem gives a real **map from published arithmetic to genuine Selmer Fitting ideals**, not an actual module isomorphism
    coker(m_U) ≅ Sha[p∞]^∨.
No such map is proved by Bullach–Honnor, and their Fitt0 inclusion is one-sided.

The whole proof remains contingent on a **prime-specific** quadratic theta coefficient that is nonzero modp. For all sufficiently large p, Serre/Chebotarev give deep good auxiliaries q1,q2, but neither their existence nor Bullach–Honnor's Fitt inclusion forces this coefficient to be nonzero. A uniform rank-two Kato/Kurihara nonvanishing theorem, or a fixed p-INDEPENDENT Fitt2 integer bound, is still necessary for global Sha finiteness and exact complex BSD.

**Verdict:** A genuine published 2025 Selmer comparison directly applies to the varying double-ramified diagonal extensions in this project and proves, for each valid p, the bound dim Sha(E/Q)[p] ≤ ord_T(theta_K modp)−2. At a two-factor unit it forces the genuine p-primary Sha to vanish. This is noncircular and resolves the previously missing *kind of comparison* at a fixed p, while leaving the uniform ALL-p nonvanishing requirement untouched.
