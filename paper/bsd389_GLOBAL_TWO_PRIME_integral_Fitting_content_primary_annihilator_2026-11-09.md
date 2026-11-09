# BSD 389a1 — Exact two-prime integral Fitting comparison and a single-witness primary annihilator

**9 Nov 2026. Theorem from Kim (2025) + Castella–Sano (2026) and Cassels–Tate; NO prime-uniform nonzero integer annihilator or complex BSD proof.**

E: y²+y=x³+x²−2x, conductor 389, MW rank 2, torsion 0, Tamagawa product 1. For each **good** p>=5 with surjective residual image and p-unit Manin constant, put S_p=Sel_{p∞}(E/Q), X_p=S_p^∨ (finite-type Zp), and let M₂(p) be the minimum of the p-adic valuations of *nonzero* two-auxiliary Kurihara coefficients δ_{qr} in their actual rings Zp/I_{qr}. Set M₂(p)=∞ if **all** length-two coefficients vanish in their defined rings, and p^∞Zp=(0).

## EXACT arithmetic–analytic equality

    **Fitt_{2,Zp}(X_p) = p^{M₂(p)} Zp.**

Proof. Kummer duality gives an exact sequence 0→Sha(E)[p∞]^∨→X_p→Zp²→0. It splits because Zp² is projective, hence X_p≅Zp²⊕Sha[p∞]^∨ and Fitt₂(X_p)=Fitt₀(Sha[p∞]^∨). Castella–Sano Th. B proves M∞=v_p(Tam_E)=0 at every good ordinary p and good supersingular p when N is squarefree, assuming surjectivity and Manin-unit conditions. Kim Th. 1.1 identifies the Kurihara minimum length ρ with corank S_p and gives length(S_p/S_p,div)=M_ρ−M∞. Since MW rank=2, ρ≥2. If M₂=∞, then ρ>2, so rank(X_p)>2 and Fitt₂=0. If M₂=e<∞, then ρ=2 and Sha[p∞] is finite of order p^e, so Fitt₂=(p^e). QED.

**This is a genuinely sourced integral Fitting–Kurihara comparison, not a guessed cohomological injection from an arbitrary 390-symbol matrix.**

## NEW single-witness annihilator principle

Let n=qr be an eligible two-prime conductor with I_n divisible by p^h, and suppose a separately certified *integrally normalized* δ_n mod p^h is **nonzero** with p-adic valuation k<h. Then M₂≤k, whence Sha[p∞] is finite of order p^{e}, with even 0≤e≤k. The nondegenerate alternating Cassels–Tate pairing at odd p implies Sha[p∞]≅⊕(Z/p^{a_i})², so its exponent divides p^{e/2}. In particular

    **p^{⌊k/2⌋} Sha(E)[p∞] = 0.**

If k=0 **or k=1**, this gives Sha(E)[p∞]=0. An independently certified δ_n=p·unit (mod p²) would therefore suffice, even though δ_n=0 (mod p). This is a conditional statement about any such *real* high-precision witness; we have NOT claimed to have found one of valuation one.

## The global ideal, and the remaining nonvanishing gate

Define for all p, including 2,3,389, the intrinsic local ideal F_p=Fitt₂(X_p), then the integral ideal

    A_E := ⋂_{p prime} (F_p ∩ Z) ⊂ Z.

Elementary finitely generated Zp-module algebra gives

    A_E=(#Sha(E/Q)) if Sha(E/Q) is finite;
    A_E=(0)             if Sha(E/Q) is infinite.

Consequently A_E is a canonical p-independent integer ideal with **A_E≠0 iff Sha(E/Q) is finite**; any nonzero D∈A_E annihilates Sha. For all good p>=5, its local factors are **exactly computed in terms of the entire two-prime Kurihara family**, via the equality above. At p=2,3,389, separate comparisons are needed.

**Not yet achieved:** exhibit a single nonzero D∈A_E. Equivalently prove M₂(p)=0 for all p sufficiently large and control the finite exceptional prime groups. A fixed finite family of q,r or a fixed finite set of good local places cannot do this: for any fixed good ℓ, H¹_f(Q_ℓ,E[p])≅E(F_ℓ)/p=0 for all sufficiently large p≠ℓ.

## Executable certificate

Companion standalone standard-library Python script:
\`verification/bsd389_two_prime_Fitting_valuation_preflight_20261109.py\`.

It independently counts E(F_q), computes h=v_p(I_{qr}), validates admissibility, and **accepts externally certified** δ_n residue to return the mathematical p-exponent bound. It DOES NOT compute Kurihara sums or prove the published theorems. Regression inputs drawn from previously certified archival unit values:
- p17, (1667,5237), δ=4 mod17;
- p19, (2243,3877), δ=4 mod19;
- p23, (1289,3727), δ=17 mod23.

## Primary sources

Kim (with Pollack), The refined Tamagawa number conjectures for GL₂, arXiv:2505.09121, Th. 1.1: https://arxiv.org/pdf/2505.09121

Castella–Sano, On refined nonvanishing conjectures by Kurihara and Kolyvagin, arXiv:2601.14504, Th. B, §1.1.3: https://web.math.ucsb.edu/~castella/Kurihara.pdf

**OPEN:** construction of a nonzero GLOBAL annihilator, and exact complex rank-two BSD L''(E,1)/2=Ω Reg·#Sha.