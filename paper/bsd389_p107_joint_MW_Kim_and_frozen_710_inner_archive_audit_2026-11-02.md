# p107: genuinely authenticated joint MW/Kurihara evidence and a direct internal 710-chunk audit

**November 2, 2026.** The user's genuine p107 two-source SHA verification is PASS; the direct tarball internal 710-payload replay has NOW BEEN GENUINELY EXECUTED ON THE USER'S UBUNTU AND PASSED. This is arithmetic proof provenance for one prime, not global Sha finiteness or full BSD.

## Genuine new user result

[Verbatim Ubuntu output](../results/bsd389_p107_Kim_joint_local_Kurihara_archive_USER_PASS_2026-11-02.md):

- Independent full local-MW JSON SHA256: 3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e.
- Real local MW matrix at q=(369793,383917): \(\begin{pmatrix}1&15\\1&53\end{pmatrix}\); \(\det=38\bmod107\), a unit. The local point count is \(\#E(\mathbf F_{107})=108\), not divisible by 107.
- Frozen **complete** Kurihara p107 tar.gz SHA256: b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754.
- Previous output says **delta=34 mod107, HISTORICAL and NOT recomputed** by the joint gate.
- New joint canonical JSON SHA256: cb2b7a59c66d2582fb5faf36ef2e6d3e7dcc507839de0fc404638f8d4ba2d37d.

The two sources are now demonstrably the previously authenticated ones. A SHA identity alone is **not a mathematical re-aggregation of archived block contributions**, and is not proof of the native C++ computation.

## Existing audit source, and the stronger newly published direct-tar auditor

The project already has [verification/kurihara_k107_final_audit.py](../verification/kurihara_k107_final_audit.py), which verifies the 710 archived JSON payload hashes, M390 dot products, exact contiguous interval coverage, final 390-dimensional weight vector, and delta=34, but requires a directory of extracted data plus original Manin table/native executable file paths.

The new independent [verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py](../verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py) directly streams the **frozen tar.gz without extracting any file or running the native 71-billion-term computation**. It checks the original full SHA, looks for all 710 named block payloads, config and final JSON, and matches the original 390-entry modular-symbol table by its exact SHA256 (00cdb5cd7ad9c7093877836412a77fe3f67985aa2e1878ddd03b8092ab90ee2f). The user's REAL run confirms that the original M390 table **WAS embedded in the archive**, so no extra table file was required. For any other archive where the table is missing, the auditor still requires exact bytes via the --table argument and **fails rather than inventing values**.

For every one of 710 JSON blocks, its full validation includes:
1. Original canonical payload SHA, expected block index and exact interval of length up to 100 million.
2. Header p=107, q1=369793, q2=383917, n=141969819181, matching source table and binary fingerprints.
3. All 390 vector entries in F107 and the **independently recomputed dot product with the original Manin M390**.
4. Aggregated W390 vector and expected SHA (ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0).
5. Coverage of every integer from 1 through 70,984,909,590 with no gap/overlap, independent half-contraction 17 and full delta=34, and FINAL_COMPLETE agreement.
6. A new canonical SHA256 pinned JSON report containing the audited output.

This is a **second, NOW USER-VALIDATED implementation of the finite archived-data aggregation**, NOT an independent recomputation of the original 70,984,909,590 numerators, and NOT a formal proof that the native Manin index map and Néron period normalization are correct for all entries. Those remain separate source audits.

Ubuntu command (no extraction, no very large recomputation):

    cd ~/bsd-389a1-p16231-computational-certificate
    git pull --ff-only origin main
    set -o pipefail
    python -u verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py \
      --output ~/bsd389_p107_frozen_tar_710_internal_reaggregate.json \
      2>&1 | tee ~/bsd389_p107_frozen_tar_710_internal_reaggregate.log

The actual user run **PASSED 710/710 payload SHA256 validations and dot contractions**, contiguous coverage 1…70,984,909,590, aggregate W390 hash ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0, and exact half=17/delta=34 against the frozen FINAL_COMPLETE record. Its canonical JSON SHA256 is 439bd3aa0bc8c861dfad63ac7b1ece48a3c5faabf28308d7c2e3fa62a06f8e62. [Verbatim user's real Ubuntu stdout](../results/bsd389_p107_frozen_tar_710_internal_reaggregate_USER_PASS_2026-11-02.md). No further table input is required for this original archive because the table and native binary were both embedded.

## Precise conditional Kim p107 consequence

[Kim's original Theorems 1.8 and 1.10](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf) relate a **genuinely nonzero degree-two Kurihara witness in the correct p-integral Manin normalization** to the dimension of the mod-p Selmer group, assuming residual GL2 surjectivity, unit Manin constant, no E(Q107)[107], and unit Tamagawa factors as appropriate. Since the independently certified MW rank is 2, a valid degree-two unit witness yields minimum Kurihara degree 2 and Sel(E[107]) dimension 2. The Kummer injection MW/107→Sel(E[107]) and exact sequence then force Sha(E/Q)[107]=0 and Sha(E/Q)[107∞]=0, without assuming its finiteness in advance.

The local determinant38 explicitly identifies P,Q as a basis of the two local Selmer lines. Once both groups are known to have dimension2 this local determinant is an independent cross-check, **not an extra required theorem hypothesis**.

This result concerns **only p107**, conditional on the original algorithm and normalization being mathematically correct. The global **uniform all-large-p two-auxiliary nonvanishing** theorem and the exact complex strong BSD leading term are NOT established by any archive verification.

See [Sha support research issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) and [p107 publication/reproducibility issue #6](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/6).
