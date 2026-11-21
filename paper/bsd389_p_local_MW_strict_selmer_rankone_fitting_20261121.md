# E389a1 — exact local MW primitivity and rank-one strict Selmer Fitting theorem

Date: 2026-11-21. Based on branch \`proof/alpoge-gma-elliptic-selmer-transfer-2026-11-21\`.

**Status:** unconditional algebraic theorem for primes satisfying an explicit local
Mordell--Weil primitivity condition; that condition has been certified with
finite arithmetic for p=5,7,11,107,599,16231. No global Sha finiteness, no
uniform-all-p theorem, and no complex BSD equality is asserted.

## 1. Definitions and the exact p-local criterion

Let E/Q be Cremona 389a1,
  y^2+y=x^3+x^2-2x,
with its certified full Mordell--Weil group
  E(Q) = Z*P + Z*Q, P=(-1,1), Q=(0,-1).

Fix p>=5, p!=389, with p not dividing N_p=#E(F_p). Then E has
good reduction at p. Its formal group E_1(Q_p) is isomorphic
to p Z_p under its formal logarithm, and E(Q_p)/E_1(Q_p) has
prime-to-p order N_p. Thus

  E(Q_p)/p^n E(Q_p) ~= Z/p^n Z      (n >= 1),
  E(Q_p) tensor Q_p/Z_p ~= Q_p/Z_p.

Let t=-x/y denote the formal group parameter at infinity.
If for a rational point R one has
  t([N_p]R) in p Z_p \ p^2 Z_p,
then R maps to a generator of E(Q_p)/p^n for every n:
[N_p]R generates E_1(Q_p), and N_p is a p-adic unit.

We term this property the **local MW primitivity criterion**.
It is a statement about the actual elliptic point R, not
a Selmer-group computation.

## 2. Exact arithmetic certificate

Use the short integral model

  Y^2 = X^3 - 3024 X + 46224,
  X = 36x+12,  Y=216y+108,

which is a unit change of variables at all p>=5. Its
discriminant is 389*6^12. The short formal coordinate
t_s=-X/Y satisfies t=6 t_s (mod p^2) near infinity.
For p=5,7,11,107,599,16231, the program

  verification/bsd389_p_local_MW_strict_selmer_rankone_20261121.py

counts points by the exact Legendre sum, computes [N_p]P
and [N_p]Q modulo p^2 with Jacobian formulas, and handles
a point at infinity modulo p by an exact first-order formal-group
translation. The generic Jacobian addition formula alone is
not sufficient at that chart; the script includes a regression
at p=19 that explicitly traverses the infinity branch.

Output (nonzero entries are t([N_p]R)/p modulo p):

| p | a_p | N_p | P | Q | Q/P mod p |
|---|---:|---:|---:|---:|---:|
| 5 | -3 | 9 | 3 | 1 | 2 |
| 7 | -5 | 13 | 2 | 4 | 2 |
| 11 | -4 | 16 | 8 | 2 | 3 |
| 107 | 0 | 108 | 13 | 42 | 102 |
| 599 | 0 | 600 | 119 | 121 | 298 |
| 16231 | 128 | 16104 | 8987 | 7760 | 698 |

All six values for P are nonzero, proving the local MW
primitivity criterion for P at each displayed p, uniformly
in n. For p=5,7,11 the results are independently verified
with rational exact elliptic point addition using Python
Fractions and checking the t-parameter modulo p^2.

A broader **diagnostic** (not a uniform result) among good primes
5<=p<2000: 4 anomalous primes with p|N_p
(859,1213,1493,1951), and 2 primes where the tested P is
not primitive (223,419) but Q is; at the remaining 294
nonanomalous primes P is primitive. This supports the need
for an adaptive choice among MW points, and demonstrates that
one cannot claim P is primitive at every prime. This finite
diagnostic is NOT part of the six-prime committed verifier.

## 3. Rank-one strict Selmer theorem at finite levels

For every p satisfying the criterion, let
  R_n=Z/p^nZ,  S_n=Sel_{p^n}(E/Q), M_n=E(Q)/p^n E(Q)~=R_n^2.
Let K_n=E(Q_p)/p^n E(Q_p)~=R_n and define
  S_n^str = ker(S_n --loc_p--> K_n),
  M_n^str = ker(M_n --> K_n).

**Theorem.** For every n>=1 there is an exact sequence
  0 --> M_n^str --> S_n^str --> Sha(E/Q)[p^n] --> 0
and M_n^str ~= R_n. Consequently, noncanonically,
  S_n^str ~= R_n + Sha(E/Q)[p^n],
  Fitt_{1,R_n}(S_n^str) = Fitt_{0,R_n}(Sha[p^n]).

**Proof.** Kummer gives 0 --> M_n --> S_n --> Sha[p^n] --> 0.
Since P has primitive localization, M_n --> K_n is surjective.
For any s in S_n subtract a global MW Kummer class with the
same localization, giving s' in S_n^str representing the
same Sha class. The kernel is exactly M_n^str. The surjection
M_n~=R_n^2 --> K_n~=R_n has a unit coefficient on P, so its
kernel is a free rank-one R_n-module. Over the Artinian principal
ring R_n=Z/p^nZ, the regular module R_n is self-injective.
Thus the injection M_n^str ~=R_n into S_n^str splits, proving
the decomposition and the Fitting identity. QED.

The splitting is noncanonical, and finite-level Fitting ideals
over R_n can saturate to zero once valuations exceed n.
They do not give a nonzero p-adic ideal without additional input.

## 4. Rank-one strict Selmer theorem at p-infinity

Write S_p=Sel_{p^infty}(E/Q), A_p=Sha(E/Q)[p^infty],
L_p=E(Q_p) tensor Q_p/Z_p~=Q_p/Z_p,
M_p=E(Q) tensor Q_p/Z_p~=(Q_p/Z_p)^2.
Define S_p^str=ker(S_p -->L_p) and M_p^str=ker(M_p-->L_p).

Surjectivity M_p-->L_p, again by P, gives the exact sequence
  0 --> M_p^str --> S_p^str --> A_p --> 0,
with M_p^str~=Q_p/Z_p.

On Pontryagin duals,
  0 --> A_p^dual --> X_p^str --> Z_p --> 0.
Since Z_p is projective over Z_p, this splits:
  X_p^str ~= Z_p + A_p^dual.

Therefore the **unconditional exact Fitting identity**
  Fitt_{1,Z_p}(X_p^str) = Fitt_{0,Z_p}(A_p^dual).
Combining with the previously established rank-two identity
  Fitt_{2,Z_p}(X_p) = Fitt_{0,Z_p}(A_p^dual),
we obtain the new equality
  Fitt_1(X_p^str) = Fitt_2(X_p).
This is valid whether A_p is finite or infinite.

Important: 'rank-one strict Selmer' refers to the one *known
Mordell--Weil corank*. The full corank is
  1 + corank(A_p),
and need not equal 1 until the desired finiteness of A_p
has independently been established.

## 5. Bridge to the regularized 2+1 upper-right block

At level n the block
  B_{p,n}=Hom(Z_p(k_n),T_p(E))/p^n,
  k_n=(p-1)p^(n-1),
is a G_Q-module isomorphic to E[p^n] by Euler congruence.
Equip B_{p,n} with local condition zero at p and transport
the elliptic Kummer conditions at all l!=p. This defines a
Selmer structure whose global Selmer group is **exactly**
S_n^str under the coefficient identification.

Thus the two-step coefficient/Selmer comparison is now
arithmetically exact at all finite levels for this **chosen
strict local condition**. In particular the quotient by
the strict global MW subgroup is exactly Sha[p^n].

At p the natural *propagated torsion Bloch--Kato* finite
condition is in fact exactly zero (proof below). This is
stronger than merely defining zero by transport.

WHAT IS NOT PROVED: (i) that an actual global regular algebraic
automorphic realization of the 2+1 coefficient representation
exists with its own integral local conditions, (ii) an integral
automorphic complex whose p-adic Fitt_1 ideal is nonzero, or
(iii) a uniform fixed integer bounding it across all p.
The intrinsic local Bloch--Kato equality just proved at p is
not itself an automorphic realization or a global bound.

## 6. Next decisive theorem

A nonzero element d_p in
  Fitt_{1,Z_p}(X_p^str)
would prove that Sha(E/Q)[p^infty] is finite, for the given p.
A p-adic unit in that ideal would prove Sha[p^infty]=0.
The missing substantive result is the construction of d_p
(or a p-uniform fixed integer D) from authentic Euler-system,
derived Kato or automorphic integral data, with correct
direction of Fitting comparison.

This note does not construct d_p, does not deduce the result
from the mere existence of P, and does not close the exact
complex BSD leading-term equality.


## 5 bis. Exact intrinsic p-local Bloch--Kato condition, not merely dimension

We can improve the previous caveat at the single place p.
Fix p in the certified set and n>=1, and keep the weight
k=k_n=(p-1)p^(n-1). Write

  T'=T_p(E)(-k),  V'=T' tensor Q_p,  A'=V'/T',
  M=T'/p^n T'=A'[p^n].

Use the **standard propagated torsion Bloch--Kato condition**
  H_f^1(Q_p,M)
    = preimage in H^1(Q_p,M) of H_f^1(Q_p,A'),
where H_f^1(Q_p,A') is the image of H_f^1(Q_p,V')
in H^1(Q_p,A').

(1) V' has Hodge--Tate weights {k,k-1}, strictly positive,
and H^0(Q_p,V')=0, so Bloch--Kato's de Rham dimension
formula gives H_f^1(Q_p,V')=0. Consequently H_f^1(Q_p,A')=0.

(2) Since k is divisible by p-1, chi_p^{-k}=1 modulo p.
Thus T'/p T' is locally isomorphic to E[p]. Since E has
good reduction at p and p does not divide #E(F_p), one has
E(Q_p)[p]=0. Therefore H^0(Q_p,T'/p T')=0. This also implies
H^0(Q_p,A')=0: any nonzero invariant of the p-primary
torsion module A' would yield an invariant element of order p.

(3) The exact sequence
  0 --> M --> A' --p^n--> A' --> 0
now gives an injection
  H^1(Q_p,M) --> H^1(Q_p,A')
because H^0(Q_p,A')=0. Its preimage of
H_f^1(Q_p,A')=0 is therefore zero.

**Conclusion (proved, with precise definition):**

  H_f^1(Q_p, T_p(E)(-k_n)/p^n) = 0.

In particular, the *intrinsic propagated torsion* Bloch--Kato
condition of this explicitly chosen high-weight block agrees
with the strict condition at p, for each n. This does NOT
establish the existence of a global automorphic representation
whose off-diagonal block has these coefficients; nor does it
settle the comparison at every l != p at the integral level.

The precise torsion propagation convention matters: arbitrary
other finite-flat, syntomic or derived local conditions are not
silently identified with this one.

Reference on local conditions and propagation: Bloch--Kato,
*L-functions and Tamagawa numbers of motives*, 1990;
see also https://math.stanford.edu/~conrad/BSDseminar/Notes/L14.pdf
and https://www.math.keio.ac.jp/~kurihara/20.ASPMstyle.pdf .
