# E389a1 — a genuine upper bound for Sha[p] via a degree-(p²−1) character field

**2026-11-14. Mathematical status:** original fixed-prime cohomological consequence plus an unconditional explicit O(p²) upper bound on the dimension of Sha[p] under specified hypotheses. **Not** the decisive all-large-p triviality or the exact complex BSD equality. The ordinary class group of the character field has NOT been computed.

## 1. The true smaller field and the dual-isogeny character

For E/Q: y²+y=x³+x²−2x with N=389, rank 2, sign +1, fix p≥5, p not 97 or 389, with full residual GL2(Fp) and good nonanomalous reduction p∤#E(Fp).

Set F=Q(E[p]), G=GL2(Fp), V=E[p]. For a line C⊂V, B=Stab_G(C), K=F^B, W=V/C and χ:B→Fp× the quotient (DUAL isogeny kernel) character. Let L=F^(ker χ), Δ=Gal(L/K)≅Fp×. Degrees:
  
  [K:Q]=p+1,  [L:Q]=n=p²−1,  [F:Q]=p(p−1)²(p+1).

L is not generally Galois over Q. The genuine p5 sextic K, 5-isogeny and dual kernel were constructed in the earlier PR #29.

## 2. THEOREM A — strict Selmer injects into the p-class group of L

Define S_p^0=ker(Sel_p(E/Q)→E(Q_p)/p) and d_p=dim_Fp Sha(E/Q)[p]. Good nonanomalous reduction implies the local p-Kummer space is a line, so the rational MW rank2 and Kummer exact sequence give

  dim_Fp S_p^0 ≥ 1+d_p.

**Claim (actual cohomological injection):**

  S_p^0 ↪ Hom_Δ(Cl(L)/p Cl(L), W).

**Proof.** PR #29 proves that restriction followed by E[p]↠W induces an INJECTION H¹(Q,E[p])→H¹(K,W), under full residual GL2, by Sah's lemma and irreducibility. Restriction from K to L remains injective, because [L:K]=p−1 is prime to p. Over L, the W-action is trivial, and the image is a Δ-equivariant homomorphism of Galois groups into W.

Every rational strict Selmer class is unramified at good primes ℓ≠p; it is ZERO locally at p by definition; and it is automatically zero locally at 389 because split type I1 gives #E(Q389)[p]=0 for p∉{97,389} and Tate local duality gives H¹(Q389,E[p])=0. Thus it becomes everywhere unramified on L. Global Artin reciprocity makes it a Δ-equivariant homomorphism Cl(L)/p→W. QED.

Put r_chi,p=dim_Fp Hom_Δ(Cl(L)/p,W). Since Δ has order p−1 prime to p, this is the χ-isotypic multiplicity of the ordinary p-class group. Therefore

  d_p ≤ r_chi,p−1 ≤ v_p(h(L))−1.

By the proved p-parity theorem and global root sign +1, d_p is EVEN even if global Sha finiteness is unknown. Hence

  **d_p ≤ 2 floor((r_chi,p−1)/2) ≤ 2 floor((v_p h(L)−1)/2).**

In particular

  **v_p(h(L))≤2 ⇒ Sha(E/Q)[p^∞]=0.**
  **Sha(E/Q)[p]≠0 ⇒ r_chi,p≥3 and p³ divides h(L).**

This is a TRUE upper bound based on a field of degree p²−1 rather than the full p-division degree ~p⁴. It is sufficient, not necessary; class groups may contain unrelated p-primary factors. The new bound concerns **Sha[p] dimension**, NOT the exponent/order of a possibly infinite Sha[p∞].

## 3. THEOREM B — an explicit all-eligible-p polynomial upper bound

L/Q is unramified outside {p,389}. At 389, E is split multiplicative type I1, with tame inertia image of order p (p≠389). Consequently v_389(D_L)≤n.

At rational p, every local ramification index e≤n=p²−1<p² satisfies v_p(e)≤1. The classical local different inequality (Serre, Local Fields III §6, remark after Proposition 13)

  d_local ≤ e−1+e·v_p(e) < 2e

therefore gives v_p(D_L)≤2n after summing residue-degree weighted local exponents. Thus

  **|D_L| ≤ (389 p²)^n.**

Minkowski guarantees an integral ideal representing each class with norm at most

  M_L=(4/π)^r2 (n!/n^n) √|D_L| < (2√389·p)^n.

Let B=p^(a n)≥M_L and H_B=Σ_{j≤B}1/j. The Dedekind-zeta Euler coefficients satisfy a_L(m)≤d_n(m), and the n-fold divisor-function tuple count proves

  h(L)≤Σ_{m≤B}a_L(m)≤B H_B^(n−1),  H_B≤1+ln B.

Pick explicit a,b with M_L<p^(a n) and H_B<p^b:
- p=5: (a,b)=(4,4). Hence h(L)<p^(8n−4).
- 7≤p<41: (a,b)=(3,3). Since ln p≤p/3 for p≥7, H_B≤1+3n ln p≤p³−p+1<p³. Hence h(L)<p^(6n−3).
- p≥41: (a,b)=(2,3). Since 2√389<41, M_L<p^(2n); H_B<p³. Hence h(L)<p^(5n−3).

Combining d_p≤v_p h(L)−1 with even parity yields the ACTUAL completely explicit upper bound

  **dim_Fp Sha(E/Q)[p] ≤ 186** for p=5;
  **dim_Fp Sha(E/Q)[p] ≤ 6(p²−1)−6** for 7≤p<41;
  **dim_Fp Sha(E/Q)[p] ≤ 5(p²−1)−6** for p≥41.

Every clause assumes p is good, nonanomalous and residual GL2, with p≠97,389. This is an O(p²) **upper** bound for the p-torsion rank, not the decisive constant zero bound. It is deliberately very loose: at p599 the bound is 1,793,994; at p16231 it is 1,317,226,794.

Standalone assistant Python /mnt/data/bsd389_classgroup_smallfield_upper_bound.py (SHA256 cc7dc986e74ccdfaf27bd79d6c266ee137298e5d18f091ba1af112845662154c) executed all sample inequality checks; it does NOT compute class groups.

## 4. A concrete p5 class-group script (not yet executed in Sage)

A separate script constructs K5=Q[t]/(389(t²+10t+5)³−1404928t), the previously authenticated cyclic degree-5 isogeny over K5, and its **DUAL** kernel polynomial. The x-coordinate extension of a nonzero dual-torsion point has degree2 over K5, and the y-coordinate adds a further quadratic, defining the ACTUAL character field L5 of degree24. Optional Sage --classgroup requests an exact proven class group and v5(h(L5)). The source was Python-syntax-checked locally, but the assistant runtime does not have Sage or Pari. No p5 class number result is claimed.

**Real missing all-large-p input:** Prove independently that r_chi,p≤2 (or v_p h(L_p)≤2) for all sufficiently large good nonanomalous p, and separately handle potentially infinite anomalous primes. Neither this O(p²) bound nor published Garnek/Dainobu *lower* class number theorems supply it. Even all-p Sha finiteness would leave the exact rank-two archimedean BSD leading term unproved.

**Literature:** Serre Local Fields III §6; W. Stein Algebraic Number Theory Chapter 7 (Minkowski), https://wstein.org/books/ant/ant/ch_classgroup.html ; Dainobu 2024 https://www.sciencedirect.com/science/article/pii/S0022314X24001434 ; Garnek 2019 https://www.numdam.org/item/JTNB_2019__31_1_227_0/ ; Sage isogenies https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_curve_isogeny.html .
