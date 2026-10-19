# Original production artifacts to import

The research bundle intentionally does **not** include historical originals missing from the model's verified working folder.

- `bsd389_c01_v11_aggregated.cpp` SHA-256 `0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187`
- `bsd389_c01_v11_loader.cpp` SHA-256 `f398d0f90a36dd3186c5d644a6b3f00f3081ebfc0a18cefd895db60db9b575d9`
- `bsd389_transposed_J_native.cpp` SHA-256 `e578ae0fac1a112a3a0b135847149c21c546e7099d952c373d25816d3089a545`
- `v19_production.py` SHA-256 `61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418`
- historical executable `bsd389_c01_v11_aggregated` SHA-256 `31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63`
- relation export `bsd389_tame_relation_export_p16231.json` SHA-256 `9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8`
- V19 final state `state_263429130.bin` SHA-256 `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`

**Never substitute generated or transcribed replacements for byte-identical originals.** Before importing, verify SHA-256 and scan for confidential data. The historical chunk corpus must be archived outside ordinary Git and linked by stable integrity manifests.

## Exact historical source archive received and authenticated — 2026-10-19

The user supplied `bsd389_sources_finales.tar.gz` (7,322 bytes) for independent review. Archive SHA-256: `fc8b30bc8045819efe7902be521fdd66efa40a5f3e2cd9403346405c30f99dd3`.

All four extracted files match the previously frozen digests, **exactly**:

| Member | SHA-256 match |
|---|---|
| `bsd389_c01_v11_aggregated.cpp` | `0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187` |
| `bsd389_c01_v11_loader.cpp` | `f398d0f90a36dd3186c5d644a6b3f00f3081ebfc0a18cefd895db60db9b575d9` |
| `bsd389_transposed_J_native.cpp` | `e578ae0fac1a112a3a0b135847149c21c546e7099d952c373d25816d3089a545` |
| `v19_production.py` | `61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418` |

**Status of repository upload:** This manifest attests received bytes and hashes; exact files still must be imported separately into version control. No archive payload is embedded in this manifest. Full relation and scalar JSON datasets are not included in this source-only archive.
