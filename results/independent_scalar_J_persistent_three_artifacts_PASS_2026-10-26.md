# Independent J — persistent copies of binary, full checkpoint and log, SHA256 PASS

Date: 2026-10-26. Terminal output supplied by the user from the Sage-enabled IONOS Ubuntu session. All three artifacts were copied to `~/bsd389-evidence-frozen/` and checked against the frozen evidence manifest.

```text
6d206751fe676e9594445335da15471430908107768ec80f10b60f088fcfce09  /home/bsdadmin/bsd389-evidence-frozen/bsd389_independent_J
16d1c293c21d30114873fefb9b6af35e82a5dc24709adef0aaac9e317157a58b  /home/bsdadmin/bsd389-evidence-frozen/bsd389_independent_J_full.chk
32de86c5d24e99c698041f9eb8ae646ac9efbc6413466451ce04f49a1c14214a  /home/bsdadmin/bsd389-evidence-frozen/bsd389_independent_J_full.log
```

The three SHA-256 hashes match the Git frozen manifest exactly. The complete checkpoint and full run journal, as well as the executable binary, are now in the user's persistent home directory instead of relying only on the original temporary binary.

Mathematical status is unchanged by making copies: the complete second scalar summation had already returned `J=4486 mod 16231` for `263429130` pairs with exit codes `0 0 0`. The 264 checkpoints and seven source/data/output file hashes had already passed the frozen evidence auditor. Byte-for-byte preservation does not independently certify the source-level Sage analytic formula, regulator normalization, or execute `E.sha().p_primary_bound(16231)`.

Related references: [frozen SHA manifest](independent_scalar_J_frozen_sha256_manifest_2026-10-26.json), [frozen-manifest audit](independent_scalar_J_frozen_manifest_audit_PASS_2026-10-26.md), [full dual-scalar run](independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md).
