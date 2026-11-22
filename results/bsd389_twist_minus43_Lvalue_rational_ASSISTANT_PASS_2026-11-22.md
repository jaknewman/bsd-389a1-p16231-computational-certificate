# Assistant-side exact rational execution — 2026-11-22

Source file: `verification/bsd389_twist_minus43_Lvalue_exact_rational_certificate.py`.
Locally executed source SHA256: `d5aafa3c2e823a7f103c0d87776fe922fd7b12369f79becb3346777902197fe7`.
Execution in Python standard library (not Sage, external modular tables or arbitrary floating point in the comparisons).

```text
N_TWIST 719261 M 1500 AP2 -2 AP11 -4 AP389 1
PI_AND_SQRT_RATIONAL_BOUNDS_PASS 314159/42450000 3927/530000
PARTIAL_L_INTERVAL 10.808892089531577 10.839871860738453
EXPLICIT_TAIL_BOUND 0.118097706532144
COMPLETE_L_INTERVAL 10.690794382999433 10.957969567270597
TWIST_MINUS43_L_INTERVAL_10_TO_11_RATIONAL_CERTIFICATE_PASS
SCOPE: under modular functional equation and root number +1; no BSD proof
```

The printed decimal bounds are readability only. The source uses exact `Fraction` inequalities, and its decisive assertion is `Fraction(10) < complete_lo < complete_hi < Fraction(11)`, with the complementary analytic proof in the associated paper. The interval bounds are **conditional only on established standard theorems** (modularity/functional equation, Weil–Deligne coefficient bound). This does not certify any prime-primary component of Sha(E/Q) or the full complex BSD identity.