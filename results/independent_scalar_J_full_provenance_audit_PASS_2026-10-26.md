# Independent global scalar J — completed-run provenance PASS

**Date:** 2026-10-26. **Source:** user-executed IONOS Ubuntu terminal, `scripts/audit_independent_scalar_J_full_execution.py`. `AUDIT_STATUS=0 0`. This is a preservation report of an actual run, not an execution by the assistant.

## Authentic terminal output

```text
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd-389a1-p16231-computational-certificate/historical/originals/bsd389_tame_relation_export_p16231.json 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd-389a1-p16231-computational-certificate/verification/independent_c01_scalar_J.cpp 41df969bf7c766ef81bfe308def1c38710896ba46b7b3b5b025fc8b652d0639d
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd-389a1-p16231-computational-certificate/historical/v65/v65_independent_terminal_ntt.cpp 77211e5290c678cb5aad343321944993d43a05ed51952c89797e9ee677966a2d
SECOND_J_EVIDENCE_SHA256 /tmp/bsd389_independent_J 6d206751fe676e9594445335da15471430908107768ec80f10b60f088fcfce09
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd389_independent_J_full.chk 16d1c293c21d30114873fefb9b6af35e82a5dc24709adef0aaac9e317157a58b
SECOND_J_EVIDENCE_SHA256 /home/bsdadmin/bsd389_independent_J_full.log 32de86c5d24e99c698041f9eb8ae646ac9efbc6413466451ce04f49a1c14214a
SECOND_J_PINNED_INPUTS_PASS
SECOND_J_FINAL_CHECKPOINT_PASS pairs 263429130 sum_mod_p 4486
SECOND_J_COMPLETE_LOG_AND_CHECKPOINT_PASS checkpoints_logged 264 last 263429130 sum_mod_p 4486
SECOND_J_REPO_COMMIT 34b92f0e557e3fb6ba4ef4893e306173b9bd76c6
SECOND_J_INDEPENDENT_FULL_EVIDENCE_PASS
BOUNDARY: hash/log/checkpoint auditor, NOT a fresh 263429130-pair computation and NOT independent eclib source data.
AUDIT_STATUS=0 0
```

## Frozen evidence

All seven source/input/executable/log/checkpoint SHA-256 digests have been copied into [frozen evidence manifest](independent_scalar_J_frozen_sha256_manifest_2026-10-26.json), which is now versioned by Git. [Frozen manifest validator](../scripts/audit_independent_scalar_J_frozen_manifest.py) is published but **has not yet been run on IONOS**. This newly added validator performs an exact match with every SHA and requires precisely all 264 expected ascending checkpoints.

## Logical boundary

The original V11/V19 and new dual-scalar engine have both completed the entire `p*(p-1)=263429130` outer domain with identical scalar `J=4486 mod 16231` but common audited V65 eclib symbol table and original Manin export. This provenance audit authenticates observed files and their completion markers, **not** an independent rerun of the 263m computations or the Sage level-3 global series. The p-primary Sha conclusion relies additionally on the algebraic Sage normalizations, p-adic regulator data, and the documented Kato/Sage proved upper-bound theorem. No exact p-adic u_p=1 or full BSD claim.
