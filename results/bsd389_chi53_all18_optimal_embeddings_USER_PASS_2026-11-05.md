# Authentic user Ubuntu Sage PASS: all 18 conductor-53 oriented optimal embeddings

**Date:** 2026-11-05. **Curve:** 389a1. **K:** Q(sqrt(-3)). **Order:** Z+53 O_K.

Source script: [verification/chi53_optimal_embedding_one_fraction_criterion.py](../verification/chi53_optimal_embedding_one_fraction_criterion.py).

**Provenance:** exact output pasted by user from Sage-enabled Ubuntu. The user executed the GitHub script against their original local `~/bsd389_chi53_stage14_orbit19.json` Stage14 archive and Sage BrandtModule(389) data. The assistant has not accessed the original private JSON or recomputed all 18 rational quaternion coordinates on this machine.

```text
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 0 BRANDT_CLASS 1 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 1 BRANDT_CLASS 2 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 2 BRANDT_CLASS 9 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 3 BRANDT_CLASS 23 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 4 BRANDT_CLASS 22 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 5 BRANDT_CLASS 11 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 6 BRANDT_CLASS 4 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 7 BRANDT_CLASS 19 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 8 BRANDT_CLASS 31 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 9 BRANDT_CLASS 16 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 10 BRANDT_CLASS 15 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 11 BRANDT_CLASS 31 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 12 BRANDT_CLASS 19 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 13 BRANDT_CLASS 11 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 14 BRANDT_CLASS 4 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 15 BRANDT_CLASS 23 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 16 BRANDT_CLASS 22 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 53]
CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS 17 BRANDT_CLASS 10 MAXIMAL_ORDER_GENERATOR_DENOMS [1, 53, 53, 1]
CHI53_ALL_18_OPTIMAL_EMBEDDINGS_PASS
CHI53_INITIAL_GROSS_POINT_CONDUCTOR_EXACTLY_53_PASS
BOUNDARY: optimality only; use archived stage22 and stage30 for the remaining arithmetic data.
OPTIMALITY_STATUS=0
```

## Exact interpretation

For each of the 18 oriented embeddings of Z[q_k] into the Brandt left order R_k, the script verifies `q_k²−q_k+2107=0`, so `omega_k=(q_k−27)/53` satisfies `omega_k²+omega_k+1=0`. The maximal order O_K=Z[omega_k], while O_53=Z[q_k]. Because f=53 is prime, the only possible intersections of K with R_k containing O_53 are O_53 and O_K. The exact rational-coordinate test finds at least one denominator 53 for every omega_k in an integral Z-basis of R_k, so omega_k is **not** in R_k. Thus all 18 intersections are exactly O_53, proving all 18 embeddings optimal.

Repeated Brandt indices (31,19,11,4,23,22) are compatible with distinct oriented optimal embeddings; deduplicating by index would be invalid for a toric orbit.

## Remaining provenance and mathematical boundary

The PASS verifies the optimality input used in the archived [Gross–Waldspurger period argument](../paper/389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md). It does **not** independently replay Stage22 rational-ideal transports, Stage23 toric coefficients, or Stage30 the 33-dimensional Hecke eigenvector/Jacquet–Langlands identification. It strengthens these inputs by replacing the prior Stage29 local-conductor reliance with a directly user-executed, short exact test for each embedding.

Under those remaining archived identifications, the order-nine finite toric period is nonzero and therefore Waldspurger implies the corresponding central Rankin value is nonzero. The nonvanishing of the **anticyclotomic pro-p theta second derivative**, `ord_T Theta_(f/K)=2`, remains unproved; finite class group C18 cannot supply it because its Z_p-augmentation ideal is idempotent when p=16231. There is no new unconditional Sha[p16231∞] vanishing, no uniform all-prime Sha support bound, and no full BSD proof from this output.

The local stdout transcript has no independent SHA256 authentication of the user's private source JSON; this document honestly records the exact user-supplied run.
