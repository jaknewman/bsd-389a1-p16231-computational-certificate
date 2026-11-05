# E389a1 conductor 53: real Ubuntu Stage22 PASS, Stage30 mathematical PASS with JSON export error

**Date:** 2026-11-05. **Source:** exact stdout pasted by user from activated Sage Ubuntu shell. The assistant did not run the actual Sage scripts remotely.

## Stage22: user replay success, exit status 0

Script: [historical/quaternion53/stage22_right_ideal_class_action.py](../historical/quaternion53/stage22_right_ideal_class_action.py).

For k=0,...,17, all reported exact quaternionic left-ideal index checks `J_INDEX 361`, forward rational ideal equality and embedding transport, and inverse checks reported `PASS`. The ordered 18 transitions were:

```text
0 1 -> 2
1 2 -> 9
2 9 -> 23
3 23 -> 22
4 22 -> 11
5 11 -> 4
6 4 -> 19
7 19 -> 31
8 31 -> 16
9 16 -> 15
10 15 -> 31
11 31 -> 19
12 19 -> 11
13 11 -> 4
14 4 -> 23
15 23 -> 22
16 22 -> 10
17 10 -> 1
STAGE22_RIGHT_IDEAL_DOUBLE_CLASS_18_PASS
STAGE22_EMBEDDING_TRANSPORT_18_PASS
STAGE22_INVERSE_TRANSPORT_18_PASS
ADELIC_ORIENTATION_AT_389_OPEN
WALDSPURGER_TEST_VECTOR_OPEN
OUTPUT /home/bsdadmin/bsd389_chi53_stage22_adelic_right_ideals.json
STAGE22_STATUS=0
```

This directly validates exact rational ideal and embedding transport on the original source data; the status messages about adelic orientation / Waldspurger test vector identify theorem-level identification not automatically established by Stage22.

## Stage30: all mathematical checks completed, report writing FAILED

Script: [historical/quaternion53/stage30_hecke_sturm.py](../historical/quaternion53/stage30_hecke_sturm.py).

The real user stdout:

```text
STAGE30_ORBIT_COORDINATES_MATCH_PASS
STAGE30_STURM_BOUND 65 PRIMES [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
HECKE_PRIME 2 A_ELL -2 COLUMN True ROW True
HECKE_PRIME 3 A_ELL -2 COLUMN True ROW True
HECKE_PRIME 5 A_ELL -3 COLUMN True ROW True
HECKE_PRIME 7 A_ELL -5 COLUMN True ROW True
HECKE_PRIME 11 A_ELL -4 COLUMN True ROW True
HECKE_PRIME 13 A_ELL -3 COLUMN True ROW True
HECKE_PRIME 17 A_ELL -6 COLUMN True ROW True
HECKE_PRIME 19 A_ELL 5 COLUMN True ROW True
HECKE_PRIME 23 A_ELL -4 COLUMN True ROW True
HECKE_PRIME 29 A_ELL -6 COLUMN True ROW True
HECKE_PRIME 31 A_ELL 4 COLUMN True ROW True
HECKE_PRIME 37 A_ELL -8 COLUMN True ROW True
HECKE_PRIME 41 A_ELL -3 COLUMN True ROW True
HECKE_PRIME 43 A_ELL 12 COLUMN True ROW True
HECKE_PRIME 47 A_ELL -2 COLUMN True ROW True
HECKE_PRIME 53 A_ELL -6 COLUMN True ROW True
HECKE_PRIME 59 A_ELL 3 COLUMN True ROW True
HECKE_PRIME 61 A_ELL -8 COLUMN True ROW True
STAGE30_COMMON_COLUMN_EIGENSPACE_RANK 32 NULLITY 1
STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS
```

Then traceback:

```text
File "historical/quaternion53/stage30_hecke_sturm.py", line 72, in <module>
  out.write_text(json.dumps(report,indent=2)+'\n')
TypeError: Object of type Integer is not JSON serializable
STAGE30_STATUS=1
```

**Important distinction:** all Sturm/Hecke mathematics completed and passed, but the script exited 1 because of a Sage Integer in the JSON `primes` list. The serialized report file is not certified to exist from this execution. Thus don't record this exact Stage30 attempt as an end-to-end exit-zero PASS.

## Fix committed

[Fix commit 4001839](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/commit/4001839dadf58cc7fe6440f446e9a22300674e68) converts `'primes':primes` into `'primes':[int(ell) for ell in primes]` before JSON serialization. All other JSON values were already converted to ordinary Python types. **Not yet rerun after patch** as of this note.

The expected new successful end messages are:

```text
STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS
OUTPUT /home/bsdadmin/bsd389_chi53_stage30_hecke_sturm.json
ADELIC_TORIC_PERIOD_IDENTIFICATION_SEPARATE_FROM_HECKE
EXIT_STATUS_SUCCESS
STAGE30_STATUS=0
```

A successful retry would finish the source/JSON Hecke provenance for the 33-dimensional Brandt eigenvector. The nonzero toric factor `Norm P(zeta9)=729` is independently certified; identifying it with a Waldspurger period still requires its automorphic and local-test-vector hypotheses. No pro-p anticyclotomic theta second derivative and no new full Sha proof is established by this stage.


## FINAL RETRY UPDATE — STAGE30 STATUS 0 (2026-11-05)

The previous JSON-export failure above is now superseded by a **new user-executed end-to-end PASS** of the corrected script. The new run printed `STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS`, successfully wrote `/home/bsdadmin/bsd389_chi53_stage30_hecke_sturm.json`, printed `EXIT_STATUS_SUCCESS`, and returned `STAGE30_FINAL_STATUS=0`.

For the **full verbatim 18-prime Hecke log**, see [Stage30 FINAL USER PASS](bsd389_chi53_stage30_Hecke_Sturm_FINAL_USER_PASS_2026-11-05.md). This earlier file preserves the actual first failure as historical provenance; it must not be mistaken for the present status.
