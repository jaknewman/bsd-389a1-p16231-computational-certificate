# Deep Chebotarev–Kummer selectors for the full p-Selmer group: exact density p^{-(2k+s-1)}

**23 November 2026. Status: new unconditional arithmetic theorem at every p≥5 for which the elliptic p-adic Galois image is full; hence for ALL sufficiently large p on non-CM E=389a1.** This strengthens the prior deep-auxiliary-prime theorem by *simultaneously* imposing an arbitrary independent set of mod-p Selmer localizations. It is not a theorem of Kurihara nonvanishing or Sha finiteness.

## 1. Statement, with correct Galois hypotheses

Let E/Q: y²+y=x³+x²−2x, with E(Q)=ZP+ZQ, rank2 and torsion0. Fix p≥5 such that

    Gal(Q(E[p^k])/Q) = GL2(Z/p^k)   for every k≥1.

For E=389a1 this holds for all sufficiently large p by its nonintegral j=112³/389, Serre's open image theorem and Serre's p-adic lifting lemma (mod-p surjective iff p-adic image full for p≥5). We do NOT assert an effective Serre cutoff.

Let S_p=Sel(Q,E[p]) and s=dim_Fp S_p. This s is finite even without any hypothesis on global Sha finiteness. Choose **any Fp-basis** c1,...,cs of S_p (in particular, begin with the Kummer classes of the saturated rational generators P,Q). For any fixed depth k≥1 and any index i∈{1,...,s}, there is a Chebotarev set of good primes q of exact natural density

    **dens(Q_{p,k,i}) = 1 / p^(2k+s−1)**

such that:
- q≡1 (mod p^k), a_q(E)≡2 (mod p^k);
- dim_Fp E(F_q)/pE(F_q) = 1;
- in the 1-dimensional finite local Kummer quotient, loc_q(c_i)≠0 and loc_q(c_j)=0 for all j≠i.

Consequently, for every p of full p-adic image and every k one can pick s pairwise distinct good auxiliary primes q1,...,qs whose localizations give a *diagonal isomorphism*

    Sel(Q,E[p]) → ⊕_{j=1}^s E(Q_{q_j})/p E(Q_{q_j}).

In particular, the first TWO distinct primes may be chosen with depth k and mod-p MW localization rows [1,0] and [0,1], even when Sha(E/Q)[p] is nonzero; their density is at least 1/p^(2k+s−1). **Without imposing zeros for the unknown Sha classes** and working with the two-dimensional Kummer subspace alone, the stronger density

    **1 / p^(2k+1)**

holds separately for the MW-axis selectors, independent of s. At k=2 this is 1/p^5.

## 2. Why mod-p Selmer classes remain independent over EVERY division field Q(E[p^k])

Let V=E[p]≈Fp² and K_k=Q(E[p^k]). Let G_k=Gal(K_k/Q)=GL2(Z/p^k). By Sah's lemma,

    H¹(G_k,V)=0.

For a direct elementary proof: the scalar z=2I is central in G_k, and acts as multiplication by 2 on V. For any cocycle f, comparing f(zg) with f(gz) yields

    (2−1)f(g)=(g−1)f(z).

As 2−1=1 is invertible, f is a coboundary.

Inflation–restriction therefore makes

    H¹(Q,V) → H¹(K_k,V)

INJECTIVE. In particular, restrictions of the independent c1,...,cs are linearly independent.

Since G_{K_k} acts trivially on V, these restricted cocycles are honest continuous homomorphisms, hence together give

    f=(c1,...,cs):Gal(Qbar/K_k) → V^s.

Let H be the image. It is G_k-stable under diagonal conjugation via GL2(Fp). The standard GL2(Fp)-module V is absolutely irreducible and End_{GL2(Fp)}(V)=Fp.

If H were a proper submodule of V^s, semisimplicity of the **specific module V^s** (it is a direct sum of simple copies of V, despite the group having p-torsion) would yield a nonzero GL2(Fp)-equivariant quotient map V^s→V that vanishes on H. Every such map is a nontrivial Fp-linear combination of the s coordinate projections. Consequently a nonzero linear combination of the restricted c_i would vanish, contradicting the H¹ restriction injectivity.

Thus H=V^s. In particular, the compositum of the p-division fields of c1,...,cs and K_k is a Galois extension L/Q fitting into

    1 → V^s → Gal(L/Q) → GL2(Z/p^k) → 1.

**No splitting of this extension is assumed or needed.** Crucially, this argument works even if s>2 (i.e. even if there are unknown Sha[p] classes). That is why the theorem is not circular.

## 3. Exact Frobenius and local-selector density

Fix U=[[1,1],[0,1]] in G_k. Direct matrix multiplication shows

    Cent_{G_k}(U) =
       { [[a,b],[0,a]] : a∈(Z/p^k)^×, b∈Z/p^k }.

Hence |Cent(U)|=p^(2k−1)(p−1), and its complete conjugacy class has Chebotarev density 1/[p^(2k−1)(p−1)].

For a good prime q with mod-p^k Frobenius A conjugate to U, the determinant and trace give

    q≡det A≡1 (mod p^k),
    a_q(E)≡tr A≡2 (mod p^k).

Modulo p, A is nonidentity unipotent, so

    W_A := V/(A−1)V

has dimension one; indeed the finite local Kummer quotient is canonically identified with H¹_unr(Q_q,V)≈W_A.

Choose any one lift in Gal(L/Q) above A. All lifts form a coset of the kernel V^s. Addition by any h=(v1,...,vs)∈V^s shifts the Frobenius cocycle value by h. The quotient V→W_A is surjective with p-element fibers. Thus the s localizations are independently and uniformly distributed in W_A^s over this exact fiber; each prescribed vector pattern has p^s preimages.

Exactly (p−1) patterns have coordinate i NONZERO and all other coordinates ZERO. Therefore the conditional probability in the fiber is

    (p−1) / p^s.

Multiplication with the density of the conjugacy class yields the exact natural density

    1/[p^(2k−1)(p−1)] · (p−1)/p^s
    = **1/p^(2k+s−1)**.

The property is conjugacy-invariant: changes of local quotient basis only scale the 1-dimensional quotient and preserve zero/nonzero. Thus Chebotarev gives the exact natural density, not just positive upper/lower density.

For the 2-dimensional Kummer span generated by P,Q, repeat the argument with s=2 even if the full Selmer group has dimension >2. The resulting two MW-axis conditions have density 1/p^(2k+1).

**Exact numeric examples (k=2, s=2):**
- p=5: density 1/3125.
- p=11: density 1/161051.
- p=107: density 1/107^5 (the theorem is conditional on full p-adic image, which is independently established for this curve).

## 4. Strongest logically valid consequence and the one remaining gap

This theorem solves **all purely local existence requirements simultaneously** for arbitrarily deep p^k Kurihara auxiliaries, even for any hypothetical excess Sha[p] Selmer dimension s. At any k one has s distinct local detectors making the full Selmer localization matrix invertible.

The theorem **DOES NOT** imply s=2. Indeed if Sha[p] has dimension t>0, then s=2+t and the theorem faithfully constructs **2+t** independent local detectors, not a contradiction.

Nor does it imply a nonzero TWO-prime Kurihara derivative:

    \tildeδ_{q1q2} mod p or mod p².

Chebotarev makes the local conditions independent over the finite Galois extension, but the modular-symbol weighted sum defining δ is an additional **global Kato/Euler-system quantity**. There is no reason its values are uniformly distributed in Fp or Z/p² solely from Chebotarev; asserting that would tacitly assume the desired Sha vanishing.

The unconditional result of Castella–Sano gives existence of a primitive Kurihara coefficient at *some auxiliary degree* (under the published hypotheses), while Kim measures the minimal such degree by s. What remains to be proved for all large p is **that this minimum s equals 2**, equivalently that a two-factor coefficient is nonzero at p (or, more weakly, at p² with valuation at most one and Cassels–Tate parity).

Thus the arithmetic obstruction has been narrowed: not existence of high-depth q, not full Selmer local detection, and not p-adic surjectivity at large p, but the **rank-two integral global reciprocity / derived Kato nonvanishing**.

## 5. Reproducibility and theorem provenance

The companion standard-library program verifies exact group-class sizes, uniform local-quotient fiber counts and density formula at p=3,5,7, k=1,2 and s=2,3. These are finite checks of group arithmetic only; Sah's lemma, Serre and Chebotarev remain the external published theorems.

Literature:
- Serre's open image theorem and p-adic lifting: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html
- Sah's central-element lemma (standard group cohomology; elementary proof in §2).
- Chebotarev's density theorem.
- The prior Selmer-only density proof: paper/bsd389_full_selmer_quantitative_chebotarev_strict_isolation_2026-11-16.md.
- The previous deep unipotent theorem: paper/bsd389_global_deep_auxiliary_chebotarev_theorem_2026-11-23.md.

**Proof status: theorem established. Full Sha finiteness and complex BSD remain unproved.**
