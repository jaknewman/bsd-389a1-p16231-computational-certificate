# Independent full scalar J recomputation (26 October 2026) — PASS

User-reported IONOS terminal completion of `verification/independent_c01_scalar_J.cpp`, running through all 263,429,130 pair IDs.

```text
INDEPENDENT_SCALAR_CHECKPOINT_PASS next=263429130 sum_mod_p=4486 of=263429130
INDEPENDENT_SCALAR_INTERVAL_PASS start=0 end=263429130 J_mod_p=4486
INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS pairs=263429130
BOUNDARY: new full scalar outer sum, independent of V11 producer/V19 chunks, but reuses pinned V65 eclib table and original independently audited Manin export.
FULL_STATUS=0 0 0
```

The three zero statuses correspond to the Python relation exporter, independently implemented C++ dual-scalar computation, and the tee logger.

## Independence

The original V11/V19 producer accumulates sparse coefficient rows and the global V19 state; the new engine computes each scalar directly from a dense precomputed Manin/Shapiro moment table. It does not read any V11/V19 TSV chunks or their checkpoints. Both complete global approaches now produce J=4486 modulo p=16231.

The new engine shares the original, exact-audited Manin relation export and independently evaluated V65 Sage/eclib table. Its basis moment construction reuses the source of the earlier independent V65 NTT/CRT terminal audit. Its earlier two pilot contributions, (1,0)=2316 and (2,3)=11725, independently matched direct level-3 eclib oracle calculations.

## Proof boundary

This is a genuine second global outer-summation PASS, but not a new Sage/eclib symbol table or an independent reproduction of the V54/V61 level-2 p-adic coefficient and regulator. The source-level C01/Sage analytic identity and Sage 10.9 precision theorem are still required to infer the p-primary bound. The full n=3 Sage p-adic L-series and p_primary_bound(16231) have not been run. Neither exact p-adic equality u_p=1 nor full BSD has been proved.

The user supplied the final terminal excerpt and successful PIPESTATUS; a separate hash of the full independent run log, final checkpoint, and compiled binary has not yet been archived. PASS is based on the supplied terminal execution.