# P599 genuine Manin-table denominator automaton PASS (2026-10-30)

User-executed on Sage Ubuntu with source `verification/kurihara_p599_denominator_automaton_differential.py`.

Table SHA256: `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8` (authentic).
Baseline: `~/bsd389_k599_native`. New separate executable: `~/bsd389_k599_denominator`.

## Exact differential checks

All nine intervals: baseline and automaton have identical 390-dimensional W390 vectors, contraction, units, weighted counts, edge counts and generators. Five small intervals additionally pass the independent Python BSGS / continued-fraction oracle.

| interval | contraction mod 599 | weighted | edges |
|---|---:|---:|---:|
| 1–30 | 237 | 29 | 108 |
| 100000–100030 | 153 | 31 | 321 |
| 6912450–6912480 | 500 | 28 | 423 |
| 13963880–13963900 | 4 | 18 | 247 |
| 48262408622200–48262408622235 | 511 | 36 | 629 |
| 1–1000000 | 456 | 996635 | 12224350 |
| 1000001–2000000 | 22 | 996637 | 13387425 |
| 24131209530207–24131210030206 | 239 | 498215 | 7397328 |
| 48262418560415–48262419060414 | 388 | 498296 | 6608176 |

Archived checkpoints over the first 2m remain consistent: 456+22=478 mod 599.

## Measured native loop times on user machine

| interval | original (s) | automaton (s) | ratio |
|---|---:|---:|---:|
| 1–1000000 | 0.107492 | 0.0808011 | 1.330 |
| 1000001–2000000 | 0.112893 | 0.0896184 | 1.260 |
| Middle 500000 | 0.0621024 | 0.0534141 | 1.163 |
| Tail 500000 | 0.0589607 | 0.0424395 | 1.389 |

Script print: `K599_DENOMINATOR_AUTOMATON_EXACT_DIFF_PASS intervals 9 median_loop_speed_ratio 1.33`. Statistical note: the script selected the upper-middle element of 4 samples; the conventional median is approximately **1.295**. Timing measurements are short, and not a full-production speed guarantee.

**Boundary:** Bounded genuine-data agreement only. No full Kurihara delta at p=599 and no Sha[599^infinity] conclusion. Keep old SHA-pinned native binary and checkpoint roots unchanged; the new binary needs its own production outdir.
