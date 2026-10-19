# Final V11 historical binary provenance PASS (2026-10-19)

This record transcribes the user-supplied IONOS terminal report. It is an audit of a finite computation, **not** an unconditional proof of global BSD.

## Exact reproducible build

- Compiler: Ubuntu GCC 13.3.0, Boost.JSON 1.83
- Historic V11 ELF SHA-256: `31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63`
- Source rebuild with `-O2`: **byte-identical SHA-256** `31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63`
- Rebuild with `-O3`: different SHA-256 `48bd036390ba672cf3b4dd7a18459dac0e7cad19a2c364492ba14fa96c281e81`, as expected
- ELF Build-ID: `41e18988d12493955a637e8e3609984f69c5d556`
- Original V11 source SHA-256: `0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187`
- Eight historical file SHA pins PASS, original Manin export structure (390 reps, 67 gens, 2012 relations) PASS, final V19 metadata cross-pins PASS.

## Original/rebuilt binaries vs archived V19 chunks

All eight comparisons PASS across four windows:

| Window | Archived output SHA-256 |
|---|---|
| `0:512` | `6890c83dcb7a0b5dcc51feb9073ae37add3048e76bdaa97a64e18148880237eb` |
| `512:1024` | `14219c05438b11da1e79dfe44131a237ef4f1c9899417d6d176de625243b914a` |
| `131714560:131715072` | `fb6059e9f05ceb5db0b6bc89411402ab600d708b73d57aa58774695317f40fc6` |
| `263429120:263429130` | `d230640c72eda33c021e73136c8ddd12c4b1be8199f44b7710680678507c361e` |

**Verbatim result markers:**

```text
BINARY_SOURCE_EXACT_REPRODUCIBLE_BUILD_PASS
PROVENANCE_REPORT_SAVED /home/bsdadmin/bsd389-c01-v14-production/v11_provenance_report_2026-10-19.json sha256 a9b853ee30d95bb48565bc99c35799dcc40c57b2bc8b9915792b81e72e3e9371
BSD389_BINARY_PROVENANCE_AUDIT_PASS verdict=EXACT_REBUILD_AND_HISTORIC_CHUNK_SAMPLE_PASS
EXIT_STATUS=0
```

## What closes, what does not

**CLOSED:** original source ↔ historic ELF exact reproducible-build provenance, and eight bounded exact comparisons with archived production chunks.

**PREVIOUSLY PASS (reported):** full V19 chunk/checkpoint chain, 390 exact rational cusp identities, source-to-C01 reference comparison, independent V65 moment contractions, and SageMath 10.9 conditional Kato arithmetic gate.

**NOT INFERRED:** that every chunk was produced by faithfully executed source code independently of stored checksums; independently reproduced full V19; unconditional mathematical BSD theorem; exact `u_16231=1`. The documented implication `Sha(E/Q)[16231^infinity]=0` follows from `J_ref=J_V19=4486`, its normalized cyclotomic bridge and Sage/Kato's proved p-primary upper bound.

A timestamped JSON verifier report is present on IONOS, with the above SHA-256, but its actual bytes have not yet been uploaded to this repository.
