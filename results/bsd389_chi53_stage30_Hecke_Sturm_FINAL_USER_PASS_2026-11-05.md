# E389a1: authentic final Sage Stage30 Hecke–Sturm / multiplicity-one PASS

**Date:** 2026-11-05.

**Provenance:** transcript supplied verbatim by user from an activated Sage Ubuntu environment, after fixing the Sage `Integer` JSON serializer in commit `4001839dadf58cc7fe6440f446e9a22300674e68`. The assistant did not run the local Brandt-module computation. The final code exited 0 and wrote a JSON report on the user's Ubuntu host.

## Run

```bash
set -o pipefail
python -u historical/quaternion53/stage30_hecke_sturm.py 2>&1 | tee ~/bsd389_chi53_stage30_final.log
echo "STAGE30_FINAL_STATUS=$?"
```

User stdout (exact):

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
OUTPUT /home/bsdadmin/bsd389_chi53_stage30_hecke_sturm.json
ADELIC_TORIC_PERIOD_IDENTIFICATION_SEPARATE_FROM_HECKE
EXIT_STATUS_SUCCESS
STAGE30_FINAL_STATUS=0
```

## Proved by this run

For the **frozen** nonzero 33-dimensional integer Brandt vector `v`, each of the 18 Hecke operators indexed by primes ell <= 65 satisfies `T_ell v = a_ell(E)v`, using exact Sage rational matrix arithmetic, with both column and row conventions returning true in the user's run. The stacked operators `T_ell - a_ell I` have rank 32 and common kernel dimension 1. The orbit value/index correspondence with original Stage14 JSON passed, and the Stage30 JSON report was successfully emitted, exit 0.

The previously user-executed Stage22 independently passed 18 forward/inverse exact rational quaternion ideal and embedding transitions with left-ideal index 361. The 18/18 optimal-embedding check and the Stage14→frozen Brandt vector→order-nine toric norm 729 check also passed. Together these provide reproducible source-level checks for all finite quaternionic input dependencies of the conditional adelic toric-period argument in [the pre-existing proof note](../paper/389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md).

## Remaining separate theorem inputs

1. The passage from the oriented finite optimal-embedding orbit to the precise adelic toric test vector / Gross period, including representation-theoretic orientation and local conditions at 389, must still be justified through the stated mathematical comparison. The standalone Stage22 and Stage30 programs explicitly mark this as outside their individual scopes. An available theoretical proof in the existing paper asserts this bridge conditional on the finite input statements; a fully independently peer-audited automorphic test-vector identification is not supplied by this log alone.
2. The finite period `P(zeta9)` with norm 729 is not the pro-p anticyclotomic theta-element second derivative, since the C18 group algebra has idempotent augmentation ideal for p=16231. No `ord_T Theta_(f/K)=2` claim.
3. Castella–Hsieh Theorem B, under its local hypotheses, could turn a *genuine* order-two theta proof into nonzero generalized Kato class, hence Selmer corank 2; the code does not prove this.
4. No unconditional p16231 Sha triviality and no full BSD follow just from the Stage30 pass.

**Historical failure provenance:** the earlier attempt returned `STAGE30_STATUS=1` solely because Sage `Integer` objects in the report's prime list were not JSON serializable. That is superseded by the successful final retry above; the original failure is preserved in [the historical replay log](bsd389_chi53_stage22_stage30_replay_USER_2026-11-05.md).
