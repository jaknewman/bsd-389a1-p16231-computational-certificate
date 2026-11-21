# E389a1: tame subfield descent of the division-field class obstruction, all good p

**2026-11-21. Proven unconditional algebraic-number-theoretic comparison,
not an all-large-p class number bound or a proof of global BSD.**

Let E/Q: y^2+y=x^3+x^2-2x, Delta_min=N=389,
E(Q)=Z^2 and E(Q)_tors=0. For a good p>=5 (p!=389)
let V=E[p], K=Q(E[p]), G=Gal(K/Q)=GL2(F_p), and
let S_p=Sel(Q,E[p]).

Fix a basis e1,e2 of V and put
  H = {diag(1,a):a in F_p^*}, |H|=p-1,
  F = K^H.
The isomorphism type of F/Q is independent of the basis:
all these H are conjugate in G.

## Theorem A. Degree-p^3 cyclotomic-complement field

One has
  [F:Q]=p*(p^2-1),
  [K:F]=p-1,
  F intersect Q(mu_p)=Q,
  F * Q(mu_p)=K.

Proof: |G|=(p^2-1)(p^2-p)=p(p-1)^2(p+1).
By the Weil pairing and full mod-p image,
K^SL2(F_p)=Q(mu_p), and determinant induces the
cyclotomic Galois character. The chosen H maps
isomorphically via det to F_p^*: H intersect SL2=1,
and G=SL2 ⋊ H. Thus the two fixed fields are
linearly disjoint and their compositum is K.
The degree formula follows. QED.

Moreover, H fixes e1, so F contains the coordinates
of the nonzero p-torsion point e1, i.e. Q(e1).
Since [Q(e1):Q]=p^2-1, the relative degree
[F:Q(e1)]=p. This relative extension need not be
Galois.

## Theorem B. Exact injection into the smaller class group

Define the *p-strict* finite Selmer group
  S_p^str=ker( S_p -> H^1(Q_p,V) ).
Let
  r_p = dim_Fp E(Q_p)/p E(Q_p)
      = 1 + dim_Fp E(Q_p)[p] in {1,2}.
For every p>=5, p!=389, there is a choice-of-basis
dependent but **injective** F_p-linear map
  S_p^str -> Hom_Fp(Cl(F)/p Cl(F),F_p).
In particular
  rank_p Cl(F) >= dim S_p - r_p
     = 2 + dim_Fp Sha(E/Q)[p] - r_p.

**Proof, including the formerly excluded p=97.**

(1) Local dimension. At good p>=5 the formal group
has Z_p-rank one, with torsion in E(Q_p) of
dimension at most one. Therefore its local Kummer
image has dimension r_p=1 or 2.
Since S_p localizes into this image,
dim S_p^str >= dim S_p-r_p.

(2) Kummer at the unique bad prime 389.
E has split multiplicative reduction of type I_1:
v_389(Delta)=1 and -c6=856 is a square modulo 389.
Tate uniformization supplies
  E(Q_389) ~= Q_389^*/q^Z,  v_389(q)=1.
Every point admits a representative u in Z_389^*,
by multiplying by an appropriate q-power.

Since K contains E[p] and p!=389, its 389-adic
completions contain the local p-torsion (in Tate
coordinates: mu_p and q^(1/p)). If Q is represented
by u, then over K_w a p-division point of Q is
represented by u^(1/p). The polynomial X^p-u has
unit discriminant at 389 (p is a 389-adic unit,
u is a unit), so adjoining u^(1/p) is an
unramified, possibly trivial, extension of K_w.
Thus the restriction of EVERY local p-Kummer
class at 389 is unramified over K_w, EVEN for p=97
where E(Q_389)/97 E(Q_389) may be nonzero.

At other finite ell!=p,389, E has good reduction,
the local Kummer classes are unramified, and remain
so over K. At p, the localization is zero by
definition of S_p^str. At archimedean places
p>=5 causes no obstruction.

(3) Restriction and global class field theory.
Since G contains a central scalar 2I acting as 2
on V, Sah's lemma gives H^1(G,V)=0.
Inflation--restriction thus injects
  S_p^str -> H^1(K,V)^G
and by (2) its image consists of everywhere
unramified classes. Since V becomes trivial
over K, class field theory identifies the target
with
  Hom_G(Cl(K)/p,V).

(4) Tame norm/extension descent for class groups.
Let A_K=Cl(K)[p^infty] and A_F=Cl(F)[p^infty].
Let j:A_F->A_K be extension of ideals and
N:A_K->A_F the ideal norm. Then
  N∘j=[p-1] on A_F,
  j∘N=Σ_{h in H}h on A_K.
Since p does not divide |H|=p-1, averaging
identifies A_K^H and (A_K)_H, and N/j
identify both with A_F. Reducing modulo p:
  (Cl(K)/p)_H ~= Cl(F)/p.

(5) Invariant covector. Let lambda in V^vee be
lambda(x e1+y e2)=x. It is H-invariant.
Given f in Hom_G(Cl(K)/p,V), composing lambda∘f
is an H-invariant F_p-valued homomorphism on
Cl(K)/p, hence (4) yields
  Hom_G(Cl(K)/p,V)
     -> Hom(Cl(F)/p,F_p).

This map is INJECTIVE. Indeed if lambda∘f=0,
the image of f is contained in ker lambda,
a proper 1D subspace of V. Because f is
G-equivariant, im f is G-stable, and
V is irreducible under full GL2(F_p).
Therefore f=0.

Composing (3),(5) gives the theorem. QED.

## Theorem C. Sharp arithmetical obstruction without an exceptional 97

The Kummer exact sequence and rank(E)=2 give
  dim_Fp S_p=2+dim_Fp Sha[p].
The p-parity theorem combined with Cassels--Tate
on the finite reduced quotient says
  dim_Fp Sha[p] is even.
If Sha[p] is nonzero then its dimension is >=2.

Combining with Theorem B:
- if p does NOT divide #E(F_p) (non-anomalous),
  then E(Q_p)[p]=0, r_p=1, so
    rank_p Cl(F) >=3
  and **p^3 divides h(F)**.
- if p DOES divide #E(F_p), then r_p<=2, so
    rank_p Cl(F) >=2
  and **p^2 divides h(F)**.
  More precisely rank_p Cl(F)>=3 if local E(Q_p)[p]=0.

This applies to ALL good p>=5, including p=97,
without an extra local strictness condition at 389.

Actual exact point count:
  a_97(E)=-9, #E(F_97)=107, so p97 nonanomal.
Thus if Sha[97]!=0, necessarily 97^3|h(F_97).
The earlier p97 exclusion in the full-division-field
comparison was conservative and can be removed by
the Tate uniformization argument.

**Converses are NOT claimed.** The class group may
contain p-torsion unrelated to E's Selmer classes.

## Minimal degree for the tame fixed-covector construction

Suppose J<=GL2(F_p) has order PRIME TO p and fixes
a nonzero covector lambda in V^vee. Such J lies
in the stabilizer of lambda, whose group order
is p(p-1). By Lagrange, |J| divides p-1.
Therefore
  [K^J:Q]>=|G|/(p-1)=p(p^2-1).
Our H attains equality. This is an **optimality
statement ONLY within the prime-to-p subgroup
norm-descent method with a fixed covector**;
it does not rule out different p-ramified or
nonsemisimple class-group descents to smaller fields.

## What would be needed to actually finish the tail

A sufficient, entirely class-field-theoretic theorem would be:
there exists B such that, for every good p>B,
  rank_p Cl(F_p)<=2 if p is nonanomal,
  rank_p Cl(F_p)<=1 if p is anomal.
Then Sha[p^infty]=0 for all p>B.
A separate proof of finite p-primary Sha at the
remaining finite set of small primes would yield
global finiteness.

NO SUCH CLASS-RANK TAIL BOUND IS PROVED HERE, NOR
SUPPLIED BY THE CURRENT PRASAD--SHEKHAR LITERATURE.
Our theorem is a necessary condition and an
optimal reduction of field degree among tame
fixed-covector descents, not a new complete BSD proof.

At p=16231, the full division field has degree
69,399,181,987,336,800 and F_p has degree
4,275,981,638,160; even the smaller field
is not viable for brute-force class-group computation.
The existing finite Gross-theta and Castella--Hsieh
route is a more practical fixed-prime strategy.

Sources:
- D. Prasad, S. Shekhar, *Relating Tate--Shafarevich
  group of an elliptic curve with class group* (2021),
  https://arxiv.org/abs/1912.12928
- Tate uniformization, e.g. Silverman,
  https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf
- Norm relations, class groups of Galois subfields,
  https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12563
- Project's previous p6 criterion:
  paper/bsd389_uniform_classfield_p6_division_field_obstruction_20261121.md
