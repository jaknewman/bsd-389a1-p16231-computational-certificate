# Authentic Ubuntu PASS: Stage14 oriented CM orbit -> Stage30 Brandt vector -> toric norm 729

**Date:** 2026-11-05. Curve E389a1; K=Q(sqrt(-3)); conductor of CM order f=53; auxiliary character chi of order 9.

**Provenance:** user's exact Ubuntu/Sage terminal output from committed
[`verification/chi53_stage14_to_order9_toric_norm729_bridge.py`](../verification/chi53_stage14_to_order9_toric_norm729_bridge.py).
This transcript is provided by the user; the assistant did not directly read the local file.

Command:

```bash
set -o pipefail
python -u verification/chi53_stage14_to_order9_toric_norm729_bridge.py \
  2>&1 | tee ~/bsd389_chi53_stage14_to_norm729.log
echo "PIPELINE_STATUS=$?"
```

Actual stdout:

```text
CHI53_STAGE14_JSON_SHA256 b0e62bc2de372919892e13b2d5910ad0af8967c7a1000b4bcb53d6db3c65f95a
CHI53_STAGE14_18_ORIENTED_ORBIT_PASS
CHI53_STAGE14_STAGE30_VECTOR_TO_STAGE23_COEFFICIENTS_PASS [0, 0, -1, 0, 0, -1, -1, 2, 2, -1, -1, 2, 2, -1, -1, 0, 0, -1]
CHI53_ORDER9_POLYNOMIAL_REDUCTION_PASS [0, -3, 0, 3, -3, -3]
CHI53_STAGE14_TO_TORIC_NORM729_PASS 729
BOUNDARY_ORBIT_RELATIONS_AND_HEECKE_EIGENVECTOR_NOT_INDEPENDENTLY_REPROVED
BOUNDARY_PRO_P_ANTICYCLOTOMIC_THETA_SECOND_DERIVATIVE_NOT_COMPUTED
BOUNDARY_SHA_P16231_NOT_PROVED_BY_THIS_TEST
PIPELINE_STATUS=0
```

### Certified by this execution

The pinned Stage14 JSON contains 18 distinct **oriented** CM embeddings, with the expected sequence of 33-class Brandt indices. Evaluating the frozen 33-dimensional integer Stage30 Brandt eigenvector at these exact indices yields the above 18 coefficients, identical to the historical Stage23 values. Reducing their polynomial P(X) modulo Phi_9(X)=X^6+X^3+1 gives [0,-3,0,3,-3,-3]. The determinant of multiplication by P(zeta_9) on the rank-6 cyclotomic integer lattice is exactly 729=3^6, proving P(zeta_9) != 0. The fixed algebraic factor is a p-adic unit at every p!=3.

### Previously verified but distinct inputs and limitations

The earlier [user-executed all-18 optimality gate](bsd389_chi53_all18_optimal_embeddings_USER_PASS_2026-11-05.md) proves optimality of the same Stage14 embeddings. The Stage22 exact rational ideal transitions and Stage30 Hecke eigenvector source checks are **not rerun by this bridge script**; the Stage30 vector is imported as a frozen constant. These identifications continue to rely on archived Stage22/Stage30 Sage computations until independently replayed. Together with those remaining data and the Waldspurger nonvanishing implication, one obtains a nonzero central Rankin value.

The order-two anticyclotomic derivative in the pro-p Iwasawa algebra is **not** computed. The finite ring-class group C18 has p-adically idempotent augmentation ideal when p=16231, so the finite polynomial's formal Taylor coefficient cannot be substituted for the missing pro-p derivative. No Sha[p16231-infinity] finiteness, triviality or all-prime BSD follows from this particular test.

**Next minimal direct validation:** rerun the already versioned Sage scripts
[`historical/quaternion53/stage22_right_ideal_class_action.py`](../historical/quaternion53/stage22_right_ideal_class_action.py) and
[`historical/quaternion53/stage30_hecke_sturm.py`](../historical/quaternion53/stage30_hecke_sturm.py), with their full output and exit codes.
