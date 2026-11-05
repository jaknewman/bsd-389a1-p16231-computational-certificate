# Genuine conductor-1 CM base and p=16231 local maximal-order split — USER PASS (2026-11-05)

**Provenance:** Exact terminal output supplied by the user from the Sage-enabled Ubuntu machine. The assistant did not run Sage on that host or access the private JSON output directly.

**Script:** [verification/bsd389_p16231_conductor1_CM_base_and_local_split.py](../verification/bsd389_p16231_conductor1_CM_base_and_local_split.py)

```text
CONDUCTOR1_CM_BRANDT_WEIGHT_HISTOGRAM {1: 32, 3: 1}
CONDUCTOR1_CM_ORDER_FOUND 32 ROOTS 2 UNITS 6 BRANDT_WEIGHT 3
CONDUCTOR1_CM_GLOBAL_EMBEDDINGS_PASS 2 ORDERS 1
CONDUCTOR1_CM_SELECTED_OPTIMAL_EMBEDDING_PASS 32 [-1, 153, -27, -64]
CONDUCTOR1_CM_LOCAL_IDEMPOTENTS_PASS
CONDUCTOR1_CM_LOCAL_MATRIX_UNITS_PASS 0 0 174820991
CONDUCTOR1_CM_LOCAL_16_PRODUCT_IDENTITIES_PASS
CONDUCTOR1_CM_LOCAL_M2_ISOMORPHISM_PASS 389
CONDUCTOR1_CM_JSON_REPORT /home/bsdadmin/bsd389_p16231_conductor1_CM_base_and_local_split.json
CONDUCTOR1_CM_GLOBAL_AND_P_LOCAL_SPLIT_PASS
BOUNDARY_PPOWER_GROSS_POINT_CLASSES_NOT_YET_COMPUTED
BOUNDARY_THETA_DERIVATIVE_AND_SHA_NOT_PROVED
CM_BASE_STATUS=0
```

## Conclusions justified by the run

The monodromy-weight histogram for the 33 Brandt ideal classes is exactly {1:32,3:1}; the unique order with weight 3 is left order of ideal index 32 and has six norm-1 units. The complete exact unit enumeration finds two roots omega of omega^2+omega+1=0 in that maximal order. In the chosen order basis, a root has coordinates [-1,153,-27,-64], certifying an optimal global embedding of **the maximal quadratic integer order** O_K=Z[omega] for K=Q(sqrt(-3)). This is a different embedding from the historical conductor-53 orbit.

The same user run builds exact local matrix units for R_32 mod p^2 (p=16231), verifies 16 multiplication identities and invertible basis determinant 389. It outputs the matrix-coordinate map at /home/bsdadmin/bsd389_p16231_conductor1_CM_base_and_local_split.json. The code's finite arithmetic checks certify a local algebra isomorphism R_32 tensor Z/p^2 -> M_2(Z/p^2), with omega mapped to diag(49689135,213756225).

**Boundary:** this establishes a conductor-one CM base and split local quaternion chart. It does not yet map actual Gross adelic points at conductor p or p^2 to Brandt class indices, and does not compute an anticyclotomic theta coefficient, Selmer upper bound, Sha finiteness or BSD. The published n=1 theta formula involves distinct conductor-p-adic local Gross points with further orientation and normalization hypotheses.

The appropriate next algorithm is to use an exact right-ideal lattice or Hecke-neighbor operation to classify a small set of CM points from this base, checking that p-primary class labels align with the previously certified norm-19 generator. The finite conductor-53 orbit is NOT substituted for the conductor-one data.
