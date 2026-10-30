# E=389a1, p=599: exact finite-level cyclotomic augmentation order two

Date 2026-10-30. The genuine user-run Sage transcript proves that the *tame-trivial projection* of the **unhalved plus-symbol sum** at conductor p² has first three coefficients C0=0, C1=0, C2=543 mod 599. The three computations used 179101 plus-symmetric unit pairs, true eclib-derived Manin 390 data, SHA256 fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8, all 598 Hecke-fibre cancellations, and took 3.231 seconds.

Let G=(Z/p²)^*, Delta its subgroup of order p-1, and Gamma=<1+p>, cyclic of order p. Let S(a/p²) be the plus Neron-normalized modular symbol (reduction mod p). Define

  Theta = sum_(a in G) S(a/p²)*[a] in Fp[G].

The tame-trivial projection of Theta in Fp[Gamma] = Fp[T]/(T^p), with [1+p]=1+T and a=omega(a)*(1+p)^k(a), has expansion

  barTheta(T) = sum_j C_j*T^j
  C_j = sum_(a in G) S(a/p²)*binomial(k(a),j).

The exact Fermat quotient k(a) is -(a^(p-1)-1)/p mod p. The coefficient values give

  barTheta(T) = 543*T² (mod T³) in F_599[T]/(T^599);
  barTheta belongs to I² and not I³, I=(T).

This is **a rigorous nonzero finite-level cyclotomic leading coefficient** and establishes the augmentation order exactly 2 for this explicitly specified projection. Numerically 543=-56 mod 599; sum_a S(a/p²)*k(a)²=2*C2+C1=487 mod 599. The latter is a dependent identity, NOT an independent computational check.

**Normalization caution:** this definition sums *both* representatives a and -a. Many Mazur-Tate conventions sum over (Z/p²)^*/{+/-1} once, yielding a factor 1/2 relative to this Theta after the evident identification; the corresponding coefficient is then 543/2=571 mod 599. Such a factor is a p-adic unit, so augmentation order and nonvanishing are unchanged. Exact numerical comparison to published theorems must fix the authors' plus-symbol normalization, periods, and quotient by signs before asserting 543 equals any stated leading term.

**No automatic Sha or Kurihara theorem:** This theta at conductor p² is *not* the rank-two auxiliary q1*q2 Kurihara delta. Nor is the finite truncated element automatically the normalized plus/minus supersingular p-adic L-function; one must account for Frobenius/trace distribution, parity level and signed regulator. A Mazur-Tate leading-term identity with Sha is conjectural in many general settings (e.g., Burns–Kurihara–Sano on derivatives of Kato's Euler system). Kurihara, *On the Tate Shafarevich groups over cyclotomic fields of an elliptic curve with supersingular reduction I*, Invent. Math. 149 (2002), Theorem 0.1, requires ord_p(L(E,1)/Omega_E)=0; this hypothesis FAILS when the rank-two curve has L(E,1)=0. Thus that theorem cannot be invoked directly to deduce Sha[599]=0 from C2=543. Sage's provable p_primary_bound may use the p-adic L-function and the p-adic regulator at suitable precision; a finite mod-p theta coefficient does not bypass that precision proof.

Relevant public references:
- https://kurihara.math.keio.ac.jp/supersingular.pdf (Kurihara 2002)
- https://arxiv.org/abs/2103.11535 (Burns–Kurihara–Sano)
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/sha_tate.html

## Independent mathematical and computational cross-check

A separate [full-convergent C++ implementation](../verification/bsd389_p599_cyclotomic_p2_independent_native.cpp) was newly authored and pushed. It reads the true 390-table file, rebuilds each rational continued fraction via full numerator+denominator states (different from the Python modular-symbol routine and the optimized denominator automaton), calculates k(a) via its own modular exponentiation, checks omega(a)*gamma^k=a for all 179101 representatives, verifies 598 b-fibres vanish, and checks that its three moments are 0,0,543. **This independent C++ check has not yet been user-executed; do not label it PASS.**

Pending: directly audit selected values against eclib; prove a suitable signed supersingular Selmer/Fitting leading-term implication with p599 regulator and normalization. Only then can the finite-level result contribute to a claim about Sha[599^infinity].
