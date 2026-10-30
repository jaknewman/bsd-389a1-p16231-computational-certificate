# BSD 389a1 — p=599 native four-worker checkpoint benchmark PASS

**Date:** 2026-10-30. **Provenance:** user-executed Ubuntu/Sage shell transcript, not independently reproduced on the same hardware. **STATUS: PARTIAL ONLY**, no global Kurihara or Sha certificate.

## Command

```bash
cd ~/bsd-389a1-p16231-computational-certificate
{
  time python -u verification/kurihara_k599_parallel_production.py \
    --native ~/bsd389_k599_native \
    --table ~/bsd389_p599_manin_table.txt \
    --outdir ~/bsd389_k599_parallel4_bench \
    --chunk-size 20000000 \
    --max-new-chunks 4 \
    --workers 4 --run
} 2>&1 | tee ~/bsd389_k599_parallel4_bench.log
```

## Complete observed output

```text
K599_PRODUCTION_CONFIG_PASS total_chunks=2413121 workers=4 chunk_size=20000000 table_sha256=fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
K599_CHUNK_PASS 2/2413121 20000001 40000000 residue=370
K599_CHUNK_PASS 3/2413121 40000001 60000000 residue=28
K599_CHUNK_PASS 1/2413121 1 20000000 residue=525
K599_CHUNK_PASS 4/2413121 60000001 80000000 residue=182
K599_NEW_CHUNKS_WRITTEN 4
K599_INCOMPLETE_NO_CERTIFICATE verified=4/2413121 units=79999984/48262408622240 partial_mod599=506

real    0m3.706s
user    0m13.236s
sys     0m0.149s
```

## Independent arithmetic checks on transcript

- Distinct complete blocks partition 1..80,000,000 without overlap or gaps.
- Sum 525+370+28+182=1105=506 (mod 599).
- In the first 80,000,000 numerators, multiples of q1=6,912,461 number floor(80,000,000/q1)=11; multiples of q2=13,963,889 number floor(80,000,000/q2)=5; there is no multiple of n=q1*q2. Therefore exact unit count is 80,000,000-11-5=79,999,984, matching output.
- Wall throughput is 80,000,000/3.706 = about 21.5866 million attempted numerators per wall second. CPU usage ratio (user+sys)/real ~3.61 cores.
- Extrapolation for entire *half-range of integer numerators* = 48,262,419,060,414 / (80,000,000/3.706) / 86400 = about 25.87 days wall, **only if observed short-run rate can be sustained**. This is not a measured long-run ETA or a guaranteed service completion time.
- Checkpoints are SHA-linked to true Sage Manin-table bytes and the on-server native executable; their detailed W390 vectors are in the user's local checkpoint archive rather than inside this report.

## No theorem from a partial residue

`506 mod 599` covers 80 million of the ~48 trillion numerator positions, not the full Kurihara half-sum. Neither the nonzero partial residue nor the local Mordell–Weil determinant implies global Kurihara nonvanishing, Sha[599^infinity]=0, or BSD.

Avoid `--full` without a separate deliberate resource/proof review. A separate checkpoint root is needed if changing chunk size or native binary. The existing 20m smoke checkpoints should be preserved.
