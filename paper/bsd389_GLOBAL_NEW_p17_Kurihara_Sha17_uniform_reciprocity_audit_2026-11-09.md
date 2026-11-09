# BSD 389a1 — NEW direct p=17 Kurihara witness, correct integral Kato comparison, and uniform support no-go (9 Nov 2026)

**Scope:** an independently repeated finite arithmetic certificate at p=17, yielding Sha(E/Q)[17∞]=0 by Kim's Theorem 1.1. Not an all-prime proof, nor an archimedean rank-two BSD leading-term equality.

## 1. Correction of the prior Kato-unit obstacle

Castella–Sano (2026), *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem 2.1.3, explicitly establishes the integral reciprocity

  exp^*_{omega_E}(res_p(kappa_n^Kato)) = u_n p^{t_p} delta_n,

with **u_n a unit of Z_p/I_n** and p^{t_p}=#E(Q_p)[p∞]. The previously stated need to prove the unit-status of a vague period scalar is outdated. At p=5,7,11,13,17 for 389a1, E(F_p) has orders 9,13,16,17,24 and E(Q_p)[p∞]=0, so p^{t_p}=1. The missing input is **nonvanishing at EXACTLY TWO auxiliary factors for unbounded p**.

Source: https://arxiv.org/pdf/2601.14504 (Theorem 2.1.3, p.7). The two older notes on Poitou–Tate/relaxed Selmer have been corrected in this PR.

## 2. Direct new p=17 certificate

E: y²+y=x³+x²−2x; conductor 389; minimal discriminant +389; full saturated MW rank 2, torsion 0, Tamagawa product 1. Surjectivity of E[17] is covered by Mazur's theorem for semistable curves; full 17-adic large image follows by lifting. Manin constant is a 17-unit, N=389 squarefree; good ordinary at 17 with a17=−6, #E(F17)=24, and no Q17-rational 17-torsion.

Select Kolyvagin/Kurihara primes

    q1=1667: a_q1=19; #E(F_q1)=1649=17·97; local MW row (1,6).
    q2=5237: a_q2=87; #E(F_q2)=5151=17·303; local MW row (1,12).

Both are ≡1 mod17, have a_q≡q+1≡2 mod17, and have nonidentity-unipotent Frobenius. Their local determinant is 6 mod17.

Using the *exact Néron-normalized integral* 390-vector of Manin symbols reconstructed independently from 1,559 integer relations (plus independent archived cusp value m^+(7/389)=−1), a C++17 direct full-half-sum computed

    FULL_KURIHARA_P17_NORMALIZED 1667 5237 4.

An independently coded **pure Python** modular-symbol/primitive-root evaluator recomputed 3,863,552 nonzero-weighted half-range terms at n=1667·5237=8,730,079 and obtained

    P17_INDEPENDENT_PYTHON_COMPLETE_KURIHARA_PASS  p=17 q1=1667 q2=5237 delta=4.

Hence the normalized Kurihara number is a 17-unit:

    delta_(1667·5237) = 4 (mod17).

By Kim's Theorem 1.1 (https://arxiv.org/pdf/2505.09121), the root sign +1, delta_1=0 (analytic rank 2), and odd-ν functional-equation vanishing give the minimal nonzero derivative order exactly 2. The mod17 unit also gives ∂^(2)=∂^(∞)=0. Kim's cofinite Selmer structure consequently is

    Sel_(17∞)(E/Q) ≅ (Q17/Z17)^2.

Using the independently certified full MW group of rank 2, Kummer yields

    **Sha(E/Q)[17∞] = 0**.

This is a new independent p17 primary certificate (using a published/theorem preprint as mathematical input), not a uniform proof.

## 3. Finite zero-support audit across FIVE p

The cross-prime audit verifies 481 *distinct* pairs, not an extrapolation:

| p | pairs | both zero | both nonzero | mismatches |
|---|---:|---:|---:|---:|
| 5 | 325 | 49 | 276 | 0 |
| 7 | 55 | 9 | 46 | 0 |
| 11 | 70 = 45 old + 25 new | 3 | 67 | 0 |
| 13 | 21 newly computed | 1 | 20 | 0 |
| 17 | 10 newly computed | 1 | 9 | 0 |
| TOTAL | 481 | 63 | 418 | 0 |

The earlier attempt to exhaust all 105 p11 pairs timed out and is **not** recorded as completed. The extra 25 p11 pairs and the 21 p13 + 10 p17 pairs are actual completed direct-sum computations.

The p13 pair (1249,4603) has local determinant and Kurihara number both zero; two p13 nonzero values and this zero were independently recalculated in Python. The alternating Kurihara pair matrix has rank 6 at p13 versus rank 2 for the local MW determinant. At p17 the ranks are 4 versus 2. Hence a factorized two-vector equality remains false even as the vanishing indicators agree in the finite samples.

## 4. Why the attractive pointwise theorem is at least as hard as Sha

**Conditional proposition.** Fix a prime p with Kim's large-image hypotheses. If Sha(E/Q)[p] is nonzero, then **all** two-auxiliary normalized Kurihara numbers vanish mod p, by the contrapositive of Kim's Theorem 1.1 and the rank-2 Kummer sequence. However the proved full two-point Kummer image over Q(E[p]) and Chebotarev produce infinitely many nonidentity-unipotent pairs (q1,q2) with an invertible MW localization determinant. Thus for such a hypothetical p there would be infinitely many explicit **mismatches** to any global pointwise assertion

    D_(q1,q2) != 0  ==>  delta_(q1·q2) != 0.

Accordingly a proof of the global pointwise implication would already be a proof of Sha[p∞]=0 for that p; no argument using local MW information alone can provide it without a genuine additional global derived-Euler/Selmer theorem. **No converse pointwise equivalence is asserted even when Sha[p∞]=0**.

## 5. Remains OPEN

(1) An independent prime-uniform result guaranteeing two-auxiliary unit Kurihara numbers, or another all-prime annihilator of Sha(E/Q). (2) Exact archimedean identity L''(E,1)/2 = Omega_E Reg(E) #Sha(E/Q). These are independent BSD obligations.

**Reproduction:** attached conversation archive \`bsd389_new_p17_and_481pair_certificate_20261109.zip\`, SHA256 \`413447bac7b04d9591f27f1eb03c2830fc1ce83e70d534aebae27df7e773ac93\`, contains 390-vector regeneration, independent p17 Python checker, C++17 evaluators, p13/p17 pair data, complete five-p audit, logs, and a per-file SHA256 manifest. No Sage required.