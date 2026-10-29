# 389a1 — p=599 genuine Manin-table five-interval differential audit
Date: 2026-10-29.

**Observed user-run output:** SageMath/eclib export of the 390-entry Manin table for p=599, q1=6912461, q2=13963889 completed. The native C++ `uint16_t` kernel and an independently implemented Python CRT/BSGS/continued-fraction oracle agreed on the **complete 390-vector and scalar** for each of five sample intervals.

| Inclusive sample interval | Shared weighted sum modulo 599 |
|---|---:|
| 1–30 | 237 |
| 100000–100030 | 153 |
| 6912450–6912480 | 500 |
| 13963880–13963900 | 4 |
| 48262408622200–48262408622235 | 511 |

Reported terminal markers:
```text
K599_INDEPENDENT_PILOT_INTERVAL_PASS 1 30 sum 237 W390 390
K599_INDEPENDENT_PILOT_INTERVAL_PASS 100000 100030 sum 153 W390 390
K599_INDEPENDENT_PILOT_INTERVAL_PASS 6912450 6912480 sum 500 W390 390
K599_INDEPENDENT_PILOT_INTERVAL_PASS 13963880 13963900 sum 4 W390 390
K599_INDEPENDENT_PILOT_INTERVAL_PASS 48262408622200 48262408622235 sum 511 W390 390
K599_INDEPENDENT_CRT_BSGS_MANIN_PILOT_PASS 5 intervals
BOUNDARY: finite partial intervals only, not full Kurihara delta.
```

**Mathematical boundary:** The value of the global `delta_{q1*q2} mod 599` has NOT been computed. No Sha[599^infinity] vanishing is certified. Equality of five finite-range implementations is a useful regression test, **not a proof of equivalence for every residue** and not a proof of all missing Selmer local conditions.

**Next bounded check:** `verification/kurihara_p599_chunk_additivity_benchmark.py` tests chunk-additivity for scalar totals, every component of W390, and exact counters on a 400000-term union. It also benchmarks separate 500000-term samples near the domain midpoint and end. The new script was tested here using a **synthetic** Manin table; running it with the user's authentic table is pending. Its days estimate is an illustrative single-core extrapolation, not a certified computation runtime.

The complete half-range contains (n-1)/2=48262419060414 integers, of which 48262408622240 are units. Direct computation remains computationally prohibitive unless a real mathematical contraction or speedup is found.

**Provenance:** Data transcribed from the user's Sage Ubuntu logs in this conversation; the full large p599 computation has not been run.
