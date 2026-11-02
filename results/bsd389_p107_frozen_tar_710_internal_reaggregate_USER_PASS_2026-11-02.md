# Genuine user-run p107 frozen 710-chunk internal archive reaggregation — PASS (2026-11-02)

**Provenance:** verbatim Ubuntu Sage-terminal stdout pasted by the user after a successful fast-forward of the repository main branch to commit `65aea99`. The script [`verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py`](../verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py) runs read-only using Python standard-library tarfile streaming. This records a **second finite implementation reaggregating real archived outputs**, not a fresh repetition of the 70,984,909,590-numerator source computation.

Command:
```bash
python -u verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py \
  --output ~/bsd389_p107_frozen_tar_710_internal_reaggregate.json \
  2>&1 | tee ~/bsd389_p107_frozen_tar_710_internal_reaggregate.log
```

Exact user stdout:
```text
K107_TAR_ORIGINAL_ARCHIVE_SHA256_PASS b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754
K107_TAR_ALL_CHUNKS_PRESENT_PASS 710 regular_members 722 large_skipped 0
K107_TAR_M390_ORIGINAL_TABLE_SHA256_PASS 00cdb5cd7ad9c7093877836412a77fe3f67985aa2e1878ddd03b8092ab90ee2f source embedded_archived_table
K107_TAR_NATIVE_IDENTITY_STATUS embedded_archived_binary
K107_TAR_CONFIG_EXACT_PARAMETER_AND_HASH_PASS
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 100 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 200 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 300 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 400 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 500 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 600 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 700 / 710
K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS 710 / 710
K107_TAR_710_INDIVIDUAL_HASHES_AND_CONTIGUOUS_COVERAGE_PASS first 1 last 70984909590
K107_TAR_710_INDEPENDENT_DOT_PRODUCTS_PASS 710
K107_TAR_GLOBAL_W390_VECTOR_SHA256_PASS ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0
K107_TAR_RECONSTRUCTED_KURIHARA_HALF17_DELTA34_PASS half 17 delta 34
K107_TAR_FINAL_COMPLETE_AGREES_INDEPENDENT_REAGGREGATION_PASS
K107_TAR_INNER_AUDIT_JSON_SHA256 439bd3aa0bc8c861dfad63ac7b1ece48a3c5faabf28308d7c2e3fa62a06f8e62
K107_TAR_INNER_AUDIT_REPORT /home/bsdadmin/bsd389_p107_frozen_tar_710_internal_reaggregate.json
BOUNDARY_FROZEN_DATA_REAGGREGATED_NOT_FULL_NATIVE_REPLAY_OR_UNIFORM_SHA
```

**Exactly checked:** Source tarball SHA256; 710 uniquely numbered chunk JSONs + original matching embedded Manin 390 table and native binary; exact 710 individual payload hashes, headers and contiguous coverage of `[1,70984909590]`; per-block independent 390-coefficient dot products; whole 390-entry weight vector; its pinned SHA; exact half contraction **17 mod107**; full Kurihara residue **34 mod107** derived from the *archived data*; final manifest matches recomputed values. New canonical user-local audit report SHA256 `439bd3aa0bc8c861dfad63ac7b1ece48a3c5faabf28308d7c2e3fa62a06f8e62`. Report itself remains on the user's Ubuntu host and was NOT uploaded to GitHub.

**Trust boundary:** Neither this Python audit nor the original frozen-archive SHA recomputes all original input rational modular-symbol values. Mathematical correctness of the C++ per-numerator continued-fraction/Manin indexing and Néron-integral normalization must be supported by the previously published separate mathematical proofs and independent Sage source audits, not by this archival reaggregation. Consequently the Kim p107 Selmer/Sha vanishing theorem is a **computer-assisted consequence conditional on accepting the archived native computation and its normalization**, not a theorem about all p and not complete strong BSD.

**Next:** issue #6's formerly pending **internal 710 payload reaggregation** is now COMPLETE (PASS), but independent source/binary/Néron normalization review and public reproducibility remain separate tasks. The p107 local MW determinant **38 mod107** was separately authenticated and is not recomputed by this archive-only audit.
