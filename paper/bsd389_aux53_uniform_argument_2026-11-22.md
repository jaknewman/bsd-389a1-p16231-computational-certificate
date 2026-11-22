# 389a1 — Auxiliary conductor 53: what is and is not uniform

22 November 2026. Independent argument, with a reproducible finite arithmetic check in `bsd389_aux53_uniform_regularity_gate.py`.

**Goal.** Fix the quadratic field K=Q(sqrt(-3)) and the auxiliary 53-anticyclotomic tower, but allow the character to vary with the target prime p. This note does not reuse any target-specific certificate.

## The obstruction to one fixed conductor

Write H_r for the ring-class field of K of conductor 53^r (r >= 1). Since K has class number 1, 53 is inert and [O_K^×:O_{53^r}^×]=3, its class number is

    h_r = 53^r * (1+1/53) / 3 = 18 * 53^(r-1).

H_r/Q is Galois of degree 2*h_r. Chebotarev shows that rational primes splitting completely in H_r have density

    1/(36 * 53^(r-1)).

At every such p, every ring-class character of conductor dividing 53^r is trivial on Frobenius. Thus no fixed conductor and no finite set of auxiliary characters of bounded conductor can make the p-stabilization roots distinct at all sufficiently large p split in K. The elliptic curve 389a1 is non-CM (its j-invariant is nonintegral), so this obstruction also occurs for infinitely many good ordinary p (supersingular primes have density zero).

## Correct 53-adic depth, explicitly computable from a representation of p

Let p be a rational prime with p ≡ 1 (mod 3), p ≠ 53, and write

    p = A^2 - A*B + B^2,
    pi = A+B*w,    w^2+w+1=0,
    pi_bar = (A-B)-B*w.

In the unramified quadratic extension K_53/Q_53, put

    u_p = pi/pi_bar = pi^2/p,
    m_p = v_53(u_p^54 - 1).

The valuation of a pair c+d*w is min(v_53(c),v_53(d)). Since u_p has norm 1 and the residue norm-one subgroup has order 54, u_p^54 is a principal norm-one unit and m_p >= 1. This valuation is finite: if u_p^54=1, then pi/pi_bar would be a root of unity in K, impossible because its fractional principal ideal has different valuations at the two primes above p.

The pro-53 norm-one group is a rank-one Z_53-module. On its principal-unit subgroup the logarithm is an isomorphism onto the rank-one trace-zero additive lattice. The value m_p is exactly the 53-adic valuation of the pro-53 Frobenius coordinate **plus one**. Thus for a finite order character chi on Gamma_53^-=Gal(K_infinity^-/K) of exact order 53^n,

    chi(Frob_pi) != 1    <=>    n >= m_p.

Such a character first occurs at ring-class conductor 53^(n+1) (the 53-primary part of Pic(O_{53^r}) has order 53^(r-1)). Therefore the first conductor depth at which a 53-power auxiliary character is regular at p is r=m_p+1.

The integer m_p is computed by modular arithmetic without real or p-adic floating-point approximations: compute u_p^54 in (Z[w]/(w²+w+1,53^k)) until it ceases to equal 1, then m_p=k-1.

## A finite exact counterexample to a tempting but incorrect depth formula

Take p=1297 and pi=39+7*w. It has prime norm:

    39^2 - 39*7 + 7^2 = 1297.

The elliptic curve E: y²+y=x³+x²-2x has a_1297(E)=-38, so 1297 is a good ordinary split prime.

Exact arithmetic shows

    u_1297^54 = 1                    (mod 53²),
    u_1297^54 = 50563+101124*w     (mod 53³),
    u_1297^54 = 1+53²*(18+36*w)   (mod 53³).

In particular m_1297=2, and all order-53 auxiliary characters vanish on this Frobenius; a character of order 53² detects it. Nevertheless

    39*7*(39-7) = 8736 ≡ 44 (mod 53).

Thus v_53(A*B*(A-B))=0 and cannot be used as m_p, nor as a certificate of first-layer regularity for arbitrary split p. This is a local exact counterexample, not an assertion about theta-order or Sha.

## Uniform auxiliary *existence*, with the character allowed to depend on p

Assume the curve-specific nonvanishing L(E^K,1) != 0, which was independently rigorously interval-certified in the existing project, and let p>163 be a good ordinary prime splitting in K, p ≠389,53.

For the weight-two newform f associated to E, the *tower prime* in Chida--Hsieh's Theorem D is fixed at 53 and the *residual prime* ell is p. The conditions hold:

- 53² does not divide N=389, and gcd(D_K,N^-)=gcd(-3,389)=1;
- p does not divide 53*389*3 and p>0=k-2;
- E[p] is absolutely irreducible: a reducible representation would yield a rational p-isogeny, excluded by Mazur for p>163; the nontrivial unipotent inertia at 389 (v_389(Delta_min)=1) rules out geometrically reducible but F_p-irreducible representations.

Chida--Hsieh's Theorem D states that, for the **fixed p**, all but finitely many characters chi of the 53-primary anticyclotomic extension have nonzero normalised central L-value mod a prime over p. The Frobenius depth lemma says all characters chi of order 53^n with n >= m_p are regular at p. Therefore some chi satisfies both

    L(E/K,chi,1) != 0,
    chi(Frob_pi) != 1.

As 53 is odd, chi has a unique square root psi among 53-power characters. The associated weight-one CM form g=theta_psi has distinct p-roots and

    L(E,ad^0(g),1) = L(E^K,1)*L(E/K,chi,1) != 0.

This **resolves the auxiliary nonvanishing-and-regularity existence question separately for every admissible p**, without assuming a conductor bound independent of p. It is an application of the published theorem, not a finite computation of the L-values.

## Exact boundary and next theorem to attack

The theta in Castella--Hsieh Theorem B is Theta_{E/K,p}(T) over the *p-anticyclotomic* tower, not the 53-anticyclotomic auxiliary tower. Fixing 53 and choosing auxiliary chi does not imply

    ord_T Theta_{E/K,p}(T) = 2.

If this independent order-two statement is proved at an admissible p, then Castella--Hsieh Theorems A and B give dim_{Q_p} Sel(Q,V_p E)=2. Since rank E(Q)=2, this proves finiteness of Sha(E/Q)[p^infinity] (not vanishing or its order).

To prove full BSD for 389a1 one additionally needs the integral information on the p-primary size of Sha and the exact complex leading-coefficient identity. None of these follow merely from the auxiliary character lemma. **The next non-redundant attack is therefore the p-dependent quadratic theta coefficient / integral leading term, not further auxiliary-53 searches.**

## A concrete next target from the Gross-point distribution relation

For the **p-anticyclotomic** theta of Castella--Hsieh, their Appendix section 6 (immediately after the order-two criterion (6.1)) gives finite approximants of the form

    Theta_{p,n}(T) = alpha_p^(-n-1) * sum_{i=0}^{p^n-1} sum_{a in mu_{p-1}}
      (alpha_p*phi(P_n^{a*u^i}) - phi(P_(n+1)^{a*u^i})) * (1+T)^i,

where alpha_p is the p-unit Hecke root. Thus its quadratic coefficient is the exact, p-dependent Gross sum

    c_(2,p,n) = alpha_p^(-n-1) * sum_i sum_a
      (alpha_p*phi(P_n^{a*u^i}) - phi(P_(n+1)^{a*u^i})) * binom(i,2).

Their interpolation relation gives Theta_p(T) congruent to Theta_(p,n)(T) modulo (1+T)^(p^n)-1. Since (1+T)^(p^n)-1 is congruent to T^(p^n) modulo p, c_(2,p,n) mod p equals the quadratic coefficient of Theta_p mod p for p>2 and n>=1. Consequently a **certificate that c_(2,p,n) is nonzero mod p** proves an upper bound ord_T Theta_p <= 2; with the known symmetry/lower bound ord >=2 it proves exactly 2.

This isolates the right target for a uniform argument. It is only a sufficient criterion (the quadratic coefficient may be divisible by p but still nonzero in Q_p). No connection of this p-anticyclotomic sum with a single integer independent of p is asserted or proved here.

## Sources

1. M. Chida and M.-L. Hsieh, *Special values of anticyclotomic L-functions for modular forms*, Theorem D (2018): https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf
2. F. Castella and M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Theorems A and B (2022): https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864