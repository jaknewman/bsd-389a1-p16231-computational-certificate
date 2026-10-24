# V19 native stratified replay — 57 archived chunks, 2026-10-24

**Verdict: PASS (user-executed on IONOS Ubuntu).** Source: terminal transcript supplied by the researcher; the full run log remains at
`~/bsd389_v19_stratified_producer.log` and has not been uploaded to GitHub. The script is committed at
`scripts/audit_v19_stratified_producer.py`.

## Invocation and observed output

```bash
python -u scripts/audit_v19_stratified_producer.py --random 24 --strata 25 \
  2>&1 | tee ~/bsd389_v19_stratified_producer.log
```

```text
V19_STRATIFIED_SAMPLE_COUNTS unique 57 total_archived_chunks 514511
V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS 1 57 0 512 6890c83dcb7a0b5dcc51feb9073ae37add3048e76bdaa97a64e18148880237eb
V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS 29 57 131714560 131715072 fb6059e9f05ceb5db0b6bc89411402ab600d708b73d57aa58774695317f40fc6
V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS 57 57 263429120 263429130 d230640c72eda33c021e73136c8ddd12c4b1be8199f44b7710680678507c361e
V19_STRATIFIED_PRODUCER_REPLAY_PASS 57 pairs_covered 28682 exceptional_E0 1186 exceptional_E1 14540
BOUNDARY: only selected chunks were re-produced; the 514511-chunk archived recomposition was already audited separately
BOUNDARY: sample is deterministic, not a formal probabilistic confidence bound
EXIT_STATUS=0
```

The actual terminal transcript contains the complete sequence of **57 individual `V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS` entries**, with the original and replayed full SHA-256 digest for each sampled chunk.

## What the script verifies

It SHA-pins the historical V11 executable and source-exported relations. It selects 57 unique chunks using 11 fixed beginning/middle/end anchors, 25 evenly spread anchors, and 24 fixed-seed pseudo-random indices (overlaps deduplicated). For each selected `[L,R)` it:

1. Reads the archived `chunks/L_R.tsv` and its adjacent SHA-256 sidecar.
2. Executes the original SHA-pinned V11 binary `BIN EXPORT L R fresh_temp_file`.
3. Requires the rerun digest to equal the archived digest and performs an **actual complete byte-for-byte equality comparison** against the archived chunk.
4. Parses the V11 exceptional-branch counters and the original `V11_AGGREGATE_PASS` marker.

The 57 intervals cover `56*512+10=28682` pair indices; nonzero exception counters `E0=1186`, `E1=14540` demonstrate sampled execution of both exceptional-path classes.

## Integration with earlier evidence

- The 2026-10-19 V11 provenance JSON reports a GCC 13.3.0 **byte-identical `-O2` rebuild** of the historical ELF.
- The 2026-10-19 complete V19 independent chain audit recomposed **all 514,511 archived chunks**, 4019 checkpoints and 263,429,130 pairs, giving frozen state SHA-256 `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.
- V23/V26/V65 independently cross-matched all 134 per-generator terminal contractions: `J0=16014`, `J1=4703`, `J=4486`.
- V54/V61 level-2 full chunk-record audit checked 254 blocks each and `A2^(2)/p=1199 (mod p)`.
- A separate source-level proof derives `A2^(3)-A2^(2)=p*J_ref/(4*alpha^2) (mod p^2)`, assuming the archived C01 source faithfully computes `J_ref`.

## Critical boundary

This is a **deterministic, non-randomly-certified sample of 57 among 514,511 chunks** (~0.0111%). It does not establish a formal statistical confidence bound and cannot establish correctness of all 514,511 chunk *mathematical outputs*. SHA sidecars and checkpoints authenticate internal consistency of stored data, not truth of all upstream calculations.

**Conclusion:** stronger historical native producer/archived-data corroboration; no claim of exact p-adic BSD quotient one, unconditional full BSD, or a completely independent fresh C01 production. The conditional p-primary deduction remains under review.
