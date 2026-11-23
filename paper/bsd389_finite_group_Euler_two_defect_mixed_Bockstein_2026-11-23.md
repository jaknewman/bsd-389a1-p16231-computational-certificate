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

## 5. New precise target suggested by the two-dimensional defect

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
