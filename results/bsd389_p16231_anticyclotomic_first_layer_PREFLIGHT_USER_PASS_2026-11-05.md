# Authentic Ubuntu first anticyclotomic layer preflight PASS — E389a1, p=16231

**Date:** 2026-11-05. **Provenance:** pasted stdout from user's activated Sage Ubuntu shell, running the committed standard-library verifier [bsd389_p16231_anticyclotomic_first_layer_preflight.py](../verification/bsd389_p16231_anticyclotomic_first_layer_preflight.py). The assistant did not run or obtain the user's original local log directly.

## Verbatim stdout

```text
K_MINUS3_P16231_SPLIT_ROOTS_MODP_PASS [6044, 10186]
K_MINUS3_P16231_HENSEL_ROOTS_MODP2_PASS [49689135, 213756225]
K_MINUS3_RINGCLASS_CONDUCTOR_P_ORDER_PASS 5410
K_MINUS3_RINGCLASS_CONDUCTOR_P2_ORDER_PASS 87809710
K_MINUS3_FIRST_P_PRIMARY_QUOTIENT_AT_P2_PASS 16231
LOCAL_PRINCIPAL_UNIT_CYCLIC_ORDER_P_PASS
E389A1_ALPHA_INVERSE_SQUARED_MODP_PASS 4986
CH_THETA_N1_RAW_TWO_INDEX_EVALUATION_COUNT 263429130
THETA_GROSS_POINT_AGGREGATES_NOT_PROVIDED
BOUNDARY_CH_THETA_CHARACTERS_TRIVIAL_NOT_CHI53
BOUNDARY_ORD_T_THETA_EQUALS_2_NOT_PROVED
ANTICYCLOTOMIC_FIRST_LAYER_PREFLIGHT_PASS
PREFLIGHT_STATUS=0
```

## Mathematical scope

K=Q(sqrt(-3)), p=16231 splits. The unit roots of omega²+omega+1 modulo p and their Hensel lifts modulo p² are validated exactly. The conductor-p ring class group has order 5410, prime to p; conductor p² has order 87,809,710=5410*p. Therefore the kernel of the natural reduction map Pic(O_(p²))→Pic(O_p) has order p, giving the first nontrivial p-primary layer. For E389a1, a_p=128, so alpha_p^(−2) mod p equals 4986.

This does **not** produce a single Gross-point class label P_1^a or P_2^a. The brute force finite n=1 theta formula contains 263,429,130 summands, but no such sum was executed. The relevant Castella–Hsieh theta is the *trivial-character* theta Theta_(f/K,1), not the old order-nine ring-class character of conductor 53.

**New next arithmetic step:** [exact local CRT norm-19 generator of first p-primary layer](../verification/bsd389_p16231_ringclass_norm19_first_layer_generator.py), newly published and independently spot/exhaustively checked in the assistant's Python working environment; **NOT YET USER EXECUTED**. It is a group-theoretic generator, not a substitute for quaternionic Gross-point or theta computation.

No proof of theta order 2, Sha p16231 finiteness or global BSD is claimed from this preflight.
