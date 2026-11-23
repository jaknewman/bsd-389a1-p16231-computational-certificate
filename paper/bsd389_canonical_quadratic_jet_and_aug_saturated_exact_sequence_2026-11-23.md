# 389a1 — canonical quadratic-jet exact sequence and **augmentation-saturated** analytic Fitting presentation

**23 November 2026. Mathematically proved for every p≥5 and every depth m=p^k, using only the genuine Hecke/Mazur–Tate identities and elementary integral commutative algebra. The theorem DOES NOT identify the saturated analytic module with a Selmer or Sha group.** It makes the missing arithmetic comparison precise and removes the known forced augmentation factor, rather than conflating it with Sha.

## 1. Original arithmetic data and fully integral ring

Let q1,q2 be distinct GOOD deep Kurihara auxiliaries for E=389a1:
    qi≡1,   a_qi(E)≡2 (mod m),
where m=p^k, p≥5, k≥1, and choose an integral diagonal Mazur–Tate theta F(X) from the genuine Manin symbols. Let s be the Frobenius-inversion shift from Ota's published Mazur–Tate functional equation. Since m odd there is a unique t modm such that 2t≡−s modm; put G=X^t F. Then
    G(X)=G(X^−1),  G(1)=0,
in Z[C_m], with C_m=<X>. The genuine Hecke norm yields
    [T²]G(1+T) ≡ δ_(q1q2) (mod m)
with T=X−1. Centering cannot change this low coefficient modulo m because F(1)=0 and F'(1)≡0 modm.

Let h=(m−1)/2, let \iota(X)=X^−1, and define
    y=X+X^−1−2 = (X−1)²/X.
Put
    S_0(y)=2, S_1(y)=y+2,
    S_j(y)=(y+2) S_(j−1)(y)−S_(j−2)(y),
    P_m(y)=1+Σ_(j=1)^h S_j(y).
Then P_m is monic degree h, P_m(0)=m, and, for a power m=p^k,
    P_m(y) ≡ y^h (modp).

The inversion-invariant group ring is
    Z[C_m]^+ ≅ Z[y]/(y P_m(y)).
Its augmentation ideal I^+ has basis
    b_j=X^j+X^−j−2=S_j(y)−2, j=1,...,h.

Multiplication by y gives a **canonical Z-module isomorphism**
    \Phi: Q_m:=Z[y]/(P_m(y)) → I^+,
    f(y) ↦ y f(y).
(Proof: I^+=(y) in Z[y]/(yP_m), and multiplication y has kernel (P_m) in Z[y].)

Because G is symmetric and has zero augmentation, it has a UNIQUE quotient
    **U(y)∈Q_m with G=y U(y)** under the preceding identification.
No rational or p-adic division has been performed: the quotient exists over Z and is unique modulo the monic integer polynomial P_m.

## 2. The CANONICAL quadratic-jet quotient \epsilon_2

Define
    \epsilon_2:I^+ → Z/mZ
by
    **\epsilon_2(z)=[T²]z(1+T) (modm)**.

This is well defined on the group ring: in Z/m[T], the relation (1+T)^m−1 has ZERO coefficients in degrees 0,1,2, because m and binom(m,2)=m(m−1)/2 are divisible by m (m odd).

Under \Phi, \epsilon_2(y f(y))=f(0) modm: since y=T²/(1+T), it starts T² with leading coefficient 1, and higher powers y² start degree4.

In the genuine basis b_j this is the EXPLICIT row functional

    **\epsilon_2(b_j)=j² modm**  for every j=1,...,h.

As P_m(0)=m, evaluation at y=0 induces the exact sequence
    0 → y Q_m → Q_m --ev_0 modm--> Z/mZ → 0.
The map is canonical and surjective because \epsilon_2(b1)=1.

## 3. ACTUAL analytic theta multiplication and the saturation sequence

Let A_m:I^+→I^+ be multiplication by G. Under \Phi this is multiplication by y U(y) on Q_m.

For ANY admissible pair, with no Kurihara unit assumption,
    G I^+ ⊆ y I^+ = ker(\epsilon_2).
Therefore the SECOND DERIVATIVE functional always annihilates the genuine multiplication matrix:

    **(1²,2²,...,h²) · A_m ≡ (0,...,0) (modm).**

This is a striking explicit modular row relation on the user's real integer matrices, independent of p-unit nonvanishing. It is not a fabricated Selmer relation.

Since P_m(0)=m!=0, multiplication by y on the free Z-module Q_m has determinant
    det(m_y)=(-1)^h*m
and is injective.

Define the **AUGMENTATION-SATURATED analytic module**
    D_(p,k,q1,q2) := coker(m_U: Q_m→Q_m).
The completely **exact Z-module sequence** is

    **0 → D_(p,k,q1,q2)
          --[z↦y z]--> coker(A_m)
          --\epsilon_2--> Z/mZ → 0.**

Proof: use the nested integral lattices y U Q_m ⊆ y Q_m ⊆ Q_m.
The middle quotient Q_m/(yUQ_m) is coker(A_m); the right quotient Q_m/yQ_m=Z/mZ; and the kernel is yQ_m/(yUQ_m)≅Q_m/UQ_m because multiplication by y is injective over Z. All arrows and their kernels are explicitly defined, and the sequence does not require finite Sha or nonzero determinant.

In particular this precisely **removes the forced augmentation torsion** from the actual analytic cokernel:
    D is the kernel of the canonical quadratic-jet map \epsilon_2 on coker(A_m).

When the determinant is nonzero, the Fitting ideals are principal and
    **det(A_m)=(-1)^h m det(m_U)**,
hence det(m_U) is exactly the integral half-character spectral product divided by m, with a known sign. It is the actual *saturated determinant*, not just its p-adic valuation.

## 4. Full p-local primewise statement: zero defect iff genuine Kurihara p-unit

Over Z_p, put \bar Q_m=Q_m/pQ_m≅Fp[y]/(y^h). The genuine Hecke low-jet congruence gives
    **U(0)≡δ_(q1q2) (modp)**.

The determinant of multiplication by U modp on the local Fp-algebra \bar Q_m is
    det(m_U) modp = U(0)^h modp,
since in monomial basis the U multiplication matrix is upper triangular with U(0) on its diagonal.

Thus the following are EXACTLY equivalent for ANY deep admissible pair:

    (i)  δ_(q1q2) is a p-unit,
    (ii) U is a unit in Q_m⊗Z_p,
    (iii) D_(p,k,q1,q2)⊗Z_p=0,
    (iv) \epsilon_2:coker(A_m)⊗Z_p → Z_p/p^k is an isomorphism.

We also get the strengthened **SIGNED** half-resultant congruence, with the canonical true integer determinant A_m,

    **det(A_m)/p^k ≡(-1)^h * δ_(q1q2)^h (modp),**

for all admissible pairs, regardless of whether δ is zero modulo p. Squaring recovers the previous Boolean congruence
    B/m² ≡ δ^(m−1)∈{0,1} modp,
but this new signed congruence determines a genuinely refined square-root residue.

When (i) holds, the first term of the exact sequence vanishes after tensor Z_p and one obtains
    0→I^+_p --G--> I^+_p --\epsilon_2--> Z_p/p^k→0.
This gives the **explicit quotient map** behind the previously proved Smith form diag(1,...,1,p^k).

When δ≡0 modp, D⊗Fp !=0, and the p-rank of coker(A_m) is at least2. The extra p-rank is an analytic "augmentation-saturated defect" — **not automatically a dimension of Sha[p]**.

## 5. THREE genuine integer examples and direct row/cokernel verification

At m=5,11,25, user-verified true theta integer histograms give after centering:

| m | h | signed det(A_m) | det(m_U)=(-1)^h det(A_m)/m | det(m_U) modp |
|--:|--:|---:|---:|--:|
|5|2|−7,220|−1,444|1|
|11|5|−395,563,875,872|35,960,352,352|1|
|25|12|−151,753,339,112,452,007,665,001,265,791,485,409,507,737,600|−6,070,133,564,498,080,306,600,050,631,659,416,380,309,504|1|

The signed congruence predicts:
- m5: (-1)^2*4²≡1 mod5;
- m11: (-1)^5*1^5≡10 mod11 for **det(A)/m**, while det(U)≡1;
- m25: (-1)^12*22^12≡1 mod5.

The actual Z-matrices m_U, their determinants, the integral polynomial U and the row relation
    (j² modm)_j * A_m ≡0 modm
are verified in
    verification/bsd389_analytic_augmentation_saturation_exact_sequence_gate.py.

## 6. The precise Selmer-theoretic theorem still NOT obtained

The module D is now an *authentic explicitly presented analytic object* whose p-primary component VANISHES exactly at the primes/conductors where the two-factor Kurihara coefficient is a p-unit. This is an algebraic theorem, not an arithmetic identification with

    Y_p = Sha(E/Q)[p∞]^∨.

In particular:
- No natural map D⊗Z_p ↠ Y_p is constructed in this note.
- Such a surjection, if independently proved for a chosen pair (and for every p in a uniform argument), would immediately give Sha[p∞]=0 whenever δ unit. But assuming it without a new Euler/Kolyvagin reciprocity and genuine Selmer-complex comparison would just beg the main BSD question.
- The quotient \epsilon_2 is a **quadratic augmentation derivative**, not a regulator or an unproved integral height map.
- The recent Kim–Kurihara finite-layer Fitting theorems apply to specific p-cyclotomic towers and Selmer local conditions; their statements do NOT automatically yield a comparison for the varying diagonal fields ramified at two auxiliary q's.

**Status:** a complete integral exact sequence that demonstrably removes the unwanted p^k analytic torsion, the signed half-resultant formula, and an explicitly computable saturation matrix at three real conductors. No new global Sha finiteness or exact complex BSD proven. This is the correct algebraic presentation to feed to a *future genuinely arithmetic* comparison.
