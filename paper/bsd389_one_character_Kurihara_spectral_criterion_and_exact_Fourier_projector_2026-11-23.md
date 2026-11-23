# E389a1 — exact single twisted-L character criterion and Fourier spectral projector for two-factor Kurihara numbers at every p^k

**Date: 23 November 2026.** Proved integral finite cyclotomic-group-ring algebra and the authentic Hecke norm, with independent exact symbolic checks at m5 and m25. This is a genuine new FORMULATION of the primewise two-factor nonvanishing test. It does NOT prove its uniform nonvanishing, global Sha finiteness or full BSD.

## 1. True Mazur–Tate finite diagonal group-ring element

Fix p≥5, k≥1, m=p^k, and good auxiliary q1,q2 with q_i≡1,a_qi(E)≡2 modp^k. Choose primitive roots and discrete logs λ_i into Z/m; let n=q1q2 and

    Θ(T)=Σ_(a∈(Z/n)^×) m_E^+(a/n) (1+T)^(λ1(a)+λ2(a) mod m)
         ∈ Z[C_m] ≅ Z[T]/((1+T)^m−1),

with the actual Néron-integral plus modular symbols.

The genuine Hecke norm relation, together with m_E^+(0)=L(E,1)/Ω_E^+=0 EXACTLY, proves

    [T⁰]Θ ≡ [T¹]Θ ≡0 (modp^k),
    [T²]Θ ≡ δ_(q1q2) (modp^k).

See paper/bsd389_p2_deep_Hecke_diagonal_full_Kurihara_mod25_2026-11-23.md. In fact [T⁰]Θ=Θ(1)=0 **exactly** for such squarefree two-prime conductor (Hecke norm to level1), but the weaker modulo-p^k vanishing suffices.

Let ζ be a primitive mth root of unity, π=ζ−1, O=Z_p[ζ]. For the primitive even character χ_diag(a)=ζ^(λ1(a)+λ2(a)), write

    A(E,χ_diag)=Θ(π)=Σ m_E^+(a/n)χ_diag(a).

This is the actual primitive twisted modular-symbol value, not an imaginary auxiliary analytic object. Standard Birch–Stevens interpolation relates A(E,χ) to τ(χ)L(E,\barχ,1)/Ω_E^+ up to the fixed sign/integral normalization.

## 2. Exact ONE-character leading-term criterion (uniform-in-p statement)

**Theorem 1.** At any p≥5, k≥1, q1,q2 as above, with m=p^k and e=φ(m):

    **A(E,χ_diag)/π² mod π = δ_(q1q2) mod p,**

provided A/π² is interpreted in the valuation ring O. The latter is integral because the constant and linear coefficients of Θ are divisible by p^k and vπ(p^k)=k*e≥4, and all remaining terms have degree≥2.

**Proof.** Choose the canonical polynomial lift Θ(T) with powers (1+T)^j for 0≤j<m. Expand

    Θ(T)=a0+a1T+a2T²+T³G(T),
    a0,a1∈p^k Z, a2 ≡δ_n (modp^k), G(T)∈Z[T].

Since vπ(p^k)=ke≥4, dividing Θ(π) by π² yields an element of O and

    Θ(π)/π² = a2 + πG(π) + (a1/π)+(a0/π²).

The last two terms have positive π-valuation because ke≥4; hence reduction modulo π equals a2 modp equals δ_n modp.

In particular

    **δ_(q1q2) !=0 modp  iff  v_π(A(E,χ_diag))=2.**

When the two-factor coefficient has valuation≥1 modulo p, the valuation of a single twisted value can be controlled by higher Taylor coefficients, so there is NO similar simple equivalence for exact valuation1 at p² without isolating the quadratic coefficient by a projector.

The formula applies to any primitive diagonal character with unit weights u,v: the residue becomes uv δ_n, and exact vπ=2 is invariant under such choices.

## 3. Exact Fourier projector for the QUADRATIC coefficient at every precision

For m≥5, ζ_m a primitive mth root, let

    F(T)=Σ_(r=0)^(m−1) a_r (1+T)^r,    a_r∈Z,

and define character values F_t=F(ζ_m^t−1)=Σ_r a_r ζ_m^(tr), for 0≤t<m.

By Fourier inversion,

    [T²]F = (1/m) Σ_(t=0)^(m−1) F_t W_t,

with

    W_t=Σ_(r=0)^(m−1) binom(r,2) ζ_m^(−tr).

For t=0, W_0/m=(m−1)(m−2)/6.

For t≠0, put z=ζ_m^(−t), z^m=1,z≠1. Differentiating the finite geometric series exactly gives

    W_t/m = − (m−1)/(2(1−z)) − z/(1−z)².

Thus the **exact cyclotomic Fourier projector identity** in Q(ζ_m) is

    **[T²]F = ((m−1)(m−2)/6)*F_0
                −Σ_(t=1)^(m−1)
                    [ (m−1)/(2(1−ζ_m^(−t)))
                       +ζ_m^(−t)/(1−ζ_m^(−t))² ]*F_t.**

For our actual rank2 diagonal Mazur–Tate θ, F_0=0 exactly, so the first term vanishes. The remaining F_t are the **actual twisted modular-symbol algebraic critical values** for characters χ_diag^t, of order dividing m (and conductor q1q2 for t≠0).

This formula is not merely a heuristic connection to twisted L-values: it EXACTLY reconstructs the p^k-level Kurihara coefficient via its finite character specializations. The rational denominators and cancellations are handled by the equality in the cyclotomic field, whose sum is the integer [T²]F.

**Important limitation:** It may happen that every twisted central L-value F_t is NONZERO and yet the above weighted sum is 0 modulo p; nonvanishing of individuals does not preclude cancellation. A uniform proof needs a *noncancellation/unit* theorem for this exact spectral projector, not simply Rohrlich-type complex nonvanishing.

## 4. Actual user-certified p5, depth25 consequence

At q1=5351, q2=10651, p=5,k=2,m=25, user executed an exact 28,488,750 term modular-symbol sum with

    [T^0]Θ = [T^1]Θ = 0 (mod25),
    [T²]Θ = 22 (mod25).

Thus with ζ=ζ25, π=ζ−1 and e=20,

    **A(E,χ_diag)/π² ≡ 22 ≡2 (mod π),**
    **v_π(A(E,χ_diag))=2,    v_5(A)=1/10**.

For any unit weights u,v modulo25, the residue becomes 22uv≡2uv mod5; hence all **400 primitive even order25 characters** χ_(u,v) of conductor q1q2 have exact cyclotomic valuation2 and NONZERO central twisted L-values (by Birch–Stevens). There are 20 full character Galois orbits, each with algebraic norm 5-adic valuation exactly2. See paper/bsd389_depth25_400_twisted_L_spectral_valuations_2026-11-23.md.

## 5. Genuine next arithmetic theorem to seek

The p-uniform nonvanishing question now has a precise **single-character** formulation:

    For all sufficiently large good p,
      there exist two p-admissible primes q1,q2
      such that the primitive even order-p (or order-p²)
      twisted modular-symbol value A(E,χ_diag)
      has v_(ζ−1)(A)=2.

By Theorem 1, this is exactly the degree-two modp Kurihara unit criterion. It remains equivalent to Sha[p]=0 under Kim's hypotheses — **not an unconditional proof of existence**.

For the weaker p² valuation-one witness, use the EXACT Fourier projector on all m character values (or a genuine higher Bockstein); one single valuation does not suffice because cubic and higher Taylor terms may dominate. The precise obstruction is now explicit in cyclotomic algebra.

**Sources:** Birch–Stevens identity as quoted in https://link.springer.com/article/10.1007/s00222-017-0784-7 and published Kim / Castella–Sano. No unproved rank-two BSD hypothesis is used in the algebraic identities above.
