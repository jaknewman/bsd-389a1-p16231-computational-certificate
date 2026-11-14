# 389a1: exact supersingular character-field discriminants and local log saturation at p599, p16231

**14 Nov 2026.** Rigorous geometric/arithmetic consequences of residual GL2, Serre's local supersingular inertia theorem, Tate curves, and genuine independent p-adic group computations. A new O(4p²) upper replaces the earlier O(5p²) bound for supersingular p≥83. **No unknown Sha component is proven zero, no uniform finite-support statement or complex BSD proved.**

## A. Definitions and authentic finite Galois representation

For E:y²+y=x³+x²−2x, N=Δ=389, let p≥5 be a good prime with rho(E[p])=GL2(Fp). Choose a line C in E[p], its Borel B, and quotient-character chi:B→Fp× on W=E[p]/C. Define F=Q(E[p]) and L=F^(ker chi). Then [L:Q]=n=p²−1. As an actual GL2-set, the n embeddings of L correspond to all nonzero covectors of V=E[p] (dual V^∨ minus 0).

Primary sources:
- Serre, Galois properties of points of finite order, translated, Proposition 13 (supersingular inertia), Proposition 14 (Tate multiplicative reduction): https://static1.squarespace.com/static/57bf2a6de3df281593b7f57d/t/600db4f1676f6519410f71e9/1611511026377/serre_1972_translation.pdf
- LMFDB 389a1 (N,Δ, split I1, MW rank2, Galois representations): https://www.lmfdb.org/EllipticCurve/Q/389a1/
- Minkowski class-number bound: https://wstein.org/books/ant/ant/ch_classgroup.html

## B. EXACT decomposition and discriminant exponent at bad 389, for all p≠97,389

Since v389(Δ)=1, the Tate inertia image is the full order-p unipotent U=[[1,1],[0,1]]; its arithmetic Frobenius quotient acts as diag(389 modp,1). For p not 97,389, put m=ord_{Fp×}(389 modp)>1. Under the contragredient action on nonzero covectors, U fixes p−1 covectors (with first coordinate 0) and has p−1 additional length-p orbits. Frobenius fixes the p−1 invariant covectors separately; it permutes the other p−1 inertia orbits in cycles of length m.

Therefore 389 factors in L EXACTLY as:
- p−1 distinct degree-one UNRAMIFIED primes with (e,f)=(1,1);
- (p−1)/m distinct primes with (e,f)=(p,m).

The degree sum is (p−1)+p·m·(p−1)/m=p²−1. Since inertia is tame at 389, the discriminant exponent is n−number-of-inertia-orbits:

  **v389(D_L)=n−2(p−1)=(p−1)².**

p599: m=299; 598 degree-one primes and two primes e599 f299, exponent 357604.
p16231: m=16230; 16230 degree-one primes and one prime e16231 f16230, exponent 263412900.

This result uses the exact true p-division Galois action, not a made-up polynomial or field discriminant.

## C. EXACT signed discriminant and signature at supersingular p

For every good supersingular p≥5 with full residual GL2, Serre Proposition 13 gives inertia I_p image equal to the **entire nonsplit Cartan F_(p²)^×** of order n. It acts regularly on the nonzero covectors, so L/Q has ONE prime above p, totally and tamely ramified with e=n, f=1. Hence v_p(D_L)=n−1=p²−2.

The division field F and L ramify only at p and389, so

  **|D_L|=p^(p²−2) 389^((p−1)²).**

Complex conjugation on E[p] has eigenvalues +1 and −1, hence fixes p−1 nonzero covectors. Thus L has r1=p−1 real embeddings and r2=p(p−1)/2 complex pairs, so signed discriminant is (−1)^r2 times |D_L|.

Actual p599: **Disc(L599)=−599^358799·389^357604, degree 358800, signature(598,179101)**.
Actual p107: **Disc(L107)=−107^11447·389^11236, degree11448, signature(106,5671)**.

Moreover (p)=P^n with n=p²−1 coprime to p, so the class of the unique P above p is killed by n and is ZERO in Cl(L)/p. For p-strict Kummer class-field computations, splitting conditions above p impose no extra p-class restriction in the supersingular case; unknown primes above 389 can still contribute.

## D. Improved TRUE unconditional upper on Sha[p] at supersingular p≥83

Under the separately proven true class-field restriction from prior PR33, for any eligible nonanomalous good p:

  d_p=dim_Fp Sha(E/Q)[p] ≤ v_p h(L_p)−1, and d_p is even.

At supersingular p, n=p²−1≥6888 for p≥83. Minkowski gives every ideal class a representative of norm at most M=(n!/n^n)(4/π)^r2 sqrt(|D_L|).

A fully elementary bound for every n≥100 is (n!/n^n)^(1/n)<2/5: from log n!≤n logn−n+1+logn, (1+logn)/n decreases and is <3/50 for n≥100, and exp(−47/50)<2/5. Furthermore (4/π)^(r2/n)<sqrt(4/3), and |D_L|^(1/(2n))<sqrt(389p). Therefore

  M^(1/n)<(4/(5sqrt3))sqrt(389p)<p

for p≥83, because 16·389/75=6224/75<83. Set B=p^n; harmonic divisor counting yields h(L)≤B(1+log B)^(n−1), and 1+n log p<p³ for p≥83. Thus

  h(L_p)<p^(4n−3),
  v_p h(L_p)≤4n−4,
  **dim_Fp Sha(E/Q)[p]≤4n−6 = 4(p²−1)−6**.

At p599, this upper is 1,435,194 (previously 1,793,994). At p107, it is 45,786 (previously 57,234). The reduction is genuine, but still much too weak for vanishing.

## E. NEW actual p599 and p16231 MW-logarithm saturation certificates

Use the short-model isomorphism X=36x+12,Y=216y+108, giving E_s:Y²=X³−3024X+46224. For a Jacobian projective point (Xj,Yj,Z), the ORIGINAL integral formal parameter is t=−6Z(Xj−12Z²)/(Yj−108Z³). For nonanomalous p and Np=#E(Fp) a p-unit,

  log_p(S)/p modp = (Np^−1 modp)·( t([Np]S)/p modp ).

Exact modular short-curve multiplication using weighted-Jacobian projective normalization (no huge rational coordinates) gives CONSISTENT residues with precision p^30,p^60 and p^100. The same implementation reproduces all earlier independently known log digits p5,7,11,13,17,19,23.

p=599: Np=600, log(P)/p=119 and log(Q)/p=121 modulo599.
  Therefore R599=Q−298P is primitive in MW and locally 599-divisible in E(Q599), checked by exact t([600]R599)=0 mod599².

p=16231: Np=16104, log(P)/p=6575 and log(Q)/p=12208 modulo16231.
  Therefore R16231=Q−698P is primitive in MW and locally 16231-divisible in E(Q16231), checked by exact t([16104]R16231)=0 mod16231².

Because E(Q389)/p=0 for both, these strict MW classes restrict to nontrivial everywhere-unramified **cyclic p-quotients** in their respective L_p character fields (using the already proved Borel/Shapiro injection). Thus the known MW baseline r_chi,p≥1 and the excess class-field injection Sha[p]→Hom_Δ(Cl(L_p)/p,W)/Fp·h_R are now validated without an unproved MW-localization assumption at p599 and p16231.

**Further integral consequence at p16231:** the previously unverified local logarithmic Kato-shadow saturation exponent d=min(v_p(log(P)/p),v_p(log(Q)/p)) is **exactly d=0**. The mod-p primitive kernel is generated by Q−698P; the normalized Kato shadow is a unit multiple thereof. This establishes no new Kato reciprocity or global Sha theorem by itself.

Reproduction:
- verification/bsd389_small_character_field_exact_ramification.py
- verification/bsd389_padic_mw_local_wedge_certified.py

Assistant-executed SHA256 of verified current-container versions:
- exact ramification 09abb55883cc82237dca223311bbdc985ef50fabf8c86156d29b50245992441e
- local MW 8f4eb384dd9c82c9adbba5e04877ba880c7efd611f4851e0cc43a76653440234

**Boundary:** No actual class group order or r_chi(599), r_chi(16231) was computed. The desired constant r_chi,p≤2 for all sufficiently large p, global Sha finiteness, and exact complex rank-two BSD leading coefficient remain unproved.
