# K599 checkpointed full-domain producer: safe dry-run result

**2026-10-30. Provenance:** complete observed stdout of the user's Sage-enabled Ubuntu terminal, without `--run`.

## Command

```bash
python -u verification/kurihara_k599_parallel_production.py \
  --native ~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt \
  --outdir ~/bsd389_k599_certified_chunks
```

## User-observed output

```text
K599_PRODUCTION_CONFIG_PASS total_chunks=48263 workers=1 chunk_size=1000000000 table_sha256=fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
K599_INCOMPLETE_NO_CERTIFICATE verified=0/48263 units=0/48262408622240 partial_mod599=0
```

The exact half-range is 1..48262419060414; its 48262408622240 units are paired under sign. With 1,000,000,000 entries per chunk, the plan comprises 48,263 checkpoints. The empty dry run created the pinned configuration and detected no completed chunks; no native computation was started and the partial residue 0 has NO mathematical evidentiary significance.

## Safe small smoke test (optional)

Use a separate directory because `--outdir` pins chunk size and executable/table hashes. **Do NOT use the existing 1e9 plan with a different chunk size.** This command runs only two small 1,000,000-entry chunks, then one can rerun the same command without `--run` to audit the resulting saved records:

```bash
python -u verification/kurihara_k599_parallel_production.py \
  --native ~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt \
  --outdir ~/bsd389_k599_smoke_1m \
  --chunk-size 1000000 --max-new-chunks 2 --workers 1 --run
```

```bash
python -u verification/kurihara_k599_parallel_production.py \
  --native ~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt \
  --outdir ~/bsd389_k599_smoke_1m --chunk-size 1000000
```

No smoke-run outputs are asserted until the user actually runs these commands.

**Boundary:** This merely verifies the state of a restartable producer. Global Kurihara delta599, its nonvanishing and Sha[599^infinity]=0 have NOT been proved. Recorded ~54–67 day one-core half-domain extrapolations remain indicative and do not guarantee linear speedup with workers.
