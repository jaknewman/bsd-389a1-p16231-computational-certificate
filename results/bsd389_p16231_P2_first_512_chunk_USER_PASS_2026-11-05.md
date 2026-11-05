# Real Ubuntu PASS: 512 exact conductor-one anticyclotomic P2 Gross points, p=16231

**Date:** 2026-11-05. **Source:** actual user stdout from Sage Ubuntu. The source program is [verification/bsd389_p16231_P2_u_orbit_chunked_moments.py](../verification/bsd389_p16231_P2_u_orbit_chunked_moments.py), with `--residue 1 --start 0 --count 512 --mu3-check`. Exit `P2_CHUNK_STATUS=0`.

## User-certified output

```text
P2_HENSEL_SPLIT_ROOTS_P4_PASS 56587842034940534 12815616197479786
P2_P4_LOCAL_IDEMPOTENTS_PASS
P2_P4_LOCAL_MATRIX_UNITS_PASS 0 0 46268972154137631
P2_P4_LOCAL_16_PRODUCTS_PASS
P2_P4_SPLIT_LIFTS_CERTIFIED_P2_CHART_PASS 389
P2_MU3_GLOBAL_CM_UNIT_CLASS_SYMMETRY_PASS I 0 CLASS 9 VALUE -1
P2_MU3_GLOBAL_CM_UNIT_CLASS_SYMMETRY_PASS I 1 CLASS 15 VALUE -1
P2_MU3_GLOBAL_CM_UNIT_CLASS_SYMMETRY_PASS I 2 CLASS 21 VALUE 1
P2_MU3_REDUCES_TEICH_REPRESENTATIVES 16230 TO 5410
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 63 DONE 64 OF 512 SECONDS 1.694
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 127 DONE 128 OF 512 SECONDS 3.054
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 191 DONE 192 OF 512 SECONDS 4.214
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 255 DONE 256 OF 512 SECONDS 5.32
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 319 DONE 320 OF 512 SECONDS 6.791
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 383 DONE 384 OF 512 SECONDS 8.358
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 447 DONE 448 OF 512 SECONDS 9.844
P2_CHUNK_PROGRESS RESIDUE 1 LAST_I 511 DONE 512 OF 512 SECONDS 10.926
P2_EXACT_CHUNK_CERTIFICATE /home/bsdadmin/bsd389_p16231_P2_u_orbit_chunk_certificates/r1_i00000_00512.json
P2_EXACT_CHUNK_SHA256 2a12796dd1fd56351e82c2337c02d74d578ab87fa01f40c564dc37c79ad66db5
P2_EXACT_CHUNK_MOMENTS_MODP [16213, 12726, 5996]
P2_EXACT_CHUNK_PASS 1 0 512
BOUNDARY_CHUNK_NOT_COMPLETE_I_OR_A_SUM_UNLESS_ALL_RECORDED
P2_CHUNK_STATUS=0
```

## Exact significance and boundary

512 distinct genuine conductor-one P2 points are certified via Hensel p4 local split, two mod-p4 congruences, index p8 HNF from independent constructions, right-ideal closure and exact Brandt equivalence witness for each. The quaternionic global CM unit of order three predicts class equality for a,lambda*a,lambda²*a; the user independently checked the nine actual ideals for i=0,1,2 and got classes 9,15,21, with equal triples and no mismatches.

The vector of moments [16213,12726,5996] is a **PARTIAL** range i=0..511 (mod 16231), for Teich residue 1. It is not the full i=0..16230 orbit, does not include the 5410 Teich residue orbits modulo mu3, and does not prove the theta order-two criterion or p-primary Sha finiteness. The source output is pinned with exact SHA256 above. The initial file is already present on the user's host and must not be overwritten during the remaining orbit.
