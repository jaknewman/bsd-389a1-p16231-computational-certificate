# Actual user PASS: 1,000,001 genuinely oriented Gross P2 states, Boost native / Sage quaternionic hybrid

**Date:** 2026-11-05. User shared 264 lines of actual Sage Ubuntu stdout. Ran `verification/bsd389_p16231_norm19_native_exact_stream.py --target-n 1000000 --checkpoint-every 65536 --oracle-every 65536 --teich-crosscheck` with `timeout 1200s` and `set -o pipefail`. Final shell exit `NORM19_NATIVE1M_STATUS=0`.

## Decisive original terminal output

```text
NORM19_NATIVE_CPP_COMPILED_PASS abccc9a5c1b855949cd6a0653535d42cd039c987091793eedccb9a6ef5eeca98
NORM19_NATIVE_EXACT_CHECKPOINT_RESTORED_PASS 50000 EDGE_KEYS 11967
NORM19_NATIVE_REGISTER_CERTIFIED_MATRIX_EDGES 11967
NORM19_NATIVE_EXISTING_COMPLETE_TEICH_ORBIT_RECHECK_PASS [0, 10775, 5515]
NORM19_NATIVE_EXACT_PROGRESS 65536 OF 87809709 MOMENTS [80, 15677, 12936] EDGE_KEYS 12216 NEW_EDGES 249 EXACT_NATIVE_STEPS 15536 SECONDS 3.436
NORM19_NATIVE_EXACT_PROGRESS 131072 OF 87809709 MOMENTS [35, 6793, 14282] EDGE_KEYS 12309 NEW_EDGES 342 EXACT_NATIVE_STEPS 81072 SECONDS 4.647
NORM19_NATIVE_EXACT_PROGRESS 196608 OF 87809709 MOMENTS [398, 14954, 6535] EDGE_KEYS 12312 NEW_EDGES 345 EXACT_NATIVE_STEPS 146608 SECONDS 4.852
NORM19_NATIVE_EXACT_PROGRESS 262144 OF 87809709 MOMENTS [915, 7580, 4668] EDGE_KEYS 12312 NEW_EDGES 345 EXACT_NATIVE_STEPS 212144 SECONDS 5.044
NORM19_NATIVE_EXACT_PROGRESS 524288 OF 87809709 MOMENTS [47, 3570, 3244] EDGE_KEYS 12312 NEW_EDGES 345 EXACT_NATIVE_STEPS 474288 SECONDS 5.74
NORM19_NATIVE_EXACT_PROGRESS 786432 OF 87809709 MOMENTS [15162, 1777, 8657] EDGE_KEYS 12312 NEW_EDGES 345 EXACT_NATIVE_STEPS 736432 SECONDS 6.438
NORM19_NATIVE_EXACT_CHECKPOINT_PASS 1000000 MOMENTS [15895, 649, 12670] EDGES 12312 SHA256 217de37be4d8235efab33d1e8da65cfcc29ddab8c9363292171889998c62a743
NORM19_NATIVE_EXACT_PROGRESS 1000000 OF 87809709 MOMENTS [15895, 649, 12670] EDGE_KEYS 12312 NEW_EDGES 345 EXACT_NATIVE_STEPS 950000 SECONDS 7.19
NORM19_NATIVE_EXACT_PREFIX_PASS 1000001 MOMENTS [15895, 649, 12670] EDGE_KEYS 12312
BOUNDARY_FULL_87809710_CLASS_SUM_NOT_YET_COMPUTED
NORM19_NATIVE_HYBRID_DRIVER_PASS 1000000 NEW_EDGES 345 SECONDS 7.19
NORM19_NATIVE1M_STATUS=0
```

## Correct interpretation

- The last real n=50000 exact native/Sage checkpoint was restored and the C++ engine advanced 950000 genuinely oriented CM Gross states with no nonintegral exact matrix division.
- Only 345 new mod19 quaternion edge keys were learned over the 950000-step run, all by genuine Sage right ideal equivariance certificate. The cache reached 12312 keys already by step n=196608 and stayed at that size through n=1,000,000. The proven *upper bound* on the number of possible keys is 33*19*20=12540; 228 possible keys are not yet learned, and cache saturation beyond this prefix is not proven.
- All 15 direct p4 Gross orientation anchor controls at n=65536,131072,...,983040 were reported PASS. Every encountered decimated norm19 n=5410 t point was also checked against the 16231-point independently computed original Teich orbit, from n=54100 to 995440 inclusive, with no failures.
- The exact partial raw moments of **n=0..1,000,000** are [15895,649,12670] modulo p=16231, **not** yet the full H=87809710 ring-class theta sum.
- The authenticated native checkpoint SHA256 is 217de37be4d8235efab33d1e8da65cfcc29ddab8c9363292171889998c62a743. The native edge table is saved separately under `~/bsd389_p16231_norm19_native_exact_edges.json`.
- Even with exact total raw moments and theta c2 nonzero, rigorous infinite theta order and any deduction about Sha or full BSD require additional theorem hypotheses and analytic normalization checks.

Next move: safely run toward n=H-1=87809709 using authenticated checkpoints, infrequent direct Gross anchors and exhaustive existing original-Teich decimated checks. Add a separate exact ring-class closure audit at the finish: w^H=213756225 modulo p², a nontrivial global cube root of unity, so the next norm19 step should return to the same Brandt class as original P2(1) (class9) even though the unit parameter is not numerically 1. This is the correct closure test modulo mu3.
