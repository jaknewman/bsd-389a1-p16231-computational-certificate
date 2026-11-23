# E389a1 — exact finite-group-ring obstruction to inverting the quadratic Euler factor; the missing mixed Bockstein map

**23 November 2026. Genuine universal finite-group-ring theorem, independently verified. This is an algebraic proof cut, not a proof of a two-factor Kurihara unit, a global Sha bound, or strong BSD.**

## 1. Context: a correct power-series identity can become noninvertible at finite level

Take any odd prime p≥5, depth a≥1 and m=p^a. Let C_m=<sigma> cyclic of order m and R=Fp[C_m]. Put T=sigma−1. By the freshman's dream in characteristic p,

    R = Fp[T]/((1+T)^m−1) = Fp[T]/(T^m).

For any genuine good p^a-admissible prime q (q≡1, a_q≡2 modp^a), the local Euler polynomial

    P_q(X)=1−a_q X+q X²

satisfies **P_q(1+T)≡T² (modp^a)** in the polynomial/power-series ring. Consequently it also satisfies this congruence modulo p in the finite cyclic group ring, **when X is represented by the chosen group-ring coordinate sigma**.

Important subtlety: in an ACTUAL Euler-system norm relation, the Frobenius appearing in P_q is an element of the Galois group of the OLD field, not automatically the generator of the NEW auxiliary cyclic factor. The calculations below model the algebra of any Euler multiplier that does identify with sigma; they do NOT establish that identification for Mazur–Tate/Kato conductor-changing maps.

Over power series, the formal coefficient shift F↦T²F has no kernel. Over R, it DOES have one because T is nilpotent.

## 2. Exact theorem: two-dimensional kernel and cokernel at every depth

**Theorem 1.** Multiplication by T² on R=Fp[T]/(T^m) has rank m−2, kernel dimension 2 and cokernel dimension 2. More precisely, there is an exact sequence of Fp-vector spaces

    0 → Fp² --iota--> R --(·T²)--> R --pi--> Fp² → 0,

where
    iota(u,v)=u*T^(m−2)+v*T^(m−1),
    pi(Σ_(j=0)^(m−1) a_j T^j)=(a_0,a_1).

**Proof.** On the basis 1,T,...,T^(m−1), multiplication T² sends T^j to T^(j+2) if j≤m−3 and to zero for j=m−2,m−1. Thus its image is (T²), its kernel is the span of the last two basis monomials, and its quotient is spanned by the first two. All claims follow; no number-theoretic assumptions are required.

At p11:
- C11: ring dimension 11, multiplication rank9, kernel spanned by T^9,T^10, cokernel represented by 1,T;
- C121: ring dimension121 after mod11, multiplication rank119, kernel spanned by T^119,T^120, cokernel 1,T.

The defect is ALWAYS exactly two, independently of p and depth a. It numerically matches rank E(Q)=2, **but there is NO canonical or proved arithmetic identification of these algebraic subspaces with the two Mordell–Weil directions P,Q**. Such a comparison would require new Kato/Selmer cohomological maps.

## 3. Two independent auxiliary variables: the defect GROWS

Let
    R_12=Fp[C_(p^a) × C_(p^b)]
        ≅ Fp[T1,T2]/(T1^m,T2^n),  m=p^a,n=p^b.

Multiplication by T1²*T2² has
    rank=(m−2)(n−2)
and
    dim ker = dim coker = mn−(m−2)(n−2)
                           = **2m+2n−4**.

This is proved by the monomial basis T1^i T2^j: a monomial survives the multiplier precisely when i≤m−3 and j≤n−3.

At p11, a=b=1 the kernel/cokernel dimension is
    **2*11+2*11−4=40**, not 2.
For p5, a=b=1 it is 16.

Thus naively iterating the single-variable two-dimensional Euler defect at two auxiliaries does **not** produce a rank-two global Selmer presentation; boundary terms proliferate.

## 4. An exact 'projection order matters' obstruction on the real Kurihara mixed jet

The mixed first-derivative coefficient of an n=q1q2 Mazur–Tate group-ring element lives in a multiaffine quotient with basis

    M = Fp[T1,T2]/(T1²,T2²)
      = span{1,T1,T2,T1*T2}.

The genuine two-prime Kurihara number is (up to primitive-root choices) the coefficient on T1*T2, after the full Mazur–Tate normalization.

But in M,
    **T1²=0=T2²**.
Therefore **multiplication by the quadratic Euler factor T_i² is the ZERO MAP on the quotient M**, even though the mixed Kurihara monomial T1*T2 is nonzero!

So a procedure that first projects an Euler norm relation to mixed first derivatives and then tries to invert a quadratic Euler factor loses all information. A valid arithmetic proof must instead construct a **higher Bockstein/divided-difference operation BEFORE projection**, and prove that this operator is compatible with the actual conductor-changing Galois actions and local Selmer conditions.

This is an explicit, checkable explanation of the missing bridge. It is not a no-go theorem for all motivic/regulator methods, merely for the naïve order-of-operations.

## 5. POSITIVE: the quadratic Euler multiplier CAN be inverted on every low-degree jet

The two-dimensional kernel in §2 consists **only of the very last** monomials T^(m−2),T^(m−1). Therefore it causes no ambiguity in the low augmentation coefficients.

**Theorem 2 (canonical low-jet quadratic quotient).** For every integer d with 0≤d≤m−3, multiplication by T² induces an exact Fp-linear isomorphism

    Fp[T]/(T^(d+1))  --×T²-->  (T²)/(T^(d+3)).

Its inverse D², defined by the explicit coefficient shift

    D²(Σ_(j=2)^(d+2) c_j T^j)
        = Σ_(r=0)^d c_(r+2) T^r,

is a canonical quadratic divided-difference map on the IMAGE ideal. In particular at every p≥5 the choice d=2 works even at first depth m=p.

The proof is immediate from the two monomial bases {1,...,T^d} and {T²,...,T^(d+2)}; their multiplication matrix is the IDENTITY. Thus **the finite-ring zero divisor is not an obstacle to recovering the low 2-jet of a truly Euler-multiplied series**. This significantly narrows the task: the blocker is identifying an actual normed arithmetic theta/Kato object with this formal Euler product, not the low-order algebraic division itself.

For two genuinely independent variables and a true factorization

    F(T1,T2)=T1² T2² G(T1,T2),

the mixed-jet identity

    **[T1*T2] G = [T1³*T2³] F**

holds modulo p whenever the finite conductor exponents are at least 5. This again is a formal theorem valid ONLY if the stated factorization is genuine.

### A REAL arithmetic test disproves applying this identity to the RAW Mazur–Tate theta

We independently summed all authentic Néron-normalized modular symbols for the two conductors already used in the project, using the historically authenticated 390-entry integer Manin vector. For q1,q2, let

    M_(i,j) = Σ_(a∈(Z/q1q2)^×) m_E^+(a/(q1q2))
              * binom(log_(gq1)(a),i) * binom(log_(gq2)(a),j) mod p,

where each log is represented by its integer residue 0,...,p−1. This is exactly [T1^i T2^j] of the RAW finite Mazur–Tate two-variable element after projecting to the p-Sylow group (no Euler norm applied).

Complete calculations (no samples):

| p | (q1,q2) | M_(1,1)=genuine Kurihara delta | M_(3,3)=RAW degree-six mixed jet |
|---|---|---|---|
|5 |(41,61) | **4** | **3** |
|11|(397,991)| **1** | **2** |

Thus in BOTH independent authentic examples,

    **M_(3,3) != M_(1,1) mod p**.

The full 5×5 p11 binomial coefficient matrix is

    [ [0,0,0,0,8],
      [0,1,1,3,10],
      [0,9,2,7,0],
      [0,4,5,2,9],
      [6,2,8,0,1] ]  (mod 11).

The p5 5×5 matrix is

    [ [0,0,0,0,0],
      [0,4,4,2,0],
      [0,0,4,2,1],
      [0,4,2,3,2],
      [0,1,3,2,4] ].

These data disprove treating the raw theta as though it had already been multiplied by T1²T2² in the norm-compatible comparison. They DO NOT disprove the correct quadratic divided-difference operator, because that operator acts on an **authentic Euler-normed** object, not arbitrary unnormalized moments.

Independent reproducible source:
    verification/bsd389_real_MazurTate_mixed_degree1_vs3_jet_countertest.py

**New precise mathematical target:** Construct an actual conductor-changing cohomological/analytic norm map whose image is divisible by the appropriate Euler factors in the CORRECT variables, and prove that its canonical low-jet divided differences commute with the true Kato–Kurihara mixed Bockstein map. Only then could the unit quadratic coefficient yield a two-prime nonvanishing criterion at every p.


## 6. New precise target suggested by the two-dimensional defect

The existing deep Chebotarev–Kummer theorem provides for all large p and all a≥1 two good auxiliary primes q_P,q_Q whose actual rational MW localization matrix has unit determinant modulo p^a. The algebraic exact sequence above shows a formally separate **two-dimensional** defect in one cyclic group-ring Euler multiplication.

To turn these into a genuine uniform rank-two arithmetic regulator, one would need:
1. the ACTUAL Euler-system norm/derived map, with its correct Frobenius coordinate, not an arbitrary identification X=sigma;
2. a canonical derived comparison between the one-variable kernel/cokernel of that map and the MW Kummer quotient (or Selmer complex determinant line);
3. compatibility with two-variable mixed Bockstein extraction and with Cassels–Tate/Poitou–Tate local conditions;
4. integral primitivity or a single p-INDEPENDENT nonzero determinant for the induced map.

**None of (1)–(4) is supplied by the finite-group-ring computation.** In particular equality of vector-space dimensions does NOT identify the modules, and invertibility of rational MW localization alone does NOT imply nonvanishing of a Kurihara mixed derivative.

We have nonetheless replaced a vague possible "divide by Euler factor" argument with an exact kernel/cokernel presentation and have identified the required order of operations.

## 6. Reproduction

Execute with ordinary Python:
    python verification/bsd389_euler_augmentation_two_defect_gate_20261123.py

The file checks the exact finite-level kernel/image/cokernel for (p,a)=(5,1),(7,1),(11,1),(5,2),(11,2), the two-variable dimension formula at p5,p11, and the annihilation of the four-dimensional multiaffine quotient by each local quadratic multiplier. The assistant actually executed this verification on 2026-11-23.

**Conclusion:** The quadratic Euler factor has a universally unit SECOND Taylor jet, but it is a zero divisor at finite p-power conductor and annihilates the mixed first-jet quotient. Any valid p-uniform 4→2 Kurihara descent must use a derived Bockstein comparison across conductor layers, not formal division in the finite group algebra. The global Sha finiteness and exact complex BSD leading coefficient are still not established.
