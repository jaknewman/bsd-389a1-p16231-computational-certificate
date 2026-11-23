# BSD389 — exact 25-th cyclotomic character valuations and 20 algebraic twisted-L norms from the user-certified 28,488,750-term Kurihara computation

**Date: 23 November 2026.** Rigorous algebraic consequence of the genuine, independently USER-RERUN exhaustive p5, depth25 conductor n=5351*10651 computation; not a new p-uniform Sha proof.

## 1. Exact input and a new eigencharacter interpretation

Let E/Q:y²+y=x³+x²−2x and n=5351*10651. Denote by m_E^+(a/n) the authentic **integer** Néron-normalized plus modular symbol encoded by the user's separately checked 390-Manin vector.

For i=1,2 choose the primitive roots g1=11 mod5351 and g2=7 mod10651, and let

    λ_i(a)=log_(g_i)(a mod q_i) mod25 ∈ Z/25.

Because q1−1=5350 and q2−1=10650 are divisible by 50, λ_i(−1)=0 modulo25. Let ζ=ζ_25 be any primitive twenty-fifth root of unity and put O=Z_5[ζ], π=ζ−1. The extension Q_5(ζ)/Q_5 is totally ramified with ramification index e=φ(25)=20, so

    (5)=(π)^20 * (p-adic unit),     v_π(5)=20.

For every pair of **unit residues** (u,v)∈(Z/25)^××(Z/25)^×, define the even primitive Dirichlet character of conductor n

    χ_(u,v)(a) = ζ^(u λ1(a)+v λ2(a)).

It is primitive at BOTH q1 and q2, of exact order25 and conductor n (since u,v are units). There are 20*20=**400** such characters.

Their genuine algebraic twisted modular-symbol values are

    A(E,χ_(u,v)) := Σ_(a∈(Z/n)^×) m_E^+(a/n) χ_(u,v)(a) ∈ Z[ζ].

By the Birch–Stevens formula for primitive **even** characters, A(E,χ) differs from the algebraic critical twisted value L(E,\barχ,1)/Ω_E^+ by the nonzero Gauss factor τ(χ), with a possible conventional sign or power of 2 that is a p-adic unit for p5. The precise convention can be pinned from the user's eclib symbol normalization; in every convention with this standard interpolation **A≠0 forces L(E,\barχ,1)≠0**.

Primary modular-symbol interpolation references:
- https://link.springer.com/article/10.1007/s00222-017-0784-7 (Birch–Stevens identity).
- https://math.mit.edu/~drew/2018Conference/SlidesRubin.pdf (explicit normalized elliptic curve plus-symbol twisted-L formula).

Gauss factor τ(χ) is a p-adic **unit** because χ is primitive at conductor n prime to p and
τ(χ)τ(\barχ)=χ(−1)n=n, and both Gauss sums are algebraic integers. The factor n is a p-adic unit. Thus the exact 5-adic valuation of A transfers to the period-normalized twisted L-value under this formula.

## 2. NEW GENERAL SPECTRAL LEMMA, all p≥5 and k≥1

Let p≥5, k≥1, R=Z/p^k, ζ a primitive p^k-th root, O=Z_p[ζ], and π=ζ−1, with
    e=φ(p^k)=p^(k−1)(p−1),    v_π(p)=e.

Let F(T) be an integral polynomial/group-ring element evaluated at T=π; assume its coefficients satisfy

    [T^0]F ≡ [T^1]F ≡0 (mod p^k)
    and  [T²]F ≠0 (mod p).

Then

    **v_π(F(π))=2** and v_p(F(π))=2/e.

**Proof.** Write F(T)=p^k a0 +p^k a1*T+c2*T²+T³G(T), where c2 is a p-adic unit, a0,a1∈Z_p and G∈Z_p[T]. Then the valuations of the four terms are respectively at least ke, ke+1, exactly2, and at least3. Since ke≥p−1≥4>2, the T² term has strictly minimal valuation. The ultrametric inequality gives vπ(F(π))=2. This is an algebraic theorem; it does NOT require a p-adic Iwasawa main conjecture.

## 3. Application to the FULL user rerun at conductor 56,993,501

The actual printed, USER-confirmed p5 modulo25 bivariate theta matrix (coefficients 0≤i,j≤2) was

    M = [ [0,0,0],
          [0,22,16],
          [0,17,14] ]  (mod25).

The exact Hecke norm identity proves the pure coefficients
    M00=M10=M01=M20=M02=0 mod25.

For arbitrary units u,v, the genuine cyclic diagonal group-ring map γ1→γ^u, γ2→γ^v gives

    F_(u,v)(T)= φ_(u,v)(Theta_n)(T),

and the general proven p^k diagonal theorem implies

    [T⁰]F_(u,v)=[T¹]F_(u,v)=0 (mod25),
    **[T²]F_(u,v)=22*u*v (mod25).**

Because 22≡2 mod5 and u,v are units, every one of these 400 quadratic coefficients is a 5-adic unit. The spectral lemma therefore gives an EXACT result simultaneously for all 400 primitive even characters:

    **v_(ζ25−1)( A(E,χ_(u,v)) ) = 2.**
    **v_5(A(E,χ_(u,v))) = 2/20 = 1/10.**
    **A(E,χ_(u,v)) != 0, hence L(E,\barχ_(u,v),1) != 0.**

Since τ(χ) is a p-adic unit and (up to conventional p-unit normalizations) A(E,χ)=τ(χ)*L(E,\barχ,1)/Ω_E^+, the period-normalized algebraic twisted central value also has 5-adic valuation 1/10.

**No new twist L-values were directly numerically evaluated.** These exact nonvanishing and valuation statements are algebraic consequences of the independently user-reproduced original 28,488,750-term computation.

## 4. The 20 full Galois orbits have exact 5-adic norm valuation 2

The Galois group Gal(Q(ζ25)/Q)=(Z/25)^× acts by scaling both (u,v) by the same t. Thus the 400 primitive characters split into **20 Galois orbits**, indexed by the unit ratio v/u mod25.

For each orbit the algebraic integer A(E,χ)∈Z[ζ25] has *local* cyclotomic valuation exactly2. Therefore its ordinary algebraic field norm is an INTEGER with

    **v_5(N_(Q(ζ25)/Q)(A(E,χ))) = 2.**

This follows from the unique totally ramified prime of Q(ζ25) above 5 (the norm of the uniformizer ideal is (5)). It is a new exact, finite, highly structured family of twenty 5-adic valuations deduced from the complete modular-symbol calculation. It is not a single integer annihilating Sha, and all data remain at fixed p5.

## 5. Meaning for the BSD program

The genuine diagonal theta coefficient can now be rephrased in a MORE ARITHMETICALLY TESTABLE way: at a primitive order-p^k character of a cyclic quotient ramified at **two** auxiliary primes, the theta eigenvalue has exactly two cyclotomic zeros, and its leading normalized value is a p-unit.

This is useful because it admits comparison to **actual twisted complex critical L-values** by Birch–Stevens. However, even simultaneous nonvanishing for 400 conductor-varying twists at p=5 does not imply a two-prime unit at all sufficiently large p or a uniform Fitt2/Sha annihilator. The twist characters vary with p and the field; a uniform arithmetic transfer remains to be proved.

Reproducibility:
  verification/bsd389_p5_depth25_twist_spectral_valuation_gate.py
  results/bsd389_p5_depth25_diagonal_USER_UBUNTU_PASS_2026-11-23.md

**Strict boundary:** no new uniform Sha finiteness or exact complex rank-two BSD identity is claimed.
