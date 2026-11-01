# Rank-two Mordell–Weil wedge: a genuine global integral candidate, but NOT a rank-two Euler system

**2026-11-01. Mathematical result and explicit proof-planning audit.**
For \(E=389a1:y^2+y=x^3+x^2-2x\), the already independently certified full free Mordell–Weil basis provides a simple and genuinely global integral **exterior-square element**. Its primitivity, however, is **not enough** to control the finite \(p\)-primary Tate–Shafarevich group. More subtly, the *Mordell–Weil rank 2* must not be confused with the *core rank* of a Mazur–Rubin Selmer structure; in the standard unramified structure for an elliptic Tate module over \(\mathbf Q\), the latter is **1**, under the paper's hypotheses.

This is a source-checked diagnostic, not the promised uniform determinant and not a proof of finite Sha.

## 1. A genuine integral object independent of Sha

The independently certified full Mordell–Weil basis in the earlier Sage project is
\[
P=(-1:1:1),\qquad Q=(0:-1:1),\qquad
E(\mathbf Q)/E(\mathbf Q)_{\mathrm{tors}}
=\mathbf ZP\oplus\mathbf ZQ.
\]
Check points exactly:
- \(P=(-1,1)\): \(y^2+y=2=(-1)^3+(-1)^2-2(-1)\);
- \(Q=(0,-1)\): \(y^2+y=0=0^3+0^2-2\cdot0\).

Define an integral, p-independent global line and element
\[
\mathcal L_{\mathrm{MW}}=\bigwedge\nolimits^2_{\mathbf Z}
 \bigl(E(\mathbf Q)/E(\mathbf Q)_{\mathrm{tors}}\bigr),
\qquad \omega_{\mathrm{MW}}=P\wedge Q.
\]
It is a free rank-one \(\mathbf Z\)-module with a chosen generator. For any *unimodular* change of full MW basis \((P',Q')=(P,Q)A\), \(A\in\mathrm{GL}_2(\mathbf Z)\),
\[
P'\wedge Q'=\det(A)(P\wedge Q)=\pm\omega_{\mathrm{MW}}.
\]
At every prime p, this element is automatically primitive in the **Mordell–Weil exterior lattice**
\[
\mathcal L_{\mathrm{MW}}\otimes\mathbf Z_p
=\mathbf Z_p\,\omega_{\mathrm{MW}}.
\]

This achieves an actual independent rational/integral *construction*, NOT a nonzero rational Selmer obstruction. No numerical p-primary computation was used to define it. Its primitivity relies on the historically certified **full basis**; the tiny pure-Python script below verifies rational-point equations but does **not** reproduce the basis saturation proof.

## 2. A rigorous proof that this primitive wedge alone cannot force Sha[p]=0

Fix any prime p and set \(R=\mathbf Z_p\). Consider the **synthetic** (not elliptic-curve-derived) Selmer-dual shape
\[
X_p^{\mathrm{toy}}
=R^2\oplus(R/pR)^2,
\]
with the free \(R^2\) carrying basis \(e_1,e_2\). Its exterior-square generator
\(e_1\wedge e_2\in\bigwedge^2R^2\) is primitive (coefficient exactly 1). Nevertheless
\[
\operatorname{Fitt}_{2,R}(X_p^{\mathrm{toy}})
=\operatorname{Fitt}_{0,R}\big((R/pR)^2\big)
=(p^2)\ne R .
\]
In fact, with presentation \(R^2\xrightarrow{D}R^4\to X_p^\mathrm{toy}\to0\) and
\[
D=
\begin{pmatrix}
0&0\\
0&0\\
p&0\\
0&p
\end{pmatrix},
\]
the 2×2 minors generate the ideal \(p^2R\) by inspection.

This toy module respects the paired-cyclic, square-order constraint of any **finite** odd-p Sha. Thus a primitive generator of the rank-two free part is **compatible with nonzero finite p-torsion**, and cannot by itself show \(\operatorname{Fitt}_2=R\). One needs a genuine arithmetic relation **between the exterior class and the torsion/cohomological obstruction**.

**This is not a counterexample to BSD or to the actual \(X_p\) of 389a1.** It only refutes the *proposed inference* from MW basis primitivity to Sha triviality.

An elementary script verifying the rational points and synthetic Fitting minors for any chosen primes is [\`verification/bsd389_mw_wedge_vs_fitt2_sanity.py\`](../verification/bsd389_mw_wedge_vs_fitt2_sanity.py). **Not yet user-executed** at the time of writing; no PASS is claimed in this note.

## 3. A subtle external-theorem check: MW rank ≠ Mazur–Rubin **core rank**

**Primary reference:** B. Mazur and K. Rubin, *Controlling Selmer groups in the higher core rank case*, Journal de théorie des nombres de Bordeaux **28** (2016), 145–183, [original preprint PDF, introduction p.2](https://www.math.uci.edu/~krubin/preprints/higherkolysys.pdf), [published record](https://jtnb.centre-mersenne.org/item/JTNB_2016__28_1_145_0/).

The authors explicitly distinguish arithmetic group rank from the **core rank** \(r(T,\mathcal F)\) of a chosen Selmer structure. For **their unramified initial Selmer conditions and stated hypotheses**, they state (introduction p.2) that
\[
r(T,\mathcal F_\mathrm{ur})=\sum_{v\mid\infty}\mathrm{corank}
H^0(G_{K_v},T^*),
\]
and for \(T=T_p(A)\), an abelian variety of dimension d over K,
\[
r(T_p(A),\mathcal F_\mathrm{ur})=d[K:\mathbf Q].
\]
For our elliptic curve over Q (\(d=1,K=\mathbf Q\)), **this gives core rank 1**, not the known MW rank 2.

**Important qualification:** This equality is for the specified Selmer setup and hypotheses in Mazur–Rubin, not a universal statement that any local condition on \(T_pE\) has core rank 1. A modified local condition may alter the core rank, but it may then control a *modified* Selmer group; the comparison back to the original Bloch–Kato p∞ Selmer and its \(Fitt_2\) must be proved, with every local correction and denominator included.

**Therefore** merely inserting the global \(\omega_{\mathrm{MW}}\) into the theory of 'higher core rank 2' is an **invalid theorem application** unless we:
1. Specify \(T_pE\), the chosen \(p\)-adic Selmer structure \(\mathcal F_p\), the local conditions and any exceptional p.
2. Compute/verify its **core rank** (which need not equal MW rank).
3. Produce a true Euler/Stark/Kolyvagin system with the **correct rank for that structure**, including auxiliary extension classes and compatibility/norm relations.
4. Identify its *derivative/Fitting comparison with the actual* \(X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\), not only with a relaxed/modified Selmer module.
5. Establish **uniform rational descent and integral p-primitivity** outside an explicit finite set by a global construction, not just by a separate p-adic result at each p.

## 4. Actual positive general theorem available (but not its missing arithmetic inputs)

- **Mazur–Rubin 2016** prove, under their conditions, that higher rank **Stark and Kolyvagin systems** control module structure of corresponding dual Selmer groups. This is a *machinery theorem*: it is not by itself the construction of the required special system from our fixed curve.
- **Burns–Sakamoto–Sano**, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, **accepted in Algebra & Number Theory, August 2025**: [institutional source](https://kclpure.kcl.ac.uk/portal/en/publications/on-the-theory-of-higher-rank-euler-kolyvagin-and-stark-systems-ii/). They prove existence of a canonical higher Kolyvagin derivative map from Euler systems over appropriate Gorenstein coefficient rings, with Selmer-structure control. This does **not** give a ready-made single global rank-two Euler system for \(E=389a1\) or a prime-independent integral comparison.
- **Mazur's own commentary** on higher rank [Euler systems](https://celebratio.org/Mazur_BC/article/1158/) explains why the **exterior power** is the natural geometric receptacle for an analytic rank-two leading term; it does not equate a wedge of existing rational points with an Euler-system class satisfying extension norm relations.

**Key conceptual distinction:** the algebraic \(P\wedge Q\) is known and globally primitive. The unknown is an *Euler-system special element* with appropriate extension norm relations **and a proven regulator/determinant comparison** to the bottom wedge that also detects the torsion in the Selmer complex. One cannot obtain this comparison simply by dividing any two nonzero elements in a one-dimensional rational space, because the integral divisibility and Selmer cohomological content are exactly what are missing.

## 4 bis. A second **concrete global arithmetic object**: the rational 389-cusp modular-symbol vector

Besides the global MW wedge, the curve's classical modular form gives a genuinely **p-independent rational modular-symbol map**
\[
m_E^+:\mathbf Q\to\mathbf Q,\qquad
r\longmapsto [r]^+_E
\]
normalized by the Néron real period. This is a **proven modularity/Manin–Drinfeld arithmetic object**, independent of Sha finiteness. The [Sage modular-symbol documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html) explains its rationality, normalization and the independently implemented \`sage\` and \`eclib\` oracles.

Choose the fixed 389 cusps \(a/389\) (\(0\le a<389\)); this is a **finite sample**, not a claim to contain all rational cusps or all 390 Manin–Shapiro relations. Put
\[
v_a=m_E^+(a/389),\qquad
D=\operatorname{lcm}_{0\le a<389}\operatorname{den}(v_a)>0,
\quad
g=\gcd_{a}(D v_a)>0.
\]
The vector \(V=(Dv_a)_a\in\mathbf Z^{389}\) is a **fixed integral vector**. A computable integer Bézout identity gives coefficients \(c_a\in\mathbf Z\) with
\[
\boxed{\sum_{a=0}^{388}c_a D\,m_E^+(a/389)=g.}
\]
Consequently, for every prime p **not dividing Dg**, at least one sample \(m_E^+(a/389)\) is a **p-adic unit**. This is an *exact uniform algebraic nonvanishing statement about modular symbols*, not a theorem about Selmer or Sha.

A new [Sage/eclib exact cross-oracle exporter](../verification/bsd389_fixed_rational_manin_content.py) calculates the 389 normalized rational values by **both independent symbol implementations**, checks every equality, computes exact D and g, constructs the Bézout witness and writes a SHA256-pinned canonical JSON. **It has not yet been executed by the user**, so D, g, nonzero count, and SHA are deliberately left unknown in this note. The resulting object is p-independent and genuinely derived from E. We must not assume that its content ideal is \(\operatorname{Fitt}_2\).

### Precise remaining bridge

The existence of the independent p-uniform symbol vector and an integral MW generator does NOT provide the missing class in a genuine rank-two Selmer complex. A successful further argument would have to **construct the relevant arithmetic Euler/Kolyvagin special element from those sources**, prove the correct field-extension norm relations and local Selmer conditions, compare its integral lattice to the actual \(Fitt_2(X_p)\), and then descend that comparison to ONE rational p-uniform scalar. This must not simply assert the existence of an Euler system whose *leading term* has the desired value.

---

## 5. Minimal constructive next goal, avoiding more gigantic prime scans

The next deliverable must be a fully specified candidate (not an abstract existence assertion):
\[
\mathfrak z_{\mathrm{arith}}\in
\bigcap^r_{\mathcal R}H^1_{\mathcal F}(\mathbf Q,T)
\quad\text{or a global motivic determinant line},
\]
together with its field-extension norm relations or explicit cohomological construction, and an independently verifiable comparison
\[
\text{derived Stark/Kolyvagin element}
\ \longrightarrow\
\operatorname{Fitt}_{2,\mathbf Z_p}(X_p).
\]
Here the correct **r and local Selmer structure** must be decided first, rather than presetting \(r=2\) from MW rank. A successful p-uniform global motivic comparison would be significant new mathematics and remains UNPROVED for 389a1 in our repository.

**In a single sentence:** We have explicitly **constructed** the canonical global **Mordell–Weil exterior generator**, but it is **not** the arithmetic Euler-system/zeta class needed for a Sha support bound. Its primitivity is true and insufficient. The core-rank audit removes a critical potential theorem mismatch.

**Two independent major BSD gaps remain:** uniform finiteness of all Sha-primary parts, and exact complex rank-two leading coefficient equality.

Tracking: [uniform support issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8), [complex strong BSD issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
