# Direct Sage/eclib J_ref pair oracle — authentic Ubuntu user run (2026-11-06)

Source script: `verification/bsd389_p16231_Jref_direct_sage_pair_gate.py` (PR #10).
Executor: user on Ubuntu, in active Sage environment.
Scope: two exact *direct cusp-symbol* pairs, no Shapiro, V65/Manin contraction or full global J re-sum.

Command:

```bash
set -o pipefail
python -u verification/bsd389_p16231_Jref_direct_sage_pair_gate.py \
  --pair 1:0:2316 --pair 2:3:11725 \
  2>&1 | tee ~/bsd389_p16231_Jref_direct.log
```

Verbatim terminal output supplied by user:

```text
JREF_DIRECT_PARAMETER_SELFTEST_PASS
JREF_DIRECT_CUSPS_PROGRESS 1 0 4096 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 1 0 8192 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 1 0 12288 OF 16231
JREF_DIRECT_SOURCE_PAIR 1 0 u 0 kappa 0 w 16230 M0 11031 M1 2316 J 2316
JREF_DIRECT_ARCHIVED_ORACLE_PASS 1 0 2316
JREF_DIRECT_CUSPS_PROGRESS 2 3 4096 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 2 3 8192 OF 16231
JREF_DIRECT_CUSPS_PROGRESS 2 3 12288 OF 16231
JREF_DIRECT_SOURCE_PAIR 2 3 u 11169 kappa 11458 w 3053 M0 11034 M1 5197 J 11725
JREF_DIRECT_ARCHIVED_ORACLE_PASS 2 3 11725
JREF_LOCAL_PAIR_GATE_PASS 2
BOUNDARY_NO_GLOBAL_J_OR_SHA_FROM_FINITE_SPOTCHECKS
```

Independent arithmetic consistency checks (can be reproduced in Python):

- Pair (1,0): `-16230*(2316-0*11031) mod 16231=2316`.
- Pair (2,3): `-3053*(5197-11458*11034) mod 16231=11725`.
- The expected two oracle values predate this run. The test does *not*
  compare to the archived C++ binary on newly chosen pairs.

**Proof boundary:** A finite number of direct cusp evaluations, even when
all correct, cannot certify the sum over all 263,429,130 pairs or prove
the analytically normalized n=3 cyclotomic coefficient. The bridge
`J_computed=4486=J_ref` and the resulting triviality of Sha[16231^infinity]
remain conditional on the full source/moment identities and archived data
provenance, or an independent provable p-primary bound.
