# BSD 389a1 p599 — exact denominator-only finite-state Manin accelerator

**Date:** 2026-10-30. **Status:** mathematically exact kernel transformation; assistant-local original-vs-optimized synthetic-table tests PASS. **Genuine Sage Manin table differential validation on user's Ubuntu remains pending.** No full Kurihara or Sha certificate.

## Exact reduction

Let n=q1*q2, with (a,n)=1 and 1<=a<=(n-1)/2. The continued-fraction algorithm of the original native engine runs Euclid on (n,a) and produces successive convergents to a/n. For two consecutive convergent denominators d_{j-1},d_j, the next denominator is

  d_(j+1) = quotient_j*d_j+d_(j-1).

The oriented level-389 Manin edge is indexed solely by the ratio of the consecutive denominators mod 389, plus a sign determined by the parity of the Euclidean step:

  edge(c,d) = 389 if c=0 mod389, otherwise d*c^(-1) mod389.

Consequently no full convergent numerators are necessary and only the denominator residues in F_389 need to be retained. Initialize old_den=0, last_den=1. At each Euclidean quotient q update

  next_den = (q*last_den+old_den) mod 389.

For negative orientation, the edge index is edge(next_den,last_den); for positive orientation, edge(last_den,next_den). Accumulate W390 and direct symbol value exactly as before. The algorithm keeps Euclidean x,y and checks gcd(x,y)=1 at termination; this follows from excluding numerator multiples of q1 or q2.

All edge indices can be precomputed in a 389x389 uint16 lookup table (about 303 KB). Thus the optimized evaluator retains exactly the same W390, numerator coverage, individual weights, edge counts and final contraction, while avoiding full convergent numerators, full convergent denominators, their updates and repeated modular ratios.

This is **still O(number of numerator residues times continued-fraction length)**, not a sublinear computation of the Kurihara number.

## Assistant-local C++ differential tests, with synthetic Manin table

Compiled both kernels using g++ -O3 -std=c++17. A deterministic synthetic 390-table was used, **not the user's authentic Sage table**. The full W390 vectors, total weighted numerator counts, Euclidean edge counts, primitive roots and contractions agreed on all seven initial tests, including:

- positions 1..30, 100000..100030;
- positions 6912450..6912480 (around q1), 13963880..13963900 (around q2);
- positions 48262408622200..48262408622235 (near the end);
- 1..1000000 and 20000001..21000000.

On three 3,000,000-position intervals, a repeated three-run benchmark on the assistant-local machine gave median native loop times:

| Region | Original (s) | Denominator automaton (s) | Original/optimized |
|---|---:|---:|---:|
| Early | 0.297094 | 0.229443 | 1.295x |
| Middle | 0.383814 | 0.276989 | 1.386x |
| Tail | 0.349286 | 0.261318 | 1.337x |

On the same intervals, every component of W390 and the contraction matched the original. These synthetic-data benchmarks are reproducible indications, NOT a measured speedup on the user's Ubuntu instance and NOT a guaranteed full-run rate.

## Safety and faithful reproduction

- [New separate C++ kernel](../verification/kurihara_native_p599_denominator_automaton.cpp): exact same CLI and two-line output protocol as the original p599 kernel.
- [Differential test driver](../verification/kurihara_p599_denominator_automaton_differential.py) compares the baseline and optimized native engines on 9 scattered intervals, 5 of which also pass an independent Python BSGS/continued-fraction oracle (importing the project's existing verifier). When the table SHA is the user's genuine `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8`, the test pins five historical local contractions and the authentic first two 1m checkpoint contractions 456 and 22.
- Do **not** overwrite/recompile the original `~/bsd389_k599_native` binary in place: its SHA is pinned in all existing checkpoint folders. Compile the new C++ kernel to a **different executable**.
- If using the new executable in checkpoint production after the differential PASS, select a **new outdir** because the producer rejects mismatched pinned binary hashes; never merge old and new checkpoints under a single config without an independently audited migration.

**Boundary:** Global delta599 remains uncomputed. A faster kernel alone cannot establish nonvanishing or Sha[599^infinity]=0. The combinatorial logarithmic work remains the principal bottleneck.
