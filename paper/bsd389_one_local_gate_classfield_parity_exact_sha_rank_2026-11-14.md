# E389a1: the bad-prime local gate vanishes, and p-Selmer parity determines Sha[p] from one ray-class multiplicity

**2026-11-14.** Rigorously established conditional-on-standard-published-theorems (Tate local duality, Sah, global class field theory, Dokchitser–Dokchitser p-parity) **arithmetic theorem**, with exact newly run elementary E389a1 reduction audit. **No actual p-ray-class group or all-large-p bound has been computed.** In particular p=599 and 16231 Sha remain unsettled by this note.

## 1. Exact local bad-place calculation at 389 — the crucial simplification

Use the *actual* minimal curve E: y²+y=x³+x²−2x, Weierstrass tuple [0,1,1,−2,0]. Its exact invariants are
$$
c_4=112,\qquad c_6=-856,\qquad\Delta=389.
$$
Thus at \(\ell=389\), \(v_\ell(\Delta)=1\), the curve has type I1, and its Tamagawa number is 1. Since
$$
-c_6\bmod389=78=95^2\bmod389
$$
the reduction is **split** multiplicative. The smooth Néron special fibre over F389 is therefore \(\mathbf G_m(\mathbf F_{389})\), of order
$$
389-1=388=4\cdot97.
$$
The finite component group has order c389=1. The pro-389 kernel of reduction is uniquely p-divisible for all p≠389. Thus for p≥5, p≠97,389,
$$
E(\mathbf Q_{389})[p]=0,\qquad E(\mathbf Q_{389})/p=0.
$$
Since V=E[p] is self-dual via Weil pairing and \(p\ne389\), local Tate duality plus the local Euler–Poincaré characteristic give
$$
\dim_{\mathbf F_p}H^1(\mathbf Q_{389},E[p])
=2\dim_{\mathbf F_p}H^0(\mathbf Q_{389},E[p])=0.
$$
Consequently
$$
\boxed{H^1(\mathbf Q_{389},E[p])=0
\quad\forall p\ge5,\ p\notin\{97,389\}.}\tag{L389}
$$
**p=97 is the ONLY good p≥5 exception to this local vanishing**, not evidence of nonzero Sha[97]. p=389 is bad and needs separate treatment. Exact finite-field node proof: cubic discriminant \(4x^3+4x^2-8x+1\) has double zero at x=299, y=194, a separate smooth vertical tangent at x=179, whole singular special fibre has 389 F389-points and 388 smooth points. These arithmetic inputs are verified in the independent companion script.

**Important:** The coefficient module E[p] is still *ramified* at 389; one may not replace the original global Galois group G_{Q,{p,389,∞}} by G_{Q,{p,∞}}. Only the **local cohomology condition** vanishes.

## 2. Division-field class-field multiplicity and a smaller ray-class module totally split at 389

Fix good p≥5, p∉{97,389}, with surjective mod-p representation. Let
$$F_p=\mathbf Q(E[p]),\quad\Gamma_p=\mathrm{GL}_2(\mathbf F_p),\quad
S=\{p,389,\infty\},\quad V=E[p].$$
Define the finite elementary p quotient of the maximal S-ramified abelian Galois group of F_p:
$$
A_{p,S}=\operatorname{Gal}(F_{p,S}^{ab}/F_p)/p.
$$
By global class field theory it is a finite Fp-vector space with a canonical \(\Gamma_p\)-action. The central \(-I\) acts by −1 on V, so Sah's lemma gives H¹(Γ,V)=H²(Γ,V)=0. Inflation–restriction yields
$$
\boxed{H^1(G_{\mathbf Q,S},V)\simeq
\operatorname{Hom}_{\Gamma_p}(A_{p,S},V).}\tag{CF}
$$

For each w|389 in F_p, let \(D_w^{ab}\subset A_{p,S}\) be the image of the **entire** local decomposition group \(G_{F_{p,w}}\) (not only inertia). Form the \(\Gamma_p\)-stable quotient
$$
\boxed{
A_p^{(389\,\mathrm{split})}:=
A_{p,S}/\sum_{w\mid389}\operatorname{im}(G_{F_{p,w}}\to A_{p,S}).
}\tag{REL}
$$
It is the maximal elementary abelian p-extension of F_p **unramified outside primes over p and completely split at all primes over 389** (the base field F_p itself remains ramified at 389).

**Theorem (genuine smaller arithmetic target).**
$$
\boxed{
H^1(G_{\mathbf Q,S},V)\simeq
\operatorname{Hom}_{\Gamma_p}(A_p^{(389\,\mathrm{split})},V)
\qquad(p\notin\{97,389\}).
}\tag{CLASS}
$$

**Proof.** Every class on the left restricts to zero in \(H^1(\mathbf Q_{389},V)=0\) by (L389). After further restriction to every \(G_{F_{p,w}}\) its cocycle is identically zero because V is a trivial module on \(G_{F_p}\) (a zero cohomology class on the larger decomposition group is a coboundary, which vanishes on the smaller subgroup acting trivially on V). Thus every homomorphism in (CF) kills all the local \(D_w^{ab}\) and factors uniquely through the quotient (REL). Conversely any \(\Gamma_p\)-equivariant homomorphism out of (REL) gives one out of \(A_{p,S}\), and (CF) supplies its unique global class. QED.

**This is stronger than just dropping the bad-place local Selmer condition**: the non-relevant p-ray-class directions at all primes over 389 have actually been quotiented away. One can compute (REL) from p-ramified ray-class data of F_p and impose completely-split relations at the primes over 389. The resulting \(\Gamma\)-module still varies with p and may be very large.

## 3. Only ONE remaining rational local condition at p

Assume also that E has **non-anomalous good reduction** at p:
$$p\nmid\#E(\mathbf F_p).$$
This implies E(Q_p)[p]=0. Good-reduction p-adic Lie theory gives \(E(\mathbf Q_p)/p\simeq\mathbf F_p\). The local p-adic Euler characteristic and local Tate duality give
$$
\dim_{\mathbf F_p}H^1(\mathbf Q_p,V)=2,\qquad
\dim_{\mathbf F_p}H^1_f(\mathbf Q_p,V)=1.
$$
Hence its singular quotient
$$H^1_s(\mathbf Q_p,V)=H^1(\mathbf Q_p,V)/H^1_f(\mathbf Q_p,V)$$
is a SINGLE \(\mathbf F_p\)-line.

Let
$$
\boxed{
m_p=\dim_{\mathbf F_p}
\operatorname{Hom}_{\Gamma_p}(A_p^{(389\,\mathrm{split})},V).
}\tag{m}
$$
The exact comparison (CLASS) defines a concrete linear p-singular localization functional
$$
\ell_p:\operatorname{Hom}_{\Gamma_p}(A_p^{(389\,\mathrm{split})},V)
\longrightarrow H^1_s(\mathbf Q_p,V)\simeq\mathbf F_p.
$$
At good primes away from p,389 local p-Selmer equals unramified local cohomology; at 389 there is *no* H¹ to constrain, and at infinity H¹=0 for odd p. Therefore:
$$
\boxed{\operatorname{Sel}_p(E/\mathbf Q)=\ker\ell_p,\qquad
\dim\Sha(E/\mathbf Q)[p]=m_p-2-\varepsilon_p,}
\tag{ONE}
$$
where \(\varepsilon_p=\operatorname{rank}_{\mathbf F_p}\ell_p\in\{0,1\}\). None of this assumes Sha finite.

For p=599, exact finite-field point count gives #E(F599)=600 and a599=0 (supersingular), so (ONE) applies. For p=16231, #E(F16231)=16104 and a16231=128, so (ONE) applies. **These are eligibility gates, not calculations of m599 or m16231.**

## 4. Parity removes the final *unknown local rank* — exact Sha[p]-dimension formula

For every elliptic curve over Q and every p, the p-parity theorem of T. and V. Dokchitser (*Annals of Mathematics* 172 (2010), pp. 567–596) identifies parity of the p∞-Selmer corank with the global root number; equivalently, by the finite paired Cassels–Tate nondivisible quotient, the parity of \(\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)-\dim E(\mathbf Q)[p]\) equals the root sign. Our curve has **global root number +1** (archimedean −1, split multiplicative at 389 −1) and E(Q)[p]=0. Hence
$$
\boxed{\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)\equiv0\pmod2.}
\tag{PAR}
$$
Primary source: https://annals.math.princeton.edu/2010/172-1/p11 .
This parity statement does **NOT** assume global finiteness of Sha.

Combining (PAR) with (ONE), the only possibilities for \(\varepsilon_p\in\{0,1\}\) are
$$
\boxed{\varepsilon_p=m_p\bmod2.}\tag{EPS}
$$
Indeed \(m_p-\varepsilon_p=\dim Sel_p\) is even.

**Theorem (new exact primewise class-field formula).** For every p satisfying the hypotheses above (good, p≥5, p≠97,389, full GL2 image, non-anomalous at p),
$$
\boxed{
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)
=2\left\lfloor\frac{m_p}{2}\right\rfloor,
\qquad
\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
=2\left\lfloor\frac{m_p}{2}\right\rfloor-2.
}\tag{MAIN}
$$
Thus \(m_p\ge2\), and
$$
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=0
\iff m_p\in\{2,3\},
\qquad
\Sha(E/\mathbf Q)[p]\ne0\Longrightarrow m_p\ge4.
}\tag{BOUND3}
$$

This is a **genuine arithmetic condition on one finite p-ramified, 389-split ray-class \(\Gamma_p\)-module**, and there is **NO need to compute the local map** \(\ell_p\) to determine \(\dim\Sha[p]\) once m_p is known.

There is an even more general sufficient criterion without the non-anomalous assumption or the p=97 exception: when the full S-ramified equivariant Hom-space has \(\mathbf F_p\)-dimension at most 3, the true p-Selmer is a subspace, has dimension at least 2 by Kummer, and has **even** dimension by p-parity; it is therefore exactly 2 and Sha[p]=0. The smaller (389-split) module and exact equality (MAIN) require the extra stated local gates.

**Crucial honest boundary:** The desired UNIFORM assertion \(m_p\le3\) for all sufficiently large p is *not proved*. Nor has any \(A_p^{(389\,\mathrm{split})}\) been computed for p=599 or 16231. Thus (MAIN) is a new primewise **arithmetic characterization**, not an unconditional Sha annihilator or a BSD proof. Also the size and Galois structure of F_p vary drastically with p; no fixed integral presentation has been built.

## 5. Executed arithmetical regression

The dependency-free certificate
[verification/bsd389_classfield_one_gate_parity_audit.py](../verification/bsd389_classfield_one_gate_parity_audit.py)
was executed in the assistant's container on 2026-11-14, with SHA256
\`1e5c78046a04dd9c67bfff60c7678561e2cfeabf504ca23a3d1665b3e11c9547\`.
It verifies *exactly*:
- c4=112, c6=−856, Δ=389, splitness witness \(95^2\equiv -c_6\bmod389\);
- the unique 389-special-fibre singular node (299,194), 389 entire special-fibre points, 388 smooth points;
- actual #E(Fp) and good/anomalous gates at p=5,7,11,13,97,599,16231, including #E(F599)=600 and #E(F16231)=16104;
- finite-dimensional floor/parity identity for possible **hypothetical m_p** values m=2,...,12.

It does **NOT** compute the actual ray-class module A_p, the number m_p, any new Sha component or a uniform cutoff.

## 6. New precise global bottleneck

Instead of separately computing all p+1 conjugate isogeny-Selmer classes, imposing p−1 descent equations, and then computing two rational local gates, the new criterion reduces the question of finite-p Sha[p] to the **isotypic multiplicity**
$$
m_p=\dim\operatorname{Hom}_{\mathrm{GL}_2(\mathbf F_p)}
\left(\operatorname{Gal}(F_p^{ab,\,p\text{-ram},\,389\text{-split}}/F_p)/p,\ E[p]\right),
$$
and a universal parity formula. To finish the all-large-p goal, one would need a NEW theorem proving \(m_p\le3\) for all p outside a finite set, or another global uniform bound. Such a theorem is not supplied by Sah, Dirichlet's units, Stein–Wuthrich's finite-range checks, or Castella–Sano's arbitrary-auxiliary-degree nonvanishing.

**Verdict:** a strictly smaller arithmetic class-field module and complete removal of a local gate, plus an exact parity-determined p-rank formula. Nontrivial mathematical sharpening of the real Selmer descent, but not yet BSD.
