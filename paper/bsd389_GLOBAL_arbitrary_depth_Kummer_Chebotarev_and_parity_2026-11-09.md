# BSD 389a1 — Arbitrary-depth Kummer–Chebotarev and the parity-reduced Kurihara gate (9 Nov 2026)

**Rigorous new arithmetic deduction. NOT a proof of prime-uniform Sha finiteness/vanishing or exact complex BSD.**

E: y²+y=x³+x²−2x; conductor 389; saturated MW basis P=(-1,1), Q=(0,-1), rank 2. For all primes p≥5, residual rho_{E,p} is GL₂(Fp) (Mazur semistable theorem at p≥11; archived p5/p7 checks); Serre's p-adic lifting lemma makes rho_{E,p^m}=GL₂(Z/p^m) for all m≥1.

## Theorem 1 — full Kummer image at *every* p^m

Put L_m=Q(E[p^m]), M_m=L_m(p^{-m}P,p^{-m}Q). Then

    Gal(M_m/L_m) ≅ E[p^m]^2 ≅ (Z/p^m)^4

for every p≥5, every m≥1, including p=389 as a Kummer/auxiliary-prime statement.

**Proof.** At m=1, Sah's lemma H¹(GL₂(Fp),E[p])=0 via central -I, and saturation of P,Q, prove Gal(M_1/L_1)=V² by the semisimple-isotypic submodule argument. For m>1 let C=M_1∩L_m. The abelian Fp-group H=Gal(C/L_1) is a quotient of V², so -I acts as -1 on H. But H is also a quotient of Gal(L_m/L_1), and central -I in GL₂(Z/p^m) acts trivially there. The actions coincide because lifts differ by an element of the abelian group H. Thus H=0 and C=L_1. Consequently reduction modulo p of Gal(M_m/L_m)⊂E[p^m]² surjects onto Gal(M_1L_m/L_m)=V². Nakayama's lemma for the free module (Z/p^m)^4 forces the image to be all of E[p^m]². QED.

## Theorem 2 — depth-p^m Chebotarev prime supply and *exact density*

Fix the primitive transvection g=[[1,1],[0,1]]∈GL₂(Z/p^m), and require Frob_q to lie in its conjugacy class. Then q≡1 mod p^m and a_q(E)≡2 mod p^m, hence q is Kurihara-admissible to depth p^m. The finite-field Kummer quotient E(F_q)/p^m≈Z/p^m is cyclic.

Each of the two prescribed rational-point local patterns

    (P,Q)=(unit,0) mod p^m,    (P,Q)=(0,unit) mod p^m

is attained by infinitely many good primes, of **exact Dirichlet density p^(−3m)**. One q of each pattern gives an invertible rank-two 2×2 Kummer matrix over Z/p^m.

**Density proof:** G=GL₂(Z/p^m) has order |GL₂(Fp)|p^{4(m−1)}; g has centralizer order φ(p^m)p^m and conjugacy class |G|/[φ(p^m)p^m]. Each quotient class has p^m translation lifts in E[p^m]. For (unit,0), the translation count is φ(p^m)p^{2m}. Divide the product by |Gal(M_m/Q)|=|G|p^{4m}, obtaining p^(−3m). Conditions are conjugacy invariant. The simpler transvection-class density (without imposed Kummer pattern) is 1/[p^m φ(p^m)].

## Theorem 3 — parity-reduced sufficient criterion for Sha_p=0

For good p≥5 with large image and p-unit Manin constant, combine Kim Theorem 1.1 and Castella–Sano Theorem B (Tamagawa product 1). Let M₂(p) be the minimum p-adic valuation across all *genuinely nonzero, integrally normalized* two-prime Kurihara numbers in their own Zp/I_n. Then

    M₂(p)<∞ ↔ Sha(E)[p∞] is finite,
    and then M₂(p)=v_p(#Sha(E)[p∞]).

By the perfect alternating Cassels–Tate pairing for *finite* odd-primary Sha, M₂(p) is even:

    **M₂(p)∈{0,2,4,...}∪{∞}.**

Thus ONE genuinely nonzero δ_(q·r) modulo p², at *p²-admissible* q,r, guarantees M₂≤1 and hence M₂=0; therefore Sha(E)[p∞]=0 and, in fact, SOME (possibly other) two-prime delta is a mod-p unit. This is weaker than directly demanding δ mod p nonzero.

Our independently reproduced authentic p5 depth-two example δ_(5351·13001)=15 mod 25 proves the criterion is nonvacuous; Sha[5∞] was already certified independently.

**Not proved:** for every sufficiently large good p there exists a depth-p² admissible pair with nonzero TWO-factor δ mod p². Theorems 1–2 construct all the needed local profiles but do not imply a nonzero *global Kato derivative*. No p-independent nonzero Sha annihilator or complex rank-two BSD equality is asserted.

## Independent executable finite-group audit

Current conversation archive includes pure standard-library Python verifier "bsd389_full_padic_Kummer_Chebotarev_density_20261109.py". It checked conjugacy class sizes, p^(−3m) density in 10 p/m cases including (5,3),(7,2),(11,2),(389,2), and **brute-force checked all matrices** in GL₂(Z/5), GL₂(Z/25), GL₂(Z/7). PASS throughout. These finite group checks do NOT compute global Selmer, Kato, or Kurihara.

Primary references: Kim https://arxiv.org/pdf/2505.09121; Castella–Sano https://arxiv.org/pdf/2601.14504; Serre lifting p≥5 https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html; Mazur semistable surjectivity via Stein-Wuthrich https://www.wstein.org/papers/bsdalg/bsdalg2.pdf.
