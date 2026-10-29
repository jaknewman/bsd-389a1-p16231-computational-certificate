# 389a1 — authentic Hecke fibre and Kurihara translation regression (p=5)

**Date:** 2026-10-29. **Status:** User-executed Ubuntu/Sage real eclib/Manin 390 calculation, all checks PASS. This proves the stated finite arithmetic identities in this example, not the general p599 Kurihara value.

## Reproducer

```bash
python -u verification/bsd389_kurihara_hecke_moment_translation_p5.py 2>&1 | tee ~/bsd389_k5_hecke_moments.log
```

## User-observed complete terminal transcript

```text
K5_HECKE_AQ_PASS 41 -3 61 -8
K5_HECKE_ALL_FIBRES_PASS modulus 41 checked 40
K5_HECKE_ALL_FIBRES_PASS modulus 61 checked 60
K5_HECKE_LOWER_LOG_MOMENTS_ZERO_PASS [0, 0, 0]
K5_KURIHARA_MIXED_MOMENT_PASS 4
K5_HECKE_TRANSLATION_INVARIANCE_PASS t 2 delta 4
K5_HECKE_TRANSLATION_INVARIANCE_PASS t 7 delta 4
K5_HECKE_TRANSLATION_INVARIANCE_PASS t 17 delta 4
K5_HECKE_TRANSLATION_INVARIANCE_PASS t 599 delta 4
BOUNDARY: exact p5 regression only; no p599 delta or Sha result
```

## Interpretation and limits

All 40 and 60 admissible fibres of the Hecke distribution hold for E=389a1, q1=41, q2=61 and p=5. Both q_i satisfy a_qi=2 mod 5, forcing the global constant, first-log1 and first-log2 moments to vanish modulo 5. The mixed moment is 4; the translated mixed moment is 4 for the four tested units. This is a separate real modular-symbol regression from the p5 Fourier/Artin–Schreier complete computation.

The corresponding Hecke identity at p599 is mathematically exact under the local admissibility hypotheses, but **the global delta599 is uncomputed**. Neither fibre verification nor local Mordell–Weil determinants provide a Selmer/Sha bound at p599.

See [mathematical proof and tame quotient boundary](../paper/bsd389_k599_hecke_marginals_wild_quotient_2026-10-29.md).
