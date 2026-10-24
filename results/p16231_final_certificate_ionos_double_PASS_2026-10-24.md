# BSD389 p=16231 final evidence-and-arithmetic self-audit — twice PASS

**Date:** 2026-10-24. **Run location:** user-operated Sage-enabled Ubuntu shell on IONOS, source `scripts/audit_p16231_final_certificate.py`.

The user supplied *two complete identical successful executions* of this **read-only verification script** in the current project checkout; `EXIT_STATUS=0` both times. The script verifies hashes, archived logs, sample replay entries, cross-file consistency, and integer arithmetic. It **does not** run the entire p-adic L-series or independently reproduce every original native computation.

## Complete output of each successful run

```text
FINAL_CERT_SOURCE_SHA_PASS original_V11_source 0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187
FINAL_CERT_SOURCE_SHA_PASS historical_V19_driver 61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418
FINAL_CERT_SOURCE_SHA_PASS original_relations_JSON 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
FINAL_CERT_SOURCE_SHA_PASS historical_original_ELF 31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63
FINAL_CERT_SOURCE_SHA_PASS V11_binary_provenance_report a9b853ee30d95bb48565bc99c35799dcc40c57b2bc8b9915792b81e72e3e9371
FINAL_CERT_SOURCE_SHA_PASS v19_full_log 7389152cd65c641b7173d69dc3de8098f510e550943179cfaf0373c748443a7a
FINAL_CERT_SOURCE_SHA_PASS v19_preflight_log 89e6cda8fc3a712f7f724b6f9f55863eae1bef3c113e05bc02e7f9d90cf5bdc4
FINAL_CERT_SOURCE_SHA_PASS v19_replay_log 07db19e00beecc654e4ccffcf8f2f55b36a10fc8f93052ddf7cd86dc5121e473
FINAL_CERT_BYTE_IDENTICAL_V11_BUILD_REPORT_PASS
FINAL_CERT_RECOMPOSED_ARCHIVED_CHAIN_REPORTED_PASS 263429130 514511 4019 9759143225
FINAL_CERT_NATIVE_SOURCE_DATA_SAMPLED_PASS windows=57 pairs=28682
FINAL_CERT_TERMINAL_MOMENTS_REPORTED_PASS 16014 4703 4486
FINAL_CERT_LEVEL3_SOURCE_IDENTITY_CONDITIONAL_PASS J 4486 A2_n2 19460969 A2_n3_mod_p2 154746354
FINAL_CERT_QUOTIENT_UNIT_CONDITIONAL_PASS v_p=0 first_digit=1
FINAL_CERT_KATO_SAGE_GATES_REPORTED_PASS
FINAL_CERT_CROSSCHECK_REPORTS_PRESENT_PASS
FINAL_CERT_ARCHIVED_EVIDENCE_AND_ARITHMETIC_PASS
CONDITIONAL_THEOREM: If historical C01 exactly evaluates J_ref, then Sha(389a1/Q)[16231^infinity]=0 by Sage's proved p-primary bound.
PUBLICATION_BOUNDARY: no full independent producer replay, no direct lp.series(n=3), no direct p_primary_bound(16231); no exact u_p=1 or full BSD theorem.
EXIT_STATUS=0
```

## Mathematical interpretation

For p=16231, one has p²=263445361, alpha mod p=128, and the verified recorded data

`J=4486 (mod p)`, `A2^(2)=19460969=1199p (mod p²)`,
`J/(4*128²)=8335 (mod p)`, hence
`A2^(3)=154746354=9534p (mod p²)` **conditional on the global C01/analytic bridge**.

The independently reported Sage regulator gives `B_p=9534p (mod p²)`; the quotient has unit residue 1 mod p, and so the valuation is zero. When the native historical global C01 output is indeed `J_ref` and all documented Kato/Sage theorem hypotheses hold, the proved bound yields `Sha(E/Q)[p^infinity]=0`.

## Strict proof boundary

The marker `FINAL_CERT_ARCHIVED_EVIDENCE_AND_ARITHMETIC_PASS` certifies the manifest/invariant checker itself. It is **not** an independent rerun of 263429130 C01 pair evaluations and **not** a new direct Sage `E.sha().p_primary_bound(16231)` result. A claim of unconditional full BSD for rank-2 curve 389a1, or exact p-adic quotient `u_p=1`, would not follow from this audit.

This report is a transcription of user-reported terminal output, *not* an assertion that the assistant accessed or independently ran the IONOS environment.

See the [fully qualified conditional certificate](../paper/p16231_final_conditional_computer_assisted_certificate_2026-10-24.md).
