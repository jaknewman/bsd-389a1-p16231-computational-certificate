# BSD 389a1 — exact two-prime Poitou–Tate reciprocity and a Kato normalization obstruction (2026-11-08)

**STATUS: PROVED conditional only on STANDARD cohomological Selmer hypotheses; NO global Sha finiteness, Kurihara unit uniformity, or exact complex BSD.**

## 1. Two-point finite–singular reciprocity

Let E:y²+y=x³+x²−2x, with full saturated E(Q)=ZP⊕ZQ, P=(-1,1), Q=(0,-1). For any p≥5 take auxiliary good primes q1,q2 (different from p and 389) with nonidentity unipotent Frobenius on V=E[p] and a nonzero 2×2 finite-local Kummer determinant B for P,Q; the earlier Kummer–Chebotarev theorem supplies such pairs uniformly. Write

    F_i = H¹_f(Q_qi,V) ≅ E(F_qi)/p ≅ Fp,
    S_i = H¹(Q_qi,V)/F_i ≅ Fp.

The local Tate pairing gives a perfect S_i×F_i→Fp pairing. Choose dual bases and let B have i-th row (λ_qi(P),λ_qi(Q)).

**THEOREM.** For ANY c∈H¹(Q,V) that is locally finite at every v outside {p,q1,q2}, write y_i for its singular class at q_i, and b_R=−⟨loc_p(c),loc_p(Kummer(R))⟩_p for R=P,Q. Global cup-product reciprocity, together with local finite Kummer spaces being self-annihilating, proves

    Bᵀ (y1,y2)ᵀ=(b_P,b_Q)ᵀ,
    hence (y1,y2)ᵀ=(Bᵀ)⁻¹(b_P,b_Q)ᵀ.

This is exact in Fp. If c is also p-finite then b_P=b_Q=0 and y1=y2=0. Consequently **no global class can have q-singular behavior only at the two separating auxiliaries while staying finite at p and everywhere else**.

## 2. Sharp Poitou–Tate Selmer comparison

Put S=Sel_p(E/Q). Let S_rel permit full local H¹ at q1,q2 but retain standard finite conditions elsewhere; let S_strict impose zero at both q_i. Tate self-duality and the Poitou–Tate five-term sequence give

    0→S→S_rel→S_1⊕S_2→S^∨→S_strict^∨→0.

The connecting map is the dual of the standard localization S→F_1⊕F_2. Since the rational MW subspace E(Q)/p maps via the invertible B onto F_1⊕F_2, this latter localization is surjective. Thus S_1⊕S_2→S^∨ is injective and

    **S_rel = S**,   **S_strict ≅ Sha(E/Q)[p]**.

The second isomorphism follows directly from the global Kummer sequence and uniqueness of the MW correction at the two primes. One gets the dual exact sequence 0→Fp²→S^∨→Sha[p]^∨→0.

**Important:** this theorem DOES NOT imply Sha[p]=0. It proves exactly why simply relaxing auxiliary local conditions adds no new class; the remaining arithmetic obstruction is the strict Selmer group itself.

## 3. Explicit p5/p7 arithmetic calibration

Previously independently computed finite-field local matrices and NEW exact reciprocal inverses:

    p=5, q=(41,61):   B=[[1,3],[1,0]], det=2,
                       (Bᵀ)⁻¹=[[0,2],[1,3]] (mod 5).

    p=7, q=(113,673): B=[[1,3],[1,6]], det=3,
                       (Bᵀ)⁻¹=[[2,2],[6,5]] (mod 7).

Our independently executed standard-library test checks Bᵀy=b for all p² possible b at each prime: 25/25 and 49/49 PASS.

NEW p-adic test: compute exact rational multiples [n]P,[n]Q for n=#E(F_p) (n=9 for p5, 13 for p7); use formal parameter t=−x/y on [n]R and formal logarithm log(t)≡t (mod p²). The local Kummer coordinates (log([n]R)/(n p)) mod p are

    p=5: P=2, Q=4;  p=7: P=5, Q=3.

Thus **at p=5 and p=7** the images of P,Q generate H¹_f(Q_p,E[p]) (a line). For any c obeying the other local conditions, a nonzero p-singular class consequently pairs nontrivially with at least one P,Q and forces a nonzero auxiliary singular coordinate via the proved matrix identity.

This is an actual theorem for arbitrary such c, not a computation of any particular Kato class.

## 4. Why Kim's Kato reciprocity does NOT supply the missing unit

Chan-Ho Kim, *The refined Tamagawa number conjectures for GL₂*, arXiv:2505.09121, §4, explicitly notes that the exact integral image of the dual exponential and the integral period comparison factor C_per are **not calculated in general**. His reciprocity relates Kato-derived singular p-localizations to modular-symbol Kurihara quantities up to a common nonzero scalar; the factor cancels in **differences of valuations** used by the structure theorem (see §4, Remark 4.1 and Proposition 4.2). It cannot simply be declared a p-adic unit.

No universal identity δ_(q1q2)=u·det B with u∈Fp× has been established. The previously audited 7-admissible (113,281) pair has δ=0 although q281 alone separates P,Q; but Frob_281=I, so it does not refute a hypothetical narrower nonidentity-unipotent-pair version.

**Exact outstanding tasks:** construct an appropriate Kato-derived global c with finite conditions away p,q1,q2; verify the integral p-unit period comparison; prove a nonzero singular localization at p that pairs with the rational MW image for all sufficiently large p; and ensure a TWO-prime unit witness rather than an unspecified higher-level one. None follows from the local Kummer determinant or Poitou–Tate alone.

**The complex BSD identity L''(E,1)/2=Omega_E Reg_E remains a separate unproved archimedean theorem.**

## Sources
- Chan-Ho Kim, arXiv:2505.09121, §4, https://arxiv.org/pdf/2505.09121
- Poitou–Tate for Selmer structures, e.g. Algebra & Number Theory 12 (2018), Theorem 3.7, https://msp.org/ant/2018/12-10/ant-v12-n10-s.pdf
- Castella–Sano, arXiv:2601.14504, https://arxiv.org/pdf/2601.14504
- Verification: verification/bsd389_global_reciprocity_Poitou_Tate_matrix_20261108.py and verification/bsd389_local_p_log_Kummer_unit_20261108.py.
