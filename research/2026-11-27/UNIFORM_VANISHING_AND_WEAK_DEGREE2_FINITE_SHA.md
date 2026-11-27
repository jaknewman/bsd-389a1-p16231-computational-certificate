# BSD 389a1 — exact rank-two forced vanishing, weak two-support finiteness, and limits of a Bockstein contraction

**27 November 2026.** Mathematical review of the hypotheses needed to descend primitive Kato/Kurihara derivatives to two auxiliary factors. Contains two valid conditional-on-published-theorems deductions plus an elementary algebraic no-go; **H₂ is not proved**, and neither the global finiteness of Sha nor full BSD is proved.

## 1. Uniform rank-forced vanishing at all good ordinary primes

Let \(E:y^2+y=x^3+x^2-2x\), of proved Mordell–Weil rank 2 and \(E(\mathbf Q)[p]=0\). Let \(p\ge5\) be a good ordinary prime for which the full cyclotomic Selmer module is torsion over \(\Lambda=\mathbf Z_p[[T]]\), and let
\(X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\vee\).

Since \(\Gamma=\operatorname{Gal}(\mathbf Q_\infty/\mathbf Q)\) is pro-\(p\), any nonzero \(\Gamma\)-stable \(\mathbf F_p\)-space \(E(\mathbf Q_\infty)[p]\) would have nonzero invariants, contradicting \(E(\mathbf Q)[p]=0\). Therefore the restriction \(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)\to\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\Gamma\) is injective. The two independent rational Kummer classes show

\[
\operatorname{rank}_{\mathbf Z_p}(X_p/TX_p)\ge2.
\]

Localize the torsion \(\Lambda\)-module \(X_p\) at the height-one prime \((T)\). Since \(p\) becomes invertible, \(\Lambda_{(T)}\) is a DVR, and
\[
\operatorname{length}_{\Lambda_{(T)}}X_{p,(T)}
=\operatorname{ord}_T(\operatorname{char}_\Lambda X_p)
\ge\dim_{\mathbf Q_p}(X_p/TX_p)\otimes\mathbf Q_p\ge2.
\]
The inequality follows from the elementary divisor structure over a DVR.

By Wuthrich, *On the Integrality of Modular Symbols and Kato's Euler System for Elliptic Curves* (2014), Corollary 19, **the characteristic series of \(X_p\) divides the analytic \(p\)-adic L-function**. Projecting to the trivial tame character is exact. Consequently,

\[
\boxed{L_p^{(\eta=0)}(E,T)\in T^2\mathbf Z_p[[T]]\quad\text{at every such ordinary }p.}
\]

For the split multiplicative prime \(p=389\), Corollary 19 has the extra full augmentation factor \(I\), which projects to \((T)\). Hence

\[
\boxed{L_{389}^{(\eta=0)}(E,T)\in T^3\mathbf Z_{389}[[T]].}
\]

**New practical consequence:** the vanishing of coefficients \(c_{p,0},c_{p,1}\) in *all* raw \(p^2\) calculations for ordinary \(p\ge5\) is now explained **uniformly**, using the finite-level stabilization lemma of this PR. It need not be checked prime by prime for new primes. These facts do **not** imply that the next coefficient is a \(p\)-unit.

## 2. A weaker degree-two theorem proves FINITENESS of Sha[p∞]

Assume \(p\ge5\) has good reduction, \(\bar\rho_{E,p}\) is surjective, the Manin constant is a \(p\)-unit, and the same exact hypotheses of the relevant theorems hold. Write
\[
\widetilde\delta_n\in\mathbf Z_p/I_n,\qquad
\rho_p=\min\{\nu(n):\widetilde\delta_n\ne0\}.
\]
This uses **nonzero modulo \(I_n\)**, *not* nonzero modulo \(p\). Let
\(\partial_p^{(i)}\) be the minimal \(\mathbf Z_p\)-valuation among degree-\(i\) Kurihara coefficients, as defined in Kim, Theorem 1.8.

Castella–Sano, *On Refined Nonvanishing Conjectures by Kurihara and Kolyvagin* (2026), Theorem B gives
\[
\partial_p^{(\infty)}=\operatorname{ord}_p(\mathrm{Tam}_E)=0
\]
for all these ordinary good primes and, when \(N=389\) is squarefree, also for good supersingular primes. Here \(\mathrm{Tam}_E=1\).

If **there exists just one** admissible \(n=\ell_1\ell_2\) with
\(\widetilde\delta_n\ne0\) in \(\mathbf Z_p/I_n\), possibly
\(\widetilde\delta_n\equiv0\bmod p\), then \(\rho_p\le2\). Kim, Theorem 1.8(1) identifies \(\rho_p\) with the \(\mathbf Z_p\)-corank of \(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)\), which is \(\ge\operatorname{rank}E(\mathbf Q)=2\). Thus \(\rho_p=2\).

Kim, Theorem 1.8(3) further shows that the Selmer quotient by its maximal divisible subgroup is finite of length
\[
\partial_p^{(2)}-\partial_p^{(\infty)}=\partial_p^{(2)}.
\]
As the two rational Kummer classes already fill its maximal divisible subgroup, this quotient equals the finite group \(\Sha(E/\mathbf Q)[p^\infty]\). Therefore

\[
\boxed{\exists \,\widetilde\delta_{\ell_1\ell_2}\ne0
\ \Longrightarrow\
\Sha(E/\mathbf Q)[p^\infty]\text{ finite},\quad
v_p(\#\Sha(E/\mathbf Q)[p^\infty])=\partial_p^{(2)}.}
\]

The finite Tate–Shafarevich group carries a perfect alternating Cassels–Tate pairing for odd \(p\), hence its order is a square and \(\partial_p^{(2)}\) is **even**.

In particular, a degree-two Kurihara witness nonzero modulo \(p^2\) but divisible by \(p\) must be accompanied by **another unit witness modulo \(p\)**; indeed its valuation is at most 1 while the minimum must be even, hence it is 0.

**Converse (equivalence).** If \(\Sha(E/\mathbf Q)[p^\infty]\) is finite, then the global Kummer sequence gives \(\operatorname{corank}_{\mathbf Z_p}\operatorname{Sel}_{p^\infty}=2\). By Kim, this corank equals \(\rho_p\). Consequently \(\rho_p=2\), and by the definition of \(\rho_p\) there exists an admissible two-factor coefficient which is nonzero in its coefficient ring. Thus, under these hypotheses, we have the complete characterization

\[
\boxed{\Sha(E/\mathbf Q)[p^\infty]\text{ finite}
\quad\Longleftrightarrow\quad
\exists n=\ell_1\ell_2:\widetilde\delta_n\ne0
\text{ in }\mathbf Z_p/I_n.}
\]

Similarly, in light of Castella–Sano's \(\partial^{(\infty)}=0\), **\(\Sha[p^\infty]=0\)** is equivalent to existence of a degree-two **unit** coefficient. These equivalences are exact reformulations of Kim and Kummer, and *not* independent proofs of either desired property.

**This gives a cheaper intermediate goal:** produce a degree-two coefficient which is merely nonzero at any \(p\)-power precision to prove finiteness first, then identify its minimal valuation to determine the finite \(\Sha\) exactly. This does not supply a uniform proof of nonzero degree-two witnesses.

## 3. Why an Euler second jet cannot be inverted integrally

For an admissible auxiliary prime \(\ell\),
\[
P_\ell(1+Y)\equiv Y^2\pmod p
\]
in the *formal polynomial* ring. But in the finite augmented group algebra,
\[
A_p=\mathbf F_p[Y]/(Y^p),
\quad\mu_{Y^2}:A_p\longrightarrow A_p,
\quad x\longmapsto Y^2x
\]
has
\[
\operatorname{rank}(\mu_{Y^2})=p-2,\qquad
\ker(\mu_{Y^2})=(Y^{p-2}),\quad
\dim_{\mathbf F_p}\ker=2.
\]
So \(Y^2\) is a zero divisor and has **no integral inverse or universal left-inverse**, despite its leading scalar coefficient being 1. This precisely prevents turning a double Euler zero into an automatic primitive contraction.

An independent p-torsion obstruction is seen in the elementary paired finite module
\[
A_e=(\mathbf Z/p^e)^2
\]
with its standard hyperbolic alternating pairing. Its presentation matrix is \(\operatorname{diag}(p^e,p^e)\); its determinantal content has valuation \(2e\). No integral change of bases can make this determinant a unit when \(e>0\). This toy model is *algebraic*, not a claim that \(\Sha(389a1)\) is nonzero.

These two barriers are logically independent: the auxiliary Euler jet being formally a unit times \(Y^2\) does not remove the p-adic Fitting obstruction carried by the global finite Selmer quotient.

## 4. What an actual new theorem must achieve

A proposed **Bockstein second-derivative contraction** must supply an explicit global integral morphism **on the Selmer complex** that, after imposing the \(p\)-local and finite-singular conditions, controls both:
1. the completely mixed augmentation coefficient (invisible under all single-prime norm projections), and
2. the \(p\)-adic Fitting-content of the finite quotient, i.e. exactly the missing p-primary obstruction.

**No universal integral inverse to \(Y^2\) exists.** It would be circular to posit an arbitrary unit-preserving contraction at degree two as a theorem without constructing and verifying its global cohomological map.

## Sources

- Wuthrich (2014), Corollary 19: https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-19/12.pdf
- Castella–Sano (2026), Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

**Not a proof of the full conjecture.**
