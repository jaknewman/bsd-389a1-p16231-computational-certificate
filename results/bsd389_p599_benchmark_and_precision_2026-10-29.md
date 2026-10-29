# BSD 389a1 — p=599, audited local Manin pilot: additive decomposition and feasibility

Date: 2026-10-29. **Status: PASS for exactly the reported finite intervals and additive decomposition; global Kurihara number and Sha[599∞] remain uncomputed.**

## Inputs and independent tests

User-executed Sage export of the 390-entry Néron-normalized plus modular-symbol table:

- `p=599`, `q1=6912461`, `q2=13963889`;
- table SHA-256 `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8`, format 390 coefficients;
- native `uint16_t` discrete-log tables, independent Python baby-step/giant-step and continued-fraction verifier: 5/5 selected intervals pass, including high-end range near `(q1*q2-1)/2`.

User-executed block additivity benchmark on the **authentic** table:

```
K599_TABLE_FORMAT_PASS sha256 fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8 len390 390
K599_W390_CHUNK_ADDITIVITY_PASS start 1 end 400000 contraction 9 units 400000 edges 4581844
K599_BOUNDED_BENCHMARK EARLY start 1 end 400000 partial 9 loop_seconds 0.03884 wall_seconds 0.19604 loop_terms_per_sec 10298555.1 EXTRAPOLATED_FULL_HALF_DOMAIN_DAYS 54.24
K599_BOUNDED_BENCHMARK MIDDLE start 24131209530207 end 24131210030206 partial 239 loop_seconds 0.060389 wall_seconds 0.218615 loop_terms_per_sec 8279598.7 EXTRAPOLATED_FULL_HALF_DOMAIN_DAYS 67.466
K599_BOUNDED_BENCHMARK TAIL start 48262418560415 end 48262419060414 partial 388 loop_seconds 0.053649 wall_seconds 0.210417 loop_terms_per_sec 9319873.0 EXTRAPOLATED_FULL_HALF_DOMAIN_DAYS 59.936
K599_GLOBAL_DELTA_STATUS UNCOMPUTED
```

One must distinguish the **integer half-range** `(q1*q2-1)//2 = 48262419060414` from the **number of invertible representatives** `phi(q1*q2)//2=48262408622240` (difference `10438174`). The loop scans the former while skipping nonunits.

## Why the native Sage supersingular p-adic alternative is not currently cheaper

SageMath 10.9 source, `src/sage/schemes/elliptic_curves/padic_lseries.py`, `pAdicLseriesSupersingular._prec_bounds(n, prec)`, implements

```
[infinity] + [2*e_j(n-1) -(n+2)]
```

for positive-degree coefficients, where `e_j(m)=min_{1<=k<=j} v_p(binomial(p^m,k))`. For **odd** p and the quadratic coefficient j=2, `e_2(m)=m`. Therefore the generic alpha-adic precision bound for the quadratic coefficient at level n is `n-4`.

At p=599, the `series(n, prec=3)` loop in the same source has exactly `(p-1)*p^(n-1)` evaluations of `measure` when no special truncation of the first two degrees is implemented:

| n | generic alpha-adic bound of T² coefficient | measure calls |
|---|---:|---:|
| 2 | -2 | 358202 |
| 3 | -1 | 214562998 |
| 4 | 0 | 128523235802 |
| 5 | 1 | 76985418245398 |

In particular, obtaining positive **generic certified** precision by this classical direct implementation would first require the n=5 scale, about 1.595 times the invertible Kurihara half-domain. The actual `Sha.p_primary_bound(p)` has a regulator-dependent initial level; its precise runtime or eventual accuracy is **not** established by this cost table. This is a cost barrier, not a proof that another algorithm or special extra cancellation cannot help.

Reference: https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/padic_lseries.py and https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py .

## Mathematical target

For n=q1*q2, define the weight `w(a)=log_{q1}(a) log_{q2}(a) mod599` on units and 0 elsewhere. The Kurihara derivative is a weighted sum of the **Néron-normalized classical modular symbols** `[a/n]^+` modulo 599.

Contraction of the continued-fraction output into a 390-component vector proves exact *finite-block* additivity. It **does not** compress the number of a-values; proving a faster-than-O(n) evaluation requires a new identity, an independent analytic modular-symbol reconstruction with rigorous integrality/error control, or a valid arithmetic Selmer upper bound via another method.

**No inference** of global Kurihara nonvanishing, Sha[599∞]=0, uniform prime support, or complete BSD is made from the benchmark.