# 389a1 at p=599: exact local gate and bounded Manin/Kurihara pilot

Date: 2026-10-29. **Status: local arithmetic PASS on user's Sage Ubuntu; full Kurihara delta and Sha[599^infinity] OPEN.**

## Fixed data (user execution)

- E = 389a1: y^2+y=x^3+x^2-2x, conductor 389, rank 2.
- p = 599, a_p = 0: good supersingular.
- q1 = 6,912,461, a_q1 = 1799, #E(F_q1) = 6,910,663 = 599*11537.
- q2 = 13,963,889, a_q2 = -4191, #E(F_q2) = 13,968,081 = 599*23319.
- Both q_i are prime, q_i = 1 (mod 599), and neither cofactor is divisible by 599.
- For P=(0,0), Q=(1,0), local coordinate matrix: [[1,536],[1,412]].
- Determinant 475 mod 599 is nonzero. Thus E(Q)/599 maps isomorphically onto the two one-dimensional finite-field quotients. **This does not establish full Selmer localization injectivity.**
- n=96,524,838,120,829; phi(n)=96,524,817,244,480; half-domain=(n-1)/2=48,262,419,060,414 **(including non-units)**. The earlier reported 48,262,408,622,240 is phi(n)/2, i.e. the number of unit representatives, not the full indexing interval.
- The Kurihara number delta_n modulo 599 remains **UNCOMPUTED**.

## Source-level computational gates

SageMath 10.9 supersingular p-adic L series: `pAdicLseriesSupersingular._prec_bounds(n,prec)` returns alpha-adic coefficient bounds `2*v_p(binomial(p^(n-1),j))-(n+2)`. For quadratic coefficient j=2 at p=599, the bounds are n-4: n=3 gives -1, n=4 gives 0, n=5 gives +1. Standard summation at n=5 involves (p-1)*p^4=76,985,418,245,398 terms. Low n=3 has 214,562,998 terms but insufficient quadratic precision.

Pollack--Stevens Sage 10.9 `_iterate_Up` explicitly rejects a nonordinary U_p eigenvalue (`ValueError: Lifting non-ordinary eigensymbols not implemented (issue #20)`). At p=599, a_p=0 and roots of X^2+599 have positive p-adic valuation, so do not launch the ordinary eigensymbol lift as a supersingular shortcut.

## Reproducible bounded pilot

The original K107 C++ native kernel uses an **unsigned char** log table. Reusing it at p=599 would truncate residues 256..598 and give invalid modular-symbol weights. `verification/kurihara_native_p599_pilot.cpp` replaces these with `uint16_t`, optimizes sequential CRT residues, and refuses intervals >1,000,000 unless `--allow-large` is explicitly set. Its output is always `STATUS=PARTIAL_ONLY`.

A separate program `verification/kurihara_p599_pilot_independent_check.py` recomputes logarithms by baby-step/giant-step and Manin edges by an independent continued-fraction implementation. It compares all 390 weights and each interval contraction for five dispersed intervals (near 1, 100,000, q1, q2 and the end of the half-domain). On a **synthetic** 390-value table, it passed all five local tests; this is a code-path test and is **not** an authentic modular-symbol or Kurihara computation.

Commands on the Sage Ubuntu repository after pulling the branch:

```bash
python -u verification/kurihara_export_manin_table.py \
  --p 599 --q1 6912461 --q2 13963889 \
  --out ~/bsd389_p599_manin_table.txt

g++ -O3 -std=c++17 -Wall -Wextra \
  verification/kurihara_native_p599_pilot.cpp -o ~/bsd389_k599_native

python -u verification/kurihara_p599_pilot_independent_check.py \
  --native ~/bsd389_k599_native --table ~/bsd389_p599_manin_table.txt

~/bsd389_k599_native \
  --table ~/bsd389_p599_manin_table.txt --start 1 --end 1000000 \
  | tee ~/bsd389_p599_pilot_1m.log
```

**No large production and no Sha conclusion should be reported from this pilot.** The open mathematical/computational target remains a sound sublinear contraction of the rank-two Kurihara coefficient, or a different valid Selmer bound.

## K107 provenance now retained in GitHub

The complete native/Manin/export/production/check scripts for the archived p=107 computation are now stored in `verification/`; source and theorem notes in `paper/`. The complete 710-chunk output remains separately on the user's server under `bsd389_k107_certificate_COMPLETE_20261028.tar.gz`, SHA-256 `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754`. The archived result was delta=34 mod107 with half-sum=17. The proof status depends on authentic eclib normalization/source correctness; do not equate Git source presence with reexecuting the complete archive.
