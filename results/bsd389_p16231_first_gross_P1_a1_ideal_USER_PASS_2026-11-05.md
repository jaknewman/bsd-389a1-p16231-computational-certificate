# Genuine Gross-point right ideal P_1^1 for E389a1, K=Q(sqrt(-3)), p=16231 — USER PASS

**Date:** 2026-11-05. The following output is pasted verbatim by the user from Sage-enabled Ubuntu. This is the actual user's execution, not an assistant remote execution.

**Script:** [verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py](../verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py).

## Authentic stdout

```text
P1_CONDUCTOR1_SPLIT_CHART_LOADED_PASS 32
P1_CONDUCTOR1_SPLIT_CHART_SHA256 63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35
CH_P0_ALL_UNITS_BASE_CLASS32_BRANDT_VALUE_ZERO_PASS
P1_CONGRUENCE_KERNEL_INDEX_P4_PASS 1
P1_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS 1
P1_RIGHT_IDEAL_CLOSURE_16_PASS 1
P1_GLOBAL_RIGHT_BRANDT_IDEAL_PASS 1
P1_CLASSIFICATION_NOT_REQUESTED
P1_RESULT_JSON /home/bsdadmin/bsd389_p16231_gross_P1_a1_ideal.json
P1_CONDUCTOR1_RIGHT_IDEAL_PILOT_PASS
BOUNDARY_ONLY_P1_NOT_P2; NO_ACTUAL_THETA_MOMENT_YET
P1_PILOT_STATUS=0
```

## Scope of the exact calculation

Starting from the true conductor-one optimal CM embedding in Brandt left order R_32 and its locally split p-adic matrix chart, the script constructs the scaled Gross right ideal J_1(1)=p P_1^1 by solving the two integral congruences mod p². The solution lattice has index p^4 in the maximal order. A separate inverse-matrix reconstruction yields the same integer HNF lattice. Sixteen exact tests verify stability under right multiplication by an order basis. Multiplication by the original right Brandt ideal I_32 yields a right ideal of the common Brandt base order.

The chart was pinned to the SHA256 **63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35** of the actual user-generated conductor-one CM local-chart JSON; this prevents accidental use of the earlier conductor-53 embedding.

The script also uses the frozen independently checked Hecke eigenvector coordinate v[32]=0 to establish phi_f(P_0^a)=0 for every p-adic unit a.

## What remains

- The Brandt class of P_1^1 was NOT computed because the user ran the source with `--a 1` but without the optional `--classify` flag. Hence no numerical nonzero/zero value of phi_f(P_1^1) has been measured.
- The `P_2^a` Gross ideals require p^4 local precision and have not yet been constructed.
- Even a successful classification of one Gross point will not itself prove a quadratic theta leading coefficient or a finite p-primary Sha theorem.

The next optional computation is the existing `--a 1 --classify` branch, which tests right-equivalence against all 33 Brandt classes. This could be expensive and should be externally timeout-guarded; report timeout explicitly as INCOMPLETE, not as an arithmetic failure.
