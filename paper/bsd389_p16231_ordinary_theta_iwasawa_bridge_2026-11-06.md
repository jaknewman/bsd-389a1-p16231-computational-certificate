# From the certified finite theta c2 to the infinite anticyclotomic theta order

Curve E=389a1; prime p=16231; K=Q(sqrt(-3)). Date: 2026-11-06.

## Computed result (real Ubuntu full pass and CM closure)

For conductor p^2, H=p(p-1)/3=87809710 genuine quaternionic Gross classes, the exact native/Sage computation and independent postrun audit give
M0=M1=0, M2=4083 modulo p, and normalized coefficients
(c0,c1,c2)=(0,0,3739) modulo p.

The native run fully closed the ringclass orbit modulo the global cubic unit; the extra quaternionic norm19 step returned to Brandt class 9. This is an **established computation** for the exact finite theta polynomial under the repository's chart and eigenvector conventions.

## Exact literature formula

Castella--Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Appendix §6, displays (their n=1)

Theta_{f/K,1}(T) = alpha_p^(-2)
 sum_{i=0}^{p-1} sum_{a in mu_(p-1)}
 [alpha_p * phi_f(P_1^(a(1+p)^i)) - phi_f(P_2^(a(1+p)^i))]
 (1+T)^i,

with P_n^a=(r_n(a) Rhat) cap B and
r_n(a)=i_p^(-1)([1,a/p^n;0,1]).

The same appendix states
Theta_{f/K}(T) = Theta_{f/K,1}(T)
  modulo ((1+T)^p-1).

Since over F_p, (1+T)^p-1=T^p, their n=1 finite layer determines **every coefficient of degree below p modulo p** of the infinite Iwasawa theta.

The repository's true P2 right-ideal builder uses p^2*r_2(a) with a real p^4 local split chart. The globally verified mu3 invariance multiplies the reduced ringclass sum by 3. The P1 term is independent of i, so for k=0,1,2 it vanishes modulo p because
 sum_(i=0)^(p-1) binom(i,k)=binom(p,k+1)=0 (mod p).
Thus under the EXACT identification of this P2 chart/eigenform/reciprocity orientation with the appendix convention,
 [T^0,T^1,T^2] Theta_{f/K} = (0,0,3739) (mod p),
and in particular its actual T^2 coefficient is a p-adic unit.

## Why mod-p vanishing of c0,c1 is NOT enough without further input

A coefficient can be divisible by p without being zero in Z_p. To deduce actual ord_T Theta=2, prove c0=c1=0 exactly.

- The central value L(E/K,1)=L(E,1)*L(E^(-3),1) is zero because L(E,1)=0 (E has rigorously certified algebraic rank 2, plus the known rank-0 theorem if L(E,1) were nonzero). By the anticyclotomic Waldspurger interpolation formula (Chida--Hsieh, Theorem A), the square of Theta(1) is proportional to this central L-value. Therefore Theta(0)=0 **exactly**.
- The functional equation (Chida--Hsieh, Theorem B) is Theta^*=epsilon_p(f)*epsilon(f)*Theta composed with sigma_(N^+)^(-1). For this pair, p is good ordinary and split, N^+=1 because 389 is inert in K, and E has global root sign +1; the expected functional equation is precisely Theta^*=Theta. In the coordinate gamma=1+T the involution acts T -> -T/(1+T), so comparison of linear coefficients gives c1=-c1 and hence c1=0 exactly over Z_p.

Combining exact c0=c1=0 with c2=3739 mod p nonzero gives ord_T Theta_{f/K}=2.

**Crucial certification boundary:** the mathematical inference is valid once the identification of the *specific* repository integral Brandt eigenvector, optimal embedding, local r_n(a) coordinates, additive group ring conventions and p-stabilized theta normalization with Castella--Hsieh's theta is independently documented and verified. A finite raw Gross sum alone does not prove this identification. Unit changes of normalization preserve nonvanishing, but a nonunit or incorrect local test-vector comparison would invalidate the conclusion.

## Separate arithmetic consequences

Castella--Hsieh's Theorem B relates ord_T Theta=2 to nonvanishing of generalized Kato classes **under additional hypotheses**, including a suitable auxiliary ringclass character with L(E^(-3),1)*L(E/K,chi,1) nonzero, residual irreducibility/ramification and parity constraints. It does not, by itself, identify the exact p-primary Sha order or prove full BSD. An earlier rigorous interval for L(E^(-3),1) was reported, but the auxiliary chi conductor-53 Waldspurger L-value identification remains a separate unfinished gate.

References:
- https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864 (Appendix §6 and Theorem B)
- https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf (Theorems A, B, Lemma 4.2).
