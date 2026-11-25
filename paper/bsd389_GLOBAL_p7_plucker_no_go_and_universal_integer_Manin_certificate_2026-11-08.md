# BSD 389a1 — Universal *integral* Manin table and a genuine rank-two Plücker obstruction (2026-11-08)

**Summary.** This is a new, independently executed, Sage-free exact computational proof for E=389a1. It reconstructs the fixed 390-entry **integer** Manin-symbol eigenvector, verifies every Manin and Hecke equation, and evaluates six complete two-prime Kurihara sums modulo 7. These six numbers violate the Plücker relation that **every decomposable two-vector determinant** must satisfy, even after any invertible independent per-auxiliary-prime rescaling. All four primes used are nonidentity-unipotent on E[7], and all six Kummer determinants are units. Therefore a natural simple *factorized rank-two determinant comparison* is **false even in the restricted admissible setting**. This does **not** refute arbitrary, pair-dependent derived Kato reciprocity, nor prove all-prime Sha finiteness or exact rank-two complex BSD.

## 1. Fully integral 390-symbol reconstruction with no Sage

Fix N=389 and E: y²+y=x³+x²−2x, with a_2(E)=−2. Set x_∞=m⁺(0) and, for t∈F_389, x_t=m⁺(−1/t)−m⁺(0), interpreting t=0 via the oriented edge 0→∞. These 390 values form a modular-symbol functional on P¹(F_389), subject to standard Manin S and U relations and plus involution x_t=x_{−t}. Hecke T₂ requires T₂ x=−2x, with T₂ written explicitly by paths between rational cusps using the two determinant-two upper triangular matrices.

The fixed exact archive gives two independently Sage/eclib-verified Néron-normalized cusp values

    m⁺(7/389)=−1,       m⁺(5/389)=−2

from `results/bsd389_fixed_rational_manin_independent_JSON_USER_RUN_PASS_2026-11-01.md`.

In the new computation, the 1559 integral equations for the 390 unknown symbols have **rank 389 mod 7**, hence rank at least 389 over Q. Their nonzero genuine modular-symbol solution gives rank at most 389, so the rational eigenline is exactly one-dimensional. A modular CRT reconstruction using p=7,11,13,17,19 fixed by m⁺(7/389)=−1 produces an explicit 390-entry integer vector satisfying **every equation exactly over Z** (not merely modulo a prime), and independently satisfies Hecke T_ell for ell=3,5,7,11,13,17 on all 390 cosets. Its histogram is

    -2:30, -1:84, 0:162, +1:84, +2:30,

its content gcd is 1, and all 389 normalized cusp values have the same 228 nonzeros previously observed in Sage/eclib. The vector is therefore independently determined as the true normalized Manin-symbol vector of E in this model.

Local reproduction script: `modsym_integral_389.py` (deliverable alongside this note), output JSON `bsd389_exact_manin_390.json`. It has no Sage/eclib dependency.

## 2. Four genuinely nonidentity-unipotent primes and their MW coordinates

Set p=7 and choose

    q=(113,673,1429,2423).

Each prime has q≡1 (mod 7), a_q≡2 (mod 7), and **v_7(#E(F_q))=1**, so its Frobenius on E[7] is a *nonidentity* unipotent matrix (identity Frobenius would yield 49 rational 7-torsion points).

Exact point counts and group operations yield:

| q | a_q | #E(F_q) | (P,Q) in E(F_q)/7, one-dimensional coordinates |
|---|----:|--------:|---------------------------------------------|
| 113 | 9 | 105 | (1,3) |
| 673 | 2 | 672 | (1,6) |
| 1429 | −5 | 1435 | (1,4) |
| 2423 | 30 | 2394 | (0,1) |

Thus every determinant of two distinct rows is a unit modulo 7. In order (113,673,1429,2423), the six pairwise determinants are

    D12=3, D13=1, D14=1, D23=5, D24=1, D34=1  (mod 7).

Their mandatory rank-two Plücker relation holds:

    D12 D34 − D13 D24 + D14 D23 = 3−1+5 = 0 (mod 7).

## 3. Six **complete** genuinely normalized Kurihara sums

Using the exact integral Manin table from §1, a standard continued-fraction path expansion for every cusp a/(q_i q_j), and discrete logs relative to the least primitive root in each F_q, an independent **full half-range sum with exact plus symmetry** gives:

| Pair | δ̃_(q_i q_j) mod 7 | Kummer D_ij mod 7 |
|---|---:|---:|
| 113×673 | 2 | 3 |
| 113×1429 | 1 | 1 |
| 113×2423 | 6 | 1 |
| 673×1429 | 2 | 5 |
| 673×2423 | 3 | 1 |
| 1429×2423 | 3 | 1 |

The first δ̃=2 reproduces the earlier authentic Sage/eclib normalized p=7 audit; the other five are now independently computed, with no Sage and no reliance on historic δ-values. All were also reproduced by a **second, compiled C++** evaluation using exactly the same integer table and independently implemented continued fractions.

**NEW OBSTRUCTION:**

    δ12 δ34 − δ13 δ24 + δ14 δ23
       = 2·3 − 1·3 + 6·2
       = 15 ≡ 1 (mod 7) ≠ 0.

Hence the collection of six Kurihara scalars is **not a decomposable 2-form** on these four auxiliary-prime labels. In particular there do not exist two vectors A,B∈F₇⁴ with δ_ij=A_i B_j−A_j B_i (for i<j). This remains false if each δ_ij is multiplied by ANY independently chosen invertible product u_i u_j, since all three Plücker terms are multiplied by the same nonzero product u_1u_2u_3u_4.

Therefore the following previously plausible simple reciprocal factorization is **impossible**:

    δ̃_(q_i q_j) = c · u_i u_j · det( local_vector(q_i),local_vector(q_j) )

for a fixed unit c and any individual local units u_i, where all four q_i have nonidentity-unipotent Frobenius and all local MW determinants are units.

**Precise boundary:** This does NOT disprove a statement with genuinely **pair-dependent** coefficients u_{ij}, nontrivial additive correction terms, or a more complicated global Kato/derived local reciprocity. Nor does it disprove the existence of a nonzero 2-prime δ for each p. Indeed all six δ above are nonzero, fully consistent with previously established Sha(E)[7∞]=0.

## 4. Consequence for uniform Sha and complex BSD

A proof that a primitive two-prime Kato/Kurihara coefficient exists for almost every p cannot be obtained from a universal exterior two-by-two determinant of local Mordell–Weil reductions with factorized local scalars: the actual modular-symbol derivatives already violate its mandatory Plücker identity at p=7.

Any valid uniform proof must use the **global, conductor-pair-dependent** structure of Kato's Euler system, its finite–singular comparisons and integral Fitting controls. The exact complex equality L''(E,1)/2=Ω_E Reg(E) is a separate archimedean higher-height theorem not implied by this calculation.

## Primary sources and artifact provenance

- Kim (with Pollack), *The refined Tamagawa number conjectures for GL2*, 2025, §2–§5: https://arxiv.org/pdf/2505.09121.
- Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Jan 2026, Theorem B and definitions: https://web.math.ucsb.edu/~castella/Kurihara.pdf.
- Project archive exact cusp values and earlier p=7 Kurihara witness (see §1).
- Independently executed deliverables in current conversation: `modsym_integral_389.py`, `bsd389_exact_manin_390.json`, `bsd389_p7_plucker_obstruction.py`, `p7_kurihara_fast.cpp`.

**Mathematical verdict:** exact original no-go for a natural factorized local rank-two reciprocity, not a BSD proof.
