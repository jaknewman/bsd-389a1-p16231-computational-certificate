# BSD 389a1 — Non-circular relative Sha descent at p=5 and p=7; new conductor 32881

**Date: 13 November 2026.** Authentic new complete Mazur–Tate computation and exact group-ring Smith/Bezout proof at p=5, plus prior exact p=7 certificate. Proves a **relative** Sha-annihilation and base-field p-primary **finiteness** without invoking previously proved Sha(Q)[p∞]=0. **No all-prime Sha annihilator and no complex rank-two BSD identity.**

## 1. New arithmetic example at p=5

E: y²+y=x³+x²−2x, conductor 389. Take q=131,r=251, n=32881, traces a_q=2, a_r=22, point counts 130,230. Let K5'/Q be the totally real C5×C5 quotient of Q(ζ_n) obtained from the discrete logs modulo 5. With primitive roots g_q=2,g_r=6, the complete **canonical unregularized plus** Mazur–Tate θ∈Z[C5²], calculated independently via the exact 390 integral Manin plus symbols, has 25 coefficients C[i,j]:

    −100 −2 −228 −86 −58
    54 −2 186 −116 24
    54 24 −116 186 −2
    −100 −58 −86 −228 −2
    104 30 246 246 30

The exact six integer augmentation moments are (S0,SX,SY,SXX,SXY,SYY)=(0,1640,−30,2660,3556,−40), so

    **θ ≡ XY mod (5,I³).**

All six Galois character-line norms are nonzero, with exact norms and v5:

    (1,0) 36825610000 (4)
    (1,1) 8608128400 (2)
    (1,2) 2273382400 (2)
    (1,3) 5382400 (2)
    (1,4) 9200646400 (2)
    (0,1) 10000 (4).

The **independently calculated full integral Smith normal form** of [multiplication by θ | N_G], the 25×26 integer matrix, has p-adic valuation histogram {0:16,1:2,2:7}. This proves

    **(θ,N_G) ∩ Z5 = 25 Z5**,
    **Z5[G]/(θ,N_G) ≅ (Z/5)^2 ⊕ (Z/25)^7**.

Independent exact Bezout solutions and full 25-coordinate group-ring convolutions checked θ A_k + N_G =25 modulo 5^k for k=4,8,12.

The old p5 choice n=2501 had exact zero at two pure-character lines, so its ideal intersection was (0); the failure at n=2501 is **conductor-specific**, not a fundamental p5 obstruction.

## 2. Independent previous p=7 example

For K7/Q real C7×C7 conductor 76049=113×673, the prior **49 authentic integer coefficients**, complete resultant norms, 49×50 Smith classification (valuation histogram {0:36,1:6,2:7}) and Bezout yield

    **(θ7,N_G)∩Z7 =49 Z7**, θ7≡2XY mod (7,I³).

These old p7 computations were NOT re-executed wholesale in this new work; the complete archived p7 Bezout witness was independently rechecked by direct convolution in every one of the 49 coordinates.

## 3. New cohomological theorem avoiding Sha(Q)[p∞]=0 as an input

Let (p,K)=(5,K5') or (7,K7). Theorem 1.4(a),(b) of Bullach–Honnor, with the already verified Galois large-image condition and K real (so ζ_p∉K), gives:

1. θ∈I^{r_p+s_p+2c_p}, r_p=corank_Zp Sel_{p∞}(E/K). Since θ∈I² but θ∉I³, r_p≤2. The two certified rational generators give r_p≥2. Thus Sel corank exactly 2, rank E(K)=2, and **Sha(E/K)[p∞] is finite**.
2. Theorem 1.4(b) places θ^# in Fitt_0(Sel_{p∞}(E/K)^∨). For E semistable, θ and θ^# are unit associates, so θ annihilates Sha(E/K)[p∞].
3. Gal(Q(E[p])/Q)=GL₂(Fp) has no nontrivial quotient of p-power order; K/Q is a p-extension, so K∩Q(E[p])=Q and **E(K)[p]=0**. Since rank E(K)=rank E(Q)=2, the free G-module E(K)/tors is Z² with trivial G-action (rational points form a finite-index G-fixed sublattice). E(K)_tors has order prime to p. Therefore H¹(G,E(K))=0 (H¹ of a finite p-group on prime-to-p torsion and on trivial free Z² vanishes). Inflation–restriction now gives an **injective restriction**:

       **Sha(E/Q)[p∞] ↪ Sha(E/K)[p∞].**

   Hence **Sha(E/Q)[p∞] finite** for BOTH primes without using prior Sha(Q)[p∞] triviality certificates.
4. Because |G|=p², aug θ=0 and aug N_G=p², any equality p²=θ A+N_G B in R=Zp[G] has aug(B)=1; thus N_G B=N_G and **p²−N_G=θ A exactly**. On Sha(E/K), θ acts by 0, N_G=res∘cor. Consequently for every x∈Sha(E/K)[p∞],

       **p² x = res(cor x).**

   Therefore:

       **p²·ker(cor_{K/Q})=0**,
       **p²·(Sha(E/K)[p∞]/res Sha(E/Q)[p∞])=0**.

   In particular the relative exponent is at most 25 at p5 and at most 49 at p7. As a separate corollary, **IF** one also uses the already archived proofs Sha(E/Q)[5∞]=Sha(E/Q)[7∞]=0, then 25 Sha(E/K5')[5∞]=0 and 49 Sha(E/K7)[7∞]=0. The relative theorem and base-primary finiteness **do not use** that premise.

## 4. Sharp limitation of scalar norm descent

For any finite p-group G of cardinal p^d and θ∈I, augmentation shows **(θ,N_G)∩Zp ⊂ p^d Zp**. Therefore no scalar obtained from θ and norm can be a p-adic unit. On classes res(y) from the base, the relation p^d x=res cor x reads p^d res(y)=res(p^d y) and is a tautology. It provides **no bound at all** for the unknown order of Sha(E/Q)[p∞] and cannot imply a global p-independent integer annihilator. An all-prime family of such relative certificates would still need a **separate finite-prime-support theorem** to prove global Sha finiteness. The exact complex rank-two BSD leading term is also unresolved.

## 5. Executed, portable reproducibility

User-downloadable current-conversation ZIP **bsd389_non_circular_relative_Sha_p5_p7_new_conductor_20261113.zip**, SHA256 **49e18d3896f5587cbc56d437dfa692e76064579f334e221a5b4af193d5124f18**, includes:
- The exact source-normalized 390 Manin integer vector and standalone cusp evaluator.
- Full new 25 integer coefficients, six character norms, integral Smith and three 5-adic Bezout witnesses at p5; fully re-executable without Sage (Python + SymPy).
- Previously certified full 49 integer coefficients and frozen p7 Bezout witness, plus a new **independent 49-coordinate convolution check**.
- The detailed theorem proof, two complete execution logs and SHA256 manifest.

Primary mathematical source: Bullach–Honnor, *On the refined ‘Birch–Swinnerton-Dyer type’ conjectures of Mazur and Tate* (2026), Theorem 1.4, Remark 1.5(a), Definition 2.2, https://dominikbullach.github.io/MazurTate.pdf . Cohomological restriction/corestriction and inflation–restriction are standard.

**VERDICT:** An actual new p5 integral theta conductor removes the former p5 scalar obstruction, and an exact **NON-CIRCULAR relative Sha transfer theorem** now holds at p5 and p7. No global finiteness of Sha(E/Q) and no exact complex BSD formula are proved.
