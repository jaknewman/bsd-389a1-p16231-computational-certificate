# Correcting the conductor in the trivial-character theta construction for 389a1

**Date:** 2026-11-05.

## Validated local input

An authenticated user Sage run of verification/bsd389_p16231_brandt_local_split_matrix_units.py returned the end-to-end status LOCAL_SPLIT_STATUS=0. It computed integral Peirce matrix units, proved all sixteen multiplication identities for the left Brandt order indexed 1, diagonalized the quadratic element omega modulo p² with p=16231, and verified an invertible Z/p² basis map with determinant 389. The corresponding report was written to the user's Ubuntu home folder. No theta coefficient is inferred.

## The crucial conductor correction

This existing local chart is attached to a **globally optimal conductor-53** embedding of K=Q(sqrt(-3)) into the quaternion algebra ramified at 389 and infinity. A local adjustment at the prime p=16231 cannot remove the embedding's conductor defect at 53: at all primes other than p the embedding/order intersection is left unchanged. Thus the naive attempt to use this chart as a base point for the *trivial-character* anticyclotomic theta would produce a CM point with an unwanted conductor-53 factor.

The correct base point requires an embedding of the **maximal quadratic order** O_K=Z[omega] in a maximal left Brandt order R_i, with omega²+omega+1=0. Its optimality is automatic: O_K is already maximal.

## Short constructive approach via quaternionic units

Let b0,...,b3 be an integral Z-basis of each Brandt left order R_i. The positive definite integer-valued quadratic form

Q(z0,z1,z2,z3) = Nrd(z0 b0 + ... + z3 b3)

has upper-triangular coefficients: diagonal Nrd(b_i), cross coefficient Nrd(b_i+b_j)−Nrd(b_i)−Nrd(b_j).

Sage's exact QuadraticForm.short_vector_list_up_to_length(2, True) enumerates **all** unit-norm elements (up to sign). A unit of trace −1 and norm 1 satisfies omega²+omega+1=0 by the reduced characteristic polynomial. This gives an exact conductor-1 optimal embedding, not a heuristic search box.

The Brandt monodromy weight w_i is half the number of units in the corresponding maximal order. An order containing O_K contains mu_6, hence its weight is divisible by 3. Preselecting the weights divisible by 3 reduces the expensive exact short-vector enumeration to the eligible orders. For discriminant 389, the usual mass formula suggests one exceptional weight-3 class, but this is deliberately checked from Sage rather than assumed.

From a resulting omega, the Hensel roots of omega²+omega+1 mod p² yield the same Peirce projector construction as the already user-certified conductor-53 chart. Verifying its 16 products and invertible four-basis determinant supplies a local chart for the **correct global conductor-1** base embedding.

The published verification script implementing these steps is:
[verification/bsd389_p16231_conductor1_CM_base_and_local_split.py](../verification/bsd389_p16231_conductor1_CM_base_and_local_split.py).

**Execution status:** code committed, NOT YET RUN on the user's Ubuntu. Its PASS lines, if they occur, will constitute a distinct certificate.

## What still needs actual mathematics

Even a successful conductor-1 embedding and local isomorphism do not yet construct the adelic Gross point classes P_n^a or their Brandt evaluations. One must still specify the global-to-local ideal representation for the p-adic unipotent matrices, compare orientations, and compute the true anticyclotomic pro-p theta coefficient in the *trivial* ring-class character branch. The norm 729 from the order-nine character at conductor 53 is a separate auxiliary Rankin-factor calculation.

No additional finite p-primary Sha theorem or BSD result follows at this stage.
