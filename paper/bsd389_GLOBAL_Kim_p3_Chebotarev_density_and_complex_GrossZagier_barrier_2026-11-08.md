# BSD 389a1 — three exact steps toward uniform all-prime Sha and the complex rank-two leading coefficient (2026-11-08)

**Status:** p=3 Kim–Pollack published explicit witness; exact Chebotarev density for admissible auxiliary primes at each residual-surjective p; exact first-derivative Gross–Zagier obstruction for quadratic base changes. **NOT** all-prime Sha vanishing; **NOT** exact rank-two BSD.

## A. A published 389a1-specific p=3 Selmer result

Chan-Ho Kim, with appendix by Robert Pollack, *The refined Tamagawa number conjectures for GL2* (arXiv:2505.09121, version 1, Theorem 1.1 and Appendix A.1.5, printed p.35): for E=389.a1, p=3, the normalized Kurihara number δ̃_(79·109) is nonzero mod 3 and

    Sel_(3∞)(E/Q) ≅ (Q_3/Z_3)^2.

Together with the independently established full Mordell–Weil rank 2, Kummer gives

    Sha(E/Q)[3∞] = 0.

This is an implication from the paper's *published reported computation*, NOT a new independent calculation of its 8,611-conductor Kurihara number. It remains appropriate to replay the modular-symbol witness before labeling it 'independently reproduced'.

The elementary admissibility conditions HAVE been independently verified in exact integer arithmetic:
- a_3 = -2, hence good ordinary;
- a_79 = -13, and 79 ≡ 1 mod 3, -13 ≡ 79+1 ≡ 2 mod 3;
- a_109 = 2, and 109 ≡ 1 mod 3, 2 ≡ 109+1 ≡ 2 mod 3.

See verification/bsd389_global_kim_p3_chebotarev_density_2026_11_08.py.

## B. Exact Chebotarev density of eligible auxiliary primes

Fix any odd prime p for which rho_(E,p):G_Q -> GL2(F_p) is surjective. For q∤389p, Frobenius satisfies

   det rho(Frob_q) = q (mod p),   tr rho(Frob_q) = a_q(E) (mod p).

The Kurihara auxiliary conditions q≡1 and a_q≡q+1 modulo p are thus equivalent to det=1 and tr=2. Such matrices are precisely the **unipotent** matrices in GL2(F_p), consisting of identity and the single nontrivial unipotent conjugacy class.

The centralizer of a nontrivial Jordan unipotent is of size p(p−1); since |GL2(F_p)| = (p²−1)(p²−p), the nontrivial class has size p²−1. Including identity gives p² eligible Frobenius matrices. Since this union is conjugacy-stable, Chebotarev gives the **exact Dirichlet density**

    density_p = p² / ((p²−1)(p²−p))
              = p/((p−1)²(p+1)) > 0.

Therefore for EACH p having surjective residual image there are infinitely many Kolyvagin-eligible primes and infinitely many distinct pairs (q1,q2). In particular this applies to all sufficiently large p by the known non-CM large-image theorem, and to all p≥5 using the independently archived residual surjectivity for p=5,7 and semistable surjectivity for p≥11.

This is an exact, simultaneously formulated infinite family theorem about **admissibility**. It is not a Kurihara nonvanishing theorem. Chebotarev does not control the modular-symbol weights defining δ̃_(q1q2).

Examples:
  p=3: 3/16 (if full mod-3 image; the Kim paper establishes the requisite large-image condition);
  p=5: 5/96;
  p=107: 107/1213488;
  p=16231: 16231/4275718192800.

No *fixed* finite set of rational auxiliary primes can serve all p, because each q admits p only when p | (q−1).

## C. A rigorous barrier to the classical Gross–Zagier route

Let K/Q be any imaginary quadratic field, with twist E^D. By Artin formalism,

    L(E/K,s) = L(E,s)L(E^D,s).

The archived exact analytic-rank-two proof gives L(E,1)=L'(E,1)=0. Differentiating,

    L'(E/K,1) = 0

for EVERY quadratic K, independently of the rank of E^D. Hence whenever the classical Gross–Zagier formula for a *trivial ring-class character* Heegner point applies, that point has canonical height zero and is torsion. In particular the classical first-derivative Gross–Zagier pairing cannot reconstruct the independent rank-two regulator of E via such points. The split-prime Heegner hypothesis is needed for the classical point construction; K=Q(sqrt(-3)) is inert at 389 so it should not be cited as a classical X_0(389) Heegner-point instance.

The **second** derivative does satisfy the exact factorization

    L''(E/K,1)/2 = L(E^D,1) * L''(E,1)/2,

which is a useful analytic transfer, not a height formula. The genuinely missing archimedean theorem is a second-derivative / two-height determinant identity, or independently proved rationality plus a denominator bound for the BSD quotient.

## D. Remaining, precisely unproved implications

1. **Uniform nonvanishing:** for all p>P0, find eligible q1(p),q2(p) with normalized δ̃_(q1q2) a p-adic unit. Kim's Theorem 1.1 would then imply Sha(E)[p∞]=0. Theorem B above supplies eligible q's but does NOT supply the required unit.
2. **Complex identity:** prove L''(E,1)/2 = Ω_E Reg(E), using the already proved degree-40 modular height normalization and exact Mellin–Fricke integral. Neither the explicit density nor Kim's Selmer theorem implies it.

The reported positive numerical match Q≈1 is evidence only. No rationality or integral denominator theorem for Q is assumed.

## Sources

- Kim–Pollack, arXiv:2505.09121v1, Theorem 1.1, Appendix A.1.5 (p.35): https://arxiv.org/pdf/2505.09121
- Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum Math Sigma 10 (2022): https://doi.org/10.1017/fms.2021.85
- Original X_0(389) modular-degree40/Arakelov and Mellin–Fricke identities in PR #12, papers dated 2026-11-06.
