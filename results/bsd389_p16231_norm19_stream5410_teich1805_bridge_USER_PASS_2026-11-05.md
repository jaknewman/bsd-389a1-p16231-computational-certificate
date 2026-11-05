# Exact user-replayed norm19 reduced CM cyclic stream n=5410, bridge to certified Teich orbit index 1805

**2026-11-05.** User ran `verification/bsd389_p16231_P2_norm19_cyclic_checkpoint_stream.py --target-n 5410 --oracle-every 512 --checkpoint-every 256 --bridge-5410` in Sage on Ubuntu, under `timeout 240s`, `set -o pipefail`. Actual exit code: `NORM19_BRIDGE5410_STATUS=0`.

## Decisive authentic terminal lines

```text
NORM19_STREAM_CHECKPOINT_PASS 128 caa1107a9060f03917bb523e69253f29135d73b7eca05623d1c70923d85643e8
NORM19_STREAM_BOOTSTRAP_128_USER_PILOT_PASS
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 512 7
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 1024 31
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 1536 21
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 2048 20
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 2560 29
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 3072 25
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 3584 4
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 4096 7
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 4608 14
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 5120 31
NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS 5410 14
NORM19_STREAM_5410_STEP_TRUE_TEICH_ORBIT_BRIDGE_PASS I 1805 CLASS 14 VALUE 1 SOURCE r1_i01536_02048.json
NORM19_STREAM_CHECKPOINT_PASS 5410 dd0990a862268c8721ae36ee53d6ffb73860464cf2e0f921dc7a0ec51d1e4cc2
NORM19_STREAM_PROGRESS 5410 OF 87809709 MOMENTS [50, 3175, 7] MAX_COORD 41238666085 ELAPSED 102.582
NORM19_STREAM_EXACT_PREFIX_PASS 5411 MOMENTS [50, 3175, 7]
NORM19_STREAM_LAST_STATE_CLASS 14
NORM19_STREAM_MAX_CM_COORD 41238666085
NORM19_STREAM_RESULT /home/bsdadmin/bsd389_p16231_P2_norm19_cyclic_stream_checkpoint.json
BOUNDARY_PREFIX_NOT_FULL_87809710_THETA_SUM
BOUNDARY_THETA_C2_AND_SHA_NOT_PROVED
NORM19_BRIDGE5410_STATUS=0
```

The 128-step authentic user pilot JSON was imported and cross-validated. Real normalized oriented quaternion 19-neighbor transitions were performed from n=128 through n=5410 with SHA256 checkpointed state, with 11 direct independently rebuilt p4 Gross anchor checks at n=512,1024,...,5120,5410. Each validated both Brandt class and oriented q embedding exactly.

At n=5410, user script matched the previously completed and separately stored 16231-point principal-unit i-orbit's **index i=1805**, Brandt class 14, modular eigenfunction value +1, while also independently rebuilding T(w^5410) and matching its CM embedding. This is not simply a class value from a loose heuristic.

Partial prefix n=0..5410 contains 5411 states, moments `[50,3175,7]` modulo 16231; last observed upper bound on integral CM embedding coordinate is 41238666085. The checkpoint is a local user file pinned by digest `dd0990a862268c8721ae36ee53d6ffb73860464cf2e0f921dc7a0ec51d1e4cc2`.

**Boundary:** This is a very small fraction of the exact H=87809710 cyclic ringclass orbit. Nonzero partial quadratic moment 7 does **not** establish nonzero global theta c2 or theta order2 or any Sha theorem.

Next mathematically useful checkpoint: n=p=16231 where the principal unit exponent becomes 0 and the ringclass generator becomes its Teich component tau=121898074, whose genuine P2 Gross ideal class 24 was previously certified at an independent anchor. A cheap additional inversion-symmetry test can exploit the already calculated 16231-point principal orbit without new quaternionic classifications.
