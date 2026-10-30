# p=599 supersingular Hecke shortcut: exact proof audit of Sage 10.9

**Date:** 2026-10-30. **Status:** algebraic finite-to-analytic bridge **derived line-by-line against Sage 10.9**; user-authenticated finite coefficient PASS; independent Sage small-prime regression / external theorem-level review still pending. Not a claim that Sage \`p_primary_bound(599)\` returned a value. Do not silently replace "derived" with "formally mechanically verified".

## Objects and source

E: y²+y=x³+x²-2x, conductor and discriminant 389, rank r=2.
p=599, a_p=0, real_components=2, p-good supersingular.
Write L=E.padic_lseries(p) with default \`implementation='eclib', normalize='L_ratio'\` and \`S_n(a)=L._modular_symbol(QQ(a)/p^n)\`. Table construction in \`verification/kurihara_manin_390_fast.py\` uses precisely eclib's \`ECModularSymbol(E,sign=1)\`; the user checked the eclib \`_scaling=1\` and the values at 1/5, 1/41 and 1/599. Full 390-entry direct Sage comparison is a **further independent normalization check**, see issue #4.

The source inspected is the tagged **Sage 10.9**:
- [\`padic_lseries.py\`](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/padic_lseries.py), \`measure()\` (~line 345), \`pAdicLseriesSupersingular.series()\` (~1145), \`_prec_bounds()\` (~1344), \`Dp_valued_series()\` (~1398).
- [\`sha_tate.py\`](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py), \`an_padic()\` (~458, supersingular block ~649), \`p_primary_bound()\` (~767).
- Stein–Wuthrich, [*Algorithms for the Arithmetic of Elliptic Curves Using Iwasawa Theory*](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf), Thms 6.2 and 7.3, Algorithm 11.1.

## Lemma 1: exact cyclotomic lift identities

For n=2,3, write a=omega(a)gamma^{j_n(a)} (mod p^n), gamma=1+p, j_n(a) in {0,...,p^{n-1}-1}. Define w_n(a)=binom(j_n(a),2).

(i) For b mod p² a unit and a=b+t p² its p lifts mod p³, we have j_3(a)≡j_2(b) (mod p); indeed j_3(a)=j_2(b)+p*t' where t' runs over {0,...,p-1}. Consequently
\`\`\`text
sum_{a=b (mod p²)} w_3(a) = p*w_2(b) (mod p²).
\`\`\`
Proof: expand binom(j+p t',2); sum t' is p(p-1)/2, so all nonconstant terms vanish mod p² for odd p.

(ii) For any fixed nonzero residue c mod p, j_2 runs once over {0,...,p-1} as b runs over its p lifts mod p². Hence
\`\`\`text
sum_{b=c (mod p)} w_2(b) = binom(p,3) = 0 (mod p), p>=5.
\`\`\`

## Lemma 2: Hecke collapses the p³ quadratic coefficient

Set
\`\`\`text
A3 = sum_{a in (Z/p³)^×} w_3(a)*S_3(a)
B3 = sum_{a in (Z/p³)^×} w_3(a)*S_2(a mod p²).
C2 = sum_{b in (Z/p²)^×} w_2(b)*S_2(b) (mod p).
\`\`\`

As a weight-two Hecke eigen-symbol for T_p, at a_p=0,
\`\`\`text
sum_{t=0}^{p-1} S_3(b+t p²)
    = a_p S_2(b)-S_1(b)
    = -S_1(b),    b in (Z/p²)^×.
\`\`\`
All S_n(a) are p-integral **provided** the eclib 390-Manin basis used to generate the user's table is the normalized S; p-integrality is checked at that basis by \`table_390\`.

By Lemma 1(i), w_3(a)≡w_2(b) mod p on each p²-fibre. Then
\`\`\`text
A3 = -sum_{b mod p² unit} w_2(b)*S_1(b) = 0 (mod p),
\`\`\`
because S_1(b) depends only on b mod p and Lemma 1(ii) applies to each fibre.

Likewise, Lemma 1(i) gives **an integral quotient** B3/p with
\`\`\`text
B3/p = C2 = 543 (mod p).
\`\`\`
This uses only S_2(b) modulo p and does not require its residues modulo p².

User-executed finite data: C0=0,C1=0,C2=543 mod 599, 179101 sign pairs, 1924081 continued-fraction edges, checksum 779927018, authenticated table SHA256 \`fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8\`.

## Lemma 3: Sage Frobenius projection and certified precision

At a_p=0, alpha²=-p. \`measure\` is
\`\`\`text
alpha^(-3)*S_3(a) - alpha^(-4)*S_2(a).
\`\`\`
Since alpha^(-3)=alpha/p² and alpha^(-4)=1/p², the coefficient of T² in the n=3 finite sum, **after dividing by the two real components** (twist D=1 and period quotient=1), is G+alpha*H with
\`\`\`text
G = -B3/(2p²),     H = A3/(2p²).
\`\`\`

In \`Dp_valued_series\`, phi=[[0,-1/p],[1,0]], and the row vector \`(G,-p*H)\` is multiplied by \`((1-phi)^(-2)).transpose()\`. Direct 2x2 algebra produces
\`\`\`text
F0 = [p*(p-1)*G+2*p²*H]/(p+1)²
   = [2*A3-(p-1)*B3/p]/[2*(p+1)²].
F1 = [2*p²*G-p²*(p-1)*H]/(p+1)²
   = [-2*B3-(p-1)*A3]/[2*(p+1)²].
\`\`\`

At (n,prec)=(3,3), the tagged Sage 10.9 \`_prec_bounds\` returns \`[+Infinity,-1,-1]\`, in **alpha-adic** valuations. An error O(alpha^-1) in the coefficient has scalar coordinate e0 in Zp and alpha coordinate e1 in p^-1 Zp (since alpha²=-p). In the above projection, e0 enters multiplied by p and e1 by p², so both F0 and F1 have **error in p Zp**. Therefore the mod-p residue from the finite n=3 sum is also the residue of the true normalized D_p-valued p-adic L-series.

Thus, without enumerating p³ units,
\`\`\`text
F0 = -(p-1)*543 / [2*(p+1)²] = 571 (mod 599),
F1 = 0 (mod 599).
\`\`\`
In particular the analytic quadratic coefficient has p-adic valuation zero in its first coordinate.

## Lemma 4: upper bound (applicability review)

User Sage arithmetic PASS: rank 2 proven, the two Mordell–Weil generators are certified; E(Q)_tors=1; a_599=0; E good supersingular at 599; residual mod-p Galois representation surjective; normalized p-adic regulator \`reg/(log_p(1+p)^2)\` has first-coordinate residue 571 (unit), second-coordinate valuation 1; Tamagawa product 1. Kato's divisibility implies analytic order of vanishing at least r=2; Lemma 3 makes it at most 2. The conditions and inequality in Stein–Wuthrich Algorithm 11.1 (supersingular branch) then give
\`\`\`text
v_p(#Sha(E/Q)(p)) <= v_p(F0) - v_p(Reg_gamma,0)
                    = 0-0 = 0.
\`\`\`
If the stated identifications, integrality and theorem hypotheses are all validated, this forces Sha(E/Q)[599^infinity]=0. The output of the short verifier is **not** itself a mechanically verified proof of these external theorems.

## Outstanding independent checks before promoting to publication-grade unconditional certificate

1. **All 390 Manin entries:** direct Sage comparison of the authentic saved p=599 table against \`L._modular_symbol\` (not just three sample cusps), including the exact normalization. The expected hash and local table input are needed.
2. **Small supersingular end-to-end regression:** at p=5 on 1483a1, directly compute the full n=3 p-adic L-series and compare its D_p quadratic coefficient to the Hecke-derived p² coefficient with the exact \`real_components\` factor. This is intentionally *not* used to prove the p599 result, but checks the convention independently.
3. **Independent external theorem review:** ensure the p599 vector valuation in the Perrin–Riou lattice, the Kato divisibility hypotheses, and the rank-2 regulator match the exact theorem, not a conjectural BSD equality.

Any failure must be archived and corrected, without relabelling previous numerical PASS reports as false or silently asserting Sha vanishing.
