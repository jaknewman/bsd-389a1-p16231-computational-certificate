# User-run exact uniform chi53 toric unit certificate — PASS (2026-10-30)

**Provenance:** transcript pasted by the user from their Sage-enabled Ubuntu host in the existing GitHub working tree after a successful `git pull --ff-only origin main` to remote `23eedf1`. Execution used **ordinary Python**, not Sage's algebraic number field implementation; the script only uses exact Python integers and polynomial reduction. This is a genuine **user-executed** run, not a GitHub Actions assertion.

Command:
```bash
python -u verification/bsd389_uniform_chi53_toric_unit.py
```

Complete stdout:
```text
UNIFORM_CHI53_EXACT_CYCLOTOMIC_FACTOR_PASS F=-3*zeta9*U
UNIFORM_CHI53_EXPLICIT_INVERSE_PASS U*UINV=1
UNIFORM_CHI53_NORM_DETERMINANT_PASS 729
UNIFORM_CHI53_P_UNIT_ALL_PRIMES_EXCEPT_3_MATHEMATICAL_PASS
SPLITTING_SCOPE chi53_K_minus3 only applies to p congruent 1 modulo 3
BOUNDARY_NO_SHA_UNIFORM_FINITE_SUPPORT_PROOF; theta_order2_and_integral_primitivity_not_proved
```

The script verifies, for the **frozen original ordered coefficients** of the 18-class conductor-53 Gross orbit, that
[
F(zeta_9)=-3zeta_9(zeta_9^4+zeta_9^3-zeta_9^2+1)
]
and that the parenthesized factor has explicit inverse (zeta_9^4-zeta_9^3-1). It independently takes the determinant of the `6×6` integer matrix of multiplication by `F`, obtaining exactly `729=3^6`. Hence this finite **algebraic factor**, and only this factor, is a `p`-adic unit for every `p≠3`.

**What it DOES NOT prove:** Provenance of the original quaternionic/Gross orbit beyond the coefficient vector; identification with the normalized adelic toric period; vanishing of lower-order anticyclotomic theta coefficients; `p`-integral primitivity of generalized Kato classes; any uniform bound on `Sha(E/Q)[p]`; all-prime BSD.

See [uniform prime-support research note](../paper/bsd389_uniform_prime_support_chi53_unit_and_split_obstruction_2026-10-30.md) and [issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
