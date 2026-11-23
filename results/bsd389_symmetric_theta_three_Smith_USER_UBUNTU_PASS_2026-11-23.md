# 389a1 — user Ubuntu independent verification of three genuine symmetric Mazur–Tate matrices and Smith forms

**Date: 2026-11-23. Status: independently USER EXECUTED on Ubuntu / Sage Conda.** Genuine analytic matrices from authentic integer Manin data, not synthetic polynomials. This verifies the analytic matrix/cokernel theorem; it does not prove an identification with the arithmetic Selmer group or Tate–Shafarevich.

User command:
```bash
python -u verification/bsd389_true_symmetric_MazurTate_matrix_and_p_cokernel.py
```

Verbatim stdout:
```text
TRUE_SYMMETRIC_MAZUR_TATE_MATRIX_AND_P_COKERNEL_PASS m 5 size 2x2 center_exponent 3 quadratic_mod_pk 4 P_constant 5 P_modp Y^2 det -7220 det_mod_p_after_dividing_m 1 smith_p_valuations [0, 1]
TRUE_ANALYTIC_COKERNEL_IS_Zp_MOD_pK_PASS 5 1
TRUE_SYMMETRIC_MAZUR_TATE_MATRIX_AND_P_COKERNEL_PASS m 11 size 5x5 center_exponent 0 quadratic_mod_pk 1 P_constant 11 P_modp Y^5 det -395563875872 det_mod_p_after_dividing_m 10 smith_p_valuations [0, 0, 0, 0, 1]
TRUE_ANALYTIC_COKERNEL_IS_Zp_MOD_pK_PASS 11 1
TRUE_SYMMETRIC_MAZUR_TATE_MATRIX_AND_P_COKERNEL_PASS m 25 size 12x12 center_exponent 10 quadratic_mod_pk 22 P_constant 25 P_modp Y^12 det -151753339112452007665001265791485409507737600 det_mod_p_after_dividing_m 1 smith_p_valuations [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
TRUE_ANALYTIC_COKERNEL_IS_Zp_MOD_pK_PASS 5 2
ALL_THREE_GENUINE_MAZUR_TATE_SYMMETRIC_MATRIX_SMITH_CERTIFICATES_PASS
BOUNDARY_THIS_ANALYTIC_COKERNEL_IS_NOT_SELmer_OR_SHA
```

The exact determinant values, Smith valuations, center exponents, p-adic quadratic coefficient and polynomial constant P_m(0)=p^k agree with the theorem in `paper/bsd389_real_symmetric_theta_matrix_canonical_cyclic_p_cokernel_2026-11-23.md`.

Caution: the tested matrices have a **built-in augmentation factor** giving cokernel `Z_p/p^k` in the unit-Kurihara cases, **even though Sha[p] has been independently proved zero at p=5 and p=11**. They must not be identified with Sha or a Selmer Fitting determinant without a genuine arithmetic comparison and saturation of that factor.
