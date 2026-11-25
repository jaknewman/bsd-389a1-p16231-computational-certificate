# BSD 389a1 — Full Selmer detection by unipotent Chebotarev (8 November 2026)

**Result:** A rigorously proved all-`p>=5` separation theorem, extending our old MW-only 2-prime Kummer result to the **entire** finite p-Selmer group. It does **not** prove the desired `Sha[p]=0`, any rank-two Kurihara unit, or the exact complex BSD identity.

Let `E: y²+y=x³+x²−2x` with full saturated MW group `E(Q)=ZP⊕ZQ`, and fix `p>=5`. The image of `rho_{E,p}` is `GL2(Fp)` (Mazur for p>=11; previously archived p5/p7). Let `S=Sel_p(E/Q)`, `d=dim_Fp(S)`.

## Theorem

There exist **d distinct** good primes `q1,...,qd !=p,389` with nonidentity-unipotent mod-p Frobenius such that

    loc_(q1,...,qd): S --> ⊕ H^1_f(Q_qi,E[p]) ≅ Fp^d

is an isomorphism. Each q satisfies `q≡1 (mod p)` and `a_q(E)≡2≡q+1 (mod p)`. For any chosen basis of S and each basis index i, there is a **positive-density** family of q with its i-th basis localization nonzero and all other basis localizations zero, of exact Dirichlet density `1/p^(d+1)`.

No smaller number of primes with 1-dimensional local finite conditions can yield injectivity. Thus if `m_p` is the minimum number of such primes needed to detect **all** of S, then

    m_p = d = 2 + dim_Fp Sha(E/Q)[p].

In particular, for every p>=5 (including the bad reduction prime p=389, because all auxiliaries q are good):

    m_p=2  iff  Sha(E/Q)[p]=0  iff  Sha(E/Q)[p^infty]=0.

This is an **exact equivalence**, not proof that `m_p=2`.

## Proof

Set `V=E[p]`, `L=Q(V)`, and choose an Fp basis `s1,...,sd` of S. Since `-I` is central in GL2(Fp) and `-I-I=-2I` is invertible for odd p, Sah's lemma implies `H¹(GL2(Fp),V)=0`. Inflation–restriction makes the restrictions of s_i to `G_L` linearly independent in `Hom(G_L,V)`.

Let `W⊂V^d` be the image of the combined d restrictions. It is GL2(Fp)-stable. The natural module V is absolutely irreducible and `End_GL2(V)=Fp`; since V^d is semisimple, any proper W would be annihilated by a nonzero GL2-equivariant map `V^d→V`. Such a map is an Fp-linear combination of coordinate projections, giving a forbidden relation between the s_i. Hence `W=V^d`, and the resulting Galois extension M/L has group `V^d`.

Fix a nonidentity unipotent `g∈GL2(Fp)`. Its quotient `V/(g-1)V` has dimension one. Lifts of g to `Gal(M/Q)` can be varied independently along all d translation coordinates, prescribing in the quotient the vectors `(nonzero,0,...,0)`, `(0,nonzero,...,0)`, etc. Chebotarev supplies infinitely many Frobenius primes q for each conjugacy-invariant pattern. Since the classes are locally unramified at good q, the finite local Selmer condition identifies with `V/(g-1)V`. Picking one q per pattern yields a diagonal invertible localization matrix.

There are `p²−1` nonidentity unipotent matrices g; at each such g the desired one-nonzero pattern has `p^d(p−1)` translation lifts. The total group order is `|GL2(Fp)|p^{2d}=(p²−1)p(p−1)p^{2d}`. Therefore the density is **exactly `1/p^{d+1}`**.

Each local space is 1-dimensional, hence k<d primes cannot detect a d-dimensional Selmer group. The Kummer exact sequence and rank E(Q)=2 give the formula for m_p. QED.

## Relation to the Kurihara obstruction

For p>=5, p!=389, under the source hypotheses, Kim's rank formula and Castella–Sano refined nonvanishing give `rho_p = corank_Zp Sel_{p∞}(E) = 2 + corank_Zp Sha[p∞]`, where rho_p is the minimum number of factors in a nonzero Kurihara number. Therefore

    m_p - rho_p = dim_Fp( (Sha[p∞]/Sha[p∞]_div)[p] ).

This detects the **finite** Sha obstruction that the minimal Kurihara order alone does not record. Kim's higher p-adic valuation invariants encode its order.

The previous local MW separation pair proves only that the known 2-dimensional MW subspace maps onto Fp². Its strict Selmer kernel is exactly Sha[p], and cannot be declared zero. Kim's core vertices/rigidity theorems (Theorems 3.7–3.9) depend on the full strict Selmer condition, not merely the local MW determinant. The present theorem constructs a core-vertex candidate using d auxiliary primes, but cannot lower d to 2 without the missing global Selmer bound.

## Computation

An independent exhaustive GL2(Fp) count confirmed the density `1/p^(d+1)` for p in {3,5,7,11,17}, d in {2,3,4}; 15/15 PASS. The p=3 counts are group-theory regressions; E-specific statement starts p>=5. No actual Selmer dimension was inferred from these tests.

## STOP

The missing implication `local MW determinant unit => Kurihara two-prime unit` is **not proved**. In fact, proving it uniformly would be equivalent to `Sha[p∞]=0`. Nothing here implies finite support of Sha across p or equality of `L''(E,1)/2` with `Omega_E Reg(E)`.

Sources: Kim arXiv:2505.09121 (Theorems 1.1, 3.7–3.9), Castella–Sano arXiv:2601.14504 (Theorem B); Mazur semistable surjectivity; Sah lemma, Kummer, Chebotarev.
