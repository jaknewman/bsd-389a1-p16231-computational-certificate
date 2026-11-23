# 389a1 — USER Ubuntu full genuine integer cyclotomic resultants + functional equation, all three levels PASS

**Date:** 2026-11-23. **Environment:** user's Ubuntu with Conda Sage; complete native p5-depth25 histogram was generated with `/tmp/bsd389_hist25` and fed to `verification/bsd389_authentic_integer_cyclotomic_resultants.py --depth25-hist /tmp/bsd389_hist25.txt`.

**User's exact stdout:**

```text
AUTHENTIC_MAZUR_TATE_FUNCTIONAL_EQUATION_AND_SQUARE_RESULTANT_PASS m 5 shift 4 sqrt_B 7220 sqrt_R 1444 sqrt_R_modp 4
AUTHENTIC_FULL_MAZUR_TATE_INTEGER_RESULTANT_PASS p 5 depth 5 conductor 2501 representatives 1200 c0 0 c1 0 c2 -166 c2_mod_pk 4 resultant_digits 8 resultant 52128400 normalized_resultant 2085136 normalized_modp 1
AUTHENTIC_MAZUR_TATE_FUNCTIONAL_EQUATION_AND_SQUARE_RESULTANT_PASS m 11 shift 0 sqrt_B 395563875872 sqrt_R 35960352352 sqrt_R_modp 1
AUTHENTIC_FULL_MAZUR_TATE_INTEGER_RESULTANT_PASS p 11 depth 11 conductor 393427 representatives 196020 c0 0 c1 -3102 c2 -12462 c2_mod_pk 1 resultant_digits 24 resultant 156470779894879023760384 normalized_resultant 1293146941279991931904 normalized_modp 1
AUTHENTIC_MAZUR_TATE_FUNCTIONAL_EQUATION_AND_SQUARE_RESULTANT_PASS m 25 shift 5 sqrt_B 151753339112452007665001265791485409507737600 sqrt_R 6070133564498080306600050631659416380309504 sqrt_R_modp 4
AUTHENTIC_FULL_MAZUR_TATE_INTEGER_RESULTANT_PASS p 5 depth 25 conductor 56993501 representatives 28488750 c0 0 c1 -404300 c2 -5067478 c2_mod_pk 22 resultant_digits 89 resultant 23029075931778856293480525074058280758975693396694573028552616039759085259154270453760000 normalized_resultant 36846521490846170069568840118493249214361109434711316845684185663614536414646832726016 normalized_modp 1
AUTHENTIC_RESULTANT_BOUNDARY_NO_UNIFORM_SHA_ANNIHILATOR
```

These are **genuine integer Mazur–Tate diagonal polynomials** computed from all Manin modular symbols using the previously separately checked 390-entry integral symbol vector, not synthetic test polynomials. Three full resultants and their **integral square roots** match exact expected integers; Mazur–Tate involution coefficients match the independently calculated Frobenius shifts (4,0,5).

**Crucial scope limitation:** these finite computations validate a global-in-p algebraic criterion at p=5/11 but do **not** establish the uniform existence of a two-prime Kurihara unit for all p, nor identify any spectral determinant with Selmer or prove global Sha finiteness and exact complex BSD. The full 390-vector was historically validated but not regenerated in this run.
