# Independent local MW/Kurihara auxiliary arithmetic — assistant-executed Python (2026-11-02)

**Execution/provenance:** Unlike the user's historical Sage logs, the following pure-Python finite-field program was **run in the assistant's own local container during this turn**, not on the user's Ubuntu host. The assistant's scratch program computed the same elliptic group law, Legendre point counts, (N_q/p) projections and Fp discrete logs as the new committed verification source [`verification/bsd389_MW_two_auxiliary_local_determinants.py`](../verification/bsd389_MW_two_auxiliary_local_determinants.py). The new committed source **has not yet been run by the user**. The stdout below is from the assistant's local scratch computation and is reproduced verbatim; it does **not** authenticate any earlier Kurihara delta archive.

```text
MW_P_ADIC_LOCAL_TORSION_GATE_PASS p 5 a_p -3 E_Fp_order 9
MW_LOCAL_ROW_PASS p 5 q 41 a_q -3 group_order 45 cofactor 9 P_coordinate 1 Q_coordinate 3 base (4, 8)
MW_LOCAL_ROW_PASS p 5 q 61 a_q -8 group_order 70 cofactor 14 P_coordinate 1 Q_coordinate 0 base (51, 21)
MW_TWO_AUXILIARY_LOCAL_MATRIX_DETERMINANT_UNIT_PASS p 5 q1 41 q2 61 rows [(1, 3), (1, 0)] det_mod_p 2 inverse 3
MW_P_ADIC_LOCAL_TORSION_GATE_PASS p 7 a_p -5 E_Fp_order 13
MW_LOCAL_ROW_PASS p 7 q 113 a_q 9 group_order 105 cofactor 15 P_coordinate 1 Q_coordinate 3 base (100, 54)
MW_LOCAL_ROW_PASS p 7 q 673 a_q 2 group_order 672 cofactor 96 P_coordinate 1 Q_coordinate 6 base (3, 667)
MW_TWO_AUXILIARY_LOCAL_MATRIX_DETERMINANT_UNIT_PASS p 7 q1 113 q2 673 rows [(1, 3), (1, 6)] det_mod_p 3 inverse 5
MW_P_ADIC_LOCAL_TORSION_GATE_PASS p 107 a_p 0 E_Fp_order 108
MW_LOCAL_ROW_PASS p 107 q 369793 a_q 2 group_order 369792 cofactor 3456 P_coordinate 1 Q_coordinate 15 base (322785, 224156)
MW_LOCAL_ROW_PASS p 107 q 383917 a_q -854 group_order 384772 cofactor 3596 P_coordinate 1 Q_coordinate 53 base (121781, 169426)
MW_TWO_AUXILIARY_LOCAL_MATRIX_DETERMINANT_UNIT_PASS p 107 q1 369793 q2 383917 rows [(1, 15), (1, 53)] det_mod_p 38 inverse 31
MW_LOCAL_CERTIFICATE_CANONICAL_JSON_SHA256 bf92672eaeff79643788932d7172938647049567b604d2fa11a4401c610803e8
MW_LOCAL_CERTIFICATE_REPORT /tmp/bsd389_MW_local_determinants_5_7_107.json
BOUNDARY_LOCAL_INDEPENDENCE_NOT_UNIFORM_SHA_FINITE_SUPPORT
```

The local signed/normalized ratios are row-basis dependent, but their **determinant nonvanishing is invariant**. The finite p=107 local gate additionally shows (#E(F_{107})=108), hence E(Q107)[107]=0 by good reduction, as required in Kim Theorem 1.10.

The JSON digest above belongs **ONLY to the assistant's scratch script and its own canonical schema**, NOT to the separate committed GitHub script's future JSON. No claim of the latter's hash is made ahead of actual execution.

**Interpretation:** The local MW class (Pwedge Q) is a unit in each sum of two auxiliary local Kummer lines, but this is not a new all-prime Sha bound. Kim's `Sel(E[p]) ≅ sum local lines` statement under authentic degree-two `delta_n ≠ 0` and all its hypotheses would imply Sha[p∞]=0 from a certified MW rank-two basis. The degree-two delta hypotheses remain **external** to these fresh calculations.

[Exact proof, local arithmetic and conditional Kim bridge](../paper/bsd389_MW_local_two_auxiliary_determinants_and_Kim_Selmer_gate_2026-11-02.md).
