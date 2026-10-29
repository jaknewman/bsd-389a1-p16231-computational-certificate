# BSD 389a1 — authentic dual Kurihara/Hecke regression at p=7

**Date:** 2026-10-29. **Status:** PASS, complete terminal output reported by the user from Sage-enabled Ubuntu. Numerical arithmetic is exact; the transcript is a user-executed calculation rather than an independent rerun by this assistant.

## Source and command

Source: [verification/bsd389_kurihara_hecke_dual_p7_regression.py](../verification/bsd389_kurihara_hecke_dual_p7_regression.py).

```bash
python -u verification/bsd389_kurihara_hecke_dual_p7_regression.py \
  2>&1 | tee ~/bsd389_k7_hecke_dual.log
```

## Complete terminal transcript

```text
K7_HEC_AUXILIARY_PASS 113 281 a_q 9 -12
K7_MANIN_ECLIB_SAMPLE_AND_PARITY_PASS 31753
K7_HEC_ALL_FIBRES_LAPLACIAN_PASS q2 281 modulus 113 checked 112
K7_HEC_ALL_FIBRES_LAPLACIAN_PASS q2 281 modulus 281 checked 280
K7_LOWER_MOMENTS_AND_WILD_DERIVATIVE_PASS q2 281 moments [0, 0, 0, 0] classes 49 roots 3 3
K7_TRANSLATION_PASS q2 281 t 2 delta 0
K7_TRANSLATION_PASS q2 281 t 7 delta 0
K7_TRANSLATION_PASS q2 281 t 17 delta 0
K7_TRANSLATION_PASS q2 281 t 599 delta 0
K7_KURIHARA_DIRECT_AND_HEC_PASS q2 281 delta 0
K7_HEC_AUXILIARY_PASS 113 673 a_q 9 2
K7_MANIN_ECLIB_SAMPLE_AND_PARITY_PASS 76049
K7_HEC_ALL_FIBRES_LAPLACIAN_PASS q2 673 modulus 113 checked 112
K7_HEC_ALL_FIBRES_LAPLACIAN_PASS q2 673 modulus 673 checked 672
K7_LOWER_MOMENTS_AND_WILD_DERIVATIVE_PASS q2 673 moments [0, 0, 0, 2] classes 49 roots 3 5
K7_TRANSLATION_PASS q2 673 t 2 delta 2
K7_TRANSLATION_PASS q2 673 t 7 delta 2
K7_TRANSLATION_PASS q2 673 t 17 delta 2
K7_TRANSLATION_PASS q2 673 t 599 delta 2
K7_KURIHARA_DIRECT_AND_HEC_PASS q2 673 delta 2
K7_DUAL_ZERO_AND_NONZERO_HECKE_REGRESSION_PASS delta_113x281 0 delta_113x673 2
BOUNDARY: authentic finite p7 tests only; no p599 delta or Sha certificate.
```

## Interpretation and strict boundary

At p=7 all 392 Hecke fibres for pair (113,281) and 784 for pair (113,673) match the rank-two Hecke Laplacian expression on the genuine eclib/390-Manin modular symbols. The constant and two linear logarithmic moments vanish in both runs, but the mixed coefficients differ: 0 and 2, respectively. Four multiplicative index shifts preserve each value. The test discriminates a vanishing and a nonvanishing Kurihara witness: it does not force nonvanishing.

No p=599 full coefficient, global Sha finiteness or universal prime bound follows from this p7 regression; the p599 tame norm and modular-symbol Fourier traces remain computationally unresolved.
