# Historical V11 binary provenance — final targeted closure protocol

**Status:** protocol ready; **NOT RUN** on IONOS after the 2026-10-19 Kato Sage gate. No unconditional BSD claim.

The historical V19 production driver pinned the exact executable SHA-256 `31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63` before doing any work. Its source SHA-256 is `61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418`. The complete independent chunk→checkpoint replay has **PASS** for 263,429,130 pair indices, 514,511 chunks, 4,019 checkpoints, final hash `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.

## Single bounded IONOS audit

The local prepared Python audit `bsd389_provenance_binaire_v11.py` is to be uploaded to `/home/bsdadmin/` and executed using `python -u` (the SageMath/Miniforge environment works, and `sage -python` is unsupported in this Sage 10.9 install).

The auditor:

1. Verifies **eight pinned SHA-256 values**: historic ELF, V11 aggregator, loader, transposed C01 source, V19 driver, canonical relation JSON, scalar values JSON, final state.
2. Checks final checkpoint JSON binds both the historical ELF and canonical export hashes; validates 390 representatives, 67 generators and 2,012 original `Gamma0(389)` relation terms.
3. Captures ELF build ID, compiler annotations and needed dynamic libraries.
4. Builds the exact received V11 sources separately with `g++ -O3` and `g++ -O2`, `-std=c++17 -DBSD389_EFFECTIVE -DBSD389_SPARSE_TOUCHED -lboost_json`; never overwrites the original ELF.
5. Tests the **historical** ELF and a **freshly rebuilt** ELF separately against the same historical sidecar-authenticated chunks for four windows: first 512, second 512, a middle 512, and the final partial 10 pairs.
6. Reports unequivocally either `BINARY_SOURCE_EXACT_REPRODUCIBLE_BUILD_PASS` (historical ELF byte-identical to rebuilt source) or `BINARY_SOURCE_EXACT_REBUILD_NOT_ESTABLISHED` (bounded equivalence only). Neither label substitutes for proof of compiler/OS correctness.

It writes `~/bsd389-c01-v14-production/v11_provenance_report_2026-10-19.json`. Runtime is limited to eight bounded producer calls and two local compilations, **no global V19 recomputation**.

## Interpretation

**Exact rebuild:** exceptionally strong historical binary↔source evidence, closing the practical compilation-identity question, together with independently proven C01 algebra and full archived aggregation. It does **not** independently reevaluate every mathematical chunk or prove full BSD.

**Different rebuild SHA, bounded checks PASS:** source/binary identity is not established because compiler and link environment may differ; proceed with build-history and ELF analysis, not with an unconditional theorem announcement.

**Any original ELF/archive mismatch:** must investigate the specific failed window or hash before claiming certification.

For complete status, see [STATUS.md](../STATUS.md), [C01 source-to-specification audit](../paper/c01_source_to_specification_audit.md), and [Kato arithmetic PASS](kato389_sage10_9_terminal_pass_2026-10-19.md).
