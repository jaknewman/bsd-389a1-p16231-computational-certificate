# E389a1 — a SINGLE FIXED weight-one CM auxiliary form works for density arbitrarily near 1/2 of all primes

2026-11-22. **A genuinely p-uniform theorem about the auxiliary input
of Castella--Hsieh**, not a proof of uniform order-two theta
nonvanishing, all-p Sha finiteness, or the complex BSD identity.

The 2026-11-21 theorem allowing conductor-53 characters to VARY
with each split prime p can be strengthened: one can fix ONE
auxiliary theta form g, independent of p, and it is regular for
an explicit positive-density set of p. Arbitrarily high conductor
allows this density to approach the maximal split-prime density 1/2.

## 1. Published unconditional theorem: fixed g on density 1/2-epsilon

Set E: y²+y=x³+x²−2x, conductor 389, with squarefree
N^-=389 inert in K=Q(sqrt(-3)) and N^+=1. Fix the
anticyclotomic Z_53-extension of K. The *tower prime*
is 53. To apply Chida--Hsieh Theorem D, take the
*residual prime* ell=7, NOT the varying p of the
BSD Selmer problem. Then:
- 53² does not divide 389;
- (D_K,N^-)=gcd(3,389)=1;
- 7 does not divide 53*389*3;
- k=2, so 7>k-2=0;
- the residual representation E[7] is absolutely
  irreducible (its full GL2(F7) image is certified
  independently in this project).

By M. Chida and M.-L. Hsieh,
*Special values of anticyclotomic L-functions for
modular forms*, THEOREM D/5.9,
https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf,
all but finitely many finite-order anticyclotomic
53-power characters chi of the fixed tower satisfy
  L(E/K,chi,1) != 0
(in fact an appropriately period-normalized value
is nonzero modulo 7).

Thus for EVERY arbitrarily large k, one can
choose an anticyclotomic chi of exact order m=53^k
with this nonvanishing, then FIX it once and for all.
Since m is odd, choose its unique square root
psi=chi^((m+1)/2) so psi²=chi. Set
  g=theta_psi,
a single FIXED weight-one CM eigenform,
independent of the varying rational prime p.
For all good p split in K, p away from the
conductor and with p-ordinary E, the condition
of distinct p-stabilization roots of g is
  psi(mathfrak p) != psi(bar mathfrak p)
  iff chi(mathfrak p) != 1,
because psi^tau=psi^-1 and chi=psi².
The central adjoint factor is likewise FIXED:
  L(E,ad^0(g),1)
    = L(E^(-3),1)*L(E/K,chi,1) !=0.
The first factor is rigorously positive by the
archived exact interval for the quadratic twist.

The field cut out by chi is cyclic of degree m
over K and generalized dihedral of degree 2m
over Q (complex conjugation acts by inversion).
Chebotarev then gives, EXACTLY,
  **density{rational primes p split in K,
     chi(mathfrak p) !=1}=(m-1)/(2m).**

E is NON-CM because j(E)=112³/389 is rational
but NON-INTEGRAL, while all CM j-invariants
are algebraic integers. Sato--Tate for
non-CM E/Q shows its supersingular good primes
have density zero (for p>3 supersingularity
means a_p=0, one atom of measure zero).
Serre open image theorem removes at most
finitely many non-surjective residual primes.
Consequently the density is UNCHANGED if we
also impose good ordinary reduction and
surjective mod-p Galois action.

**THEOREM:** For every epsilon>0, there is
a single fixed weight-one form g with
nonzero central adjoint L-value satisfying
all its auxiliary regularity hypotheses at
a set of good ordinary, residual-surjective
rational primes of density
  (m-1)/(2m)>1/2-epsilon.
This is an unconditional application of published
nonvanishing, Chebotarev, Sato--Tate and
known rank-zero twist/non-CM facts.

The construction is existential in chi:
Chida--Hsieh Theorem D does not specify
a smallest conductor or an effectively
computable chi for a chosen epsilon.

## 2. Constructive fixed CHI OF ORDER NINE: density 4/9

The archived conductor-53 class group
  Pic(O_53) ~ C18
comes from h(K)=1, inert 53, and unit index 3.
A Gross-orbit character chi9 of exact order 9
is defined by chi9([ell19])=zeta_9.
The archived 18 full oriented Gross coefficients
give a finite toric period polynomial F with
  F(zeta9)=-3*zeta9*(1-zeta9²+zeta9³+zeta9⁴),
and the parenthesized algebraic integer is an
EXPLICIT unit in Z[zeta9].
Its cyclotomic norm is
  Norm(F(zeta9))=3^6=729 !=0.

The global Gross/Waldspurger source comparison is
documented in
  paper/389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md
and the optimality test for all 18 points was
user-executed at
  results/bsd389_chi53_all18_optimal_embeddings_USER_PASS_2026-11-05.md.
Under these faithful archived identifications,
Waldspurger gives
  **L(E/K,chi9,1)!=0**.
Thus the SINGLE EXPLICIT chi9 works for
an EXACT density (9-1)/(2*9)=**4/9**
of rational primes p, even before invoking
Chida--Hsieh's general theorem D.
Unlike the first theorem, the explicit chi9
central-value claim retains its archived
computer-assisted Gross test-vector provenance
rather than being independently rerun here.

## 3. Elementary EXACT Frobenius criterion modulo 53

Let p≡1 mod3 be a split prime, p≠53,
and write the Eisenstein prime above it as
  pi=a+b*omega,
  p=a²-ab+b², omega²+omega+1=0.
53 is INERT in K. Therefore
  (O_K/53)^× / (F_53)^× ~ C54
and the norm-one quotient is C54 under
  z -> z/bar z.
The image of global units O_K^× has order 3.
Hence Pic(O_53)=C54/C3=C18.
Any primitive order-nine character has kernel
order 2 on C18, so its full inverse-image
in C54 is the unique subgroup C6.

Writing
  **r_p=pi/bar pi ≡ pi²*p^(-1) mod 53,**
the exact, choice-independent criterion is
  **chi9(mathfrak p) !=1
      iff r_p^6 != 1 in F_(53²).**
The RHS is unchanged by conjugation pi<->bar pi,
multiplication of pi by any Eisenstein unit,
or changing the orientation of the order-nine
ring-class character.

Thus the Chebotarev density 4/9 is not merely
an existence statement; prime-by-prime
regularity is decided by O(log p) small-field
arithmetic once p=a²-ab+b² is represented.
There is no degree growing with p.

The stdlib-only file
 verification/bsd389_fixed_chi9_chebotarev_mod53_gate_20261122.py
checks the criterion, unit invariance and the exact
arithmetic on 15 previously selected split primes.
An independent local census of all primes <=200000
yielded exactly 8004 regular split primes among
17984 rational primes, consistent with (not proving)
the Chebotarev density 4/9.

## 4. Exact LIMIT: this does NOT bound Sha at the density-4/9 primes

Castella--Hsieh Theorem A+B also requires
  **ord_T Theta_(E/K,p) = 2**
for the UNTWISTED p-adic anticyclotomic
theta attached to the varying prime p.
The fixed finite ring-class character chi9
or fixed high-order chi from Theorem D
is auxiliary to the weight-one form g.
Its nonzero L(E/K,chi,1) is a DIFFERENT
central value from the quadratic coefficient
of the p-varying anticyclotomic theta.

There is no algebraic implication
  F(zeta9) a 3-unit
       => [T²]Theta_(E/K,p) a p-unit.
Indeed the 53-primary/tame finite
character projectors and the p-adic
T-adic augmentation jet are independent
coordinates. A formal group-ring product
can be constant nonzero in the chi9
component while its trivial-component
T² coefficient is zero.

Therefore **NO prime of Sha[p] is excluded
by the present theorem**. To obtain
full p-primary Sha finiteness via
Castella--Hsieh on the density set,
one still needs a NEW, independent
proof of ord_T Theta_(E/K,p)=2
for those primes. To prove full BSD
one also needs all other primes and
an exact complex leading-term formula.

This theorem is valuable precisely because
it isolates the TRUE variable-p obstruction:
the auxiliary choice can be fixed for density
as close as wanted to 1/2, rather than
continually varying the auxiliary data.


## 5. An exact quantifier barrier for any FINITE list of fixed characters

Let chi_1,...,chi_s be ANY finite-order anticyclotomic
ring-class characters of K, of any fixed conductors.
Let F be the compositum of their finite Galois
fields over Q, including K. Since F/Q has finite
degree d, Chebotarev gives a density EXACTLY 1/d
of rational primes splitting completely in F.
Every such prime splits in K and has
  chi_j(mathfrak p)=1 for ALL j=1,...,s.

Thus **NO FINITE LIST of fixed auxiliary weight-one
CM characters can be p-regular at EVERY sufficiently
large split p**, even after excluding finitely
many bad primes, because the simultaneous failure
set has positive density >=1/d.

For a SINGLE primitive character of order m,
the failure density is precisely 1/(2m),
while the success density is (m-1)/(2m).
This makes Section 1's approach "arbitrarily
close to all split primes" asymptotically optimal
in the class of fixed finite auxiliary data.

This is only a NO-GO for fixed auxiliary data:
allowing a character to vary with p (as in the
prior effective 53-adic-depth theorem) addresses
regularity at every split p, but does not produce
the missing order-two theta nonvanishing.
