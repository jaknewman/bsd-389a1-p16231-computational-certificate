# 389a1 — authentic one-variable diagonal Kurihara identity at **every p^k depth**, with a 28,488,750-term p=5, k=2 certificate

**23 November 2026.** The source-level theorem is proved by exact Mazur–Tate/Hecke distributions and formal integral group-ring algebra, **independently of Sha finiteness**. The displayed p=5 depth25 numerical output was **actually executed by the assistant** in compiled C++ using a separately archived genuine 390-Manin integral vector. It has **not yet been rerun independently by the user on Ubuntu**. No all-large-p Sha bound or full BSD claim is made.

## 1. Full p^k theorem

Let E:y²+y=x³+x²−2x (optimal curve 389a1, sign +1, L(E,1)=0). Let p≥5, k≥1, R=Z/p^kZ, and q1,q2 be **distinct good auxiliary primes** satisfying

    q_i≡1 (modp^k),     a_(q_i)(E)≡2 (modp^k).

Choose a primitive root g_i at each q_i and let λ_i:(Z/q_iZ)^×→Z/p^kZ be the discrete log mod p^k. This is well defined since p^k|q_i−1. Since q_i are odd and p is odd, automatically 2p^k|q_i−1, hence λ_i(−1)=0; this licenses exact plus-symbol half summation.

Define the Mazur–Tate plus element in the *genuine* finite quotient group algebra

    Θ_n(T1,T2)
      = Σ_(a∈(Z/n)^×) m_E^+(a/n)
            (1+T1)^λ1(a) (1+T2)^λ2(a)
       ∈ R[C_(p^k)×C_(p^k)], n=q1q2.

Let M_ij=[T1^i T2^j]Θ_n modulo p^k for 0≤i+j≤2. All these are unambiguously defined by the truncated polynomial group algebra because (1+T)^{p^k}−1 has no terms of degree <p^k, and p^k≥5.

**Theorem.**
    M00=M10=M01=M20=M02=0 (modp^k).
For any u,v∈(Z/p^k)^×, under the actual diagonal group algebra homomorphism γ_i→γ^u,γ^v, respectively,

    **[T²] φ_(u,v)(Θ_n) = u v M11 (mod p^k).**

Here the original **p^k-depth two-factor Kurihara number** is the class M11 in R, whose image in Z_p/I_n is the normalized Kurihara coefficient (provided the usual p-adic p-unit Néron/Manin period normalization is used). The corresponding local ideals I_{q_i}=(q_i−1,a_{q_i}−q_i−1)Z_p are contained in p^kZ_p.

**Proof.** The genuine Hecke/Manin norm relation is, for coprime good ℓ and m,

    proj_(mℓ→m) Θ_(mℓ) =
         (a_ℓ − σ_ℓ − σ_ℓ^−1) Θ_m.

The augmentation of Θ_q vanishes **exactly** because the augmentation of Θ_1 is m_E^+(0)=L(E,1)/Ω_E=0. For the projection T1=0 of Θ_(q1q2), let e=λ2(q1) and σ=(1+T2)^e. The above relation gives

    Θ_(q1q2)(0,T2)
        = [a_(q1)−(1+T2)^e−(1+T2)^−e] Θ_(q2)(T2).

Modulo p^k the bracket has zero constant (a_q1−2≡0) and zero linear coefficient (because σ+σ^-1 is invariant under inversion); it belongs to (T2²). Since Θ_q2(0)=0, the product belongs to (T2³) modulo p^k. Consequently M00=M01=M02=0. Interchange q1,q2 to get M10=M20=0.

Under T1=(1+T)^u−1 =uT+binom(u,2)T²+..., and T2=(1+T)^v−1 similarly, every degree≤2 term vanishes except M11*T1*T2, which contributes u v M11 T². QED.

**Caveat:** The diagonal cyclic theta is over a quotient of Q(ζ_(q1q2)) that varies with p and q1,q2. It is **not** the fixed cyclotomic Z_p-extension p-adic L function; no signed main conjecture may be applied to its leading coefficient without an actual transfer theorem.

## 2. Concrete 25-admissible pair discovered by exact finite-field search

    p=5, k=2, q1=5351, q2=10651, n=56,993,501.

Both are prime, distinct and good for E. They satisfy

    q1−1=5350=25·214,    a_q1(E)=−23≡2 (mod25),
    q2−1=10650=25·426,   a_q2(E)=2.

Independent exact curve point counting gives

    #E(F_5351)=5375=125·43,
    #E(F_10651)=10650=25·426.

The rational points P=(-1,1), Q=(0,−1), after projection to the corresponding prime-to-five parts of E(F_q), have local rows modulo 25

    q=5351: (1,14); q=10651: (1,2).

In detail, [43]Q=[64]([43]P) at q5351 and [43]P has exact order 125; and [426]Q=[2]([426]P) at q10651 and [426]P has exact order25. Hence the 25-level matrix has

    **det [[1,14],[1,2]] = 13 mod25, a UNIT.**

This is a genuine finite-field local saturation check, not a restatement of Chebotarev.

## 3. 28,488,750 representative full real Mazur–Tate calculation

The independent archival integer 390-Manin vector is encoded by 390 digits v+2∈{0,1,2,3,4}, with SHA256 of the resulting **390 raw digit bytes**:

    31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee.

(The SHA256 of the 390 ASCII digits is different and is NOT the canonical vector hash.)

A stand-alone compiled C++ program using continued-fraction Manin edges computed all

    φ(n)/2 = ((5351−1)(10651−1))/2 = **28,488,750**

plus-symmetry representatives at conductor n. Its exact source primitives use primitive roots

    g1=11 (mod5351), g2=7 (mod10651),

and the usual Néron-normalized integer modular symbols. It was run to completion on the assistant CPU on 2026-11-23. The **entire** low-degree bivariate moment matrix (rows i, columns j, 0≤i,j≤2), modulo25, is

          j0  j1  j2
    i0    0   0   0
    i1    0  22  16
    i2    0  17  14.

Thus the exact assertions are

    **M11 = δ_(5351·10651) ≡22 mod25**,
    **[T²]Θ_diagonal^(1,1) ≡22 mod25**,
    **M00=M10=M01=M20=M02=0 mod25**.

The primitive two-prime Kurihara number is already a **unit**, since 22≡2 mod5. It supplies a new authentic p5 witness at the deeper auxiliary precision p², independent of the earlier p5 pair (41,61).

Complete assistant stdout:

\`\`\`text
P5_MOD25_LOCAL_POINT_COUNTS 5375 10650
P5_MOD25_TRUE_LOCAL_MW_MATRIX [[1,14],[1,2]] DET 13
0 0 0
0 22 16
0 17 14
P5_MOD25_DEEP_Q1 5351 TRACE -23
P5_MOD25_DEEP_Q2 10651 TRACE 2
P5_MOD25_DEEP_COUNTS 28488750 nonzero_symbols 23811548
P5_MOD25_DEEP_MIXED_KURIHARA 22 diagonal 22 pure2 0,0 pure_linear 0,0 augmentation 0
P5_MOD25_EXACT_DIAGONAL_MATCH PASS
SECONDS 3.31445
\`\`\`

Source on this branch:
    verification/bsd389_p5_depth25_real_two_prime_diagonal_native.cpp

Reproduce on Ubuntu (with g++ available):

\`\`\`bash
g++ -O3 -std=c++17 -o /tmp/bsd389_p5_depth25 \
  verification/bsd389_p5_depth25_real_two_prime_diagonal_native.cpp
/tmp/bsd389_p5_depth25
\`\`\`

The above full sum is NOT a fresh independent Sage/eclib extraction of all 28 million modular symbols; it uses the historically separately checked frozen 390-Manin integer vector, the same approach that matched the authentic eclib p5 (41,61) and p11 (397,991) examples. For stronger provenance, independently spot-check random rational cusps in Sage/eclib on the user's machine.

## 4. True implication and honest global boundary

The **general depth p^k diagonal equivalence is PROVED** by exact Hecke norm algebra; the concrete p² witness is a new authenticated-from-Manin-vectors exhaustive example. It demonstrates that the rank-two diagonal reduction is *not merely a modp artifact*.

For all sufficiently large p, Serre and Chebotarev produce deep auxiliary q1,q2, but neither those theorems nor the diagonal identity forces M11 to have valuation≤1 for at least one such pair. Obtaining that uniform nonvanishing still requires a conductor-varying integral Kato/Kurihara–Selmer comparison or a genuinely new arithmetic nonvanishing theorem.

**No all-prime Sha finiteness or complex exact BSD leading-term identity is claimed.**
