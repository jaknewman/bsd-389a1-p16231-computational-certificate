# E389a1: exact diagonal quadratic Mazur–Tate identity for the two-factor Kurihara invariant

**23 November 2026. New genuine all-p, all-admissible-pair algebraic/Hecke theorem, not a proof of the unit's existence uniformly in p.** This is the first actual bridge in this phase between the quadratic Euler-factor norm calculations and the true conductor-dependent Mazur–Tate element. It was **numerically verified on real integer Manin modular symbols** at both p5 and p11, and the proof uses the exact Hecke distribution relation.

## 1. Setup

Let E/Q:y²+y=x³+x²−2x be the optimal rank-two curve 389a1, with positive Néron-normalized plus modular symbols m(a/n). We have

    m(0)=L(E,1)/Omega_E^+ = 0,

**exactly**, since L(E,1)=0 (rank two analytic certification). Fix a good prime p≥5, two distinct good p-admissible primes q1,q2 with

    q_i ≡1 (mod p),     a_(q_i)(E)≡q_i+1≡2 (mod p),

and, for simplicity of plus-pairing, q_i≡1 (mod 2p) (automatic for odd q_i≡1 modp).

Put n=q1q2 and let G=(Z/n)^×. Its p-power *quotient of exponent p* is C_p×C_p if the p-part of q_i−1 is exactly p; in general project to the canonical C_p quotient in each factor. Choose a primitive root g_i modq_i and the resulting character λ_i:G→Fp defined by λ_i(a)=log_(g_i)(a modq_i) modp.

Define the projected finite Mazur–Tate element in A=Fp[C_p×C_p]:

    theta_n(T1,T2)
      = Σ_(a ∈ (Z/n)^×) m(a/n)
          (1+T1)^λ1(a) (1+T2)^λ2(a).

Here A≈Fp[T1,T2]/(T1^p,T2^p). Its quadratic mixed coefficient is precisely Kurihara's number

    **δ_(q1q2) = [T1T2] theta_n modp.**

## 2. Actual Hecke distribution relation, not a formal variable substitution

For ℓ∤n (both prime to 389), the weight-two plus modular symbol Hecke relation is

    Σ_(b modℓ) m((a+b*n)/(nℓ))
      = a_ℓ(E)*m(a/n) − m(ℓ*a/n).

Among these ℓ terms exactly one has ℓ|(a+bn), and its modular symbol equals m(ℓ^-1*a/n) (the inverse interpreted modulo n, and rational cusps modulo 1).

Hence restricting to primitive a modnℓ and projecting the Mazur–Tate element to conductor n yields the **true exact group-ring norm relation**

    **proj_(nℓ→n) theta_(nℓ)
      = [a_ℓ(E) − σ_ℓ − σ_ℓ^-1]*theta_n.**

Any choice whether σ_a denotes a or a^-1 only interchanges σ_ℓ and its inverse, leaving the displayed symmetric multiplier unchanged.

At n=1 the right-hand theta equals m(0)=0. Consequently the augmentation of every single-prime theta_q vanishes EXACTLY:

    theta_q(0)=0.

Now take n=q1q2 and project the q1-variable to 1, i.e. T1=0. The norm relation gives

    theta_(q1q2)(0,T2)
      = (a_q1 − (1+T2)^e − (1+T2)^(-e))
        *theta_q2(T2)

where e=λ_q2(q1)∈Fp. Since a_q1≡2 modp, the factor is

    ≡ -e² T2² + O(T2³) modp.

The factor has zero constant and linear coefficient. Since theta_q2(0)=0, its product has **no constant, no linear and NO QUADRATIC term**.

Exchanging q1,q2 proves both pure quadratic coefficients vanish:

    [T1²]theta_n = 0 = [T2²]theta_n.

The constant and both linear coefficients vanish too. Thus the entire degree≤2 expansion is

    **theta_n(T1,T2) ≡ δ_(q1q2)*T1*T2 (mod total-degree≥3).**

This is a genuine equality for E389a1, for every good p and any admissible auxiliary pair: it does not suppose Sha finite or that δ is nonzero.

## 3. Diagonal specialization: a single ONE-VARIABLE quadratic coefficient

For any u,v∈Fp× let φ_(u,v):Fp[C_p×C_p]→Fp[C_p] be the genuine group algebra homomorphism

    σ1→γ^u,  σ2→γ^v, γ=1+T.

Equivalently substitute T1=(1+T)^u−1, T2=(1+T)^v−1.

Since T1≡uT (modT²) and T2≡vT (modT²), the pure quadratic vanishing gives the exact identity

    **[T²] φ_(u,v)(theta_(q1q2)) = u*v * δ_(q1q2) (modp).**

In particular for u=v=1:

    **δ_(q1q2) = [T²] Σ_(a modn)^× m(a/n)
              (1+T)^(λ1(a)+λ2(a)) modp.**

Therefore, for EVERY good p and every admissible pair, nonvanishing of the authentic two-prime Kurihara number is EQUIVALENT to nonvanishing of the QUADRATIC Taylor coefficient of a one-variable Mazur–Tate element over a cyclic order-p quotient of the cyclotomic field of conductor n, ramified at BOTH q1,q2.

This is a new **primewise diagonal rank-two criterion**: it reduces the *dimension of the analytic coefficient extraction* from two independent auxiliary variables to one, without altering the arithmetic nonvanishing question.

Under the Kim/Castella–Sano hypotheses (p≥5, residual surjective, Manin unit, p nonanomalous), the known minimal-degree criterion gives

    Sha(E/Q)[p]=0
      iff there exist q1,q2 with δ_(q1q2) !=0
      iff there exist q1,q2 and u,v units
          with [T²]φ_(u,v)(theta_(q1q2))!=0.

This is a **reformulation**, not a proof of existence for every p.

## 4. Fully genuine p11 and p5 Hecke norm validations

The original authenticated 390-term integer Manin vector independently reconstructs all modular symbols. We evaluated:

### p11, q1=397, q2=991

- primitive roots g397=5, g991=6;
- p-Sylow cross-logs e=log_991(397)=9, e'=log_397(991)=5.
- authentic single-prime theta_397 starts [0,0,9,5,5,9,6] mod11 in degrees0..6;
- authentic single-prime theta_991 starts [0,0,9,10,0,0,0] mod11.
- full q1q2 theta projected to T1=0 has coefficients [0,0,0,0,8,7,6].
- full theta projected to T2=0 has coefficients [0,0,0,0,6,1,7].
- BOTH projections match the exact a_q−σ_q−σ_q^-1 Hecke Euler factor multiplied by the respective authentic single-prime theta, coefficient by coefficient THROUGH DEGREE SIX.

The quadratic coefficient of the 2-variable theta matrix has

    M00=M10=M01=M20=M02=0; M11=1 mod11.

For the canonical diagonal φ_(1,1),

    **[T²]φ_(1,1)(theta_(397*991))=1 mod11.**

The pure degree4 projection checks match quadratic leading Euler units:
    -e²*[T²]theta_991 = -9²*9 = 8 mod11;
    -e'²*[T²]theta_397 = -5²*9 = 6 mod11.

### p5, q1=41, q2=61

The same fully enumerated 390-Manin modular symbol data gave

    M00=M10=M01=M20=M02=0; M11=4 mod5.

Both Hecke projections to θ41 and θ61 agree with their exact Euler multipliers through degree6. Thus

    **[T²]φ_(1,1)(theta_(41*61))=4 mod5**.

These checks are arithmetic evidence of the stated Hecke identity independent of the derivation; they do not extend a fixed pair to all p.

## 5. Strict boundaries for the BSD proof

- The diagonal subgroup/quotient is associated with a genuinely varying cyclotomic field Q(ζ_{q1q2}); it is NOT the fixed cyclotomic Z_p-extension of Q. Do not substitute its theta into the fixed-p cyclotomic Iwasawa main conjecture without a transfer theorem.
- The relation shows equality of two ANAYLTIC tests, not their unit nonvanishing at all p.
- The published prime-exchange rigidity of Castella–Sano does not reduce the auxiliary degree.
- The exact complex rank-two BSD leading coefficient is not identified by this finite-field calculation.

**Specific next target:** construct a p-independent integral Selmer/Bockstein or Artin formalism comparison controlling the quadratic coefficient of the cyclic order-p diagonal Mazur–Tate theta, instead of controlling every two-variable mixed coefficient separately. This is the first genuine conductor-dependent Euler-norm compatibility established in this phase, and it points to a strictly smaller analytic invariant, but a new global arithmetic comparison theorem remains necessary.
