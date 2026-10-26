# Independent u-index level-2 A2 — all 8115 checkpoints and 254 V61 blocks PASS

Executed on 2026-10-26 by the user on IONOS, via `scripts/audit_independent_p16231_level2_u_full.py`. Actual reported process status: `LEVEL2_EVIDENCE_STATUS=0 0`.

```text
INDEPENDENT_U_ALL_8115_CHECKPOINTS_PASS
INDEPENDENT_U_ALL_254_V61_BLOCKS_AGREE_PASS
INDEPENDENT_U_INDEXED_RESIDUES 131714565
INDEPENDENT_U_ECLIB_NONZERO_TERMS 131698335
INDEPENDENT_U_RAW_F2_MOD_P2 79629286
INDEPENDENT_U_F1_MOD_P2 0
INDEPENDENT_U_A2_N2_MOD_P2 19460969
INDEPENDENT_U_A2_N2_OVER_P_MOD_P 1199
INDEPENDENT_U_8115_CHECKPOINTS_COMBINED_SHA256 380dfc36b89394e12d6b533f70d0361ab574366000cb0099edb50e332ea00d3c
INDEPENDENT_U_254_OLD_V61_BLOCKS_COMBINED_SHA256 63305664af7aeac87942f880c1f9addc6a31eec8f9834ad374f5dcf5730d6386
INDEPENDENT_U_COMPLETE_RUN_LOG_SHA256 e4597c8fad06e9889420b958ab5cf43ba73550c832bff8aa9e70ceddd0201a91
INDEPENDENT_U_FULL_1199P_EVIDENCE_AND_V61_254_BLOCK_AGREEMENT_PASS
LEVEL2_EVIDENCE_STATUS=0 0
```

Independent-u evaluator source SHA256: `395264188ca241006c17f4fbaff45e1edb6ec6b849c65cd7ca423cc16c8a5ef9`.

All 8,115 per-row SHA-checksummed records and all 254 V61 old chunk SHA-checksummed records recomposed and matched. The level-2 coefficient is `A2^(2)=19460969 = 1199*16231` modulo `16231^2`. Second full computation used direct cyclotomic exponent u enumeration and new Sage/eclib evaluations rather than original V61's Fermat quotient pair enumeration. This audit checks checkpoints and comparison, not another execution of the 131698335 eclib values. Both full level2 algorithms share Sage/eclib as oracle.

No full level-3 Sage L-series or direct Kato/Sage p_primary_bound(16231) executed. Exact p-adic u_p=1 and full BSD not claimed.
