# BSD 389a1 — 55 exact Kurihara pair coefficients, rank-ten obstruction, and minimal five-wedge reconstruction (8 November 2026)

**Theorem proved by a reproducible finite computation, NOT a BSD theorem.** A fixed 390-value integral Manin table for E=389a1 is reconstructed without Sage (from all Manin/Hecke relations plus independent archived cusp-period normalization) and used to compute 55 complete two-prime Kurihara values modulo seven. The ordered alternating pair-coefficient matrix has rank ten rather than the rank two of a single Mordell–Weil local determinant. The exact zero sets coincide **on this finite data set**, but no global zero-locus equivalence is proved.

## 1. Genuine normalized input

E:y²+y=x³+x²−2x, N=389, minimal discriminant +389, Mordell–Weil basis P=(-1,1), Q=(0,-1). A previous independent Sage/eclib certificate established the exact Néron-normalized plus modular-symbol values m⁺(7/389)=−1 and m⁺(5/389)=−2. The reconstruction from 1559 integer Manin/plus/Hecke-T2 equations, with rank 389 modulo 7 and exact integer verification, produces a unique normalized 390-entry vector with values in {-2,-1,0,1,2}, content gcd 1, 228 nonzero classical cusp symbols. All six additional Hecke operators T_3,T_5,T_7,T_11,T_13,T_17 were checked on all 390 cosets.

An independently compiled C++ evaluator uses that exact table and full weighted modular-symbol sums to calculate normalized two-prime Kurihara numbers, with q-pairs oriented by increasing order for the matrix constructed below. The earlier archived p=7 witness δ_(113·673)=2 is independently reproduced.

## 2. Exactly 55 arithmetic pairs

Fix p=7. The 11 distinct good auxiliary primes are

    113, 673, 1429, 2423, 3389, 4943, 5657, 5881, 6217, 6427, 6959.

Each satisfies q≡1 mod7, a_q≡q+1≡2 mod7 and v_7(#E(F_q))=1; the mod-7 Frobenius is therefore **nonidentity unipotent**, and E(F_q)/7 has dimension one. The reductions of P,Q in each one-dimensional quotient were recomputed using exact group operations.

For every i<j we compute:

    D_ij = determinant of local Kummer rows for (P,Q) at (q_i,q_j), mod 7;
    K_ij = integrally normalized Kurihara delta_(q_i*q_j), mod 7.

A complete 55-pair enumeration returns

    (D_ij==0) iff (K_ij==0)   for all 55 pairs.
    Exactly nine pairs satisfy both vanishings.

This is an exact *sample-wide computational fact*, **not** a theorem about all primes p or all admissible q-pairs, and **not** an identification of the actual scalar values.

## 3. Rank-ten Plücker obstruction

For the chosen increasing order q_1<...<q_11, extend K_ij and D_ij to alternating 11×11 matrices using K_ji=−K_ij and D_ji=−D_ij, with zeros on the diagonal. Then:

    rank_F7(D)=2,  rank_F7(K)=10.

The principal 10×10 block on

    [113,673,1429,2423,3389,4943,5657,5881,6217,6427]

has Pfaffian **6 mod 7**. Its determinant, verified independently using SymPy over the integers and reduced modulo seven, is 6²≡1 mod7. Therefore the rank of the full alternating Kurihara matrix is ten.

**A stronger new identity:** for EVERY c in F_7,

    Pf((K−cD)[first ten indices]) = 6 mod 7.

The Pfaffian of K−cD is affine in c because D has rank two, hence D∧D=0; the direct exact computation at c=0 and c=1 finds the same value six, proving the displayed identity for all c. In particular rank_F7(K−cD)=10 for all c.

Thus subtracting **any globally constant multiple** of the rational-point determinant cannot reduce the rank of this pair matrix or explain its values.

**Caution:** K is made alternating using the fixed increasing order on the pair labels, whereas the original δ_(q_iq_j) itself is symmetric in the unordered pair. The rank-ten result is a valid obstruction to a single ordered determinant factorization (and to an independent per-prime unit rescaling), not a claim of a newly identified ten-dimensional Galois motive.

## 4. Exact minimum five-channel representation

Finite-field symplectic elimination constructs five pairs of vectors A_h,B_h in F_7^11 such that every one of the 121 entries of K satisfies

    K_ij = sum_(h=1)^5 [ A_h(i)B_h(j) − A_h(j)B_h(i) ] (mod 7).

Because rank K=10, five decomposable wedges are **minimal**. A complete vector certificate (110 coordinates) is shipped as JSON. The pivot pairs in the construction are

    (113,673), (1429,2423), (3389,4943), (5657,5881), (6217,6427).

This is a fully exact finite algebraic decomposition, not an established integral Kato reciprocity law: the vectors are obtained *after computing δ*, and no uniform-in-p motivic meaning has been proved.

## 5. Targeted stress test on a possibly exceptional local slope

At p=7 the p-adic local Kummer vector of (P,Q) has slope 2 (in the previously computed normalization). Good primes 5657,13007,13763 all have local mod7 row (1,2). Three additional direct complete Kurihara computations give

    δ_(5657·13007)=0,
    δ_(5657·13763)=0,
    δ_(13007·13763)=0 mod7,

consistent with their vanishing local determinants. These are additional checks **outside** the 55-pair matrix; the two-prime zero-support statement remains empirical.

## 6. Logical boundary and next real question

- **Proved here:** exact fixed-p calculation, 55/55 matching zero pattern, rank-ten obstruction, universal-in-c Pfaffian nonvanishing, minimal five-wedge decomposition.
- **NOT proved:** any all-p statement of the form δ_(q1q2) unit for sufficiently large p, Sha(E)[p∞]=0 uniformly, exact complex leading coefficient L''(E,1)/2=Ω_E Reg(E), or an identification of these algebraic wedges with the global Kato/Bockstein class.
- **Literature:** Kim's *The refined Tamagawa number conjectures for GL2* (2025, Thm. 1.1 and §3–§5, https://arxiv.org/pdf/2505.09121); Castella–Sano *On refined nonvanishing conjectures by Kurihara and Kolyvagin* (2026, Thm. B, https://web.math.ucsb.edu/~castella/Kurihara.pdf). Their some-length nonvanishing results do not force a primitive two-prime coefficient in rank two.

An auditable standalone zip, generated and verified in this conversation, contains `modsym_integral_389.py`, `bsd389_exact_manin_390.json`, `p7_kurihara_fast.cpp`, `modsym7.h`, `bsd389_p7_11prime_kernel_rank_audit_20261108.py`, `bsd389_p7_11prime_kernel_rank_certificate_20261108.json`, `bsd389_p7_five_channel_decomposition_20261108.py`, `bsd389_p7_five_channel_decomposition_20261108.json`, and execution logs.

**New precision:** The pairwise zero-pattern coincidence is a real finite observation worthy of investigating in Kim's *modified/transverse* Selmer structures, but reducing it to the known Mordell–Weil determinant for *all* p without separately controlling Sha would be circular. An exact higher-rank integral reciprocity/comparison theorem is still needed.
