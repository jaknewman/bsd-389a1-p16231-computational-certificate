# E389a1: unconditional all-good-prime Kurihara/Fitting formula and a regular GL3 obstruction

Date 2026-11-21. This note advances the uniform arithmetic reduction;
it does NOT claim full BSD or finiteness of the entire Sha.

E/Q: y^2+y=x^3+x^2-2x, N=389, Delta_min=389,
MW E(Q)=Z^2, E(Q)_tors=0, Tamagawa product 1.
The modular parametrization is optimal, with Manin constant 1.
LMFDB: https://www.lmfdb.org/EllipticCurve/Q/389a1/
LMFDB also reports maximal mod-p image for every rational prime.

Primary inputs, checked against printed theorem statements:

1. F. Castella and T. Sano, *On refined nonvanishing conjectures
   by Kurihara and Kolyvagin*, 2026-01-20, Theorem B, pp. 2--3:
   https://web.math.ucsb.edu/~castella/Kurihara.pdf
2. C.-H. Kim, *The structure of Selmer groups and the Iwasawa
   main conjecture for elliptic curves*, Amer. J. Math. (2026),
   Theorem 1.8, printed pp. 7--8:
   https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

## 1. A genuinely UNIFORM nonvanishing theorem, already in the literature

Let p >= 5, p != 389. This includes ordinary AND supersingular
good-reduction primes: E is non-CM, p is good, and N=389 is squarefree.
The mod-p image is surjective (LMFDB and the earlier Sage
all-prime certificate), and p does not divide the Manin constant 1.

Write delta_{p,n} for the collection of Kurihara coefficients
of the plus modular symbol at squarefree products n of
p-admissible auxiliary primes, as defined in the two papers.
Let M_r(p) be the minimum p-divisibility index of coefficients
whose auxiliary conductor has exactly r prime factors; take
+infinity if there are none nonzero. Let M_infty be the
decreasing even-degree limiting minimum of those indices.

**Theorem 1.** For EVERY p >= 5, p != 389,

  M_infty(delta_p) = v_p(Tam(E)) = 0.

**Proof.** Apply Castella--Sano Theorem B. Its ordinary clause
covers good ordinary p; the supersingular clause covers good
supersingular p when N is squarefree, as it is. All its Galois
and Manin hypotheses hold here. The Tamagawa product is 1,
so the asserted identity is zero. QED.

This means at least one coefficient of SOME auxiliary degree
is a p-adic unit for every such p. It does NOT say that an
auxiliary conductor of degree two has a unit coefficient.
Previously repeated attempts merely to prove existence of a
nonzero Kurihara number for each p are superseded by this
published all-prime theorem.

## 2. Exact UNIFORM identity for Fitt_2 of the full Selmer dual

Define
  S_p = Sel_{p^infty}(E/Q),  X_p=S_p^vee,
  A_p = Sha(E/Q)[p^infty],
and
  m_2(p) = M_2(p) = min_{nu(n)=2} v_p(delta_{p,n}),
with v_p(0)=+infinity and the finite modulus I_n properly
taken into account (see the published definitions).

**Theorem 2.** For EVERY p >= 5, p != 389,

  Fitt_{2,Z_p}(X_p) = p^{m_2(p)} Z_p

with p^{+infinity}Z_p=(0).

**Proof.** Theorem 1 ensures ord(delta_p)<infinity and
partial^(infinity)(delta_p)=0. Kim Theorem 1.8(1--2)
identifies the Selmer corank with ord(delta_p) and
Fitt_i(X_p) with p^{partial^(i)-partial^(infinity)}
at admissible indices i >= ord(delta_p), vanishing
for i < ord(delta_p).

As E(Q) has rank 2, corank(S_p) >=2. If a nonzero
two-factor coefficient exists, ord(delta_p)=2
(the zero-factor coefficient L(E,1)/Omega=0 and parity
rules out a one-factor coefficient), and the formula
for i=2 gives p^{m_2(p)}. If no two-factor
coefficient exists, ord(delta_p)>2 and Fitt_2(X_p)=0,
matching m_2(p)=+infinity. QED.

Independently, Kummer and Pontryagin duality give
  X_p = Z_p^2 (+) A_p^vee,
  Fitt_2(X_p)=Fitt_0(A_p^vee).
Thus **with no assumed finiteness of A_p**:

- m_2(p)=0 iff A_p=0.
- 0<m_2(p)<infinity iff A_p is finite nonzero, and then
    #A_p = p^{m_2(p)}.
- m_2(p)=infinity iff A_p is infinite, with
  positive Z_p-corank (of its discrete p-primary part).

For finite A_p the odd-primary Cassels--Tate alternating
pairing makes #A_p a perfect square. Thus **m_2(p)
is even whenever finite**; the only possible values are
0,2,4,... or infinity. A computed finite m_2=1,3,...
would be evidence of a normalization/theorem error.

For E's global sign +1, Mazur--Tate functional-equation
parity kills every odd auxiliary degree. Therefore
ord(delta_p) is even. If m_2(p)=infinity, ord(delta_p)>=4,
so the Sha[p^infty] corank is at least TWO:
  corank(S_p)=ord(delta_p)=2+corank(A_p).

This is a genuine uniform identity and strong structural
reduction, not a uniform upper bound on m_2(p).

## 3. Rank-one strict Selmer identity where MW localizes primitively

At primes p where the p-local elliptic Kummer quotient is
a rank-one Z_p module, and at least one saturated global
MW generator localizes primitively, the previously proven
exact strict Selmer sequence gives
  X_p^str = Z_p (+) A_p^vee
and hence:
  Fitt_1(X_p^str)=Fitt_2(X_p)=p^{m_2(p)} Z_p.

This holds for certified primes p=5,7,11,17,23,107,599,16231,
subject to the local certificates already archived.
DO NOT claim that the rank-one strict construction applies
to *every* p: at anomalous p, local p-torsion may enlarge
the local Kummer quotient; local MW primitivity is itself
a nontrivial p-dependent condition.

The FULL Selmer formula of Section 2 has no such local
primitivity restriction and is the correct uniform object.

## 4. The sharpened remaining global BSD problem

An actual proof of Sha(E/Q) finite would follow by constructing
a single independently certified nonzero integer D with
  D in Fitt_2,Z_p(X_p) for all p>=5, p!=389,
and separately proving finiteness at p=2,3,389.

By Theorem 2, for every eligible p this means
  m_2(p)<=v_p(D).
In particular m_2(p)=0 outside the finite set of primes
dividing D. Conversely, if the relevant prime-primary
components are all finite and nonzero for only finitely
many p, such a D exists (take product p^{m_2(p)}).
The theorem does NOT produce D.

A mere uniform bound 0<=m_2(p)<=C, with C fixed,
does NOT force Sha finite: a hypothetical algebraic
group direct_sum_p (Z/p)^2 has m_2(p)=2 at all p,
finite individually but infinite as a global direct sum.
Nor does Theorem 1's all-prime nonvanishing in some degree
force a finite m_2(p).

The necessary new input is a global control of degree TWO
Kurihara coefficients (possibly mod p^n), or an
independent p-uniform annihilator construction. In the
language of Selmer coranks, proving
  corank_Zp Sel_{p^infty}(E/Q) <= 3
for all but finitely many good p, plus parity (even corank),
would already force that corank to equal 2 at those p
and hence would prove p-primary Sha finiteness outside
the finite exceptional set. This alone still does NOT
force triviality at almost all p or finite global support.

## 5. General no-go theorem for a fixed regular GL3 2+1 transfer

Let V=V_p(E), de Rham at p with Hodge--Tate weights
{0,-1}. Let W be a two-dimensional de Rham representation,
psi a one-dimensional de Rham character, and R a
three-dimensional de Rham representation which is an
extension of psi by W (or conversely). Suppose its
off-diagonal coefficient module is exactly the UNTWiSTED
elliptic representation:
  Hom_Qp(psi,W) ~= V
as G_Qp-representations.

Then W ~= V tensor psi. If psi has Hodge--Tate weight h,
W has weights {h,h-1}. The multiset of Hodge--Tate weights
of R is {h,h,h-1} (also for nonsplit extensions).
In particular R is NOT Hodge--Tate regular.

**Conclusion:** no fixed regular de Rham 3-dimensional
2+1 extension of this architecture can realize V_p(E)
as its untwisted upper-right adjoint block. This theorem
allows arbitrary de Rham characters psi, not only Tate
twists. It does not exclude nonregular/Eisenstein
automorphic representations or entirely different
derived/cohomological transfer mechanisms.

## 6. Quantitative obstruction to high-weight mod p^n repairs

For the n-dependent regularized family
  R_{p,n}=T_p(E) (+) Z_p(k), k != 0,
the offdiagonal residual coefficient is
  T_p(E)(-k)/p^n.

**Necessary condition** for it to be isomorphic to
T_p(E)/p^n as a G_Q-module:
  (p-1)p^{n-1} | 2k.

Proof: compare determinants. The two determinants differ
by chi_p^{-2k}; the full cyclotomic image modulo p^n is
(Z/p^n)^*, a cyclic group of order phi(p^n).
Therefore chi_p^{2k}=1 modulo p^n implies the divisibility.

Hence every nonzero candidate satisfies
  |k| >= (p-1)p^{n-1}/2.
If we demand the stronger CANONICAL congruence
chi_p^k=1 mod p^n, then phi(p^n) | k.
The previous choice k=phi(p^n) realizes this
stronger congruence exactly, but necessarily has
unbounded integer weight as n grows.

This is a proven *weight-growth obstruction*, not
a proven lower bound on denominators of automorphic
periods and not an impossibility theorem for all
higher-rank automorphic approaches.

**Research decision:** for Sha uniformity, prioritize
the GL2 Kurihara/Selmer determinant theorem already
available above. Do not spend further cycles on
regular GL3 offdiagonal repairs unless a distinct
integral comparison mechanism is supplied.

## 7. Separate second BSD obligation

All results above address Sha. They do NOT prove the
complex exact leading-term equality
  L''(E,1)/2 = Omega_E Reg(E).
LMFDB gives numerical agreement with Sha_an near 1,
which does not identify the actual #Sha without
the global finiteness theorem and a genuinely exact
archimedean/integral comparison.


## 8. A sharp uniform mod-p Selmer dimension threshold

Let p>=5, p!=389. The Kummer exact sequence at level p is
  0 -> F_p^2 -> Sel(Q,E[p]) -> Sha(E/Q)[p] -> 0.
The p-infinity Selmer parity theorem (Dokchitser--Dokchitser,
*On the Birch--Swinnerton-Dyer quotients modulo squares*,
Ann. of Math. 172 (2010)) gives even corank for the
divisible Sha p-primary component because the analytic
root number is +1. The alternating Cassels--Tate
pairing on Sha modulo its maximal divisible subgroup
gives even F_p-dimension for the p-torsion of the finite
quotient (p odd). Combining both with rank MW=2:
  dim_Fp Sel(Q,E[p]) is EVEN.
See https://annals.math.princeton.edu/2010/172-1/p11 .

Therefore a bound as weak as
  dim_Fp Sel(Q,E[p]) <= 3
already forces dim_Fp Sel(Q,E[p])=2 and Sha[p]=0.
Consequently Sha[p^infty]=0 (every nonzero p-primary
torsion group has an element of order p).

**A useful all-prime sufficient criterion** is thus an explicit
finite set S and a proof of dim_Fp Sel(E[p]) <=3 for
every p>=5 outside S union {389}. It would yield finite
p-support of Sha; separate p-primary finiteness at
p in S union {2,3,389} would finish the global finiteness.

This is strictly weaker-looking than calculating exact two-factor
Kurihara numbers, but no such uniform dimension upper bound
has been proved in the project. It must come from a genuine
global cohomological/euler-system argument, not local
MW determinant surjectivity.

## 9. Why finitely many fixed auxiliary pairs cannot prove all-prime support

For any fixed auxiliary prime q used in a p-Kurihara number,
admissibility includes q == 1 (mod p). Hence
  p | (q-1).
For a fixed pair q1,q2, any admissible p divides
  gcd(q1-1,q2-1).
Thus a finite list of fixed pairs can certify only a
FINITE set of p. Examples from the archive:

| pair (q1,q2) | gcd(q1-1,q2-1) | eligible prime >=5 |
|---|---:|---:|
| (41,61) | 20 | 5 |
| (113,673) | 112 | 7 |
| (397,991) | 198 | 11 |
| (1667,5237) | 238 | 7,17 |
| (1289,3727) | 46 | 23 |
| (369793,383917) | 1284 | 107 |

Additional trace and Frobenius conditions may reduce the eligible
set further. This elementary fact rules out extrapolating
our finitely many archived pairs to a fixed p-independent
certificate. A true uniform result must construct q_i=q_i(p)
and control nonvanishing, or bypass pairwise Kurihara tests.
