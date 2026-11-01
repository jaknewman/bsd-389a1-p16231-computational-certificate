# Uniform profinite-det counterexample: actual Sage-Ubuntu user run PASS (2026-11-01)

**Provenance:** verbatim user-supplied terminal output; the script uses Python standard library and was run in the user's existing Sage-enabled terminal. After a verified fast-forward from `cc80577` to `4873b1a`, the user ran:

```bash
cd ~/bsd-389a1-p16231-computational-certificate
python -u verification/bsd389_uniform_profinite_det_counterexample.py \
  --integer 729 --exclude 2,3,5,7,389
```

Output:

```text
FINITE_LOCAL_FITTING_MINORS_PASS prime 59552011 fitt2_generator 3546442014144121
CONSTRUCTIVE_NO_FIXED_DIAGONAL_INTEGER_PASS candidate_C 729 counterexample_prime 59552011 q_divides_C_times_excluded_product_plus_one True excluded [2, 3, 5, 7, 389] q_divides_C False
MATHEMATICAL_GLOBAL_PROFINITE_COUNTEREXAMPLE R=product_p(Zp) b=(p)_p Fitt2=(b^2) components=(p^2) for ALL p
BOUNDARY_NOT_A_REAL_SHA_MODULE_AND_NOT_AN_ALL_PRIME_SHA_PROOF
```

The output was independently confirmed by integer arithmetic: \(729(2\cdot3\cdot5\cdot7\cdot389)+1=59\,552\,011\) (prime); \(q^2=3\,546\,442\,014\,144\,121\); \(\gcd(q,729)=1\).

**Exactly what passed:** the 2×2 minor gcd of an **artificial rank-two profinite module** is \(q^2\), even though the candidate diagonal integer 729 is a q-adic unit. The code exhibits an example of a nonzero profinite determinant whose p-components are never units, and the mathematical Euclid argument extends beyond this single example to all choices of nonzero C and finite excluded prime sets.

**NOT a theorem about the actual Sha of 389a1.** Does NOT compute an actual Selmer group, a real Fitting ideal, a motivic determinant, a finite-support bound for Sha, or any part of BSD. Its purpose is to invalidate an unsafe inference in the proof strategy. See [exact source theorem and corrected next-step boundary](../paper/bsd389_uniform_global_integral_det_vs_profinite_counterexample_2026-11-01.md).
