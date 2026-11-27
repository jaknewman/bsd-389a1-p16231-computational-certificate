# Reassessment of p-primary BSD389a1 conclusions — 27 November 2026

**Status:** primary-source theorem scope checked; the one-command numerical certificate and full source CSV are archived. This note distinguishes the *primitive real-period modular-symbol convention*, the full BSD real period, and **proved conclusions for audited primes** from extrapolations.

## 1. Correct the period-convention discrepancy

For the optimal curve
\(E:y^2+y=x^3+x^2-2x\), conductor 389, discriminant +389, the real locus has two connected components.

- The **least positive real period** is \(\omega^+\simeq2.49021256085505507532135779194\).
- The **real period in the complex BSD formula** is
  \(\Omega^{\rm BSD}=2\omega^+\simeq4.9804251217101101506427155839\).

The 390-component table \`verification/manin_390.txt\` is normalized by \(\omega^+\), in agreement with Wuthrich's modular-symbol definitions \([r]_E^+=\Re(\lambda(r))/\Omega_E^+\) (Wuthrich, 2014, §1) and Sage's *elliptic-curve modular symbol* convention.

However, Sage's **p-adic L-series default** is normalized using the Néron **BSD real period**, which produces a factor \(1/2\) relative to the primitive-symbol series. This factor is a \(\mathbf Z_p\)-unit for every odd p and therefore cannot change \(\mu\), \(\lambda\), nor the p-primary Selmer conclusion.

For good ordinary p, denote the raw second binomial moment
\(C_p=\sum_{a\bmod p^2,\ p\nmid a}m^+(a/p^2)\binom{j_p(a)}2\bmod p\).
The primitive-period leading coefficient and the Sage/BSD-period coefficient are respectively

\[
u_p\equiv a_p^{-2}C_p\pmod p,\qquad
u_p^{\rm BSD}\equiv 2^{-1}a_p^{-2}C_p\pmod p.
\]

Examples (raw \(C_p\), primitive \(u_p\), BSD/Sage \(u_p^{\rm BSD}\)):

|p|raw|primitive|BSD/Sage|
|---:|---:|---:|---:|
|5|2|3|4|
|7|5|3|5|
|11|2|7|9|
|13|2|6|3|
|17|1|9|13|
|89|8|78|39|

The independently published Sage documentation for \`EllipticCurve('389a').padic_lseries(5).series(2)\` has \([T^2]\equiv4\pmod5\), confirming the crucial factor-two convention; the previous posted coefficient 3 was the *primitive-period convention*, not Sage's one.

At split multiplicative \(p=389\), the primitive leading coefficient \(321\) corresponds to \(321/2\equiv355\pmod{389}\) in the BSD/Sage real-period convention; both are units.

**Do not confuse this factor-two unit with the theorem on exact normalization of the integral Manin table: that theorem remains valid.**

## 2. Primary theorem and no-finite-submodule criterion

Wuthrich, *On the integrality of modular symbols and Kato's Euler system for elliptic curves*, Documenta Math. 19 (2014), **Corollary 19**, proves for odd primes of ordinary semistable reduction

\[
\operatorname{char}_{\Lambda_{\rm full}}(X_{\rm full})\mid(L_p(E)),
\]

or in the split multiplicative case

\[
I\,\operatorname{char}_{\Lambda_{\rm full}}(X_{\rm full})\mid(L_p(E)).
\]

Projection by the integral trivial tame idempotent
\(e_0=(p-1)^{-1}\sum_{\delta\in\Delta}\delta\)
gives the corresponding divisibility for
\(X=\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\vee\),
with \(e_0I=(T)\).

Greenberg, *Iwasawa Theory for Elliptic Curves* (1998),
**Proposition 4.15(ii)** applies because \(F=\mathbf Q\),
\(e_p=1\le p-2\), and E has good ordinary or multiplicative reduction:
if \(X\) is torsion over \(\Lambda\), it has **no nonzero finite \(\Lambda\)-submodule**.

Algebraic rank-two bridge (fully proved in \`SELMER_BRIDGE_LEMMA.md\`):

\[
\mu(X)=0,\quad\lambda(X)\le2,\quad
\operatorname{rank}E(\mathbf Q)=2,\quad
E(\mathbf Q)[p]=0,\quad
X_{\rm finite}=0
\quad\Longrightarrow\quad
X\simeq\mathbf Z_p^2,\ T|_X=0,\ \Sha(E/\mathbf Q)[p^\infty]=0.
\]

The final implication relies on the injective restriction map
\(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)\to
\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\Gamma\).
The kernel vanishes because \(\Gamma\) is pro-p and
\(E(\mathbf Q)[p]=0\) implies \(E(\mathbf Q_\infty)[p]=0\).

## 3. Conclusions to record, with evidence levels

**A. 3-primary component.** User-supplied complete Magma \`ThreeSelmerGroup(E)\` transcript returns \(\operatorname{Sel}_3(E/\mathbf Q)\simeq(\mathbf Z/3)^2\). Given the already independently certified rank-two Mordell–Weil group, the Kummer sequence shows \(\Sha[3^\infty]=0\). The exact run was performed by the user; external rerun remains recommended.

**B. Good ordinary primes.** All 297 primes in the original CSV \`data/ordinary_p2_5_to_1999.csv\` have \(C_{p,0}=C_{p,1}=0\) and \(C_p\ne0\bmod p\), with exact p² sums recorded. This is a finite, reproducible source computation, **not a uniform theorem for p>1999**. The independent sample \`5,7,11,13,17,89,997,1721,1999\` was recomputed directly in this conversation; the whole 297-prime source sweep is separately rerunnable. When that computation is authenticated, Wuthrich–Greenberg and the exact Néron table give \(\Sha(E/\mathbf Q)[p^\infty]=0\) for each such p.

**C. Split multiplicative p=389.** Independent Python and native C++ verified the complete level-389² Fourier–Manin sum, first coefficients
\((0,0,0,321,102,102)\bmod389\), and the 388 exact \(U_{389}\)-distribution identities. Its leading coefficient 321 is a unit. The full-character trivial component gives \(\lambda(L_{389})=3\). Wuthrich's extra factor T forces \(\lambda(X_{389})\le2\); Greenberg 4.15(ii) excludes finite submodules; rank two fills the Selmer. Consequently

\[
\boxed{\Sha(E/\mathbf Q)[389^\infty]=0}
\]

under the source-identified p-adic measure convention; this conclusion does not assume BSD or the Iwasawa main conjecture. Independent publication-level source and tool review remain advised.

**D. Not yet settled by this finite-cyclotomic method.** p=2 needs the separate descent certificate independently audited. The good supersingular primes \(107,599,1049\) require signed methods. No finite sweep for \(p<2000\) controls the infinitely many \(p\ge2000\). Finally, the **exact complex leading-term identity**
\(L''(E,1)/2=\Omega_E^{\rm BSD}\operatorname{Reg}(E)\)
does not follow from these p-adic Selmer computations.

## 4. Independent external cross-checks

- [Sage elliptic curve modular symbols](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html).
- [Sage p-adic L-series; 389a example, p=5, T² coefficient 4](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html).
- [LMFDB 389.a1 underlying invariants and real period](https://www.lmfdb.org/EllipticCurve/Q/data/389.a1).
- [Wuthrich, Corollary 19](https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-19/12.pdf).
- [Greenberg, Proposition 4.15(ii)](https://arxiv.org/pdf/math/9809206).

### Explicitly prohibited inference

\[
(\forall\,p<2000\text{ in the tested ordinary set},\,\Sha[p^\infty]=0)
\not\Longrightarrow
\Sha(E/\mathbf Q)=0.
\]

Nor does \(\Sha[p^\infty]=0\) at a fixed p imply the exact *complex* BSD leading-term formula.

## Working code

\`verification/bsd389_period_convention_audit.py\` reads the **byte-exact unmodified CSV** (the initial repository import accidentally included text-extraction header lines and indices; this was corrected, with Git blob SHA equal to the original). It checks all 297 entries for the unit factor, the Sage p=5 value, and the p=389 factor-2 adjustment.
