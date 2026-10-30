# BSD 389a1 p=599: authentic two-checkpoint restart smoke test

**Date:** 2026-10-30. **Provenance:** complete shell transcript supplied by the user, running the native `uint16_t` engine and actual 390-entry Sage Manin table on Ubuntu.

## Production run

```bash
python -u verification/kurihara_k599_parallel_production.py \
  --native ~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt \
  --outdir ~/bsd389_k599_smoke_1m_20261030 \
  --chunk-size 1000000 --max-new-chunks 2 --workers 1 --run
```

Reported stdout:

```text
K599_PRODUCTION_CONFIG_PASS total_chunks=48262420 workers=1 chunk_size=1000000 table_sha256=fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
K599_CHUNK_PASS 1/48262420 1 1000000 residue=456
K599_CHUNK_PASS 2/48262420 1000001 2000000 residue=22
K599_NEW_CHUNKS_WRITTEN 2
K599_INCOMPLETE_NO_CERTIFICATE verified=2/48262420 units=2000000/48262408622240 partial_mod599=478
```

The nonoverlapping chunk contractions agree: (456+22) mod 599 = 478. All first two million numerators are coprime to n, since both auxiliary primes exceed 2 million.

## Audit-only rerun

```bash
python -u verification/kurihara_k599_parallel_production.py \
  --native ~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt \
  --outdir ~/bsd389_k599_smoke_1m_20261030 --chunk-size 1000000
```

Reported stdout:

```text
K599_PRODUCTION_CONFIG_PASS total_chunks=48262420 workers=1 chunk_size=1000000 table_sha256=fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
K599_INCOMPLETE_NO_CERTIFICATE verified=2/48262420 units=2000000/48262408622240 partial_mod599=478
```

Thus, persistent checkpoints were reread and SHA/interval/table/native identity and W390-dot-product checks passed without running the native producer again. Binary SHA and detailed W390 records are in the user's retained JSON files, not this transcript.

**Strict limitation:** 478 is a partial sum over numerators 1..2,000,000, NOT the full half-domain contraction, NOT the global Kurihara delta, and NOT evidence of nonvanishing or of Sha[599^infinity]=0. No complete certificate yet exists.
