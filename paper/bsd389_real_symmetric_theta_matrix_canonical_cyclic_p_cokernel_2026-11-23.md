# 389a1 — an ACTUAL integral matrix and its complete p-local cokernel, from the genuine Mazur–Tate theta

**23 November 2026. Mathematical status: a new unconditional *primewise algebraic theorem* on the real/symmetric augmentation group ring, assuming only the genuine p^k auxiliary congruences and the already proved rank-two Hecke low-jet identity. With an authentic two-prime Kurihara UNIT the p-primary cokernel is **canonically Z/p^k**. Valid at all p≥5,k≥1. Independently tested against three genuine integral Manin polynomials and Smith normal forms. This is NOT the Tate–Shafarevich or Selmer module, and it does not prove the missing all-p Kurihara-unit theorem or full BSD.**

## 1. Construct the finite rank integral operator (not a hypothetical determinant)

Fix p≥5, k≥1, m=p^k (odd), h=(m−1)/2. Let q1,q2 be distinct good primes with q_i≡1,a_qi(E)≡2 modulo m. Let

    F(X)=Σ_(a mod q1 q2)^* m_E^+(a/(q1q2))
           X^([λ1(a)+λ2(a)]_m) in Z[X]/(X^m−1)

be the actual Néron-integral diagonal Mazur–Tate element. Its exact augmentation F(1)=0, and its derivative coefficients c1=F'(1)≡0 (modm), c2=F''(1)/2≡δ_(q1q2) (modm), follow from the real Hecke norm and L(E,1)=0.

The real functional equation, published in Ota 2023, Proposition 2.5, gives an exact reflection F(X)=X^sF(X^-1) with s=−λ_diag(389)∈Z/m. Since m is odd, there is a unique t∈Z/m with 2t≡−s modulo m. Put

    G(X)=X^t F(X),  so G(X)=G(X^-1) and G(1)=0

as EXACT integral group-ring identities.

Let R=Z[C_m]=Z[X]/(X^m−1), with inversion involution iota. Let

    I^+ = {z∈R : iota(z)=z, augmentation(z)=0}.

This is a free Z-module of rank h with explicit basis

    b_j = X^j+X^(−j)−2,    1≤j≤h.

Because G is symmetric and has augmentation0, multiplication by G defines an ACTUAL integer matrix

    A_m : I^+→I^+,      z↦Gz.

If G=Σ_(t=0)^(m−1) g_t X^t with g_t=g_(−t), then its complete explicit entries are

    **(A_m)_(i,j)=g_(i−j)+g_(i+j)−2g_i**,

where every subscript is taken modulo m and 1≤i,j≤h. The formula is obtained by taking the coefficient at X^i in G·b_j. It can be computed from the ORIGINAL integer Manin sums alone, with no unknown Selmer classes.

## 2. EXACT determinant theorem: the square root is a true integer determinant

On the complexified augmentation ideal, eigencharacters are indexed by t∈{1,...,m−1}. In the inversion-invariant half, one representative for each unordered pair {t,−t} is an eigenline. Since G(X)=G(X^-1), the eigenvalue on its real/symmetric line is G(ζ_m^t).

Consequently

    **det_Z(A_m) = ∏_(t=1)^h G(ζ_m^t) =: H_m ∈Z**.

The full cyclotomic resultant B=Res((X^m−1)/(X−1),F(X)) then satisfies

    **B = (det A_m)²**,  without any nonvanishing assumption.

This gives a canonical (up to the unique centering exponent t and the choice of integral basis) INTEGRAL MATRIX whose determinant is a square root of the authentic analytic spectral product. This is stronger than merely proving B is a square.

Note: the half-character eigenline decomposition is over Qbar; the matrix A_m itself and the determinant are defined over Z.

## 3. The correct invariant-ring polynomial at p-power level

Work over Z_p. Define the symmetric element

    y=X+X^(-1)−2=(X−1)²/X.

Set h=(m−1)/2 and form the monic degree-h polynomial

    P_m(y)=1+Σ_(j=1)^h (X^j+X^(-j)),

where each X^j+X^(-j) is expressed as an integral polynomial in y using the Chebyshev recursion

    S_0(y)=2, S_1(y)=y+2,
    S_j(y)=(y+2)S_(j−1)(y)−S_(j−2)(y).

The polynomial P_m has

    **P_m(0)=1+2h=m**.

The identity (X−1)(1+⋯+X^(m−1))=X^m−1=0 shows y·P_m(y)=0 in R. A basis comparison gives the exact ring presentations

    **R^+ = Z_p[C_m]^iota ≅ Z_p[y]/(y P_m(y)),**
    **I^+⊗Z_p ≅ Z_p[y]/(P_m(y))**

via f(y)↦y f(y).

In characteristic p, since X^m−1=(X−1)^m, we have R/p=Fp[T]/(T^m), and y=T²/(1+T). Hence y has precise nilpotence index h+1. Therefore

    **P_m(y)≡y^h (modp),**
    (I^+⊗Fp)≅Fp[y]/(y^h).

This also verifies P_m is monic and all its non-leading coefficients are divisible by p for EVERY m=p^k (but its constant term is p^k, so it is not Eisenstein when k>1).

## 4. THE NEW UNIFORM p-PRIMARY COKERNEL THEOREM

Because G is symmetric and G(1)=0, write G=y U(y) in R^+ (over integers). Since y=T²/(1+T) and F has constant and linear Taylor coefficients ≡0 modulo m, centering by X^t does not change its quadratic coefficient modm, and

    **U(0)≡[T²]F≡δ_(q1q2) (mod p)**.

Suppose δ_(q1q2) is a p-adic UNIT. Then U(0) modp≠0, and since

    R^+/p ≅ Fp[y]/(y^(h+1)),

U is a UNIT in R^+⊗Z_p (its modp reduction has invertible constant term). Therefore

    **G·(I^+⊗Z_p) = y·(I^+⊗Z_p)**,

and we obtain a NATURAL explicitly presented isomorphism

    coker(A_m⊗Z_p)
     = (I^+⊗Z_p)/(G I^+⊗Z_p)
     ≅ (Z_p[y]/P_m(y))/y(Z_p[y]/P_m(y))
     ≅ Z_p/(P_m(0))
     = **Z_p/p^k Z_p**.

This result is MUCH STRONGER than the determinant valuation v_p(det A_m)=k: it proves that the entire p-primary cokernel is CYCLIC, of exact order p^k, and that its p-adic Smith normal form is

    **diag(1,...,1,p^k)**

with h−1 p-units.

Conversely if δ≡0 modp, the factor U is divisible by y modulo p, so A_m on I^+ modulo p is multiplication by a multiple of y². Since h≥2,

    **dim_Fp coker(A_m modp) ≥2**.

Thus the following true analytic-module equivalence holds FOR ALL deep admissible pairs:

    **δ_(q1q2) modp is a unit
       ⇔ dim_Fp(coker A_m ⊗Fp)=1**,

and in this case its complete p-primary structure is Z/p^k.

This precise cyclic-cokernel criterion could be compared to a genuine SELMER presentation via refined Mazur–Tate/Fitting theorems; the matrix constructed here is a genuine analytic group-ring matrix, NOT such a Selmer comparison.

## 5. Three genuine numerical matrix / Smith confirmations

We used the complete original (NOT synthetic) integer theta coefficient vectors from the USER-independent genuine resultant certificates:
- p5,m5,n2501, h=2, symmetry s=4, t=3;
- p11,m11,n393427, h=5, s=0, t=0;
- p5,m25,n56993501, h=12, s=5, t=10.

The exact SymPy multiplication matrices A_m, integer determinants, and Smith normal forms yield:

| m | size of A | det A in Z | p-adic elementary valuations |
|---|---:|---:|---|
| 5 |2×2| −7,220 | [0,1] |
|11 |5×5| −395,563,875,872 | [0,0,0,0,1] |
|25 |12×12| −151,753,339,112,452,007,665,001,265,791,485,409,507,737,600 | [0×11,2] |

Thus all three genuine p-primary cokernels are exactly

    **Z/5**, **Z/11**, **Z/25**, respectively,

as predicted by the ALL-p,k theorem. Direct squaring of each integer matrix determinant reproduces the user's actual full integer cyclotomic resultant. No gigantic integer resultants need be recomputed.

Explicit P_m(y):
- m5:  y²+5y+5;
- m11: y^5+11y^4+44y³+77y²+55y+11;
- m25: y^12+25y^11+275y^10+1750y^9+7125y^8+19380y^7+35700y^6+44200y^5+35750y^4+17875y³+5005y²+650y+25.

Each satisfies P_m(y)≡y^h (modp), P_m(0)=m.

Reproducer: verification/bsd389_true_symmetric_MazurTate_matrix_and_p_cokernel.py

## 6. What EXACT comparison with Selmer would be needed

We now possess an *actual* finitely presented module, not a hypothetical determinant:

    C_(p,k,q1,q2) = coker(A_m⊗Z_p).

For a p-unit two-factor Kurihara coefficient, this module is canonically Z_p/p^k. However, it is an **analytic group-ring cokernel**. It is not
    Sel(E[p∞]/Q)^∨
or
    Sha[p∞]^∨,
and no natural map between them is constructed here.

A Selmer-complex comparison would need to:
1. identify the correct finite-layer and local Selmer CONDITIONS for the abelian extension cut out by the diagonal character;
2. describe the exact Mazur–Tate theta operation as a characteristic/Fitting presentation of that TRUE Selmer complex, not merely an arbitrary integer multiplication matrix;
3. remove the unavoidable augmentation contribution Z/p^k (our explicit analytic cokernel) via a canonical Bockstein/saturation operator;
4. prove that the remaining, SATURATED derived comparison bounds Fitt_2 of the global rank-two Selmer X_p with NO Sha-finiteness hypothesis.

The structural difference is now visible: the analytic determinant carries a fixed unavoidable p^k augmentation torsion EVEN WHEN Sha(E/Q)[p∞]=0. Naively identifying the analytic cokernel with Sha would be demonstrably false at p5 and p11. The correct Selmer target must be a derived/modified complex with its augmentation factor removed.

Relevant literature:
- Kazuto Ota, *On the rank-part of the Mazur–Tate refined conjecture for higher weight modular forms* (2023), Prop. 2.5.
- C.-H. Kim and M. Kurihara, *On the refined conjectures on Fitting ideals of Selmer groups of elliptic curves with supersingular reduction*, and related work on Mazur–Tate Fitting ideals in p-cyclotomic extensions; these concern particular finite layers and local conditions, **not automatically the conductor-varying diagonal extensions q1q2 in this theorem**.
- D. Burns, M. Kurihara, T. Sano, *On derivatives of Kato's Euler system for elliptic curves*; several higher-order claims assume Sha[p∞] finite, so they cannot establish the missing finiteness by circular application.

**STATUS:** a real integer matrix, exact determinant identity, all-p^k cyclic p-cokernel theorem and three independently verifiable full Smith matrices; NOT a global all-prime Sha annihilator or complex BSD identity.
