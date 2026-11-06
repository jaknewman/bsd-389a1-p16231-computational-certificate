# p16231 direct Sage/eclib versus frozen independent C++: two new pairs (user run 2026-11-06)

The user executed in their Sage-enabled Ubuntu shell:

```bash
python -u verification/bsd389_p16231_Jref_direct_sage_pair_gate.py \
  --pair 1:1 --pair 16230:16230 \
  --cpp-binary "$B" --v65-table "$T" \
  2>&1 | tee ~/bsd389_p16231_Jref_new_pairs.log
echo "JREF_STATUS=$?"
```

The user supplied these exact stdout lines:

```text
JREF_DIRECT_PARAMETER_SELFTEST_PASS
JREF_DIRECT_CUSPS_PROGRESS 1 1 4096 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 1 1 8192 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 1 1 12288 OF 16231
JREF_DIRECT_SOURCE_PAIR 1 1 u 1 kappa 0 w 1 M0 11033 M1 1335 J 14896
JREF_DIRECT_SAGE_VS_FROZEN_CPP_PASS 1 1 14896
JREF_DIRECT_CUSPS_PROGRESS 16230 16230 4096 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 16230 16230 8192 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 16230 16230 12288 OF 16231
JREF_DIRECT_SOURCE_PAIR 16230 16230 u 0 kappa 16230 w 1 M0 11031 M1 2884 J 2316
JREF_DIRECT_SAGE_VS_FROZEN_CPP_PASS 16230 16230 2316
JREF_LOCAL_PAIR_GATE_PASS 2
BOUNDARY_NO_GLOBAL_J_OR_SHA_FROM_FINITE_SPOTCHECKS
JREF_STATUS=0
```

Arithmetic: `(-1335) % 16231 = 14896`, and
`-(2884 - 16230*11031) % 16231 = 2316`.

**Assessment:** 2 additional exact direct Sage/eclib-to-C++ single-pair checks, beyond the two pre-existing oracle comparisons, pass. The second pair is symmetric with (1,0) in its J value, so these two checks do not establish global correctness. No independently verified full-domain source-to-reference comparison has been executed; the complete archived J=4486 relies on separately proved/certified Shapiro/Manin transforms and eclib reference table. This record is not a proof of Sha[16231^infinity]=0. No further spotcheck campaign is proposed; next step is a structural proof/audit of the universal identification plus the p-adic L-series normalization/precision used in Kato/Stein-Wuthrich bound.
