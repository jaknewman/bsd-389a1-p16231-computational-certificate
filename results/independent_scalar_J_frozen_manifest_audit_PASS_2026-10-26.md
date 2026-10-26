# Frozen SHA-256 independent global scalar J evidence — full manifest audit PASS

**Execution date:** 2026-10-26. **Provenance:** terminal output supplied by the user from Sage-enabled IONOS Ubuntu, running the versioned read-only checker `scripts/audit_independent_scalar_J_frozen_manifest.py`. The reported Bash pipeline returned `FROZEN_STATUS=0 0`.

## Full recorded terminal verdict

```text
FROZEN_J_SHA256_PASS compiled_elf 6d206751fe676e9594445335da15471430908107768ec80f10b60f088fcfce09
FROZEN_J_SHA256_PASS completed_checkpoint 16d1c293c21d30114873fefb9b6af35e82a5dc24709adef0aaac9e317157a58b
FROZEN_J_SHA256_PASS completed_log 32de86c5d24e99c698041f9eb8ae646ac9efbc6413466451ce04f49a1c14214a
FROZEN_J_SHA256_PASS independent_scalar_cpp 41df969bf7c766ef81bfe308def1c38710896ba46b7b3b5b025fc8b652d0639d
FROZEN_J_SHA256_PASS original_manin_export 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
FROZEN_J_SHA256_PASS v65_eclib_table aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c
FROZEN_J_SHA256_PASS v65_ntt_cpp 77211e5290c678cb5aad343321944993d43a05ed51952c89797e9ee677966a2d
FROZEN_J_CHECKPOINT_PASS pairs=263429130 J_mod_p=4486
FROZEN_J_ALL_264_CHECKPOINTS_PASS
FROZEN_J_263429130_PAIRS_J4486_EVIDENCE_PASS
BOUNDARY: frozen full-run file consistency only; not an independent recomputation of J or direct p_primary_bound.
FROZEN_STATUS=0 0
```

## Scope

**All seven SHA-256 digests match** the immutable versioned JSON manifest `results/independent_scalar_J_frozen_sha256_manifest_2026-10-26.json`. The preserved full log records **all 264 consecutively expected checkpoints** (263 million-pair steps plus final 429,130 pairs) and the terminal sum `J=4486 mod p=16231`. The frozen final checkpoint has interval start=0, stop=263429130, next=263429130 and sum=4486.

This completes the additional **frozen-file integrity and checkpoint coverage audit** of the user's previously executed second global scalar sum; it adds no new mathematical pair evaluations.

The two global algorithms both return `J=4486 mod p`: original V11/V19 chunk accumulation and the independently programmed dual-scalar full-domain evaluation. The new algorithm shares an independently computed Sage/eclib V65 table and the audited original Manin/Shapiro export. The result supports the computer-assisted p-primary BSD consequence **subject to correctness of the universal modular-symbol/Sage analytic identification, level-2 input, p-adic regulator and Kato/Sage upper-bound hypotheses**. It is not a direct run of `Sha.p_primary_bound(16231)`, a proof of exact `u_{16231}=1` as a p-adic number, or a full BSD proof.

## Linked primary artifacts

- [Frozen seven-file SHA manifest](independent_scalar_J_frozen_sha256_manifest_2026-10-26.json)
- [Verifier source](../scripts/audit_independent_scalar_J_frozen_manifest.py)
- [Second global scalar full-run output](independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md)
- [Prior completed-execution provenance audit](independent_scalar_J_full_provenance_audit_PASS_2026-10-26.md)
