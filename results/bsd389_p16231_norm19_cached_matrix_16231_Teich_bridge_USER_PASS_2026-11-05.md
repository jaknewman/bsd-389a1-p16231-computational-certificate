# Actual USER PASS: 16231th norm19 Gross-point step, full Teich anchor class 24

**Date:** 2026-11-05. User executed in Sage Ubuntu:

```bash
timeout 240s python -u verification/bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py \
  --target-n 16231 --audit-every 512 --oracle-every 2048 \
  --checkpoint-every 1024 2>&1 | tee ~/bsd389_p16231_cached_norm19_pstep.log
echo "NORM19_CACHED_PSTEP_STATUS=$?"
```

Selected authentic output:

```text
NORM19_CACHED_MATRIX_EDGES_RESTORED 1642
NORM19_FAST_CACHED_CHECKPOINT_RESTORED 7168
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 7680 28
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 8192 0
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 8192 CLASS 0
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 10240 28
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 10240 CLASS 28
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 12288 2
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 12288 CLASS 2
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 14336 19
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 14336 CLASS 19
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 16231 CLASS 24
NORM19_FAST_TEICH_P_STEP_PASS 16231 A 121898074 CLASS 24
NORM19_CACHED_MATRIX_EDGE_TABLE_SAVED 7216 111ea4dfc9109dc8cabef4d44e6fc74543ce139394e3e070cf8adfc9f5c7c3f1
NORM19_FAST_CACHED_CHECKPOINT_PASS 16231 36c1e557221416bc943fd5ab1637a90c1d2b149fe330f7f8f7c32087d89f6a95 EDGES 7216
NORM19_FAST_CACHED_PROGRESS 16231 MOMENTS [33, 348, 11277] CACHE_HITS 3489 NEW_EDGES 5574 TOTAL_EDGES 7216 MAX_COORD 41240234533 ELAPSED 68.801
NORM19_FAST_CACHED_MATRIX_PILOT_PASS 16231 CACHE_HITS 3489 NEW_EDGES 5574 SECONDS 68.801
NORM19_FAST_CACHED_EDGE_UPPER_BOUND 12540
BOUNDARY_PREFIX_NOT_FULL_RINGCLASS_THETA
BOUNDARY_SHA_AND_BSD_NOT_PROVED
NORM19_CACHED_PSTEP_STATUS=0
```

This run restored the exact n=7168 4x4 rational matrix edge table and normalized oriented state. It computed 9063 new Gross points through n=p=16231, reusing 3489 exact cached transitions and constructing 5574 new keys. All periodic genuine Sage slow oriented quaternion ideal-transport audits and independent direct p4 local Gross anchors passed.

At n=p the principal-unit coordinate i_n=10816 n modulo p is zero; w^p modp² =121898074, its Teich component. Direct P2(121898074) was independently classified as Brandt index24, value0 in the earlier five-anchor user PASS, and this fast run re-verified its exact oriented embedding.

The prefix through n=p (inclusive) has 16232 points with raw moments (33,348,11277) modulo16231; the native speedup has **not** computed the full H=87809710 class cycle. The cache upper bound 12540 applies to possible mod19 q reductions, while observed 7216 unique edges have been learned. Source-file provenance and sha256 of cache/checkpoint are recorded. Avoid claiming exact theta global coefficient, order2, or any Sha theorem.
