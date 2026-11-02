# Genuine p=107 joint MW-local/global-Kurihara archive cross-certificate — user Ubuntu PASS (2026-11-02)

**Provenance:** exact stdout pasted by the user from the Sage-enabled Ubuntu shell after successful fast-forward of GitHub `main` from commit `2a498dd` to `7c3ea9f`. The script [`verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py`](../verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py) is **a SHA identity and exact local-record gate**; it does **NOT** independently recompute the large historical Kurihara sum or prove the original algorithm mathematically sound.

## Executed command

```bash
python -u verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py \
  --output ~/bsd389_p107_joint_Kim_bridge.json \
  2>&1 | tee ~/bsd389_p107_joint_Kim_bridge.log
```

## User's verbatim stdout

```text
P107_NEW_MW_LOCAL_JSON_SHA256_EXACT_USER_PASS 3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e
P107_MW_KUMMER_LOCAL_DET_EXACT_PASS p 107 q [369793, 383917] matrix [[1, 15], [1, 53]] det 38 E_F107_order 108
P107_FROZEN_KURIHARA_GLOBAL_ARCHIVE_SHA256_PASS b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754
P107_GLOBAL_KURIHARA_DELTA_34_HISTORICAL_ARCHIVE_INPUT delta_mod107 34 NOT_RECOMPUTED
P107_KIM_THEOREM_1_10_EXACT_MODP_SELMER_GATE_CONDITIONAL rank_MW 2 local_dim 2 needs_valid_delta_algorithm_and_residual_Manin_Tamagawa_hypotheses
P107_SHA_PRIMARY_ZERO_CONDITIONAL_ON_VERIFIED_KIM_HYPOTHESES MW_map_determinant 38 no_global_uniform_SHA_claim
P107_KIM_JOINT_CANONICAL_JSON_SHA256 cb2b7a59c66d2582fb5faf36ef2e6d3e7dcc507839de0fc404638f8d4ba2d37d
P107_KIM_JOINT_REPORT /home/bsdadmin/bsd389_p107_joint_Kim_bridge.json
BOUNDARY_P107_ONLY_AND_EXTERNAL_GLOBAL_DELTA_NOT_RECOMPUTED
```

## Precisely established and the remaining external conditions

1. New independent **genuine** local MW source JSON SHA `3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e` was matched; all local numerical data were inspected from it for the p107 pair and `det([[1,15],[1,53]])=38 mod107` independently confirmed by script.
2. Old historical **complete** p107 Kurihara certificate archive SHA `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754` matches the frozen expected digest. The historical archived value **δ=34 mod107 is a hard-coded expectation in the gate, NOT an independently extracted or recomputed archive summation**.
3. If the archive does contain a mathematically correct full modular-symbol weighted sum `δ=34 mod107` in the required integral/Manin normalization, with p107 residual surjectivity, unit Manin constant and all Tamagawa factors p-units, and `E(Q107)[107]=0`, then Kim [Thm 1.10](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8) yields `Sel(Q,E[107]) ≅ E(Q_q1)/107 ⊕ E(Q_q2)/107`, which has dimension2. The saturated MW rank2 Kummer injection then gives **Sha[107]=0 and hence Sha[107∞]=0**, *conditional on all these independent mathematical inputs*.
4. The user-run program did **not** establish that the archive includes complete independent per-block residues or check a 710-block sum, nor replay all its modular symbols. The exact next archival proof step is to inspect the archive's manifest and per-block results, verify their mathematical structure and perform a **finite aggregation of already saved block residues** if present.

**Boundary:** This is a genuine and useful *joint provenance* certificate for **one prime p107**, not an all-prime Sha bound, a new rank-two Euler system theorem, or a proof of full strong BSD.
