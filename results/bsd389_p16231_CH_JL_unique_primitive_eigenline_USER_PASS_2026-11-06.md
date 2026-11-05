# Actual USER PASS: unique primitive Jacquet-Langlands Brandt eigenline for 389a1

**2026-11-06**. User executed `verification/bsd389_p16231_CH_Brandt_unique_JL_eigenline_gate.py` on Sage Ubuntu with `timeout 120s` and `set -o pipefail`. Terminal exit `JL_EIGENLINE_STATUS=0`.

Authentic console output:

```text
CH_JL_INTEGER_PRIMITIVE_BRANDT_V_PASS
CH_JL_EXACT_HECKE_EQUALITY_PASS 2 A_P -2
CH_JL_EXACT_HECKE_EQUALITY_PASS 3 A_P -2
CH_JL_EXACT_HECKE_EQUALITY_PASS 5 A_P -3
CH_JL_EXACT_HECKE_EQUALITY_PASS 7 A_P -5
CH_JL_COMMON_HECKE_EIGENSPACE 1 DIM 1
CH_JL_COMMON_HECKE_EIGENSPACE 2 DIM 1
CH_JL_COMMON_HECKE_EIGENSPACE 3 DIM 1
CH_JL_COMMON_HECKE_EIGENSPACE 4 DIM 1
CH_JL_UNIQUE_RATIONAL_HEKCE_LINE_PASS DIM 1 PRIMITIVE_GCD 1
BOUNDARY_GLOBAL_ADELIC_GROSS_RIGHT_IDEAL_IDENTIFICATION_STILL_TO_WRITE
JL_EIGENLINE_STATUS=0
```

The script uses Sage exact QQ matrices. The 33-entry integral Brandt V is primitive, and the simultaneous kernels of T_l-a_l at ell=2,3,5,7 span dimension exactly one. The unique rational eigenvector is a scalar multiple of V; because V has gcd1, it generates the primitive integral lattice on this line.

This means ambiguity among different rational Hecke eigenvectors has been removed. It does NOT alone prove equality of the global Gross right ideals with the published Castella-Hsieh construction nor fix the choice of anticyclotomic generator, but the prior local HNF p^4, global Morita construction, full CM cubic closure and local n1/n2 check considerably constrain the needed identifications.

The completely executed full finite theta remains (c0,c1,c2)=(0,0,3739) modulo p16231. To prove an infinite Iwasawa theta order2, combine a mathematically justified comparison of finite theta elements (the published Appendix §6 congruence) with exact trivial-character constant vanishing and the anticyclotomic functional equation. Only after that, and additional Theorem A hypotheses and auxiliary-character nonvanishing, can one conclude p-adic Selmer dimension 2 and finiteness of Sha[p∞], not Sha[p∞]=0.
