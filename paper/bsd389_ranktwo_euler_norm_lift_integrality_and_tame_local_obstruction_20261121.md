# E389a1: rank-two Euler norm correction via the group-ring norm, and the genuine local trace obstruction

Date: 2026-11-21. **Proved algebraic lemmas, with explicit finite-field arithmetic.**
This is a new proof-cut, NOT an Euler system on actual elliptic cohomology,
a uniform Sha annihilator, or a complete BSD proof.

Curve: E: y^2+y=x^3+x^2-2x, rational saturated MW basis
P=(-1,1), Q=(0,-1), rank 2.
Let p>=5 and q != p,389 be a prime with p | (q-1) and
v_p(#E(F_q))=1. Let L=L_{p,q} be the unique cyclic degree-p
subfield of Q(mu_q); it is totally (tamely) ramified at q,
of residual degree 1. Write H=Gal(L/Q)=C_p,
R=Z_p[H], and N_H=sum_{h in H}h.

## 1. Source audit — the correct higher-rank Euler system norm

Burns--Sakamoto--Sano, *On the theory of higher rank Euler,
Kolyvagin and Stark systems, II: the general theory*,
accepted version, Definition 6.1, pp. 32--33:
https://kclpure.kcl.ac.uk/portal/files/345599305/bss-acceptedversion.pdf
The rank-r Euler norm uses the r-th exterior power of
corestriction, and ONE Euler polynomial
P_q(Fr_q^{-1}); Remark 6.2 explicitly corrects a previous
incorrect definition for r>1, making this normalization
audit essential.

For T=T_p(E) self-dual via the Weil pairing,
P_q(X)=1-a_q(E) X + q X^2. At the base F=Q,
Fr_q acts as 1, so P_q(1)=1-a_q+q=#E(F_q)=:M_q.

Put kP,kQ in H^1(Q,T) for the global p-adic Kummer
classes and omega=kP wedge kQ. Its rational image
is nonzero, since P,Q are independent.

## 2. Negative result, with a precise scope: integral SCALAR restriction fails

If one tries to define the level-L rank-two class by
  c_L = u*(res kP wedge res kQ)
with u in Z_p and the base class c_Q=omega, then
  Cor^{(2)}(c_L) = u*p^2*omega.
The prescribed Euler norm is M_q*omega, and
v_p(M_q)=1. Because omega is nonzero over Q_p,
the equality would require
  u=M_q/p^2,
whose p-adic valuation is -1, NOT in Z_p.

This proves the failure of the **scalar-u-in-Z_p
restriction-only recipe**. It does NOT assert that
every integral rank-two Euler class of the required
form is impossible. In particular, a rational
scalar multiplying a p-divisible class in a
group-ring exterior lattice may yield an integral
element: see the positive result below.

For the full Q(mu_q)/Q extension of degree q-1,
the analogous scalar is M_q/(q-1)^2, also of
valuation -1 when v_p(q-1)=1, but the definition
from BSS is formulated on abelian pro-p towers,
so the cyclic degree-p field L is the canonical test.

## 3. Positive correction theorem — norm element clears the denominator

Assume there exist two (not necessarily Kummer)
global cohomology classes
  yP,yQ in H^1(O_{L,S(L)},T)
such that
  Cor_{L/Q}(yP)=kP, Cor_{L/Q}(yQ)=kQ.

Group-cohomological restriction/corestriction gives
  res(kP)=N_H*yP,  res(kQ)=N_H*yQ.
In R one has the UNIVERSAL identity
  N_H^2=p*N_H
(since every h in H appears exactly p times
in the product N_H*N_H).

Consequently, in the R-exterior square,
  res(omega)=N_H^2*(yP wedge_R yQ)
            =p*N_H*(yP wedge_R yQ).

Define the group-ring integral candidate
  **c_L=(M_q/p)*N_H*(yP wedge_R yQ)**.

Here M_q/p belongs to Z_p because p|M_q.
The class is integral in the ordinary R-exterior
square, and hence has an integral image under the
canonical map to the Rubin exterior bidual whenever
the relevant integral cohomology/bidual setup is
defined as in BSS.

Under the BSS CORRECTED r=2 norm map,
  Cor^{(2)}(c_L)
    =(M_q/p)*aug(N_H)*(kP wedge kQ)
    =M_q*omega.
(The augmentation sends N_H to p.)

Equivalently, inside the *rational* exterior square,
  c_L=(M_q/p^2)*res(omega).
Although M_q/p^2 is NOT in Z_p, the entire class
is integral by the identity N_H^2=pN_H.
Thus negative p-adic valuation of a scalar ALONE
is not a proof of non-integrality in exterior-bidual
Euler-system theory. This repairs any misleading
strong interpretation of Section 2.

**No automatic existence of yP,yQ is asserted.**
The theorem is a valid one-level construction IF
the actual cohomological corestriction lifts exist,
and imposes no simultaneous norm compatibility
between distinct auxiliary q. Either issue is a
substantive arithmetic condition.

## 4. A real arithmetic obstruction to POINT-valued lifts

At q the curve has good reduction. Because L/Q has
degree p and is totally ramified at q, the residue field
of L_w is still F_q. For any R0 in E(L_w),
the group-law trace over H reduces to
  reduction(Tr_{L_w/Q_q} R0)
      =[p] reduction(R0) in E(F_q).
Therefore every POINT-valued local trace lies in
  p E(F_q).
This is exact; it uses only that H acts trivially
on the residue field.

If reduction(P) is nonzero in E(F_q)/p E(F_q),
then P cannot be the group-law trace of any point
in E(L_w), even after p-adic completion.
By Kummer naturality, **no local cohomology class
obtained from a point of E(L_w) can corestrict
to the Kummer class of P**.

For E389a1 at q41, p5, #E(F41)=45:
  [9] Pbar is nonzero 5-torsion,
  [9] Qbar = [3]([9] Pbar).
Thus both P and Q are nontrivial in E(F41)/5,
and NEITHER is a point trace from E(L_{5,41}).
This also holds for the tested q113/p7, q397/p11,
q1667/p17, q1289/p23 because the first local
row of P is a unit.

More generally, the map from the rank-two MW lattice
to E(F_q)/p has rank one for these auxiliary primes;
two independent point-trace lifts cannot exist.
Hence any actual two-corestriction-lift construction
as in Section 3 would require genuine GLOBAL GALOIS
COHOMOLOGY CLASSES with localizations outside the
usual good-reduction Kummer subgroup at q (i.e. classes
ramified at the auxiliary q), rather than just
new algebraic points in E(L).

This is an independent arithmetic reason WHY derived
Kato/Kolyvagin cohomology, not naive extra rational
points, is necessary for the proposed rank-two recipe.

## 5. Quantified first norm jet

Set b_q=M_q/p, a p-adic unit when p||M_q.
For any integral correction c_L satisfying the norm
  Cor^{(2)} c_L=M_q*omega,
the coefficient of omega in
  (Cor^{(2)} c_L)/p
after reduction mod p must be
  **b_q mod p**, a computable, nonzero target.

In the simple R-free model with yP,yQ corestriction
lifts, this first norm jet is realized by
  c_L=b_q N_H (yP wedge_R yQ).
The fixed source-point wedge by itself has
  Cor^{(2)}(res omega)=p^2 omega,
so its first norm jet is zero.

The computed targets for (p,q)=(5,41),(7,113),
(11,397),(17,1667),(23,1289),(107,369793)
are respectively 4,1,1,12,9,32.

See verification/bsd389_ranktwo_euler_norm_group_ring_gate_20261121.py
for exact integer, group-ring convolution and finite-field
point-law checks.

## 6. What a truly decisive theorem would now have to prove

Produce integral cohomology classes yP,yQ at a family of
auxiliary p-extension levels, or an equivalent derived
rank-two Euler/KS element, such that:
 (i) all the prescribed corrected exterior norm relations
     hold at EVERY auxiliary transition;
 (ii) local ramification at auxiliary primes is controlled;
 (iii) the derived system maps to the ACTUAL full rank-two
     Selmer dual via a correctly oriented integral Fitting
     inclusion;
 (iv) its leading coefficient is controlled by a FIXED
     nonzero rational/integer scalar independent of p.

Sections 2--5 prove useful necessary conditions and a
ONE-LEVEL CONDITIONAL POSITIVE SOLUTION to integrality,
but they do not prove (i)--(iv). No global Sha finiteness
or exact complex BSD equality is concluded.


## 7. Fundamental second obstruction: norm-corrected classes are Kolyvagin-imprimitive

The integral correction from Section 3 solves one Euler norm
equation, but is *too invariant* to yield a p-unit derived
Kolyvagin/Kurihara class. This is a new unconditional
group-ring obstruction with no assumptions about Sha.

Let R=Z_p[C_p], H=<sigma>, N=sum_{i=0}^{p-1}sigma^i,
and write the standard first Kolyvagin differential operator
  D=sum_{i=0}^{p-1} i*sigma^i.
For any a=sum_i a_i sigma^i in R:
  **a*N=aug(a)*N**,
since sigma^j N=N for each j.

In particular,
  **D*N=[p(p-1)/2]*N**.
This lies in p R for every odd p, so
  **D*(N*x)=0 mod p** for every R-module element x.
If c_L=b_q*N*(yP wedge_R yQ), then
  **D*c_L=0 mod p**
regardless of whether the actual corestriction lifts exist.

Over F_p[C_p] with T=sigma-1,
  N = T^(p-1).
Thus a group-ring class in N R is in the very high
augmentation degree p-1; since p>=5 this is at
least 4, and in particular its degree-1 and
degree-2 Taylor/augmentation coefficients vanish.
For s independent auxiliary C_p factors,
  N_{G_S}=prod_j N_j=prod_j T_j^(p-1) (mod p).
The mixed degree-two coefficient [T_1 T_2]
is zero, and so are all degree-two Kolyvagin
derivatives extracted directly from this pure-norm
group-ring class.

At nontrivial characteristic-zero p-power
characters chi of H, chi(N)=0. So the same
construction has zero nontrivial-character
specializations. It cannot encode the
nontrivial arithmetic variation detected by
a unit rank-two Kurihara coefficient.

**Consequent refined verdict:**
- Naive scalar-Z_p restrictions fail a one-level norm equation.
- The norm-projector correction can solve that norm equation
  INTEGRALLY if suitable cohomological lifts exist.
- But the resulting *pure norm-image* class is necessarily
  mod-p Kolyvagin-imprimitive.
- Therefore actual rank-two primitivity requires
  NON-invariant augmentation components, which must arise
  from genuinely arithmetic ramified Euler/Kato cohomology,
  not just the invariant span of two restricted MW points.

The algebraic identities are fully general for odd p, not
just for the sample auxiliary primes. The actual derivative
map from an Euler system to Selmer Fitting ideals still
requires all the Mazur--Rubin/Burns--Sakamoto--Sano
hypotheses; no assertion that every such non-invariant
component necessarily survives a regulator map is made.

## 8. Exact *global* corestriction-lift obstruction

The conditional yP,yQ from Section 3 must NOT be
postulated. They can instead be characterized by an
actual Galois cohomological boundary map.

For L/Q cyclic of degree p and a finite set of primes S
containing p, 389, q, and infinity, let
  I_H = ker(aug:Z_p[H]->Z_p).
Tensor the augmented induced representation sequence
by T=T_p(E):
  0 -> T tensor I_H
    -> T tensor Z_p[H]
    -> T -> 0,
where G_Q acts diagonally, using its quotient to H.
By Shapiro, the middle-term H^1 is H^1(O_{L,S_L},T),
and the map induced by augmentation is corestriction.

The connecting homomorphism in the long exact sequence
  partial_{L/Q}: H^1(O_{Q,S},T)
          -> H^2(O_{Q,S},T tensor I_H)
therefore has
  ker(partial_{L/Q}) = image(Cor_{L/Q}:H^1(L,T)->H^1(Q,T))
in the same ramification-relaxed S-cohomology.

Thus the proposed two lifts exist **if and only if**
  partial_{L/Q}(kP)=partial_{L/Q}(kQ)=0.

This gives a precise, finite-level, non-circular
ARITHMETIC TEST for the first missing input. A
certificate of these two H^2 vanishings at a few
auxiliary primes would not yet construct the
coherent Euler system or prove a uniform Fitting
bound, but it would settle the exact first gate
without assuming Sha finiteness.

Warning: the notation T tensor I_H means the
augmentation-ideal Galois module with diagonal
action; one must keep the integral Galois action
of the induced representation, not treat I_H as
a trivial module.


## 9. Conditional ALL-LEVEL norm-coherent construction, and why it still cannot be primitive

The Section 3 argument extends beyond one auxiliary prime,
and this sharpens the distinction between EULER NORM RELATIONS
and PRIMITIVITY of the resulting Kolyvagin system.

Fix p>=5 and a finite set S of distinct p-admissible
auxiliary primes q with p||M_q=#E(F_q) and p|(q-1).
Let L_q/Q be the cyclic degree-p subfield of Q(mu_q),
and let F_S be their compositum. Since the conductors
q are distinct, G_S=Gal(F_S/Q)=(C_p)^S, with
R_S=Z_p[G_S] and N_S=sum_{g in G_S}g.
Put b_q=M_q/p in Z_p^×.

ASSUME the existence of a collection of integral classes
  y_{i,S} in H^1(O_{F_S,S(F_S)},T_p(E)), i=P,Q,
with y_{P,empty}=kappa(P), y_{Q,empty}=kappa(Q),
and every transition satisfying
  Cor_{F_S/F_{S\{q\}}}(y_{i,S})=y_{i,S\{q\}}.
This is a STRONG arithmetic universal-norm hypothesis
and is NOT proved by the present project.

Define in the R_S exterior square
  c_S=(prod_{q in S}b_q)*N_S*
                  (y_{P,S} wedge_{R_S} y_{Q,S}).

**Algebraic theorem.** For every q in S,
  Cor^{(2)}_{F_S/F_{S\{q\}}}(c_S)
    =M_q*c_{S\{q\}}
    =P_q(Frob_q^{-1})*c_{S\{q\}}.
Hence these elements satisfy ALL the required higher-rank
Euler norm equations under the stated universal-norm
hypothesis, and are integral at every level.

Proof. Let S'=S\{q\}. The natural map R_S->R_{S'}
augments the new C_p-factor, and sends N_S to p N_{S'}.
Each y_i descends by assumption. Therefore
  Cor^{(2)} c_S
    =p*(prod_{r in S}b_r)*N_{S'}*
                      (y_{P,S'} wedge y_{Q,S'})
    =M_q*c_{S'}.
For general S', Frobenius of q in G_{S'} need NOT be
the identity. However c_{S'} is fixed by G_{S'}
because N_{S'} is a global norm element; hence
  P_q(Frob_q^{-1}) c_{S'}=P_q(1)c_{S'}=M_q*c_{S'}.
This point avoids an incorrect scalarization of Euler
polynomials on arbitrary non-invariant Euler classes.
QED.

**Two-prime numerical example** p=5:
M_41=45, M_61=70, b_41=9, b_61=14.
At the level F_{41}F_{61} the integral coefficient is
  b_41*b_61=126, i.e. c_{41,61}=126*N_41*N_61*wedge(yP,yQ).
Corestricting from the two-prime level to F_41
multiplies this coefficient by 5:
  5*126=630=70*9 = M_61*b_41,
as required. Corestricting down to Q gives
  25*126=3150=45*70.
The program also checks the same identities at p=7,11,17,
23,107 using archived true q,a_q input.

**Nonprimitivity nevertheless survives at ALL levels.**
Modulo p:
  N_S=prod_{q in S}(sigma_q-1)^(p-1).
Every q-derivative D_q with augmentation divisible by p
annihilates this pure-norm element modulo p. Its mixed
two-variable degree-two coefficient is zero.

Thus even a hypothetically norm-coherent integral rank-two
Euler system constructed ONLY in the invariant norm-image
is insufficient to yield a unit rank-two Kurihara witness
or a nonzero uniform Fitt_2. Its existence and its
p-primitivity are genuinely different arithmetic tasks.

The only credible next mechanism must add classes with
NONTRIVIAL group-ring augmentation/character components;
these cannot be manufactured by scalar rescaling of
MW wedges. The source-to-Selmer Fitting comparison and
p-uniform integrality then remain to be proved.
