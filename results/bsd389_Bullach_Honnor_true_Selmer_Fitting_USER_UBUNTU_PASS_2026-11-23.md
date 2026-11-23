# 389a1 — User Ubuntu genuine Bullach–Honnor Selmer-Fitting arithmetic-input gate PASS

**Date:** 2026-11-23. **Evidence:** exact terminal output supplied directly by the user after running `python -u verification/bsd389_Bullach_Honnor_real_Selmer_Fitting_bridge_gate.py` in the Ubuntu `sage` Conda environment.

```text
TRUE_MAZUR_TATE_THETA_ORDER_TWO_MOD_P_PASS p 5 depth_k 1 conductor 2501 Taylor_coefficients [0, 0, -166] reduced_mod_p [0, 0, 4] minimal_degree 2
BULLACH_HONNOR_THM_1_4_PLUS_LOCAL_FITTING_NAKAYAMA: Fitt0(Sel_p_infty(K)^dual) subset maximal_ideal^d theta_notin_maximal_ideal^3 therefore_d_le_2
RESIDUAL_GL2_PLUS_INFLATION_RESTRICTION: dim_Sel(E[p]/Q)=2+dim_Sha(Q)[p] <= d <= 2 therefore_Sha[p]=0 by the published theorem
TRUE_MAZUR_TATE_THETA_ORDER_TWO_MOD_P_PASS p 11 depth_k 1 conductor 393427 Taylor_coefficients [0, -3102, -12462] reduced_mod_p [0, 0, 1] minimal_degree 2
BULLACH_HONNOR_THM_1_4_PLUS_LOCAL_FITTING_NAKAYAMA: Fitt0(Sel_p_infty(K)^dual) subset maximal_ideal^d theta_notin_maximal_ideal^3 therefore_d_le_2
RESIDUAL_GL2_PLUS_INFLATION_RESTRICTION: dim_Sel(E[p]/Q)=2+dim_Sha(Q)[p] <= d <= 2 therefore_Sha[p]=0 by the published theorem
TRUE_MAZUR_TATE_THETA_ORDER_TWO_MOD_P_PASS p 5 depth_k 2 conductor 56993501 Taylor_coefficients [0, -404300, -5067478] reduced_mod_p [0, 0, 2] minimal_degree 2
BULLACH_HONNOR_THM_1_4_PLUS_LOCAL_FITTING_NAKAYAMA: Fitt0(Sel_p_infty(K)^dual) subset maximal_ideal^d theta_notin_maximal_ideal^3 therefore_d_le_2
RESIDUAL_GL2_PLUS_INFLATION_RESTRICTION: dim_Sel(E[p]/Q)=2+dim_Sha(Q)[p] <= d <= 2 therefore_Sha[p]=0 by the published theorem
TRUE_PRIMEWISE_SELmer_FITTING_BRIDGE_ARITHMETIC_INPUTS_PASS
BOUNDARY_BULLACH_HONNOR_IS_EXTERNAL_PUBLISHED_THEOREM
BOUNDARY_NO_NEW_ALL_LARGE_P_UNIT_OR_GLOBAL_SHA_FINITE
```

**Interpretation:** the executable checks the three full true integer theta Taylor coefficient vectors and prints the *mathematical implication* through an external published theorem. It does NOT compute Sel(E/K,p∞) or Sha(E/K) directly, and the result `Sha(E/Q)[p∞]=0` at p5/11 was already independently established through existing methods. The precise theorem is Bullach–Honnor, *On the refined 'Birch–Swinnerton-Dyer type' conjectures of Mazur and Tate*, arXiv:2511.07203 v1, Theorem 1.4(b), Hypothesis 1.2, printed page2 (primary author manuscript https://arxiv.org/pdf/2511.07203), confirmed directly by mathematical source audit. 

The complete arithmetic proof at p-fixed is recorded in `paper/bsd389_Bullach_Honnor_true_Selmer_Fitting_Kurihara_quadratic_bridge_2026-11-23.md`.

**Important boundary:** neither this output nor the Fitt0 inclusion proves existence of a p-unit quadratic theta coefficient for every large p, global Sha finiteness or the rank-two exact BSD leading coefficient.
