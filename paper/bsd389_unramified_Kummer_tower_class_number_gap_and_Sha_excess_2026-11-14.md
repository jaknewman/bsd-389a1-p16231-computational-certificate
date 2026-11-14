# E389a1: actual everywhere-unramified Kummer towers and a p^6 class-number obstruction to nonzero Sha[p]

**14 November 2026 — genuine arithmetic theorem (under stated published Galois/parity inputs) and assistant-executed exact local point computations.** This note directly attacks the *class-field module*, not another formal Selmer-Fitting identity. It proves divisibility of ordinary ideal class numbers by large p-powers and constructs explicit primitive rational points realizing unramified Kummer extensions at p=5,7. It also proves a one-way numerical criterion for Sha[p]=0. It **does not** calculate any complete division-field class number, prove the desired upper bound on class multiplicities at all p, prove global finiteness of Sha or the complex BSD leading-term identity.

## 1. Fully grounded curve and local prerequisites

Let
$$E/\mathbf Q:y^2+y=x^3+x^2-2x,\qquad E(\mathbf Q)=\mathbf ZP\oplus\mathbf ZQ,$$
$$P=(-1,1),\quad Q=(0,-1),\quad N=389,\quad \Delta=+389.$$
Fix an odd good prime **p≥5, p≠97,389**, assume the natural residual representation \(\rho_{E,p}:G_\mathbf Q\twoheadrightarrow\mathrm{GL}_2(\mathbf F_p)\) is surjective, and require **non-anomalous** good reduction
$$p\nmid \#E(\mathbf F_p).$$

The published Stein–Wuthrich/LMFDB Galois information and Serre's open-image theorem supply residual surjectivity for all sufficiently large p, and the specific p5,7,11,13,17,19,23,599,16231 are treated independently in the project. The reduced smooth component at 389 is split multiplicative of type I1, with
$$\#\widetilde E_{\mathrm{ns}}(\mathbf F_{389})=389-1=388=4\cdot97,\qquad c_{389}=1.$$
For p≥5, p not 97,389, the formal kernel of reduction at 389 is a pro-389 group; hence
$$\boxed{E(\mathbf Q_{389})/p^nE(\mathbf Q_{389})=0\quad\forall n\ge1.}\tag{L389}$$
At the good nonanomalous p, the reduction group is of order prime to p and the formal logarithm is an isomorphism \(E_1(\mathbf Q_p)\simeq p\mathbf Z_p\); therefore
$$
\boxed{E(\mathbf Q_p)/p^nE(\mathbf Q_p)\simeq\mathbf Z/p^n\mathbf Z\quad\forall n\ge1.}\tag{Lp}
$$
These two statements are the *local* key, and they are independent of Sha.

Class-number lower bounds for division fields have prior literature (not claimed invented here): J. Garnek, *On class numbers of division fields of abelian varieties*, J. Théor. Nombres Bordeaux 31 (2019), pp.227–242, https://www.numdam.org/item/JTNB_2019__31_1_227_0/; N. Dainobu, *Ideal class groups of division fields of elliptic curves and everywhere unramified rational points*, J. Number Theory 264 (2024), pp.211–232, https://www.sciencedirect.com/science/article/pii/S0022314X24001434 . The present specialization to 389a1 and its exact local witnesses are proved below.

## 2. THEOREM A — true unramified Kummer extensions of order p^(2n), at every level

Define the genuine division field
$$F_{p,n}=\mathbf Q(E[p^n]).$$

**Theorem A.** For **every** \(n\ge1\), under §1's conditions there exists an actual primitive rational MW vector \(R_{p,n}=aP+bQ\), where \((a,b)\not\equiv(0,0)\bmod p\), such that \(R_{p,n}\in p^n E(\mathbf Q_p)\) and \(R_{p,n}\in p^n E(\mathbf Q_{389})\). The actual Kummer extension
$$
\boxed{L_{p,n}=F_{p,n}([p^n]^{-1}R_{p,n})/F_{p,n}}
$$
is an **everywhere unramified Galois extension** with
$$
\boxed{\operatorname{Gal}(L_{p,n}/F_{p,n})
\simeq E[p^n]\simeq(\mathbf Z/p^n\mathbf Z)^2,\quad
[L_{p,n}:F_{p,n}]=p^{2n}.}\tag{A}
$$
The primes of \(F_{p,n}\) above p and 389 are **completely split** in \(L_{p,n}\). Hence, without invoking BSD,
$$
\boxed{p^{2n}\mid h(F_{p,n})\qquad\text{for every }n\ge1.}\tag{CLASS-TOWER}
$$

**Proof.** Reduction of the saturated MW lattice modulo p^n is \(M_n=(\mathbf Z/p^n)^2\). By (Lp), its localization into \(E(\mathbf Q_p)/p^n\cong\mathbf Z/p^n\) is a row \((a_n,b_n)\) over \(R=\mathbf Z/p^n\). Such a map \(R^2\to R\) always has a **primitive kernel vector**: if the row has common p-adic valuation e<n, divide it by p^e and take \((b_n/p^e,-a_n/p^e)\); if the row is zero, take (1,0). Lift this vector to \(\mathbf ZP+\mathbf ZQ\) to obtain \(R_{p,n}\). It is not globally p-divisible, hence not globally p^n-divisible. By (L389) it is also p^n-divisible locally at 389.

Let \(V_n=E[p^n]\) and \(\Gamma_n=\operatorname{Gal}(F_{p,n}/\mathbf Q)\subseteq\mathrm{GL}_2(\mathbf Z/p^n)\). Its mod-p image is all GL2(Fp). The kernel of reduction modp is a p-group. The preimage of central \(-I\) modp in \(\Gamma_n\) contains an **order-two element** by Schur–Zassenhaus, and any order-two matrix congruent to −I modulo p is exactly −I (since \(g-I\) is invertible and \((g-I)(g+I)=0\)). Thus \(-I\in\Gamma_n\) **and is central**. Sah's lemma gives \(H^1(\Gamma_n,E[p])=0\).

The ordinary rational p-Kummer class of the primitive \(R_{p,n}\) is NONZERO in \(H^1(\mathbf Q,E[p])\), hence remains NONZERO after restriction to \(F_{p,n}\) by the inflation–restriction injection. Equivalently the \(\Gamma_n\)-equivariant mod-p reduction of the p^n-Kummer homomorphism
$$
h_n:G_{F_{p,n}}\to E[p^n],\quad
\sigma\mapsto\sigma(T)-T,\quad [p^n]T=R_{p,n}
$$
has nonzero image inside E[p]. That image is stable under the full GL2(Fp), hence is ALL of E[p] by irreducibility. Thus the Z/p^n-submodule \(\mathrm{im}\,h_n\subset E[p^n]\) surjects on its reduction modulo p; Nakayama's lemma forces \(\mathrm{im}\,h_n=E[p^n]\). Therefore the extension has the advertised degree \(p^{2n}\).

At every good ℓ different from p, a rational point's p^n-Kummer class is unramified (the local Kummer condition is the unramified subgroup for ℓ≠p and good reduction). At p and 389, R_{p,n} is actually locally p^n-divisible, so its restricted class is zero and its Kummer extension even **splits completely** after passage to \(F_{p,n}\). Thus \(L_{p,n}/F_{p,n}\) is everywhere unramified. Artin reciprocity embeds its finite abelian Galois group as a quotient of the ordinary ideal class group of \(F_{p,n}\), giving (CLASS-TOWER). QED.

**Subtle point:** The assertion at EVERY n does **not** follow by naively replacing p with p^n in the mod-p Sah lemma. The argument above uses the central order-two element at the full division level, reduction of the p^n-Kummer homomorphism, and Nakayama; this step is essential.

## 3. Explicit genuine rational point witnesses — exact arithmetic, no Sage

Define the formal parameter \(t=-x/y\) at the origin, and let \(N_p=\#E(\mathbf F_p)\), a p-adic unit under §1's hypotheses. For any rational point \(S\),
$$
\frac{\log_p S}{p}\equiv
N_p^{-1}\frac{t([N_p]S)}p \pmod p.
$$
This uses the integral invariant differential dx/(2y+1); the logarithm begins \(t+O(t^2)\) and t([N]S)∈pZp, so the congruence is exact.

A standalone standard-library **Python Fraction** verifier was ACTUALLY EXECUTED in the assistant container (source [here](../verification/bsd389_unramified_division_classgroup_certificate.py)); it counts E(Fp), applies exact rational Weierstrass group laws, and checks t([N_p]R)≡0 modulo p², without approximations.

| p | #E(Fp) | log(P)/p modp | log(Q)/p modp | selected primitive R=aP+bQ | exact R coordinates |
|---:|---:|---:|---:|---|---|
| 5 | 9 | 2 | 4 | −2P+Q | (−3/4,7/8) |
| 7 | 13 | 5 | 3 | −2P+Q | (−3/4,7/8) |
| 11 | 16 | 6 | 7 | −3P+Q | (133,−1540) |
| 13 | 17 | 6 | 3 | −P+2Q | (−2,0) |
| 17 | 24 | 10 | 10 | −P+Q | (1,−1) |
| 19 | 15 | 15 | 17 | −P+2Q | (−2,0) |
| 23 | 28 | 6 | 5 | −3P−Q | (2869/676,154413/17576) |

The SAME point \(R=-2P+Q=(-3/4,7/8)\) is locally 5-divisible and 7-divisible, but primitive in the integral MW basis, and yields real unramified degree-25 and degree-49 extensions of F_{5,1} and F_{7,1}. **These extensions are mathematically defined via all p-division points of R; their defining polynomials and class groups have NOT been numerically computed.**

The same exact script independently verifies stronger n=2 **actual local p²-divisibility**:
- p=5, \(R_{5,2}=-4P-3Q=(6832045/511392996,\ -315516267935/11564641211544)\), and \(t([9]R_{5,2})\equiv0\bmod125\);
- p=7, \(R_{7,2}=-4P-5Q=(-5476046670171/4640693967529,\ 10357242007585928617/9997108243588095083)\), and \(t([13]R_{7,2})\equiv0\bmod343\).

**A stronger exact fifth-adic surprise.** The local audit goes beyond the p² congruence: for the *same* primitive vector
$
R_{5}^\star=-4P-3Q,
$
the exact fraction \(t([9]R^\star_5)\) has
$
\boxed{v_5(t([9]R^\star_5))=5.}
$
Indeed the rational numerator is divisible by \(5^5\) and NOT by \(5^6\), while its denominator is a 5-adic unit; a direct residue check gives \(t([9]R^\star_5)\equiv6250\bmod5^6\). Formal log identifies the reduction kernel with \(5\mathbf Z_5\), hence \(R^\star_5\) is locally divisible by \(5^4=625\) in \(E(\mathbf Q_5)\) (but not by \(5^5\)). By Theorem A this **single explicit rational point** constructs a mathematically genuine **everywhere-unramified extension**
$
\boxed{
[\mathbf Q(E[5^4],[5^4]^{-1}R^\star_5):\mathbf Q(E[5^4])]
=5^8=390625.
}
\tag{EXPLICIT-5-4}
$
For comparison, \(v_7(t([13]R^\star_7))=3\) for \(R^\star_7=-4P-5Q\), so its certified local divisibility exponent is precisely \(7^2\), producing degree \(7^4=2401\). These exact numerator valuations were recomputed from independent rational-coordinate group operations, **not** inferred merely from the p² formal log linear congruence. No full number-field class group calculation is claimed.

Both vectors are primitive modulo p, so the corresponding **everywhere-unramified** division extensions above F_{5,2} and F_{7,2} have genuine degrees
$$
\boxed{[L_{5,2}:F_{5,2}]=625,\qquad[L_{7,2}:F_{7,2}]=2401.}
$$
These degree statements follow from the proved Kummer theorem, NOT from computation of Galois groups via explicit field polynomials.

## 4. THEOREM B — an arithmetic class-number GAP if Sha[p]≠0

At level n=1 write \(F=F_{p,1}\), \(\Gamma=\mathrm{GL}_2(\mathbf F_p)\), \(V=E[p]\), and define the finite **ordinary ideal class group quotient**
$$
\boxed{
C_p:=
\frac{\mathrm{Cl}(F)}
{p\,\mathrm{Cl}(F)+\langle [\mathfrak p]:\mathfrak p\mid p\cdot389\rangle}.
}\tag{C}
$$
The quotient means the maximal elementary p-class-field extension unramified at ALL finite primes and **totally split above p and 389**. The finite Γ-action is the actual one on ideal classes.

Define the p-strict Selmer subgroup
$$
S_p^0=
\ker\big(\operatorname{Sel}(E[p]/\mathbf Q)\xrightarrow{\operatorname{loc}_p}
E(\mathbf Q_p)/pE(\mathbf Q_p)\big).
$$
Since every p-Selmer class is unramified outside p389, and the local class at 389 is identically zero by §1, its restriction to F is everywhere unramified if it is p-strict, and trivial at every decomposition group over p,389. The central −I Sah injection then gives a **genuine Fp-linear injection**
$$
\boxed{
S_p^0\hookrightarrow\operatorname{Hom}_\Gamma(C_p,V).
}\tag{FINE}
$$

Set \(d_p=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]\), which is EVEN because E has root number +1, MW rank2, the proved p-parity theorem (Dokchitser–Dokchitser), and the Cassels–Tate alternating quotient theorem; no global finiteness of Sha is assumed. The exact Kummer sequence gives
$$
\dim\operatorname{Sel}(E[p]/\mathbf Q)=2+d_p.
$$
The local p-Kummer target has dimension 1, so
$$
\dim S_p^0\ge1+d_p.
$$
Writing \(k_p=\dim_{\mathbf F_p}\operatorname{Hom}_\Gamma(C_p,V)\), (FINE) gives
$$
\boxed{k_p\ge1+d_p.}\tag{K}
$$

Because V is ABSOLUTELY irreducible and \(\operatorname{End}_\Gamma(V)=\mathbf F_p\), the maximal semisimple quotient of C_p has a direct factor \(V^{k_p}\). Indeed independent maps C_p→V induce a surjection onto V^{k_p} (the target is a direct sum of copies of one simple module; any proper Γ-submodule has an Fp-linear relation between component maps). Hence the ordinary ideal class group of F has order divisible by \(p^{2k_p}\). This yields **the proven quantitative inequality**
$$
\boxed{
v_p(h(F_{p,1}))\ge2+2d_p.
}\tag{GAP}
$$

If Sha[p]≠0, p-parity says \(d_p\ge2\), so
$$
\boxed{
\Sha(E/\mathbf Q)[p]\ne0\ \Longrightarrow\
p^6\mid h(F_{p,1}).}
\tag{P6}
$$
And the **contrapositive**, valid even if the global Sha is not known finite, is
$$
\boxed{
v_p(h(F_{p,1}))\le5\ \Longrightarrow\
\Sha(E/\mathbf Q)[p^\infty]=0.}
\tag{VANISH}
$$

A still stronger, representation-theoretic practical criterion is \(k_p\le2\Rightarrow \Sha[p^\infty]=0\). These are **sufficient** criteria; class-group p-primary size could be much larger for unrelated reasons even when Sha[p]=0. Nothing in the proof establishes \(k_p\le2\) or \(v_p h(F)\le5\) uniformly.

## 5. THEOREM C — explicit removal of the *forced* Mordell–Weil class-field quotient

Let
$$M_p=E(\mathbf Q)/pE(\mathbf Q)=\mathbf F_p\{P,Q\},\qquad
M_p^0=M_p\cap S_p^0.$$
Suppose at least one of the local normalized logs of P,Q is nonzero modulo p (i.e. MW localization \(M_p\to E(\mathbf Q_p)/p\) is **surjective**). The genuine exact local tests above prove this extra hypothesis for p=5,7,11,13,17,19,23; it is NOT known for all p and must not be silently assumed in an all-large-p argument.

Then \(\dim M_p^0=1\). Choose a primitive generator \(R_p\in M_p^0\), and let
$$h_{R_p}:C_p\twoheadrightarrow V$$
be its genuine everywhere-unramified surjective Kummer homomorphism constructed in Theorem A. The p-Selmer Kummer exact sequence and surjectivity of the MW localization imply
$$
S_p^0/M_p^0\simeq\Sha(E/\mathbf Q)[p].
$$
Quotienting the injection (FINE) by the known one-dimensional image of M_p^0 yields the **canonical-after-choosing-\(R_p\), ACTUAL independent-of-Sha injection**
$$
\boxed{
\Sha(E/\mathbf Q)[p]\hookrightarrow
\operatorname{Hom}_\Gamma(C_p,V)/\mathbf F_p\,h_{R_p}.
}\tag{EXCESS}
$$

This is mathematically a stronger realization of the user's desired comparison: instead of *all* class-field classes, the finite target is the **excess after removing the explicit known unramified MW class**. Its dimension is \(k_p-1\). If it has dimension ≤1, Cassels–Tate parity forces Sha[p]=0. The maps depend on p and no uniform bound on the excess is proved.

An even more concrete, though not canonically split, class-group sequence comes from the explicit surjection \(h_{R_p}:C_p\twoheadrightarrow V\). Its kernel \(D_p^{\rm ex}\) is a finite Γ-module. Restriction of all morphisms from C_p to this kernel induces an injection
$$
\operatorname{Hom}_\Gamma(C_p,V)/\mathbf F_p h_{R_p}
\hookrightarrow \operatorname{Hom}_\Gamma(D_p^{\rm ex},V).
$$
Proof: the only morphisms C_p→V annihilating ker(h_R) are those factoring through C_p/ker(h_R)=V; such maps are Fp-multiples of h_R by Schur's lemma. Consequently Sha[p] injects into \(\operatorname{Hom}_\Gamma(D_p^{\rm ex},V)\) when the MW local log gate holds, and if Sha[p] has dimension d≥2 then this *excess kernel* must have a quotient V² and order divisible by p^4. This describes the **precise arithmetic object** in the class group that needs to be bounded, AFTER the unavoidable p² baseline is removed.

This is not an injection into a p-INDEPENDENT finite group, and the existence of the actual quotient h_R does not imply D_p^{ex}=0.

## 6. A density-one, genuinely global-in-p consequence (but in the WRONG DIRECTION for BSD)

For p≥7, the condition p | #E(Fp) forces a_p=1, since #E=p+1−a_p and |a_p|≤2√p<p−1. E has NO CM (j=1404928/389 is not an algebraic integer). Serre's open-image theorem gives full residual GL2(F_ell) for all sufficiently large auxiliary ell.

Fix such an ell. The set of good rational primes p with a_p=1 is contained in the Chebotarev set trace(Frob_p)=1 modulo ell. There are at most ell³ matrices with prescribed trace in GL2(Fell), so its upper density is ≤
$$
\frac{\ell^3}{|\mathrm{GL}_2(\mathbf F_\ell)|}
=\frac{\ell^2}{(\ell-1)^2(\ell+1)}\xrightarrow[\ell\to\infty]{}0.
$$
Thus the anomalous primes have natural density zero. Residual full-GL2 holds for all but finitely many p by Serre. Hence:

**Corollary (TRUE uniform density-one theorem).** For a set of rational primes p of natural density ONE, all levels n≥1 satisfy
$$
\boxed{p^{2n}\mid h(\mathbf Q(E[p^n])).}
$$

This is an authentic global divisibility theorem following from the rank-two MW lattice and local arithmetic. **It is NOT** a uniform Sha upper bound: the unavoidable MW contribution forces class numbers to be divisible by p² at almost every p, so a naive 'class numbers prime to p' approach to killing Sha is impossible.

## 7. What remains unsolved, exactly

- Calculate the actual p-primary ideal class group or at least its V-isotypic **excess beyond h_R** at a new unproved p. This may be impractically large for F_{599}, F_{16231}.
- Prove, by an INDEPENDENT global arithmetic theorem, that the excess \(\operatorname{Hom}_\Gamma(C_p,V)/\mathbf F_p h_R\) has dimension ≤1 for all sufficiently large nonanomalous p, plus handle anomalous primes. This would imply Sha[p]=0 at those primes. The theorem itself is not produced here.
- The lower bound \(p^{2n}\mid h(F_{p,n})\) points IN THE OPPOSITE DIRECTION of a small class-number upper bound and may explain why this class-field approach is harder than the Kato–Iwasawa approach.
- Strong BSD additionally needs the exact complex leading-coefficient identity \(L''(E,1)/2=\Omega_E\operatorname{Reg}_E\cdot\#\Sha(E)\). The positive certified analytic rank-two interval is independent of this equality.

**VERDICT:** genuinely constructed everywhere-unramified Kummer extensions for all n and all p under explicit local gates; exact p^6 class-number gap if Sha[p]≠0; actual injection of Sha[p] into the *excess after removing a known unramified MW class*; and density-one class-number divisibility. No all-large-p Sha vanishing or full BSD.
