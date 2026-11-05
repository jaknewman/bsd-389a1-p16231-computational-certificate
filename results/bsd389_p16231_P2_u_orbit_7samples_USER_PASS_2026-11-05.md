# User-executed: seven genuine P2 Gross-point classes along the 1+p orbit

Date: 2026-11-05; Sage Ubuntu; `P2_ORBIT_STATUS=0`.

Source: [verification/bsd389_p16231_P2_u_orbit_first_samples.py](../verification/bsd389_p16231_P2_u_orbit_first_samples.py). User executed with `timeout 240s` and `set -o pipefail`.

All seven sample points passed the genuine p4 Hensel local chart, p8-index two-congruence lattice, independent preimage, 16 right order closure identities, and exact right-ideal class witness.

| i | a=(1+16231)^i mod p² | right Brandt class | v[class] | individual bracket modulo p |
|---:|---:|---:|---:|---:|
| 0 | 1 | 9 | -1 | 15976 |
| 1 | 16232 | 15 | -1 | 15976 |
| 2 | 32463 | 21 | 1 | 15974 |
| 3 | 48694 | 9 | -1 | 15976 |
| 4 | 64925 | 11 | -1 | 15976 |
| 8 | 129849 | 17 | 0 | 15975 |
| 16 | 259697 | 23 | 0 | 15975 |

Terminal ending:

```text
THETA_N1_P1_PART_CANCELS_MODP_FOR_T_POWER 0
THETA_N1_P1_PART_CANCELS_MODP_FOR_T_POWER 1
THETA_N1_P1_PART_CANCELS_MODP_FOR_T_POWER 2
P2_ORBIT_SAMPLES_ONLY_NOT_FULL_THETA_MOMENT 7
P2_ORBIT_SAMPLES_JSON /home/bsdadmin/bsd389_p16231_P2_u_orbit_sample_residue1.json
P2_U_ORBIT_FIRST_SAMPLES_PASS 7 SECONDS 0.176
BOUNDARY_C2_SUM_OVER_ALL_I_AND_A_NOT_COMPUTED
BOUNDARY_THETA_ORDER_TWO_NOT_PROVED
P2_ORBIT_STATUS=0
```

The sample is not a full i sum and does not imply nonzero theta quadratic coefficient. The proven P1 cancellation uses only the mod-p hockey-stick identity, not exact integral vanishing.

A new [restartable full-i orbit chunk/aggregation program](../verification/bsd389_p16231_P2_u_orbit_chunked_moments.py) is published but not yet user-executed.
