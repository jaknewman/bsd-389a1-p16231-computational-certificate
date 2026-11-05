# E389a1 p16231: first Gross P1(a=1) class — verified user run

**Date 2026-11-05.** User executed `verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py --a 1 --classify` on Sage Ubuntu, with `set -o pipefail` and `timeout 180s`.

Exact decisive stdout:

```
P1_CONDUCTOR1_SPLIT_CHART_LOADED_PASS 32
P1_CONDUCTOR1_SPLIT_CHART_SHA256 63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35
CH_P0_ALL_UNITS_BASE_CLASS32_BRANDT_VALUE_ZERO_PASS
P1_CONGRUENCE_KERNEL_INDEX_P4_PASS 1
P1_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS 1
P1_RIGHT_IDEAL_CLOSURE_16_PASS 1
P1_GLOBAL_RIGHT_BRANDT_IDEAL_PASS 1
P1_RIGHT_IDEAL_EQUALITY_WITNESS_PASS 29
P1_CONDUCTOR1_TRUE_GROSS_BRANDT_CLASS_PASS 1 29
P1_TRUE_GROSS_BRANDT_VALUE_PASS 1 -2
P1_THETA_N0_SINGLE_A_BRACKET_MODP 1 2
P1_CLASSIFY_ELAPSED_SECONDS 0.014
P1_RESULT_JSON /home/bsdadmin/bsd389_p16231_gross_P1_a1_class.json
P1_CONDUCTOR1_RIGHT_IDEAL_PILOT_PASS
P1_CLASSIFY_STATUS=0
```

After checking candidates 0 through 29, the program obtained an exact quaternionic right-ideal equivalence witness to class **29**; the frozen independently Hecke-certified vector has v[29]=-2. The conductor-one base class is 32 with v[32]=0. Thus the **individual** n=0 bracket for a=1 equals 2 modulo p. This is not the character-summed n=0 theta element and does not establish the theta derivative.

The source chart is pinned to SHA256 63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35. The full quaternionic witness itself is in the user's local JSON but was not copied into this markdown file.

Next: [p4 local split and genuine P2 ideal pilot](../verification/bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py). This is published but has not yet been executed on Ubuntu. No p-primary Sha or full BSD conclusion.
