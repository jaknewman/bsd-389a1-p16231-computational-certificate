# BSD 389a1 — Exact Euler norm identities and genuine Selmer-Fitting consequences over two p-bicyclic fields

**2026-11-13. Verified integer computation and application of Bullach–Honnor (2026) Thm 1.4. NOT a global Sha annihilator or exact rank-two complex BSD.**

## Exact finite-level elements and Euler compatibility

For E:y²+y=x³+x²−2x, N=389, use the archived 390-entry **integer** normalized plus Manin symbol m(a/n) with m(7/389)=−1,m(5/389)=−2, period normalization a p-unit for p=5,7. Put θ_n=Σ_(a mod n)×m(a/n)σ_a∈Z[(Z/n)×]. For distinct good auxiliary primes q,ℓ, the Hecke relation proves coefficient by coefficient

    **π_{qℓ,q}(θ_{qℓ})=(a_ℓ−σ_ℓ−σ_ℓ^{-1})θ_q.**

For the squarefree regularization m*_(qℓ)(a)=m(a/qℓ)−m(aℓ^{-1}/q)−m(aq^{-1}/ℓ), given m(0)=0 and aug(θ_ℓ)=0 at our four auxiliary primes, the exact alternative is

    **π_{qℓ,q}(θ*_{qℓ})=(a_ℓ−ℓσ_ℓ−σ_ℓ^{-1})θ_q
                          =−σ_ℓ P_ℓ(σ_ℓ^{-1})θ_q.**

Here P_ℓ(T)=1−a_ℓT+ℓT² is the genuine local Euler polynomial; augmentation of this regularized norm factor is −#E(F_ℓ). **Do not confuse θ* with the canonical unregularized Mazur–Tate θ of Bullach–Honnor's Fitting theorem.** The first formula agrees with Bullach–Honnor Proposition (2.4).

Exactly evaluated all 40+60+112+672=**884** coefficients in EACH normalization (**1,768 integer equalities**):

| projection | a_ℓ | #E(F_ℓ) | raw and regularized norms | regularized projected rank2 jet |
|---|---:|---:|---|---:|
| 2501→41, ℓ=61 | −8 | 70 | PASS 40+40 | 20 mod40 |
| 2501→61, ℓ=41 | −3 | 45 | PASS 60+60 | 0 mod60 |
| 76049→113, ℓ=673 | 2 | 672 | PASS 112+112 | 0 mod112 |
| 76049→673, ℓ=113 | 9 | 105 | PASS 672+672 | 0 mod672 |

## Fully explicit *integral* group-ring elements on two real p-extensions

Let K₅ be the degree-25 abelian real extension of conductor 2501 with Gal(K₅/Q)=C₅×C₅. Let K₇ be the degree-49 real extension of conductor 76049 with Gal(K₇/Q)=C₇×C₇. Both arise from the p-Sylow quotients of (Z/2501)× and (Z/76049)× respectively. Their canonical **unregularized plus theta** comes from θ_n, up to the audited p-unit period convention.

Computed the **complete** 25 and 49 integer coefficients in Z[Cp×Cp] by direct rational-cusp evaluation, recorded in the downloadable archive and two complete CSVs. For primitive roots (6,2) and (3,5), with X=σ_q−1, Y=σ_r−1, the six full integer moments are

    n=2501, p=5: (0,280,60,5360,244,950)
    n=76049,p=7: (0,−448,−26208,−23408,−2604992,−9552816).

Therefore EXACTLY (in the indicated p-bicyclic group rings)

    **θ_{K₅} ≡ 4XY   (mod 5,I³)**
    **θ_{K₇} ≡ 2XY   (mod 7,I³)**.

Both lower and pure quadratic terms vanish. Since 4 mod5 and 2 mod7 are units, the integral rank-two classes have **exact mod-p augmentation order two**.

As an additional independent check, the exact regularized *real-plus* mixed digits are 2 mod5 and 1 mod7: these differ by the expected factor 2 and cannot be substituted without stating normalization.

## New application: actual p-primary Selmer corank over degree 25 and 49 fields

Source: Bullach–Honnor, *On the refined 'BSD type' conjectures of Mazur and Tate* (2026), Hypothesis (1.2), Theorem (1.4)(a),(b), Remark (1.5)(a), https://dominikbullach.github.io/MazurTate.pdf.

At the specific pairs (K₅,p=5) and (K₇,p=7), the hypotheses hold: the prior 389a1 mod-p surjectivity certificates and p≥5 imply p-adic image contains SL₂(Zp); Kp is **totally real**, so does not contain ζp; E has good reduction at p so no additive caveat. Manin/real-period conventions differ only by a **p-unit** in these two cases and do not alter the following nonvanishing.

Theorem (1.4)(a) yields θ^MT_K∈I^{r_p+s_p(m)+2c_p(K)}, with r_p = rank_Zp Sel_{p∞}(E/K)^∨ and other terms ≥0. Our nonzero I²/I³ coefficient modulo p gives r_p≤2. The two known rational points give r_p≥2; hence

    **corank Sel_{5∞}(E/K₅)=2, rank E(K₅)=2, Sha(E/K₅)[5∞] FINITE.**
    **corank Sel_{7∞}(E/K₇)=2, rank E(K₇)=2, Sha(E/K₇)[7∞] FINITE.**

This is an inference using a new external theorem plus exact theta arithmetic, NOT an independent direct Selmer calculation over Kp. It does not assert Sha(Kp)[p∞]=0.

Theorem (1.4)(b) + semistable functional equation also places the canonical explicit θ_K in

    **Fitt₀_{Zp[Cp²]}(Sel_{p∞}(E/K)^∨) ⊂ Ann_{Zp[Cp²]}(Sel_{p∞}(E/K)^∨)**,

giving actual **group-ring annihilators** of Selmer over these fields, not scalar integers annihilating Sha over Q.

Sharp caution: R=Zp[Cp×Cp], M=R/(X²,Y)⊕R/(X,Y) has Zp-rank2 and finite p-torsion while XY∈Fitt₀(M). Thus a unit mixed XY jet alone does not force Sha(Kp)[p∞]=0.

## Outstanding

These two finite abelian fields and their group-ring annihilators neither supply one nonzero integer D with D·Sha(E/Q)=0 nor prove the classical rank-two archimedean BSD identity. A genuine uniform Kato derivative / integral cohomological term comparison for all p remains OPEN. We make **no rank assertion over the much larger maximal real cyclotomic fields**, only over the explicit degree25/49 p-extensions.

## Reproducibility

The user-downloadable archive \`bsd389_integral_Euler_norm_bicyclic_Selmer_20261113.zip\` contains complete coefficients, all 390 integer symbols, separate full-conductor norm and p-quotient programs, complete independent 5×5/7×7 matrices, logs, SHA256SUMS and this proof. An additional exact 390-symbol JSON is in \`verification/bsd389_390_integral_manin_vector_20261113.json\`.

References: Bullach–Honnor (2026), Theorem 1.4 and Proposition 2.4; Burns–Kurihara–Sano (2024), Conjecture 1.1 and Theorem 1.3 for the still-OPEN global archimedean leading term.
