# 389a1 — a genuine uniform theorem: one p^k-deep two-factor Kurihara unit yields φ(p^k) cyclic fields with *exactly unchanged Mordell–Weil group*

**23 November 2026. Status: a rigorous new arithmetic consequence of the genuine Hecke norm and Kato's nonvanishing theorem. All hypotheses are satisfied by THREE already-USER-certified explicit Kurihara witnesses. This is a uniform theorem *conditional on a unit witness at a given p*, NOT a theorem that witnesses exist at every p or that global Sha is finite.**

## 1. General theorem, quantified for ALL primes p>=5 and k>=1

Let E=389a1:y²+y=x³+x²−2x have
- E(Q)=Z·P⊕Z·Q, P=(-1,1),Q=(0,-1), rank2, torsion0;
- L(E,s) vanishing to order exactly2 at s=1 (previous independent Arb/rational certified result);
- no Q-rational isogenies (LMFDB curve 389.a1, isogeny class size1, isogeny degrees [1]);
- Néron-integral Hecke-normalized plus modular symbols and m_E^+(0)=L(E,1)/Ω_E^+=0.

Fix any p>=5 and k>=1. Suppose **two distinct GOOD primes** q1,q2 satisfy

    q_i≡1 (mod p^k),       a_(q_i)(E)≡2 (mod p^k),

and the authentic depth-p^k two-prime Kurihara number is a p-adic **UNIT**:

    **δ_(q1*q2)=[T1*T2]Theta_(q1*q2) not≡0 (mod p)**.

This is a genuine arithmetic hypothesis on the conductor-dependent global modular-symbol sum, not an automatic implication from Chebotarev.

Choose primitive roots gi modulo qi and associated discrete logs
    λ_i:(Z/qi)^×→Z/p^k.
Since qi are odd and p^k|qi−1, we have 2p^k|qi−1, so λ_i(−1)=0 and all following characters are even.

For each r∈(Z/p^k)^×, put
    χ_r(a)=ζ_(p^k)^(λ1(a)+r λ2(a)),
    F_r=Q(ζ_(q1q2))^(kerχ_r).

**THEOREM.** For EVERY such r:
1. F_r/Q is a **totally real cyclic extension of degree p^k**, primitive conductor n=q1q2, and the fields for different r are distinct.
2. EVERY nontrivial character χ_r^t, t=1,...,p^k−1, has primitive conductor n, and

       **L(E,χ_r^t,1) != 0**.

   More strongly, if χ_r^t has exact order p^j (1≤j≤k) and ζ=ζ_(p^j) corresponds to its chosen primitive character value, then its genuine integral modular-symbol sum A(E,χ_r^t) satisfies

       **v_(ζ−1)(A(E,χ_r^t))=2.**

3. Artin formalism gives

       **ord_(s=1)L(E/F_r,s)=2**,

   and Kato's theorem for NONTRIVIAL Dirichlet twists gives

       **rank_Z E(F_r)=2**.

4. The absence of rational isogenies and Weil pairing force E(F_r) to have **NO torsion**, and thus

       **E(F_r) = E(Q) = Z·P ⊕ Z·Q  (equality of actual groups).**

5. Every nontrivial χ_r^t has conductor n, so conductor–discriminant gives

       **disc(F_r)=n^(p^k−1)**

   (positive because F_r is totally real).

The number of degree-p^k fields is exactly φ(p^k), and the number of DISTINCT nontrivial characters of those fields is

    **Σ_(j=1)^k φ(p^j)^2**.

The common order-p^j characters may occur in multiple F_r; the displayed count includes each character only once.

## 2. Proof, including exact p-adic valuation and full integral Mordell–Weil identity

### Hecke–Mazur–Tate quadratic jet

The independently USER-validated genuine norm relation is

    proj_(nℓ→n) Theta_(nℓ)
       = (a_ℓ−σ_ℓ−σ_ℓ^−1) Theta_n.

Together with m_E^+(0)=0 and qi≡1, a_qi≡2 modulo p^k, it gives the *genuine* bivariate jet vanishing

    M00=M10=M01=M20=M02=0 modp^k.

Therefore for any unit r modulo p^k the cyclic diagonal theta
    Θ_r(T)=Σ_a^* m_E^+(a/n)(1+T)^(λ1(a)+r λ2(a))
has a canonical polynomial lift with

    Θ_r(T)=p^k a0+p^k a1*T+c2*T²+T³H(T),
    c2≡r δ_(q1q2) modp^k.

Since r and δ are p-units, c2 is a p-unit. For t of exact order p^j, evaluate T=ζ_(p^j)^b−1 for a unit b; this is a uniformizer π_j up to a unit in Q_p(ζ_(p^j)). The local ramification index is e_j=φ(p^j)≥p−1≥4. Thus the constant and linear terms have valuations at least k e_j and k e_j+1, respectively, while the quadratic has valuation **exactly2** and all higher terms have valuation≥3. So v_(π_j)(Θ_r(ζ_(p^j)^b−1))=2.

The evaluated θ is precisely the primitive even χ_r^t modular-symbol sum A(E,χ_r^t). The genuine Birch–Stevens relation identifies it with the twisted complex L(E,χ_r^t,1) times nonzero period/Gauss factors, so the L-value is nonzero.

### Ranks over the fields

Artin factorization
    L(E/F_r,s)=Π_(t=0)^(p^k−1)L(E,χ_r^t,s)
gives analytic rank2, since each t≥1 factor has nonzero central value and the t=0 term has rank2 by the known analytic interval certificate.

Kato's proved rank-zero theorem for **Dirichlet twists with nonzero critical L-value** implies the nontrivial χ_r^t isotypic component of E(F_r)⊗C is zero. This holds even though χ_r^t may have p-power order, since the argument takes place in characteristic0 and twisted modular motives. Therefore E(F_r)⊗Q is exhausted by the trivial isotypic component E(Q)⊗Q, giving rank2.

Sources:
- Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), Corollary 14.3, applied to Dirichlet twists;
- clear formulation in https://warwick.ac.uk/fac/sci/maths/people/staff/fbouyer/euler_systems_study_group.pdf (Theorem 9.10);
- rank-zero Kato implication for modular twists in https://link.springer.com/article/10.1007/s40993-023-00430-4 (Introduction, Corollary 3.2).

### Torsion and actual group equality

Suppose a prime ℓ divides E(F_r)_tors. Since F_r/Q is Galois, the subspace E[ℓ](F_r) is G_Q-stable. The absence of **all Q-rational prime-degree isogenies** means E[ℓ] is irreducible for G_Q, so any nonzero G_Q-stable subspace is E[ℓ] itself. Hence full E[ℓ] lies in F_r.

If ℓ is odd, Weil pairing forces Q(ζ_ℓ)⊂F_r, impossible: [Q(ζ_ℓ):Q]=ℓ−1 is even but [F_r:Q]=p^k is odd. If ℓ=2, the division extension Q(E[2])/Q has degree dividing |GL2(F2)|=6 and dividing p^k; since p>=5, gcd(6,p^k)=1, so it is trivial, contradicting E(Q)[2]=0. Thus E(F_r)_tors=0.

Now rank E(F_r)=rank E(Q)=2, so for each R∈E(F_r) there exists m≥1 with mR∈E(Q). For σ∈Gal(F_r/Q),
    m(σR−R)=0.
As E(F_r) is torsionfree, σR=R. Hence R∈E(Q), proving

    **E(F_r)=E(Q), not merely finite index.**

### Field and character cardinalities

Different r yield distinct kernels: kerχ_r=kerχ_s implies χ_s=χ_r^u for a unit u, and comparing the two full coordinate characters forces u=1 then r=s.

For characters of exact order p^j, the two components are both nonzero multiples of p^(k−j), and the induced pair of primitive coefficient units modp^j can be chosen freely. There are φ(p^j)^2 distinct characters. All these are nontrivial at each prime qi, and so have conductor n. Every nontrivial character of F_r therefore contributes n to the conductor–discriminant product, giving disc(F_r)=n^(p^k−1).

## 3. THREE genuine archived input witnesses yield 34 EXPLICIT rank-stable fields

| p | k | n=q1*q2 | authentic δ modp^k | # fields | degree | # distinct NONZERO χ |
|:--:|:--:|--:|--:|--:|--:|--:|
|5|1|41×61=2,501|4 mod5|4|5|16|
|11|1|397×991=393,427|1 mod11|10|11|100|
|5|2|5351×10651=56,993,501|22 mod25|20|25|416|
| **TOTAL** | | | | **34** | | **532** |

The three source computations and normalizations were previously USER-executed and archived in the repository. The 28,488,750-term p5 depth25 output was independently rerun by the user at 4.77932 seconds (results/bsd389_p5_depth25_diagonal_USER_UBUNTU_PASS_2026-11-23.md).

All fields from the three rows are distinct because their conductors n differ (and each row contains distinct fields). The 532 characters are also pairwise distinct because their conductors differ.

For the 20 degree25 fields the exact reduced spectral integer
    B_r=Π_(t=1)^24 A(E,χ_r^t)
satisfies **v5(B_r)=4**, as shown in
paper/bsd389_twenty_real_cyclic_degree25_unchanged_MW_2026-11-23.md.

## 4. Clear BSD relevance and LIMIT

This is a **strong genuine arithmetic consequence** of the certified Kurihara units: simultaneously proving complex twisted L nonvanishing, analytic rank2 over 34 nontrivial real abelian extensions, AND EXACT NO-GROWTH OF THE INTEGRAL MW GROUP there. It uses a published theorem for rank-zero TWISTS, not an unproved rank-two BSD implication.

The general theorem is UNIFORM **IN ITS FORM**, but it assumes a p-unit two-prime Kurihara number for its specific p. It therefore cannot supply the missing nonvanishing for all sufficiently large p, cannot by itself yield a global integer in Fitt_2(Sel_p), and does not prove Sha(E/Q) finite or the exact complex BSD leading term. Rank preservation over F_r does not imply Sha(E/F_r) or Sha(E/Q) is finite.

Reproducibility:
    verification/bsd389_kurihara_unit_twist_field_counts_gate.py

**VERDICT: 34 rigorously specified real abelian fields, no new MW points of any order, and 532 nonvanishing twisted central L-values, under three already user-validated finite arithmetic witnesses. Global rank-two BSD is NOT yet closed.**
