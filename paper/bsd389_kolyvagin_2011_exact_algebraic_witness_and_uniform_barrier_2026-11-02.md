# E389a1: Stein 2011 algebraic Kolyvagin computation, p3 witness, and uniformity boundary

Date: 2026-11-02.

## Primary source (2011)

William Stein, *Kolyvagin's Conjecture for Specific Higher Rank Elliptic Curves*, 26 March 2011:
https://wstein.org/papers/kolyconj2/kolyconj.pdf

Compared to the 2009 preliminary exposition, this paper presents a fully algebraic modular-curve / supersingular quaternionic algorithm. Its **Algorithm 2.1** (printed pp. 3–4) computes the reduction of the derived Heegner class up to a fixed nonzero scalar. **Remark 2.2** explicitly emphasizes that it uses no numerical approximation. The author reports that Sage implementation was reviewed by John Cremona for inclusion (footnote adjacent to Table 8.1, printed p. 27).

In **Table 8.2** (printed p. 29), the row `E=389a1, D=-7, p=3, ell=5` gives supersingular-divisor-module dimension 130, `max c=19031`, `z=0` count 152 and `z != 0` count 121. Among the listed first nonzero values are `c=41,59,83,587`. The special `c=41` datum confirms the p3 published witness used by the earlier 2009 preliminary paper.

**Evidence category:** literature-authored exact-algorithm computation, NOT independently recomputed by the user. The user's authentic Sage 10.9 preflight validates splitting/inertness, a41=-3, and #E(F5)=9, but does not calculate the nonzero quaternionic Heegner derivative. The 2011 Table 8.2 datum is independent of the user's Sage preflight only in mathematical construction/provenance; do not describe it as a fresh independent user execution.

## The rank-one uniformity trap (rigorous exclusion)

For any quadratic imaginary K, `E(Q)⊂E(K)`, hence `rank E(K)>=2` because E389a1 has saturated rational rank 2. The classical Gross–Zagier–Kolyvagin *non-torsion basic Heegner point* theorem implies `rank E(K)=1`. Its hypothesis cannot hold for 389a1 over any Heegner K. This is why `Sha.bound_kolyvagin` (classical rank-one) cannot furnish the desired uniform finite support here, and why higher derived Kolyvagin classes enter Stein's calculations.

The proof of p3 vanishing **via Stein's Theorem 2.7 (2009 version)** must preserve all standing local and Selmer hypotheses, including the algebraic rank-two property; nonvanishing alone with unconstrained hypotheses must not be promoted to a uniform theorem.

## A precise global uniform target

Given the family of p-admissible primes c and derived classes `tau_(c,p)`, one would need to prove, for every sufficiently large good p, a suitable *rank-two primitive derived system* whose localization or duality pairing constrains the 2-dimensional MW Selmer quotient without introducing unbounded p-torsion. Stein's Table 8.2 only treats finitely many selected p and c. Neither the algorithm nor its data prove all-large-p primitivity.

A conceivable proof route is a comparison between a fixed integral rank-two determinant line over Q and the leading term of a higher derivative Euler/Kolyvagin system with control of integral denominators independent of p. **Such a comparison is not constructed in this project.** It may be as difficult as the desired finite support of Sha, and must not assume it.

## Separate strong evidence on p107

For p107, the genuine Ubuntu Sage 10.9 `p_primary_bound(107)=0` is independent of the old frozen Kurihara native computation. The p3 Heegner literature route does not replace or verify that independent p107 upper-bound method.
