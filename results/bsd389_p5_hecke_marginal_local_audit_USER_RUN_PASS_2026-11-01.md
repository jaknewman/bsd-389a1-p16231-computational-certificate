# Genuine user-run p=5 Hecke marginal local audit — PASS (2026-11-01)

**Provenance:** exact Ubuntu terminal output supplied by the user after successful `git pull --ff-only origin main` to commit `f4ed858`. The script used ordinary Python: no Sage, no eclib, and no recomputation of `M11`.

Run:
```bash
python -u verification/bsd389_p5_hecke_marginal_local_audit.py
```

Verbatim stdout:
```text
P5_HECKE_INDEPENDENT_POINTCOUNTS_PASS a41 -3 a61 -8
P5_HECKE_MARGINAL_GROUP_RING_FACTOR_JETS_PASS log61_mod41 34 log41_mod61 54 first (0, 0, 4) second (0, 0, 4)
P5_HECKE_PURE_QUADRATIC_MOMENTS_FORCED_ZERO_PASS M00 0 M10 0 M20 0 M01 0 M02 0
P5_MIXED_M11_HISTORICAL_USER_RUN 4 NOT_RECOMPUTED_BY_THIS_LOCAL_AUDIT
BOUNDARY_UNIVERSAL_HECKE_JET_STRUCTURE_NOT_UNIFORM_M11_NONVANISHING
```

**Exact scope:** independent finite-field point counts `a41=-3`, `a61=-8` verify both q's admissibility modulo p=5. Group-ring logarithms `d1=34`, `d2=54`, with Hecke marginal factors `a_q-X^d-X^{-d}`, yield jets `(0,0,4)` for both factors; their multiplication with a one-prime theta with augmentation zero modulo 5 forces `M00=M10=M20=M01=M02=0`. These zeros are rigorous algebraic consequences of the source-verified Hecke identity. The separate user's genuine elliptic mixed-jet Sage/eclib run previously computed `M11=4`, `mixed_rank=39`, giving the total-degree 2 jet `4TU`; this particular script **explicitly did not recompute** that value.

**No new p-uniform Sha or complete BSD theorem follows.** See the [exact Hecke marginal proof](../paper/bsd389_kurihara_hecke_marginals_force_low_jets_2026-11-01.md) and [the genuine actual mixed-value run](bsd389_p5_real_kurihara_mixed_jet_SAGE_PASS_2026-11-01.md).
