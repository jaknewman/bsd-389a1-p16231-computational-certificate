# C01/Shapiro exact Manin and high-p direct Sage exceptional oracle — PASS

**Date:** 2026-10-26. **Observed provenance:** output supplied by user from Sage-enabled Ubuntu IONOS. Two independent scripts executed successfully and both Bash pipeline exit vectors were `0 0`.

## 1. Exact rational divisor/transport audit

Program: `verification/audit_c01_exact_manin_cusps_and_exceptional_cosets.py`.

```text
EXACT_MANIN_390_CUSP_DIVISOR_IDENTITIES_PASS
EXACT_MANIN_2012_TERMS_DET_ONE_PASS
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 0 {'gen': 1, 'rel': 1, 'e0': 0, 'e1': 0}
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 38 {'gen': 1, 'rel': 10, 'e0': 0, 'e1': 1}
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 67 {'gen': 3, 'rel': 6, 'e0': 1, 'e1': 66}
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 16234 {'gen': 2, 'rel': 5, 'e0': 0, 'e1': 0}
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 131714565 {'gen': 1, 'rel': 2, 'e0': 0, 'e1': 0}
EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS 263429129 {'gen': 1, 'rel': 2, 'e0': 0, 'e1': 0}
EXACT_SHAPIRO_E0_E1_BRANCHES_PASS
EXACT_C01_MANIN_SHAPIRO_ORIENTATION_AUDIT_PASS
BOUNDARY: independent exact algebra, not a Sage n3 numerical oracle
EXACT_STATUS=0 0
```

## 2. Direct Sage/eclib versus immutable executable at p=16231

Program: `verification/independent_c01_shapiro_exceptional_sage_oracle.py`. For each pair, independently computes all 16,231 weighted level-3 modular symbols and compares the local scalar against the SHA-pinned saved C++ full-J executable.

```text
HIGH_P_ADVERSARIAL_EXCEPTIONAL_IDS {'e0': 67, 'e1': 38} id_67 {'gen': 3, 'rel': 6, 'e0': 1, 'e1': 66}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 0 direct 2316 native 2316 branches {'gen': 1, 'rel': 1, 'e0': 0, 'e1': 0}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 38 direct 6198 native 6198 branches {'gen': 1, 'rel': 10, 'e0': 0, 'e1': 1}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 67 direct 8719 native 8719 branches {'gen': 3, 'rel': 6, 'e0': 1, 'e1': 66}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 16234 direct 11725 native 11725 branches {'gen': 2, 'rel': 5, 'e0': 0, 'e1': 0}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 131714565 direct 10993 native 10993 branches {'gen': 1, 'rel': 2, 'e0': 0, 'e1': 0}
HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS id 263429129 direct 2316 native 2316 branches {'gen': 1, 'rel': 2, 'e0': 0, 'e1': 0}
HIGH_P_DIRECT_SAGE_EXCEPTIONAL_E0_E1_ORACLE_PASS
BOUNDARY: sampled adversarial high-p local check, not full direct Sage n3.
ADVERSARIAL_STATUS=0 0
```

The independent exact arithmetic oracle verified 390/390 rational cusp-divisor identities and all 2012 relation terms. The direct Sage n=3 pair oracle then succeeded in all six single-pair comparisons, including both exceptional branch types at ids 38 and 67.

**Interpretation:** This is independent, adversarial, high-p local verification of the C01/Shapiro source-to-J reference identification. It is not a formal proof of the full domain and not a full direct 263,429,130-pair Sage n=3 evaluation. The full domain was evaluated twice by the archived V19 C01 and independent dual-scalar C++ methods; both rely on audited original Manin relations and shared V65/eclib input table. The mathematical inference to the p-primary Sha bound still depends on exact source-level C01/Sage normalization, p-adic regulator, and Kato/Sage hypotheses. Exact p-adic u=1 and full BSD are not proved.

Sources: [formal C01/Shapiro duality](../paper/c01_shapiro_formal_duality_and_exceptional_audit_2026-10-26.md), [direct Sage oracle script](../verification/independent_c01_shapiro_exceptional_sage_oracle.py), [exact algebra script](../verification/audit_c01_exact_manin_cusps_and_exceptional_cosets.py), [whole scalar J PASS](independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md).
