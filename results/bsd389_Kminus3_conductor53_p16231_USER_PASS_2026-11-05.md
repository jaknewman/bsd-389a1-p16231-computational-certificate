# 389a1: authentic user Ubuntu PASS — ring-class conductor 53 and rational L-value interval

**Date:** 2026-11-05.

**Provenance:** the following two command transcripts are copied verbatim from the user's Sage-enabled Ubuntu shell. The assistant did not remotely run the programs or access the user's local log files. The scripts are versioned under `verification/`.

## 1. Exact ring-class and ordinary-prime gate

Command:

```bash
set -o pipefail
python -u verification/bsd389_Kminus3_conductor53_p16231_ringclass_gate.py \
  2>&1 | tee ~/bsd389_chi53_p16231_gate.log
```

Actual user stdout:

```text
RINGCLASS_MINUS3_CONDUCTOR53_ORDER_PASS 18
RINGCLASS_NORM19_GENERATOR_ORDER18_PASS
K_MINUS3_389_INERT_P16231_SPLIT_PASS
RINGCLASS_PI_EQUALS_25_G4_MOD53_PASS
RINGCLASS_P16231_FROBENIUS_ORDER9_PASS
CASTELLA_HSIEH_CHI_PBAR_NONTRIVIAL_PASS
E389A1_AP16231_ORDINARY_PASS 128
RINGCLASS_53_P16231_ARITHMETIC_CERTIFICATE_PASS
BOUNDARY_L_E_MINUS3_AND_L_E_OVER_K_CHI_NONVANISHING_NOT_PROVED
BOUNDARY_ANTICYCLOTOMIC_THETA_ORDER2_NOT_PROVED
BOUNDARY_SHA_P16231_NOT_PROVED
```

Mathematical scope: K=Q(sqrt(-3)), conductor 53 ring-class group has order 18, the norm-19 class is a generator, a prime above 16231 has class of order 9, the chosen anticyclotomic order-nine character is nontrivial there, and a_16231=128 proves ordinary reduction. The `BOUNDARY_L_E_MINUS3...` is the scope of THIS first script alone; the twist nonvanishing is proved independently by the second script below.

## 2. Rigorous rational interval for the -3 quadratic twist

Command:

```bash
python -u verification/bsd389_Kminus3_twist_Lvalue_rational_interval.py \
  2>&1 | tee ~/bsd389_twist_minus3_interval.log
```

Actual user stdout:

```text
E389A1_ROOT_PLUS_AND_TWIST_MINUS3_ROOT_PLUS_PASS
TWIST_CONDUCTOR 3501
RATIONAL_PARTIAL_INTERVAL 4.552573780109 4.555645450723
RATIONAL_TAIL_UPPER 0.039997400578
L_E_MINUS3_1_RATIONAL_INTERVAL_PASS 4.51 < L < 4.60
L_E_MINUS3_1_PROVABLY_NONZERO_PASS
BOUNDARY_L_E_OVER_K_CHI_AND_THETA_ORDER2_NOT_PROVED
BOUNDARY_SHA_P16231_NOT_PROVED
```

After these two commands the user ran:

```text
PIPELINE_STATUS=0
```

The exact Fraction comparisons within the second verifier, combined with the standard modular L-series functional equation, prove

```text
4.51 < L(E^(-3),1) < 4.60
```

without BSD or a Sha-finiteness hypothesis. Displayed decimal endpoints are diagnostics; the code asserts exact rational comparisons. The previous October 26 work already contained a coarser rational positive interval, so this is a **genuine new independent user execution / tighter reproduction**, not a claim that the nonvanishing was first discovered today.

## 3. Open gates: not proved by these two programs

- The central Rankin factor `L(E/K,chi_9,1)` from the historical conductor-53 Gross orbit is conditional on the archived quaternionic optimal-embedding, class action and Jacquet–Langlands test-vector identification; this user run does not independently replay those inputs.
- The anticyclotomic pro-p theta leading order `ord_T Theta_(f/K)=2` is NOT determined by the finite order-18 ring-class polynomial. At p=16231 the finite group algebra has idempotent augmentation ideal, whereas the anticyclotomic Z_p-tower has a genuine augmentation filtration.
- A nonzero generalized Kato class, even if separately proved, controls Selmer corank (and possible Sha[p∞] finiteness), not automatically its finite p-torsion or full BSD.
- No unconditional Sha[16231∞]=0 result and no all-prime Sha finiteness result follow from these two scripts.

## Next shortest provenance gate

The short Sage file [verification/chi53_optimal_embedding_one_fraction_criterion.py](../verification/chi53_optimal_embedding_one_fraction_criterion.py) tests the conductor-53 optimality of all 18 actual oriented embeddings based on the existing `~/bsd389_chi53_stage14_orbit19.json` file. Its syntax error was fixed in commit 0940099320acc0924ddfb9e7e70d0a0cfa0af33b. Run it on Ubuntu only if that original Stage 14 JSON exists; it is not part of the two PASS outputs above.

Related mathematical notes: [p16231 CH gates](../paper/bsd389_Kminus3_conductor53_p16231_Castella_Hsieh_exact_gates_2026-11-05.md); [finite C18 theta no-go](../paper/bsd389_chi53_C18_augmentation_idempotent_no_theta2_2026-11-05.md).
