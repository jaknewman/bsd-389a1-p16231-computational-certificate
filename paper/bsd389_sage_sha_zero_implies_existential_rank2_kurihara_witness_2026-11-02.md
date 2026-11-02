# E389a1: Sage-certified p-primary Sha zero implies existence of an authentic degree-two Kurihara unit (without the native algorithm)

**Date:** 2026-11-02.

## Statement

Let E be 389a1, E(Q) of certified rank 2 and rational torsion 1, conductor 389 and product of Tamagawa factors 1. Fix a good prime p>=5 with surjective residual representation and optimal Manin constant a p-unit, such that the Chan-Ho Kim Theorem 1.8 and Castella–Sano Theorem B hypotheses hold (ordinary p or supersingular p with squarefree conductor). Assume an independent rigorous upper-bound method has proved `Sha(E/Q)[p^infinity]=0`.

**Then there exist distinct p-admissible auxiliary primes q1,q2 with the correctly Néron-normalized two-prime Kurihara element `delta_(q1 q2) != 0 mod p`.**

In particular p=107 is covered by the user's genuine SageMath 10.9 `p_primary_bound(107)=0` execution, *independently of the native 710-block dataset*.

## Proof

The p-primary Kummer exact sequence and rank 2 give

`Sel_(p∞)(E/Q) = E(Q) ⊗ (Q_p/Z_p) ≅ (Q_p/Z_p)^2`

and hence its Pontryagin dual X_p is isomorphic to `Z_p²`. Therefore `Fitt_(2,Z_p)(X_p) = Z_p`.

Castella–Sano Theorem B supplies `partial^(infinity)(delta)=v_p(Tam_E)=0`. The nonzero Kurihara family allows Kim Theorem 1.8, and its Fitting formula with Selmer corank 2 gives

`Z_p=Fitt_2(X_p)=p^(partial^(2)(delta)-partial^(infinity)(delta)) Z_p=p^(partial^(2)(delta))Z_p`.

Thus `partial^(2)(delta)=0`. By Kim's definition of the minimum over two-prime admissible products, an actual **two-prime degree-two unit** occurs. QED.

## What this does and does NOT certify

- **YES, independently of the native p107 computation:** at least one genuine correctly normalized p107 Kurihara degree-two unit witness exists. This is a new arithmetic *consequence* of the Sage p-primary certificate plus published theorems, not an original theorem stronger than them.
- **NO:** the theorem does not identify those q1,q2. It does not independently validate that the historical particular pair q1=369793, q2=383917 has `delta=34`. The frozen 710-block reaggregation proves stored data consistency, not correctness of the original full native 70.98bn summand generation.
- **NO:** the theorem does not imply existence uniformly for all sufficiently large p. It gives witnesses only for independently certified p. Extending the conclusion to all p without proving the corresponding Sha triviality would be circular.
- **YES for other Sage-certified p:** the same argument applies under verified assumptions for p=5,7,11,13. The user has Sage `p_primary_bound(p)=0` for each, but this theorem does not depend on reproducing their original Kurihara sums.
- **NO for p2 or p3 through this statement:** p2 and p3 lie outside the specified p>=5 theorem hypotheses; their separate 2-Selmer / Heegner results are unaffected.

## Primary literature and executed evidence

- Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8 and the definition of Kurihara partial invariants: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Actual user Sage transcript: [results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md](../results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md)
- Existing precise Kim/CS criterion: [paper/bsd389_exact_good_prime_equivalence_rank2_two_Kurihara_unit_and_Sha_zero_2026-11-02.md](bsd389_exact_good_prime_equivalence_rank2_two_Kurihara_unit_and_Sha_zero_2026-11-02.md).
