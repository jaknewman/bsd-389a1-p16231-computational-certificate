# E389a1 — an effective prime-uniform regular auxiliary character theorem in the fixed 53-anticyclotomic tower

Date: 2026-11-21. **Unconditional global number-theoretic theorem**, combined with the authentic nonvanishing Theorem D of Chida--Hsieh under its precisely stated residual conditions. NO global Sha finiteness, all-prime theta2 nonvanishing, or complex BSD identity is asserted.

This paper NEVER uses the already completed case-specific theta computation. It treats every rational prime splitting in K in a uniform, elementary fashion.

## Setup

E/Q: y^2+y=x^3+x^2-2x, conductor 389.
K=Q(sqrt(-3)), O_K=Z[omega], omega^2+omega+1=0,
class number 1, units mu6.
The unique bad conductor prime 389 is inert in K (389=2 mod3).
Tower prime l=53 is ALSO inert in K (53=2 mod3), is good ordinary
for E (a_53=-6) and 53^2 does not divide conductor 389.

Let q>=7 be ANY rational prime with q=1 mod3, q!=53.
Then q splits into distinct prime ideals in K,
and q=N(pi), pi=a+b*omega with a,b integers and b!=0:
   a^2-a*b+b^2=q.
Its conjugate is pi_bar=(a-b)-b*omega.
The quotient u_q=pi/pi_bar=pi^2/q is a 53-adic unit of norm one.
It represents, up to inversion, the Frobenius at a prime over q
in the 53-primary anticyclotomic ring-class tower.

## Theorem 1 — an exact Lucas integer computes the Frobenius depth

Define the order-2 integer recurrence
   U_0=0, U_1=1,
   U_(n+2)=(2a-b)*U_(n+1)-q*U_n.
Then the exact identity in O_K is
   pi^n-pi_bar^n=b*(1+2 omega)*U_n.
At n=54,
   **m_q := v_53(b U_54)
         = v_53((pi/pi_bar)^54-1) >=1.**
Here v_53 is the integer valuation in the unramified
quadratic extension K tensor Q_53, normalized by v_53(53)=1.

Proof. pi, pi_bar have trace 2a-b and product q.
Their divided difference satisfies the displayed recurrence.
The difference pi-pi_bar=b(1+2omega), where 1+2omega
is a 53-adic unit. Since q!=53, pi_bar is a 53-adic unit.
The norm-one residue group of F_(53^2)^*/F_53^* has order
53+1=54; raising u_q to 54 gives 1 mod53.
Hence m_q>=1. QED.

The integer bU_54 is NONZERO. If it were zero, then
(pi/pi_bar)^54=1, so the global element pi/pi_bar
would be a root of unity of K, and (pi)=(pi_bar).
That is impossible for a split prime q.

The number m_q is INDEPENDENT of the norm-generator:
multiplying pi by any unit eps in mu6 multiplies
pi/pi_bar by eps/eps_bar=eps^2 of order <=3,
which disappears on raising to 54; conjugating pi
inverts u_q and preserves v_53(u_q^54-1).
Thus this is a genuine, choice-free Frobenius invariant.

## Theorem 2 — exact regularity threshold in the class-field tower

The 53-primary part of Pic(O_(53^r)) has cyclic order
   53^(r-1),   r>=1,
because 53 is inert, K has class number one,
and the tame factor 54 is prime to 53.
The global unit factor mu6 is also prime to 53.

Under the usual identification of this 53-part
with the norm-one principal units modulo 53^r,
the Frobenius class of a prime over q is represented
by pi/pi_bar (or its inverse depending on reciprocity).
A primitive character chi of the 53-primary cyclic
quotient at conductor 53^r is faithful.
The norm-one Teichmuller factor has order 54
and disappears in the 53-primary quotient.
Thus, by Theorem 1, the Frobenius class is NONTRIVIAL
in the quotient if and only if r>m_q.

**For EVERY primitive 53-power anticyclotomic ring-class
character chi of conductor 53^r with r>m_q:**
  **chi(q-prime) !=1 and chi(q-conjugate-prime)!=1.**

The two p-stabilization roots of a CM theta series
g=theta_psi, with chi=psi^2 and psi^tau=psi^-1,
are thus DISTINCT at the target prime q, whenever
q is ordinary for E and the weight-one setup applies.
This is a uniform regularity result, not a
claim of nonzero generalized Kato class.

## Theorem 3 — an effective unconditional conductor bound

Since |pi|=|pi_bar|=sqrt(q) under the complex embedding,
  |pi^54-pi_bar^54| <= 2 q^27.
But pi^54-pi_bar^54 is a nonzero algebraic integer,
divisible by 53^(m_q) in O_K.
Every nonzero element of O_K has complex absolute
value at least 1 (its norm is a positive integer).
Therefore
  **53^(m_q) <= 2 q^27.**

In particular ANY integer r such that
  **53^r > 2 q^27**
is strictly greater than m_q, and all primitive
order-53^(r-1) characters of conductor 53^r are
regular at q.

The bound r is O(log q), completely effective,
and requires NO ring-class-field construction
or gigantic class group computation.
The actual exact threshold m_q+1 is often
much smaller, and is computed in 54 integer
recurrence steps.

## Theorem 4 — existence of a simultaneous REGULAR and NONVANISHING auxiliary form

Let q>=7 be ANY rational prime with
 (i) q=1 mod3 (split in K),
 (ii) q!=389 and E has good ORDINARY reduction at q,
 (iii) the residual representation E[q] is
      absolutely irreducible (the project has a
      separately certified uniform surjectivity result).

**Chida--Hsieh Theorem D / Theorem 5.9** applies with
tower prime p_tower=53 and residual prime ell=q:
- 53^2 does not divide N=389;
- (D_K,N^-)=gcd(3,389)=1;
- q does not divide 53*389*3, and q>k-2=0;
- the residual E[q] representation is
  absolutely irreducible.

The paper proves that for ALL BUT FINITELY MANY
finite-order characters chi of the 53-primary
anticyclotomic extension,
  L(E/K,chi,1)/Omega_(f,389) is nonzero modulo
  the prime above q, hence its complex central
  value is NONZERO.

By Theorem 2, every primitive chi of sufficiently
large conductor 53^r (r>m_q) has
  chi(q-prime)!=1.
The intersection of these two cofinite subsets
is nonempty and indeed infinite.

Choose such a chi, and the unique odd-order
square root psi with psi^2=chi.
Then g=theta_psi is a genuine CM weight-one
auxiliary form with distinct q-stabilization
roots. The already independently certified
  L(E^(-3),1)>0
implies
  L(E,ad^0(g),1)
     =L(E^(-3),1)*L(E/K,chi,1)!=0.

**Corollary:** for ALL primes q satisfying
(i)--(iii), the auxiliary "Rankin central value
nonzero + regular weight-one stabilization"
gate of the Castella--Hsieh generalized Kato
criterion is SOLVED UNIFORMLY. One does not need
a newly invented auxiliary field or an explicit
central L-value computation for each q.

Theorem D makes no uniform effective statement
about its finite exceptional-character set as
ell=q varies. Accordingly, our explicit bound
r>m_q is effective for LOCAL REGULARITY alone.
It is **not an explicit upper bound for the
least conductor giving simultaneous central
nonvanishing**. No such stronger bound is claimed.

Primary source, visually inspected at printed p. 3:
M. Chida and M.-L. Hsieh,
*Special values of anticyclotomic L-functions
for modular forms*, Theorem D / 5.9,
https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf

## 5. Actual independent arithmetic examples and reproducibility

An exact standard-library-only program performs:
  - Cornacchia-type norm representations q=a^2-ab+b^2;
  - 54 recurrence steps for U54;
  - valuation m_q=v53(b*U54);
  - a direct, independent computation of
    (pi/pi_bar)^54 in (Z/53^(m_q+1))[omega];
  - the universal inequality 53^m <= 2 q^27;
  - the safe conductor exponent r.

Actual successfully checked split primes:

  q=7:    pi=3+omega,   m=1, first regular r=2.
  q=13:   pi=4+omega,   m=1, first regular r=2.
  q=97:   pi=11+3omega, m=1, first regular r=2.
  q=1297: pi=39+7omega, m=2, first regular r=3.
  q=1579: pi=42+5omega, m=2, first regular r=3.
  q=2383: pi=54+13omega,m=3, first regular r=4.
  q=4423: pi=67+omega,  m=2, first regular r=3.

Across 15 independent split primes, the exact depths
1,2,3 were all witnessed. The direct modulo-53^r
unit computations agree with the Lucas valuation
for all 15.

Verification:
  verification/bsd389_aux53_all_split_primes_effective_depth_20261121.py

## 6. The exact remaining global theorem, no disguised proof

A regular auxiliary g with L(E,ad^0 g,1)!=0
is only ONE of the hypotheses of the
generalised-Kato/Selmer criterion at q.

To conclude finite Sha(E/Q)[q^infty] by that
criterion still requires independently proving,
for all sufficiently large target q,
  ord_T Theta_(f/K,q)=2
or an equivalent nonzero appropriate
global Selmer/generalised Kato class.

The quadratic theta coefficient is q-adic and
depends on q. The present recurrence does
NOT establish its nonvanishing.
Nor can a method restricted to primes splitting
in ONE fixed imaginary quadratic field cover
all rational primes: any finite collection
of such fields omits infinitely many inert p
(see the project's earlier rigorous Dirichlet
obstruction note).

The missing all-prime support theorem and
the exact complex BSD leading term therefore
remain mathematically separate, although this
paper makes the AUXILIARY choice uniform on
the infinite split/ordinary subfamily.


## 7. Stronger theorem exploiting the global cubic CM units: exponent 18, NOT 54

The elementary conductor estimate in Theorem 3 can be
**improved by a factor of THREE in its logarithmic exponent**
by working modulo the global cubic units from the start.

**Theorem 5 (improved exact Frobenius valuation and effective bound).**
For every split rational prime q as above, compute the **18th**
power (only 18 ring multiplications/power operations):
  pi^18=A+B omega, with A,B in Z.
Exactly ONE of the three integers
  A, B, A-B
is divisible by 53. None is zero. Then

  **m_q=v_53(A*B*(A-B))**, and
  **53^(m_q) <= 2 q^9**.

Therefore every primitive 53-primary ringclass
character of conductor 53^r is regular at q
as soon as
  **53^r > 2 q^9**.

**Proof (including the subtle cubic-unit normalization).**
The residual unit ratio u=pi/pi_bar lies in the
norm-one subgroup of F_(53²)^×, of order 54.
Thus u^18 reduces to one of the three cubic
roots of unity: zeta in {1,omega,omega²}.
Their reductions remain distinct because 53!=3.

Write pi^18=A+B omega and
pi_bar^18=(A-B)-B omega.
One obtains the THREE EXACT integral identities:
 if zeta=1:
  pi^18-zeta*pi_bar^18=B*(1+2omega);
 if zeta=omega:
  pi^18-zeta*pi_bar^18=(A-B)*(1-omega);
 if zeta=omega²:
  pi^18-zeta*pi_bar^18=A*(2+omega).
The three parenthetical factors all have
absolute norm 3, so are units at 53.
Exactly one identity has a difference divisible
by 53; the other two do not. Since pi is a 53-unit,
A,B,A-B cannot vanish simultaneously modulo53,
so exactly one among them is divisible by53.

Set x=u^18/zeta; it satisfies x=1 mod53.
Since 3 is a 53-unit:
 v_53(u^54-1)=v_53(x³-1)=v_53(x-1)
             =v_53(pi^18-zeta*pi_bar^18).
The last valuation is exactly v_53(A B (A-B))
because exactly one factor is 53-divisible.
This equals the earlier Lucas invariant
v_53(b U_54), and is independent of pi and
reciprocity orientation.

The nonzero algebraic integer
D=pi^18-zeta*pi_bar^18 has complex absolute
value |D|<=2q^9. As D/53^(m_q) is a
nonzero algebraic integer in the imaginary
quadratic ring O_K, its complex absolute value
is at least 1. Thus
  53^(m_q)<=|D|<=2q^9. QED.

This bound is a **genuine gain** from the
global CM cubic-unit quotient, rather than a
numerical improvement from increasing precision.

Selected exact arithmetic:
  q=7:    m=1, first regular r=2, safe r=5;
  q=1297: m=2, first regular r=3, safe r=17;
  q=2383: m=3, first regular r=4, safe r=18;
  q=4423: m=2, first regular r=3, safe r=20.

For comparison, the old 54-power bound gives
safe r=14,49,54,58 respectively. Exact m+1
is the best conductor level for LOCAL regularity;
the safe formula bounds it without finding pi.
There is no claim of an effective conductor bound
for the simultaneous analytic Rankin nonvanishing,
whose finite exceptional-character set is not
effectively bounded by Theorem D.

The companion test script now also computes
A,B via O_K arithmetic at exponent 18,
independently cross-checks the U_54 recurrence
and the 53-adic local ring-power criterion,
and verifies the improved bound for all examples.
