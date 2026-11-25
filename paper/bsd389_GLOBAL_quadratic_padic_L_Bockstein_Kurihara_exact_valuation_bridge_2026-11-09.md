# BSD 389a1 — Exact rank-two p-adic L / Bockstein regulator / Kurihara **valuation** bridge (9 Nov 2026)

**A rigorous deduction from published theorems, not a uniform Sha annihilator and not full BSD.**

## 1. Fixed good ordinary prime, real cohomological complex

Let E:y²+y=x³+x²−2x, N=389, full MW rank 2, torsion 1, Tamagawa product 1. Fix a good ordinary p≥5 with large residual Galois image and p-unit Manin constant. Let L_p(E,T) be the cyclotomic p-adic L-function, and f_{E,p}(T) the characteristic series of the cyclotomic Selmer dual, T=χ_cyc(γ)−1. Rank 2 gives order at least two, so put ℓ_{p,2}=[T²]L_p(E,T).

**New exact source-based implication, without assuming the full main conjecture:**

    ℓ_{p,2}≠0 ⇒ ord_T f_{E,p}=2
             ⇒ (Sha(E/Q)[p∞] finite AND cyclotomic p-adic height regulator R_(γ,p) nonzero).

The first arrow is Kato's *one-sided* divisibility f_{E,p} | p^m L_p(E,T) combined with ord f≥MW rank=2. The second is Perrin-Riou–Schneider's order-of-vanishing theorem (Balakrishnan–Müller–Stein 2012, Ths. 1.6–1.7). This is a genuine analytic criterion for p-primary Sha **finiteness** with only a single p-adic L-function coefficient, not a hypothetical matrix comparison.

## 2. Full **valuation** equality (ordinary main conjecture known in this setting)

Castella–Sano 2026, Theorems A/B, identify the proved ordinary Iwasawa Main Conjecture with the integrally normalized all-length Kurihara primitivity. The main conjecture identifies L_p and f_{E,p} up to an invertible element of Zp[[T]]. Therefore the converse of the order-of-vanishing implication also holds, and when ℓ_{p,2}≠0:

    v_p(ℓ_{p,2})
       = v_p(ε_p) + v_p(R_(γ,p)) + v_p(#Sha(E/Q)[p∞]),

where α_p is the p-adic unit root of X²−a_p X+p and ε_p=(1−α_p^{-1})². In particular v_p(ε_p)=2v_p(#E(Fp)). No Tamagawa or MW-torsion term remains for E389a1.

Kim's refined Kurihara structure theorem, combined with Castella–Sano's M∞=v_p(Tam_E)=0, identifies M₂(p)=v_p(#Sha[p∞]) whenever ρ_p=2. Thus:

    **M₂(p)=v_p(ℓ_{p,2})−2v_p(#E(Fp))−v_p(R_(γ,p)) ∈ 2 Z_{≥0}.**

The equality is **of valuations/ideals**, NOT of full p-adic numerical values. If the RHS is 0, Sha(E)[p∞]=0. If ℓ_{p,2}=0, this particular rank-two formula cannot be used: the p-primary Sha might be infinite, or the p-adic height pairing might be degenerate. Cassels–Tate forces the displayed value to be even whenever Sha_p is finite.

## 3. Concrete 389a1 p5 consistency test from two *published* independent computational sources

SageMath's documented p-adic L-series for 389a at p=5 has

    [T²] L_5(E,T) = 4 + O(5).

Mazur–Stein–Tate, *Computation of p-adic heights and log convergence*, §4.3, give normalized cyclotomic regulator

    R_(5,MST) = 1 + 2·5 + 2·5² + ... .

Independent exact finite-field arithmetic on E gives #E(F5)=9, a5=−3, α5≡2 mod5, and ε5≡4 mod5. Thus the published mod5 digits are compatible with the predicted unit

    4 / (4 · 1) ≡ 1 (mod5).

This *does not recompute either published p-adic quantity* and is not an independent proof of precise p-adic BSD; matching the choice of χ(γ)=1+p and the height period convention is essential for comparison of actual values. The zero v5(#Sha)=0 already has independent proven certificates.

An executed standard-library Python cross-check enumerated E(Fp) at all 13 p in Mazur–Stein–Tate's §4.3 regulator table, verified good ordinary/nonanomalous, and checked the p5 Euler and numerical unit ratio. All checks PASS.

## 4. A targeted reproducible Sage gate for the SW2013 exceptional ordinary p=16231

Sage 10.x script \`verification/bsd389_quadratic_padic_L2_Sage_gate_20261109.py\` performs:

  1. Check p is good ordinary and read Np=#E(Fp);
  2. Compute L_p(E,T) to coefficient T² and certified p-adic precision;
  3. If [T²]L_p≠0 with sufficient accuracy, use Kato+Perrin-Riou–Schneider to prove **Sha[p∞] finite**;
  4. Optionally calculate E.padic_regulator(p,precision). Its Sage raw cyclotomic normalization has v(Reg_raw)=v(R_(γ,p))+2 for χ(γ)=1+p and rank 2; compare v_p(ℓ₂)−2v_p(Np)−(v_p(Reg_raw)−2), using the main conjecture and source normalization to test Sha's p-primary order.

The Sage script was **NOT EXECUTED in this session** (Sage unavailable); it is a *test design*, not a p16231 certificate. The p16231 gate is not claimed closed.

Example:
\`\`\`bash
python -u verification/bsd389_quadratic_padic_L2_Sage_gate_20261109.py --p 5
python -u verification/bsd389_quadratic_padic_L2_Sage_gate_20261109.py --p 16231 --skip-regulator
\`\`\`

## 5. Uniform and archimedean boundaries

No theorem established here forces ℓ_{p,2}≠0 for **all sufficiently large** good ordinary primes; and a proof of p-primary **finiteness individually** is still short of an integer annihilator of global Sha, unless one additionally proves that the p-primary group is zero for all but finitely many p. Good supersingular p and the bad prime 389 require separate local frameworks.

Even proving the p-adic valuation formulas at every p would not establish the complex identity L''(E,1)/2 = Ω_E·Reg_NT(E)·#Sha(E/Q).

## Sources

- Balakrishnan–Müller–Stein (2012), Theorems 1.6 and 1.7: https://www.math.uni-hamburg.de/home/js.mueller/pbsd.pdf
- Castella–Sano, Theorems A/B (2026): https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Kim, Theorem 1.1 (2025): https://arxiv.org/pdf/2505.09121
- Mazur–Stein–Tate (2006), §4.3: https://www.wstein.org/papers/pheight/pheight.pdf
- SageMath elliptic curve p-adic L-function docs, published p5/T² digit: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html

**STATUS:** precise local rank-two cohomological bridge PROVED from published results, p5 normalization audit PASS, all-p Sha annihilation and classical BSD OPEN.