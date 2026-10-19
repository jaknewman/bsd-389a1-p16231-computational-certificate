# SageMath 10.9 arithmetic Kato gate — terminal record (2026-10-19)

**Reported execution:** IONOS Ubuntu, SageMath 10.9 activated from `/home/bsdadmin/miniforge3/envs/sage`, using `python -u bsd389_porte_finale_kato_p16231.py` under `set -o pipefail`. The user supplied the complete successful terminal output below.

## Complete terminal record (verbatim)

```text
KATO389_GATE_START p=16231
KATO389_LOCAL_RANK2_SURJECTIVE_ORDINARY_PASS
KATO389_NORMALIZATION_LEVEL3_PRECISION_PASS ['+Infinity', '2', '2']
KATO389_REGULATOR_BSD_FACTOR_PASS 1930 9534
SAGE_METHOD_SOURCE p_primary_bound /home/bsdadmin/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/elliptic_curves/sha_tate.py ea1e3405cbf82fd3e920cedac4bec706363ec9b738eae26430c6f59360ffc708
SAGE_METHOD_SOURCE an_padic /home/bsdadmin/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/elliptic_curves/sha_tate.py ea1e3405cbf82fd3e920cedac4bec706363ec9b738eae26430c6f59360ffc708
KATO389_INSTALLED_BOUND_METHOD_SEMANTICS_PASS
KATO389_CONDITIONAL_ANALYTIC_COEFFICIENT_PASS 4486 9534
KATO389_CONDITIONAL_QUOTIENT_UNIT_PASS v_p=0 digit=1
KATO389_CONDITIONAL_SHA_P_PRIMARY_TRIVIAL_BY_PROVED_BOUND
BOUNDARY: coefficient J_ref=J_V19 still assumes trusted historic C01 machine execution
BOUNDARY: Sha.p_primary_bound(16231) NOT called; no new full L-series computation
KATO389_ARITHMETIC_GATE_PASS
EXIT_STATUS=0
```

## Precisely what passed

- Rank-2, good ordinary reduction, local Galois-surjectivity and associated mathematical prerequisites were checked on this Sage version.
- `_prec_bounds(3,3)` produced `[+Infinity,2,2]`, sufficient to transfer the level-three approximation's quadratic coefficient modulo `p²` under the documented normalization.
- The independently recomputed regulator has `Reg_p/p³ ≡1930` and the Sage-normalized BSD factor `B_p/p ≡9534` mod `p`.
- The **installed** `Sha.p_primary_bound` and `Sha.an_padic` source methods were inspected and share the above SHA-256.
- Arithmetic conditional on the archived C01 computation gives `J=4486`, correction `8335`, and therefore `A_2/p ≡9534` and `A_2/B_p ≡1` mod `p`. Thus the quotient's valuation is zero.

## Scope and outstanding publication gate

The script does **not** call the expensive `Sha.p_primary_bound(16231)` nor compute `lp.series()` at level three. It checks a *conditional* numerical coefficient obtained from the historical C01 run. The implication from `v_p(A_2/B_p)=0` to `#Sha[p^infty]≤1` follows from Sage's proven upper-bound theorem subject to its assumptions, so the arithmetic stage is **PASS**.

The end-to-end proof that the original historic compiled binary produced exactly the mathematical reference `J_ref` remains an explicit computational provenance/trust requirement. The full BSD conjecture and exact p-adic equality `u_{16231}=1` are **not** established.

**Do not confuse the printed `KATO389_CONDITIONAL_SHA_P_PRIMARY_TRIVIAL_BY_PROVED_BOUND` label with an independently executed full p-adic L-series or unconditional proof.**
