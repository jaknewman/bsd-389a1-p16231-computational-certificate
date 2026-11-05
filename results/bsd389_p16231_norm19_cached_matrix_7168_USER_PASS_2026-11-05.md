# USER PASS: exact cached matrix quaternion transport to n=7168

Date: 2026-11-05. The user executed `verification/bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py --target-n 7168 --audit-every 128 --oracle-every 512 --checkpoint-every 256` on Ubuntu under Sage, pipefail, timeout 240s, and posted the output. `NORM19_CACHED_PILOT_STATUS=0`.

Key terminal lines (genuine user execution):

```text
NORM19_FAST_BOOTSTRAP_FROM_USER_SLOW_STREAM_PASS 5410 CLASS 14
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 5504 25
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 5632 12
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 5632 CLASS 12
NORM19_FAST_CACHED_PROGRESS 5632 MOMENTS [67, 2862, 8883] CACHE_HITS 2 NEW_EDGES 220 TOTAL_EDGES 220 MAX_COORD 41238666085 ELAPSED 2.422
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 6144 29
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 6144 CLASS 29
NORM19_FAST_CACHED_PROGRESS 6144 MOMENTS [58, 14486, 10394] CACHE_HITS 12 NEW_EDGES 722 TOTAL_EDGES 722 MAX_COORD 41238666085 ELAPSED 8.878
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 6656 23
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 6656 CLASS 23
NORM19_FAST_CACHED_PROGRESS 6656 MOMENTS [26, 9715, 4512] CACHE_HITS 56 NEW_EDGES 1190 TOTAL_EDGES 1190 MAX_COORD 41238666085 ELAPSED 15.103
NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS 7168 6
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 7168 CLASS 6
NORM19_CACHED_MATRIX_EDGE_TABLE_SAVED 1642 6fbf0c2cb10a05dffb3b682b335932729c0bdebf13023fcb03cc7b12ac6a315b
NORM19_FAST_CACHED_CHECKPOINT_PASS 7168 04523cbe0eb83f4a90bafcf458a82123a8e829d75c1d647945c14508d8408167 EDGES 1642
NORM19_FAST_CACHED_PROGRESS 7168 MOMENTS [7, 1915, 5343] CACHE_HITS 116 NEW_EDGES 1642 TOTAL_EDGES 1642 MAX_COORD 41238666085 ELAPSED 20.338
NORM19_FAST_CACHED_MATRIX_PILOT_PASS 7168 CACHE_HITS 116 NEW_EDGES 1642 SECONDS 20.338
NORM19_FAST_CACHED_EDGE_UPPER_BOUND 12540
BOUNDARY_PREFIX_NOT_FULL_RINGCLASS_THETA
BOUNDARY_SHA_AND_BSD_NOT_PROVED
NORM19_CACHED_PILOT_STATUS=0
```

The run covered 1758 *new* n transitions since the n=5410 user-certified slow checkpoint. For 116 transitions, a stored exact 4x4 rational matrix was reused, and 1642 new local mod19 quaternionic neighbor edges with witnesses were discovered and saved; every new edge was explicitly constructed, matched to a canonical Brandt ideal, its witness was verified, and its matrix conjugation identity was checked. There were 14 slow-vs-fast exact oriented CM audits at steps 5504,5632,...7168 and 4 independently constructed true Gross anchors at 5632,6144,6656,7168, all passing.

Actual prefix n=0..7168 has 7169 states and raw cyclic moments [7,1915,5343] modulo 16231. This is NOT the globally summed theta quadratic coefficient. The 19-neighbor cache has at most 33*19*20=12540 possible local keys; the observed hit rate 116/1758 is only 6.6%, so do not overstate speed-up in this pilot. The fast checkpoint and edge table remain on the user's Ubuntu, not copied into this git markdown.

Next targeted audit: advance from fast checkpoint n=7168 to n=p=16231. At n=p, w^p mod p²=121898074 has principal-unit exponent zero and its independently USER-certified Gross point was class24, value0. The newly built accelerator already checks that exact anchor when target-n=16231. Use less frequent checkpoints, e.g. 1024, to avoid repeatedly serializing the growing edge cache. Full H=87809710 still requires a complete cyclic run and independent checks.
