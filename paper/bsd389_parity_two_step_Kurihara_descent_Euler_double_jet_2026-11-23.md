# 389a1 — parity-aware two-step conductor descent: a rigorous obstruction and an exact Euler-factor jet shift

**23 November 2026. Scope: elementary and published-theorem deductions; this document does NOT construct an all-large-prime degree-two Kurihara unit or a global annihilator of Sha.**

## 1. Exact arithmetic input and source

E: y²+y=x³+x²−2x, conductor389, root number +1, rank2, MW saturated basis P=(-1,1), Q=(0,-1). Good p>=5 with residual GL2(Fp) and Manin p-unit.

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Proposition 3.16, explicitly proves the Kurihara functional-equation parity:

    delta_n mod I_n = 0   whenever (-1)^nu(n) != w(E).

Primary manuscript (version number may differ from earlier arXiv numbering):
https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
The same source is textually accessible at
https://www.researchgate.net/publication/359435755_The_structure_of_Selmer_groups_and_the_Iwasawa_main_conjecture_for_elliptic_curves

Since w(E)=+1, EVERY odd number of auxiliary factors forces zero, whether or not their local Kummer matrix is invertible and whether or not their prime-depth local conditions are ideal:

    **delta_(q1*...*q_(2r+1)) = 0 (mod I_n).**

The user's actual p11, n0=397*991 calculation has delta_n0=1 mod11. Thus for EVERY distinct good 11-admissible auxiliary q≠397,991,

    **delta_(397*991*q)=0 mod11.**

This conclusion comes from the functional equation; it does not require enumerating the 520-million-class conductor when q=1321.

## 2. Why single-step *analytic* degree descent/extension cannot preserve units

At odd p, on the r-th augmentation graded piece of a group ring the inversion involution sends a top exterior/mixed monomial T1...Tr to (-1)^r T1...Tr; indeed

    sigma_i=1+Ti  implies  sigma_i^-1-1=-Ti/(1+Ti)
                              =-Ti+O(Ti²).

The Mazur–Tate functional equation relates the theta element and its inversion by the global root number w(E), so its pure r-factor coefficient d_r obeys

    d_r = w(E)*(-1)^r*d_r.

As p is odd, when w(E)=+1 and r is odd, 2*d_r=0 implies d_r=0 in Fp. In our case any unit-transport operation on Kurihara **NUMBERS** across a single auxiliary factor would immediately contradict the parity theorem. A conductor-reduction method preserving mod-p unit information, if it exists, must connect even auxiliary degrees (for example 4→2), not insist on preserving unit at every intermediate degree.

Important distinction: Kato's **COHOMOLOGY** derivatives need not have the same parity behavior; Kim explicitly warns after his Proposition 3.15 that nonvanishing of kappa_n and delta_n are NOT equivalent at each individual n. One must not transfer the analytic parity statement blindly to the cohomological classes.

## 3. Exact universal Euler-factor Taylor polynomial at any depth p^k

For a good auxiliary prime q with
    q≡1 (mod p^k),
    a_q(E)≡q+1≡2 (mod p^k)
the *usual local degree-two Euler polynomial*
    P_q(X)=1-a_q(E) X+q X²
satisfies, with X=1+T,

    P_q(1+T)
      = (q+1-a_q) +(2q-a_q)T +q T²
      ≡ **T² (mod p^k)**

as an identity of Z/p^kZ[T].

In particular its constant and first augmentation jets vanish to order p^k, and its SECOND jet is a p-adic unit, uniformly in q, p and k. For any finite polynomial or formal power series f(T),

    [T^(r+2)](P_q(1+T)*f(T))
       ≡ [T^r] f(T) (mod p^k)

for EVERY r>=0. This is a genuine algebraic degree-shift identity requiring no Sha finiteness hypothesis.

**Interpretation limitation:** This identity concerns the universal Euler polynomial in ONE formal cyclotomic augmentation variable T. The Kurihara number at conductor n=q1...qr is instead a mixed derivative in r distinct auxiliary discrete-log variables of a Mazur–Tate element. Consequently this polynomial identity alone CANNOT remove two auxiliary factors from a nonzero Kurihara derivative. One needs an authentic global Euler-system compatibility plus a compatible multivariable Bockstein/divided-difference map that identifies the correct mixed coefficient. That comparison is precisely the unproved arithmetic bridge. Calling the Euler polynomial itself a 'two-factor descent operator' would be false.

Changing the Euler factor convention by X↦X^-1 or multiplication by a unit does not change its DOUBLE root at augmentation modulo p^k.

## 4. Why existing prime-exchange rigidity does not close 4→2

Castella–Sano (2026), *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Proposition 2.1.5:
https://arxiv.org/html/2601.14504

This proves a **rigidity of the divisibility index** of genuine Kato Kolyvagin classes when the set of allowed auxiliary primes is restricted to arbitrarily deep admissible sets. The proof can REPLACE a prime factor q in the conductor n by another admissible prime q′ through global duality and Kolyvagin-system relations. The replacements preserve the number of prime factors nu(n). Their proposition is NOT a degree-lowering theorem.

The p-adic Kato Euler/Kolyvagin system has *core rank one*, even for a curve with MW rank2; replacing core rank by the MW rank in a purported two-factor determinant is an error.

The actual missing 4→2 arithmetic step is a global rank-two derived Selmer/Fitting comparison, rather than a formal application of the already known exchange lemma.

## 5. Sharp logical minimal-degree barrier

For nonanomalous good p (E(Q_p)[p]=0) and the other Kim/Castella–Sano hypotheses, the mod-p minimal auxiliary degree satisfies the already proved project identity

    mu_p = dim_Fp Sel(E[p]/Q)
         = 2 + dim_Fp Sha(E/Q)[p].

Thus:
- if Sha[p]=0, minimal unit degree is two;
- if Sha[p] has dimension2, minimal unit degree is four;
- if dimension4, minimal unit degree is six, etc.

The extra dimension is even by p-parity/Cassels–Tate constraints for this rank-two sign-plus curve. A hypothetical **UNIVERSAL** degree-decreasing, unit-preserving operation 4→2 applied to an arbitrary primitive 4-factor coefficient would **force Sha[p]=0**: such a universal operation cannot be derived from the formal Kolyvagin axioms alone, because those axioms are compatible with higher-dimensional Selmer groups and mu_p=4.

Therefore, before claiming any uniform conductor descent, a proof must explicitly exhibit the additional **genuine global arithmetic information** it uses to rule out excess Sha dimensions. The fixed primitive 390-Manin vector, local MW determinant-unit Chebotarev selectors and the exact quadratic Euler-factor jet are independently useful, but none of them by itself proves the 4→2 step.

## 6. Concrete reproducible p11 checks

For q=397,991,1321,2113,3389,3433, each is good, prime, q≡1 mod11 and a_q≡2 mod11 (verified by exact point counts). The Euler polynomial satisfies P_q(1+T)≡T² mod11. At q=397 and 991 the coefficients are:

    P_397(1+T)=374 +770 T +397 T²
    P_991(1+T)=1045+2035 T +991 T².

All constant and linear terms are divisible by11 and the quadratic coefficients are ≡1 mod11.

This **does not** compute delta_(397*991*1321), whose exact mod11 vanishing instead comes from the already cited functional equation.

Reproducer: verification/bsd389_p11_Kurihara_parity_and_Euler_quadratic_jet_gate.py.

**Verdict:** We have pinned down the unavoidable EVEN-degree nature of any genuine unit-preserving conductor descent, together with the exact p^k Euler factor two-jet unit. The needed comparison between that jet and the conductor-dependent Kurihara MIXED derivative is not a theorem in the cited sources and remains the target.
