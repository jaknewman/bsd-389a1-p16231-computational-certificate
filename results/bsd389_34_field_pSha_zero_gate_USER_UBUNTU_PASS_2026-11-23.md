# 389a1 — user Ubuntu independent 34-cyclic-field p-Sha-vanishing theorem premises PASS

**Date:** 2026-11-23; source is the user's exact terminal output from `sage` Conda Ubuntu; verified mathematical conditions are the authentic p-unit quadratic Mazur–Tate low-jet inputs from three previously independent full Manin-vector calculations. The program **does not compute 34 Sha groups**; its p-Sha vanishing printout refers to a *published* Bullach–Honnor theorem plus the rigorously proved local Fitting/minor lemma.

```text
GENUINE_34_FIELD_THETA_P_UNIT_LEADING_ORDER_PASS p 5 k 1 n 2501 delta 4 field_count 4 all_unit_choices [4, 3, 2, 1]
EXTERNAL_BULLACH_HONNOR_A_PLUS_B_AND_UNIT_MINOR_LEMMA: Selmer_dual_over_K_is_Zp_squared Sha(E/K)[p_infinity]=0
GENUINE_34_FIELD_THETA_P_UNIT_LEADING_ORDER_PASS p 11 k 1 n 393427 delta 1 field_count 10 all_unit_choices [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EXTERNAL_BULLACH_HONNOR_A_PLUS_B_AND_UNIT_MINOR_LEMMA: Selmer_dual_over_K_is_Zp_squared Sha(E/K)[p_infinity]=0
GENUINE_34_FIELD_THETA_P_UNIT_LEADING_ORDER_PASS p 5 k 2 n 56993501 delta 22 field_count 20 all_unit_choices [2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3]
EXTERNAL_BULLACH_HONNOR_A_PLUS_B_AND_UNIT_MINOR_LEMMA: Selmer_dual_over_K_is_Zp_squared Sha(E/K)[p_infinity]=0
REAL_34_FIELDS_PPRIMARY_SHA_ZERO_THEOREM_PREMISES_PASS 34
BOUNDARY_EXTERNAL_FITTING_THEOREM_AND_UNIT_MINOR_LEMMA_ARE_MATHEMATICAL_INPUTS
BOUNDARY_NO_ALL_LARGE_P_WITNESSES_OR_GLOBAL_SHA_FINITE
```

**Original mathematical reference independently checked against its primary PDF and screenshots:** Dominik Bullach and Matthew Honnor, *On the refined “Birch–Swinnerton-Dyer type” conjectures of Mazur and Tate*, arXiv:2511.07203v1 (10 Nov 2025), Theorem 1.4(a,b), Hypothesis 1.2 and Remark 1.5(a), https://arxiv.org/pdf/2511.07203. The theorem proves theta in the *true p-primary Selmer dual's* Fitting ideal without assuming Sha finiteness. Its Mazur–Tate modular-symbol normalization differs from the standard even plus-symbol convention only by a factor of 2, a p-unit for p=5,11, as confirmed by Definition 2.2 and Remark 2.3(b).

**Boundaries:** The source test checks real low-jet arithmetic and finite algebra, not the published theorem itself. It is **not an all-p Sha finiteness theorem** and does not prove exact rank-two complex BSD.
