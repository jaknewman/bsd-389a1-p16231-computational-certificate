# Global exact BSD ratio via denominator rigidity, not a p-adic spot-check

Date: 2026-11-06. Pure elementary exact theorem and its correct research scope. This is NOT a proof that the needed denominator bound is available.

For E=389a1, with the TOTAL Neron real period Ω_E and the full saturated Neron–Tate regulator Reg_E, define the positive real number
Q_E = [L''(E,1)/2]/[Ω_E Reg_E].
The previously certified analytic coefficient and periods imply numerically Q_E≈1. Its positivity follows from the certified interval. No rationality of Q_E is yet proved.

**Theorem (global denominator rigidity).** Suppose an independent global arithmetic theorem gives integers a,b with b>0 and b<=B, and Q_E=a/b. Suppose further that independent CERTIFIED intervals for L''(E,1)/2, Ω_E, Reg_E give
|Q_E-1|<1/B.
Then Q_E=1 EXACTLY.

Proof: If a/b≠1, then |a/b-1|=|a-b|/b>=1/b>=1/B. This contradicts the strict interval. QED.

**Strong, conveniently checkable version.** If one proves D Q_E is an integer for some explicit nonzero D>0, then b divides D (in lowest terms) so b<=D. Thus a rigorous interval |Q_E-1|<1/D proves Q_E=1. This is weaker than proving Q_E is an INTEGER outright, and its proof need only bound denominators.

**Uniform global significance.** The exact Mellin–Fricke q-series formula and its geometric tail in the companion paper make the L'' side rigorously approximable to arbitrarily small tolerance. Certified real period and Neron height algorithms can likewise enclose the two other positive factors. Thus **once** an independent B or D is constructed from exact arithmetic, increasing numerical precision is a routine FINITE procedure, and the exact complex BSD identity with Sha=1 follows.

**Critical missing theorem:** For this rank-two non-CM curve, no independent exact rationality theorem or a fixed denominator bound for Q_E has been established in our dossier. The same curve and the challenge to prove even rationality of Q_E are William Stein's explicit E389a Open Problem 2.18: https://wstein.org/books/bsd/bsd.pdf. Claiming D by letting it be the unknown denominator of Q_E is CIRCULAR. The denominator bound must be derived from a separately proved global regulator/height/motivic relation, not from BSD or apparent decimal coincidence.

**Further BSD obligation:** Even proving Q_E=1 EXACTLY does not prove Sha(E/Q)=0 as an abstract group; the global uniform Sha finiteness and vanishing problem remains logically independent unless an additional valid arithmetic leading-term theorem bridges them. See global Mellin/all-prime paper in this PR.

This lemma replaces the stricter requirement Q_E∈Z previously mentioned in the project with the weaker, more flexible target: Q_E∈(1/D)Z for an independent explicit fixed D. It does not itself construct such D.
