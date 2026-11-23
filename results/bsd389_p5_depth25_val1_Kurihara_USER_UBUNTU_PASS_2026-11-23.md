# E389a1 — user Ubuntu independently reproduced 34,775,000-term p5-depth25 valuation-one Kurihara certificate

**Date: 2026-11-23.** User's original Ubuntu `sage` Conda terminal (verbatim) running:

```bash
/tmp/bsd389_p5_val1 > /tmp/bsd389_p5_val1_hist.txt
python -u verification/bsd389_p5_depth25_valuation1_Fitting_gate.py \
 --hist /tmp/bsd389_p5_val1_hist.txt
```

Actual user stdout:

```text
TRUE_MOD25_VALUATION1_HECKE_AND_QUOTIENT_FILT_GATE_PASS conductor 69568351 reps 34775000 q_point_counts (5375, 13075) q_traces (-23, -73) primitive_roots (11, 3) c0_c1_c2_c3 [0, -108600, -993960, -6066100] delta_mod25 15 delta_mod5 0
LOCAL_RING_THEOREM theta_image_in_Z25_T_MOD_T3 = 15*T^2 !=0
LOCAL_RING_THEOREM (5,T)^4_killed => theta_notin_(5,T)^4
PUBLISHED_BULLACH_HONNOR_FITTING => minimal_R_generators_at_most_3
RESTRICTION_TO_Q => dim_Sha_Q_5 <=1
DOKCHITSER_P_PARITY_PLUS_CASSELS_TATE => dim_Sha_Q_5 even => zero
AUTHENTIC_VALUATION1_INTEGER_RESULTANT_AND_SMITH_PASS resultant_digits 89 v5_B 8 normalized_mod5 0 v5_normalized 4 sqrt_B 224595822642553414416922351284439356643840000 center 24 p_smith_valuations [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]
IMPORTANT_NO_INFERENCE_OF_SHA_K_ZERO_AT_VALUATION_ONE
UNIFORM_GOAL_FOR_ALL_LARGE_P: SOME_P2_DEEP_TWO_PRIME_DELTA_NOT_ZERO_MOD_P2
BOUNDARY_NO_ALL_PRIME_EXISTENCE_OR_EXACT_COMPLEX_BSD
```

The gate verifies the user's independently generated complete original 25-integer histogram, genuine curve point counts, roots, quadratic coefficient and exact integer resultant & symmetric Mazur--Tate matrix Smith invariants. The **theorem implication** `Sha(E/Q)[5∞]=0` follows from external Bullach–Honnor Fitting + p-parity and is NOT a direct software computation of Sha. No claim `Sha(E/K)[5∞]=0` for the new conductor.

Follow-up NEW assistant-only calculation of all 20 r-orientations at this same user-reproduced conductor appears in:
`paper/bsd389_val1_20_new_degree25_rank_stable_fields_416_twisted_L_nonzero_2026-11-23.md`. That all-r extension has NOT been user rerun yet.
