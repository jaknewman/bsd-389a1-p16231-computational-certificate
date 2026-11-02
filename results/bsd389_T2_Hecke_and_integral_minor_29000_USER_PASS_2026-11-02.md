# Real user-run T2 non-marginal Hecke PASS and integral Hecke-eigenline minor 29000 (2026-11-02)

**Provenance:** user's verbatim Sage-enabled Ubuntu terminal stdout, after `git pull --ff-only origin main` to source commit `893a91d`. Two independently published scripts were executed. No numerical results invented; output JSON remains on the user's Ubuntu host and is not copied to this repository.

## A. Real T2 dual Sage/eclib verification

User command:
```bash
python -u verification/bsd389_p5_T2_nonmarginal_manin_gate.py \
  2>&1 | tee ~/bsd389_p5_T2_nonmarginal.log
```

Exact stdout:
```text
P5_T2_EIGHT_TERM_CRT_EXACT_PASS support 8 indices [1, 124, 486, 609, 1892, 2015, 2377, 2500]
P5_T2_HEKKE_CUSP_PERTURBATION_VALUES_PASS [1, 0, 0, 0]
P5_T2_3H_FLIPS_M11_4_TO_0_BUT_HEKKE_DEFECT_PASS old 4 new 0 defect_mod5 4
P5_T2_REAL_SAGE_ECLIB_EXACT_HECKE_IDENTITY_PASS oracle sage values ['2', '-2', '-1', '-1']
P5_T2_FAKE_8TERM_ZERO_EXTENSION_VIOLATES_HECKE_PASS oracle sage defect_exact -6 defect_mod5 4
P5_T2_REAL_SAGE_ECLIB_EXACT_HECKE_IDENTITY_PASS oracle eclib values ['2', '-2', '-1', '-1']
P5_T2_FAKE_8TERM_ZERO_EXTENSION_VIOLATES_HECKE_PASS oracle eclib defect_exact -6 defect_mod5 4
BOUNDARY_ZERO_EXTENSION_CHECK_NOT_UNIFORM_SHA_OR_BSD
```

Thus the exact true symbol values at `r=1/2501` and `2r,r/2,(r+1)/2` are `(2,-2,-1,-1)` and satisfy `-2*2-(-2)-(-1)-(-1)=0`. The artificially zero-extended 8-term `3H` has perturbation `[3,0,0,0]`, so creates Hecke defect `-6=4 mod5` without changing **either** full marginal. **Only that zero extension is ruled out**; it is not claimed that all Hecke-compatible extensions at other denominators are impossible.

## B. Actual integral Hecke matrix and one nonzero maximal minor

User command:
```bash
python -u verification/bsd389_integral_hecke_eigenline_uniform_minor.py \
  --output ~/bsd389_integral_hecke_eigenline_minor.json \
  2>&1 | tee ~/bsd389_integral_hecke_minor.log
```

Exact stdout:
```text
HECKE_INTEGRAL_MANIN_AMBIENT_DIM 33
HECKE_INTEGRAL_LATTICE_RANK_PASS 33
HECKE_INTEGRAL_STACK_PROGRESS ell 2 ap -2 rows 33 rank_Q 32 target 32
HECKE_INTEGRAL_FIXED_OPERATORS_Q_EIGENLINE_DIM1_PASS number_hecke_primes 1 rank 32
HECKE_INTEGRAL_PRIMITIVE_GLOBAL_KERNEL_VECTOR_PASS entries 33 nonzero 17
HECKE_UNIFORM_INTEGER_NONZERO_MINOR_PASS size 32 abs_det_bits 15 pivot_field QQ
HECKE_UNIFORM_INTEGER_DETERMINANT 29000
HECKE_INTEGRAL_FINITE_FIELD_PROBE p 5 rank 29 kernel_dimension 4 selected_minor_unit False
HECKE_INTEGRAL_FINITE_FIELD_PROBE p 7 rank 32 kernel_dimension 1 selected_minor_unit True
HECKE_INTEGRAL_FINITE_FIELD_PROBE p 107 rank 32 kernel_dimension 1 selected_minor_unit True
HECKE_UNIFORM_CANONICAL_JSON_SHA256 afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64
HECKE_UNIFORM_REPORT /home/bsdadmin/bsd389_integral_hecke_eigenline_minor.json
HECKE_UNIFORM_ALL_P_OUTSIDE_DIVISORS_C_EIGENLINE_RIGID_PASS conditional_on_correct_integral_hecke_matrices
BOUNDARY_C_HECKE_IS_NOT_C_SHA_AND_DOES_NOT_PROVE_BSD
```

**Fixed integer certificate from a real 33×33 integral Hecke matrix:** `A=T_2-a_2(E)*I=T_2+2I` has rank 32 over Q; one fixed exact **32×32 minor** has determinant `abs(det)=29000=2^3*5^3*29`. Therefore its mod-p rank is **exactly 32 for every rational prime p outside {2,5,29}** (a primitive integer kernel vector exists), and the kernel has dimension **exactly 1 in this fixed integral lattice**. The exception set here is merely a *sufficient* prime set from one selected minor, not necessarily the intrinsic eigenline congruence-prime set. Direct at p=5, `rank=29`, kernel dimension **4**, so the lone T2 eigenline is genuinely non-unique there. p7 and p107 both have rank32.

**Crucial limitation:** `29000` is **C_Hecke, NOT C_Sha**. It controls one integral Hecke eigenspace, not a Selmer Fitting ideal, nor any two-prime Kurihara coefficient or `Sha[p^∞]`. It also does not establish equality between this integral lattice reduction and all characteristic-p modular symbols.

**Independent next arithmetic task:** obtain the **Smith normal form elementary divisors** of the stacked *integral* matrices for T2,T3,... . The product of the nonzero elementary divisors is the **gcd of all rank-32 minors**, which is a divisor of 29000, and hence tests exactly whether adding Hecke operators removes the apparent bad primes (especially 5,29). This tightens a genuine all-prime congruence certificate without conflating it with Sha.
