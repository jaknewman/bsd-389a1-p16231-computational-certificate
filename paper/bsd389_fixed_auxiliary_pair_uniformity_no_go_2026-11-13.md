# E389a1: no finite fixed set of auxiliary Kurihara conductors can cover all large p

**2026-11-13. Theorem proved by elementary integer arithmetic.** No claim of BSD, Sha finiteness or nonvanishing of an actual Kurihara number.

Let E/Q be 389a1: y²+y=x³+x²−2x. For an odd good auxiliary prime q, let a_q=q+1−#E(F_q). For p≥5 prime, p≠q, the standard congruence part of Kurihara p-admissibility is

- q≡1 (mod p);
- a_q≡q+1≡2 (mod p).

Define the *fixed auxiliary admissibility integer*

$$A(q)=\gcd(q-1,a_q-2)>0.$$

Then the pair of congruences holds **if and only if** p|A(q). For a fixed pair of distinct good auxiliary primes q₁,q₂, both are admissible **if and only if**

$$p\mid D(q_1,q_2),\qquad D(q_1,q_2)=\gcd(A(q_1),A(q_2))>0.$$

In particular, only finitely many rational primes p can satisfy this condition for a *fixed* q-pair. If a finite set of distinct pairs is fixed, the union of their sets of qualifying p is finite as well. Thus any hoped-for all-sufficiently-large-p proof using **the same finite list of individual two-prime Kurihara coefficients** fails at the admissibility stage. This does not rule out a genuinely p-independent *global arithmetic/cohomological invariant* whose specialization at p is evaluated with **p-dependent** auxiliary primes.

## Exact independent arithmetic on the three archived pairs

For E, completing the square yields (2y+1)²=4x³+4x²−8x+1. For odd good prime q:

$$a_q=-\sum_{x\in\mathbf F_q}\left(\frac{4x^3+4x^2-8x+1}{q}\right).$$

The pure-Python verifier counts every x exactly (including zero discriminants) and computes the gcds, with results:

| (q₁,q₂) | (a_q1,a_q2) | (A(q₁),A(q₂)) | D | prime divisors of D ≥5 |
|---|---|---|---|---|
| (41,61) | (-3,-8) | (5,10) | 5 | 5 |
| (113,673) | (9,2) | (7,672) | 7 | 7 |
| (369793,383917) | (2,-854) | (369792,428) | 428=4·107 | 107 |

See the companion self-contained verification source [fixed-pair arithmetic](../verification/bsd389_fixed_auxiliary_pair_uniformity_obstruction.py). These are *admissibility* checks, **not Kurihara coefficient computations**. An actual unit coefficient for p=107 is separately discussed with provenance limitations in the prior archive audit.

## What this theorem changes in the uniform Sha strategy

A *finite fixed inventory of conductor-specific Kurihara residues* cannot yield all-large-p nonvanishing because each conductor has finitely many possible admissible p. A valid alternative must either:

1. Build a genuinely p-independent global *integral arithmetic/cohomological class or morphism*, and establish a non-circular comparison with the **actual** Sha/Selmer obstruction at all but finitely many p, while allowing q₁(p),q₂(p) to vary; or
2. Prove a direct prime-uniform nonvanishing theorem for a p-dependent auxiliary pair, beyond the current local Mordell–Weil Chebotarev independence.

Neither construction is supplied here. A primitive Mordell–Weil exterior generator or a fixed Hecke-lattice minor **does not** control Sha by itself; the missing comparison is precisely the arithmetic gap.

The exact good-p equivalence between 2-prime Kurihara unit witnesses and p-primary Sha vanishing is recorded separately in [the project criterion](bsd389_exact_good_prime_equivalence_rank2_two_Kurihara_unit_and_Sha_zero_2026-11-02.md). This note proves a necessary restriction on *uniform proof architecture*, not the desired uniform theorem.