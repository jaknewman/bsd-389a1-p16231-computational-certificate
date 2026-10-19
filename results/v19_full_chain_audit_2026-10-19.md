# V19 full chunk-to-checkpoint chain audit — completion record

**Date reported:** 2026-10-19 (IONOS Ubuntu, user-provided terminal output).  
**Status:** **PASS for exhaustive recomposition of the archived chunk files into checkpoint states.**  
**Methodological boundary:** **NOT** an independent re-evaluation of the mathematical contribution of every chunk; checksums validate archived chunk bytes against their accompanying sidecar files.

## Final terminal record (verbatim)

```text
V19_CHAIN_BLOCK_PASS 3840 end 251789312 rows 9327752280 elapsed_s 27899.3
V19_CHAIN_BLOCK_PASS 3856 end 252837888 rows 9366751777 elapsed_s 28007.6
V19_CHAIN_BLOCK_PASS 3872 end 253886464 rows 9405720973 elapsed_s 28125.3
V19_CHAIN_BLOCK_PASS 3888 end 254935040 rows 9444773808 elapsed_s 28238.2
V19_CHAIN_BLOCK_PASS 3904 end 255983616 rows 9483837641 elapsed_s 28353.2
V19_CHAIN_BLOCK_PASS 3920 end 257032192 rows 9522861086 elapsed_s 28463.9
V19_CHAIN_BLOCK_PASS 3936 end 258080768 rows 9561594947 elapsed_s 28576.6
V19_CHAIN_BLOCK_PASS 3952 end 259129344 rows 9600491542 elapsed_s 28691.4
V19_CHAIN_BLOCK_PASS 3968 end 260177920 rows 9639471346 elapsed_s 28802.9
V19_CHAIN_BLOCK_PASS 3984 end 261226496 rows 9678252393 elapsed_s 28911.9
V19_CHAIN_BLOCK_PASS 4000 end 262275072 rows 9717018085 elapsed_s 29020.2
V19_CHAIN_BLOCK_PASS 4016 end 263323648 rows 9755569608 elapsed_s 29134.1
V19_CHAIN_BLOCK_PASS 4018 end 263429130 rows 9759143225 elapsed_s 29144.8
V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS pairs 263429130 expected_chunks 514511 checkpoints 4019 all_rows 9759143225 final_sha256 5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e
LIMIT: chunk contents authenticated against sidecars; independent mathematical re-evaluation of every chunk NOT performed.
```

## Certified scope of the reported run

| Item | Reported terminal result |
|---|---:|
| Pair-index domain | 263,429,130 |
| Archived chunk files | 514,511 |
| Checkpoint states | 4,019 |
| Parsed sparse rows | 9,759,143,225 |
| Final endpoint | 263,429,130 |
| Audit wall time (reported elapsed seconds) | 29,144.8 |
| Final state SHA-256 | `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e` |

The final SHA-256 agrees with the previously frozen V19 expected state hash. The complete raw log, chunk files, sidecar digests and checkpoint states have **not** been uploaded to this repository. These figures are transcribed from the user-supplied final terminal output; they are not a fresh GitHub Actions execution.

## What remains unproven by this audit

1. Independent computation of every `[L,R)` contribution from the modular-symbol definitions (the audit *recombines* archived outputs).
2. Complete proof that the historical producer executable implements the reference mathematical functional `J_ref` on every input, with justified integer-width, branch and cusp normalization behavior.
3. Unconditional passage from the reported V19 terminal invariant to the level-3 p-adic L-series coefficient. The conditional comparison manuscript and independent bounded checks remain relevant.

**Therefore this PASS closes the historical chunk-to-checkpoint recomposition obligation only; it is not an unconditional BSD theorem.**
