# Minimal mathematical dependency certificate: 389a1, p=16231

Date: 2026-10-26. The **computer-assisted numerical gates have independently reproduced results**, but the theorem below remains conditional on the exact algebraic identification and faithful common Sage/eclib source/data described explicitly. This is **not** a claim of exact p-adic BSD quotient 1 or BSD for every prime.

## Precisely stated implication

Let `E: y²+y=x³+x²−2x` over Q and `p=16231`. Let `A2` denote the coefficient of `T²` of the ordinary untwisted Sage 10.9 `E.padic_lseries(p).series(n=3,prec=3)` with eta=0, gamma=1+p, L_ratio plus modular symbol and period quotient one. Let

`B_p = Tam(E) * Reg_p * (1-alpha^(-1))² / (Tor(E)² log(1+p)²)`,

where alpha is the unit root of `X²-a_p X+p`, and regulator uses the canonical Sage cyclotomic p-adic height basis. Here the verified local gates are: analytic/algebraic Mordell–Weil rank 2, ordinary good reduction at p, a_p=128, Tam=1, torsion=1, real components 2, E's twist D=1, and p-adic Galois residual surjectivity.

**Conditional finite-input theorem.** If the universal C01/Hecke/Manin/Shapiro identity and the values computed from authenticated Sage/eclib table and source semantics are correct, then the proved upper bound of Sage 10.9/Kato applied to E at p is zero and consequently `Sha(E/Q)[p^infinity]=0`.

## Finite dependencies, now distinctly tested

1. Direct Sage/eclib evaluation of `A2^(2) mod p²`: historic V61 complete 254-checkpoint calculation and the independent whole 8115-row cyclotomic-u computation both return `A2^(2)=19460969=1199*p mod 263445361`. The second performed 131698335 nonzero-weight eclib evaluations; separate external audit checked all 8115 row SHA records and exact agreement with all 254 V61 archived blocks.

2. Full p-modular C01 reference scalar: archived V11/V19 sparse producer/contraction and independent complete dual-scalar C++ program each ran through the whole `p(p-1)=263429130` pair domain, both yielding `J=4486 mod p`. The independent run passed 264 exact checkpoints, seven frozen SHA file pins and a second immutable-manifest audit. The two engines share original Manin relations and independently computed V65 Sage/eclib basis table.

3. Algebraic reference equivalence: from the Hecke relation, the two moments `M0, M1` transform for every h in Gamma0(Np) by the 2-by-2 triangular matrix `T(h)=[[1,0],[-ab,a²]]` modulo p. The dual `C0/C1` coefficient transport obeys the transpose action, and exact Manin cusp-divisor relations (390/390, 2012 terms) preserve the functional, including infinity Shapiro cosets. Direct high-p Sage n3 tests were executed for six pairs, including exceptional id=38 (one internal infinity) and id=67 (one external plus 66 internal infinity), with six perfect numeric Sage/C++ matches. These regression tests supplement, and cannot replace, the universal algebraic proof.

4. Analytic bridge: Sage's standard ordinary measure `mu_n(y)=alpha^(-n)(m(y/p^n)-alpha^(-1)m(y/p^(n-1)))`, its exact distribution relation, binomial increment for lifts `j=u+p*v`, and two real components yield

`A2^(3)-A2^(2) = p * J / (4*alpha²) mod p²`.

Small primes 5 and 7 were direct whole n2/n3 Sage/eclib comparisons and matched both the reference scalar correction and the native Sage n3 coefficient. For high p, this bridge is a mathematical source-level derivation rather than a completed direct full n3 Sage summation.

5. Regulator/normalization: two alternative Sage 10.9 p-adic height algorithms, sigma and multiply, independently computed the same 2-by-2 height determinant modulo p^5 on two rank-2 generators, yielding `Reg_p/p³=1930 mod p`, and factor `B_p/p=9534 mod p`. They share foundational Sage elliptic and p-adic arithmetic.

## Deduction

Modulo p, alpha=128, so the measured correction is

`J / (4*alpha²) = 4486 * (4*128²)^(-1) = 8335 mod 16231`.

The n3 coefficient is therefore `A2^(3)=p*(1199+8335)=p*9534 mod p²`. Both n3 analytic coefficient and the BSD factor have valuation precisely one, so the quotient `A2^(3)/B_p` is a p-adic unit with first residue 1 mod p. The ordinary `lp._prec_bounds(3,3)[2]=2` provides absolute p² precision in the coefficient, sufficient to establish that the true analytic quotient is a unit. The Sage 10.9 source method `Sha.p_primary_bound(p)` checks ordinary reduction and Galois image and returns `valuation(an_padic(p,prec=0,use_twists=True))`; for the already independently checked D=1 branch and rank 2, this is valuation zero. As the code documentation describes the exponent as a **provable** upper bound using Kato's Euler-system theorem, exponent 0 forces the p-primary Sha group to be trivial, provided the stated source/precision/theorem prerequisites are correct.

## Exactly what has *not* been certified

- Source-level derivations are human-reviewable proofs but have not been formalized in Lean/Coq, machine verified, or peer reviewed as a single end-to-end theorem.
- Both full C01 programs rely on the same V65 eclib symbol data and exact Manin export. Their independence is in the outer sum and the operator direction, not the underlying modular-symbol oracle.
- Both full level-2 computations rely on Sage/eclib `L_ratio` plus symbols and trusted Sage arithmetic; regulator methods share Sage elliptic data.
- The six direct high-p n3 Sage evaluations are **individual pair** tests only; the full `lp.series(n=3,prec=3)` at p=16231 was NOT run.
- A direct `E.sha().p_primary_bound(16231)` call has NOT been run. The proved upper-bound theorem is applied mathematically by substituting the independently justified same leading coefficient.
- The congruence of the analytic quotient to 1 mod p does not imply exact p-adic equality 1; full all-prime BSD and complex leading coefficient not proved.

## Verification trail

- [Full independent scalar C01 output](../results/independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md), [frozen manifest](../results/independent_scalar_J_frozen_sha256_manifest_2026-10-26.json)
- [Full independent level-2 output](../results/independent_level2_u_full_131714565_residues_PASS_2026-10-26.md), [8115/254 evidence audit](../results/independent_level2_u_full_checkpoint_audit_PASS_2026-10-26.md)
- [Two independent Sage height algorithms](../results/independent_level2_u_firstblock_and_two_height_regulator_PASS_2026-10-26.md)
- [Formal C01/Shapiro duality](c01_shapiro_formal_duality_and_exceptional_audit_2026-10-26.md), [all 390 exact Manin plus six adversarial high-p Sage oracle PASS](../results/c01_shapiro_exact_and_adversarial_high_p_sage_PASS_2026-10-26.md)
- [Universal Sage correction lemma](c01_sage_n3_minus_n2_universal_lemma_auditable_2026-10-26.md), [p=5 and p=7 direct full n2/n3 comparison](../results/bridge_small_primes_5_7_direct_n2_n3_sage_PASS_2026-10-26.md)
- [Sage 10.9 pinned source: sha_tate.py](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py), [Sage 10.9 pinned ordinary L-series: padic_lseries.py](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/padic_lseries.py).
