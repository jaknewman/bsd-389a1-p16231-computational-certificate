# E389a1: actual p16231 norm-19 Gross P2 orientation and exact ideal-identity PASS

**Date:** 2026-11-05. Authentic stdout pasted by the user from their Sage Ubuntu execution (timeout 240 seconds, pipefail) of [verification/bsd389_p16231_P2_norm19_one_step_adelic_transport.py](../verification/bsd389_p16231_P2_norm19_one_step_adelic_transport.py).

```text
P2_HENSEL_SPLIT_ROOTS_P4_PASS 56587842034940534 12815616197479786
P2_P4_LOCAL_IDEMPOTENTS_PASS
P2_P4_LOCAL_MATRIX_UNITS_PASS 0 0 46268972154137631
P2_P4_LOCAL_16_PRODUCTS_PASS
P2_P4_SPLIT_LIFTS_CERTIFIED_P2_CHART_PASS 389
P2_NORM19_CRT_GALOIS_RATIO_PASS 138112843 56004792
P2_GROSS_UNIT_PARAMETER 1
P2_CONGRUENCE_KERNEL_INDEX_P8_PASS
P2_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS
P2_RIGHT_IDEAL_CLOSURE_16_PASS
P2_GLOBAL_RIGHT_BRANDT_IDEAL_PASS
P2_GROSS_UNIT_PARAMETER 138112843
P2_CONGRUENCE_KERNEL_INDEX_P8_PASS
P2_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS
P2_RIGHT_IDEAL_CLOSURE_16_PASS
P2_GLOBAL_RIGHT_BRANDT_IDEAL_PASS
P2_GROSS_UNIT_PARAMETER 56004792
P2_CONGRUENCE_KERNEL_INDEX_P8_PASS
P2_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS
P2_RIGHT_IDEAL_CLOSURE_16_PASS
P2_GLOBAL_RIGHT_BRANDT_IDEAL_PASS
P2_CONDUCTOR_P2_Q_IN_LEFT_ORDER_PASS
P2_NORM19_SPLIT_ROOTS_PASS 9 4
P2_NORM19_ORIENTED_NEIGHBOR_INDEX_361_PASS G 9
P2_NORM19_GLOBAL_MULTIPLIER_EQUALITY G True
P2_NORM19_RIGHT_EQUIVALENCE_WITNESS_PASS G ROOT 9
P2_NORM19_EXPLICIT_GLOBAL_TRANSPORT_PASS G
P2_NORM19_ORIENTED_NEIGHBOR_INDEX_361_PASS G_CONJUGATE 4
P2_NORM19_GLOBAL_MULTIPLIER_EQUALITY G_CONJUGATE True
P2_NORM19_RIGHT_EQUIVALENCE_WITNESS_PASS G_CONJUGATE ROOT 4
P2_NORM19_EXPLICIT_GLOBAL_TRANSPORT_PASS G_CONJUGATE
P2_NORM19_ONE_STEP_JSON /home/bsdadmin/bsd389_p16231_P2_norm19_one_step_transport.json
P2_NORM19_ONE_STEP_BOTH_DIRECTIONS_PASS
BOUNDARY_NO_THETA_SUM_OR_ALL_19_CYCLE_COMPUTATION
NORM19_TRANSPORT_STATUS=0
```

## Exact certified content

At conductor m=p²=263445361, p=16231, K=Q(sqrt(-3)), use genuine Gross right ideal T(a)=J2(a)*I32 based on a conductor-one globally optimal CM embedding omega. Let g=5+3omega, gbar=2-3omega, Norm g=19. The r_2(1) left order L contains q=m*omega. Split 19 roots of q²+mq+m² modulo19: 9 (g) and 4 (gbar). For J_r=L.left_ideal([q-r,19]) of index 19², user Sage verified the following **strict equalities of rational right-ideal lattices**, not just equivalence classes:

(g/19) * conjugate(J_9) * T(1) = T(138112843),
(gbar/19) * conjugate(J_4) * T(1) = T(56004792).

Both independently constructed target Gross right ideals were verified by mod-p4 local matrix chart, exact HNF, index p8, 16 right-ideal closure checks, plus independent right-equivalence witnesses. Both exact candidate multipliers passed.

The target 138112843 is the exact norm19 split CRT Galois ratio w(g) modulo p², and 56004792 its inverse.

**Scope:** proven as actual executions for a=1 in two directions. A general all-a formula is not certified by this particular finite test alone. Even if a formula is established algebraically, class values across all H=87809710 ring classes and full theta moments are not computed. No theta order-two, Sha finiteness, or BSD claim is warranted.
