# Independent native V11 / V65 / Sage-eclib local n=3 analytic bridge — PASS

**Execution:** User-supplied IONOS Sage-shell transcript, 2026-10-24. Actual run of `verification/local_level3_native_eclib_oracle.py --a 1 --b 0`, exit 0. This is not an unperformed proposed test. The source file is archived in the repository.

## Complete reported output

```text
LOCAL_NATIVE_V65_CONTRACTION 1 0 sparse_slots 4 J_mod_p 2316
LOCAL_LEVEL3_PROGRESS 1 0 lifts_done 1
LOCAL_LEVEL3_PROGRESS 1 0 lifts_done 4096
LOCAL_LEVEL3_PROGRESS 1 0 lifts_done 8192
LOCAL_LEVEL3_PROGRESS 1 0 lifts_done 12288
LOCAL_LEVEL3_PROGRESS 1 0 lifts_done 16231
LOCAL_NATIVE_DIRECT_ECLIB_J_PASS 1 0 2316
LOCAL_SAGE_HECKE_DISTRIBUTION_PASS 1 0
LOCAL_SAGE_LEVEL3_MINUS_LEVEL2_PASS 1 0 difference_mod_p2 227347617 J_over_4alpha2_mod_p 14007
LOCAL_INDEPENDENT_ANALYTIC_C01_BRIDGE_PASS 1 0
BOUNDARY: verified a single x=a+p*b, not the sum over p(p-1) residues
EXIT_STATUS=0
```

## Verification and implications

For `p=16231`, `alpha mod p=128`, `p^2=263445361`, the independent direct coefficient difference at the single residue `x=1` is

`227347617=16231*14007 (mod p^2)`.

The original SHA-pinned V11 one-pair native producer, contracted with separately generated SHA-pinned V65 eclib table (4 sparse slots), gives `J(1,0)=2316 (mod p)`. Sage eclib directly recomputed all `p=16231` level-three lifts `1+p^2 c` and checked

`(A2^(3)-A2^(2))_(1,0) = p*J(1,0)/(4*alpha^2) (mod p^2)`,

including the `1/2` binomial and `1/2` real-components factors.

The test separately checked the exact distribution relation between level 3 and level 2 at this residue. This is independent of the formal C01–Sage paper insofar as the n3 loop evaluates the original eclib modular symbol at every level-three lift (not a substitution of the closed-form expected answer).

**Important boundary:** A single residue is a local analytic oracle. It does not compute or independently recheck all `263429130` outer residue pairs, does not produce `lp.series(n=3)` globally, and does not independently execute `Sha.p_primary_bound(16231)`. The full-sha conclusion remains dependent on the authentic global C01 numeric computation and the source-level identity.
