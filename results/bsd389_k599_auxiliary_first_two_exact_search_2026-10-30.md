# BSD 389a1 p599 — first two verified Kolyvagin auxiliary primes in exact bounded scan

**2026-10-30; assistant-local computation.** Source: [verification/bsd389_p599_auxiliary_local_certificate.py](../verification/bsd389_p599_auxiliary_local_certificate.py). Run locally in CPython, not in the user's Sage shell:

```bash
python -u verification/bsd389_p599_auxiliary_local_certificate.py --search --limit 20000000 --hits 50
```

Complete stdout:

```text
P599_DISCOVERED_EXACT_PRIME 6912461 a_q 1799 N 6910663 row [1, 536]
P599_SEARCH_PROGRESS 8877181 primes_checked 1000 hits 1
P599_DISCOVERED_EXACT_PRIME 13963889 a_q -4191 N 13968081 row [1, 412]
P599_INDEPENDENT_LOCAL_PAIR 6912461 13963889 det 475
BOUNDARY: pair does not imply Kurihara nonvanishing.
```

Observed local wall time: about 8.15 s.

The exact scan covers q congruent 1 mod 599 in increasing order, proves candidate primality by trial division, considers all Hasse-compatible a_q=2+k*599, applies the necessary `[#E]P=[#E]Q=O` filtering, and exhaustively computes the exact point count for survivors before confirming p-admissibility. For the found candidates it additionally checks that p divides #E(F_q) exactly once and computes coordinates of two rational generators, giving determinant 475 mod 599. As no other candidates passed the exact verification before q2, these are the first two accepted primes in the stated bounded scan.

**Scope:** The scan does not construct a Kurihara witness. Nor does the local determinant prove that Sha[599] vanishes. Using arbitrary larger auxiliary primes would generally make a two-prime product larger, but one might use a different computational theorem or a changed number of primes; no speedup claim follows.
