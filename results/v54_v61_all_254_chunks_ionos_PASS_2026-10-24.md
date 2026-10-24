# Full archived V54–V61 level-2 chunk audit — 2026-10-24

**Source:** User-supplied transcript of an actual IONOS invocation of `python -u scripts/audit_v54_v61_level2_archive.py`. The files have been uploaded and reviewed at `historical/level2/`; this markdown is a report, not a fresh remote execution by GitHub Actions.

## Terminal verdict (reported)

```text
V54_V61_ALL_CHUNK_DIGESTS_PASS 254 254
V54_V61_ALL_CHUNK_MODP_REDUCTIONS_PASS 254
V54_V61_TOTAL_PAIR_COUNT 131714565
V61_EVALUATIONS 131698335
V61_ALPHA_MOD_P2 179060520
V61_RAW_F2_MOD_P2 79629286
V61_LOWER_TERM_MOD_P2 0
V61_A2_N2_MOD_P2 19460969
V61_A2_N2_OVER_P_MOD_P 1199
V61_A2_N3_OVER_P_CONDITIONAL 9534
V54_V61_ARCHIVE_RECOMPOSITION_PASS
EXIT_STATUS=0
```

All 254 V54 blocks match their declared checksums. All 254 V61 blocks match their canonical JSON checksums and reduce to the respective V54 blocks modulo 16231. The 254-block reconstruction and alpha-unit-root arithmetic give the level-2 quadratic coefficient

`A2^(2) = 19460969 = 1199*16231 (mod 16231^2)`.

V61 executed 131,698,335 positive-weight eclib symbol evaluations in the original producer run, while the number of *indexed* half-range pairs is 131,714,565. This audit verifies stored records and arithmetic, **not a new evaluation of those eclib values**.

The recorded `A2^(3)/p=9534` is **conditional** on the exact C01/Sage correction formula and authenticated full global terminal `J=4486`. The V61 program itself explicitly labels this term conditional and performs no direct level-3 computation.

The labels in this report are output markers, not executable Linux shell commands. The user subsequently pasted them into the terminal and received `command not found`; those messages are irrelevant and do not invalidate the earlier successful audit.

## Chain of available corroborating evidence

- Frozen V19 state SHA-256 and eight original artifact SHA-256 identities PASS on IONOS.
- Exactly 390/390 rational-cusp relations and 2,012 group matrices independently checked from original relation JSON.
- V23 J0=16014 / V26 J1=4703 recomposed from 67 entries each.
- V65 independent eclib Hecke table SHA and all 134 per-generator moment contributions verified by `scripts/audit_v23_v26_v65_terminal.py` on IONOS, exit zero.
- Sage-level cyclotomic correction derived in `paper/c01_to_sage_quadratic_coefficient_identity_2026-10-24.md`.
- Full archived V19 chunk-to-checkpoint recomposition and byte-identical V11 rebuild documented in separately qualified reports.

**Boundary:** standard computational trust in archived producer outputs, complete provenance, and Sage version normalization remains relevant. Do not infer unconditional full BSD or exact `u_16231=1`; `Sha[16231^infinity]=0` remains a computer-assisted arithmetic implication contingent on the certified analytic coefficient.
