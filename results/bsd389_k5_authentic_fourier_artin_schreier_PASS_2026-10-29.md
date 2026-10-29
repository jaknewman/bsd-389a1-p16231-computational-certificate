# BSD 389a1 — authentic Fourier–Artin–Schreier Kurihara p=5 end-to-end PASS

**Date:** 2026-10-29. **Provenance:** user-executed Ubuntu Sage environment; complete terminal output supplied in conversation. This is an exact finite arithmetic/modular-symbol regression for a known witness, not a sublinear p=599 algorithm and not global BSD.

## Reproducer

```bash
python -u verification/bsd389_kurihara_fourier_trace_p5_authentic.py \
  2>&1 | tee ~/bsd389_k5_fourier_trace.log
```

Source code: [`verification/bsd389_kurihara_fourier_trace_p5_authentic.py`](../verification/bsd389_kurihara_fourier_trace_p5_authentic.py), with 2026-10-29 Sage 10.9 PARI ffelt `polynomial().list()` coordinate fix in commit `5e501b123aa3dce5d80260295208b12072ca623c`.

## Complete user-observed terminal output

```text
K5_AUTHENTIC_MANIN_DIRECT_DELTA_PASS 4 n 2501
K5_ARTIN_SCHREIER_FIELD_PASS degree 60 c (2, 2) lambda 1 beta 0
K5_BETA_NORMALIZATION_ROOT_CHANGE_PASS root_exponent 1
K5_SIGN_FROBENIUS_ORBITS_PASS 20
K5_FOURIER_ORBIT_TRACE_PASS 0 1 trace 0 h_top [4, 3, 0]
K5_FOURIER_ORBIT_TRACE_PASS 19 87 trace 0 h_top [2, 4, 3]
K5_AUTHENTIC_FOURIER_ARTIN_SCHREIER_DELTA_PASS 4 classes 20 target_coefficients 60 seconds 1.013
BOUNDARY: proves small-prime regression, NOT a sublinear p599 algorithm.
```

## What is established

1. Real eclib modular symbols on E=[0,1,1,-2,0], compressed to 390 Manin edge classes, reproduce direct normalized `delta_2501 = 4 mod 5`.
2. An explicit `GF(5^60)` root-of-unity construction reproduces the Artin–Schreier constants and `beta=0` in the chosen gauge.
3. All `20` even Frobenius frequency classes pass the relative trace and top-three-coordinate identities; the final Parseval/Fourier result is exactly `4 mod 5`.
4. This validates the complete **formula** at p=5 using authentic modular symbols.

**NOT established:** an algorithm to compute `p=599` modular-symbol relative traces sublinearly; a nonzero `delta` at p=599; a `599`-primary Sha bound; any uniform theorem bounding the prime support of Sha.

The `seconds 1.013` field is the program's reported overall elapsed time on the user's machine, not the time for computing a full p599 witness.
