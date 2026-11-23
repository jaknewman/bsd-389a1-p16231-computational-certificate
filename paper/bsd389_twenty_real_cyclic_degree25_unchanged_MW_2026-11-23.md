# E389a1 — twenty explicit totally real cyclic degree-25 fields with **exactly the original Mordell–Weil group**

**Date: 23 November 2026. Status: rigorous new conclusion by combining the USER-executed exhaustive 28,488,750-symbol p=5 depth-25 certificate, the genuine Hecke–Mazur–Tate norm, Birch–Stevens interpolation, Kato's rank-zero theorem for Dirichlet twists, and the independently recorded absence of rational isogenies for 389a1. No global finiteness of Sha(E/Q), no rank-two exact complex BSD is claimed.**

## 1. Arithmetic input and definitions of the twenty actual fields

Let
    E/Q : y² + y = x³ + x² − 2x   (389a1)
with E(Q)=Z·P⊕Z·Q, P=(-1,1), Q=(0,-1), torsion0 and rank2. The curve is optimal, semistable, has analytic rank2, and **has no rational isogenies**, including no rational isogeny of prime degree. Data:
https://www.lmfdb.org/EllipticCurve/Q/389a1/
https://www.lmfdb.org/EllipticCurve/Q/data/389.a1
(the latter reports isogeny class size 1, isogeny degrees [1], and rank2).

Fix the USER-REPRODUCED exact p5 depth25 auxiliary primes
    q1=5351, q2=10651, n=q1*q2=56,993,501.
The primitive roots from the native Manin program are g1=11, g2=7, and the canonical discrete logarithms
    lambda_i : (Z/q_i)^× → Z/25,
    lambda_i(g_i)=1.
Both q_i−1 are divisible by 50, so lambda_i(−1)=0 modulo25.

Let U=(Z/25)^×, |U|=20. For every r∈U define a Dirichlet character
    chi_r(a)=zeta25^(lambda_1(a) + r*lambda_2(a))
of exact order25. Define the **actual number field**
    F_r = Q(zeta_n)^(ker chi_r),
a totally real cyclic extension of Q of degree25.

The F_r are **20 DISTINCT** fields: if ker chi_r = ker chi_s, then chi_s=chi_r^u for a unit u mod25. Comparing lambda_1 coefficients gives u=1 and then r=s. Every nontrivial chi_r^t (t=1,...,24) is nontrivial at BOTH q1 and q2 (even t=5,10,15,20), so has exact primitive conductor n. The conductor–discriminant theorem therefore gives

    **disc(F_r)=n^24=(56,993,501)^24 >0.**

Distinct F_r have distinct Galois-kernel subgroups, although their unique cyclic order-5 subfields coincide for r with the same residue modulo 5 (hence there are only four such subfields).

## 2. All 24 nontrivial characters of EACH field have L(E,chi,1) != 0

The user's complete native C++ program enumerated ALL
    φ(n)/2=28,488,750
Néron-normalized Manin plus-symbol representatives and obtained the full bivariate degree<=2 moment matrix modulo25:

     [ [0,0,0],
       [0,22,16],
       [0,17,14] ].

This source data is archived in:
    results/bsd389_p5_depth25_diagonal_USER_UBUNTU_PASS_2026-11-23.md.

The genuine Hecke norm implies the constant, both linear and both pure quadratic terms are ZERO modulo25 (no Sha-finiteness assumption). For any r∈U let

    Theta_r(T)=sum_{a mod n}^* m_E^+(a/n)
      (1+T)^(lambda_1(a)+r lambda_2(a) mod25)
       ∈Z[T]/((1+T)^25−1),

using integral Néron plus modular symbols. Its canonical 25-term polynomial representative satisfies

    Theta_r(T)=25*a0+25*a1*T+c2*T²+T³H(T),
    **c2≡22r mod25**,  c2∈Z_5^×, H∈Z[T].

The coefficient formula is **exact** from the true bivariate Hecke projection, not a conjectured interpolation.

Take zeta=zeta25 and pi=zeta25−1, v_pi(5)=20.

- If 5∤t, then zeta^t−1 is a uniformizer (v_pi=1). The quadratic term is uniquely of smallest valuation, hence
      **v_pi(Theta_r(zeta^t−1))=2**.

- If t∈{5,10,15,20}, then zeta^t is a primitive fifth root and v_pi(zeta^t−1)=5. The constant/linear coefficients are divisible by25, so their valuations are at least40 and45; c2*(zeta^t−1)^2 has valuation exactly10; all higher terms have valuation≥15. Thus
      **v_pi(Theta_r(zeta^t−1))=10**
  or equivalently v_(zeta5−1)=2 in Q5(zeta5).

These 24 evaluations are exactly the primitive-even Dirichlet-character Manin sums
      A(E,chi_r^t)=sum_{a mod n}^*m_E^+(a/n)chi_r^t(a).

By the genuine Birch–Stevens formula, since the Gauss factor and periods are nonzero,

    **L(E,chi_r^t,1)!=0  for ALL r∈U and 1≤t≤24.**

There are **416 distinct primitive-even nontrivial characters** across the 20 fields:
- 400 characters of exact order25 (20 full Galois orbits);
- 16 characters of exact order5 (4 full Galois orbits).
The four order-5 characters in each F_r overlap between the five fields with the same r mod5. The total unique count is 400+16=416, not 480.

The result includes the earlier 400-character theorem as a strict subset and proves the missing order-5 layer.

## 3. NEW RANK THEOREM by Kato — each real F_r has rank EXACTLY 2

Artin formalism gives

    L(E/F_r,s)=∏_(t=0)^24 L(E,chi_r^t,s).

For every t>=1, the t-twisted central factor is NONZERO by §2. The trivial factor L(E,s) has analytic rank exactly2 by the project's earlier rational/Arb analytic certificate. Consequently

    **ord_(s=1) L(E/F_r,s)=2**, for all 20 fields.

To establish the *algebraic* statement without assuming BSD, invoke Kato's nonvanishing theorem for the Dirichlet-twisted modular elliptic representation: if L(E,chi,1)!=0, then the chi-isotypic Mordell–Weil component of E(F)⊗C is zero for any finite abelian extension F/Q containing the field of chi. This is stated explicitly as Theorem 9.10 in
https://warwick.ac.uk/fac/sci/maths/people/staff/fbouyer/euler_systems_study_group.pdf
and follows from Kato's Euler system (Kato, Astérisque 295 (2004), Corollary 14.3, for weight-two modular twists). See also:
https://link.springer.com/article/10.1007/s40993-023-00430-4 (Corollary 3.2, Lemma 3.1 and the rank-zero Kato theorem cited in its introduction).

As every nontrivial chi_r^t has nonzero central value, the full rational Mordell–Weil representation has ONLY its trivial isotypic component. Therefore

    **rank_Z E(F_r)=rank_Z E(Q)=2**.

This is a genuine use of a proved rank-zero theorem for NONTRIVIAL twists; it does not invoke a conjectural higher-rank rank-equality implication for the trivial character.

## 4. Even stronger: there are NO new torsion points, hence E(F_r)=E(Q) AS GROUPS

**Lemma (normal Galois torsion).** Let F/Q be Galois and suppose E/Q admits NO rational prime-degree isogeny. If E(F)[ell] !=0 for a prime ell, then E[ell]⊂E(F).

**Proof.** W=E[ell]^{G_F}=E(F)[ell] is an F_ell-linear subspace of E[ell]. Since G_F◁G_Q, W is G_Q-stable. No rational ell-isogeny means the two-dimensional mod-ell G_Q-representation is irreducible: its only invariant subspaces are 0 and E[ell]. As W!=0, W=E[ell]. QED.

For an odd prime ell, E[ell]⊂F_r would imply mu_ell⊂F_r by the Weil pairing, so ell−1 divides [F_r:Q]=25. The only prime ell with ell−1|25 is ell=2. Therefore E(F_r)[ell]=0 for EVERY odd prime ell.

At ell=2, full E[2] over F_r would give Q(E[2])⊂F_r. The extension Q(E[2])/Q has degree dividing |GL2(F2)|=6, but also dividing 25; hence it has degree1. This would imply E(Q)[2] !=0, contradicting known torsion0. Thus also E(F_r)[2]=0.

Therefore **E(F_r)_tors=0** for each r.

Since E(F_r) and E(Q) have the SAME rank2, E(F_r)/E(Q) is a finite abelian group. Because the rational span E(F_r)⊗Q equals E(Q)⊗Q (from §3), G=Gal(F_r/Q) acts trivially after tensoring Q. For any R∈E(F_r), each σR−R is thus a torsion point. But E(F_r) has no torsion, so σR=R for all σ∈G. Therefore R∈E(F_r)^G=E(Q).

We conclude the unexpectedly strong, fully integral identity

    **E(F_r) = E(Q) = Z·(-1,1) ⊕ Z·(0,-1)**

for ALL TWENTY explicit totally real cyclic degree-25 fields F_r.

This statement does **not** say Sha(E/F_r) is trivial or finite: there can be new Selmer torsion even when the MW group is unchanged.

## 5. A concrete integral reduced-character norm with a fixed 5-adic valuation

For each r define the Galois-invariant algebraic integer

    B_r = ∏_(t=1)^24 A(E,chi_r^t) ∈ Z.

All factors are algebraic integers because the frozen Néron-normalized plus symbols are integers. In Q5(zeta25), the exact local valuations of the 20 primitive-order25 terms are 2 each, and of the four order5 terms are 10 each. Their product has pi-valuation

    20*2+4*10=80,

and v_pi(5)=20, so

    **v_5(B_r)=80/20=4**.

Thus every B_r is a NONZERO honest integer with exact order
    **5^4 || B_r**.

This spectral integer is computed independently of the unknown Sha, but it is tied to the FIXED auxiliary conductor and p=5. It does NOT give a global all-prime Fitt2 annihilator or the exact BSD leading coefficient. Do not confuse the spectral integer B_r with a Selmer determinant.

## 6. Independently executed arithmetic gate

A standard-library Python verifier checks 20 ratio classes, all 400 distinct order25 and 16 distinct order5 characters, exact quadratic-unit residues, 20/4 character-orbit cardinalities, and the exact local norm valuation 4. It does not recompute the original 28,488,750 Manin terms nor prove Kato's theorem.

File: verification/bsd389_p5_20_cyclic25_Kato_rank_stability_gate.py

Sources: the user's exact genuine depth25 stdout, Birch–Stevens, Kato rank-zero for twists, Artin formalism, Weil pairing, the LMFDB-certified absence of rational isogenies.

**Scope:** 20 NEW explicit degree25 number fields with exact analytically and algebraically rank2 and unchanged complete Mordell–Weil groups, plus exact nonzero 5-adic spectral integer of valuation4. This does **not** prove finiteness of Sha(E/Q), a p-independent integer annihilator, or strong BSD.
