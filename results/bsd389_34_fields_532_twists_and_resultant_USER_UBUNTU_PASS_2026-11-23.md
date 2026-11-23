# 389a1 — user Ubuntu verification of 34-field combinatorics and exact normalized-resultant control

**Date:** 2026-11-23. **Execution:** user's Sage-Conda Ubuntu terminal, Python. Output copied exactly from the user, not synthesized.

## 34 fields / 532 characters — user log

```text
KURIHARA_UNIT_GIVES_RANK_STABLE_CYCLIC_FIELDS_PASS p 5 k 1 q1 41 q2 61 delta 4 degree 5 fields 4 distinct_twists 16 conductor 2501
KURIHARA_UNIT_GIVES_RANK_STABLE_CYCLIC_FIELDS_PASS p 11 k 1 q1 397 q2 991 delta 1 degree 11 fields 10 distinct_twists 100 conductor 393427
KURIHARA_UNIT_GIVES_RANK_STABLE_CYCLIC_FIELDS_PASS p 5 k 2 q1 5351 q2 10651 delta 22 degree 25 fields 20 distinct_twists 416 conductor 56993501
BSD389_TOTAL_EXPLICIT_REAL_CYCLIC_FIELDS_NO_MW_GROWTH 34
BSD389_TOTAL_DISTINCT_NONZERO_TWIST_L_CENTRAL_VALUES 532
EXTERNAL_KATO_PLUS_NO_ISOGENY_IMPLICATION: MW_UNCHANGED_IN_ALL_34_FIELDS
BOUNDARY_NO_SHA_GLOBAL_FINITE_AND_NO_EXACT_COMPLEX_RANK2_BSD
```

Program: `verification/bsd389_kurihara_unit_twist_field_counts_gate.py`. This enumerates the characters and evaluates their arithmetic index/cardinality conditions. Its statement about exact Mordell–Weil groups over number fields is a **conditional mathematical implication using external published Kato rank-zero theory and absence of isogenies**, not a direct computation of Mordell–Weil points over these 34 fields.

## Normalized resultant Boolean test — user log

```text
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 1 c2 4 resultant_digits 6 normalized_modp 1 expected 1
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 1 c2 5 resultant_digits 6 normalized_modp 0 expected 0
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 1 c2 0 resultant_digits 6 normalized_modp 0 expected 0
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 11 k 1 c2 1 resultant_digits 15 normalized_modp 1 expected 1
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 11 k 1 c2 11 resultant_digits 15 normalized_modp 0 expected 0
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 11 k 1 c2 0 resultant_digits 15 normalized_modp 0 expected 0
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 2 c2 22 resultant_digits 41 normalized_modp 1 expected 1
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 2 c2 5 resultant_digits 43 normalized_modp 0 expected 0
EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS p 5 k 2 c2 0 resultant_digits 45 normalized_modp 0 expected 0
RESULTANT_THEOREM_SCOPE: true theta quadratic jet comes from Hecke
BOUNDARY: NOT A PRIME-INDEPENDENT SHA ANNIHILATOR
```

Program: `verification/bsd389_normalized_resultant_boolean_gate.py`. This actually computes **synthetic** integer-polynomial resultants for both unit and nonunit quadratic coefficients and confirms the algebraic theorem; it does **not** compute the potentially enormous actual full `Res(S_m,F_r)` from 28 million genuine Manin terms, which is mathematically unnecessary once the low-jet theorem is proved.

External rank-zero source independently checked: Kato Corollary 14.3 as discussed by Koji Matsuda, *Research in Number Theory* (2023), Lemma 3.1 and Corollary 3.2, https://link.springer.com/article/10.1007/s40993-023-00430-4 . The one-way implication L(f,1)≠0 ⇒ rank A_f(Q)=0 is valid; the converse is not known in general and **must not be used**.

**Boundary:** No prime-independent integer D with (D)⊂Fitt2(X_p) for every p, no uniform all-large-p Kurihara unit, and no exact complex rank-two BSD leading-term theorem follow from this user run.
