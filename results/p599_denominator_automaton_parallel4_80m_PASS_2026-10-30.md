# E=389a1 p=599 — denominator automaton: genuine four-worker 80M PASS

**Date:** 2026-10-30. **Provenance:** full user-provided Sage Ubuntu terminal output. Four distinct native subprocesses; genuine Sage-exported 390-entry Manin table; preexisting baseline benchmark retained independently. **Status:** exact bounded regression, not a full Kurihara delta or Sha certificate.

## User-executed command

```bash
cd ~/bsd-389a1-p16231-computational-certificate
{
  time python -u verification/kurihara_k599_parallel_production.py \
    --native ~/bsd389_k599_denominator \
    --table ~/bsd389_p599_manin_table.txt \
    --outdir ~/bsd389_k599_denominator_parallel4 \
    --chunk-size 20000000 \
    --max-new-chunks 4 \
    --workers 4 \
    --run
} 2>&1 | tee ~/bsd389_k599_denominator_parallel4.log
```

## User-observed complete stdout

```text
K599_PRODUCTION_CONFIG_PASS total_chunks=2413121 workers=4 chunk_size=20000000 table_sha256=fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
K599_CHUNK_PASS 1/2413121 1 20000000 residue=525
K599_CHUNK_PASS 2/2413121 20000001 40000000 residue=370
K599_CHUNK_PASS 3/2413121 40000001 60000000 residue=28
K599_CHUNK_PASS 4/2413121 60000001 80000000 residue=182
K599_NEW_CHUNKS_WRITTEN 4
K599_INCOMPLETE_NO_CERTIFICATE verified=4/2413121 units=79999984/48262408622240 partial_mod599=506

real    0m3.459s
user    0m10.729s
sys     0m0.173s
```

## Exact arithmetic and differential comparison

Four non-overlapping blocks cover numerators 1..80,000,000. Their contractions are `525, 370, 28, 182`, identical to the original `~/bsd389_k599_native` binary measured in the prior [four-worker benchmark](bsd389_k599_four_workers_80m_benchmark_PASS_2026-10-30.md); the sum `1105 mod 599 = 506`. Exactly 16 non-units are excluded (11 multiples of 6,912,461 plus 5 multiples of 13,963,889; no overlaps), leaving `79,999,984` units.

This is additional exact agreement over the same 80M range using the optimized executable in a **separate** checkpoint directory. The two checkpoint sets have distinct native-binary SHA pins and must **not** be merged without a separately audited protocol.

## Timings and limited extrapolation

| measurement | prior native engine | new denominator automaton | change |
|---|---:|---:|---:|
| real wall | 3.706 s | 3.459 s | ~6.7% less time / ~1.0714x throughput |
| user CPU | 13.236 s | 10.729 s | ~18.94% less user CPU |
| sys CPU | 0.149 s | 0.173 s | larger by 0.024 s |
| overall throughput | 21.59 million integers/s | 23.13 million integers/s | ~7.14% higher |
| total original range | 80 million | 80 million | same |
| sum modulo 599 | 506 | 506 | exact match |

The complete half interval comprises 48,262,419,060,414 integer positions. Extrapolating the optimized 80-million rate to that interval would suggest ~24.15 days wall on a machine sustaining precisely these conditions, **NOT** a verified production ETA. 4 out of 2,413,121 checkpoints have been produced in this particular configuration. Other checkpoint directories are partial and are not safely mergeable by default.

**Boundary:** 506 is a partial value and neither implies delta_n != 0 nor Sha[599^infinity]=0. This speedup is a constant factor, not a sublinear algorithm.
