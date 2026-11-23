# 389a1 — uniform existence and exact Chebotarev density of arbitrarily deep Kurihara auxiliary primes

**2026-11-23. Unconditional mathematical theorem for all sufficiently large p, at every fixed p-adic depth k≥1.** The *availability* of two suitable primes q is proved, independently of the Tate–Shafarevich group. The **nonvanishing of the actual two-prime Kurihara number is NOT proved**; therefore no new all-p Sha or full BSD conclusion follows.

## 1. A genuine global hypothesis: E389a1 is non-CM

Let E/Q be the minimal curve y²+y=x³+x²−2x, N=389. Its invariants are b2=4, b4=−4, c4=112, Δ=389; hence

    j(E) = 112³/389 = 1404928/389,

which is not an integer (numerator is 249 mod389). The j-invariant of a CM elliptic curve is an algebraic integer, and a rational algebraic integer lies in Z. Therefore E is non-CM.

By Serre's open image theorem, for every **sufficiently large rational prime** p, the mod-p Galois representation of E is surjective onto GL_2(F_p). For p≥5 over Q, Serre's p-adic lifting result says mod-p surjectivity of the elliptic-curve representation implies full p-adic image GL_2(Z_p). Thus, for every such p and every fixed integer k≥1,

    Gal(Q(E[p^k])/Q) = GL_2(Z/p^kZ).

This conclusion does not use BSD or any Sha assertion. It supplies an (uncomputed) **uniform tail cutoff B(E)** from a proved theorem. The explicit 2026 project certificates for residual surjectivity may improve that cutoff, but we do not need or assert an explicit B here.

Source: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html (the documented Serre lifting equivalence for p≥5); Serre's open image theorem.

## 2. An exact positive-density Frobenius class for every depth

Fix p≥max(5,B(E)+1) and k≥1, and put R=Z/p^kZ and

    U = [[1,1],[0,1]] in GL_2(R).

Let C_{p,k} be its complete conjugacy class. For a matrix A=[[a,b],[c,d]] in GL2(R), the relation AU=UA is equivalent to **c=0 and a=d**. Hence

    Cent_G(U) = { [[a,b],[0,a]] : a∈R^×, b∈R },

whose cardinality is

    |Cent_G(U)| = |R^×|·|R|
                 = p^{k−1}(p−1)·p^k
                 = p^{2k−1}(p−1).

By Chebotarev, the set Q_{p,k} of good rational primes q≠p,389 whose p^k-division Frobenius is conjugate to U has the **exact natural density**

    **dens(Q_{p,k}) = |C_{p,k}|/|G|
                      = 1 / [p^{2k−1}(p−1)].**

In particular Q_{p,k} is infinite, and two distinct primes q1,q2 can always be chosen from it. No effective upper bound for the smallest q is claimed.

## 3. These primes meet every high-precision Kurihara local gate

For any q∈Q_{p,k}, Weil pairing and the elliptic Galois representation give

    q ≡ det(Frob_q) ≡ det(U) = 1 (mod p^k),
    a_q(E) ≡ tr(Frob_q) ≡ tr(U) = 2 (mod p^k).

Therefore

    q−1 ∈ p^k Z,           a_q(E)−q−1 ∈ p^k Z.

The Kurihara local modulus
    I_q=(q−1,a_q(E)−q−1)Z_p
is contained in p^kZ_p.

Moreover U modulo p is a **nonidentity unipotent** with exactly one eigenline for eigenvalue 1. Consequently E(F_q)[p] is 1-dimensional over F_p; equivalently E(F_q)/p E(F_q) is 1-dimensional. Thus these are exactly the **one-dimensional** local Kummer conditions needed for semilocal Kurihara–Kim methods, not scalar-Frobenius primes with two-dimensional unwanted local quotients.

For distinct q1,q2∈Q_{p,k},

    I_{q1q2}=I_{q1}+I_{q2} ⊂ p^k Z_p.

Hence a correctly normalized two-prime Kurihara number at n=q1q2 is mathematically **defined to p^k precision**. This proves the unconditional existence of the auxiliary input for the arbitrary-depth criterion already formalized in
    paper/bsd389_kurihara_deep_precision_sha_gate_2026-11-22.md
for every sufficiently large p, at any prescribed k. At k=2, the exact Chebotarev density is

    **1 / [p³(p−1)].**

## 4. Crucial dividing line: Chebotarev does not prove that δ is nonzero

The preceding construction controls *only local Frobenius matrices and the resulting local Selmer quotients*. It does not control the global modular-symbol weighted sum

    \tilde δ_{q1q2}(E) ∈ Z_p / I_{q1q2}.

For the p-tail, the **strictly sufficient** missing input is

    for all sufficiently large p,
      there exist distinct q1,q2∈Q_{p,2}
      such that v_p(\tilde δ_{q1q2}) ≤ 1
      (with the correctly normalized class nonzero modulo p²).

The already proved primewise Kim+Castella–Sano+Cassels–Tate depth criterion then gives Sha(E/Q)[p∞]=0: a nonzero depth-2 residue of valuation at most one bounds v_p(#Sha)≤1, but when finite the order of the p-primary Sha is a perfect square and its valuation is even. This is **weaker for a specific pair** than requiring \tilde δ modp to be a unit; the depth-2 witness may have valuation one.

The Chebotarev theorem just proved guarantees there are infinitely many pairs at the necessary depth; it **does NOT guarantee the global weighted-sum valuation bound**. Making that final nonvanishing uniform is exactly the new arithmetic theorem still to prove, likely requiring higher-rank derived Euler/Kolyvagin classes and an integral comparison. Do not replace it by an assertion of equidistribution of Kurihara sums: Chebotarev distribution of individual Frobenius classes does not imply such a distribution.

## 5. Checkable exact group arithmetic

A dependency-free Python test checks centralizer equalities at mod 9 and mod 25 and the exact centralizer formula; these tests verify the finite group count, NOT Serre's or Chebotarev's theorems.

Examples:
- p=3,k=2: |GL2(Z/9)|=3888, centralizer=54, conjugacy class=72; density=1/54.
- p=5,k=2: |GL2(Z/25)|=300000, centralizer=500, conjugacy class=600; density=1/500.
- p=11,k=2: centralizer=13310, density=1/13310.

**Verdict:** A new global **existence-and-density theorem for high-depth local Kurihara primes**, with an explicit conjugacy class independent of Sha. The failure of global BSD in this step is localized to **nonvanishing of the exact global weighted modular-symbol derivative on at least one of these available pairs for each sufficiently large p**. Neither a global integer D nor that nonvanishing theorem has been constructed here.
