# Real Ubuntu PASS: synthetic full-rank p=5 mixed-distribution obstruction (2026-11-02)

**Provenance:** verbatim stdout supplied by the user from the `bsdadmin@ubuntu` Sage-enabled shell, after a successful `git pull --ff-only origin main` fast-forward `f4ed858..3392961`. The code is pure Python. This is **not** a calculation of an elliptic Selmer group, actual E eigensymbol, Kurihara witness for E, or Sha.

Executed:
```bash
python -u verification/bsd389_p5_maximal_mixed_rank_zero_kurihara_toy.py
```

User's exact output:
```text
P5_TOY_SIGN_PLUS_AND_UNIT_SAMPLE_PASS f_1_1 4 entries 2400
P5_TOY_ALL_FIVE_HECKE_MARGINAL_JETS_ZERO_PASS M00_M10_M20_M01_M02 [0, 0, 0, 0, 0]
P5_TOY_MIXED_ANCHORED_MATRIX_MAXIMAL_RANK_PASS rank 39 max 39
P5_TOY_FULL_RANK_AND_ALL_PURE_JETS_YET_M11_ZERO_PASS actual_M11 0 direct_mixed_contraction 0 unit_sample 4
BOUNDARY_SYNTHETIC_FUNCTION_NOT_REAL_EIGENSYMBOL_OR_SHA
```

**Exact conclusion:** a *synthetic* plus-symmetric function on the 40x60 CRT exponent grid has a unit sample, all five low/pure Hecke-type moments zero and maximal anchored mixed finite-difference rank 39, yet weighted two-prime mixed coefficient `M11=0`. The previously **real** direct Sage/eclib E389a1 run on the same grid had maximal rank 39 and `M11=4`. Therefore Hecke **marginal vanishing alone**, mixed maximal rank and sign symmetry cannot prove uniform two-prime Kurihara nonvanishing.

**New sharper theorem discovered afterward:** even fixing the **entire two one-variable Hecke marginal polynomials**, not merely their low-degree jets, leaves the mixed coefficient arbitrary modulo every odd p: the eight-term sign-plus invariant kernel perturbation `H=(1+X^(h1/2)Y^(h2/2))(1-X)(1-Y)` has both marginals **exactly zero** and `[TU]H(1+T,1+U)=2`. See [exact new proof](../paper/bsd389_kurihara_full_marginal_kernel_and_free_mixed_coefficient_2026-11-02.md). This proves a limitation of **marginal information alone**, not a limitation on full Hecke eigensymbol relations at all levels.

**Remaining math:** a prime-uniform arithmetic relation that controls the **genuine** E-eigensymbol's degree-two Kurihara coefficient, and the separate full BSD complex leading-term identity. Neither is proved.
