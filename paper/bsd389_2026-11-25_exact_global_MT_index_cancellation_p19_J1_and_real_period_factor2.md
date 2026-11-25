# 389a1 — an exact global Mazur–Tate conductor-index cancellation, a full p19 reduction-lattice certificate, and the origin of the factor TWO

**25 November 2026.** MATHEMATICAL STATUS:
- **PROVED UNCONDITIONALLY:** general lattice-index/cokernel cancellation, exact actual p19 complete reduction-surjectivity \(J_S=1\), honest integral basis of the true Mazur–Tate restricted lattice, its determinant \(8,548,841\), and change-of-lattice factor \(23,681\).
- **SOURCE-LEVEL NORMALIZATION:** real-period doubling between the least positive real period used by Sage/eclib positive modular symbols and the full BSD real period of Burns–Kurihara–Sano, because the discriminant is **+389** and \(E(\mathbf R)\) has 2 connected components.
- **CONDITIONAL HEIGHT NUMERICS:** \(\det\mathscr H\equiv3\bmod19\) depends on the claimed local tame Néron/Poincaré-to-Tate monodromy identification. The cited Robert finite-field pairing theorem alone does not prove that IDENTIFICATION of Tan's local tame splitting with this monodromy; this remains a source-level geometric verification obligation. One must NOT claim a second independent original Mazur–Tate height computation.
- **NOT PROVED:** global Kato-to-Mazur–Tate leading-term identity, all-large-p Sha triviality, exact complex BSD. The BKS leading-term formula explicitly includes Sha and is conjectural at rank two.

## 1. New exact universal rank-two index cancellation theorem

Let E/Q be a torsion-free rank-two elliptic curve with two good distinct auxiliary primes q1,q2 for which:
\[
A_i:=E(\mathbf F_{q_i}),\quad |A_i|=p M_i,\quad p\nmid M_i,\qquad
\lambda:E(\mathbf Q)/p\xrightarrow{\sim} A_1/pA_1\oplus A_2/pA_2.
\]
Let \(M=E(\mathbf Q)=\mathbf Z^2\), \(\rho:M\to A=A_1\oplus A_2\), \(L=\ker\rho=E_S(\mathbf Q)\), \(H=\operatorname{im}\rho\), and \(J_S=|A/H|\). Let \(G\) be a cyclic order-p quotient of the tame ray class group, and
\[
h_S:M\otimes\mathbf Z_p\times L\otimes\mathbf Z_p\to I(G)/I(G)^2\simeq\mathbf F_p\,T
\]
be the ACTUAL Mazur–Tate biextension height. The restriction gives \(L\otimes\mathbf Z_p=p(M\otimes\mathbf Z_p)\). Define the honest divided height
\[
\mathscr H(x,y)=h_S(x,p y)
\]
on \(M/pM\), with matrix \(\mathscr H_{ij}\) in the basis P,Q.

**THEOREM (exact conductor-index cancellation):**
\[
\boxed{J_S\operatorname{Reg}_S^{\rm MT}
=\pm M_1M_2\det(\mathscr H)\; T^2
\quad\text{in }I(G)^2/I(G)^3\simeq\mathbf F_p\,T^2.}
\tag{1}
\]
The orientation sign is fixed to + by compatible orientations of the bases. This theorem uses only the genuine biextension height's bilinearity, group orders and lattice index; it does **not** require Sha finiteness, any Kato element or any BSD conjecture.

**Proof.** The p-primary component of H equals the entire A[p∞], which is \((\mathbf Z/p)^2\) by the hypothesis on λ. Hence \(|H|=p^2 h\) for some positive integer \(h\mid M_1M_2\), and
\[
J_S=\frac{p^2M_1M_2}{p^2 h}=\frac{M_1M_2}{h}.
\]
The index of L in M is \(|H|=p^2h\). Choose any oriented integral basis \(b_1,b_2\) for L, and write it in the original P,Q basis as the columns of an integer matrix B with determinant \(+p^2h\). Since \(L\otimes\mathbf Z_p=pM_p\), the matrix \(A=B/p\in\mathrm{GL}_2(\mathbf Z_p)\) is integral over \(\mathbf Z_p\), with determinant \(h\). By the bilinearity of the actual Mazur–Tate height and its extension to \(\mathbf Z_p\), its regulator matrix on P,Q versus \(b_1,b_2\) is exactly \(\mathscr H A\), and so
\(\operatorname{Reg}^{MT}_S=h\det(\mathscr H)T^2\).
Multiply by \(J_S=M_1M_2/h\); h cancels EXACTLY, proving (1).

**Additional consequence:** there is no independent or mysterious prime-to-p reduction-cokernel factor in the fully correct BKS product \(J_S\operatorname{Reg}_S\); the conductor factor is **precisely \((\#A_1/p)(\#A_2/p)\)** times the divided-height discriminant. DO NOT drop either J_S or the lattice index separately.

## 2. Complete, independently verified p=19 finite-field arithmetic

E=389a1: \(y^2+y=x^3+x^2-2x\); P=(-1,1), Q=(0,-1). Take q1=2243 and q2=3877. Actual finite groups:
\[
\#E(\mathbf F_{2243})=2261=19\cdot119,\quad
\#E(\mathbf F_{3877})=3781=19\cdot199.
\]
Both orders are squarefree, so the groups are cyclic. Direct group-law verification proves that \(G_1=(2,883)\) has order2261 and \(G_2=(0,0)\) has order3781. Exhaustive independently recomputed discrete logarithms are
\[
\begin{array}{c|rr}
&\log P&\log Q\\\hline
E(\mathbf F_{2243})\simeq\mathbf Z/2261 &2144&2163\\
E(\mathbf F_{3877})\simeq\mathbf Z/3781 &3439&3780
\end{array}
\]
Thus the reduction map M=Z²→Z/2261⊕Z/3781 is given EXACTLY by
\[
(a,b)\mapsto (2144a+2163b,\ 3439a+3780b).
\]

**THEOREM (true p19 cokernel).** The gcd of the six 2×2 minors of
\[
\begin{pmatrix}
2261&0&2144&2163\\
0&3781&3439&3780
\end{pmatrix}
\]
is 1. Consequently the MW reduction map is SURJECTIVE onto the ENTIRE product of finite groups (not only its 19-part), and
\[
\boxed{J_S=1.}
\]
A genuine oriented integral basis of the full restricted lattice \(L=E_S(\mathbf Q)\) is
\[
\boxed{b_1=1995P+2071Q,\qquad b_2=-2261P+1938Q.}
\]
Both satisfy both exact reduction congruences; their determinant equals
\[
1995\cdot1938+2261\cdot2071
=\boxed{8,548,841}=2261\cdot3781.
\]
Since the image has this order and the basis generates a sublattice of exactly this index, it is a basis of the COMPLETE actual L, not a merely computational sublattice.

The mandatory p-adic basis-change factor is
\[
h=\frac{8,548,841}{19^2}=\boxed{23,681}=119\cdot199,
\qquad h\bmod19=7.
\]
This p19 data was computed independently via exact group law and integer-gcd arithmetic in the model runtime; the companion verification script is available and fast.

## 3. Height determinant and precise p19 comparison of the normalized coefficients

Independently computed p19 reduced Tate weights are \(w_{2243}=17,\ w_{3877}=18\), with MW local rows (1,1), (0,1). Assuming the **previously claimed** tame Néron/Poincaré-to-finite-Tate monodromy comparison
\[
H_q=\varepsilon\,M_q^{-1}\mathcal B_q
\]
(with the common sign ε cancelling in rank2), the divided height matrix is
\[
\mathscr H=\varepsilon\begin{pmatrix}11&11\\11&13\end{pmatrix}\bmod19,\qquad
\det\mathscr H=\boxed{3}\bmod19.
\]
Theorem (1) with J_S=1 then yields
\[
\boxed{\operatorname{Reg}^{MT}_S
=23,681\cdot3
\equiv\boxed{2}\pmod{19}.}
\tag{2}
\]
**Important:** equation (2) is conditional on the exact q-adic tame splitting comparison, which has NOT been separately tested by direct computation of the original Mazur–Tate biextension height. Robert's Cor.3.12 alone states finite-field monodromy=Tate, not the q-adic-to-finite-field comparison. This is an integrity gate before labeling equation (2) a source-independent full MT computation.

The genuine modular-symbol theta quadratic coefficient, independently computed by the complete 4,344,996-representative Hecke/Manin sum, is
\[
c_2^{\mathrm{project}}\equiv\boxed4\bmod19.
\]

## 4. The factor TWO: not a mysterious Kato global scalar, but a real-period NORMALIZATION

E389a1 has minimal discriminant **+389**, so \(E(\mathbf R)\) has TWO connected components. Write \(\Omega_{\mathrm{prim}}^+\) for the *least positive real period* of the Néron differential and \(\Omega_{\rm BSD}=2\Omega_{\mathrm{prim}}^+\) for the complete BSD real period. From LMFDB,
\[
\Omega_{\rm BSD}=4.9804251217101101506427155839\ldots
\]
and hence \(\Omega_{\mathrm{prim}}^+=2.4902125608550550753\ldots\).

The documented Sage/eclib plus modular symbol is normalized by \(\Omega_{\mathrm{prim}}^+\). Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur–Tate Conjecture*, §2.1, defines \(\Omega^+=c_\infty\int_\gamma\omega\) with \(c_\infty=2\) for E389a1; their paper also notes that its \(\Omega^+\) is twice the period used in the **original** Mazur–Tate convention. Thus, with the same modular parametrization and the Gauss-factor convention,
\[
\frac{\int f}{\Omega_{\mathrm{prim}}^+}
=2\frac{\int f}{\Omega_{\rm BSD}}.
\]
For a cyclic order-p character \(\chi\) ramified at both auxiliary q1,q2, every nontrivial character of the chosen quotient has the same primitive conductor q1q2. The trivial character has theta value zero because \(L(E,1)=0\). Interpolation at ALL characters therefore identifies the project plus-symbol theta and the BKS full-real-period theta by
\[
\boxed{\Theta_{\mathrm{project}}=2\,\Theta_{\mathrm{BKS}}}
\tag{3}
\]
with compatible character/primitive-root conventions. This is a period-normalization identity, NOT BSD. If the source 390-Manin integer table was rescaled after its original eclib generation, that change must be checked before declaring (3) an identity for the frozen table bytes.

Consequently the true p19 projected quadratic coefficient 4 corresponds to a BKS-normalized coefficient
\[
\boxed{c_2^{\rm BKS}\equiv 2\bmod19.}
\]

**Comparison:** equations (2),(3) show that the BKS-normalized p19 coefficient and the *conditionally computed genuine MT regulator* agree modulo19, both equal 2. This is precisely what the Mazur–Tate rank-two leading-term conjecture predicts when \(\Sha(E/\mathbf Q)[19^\infty]=0\), an arithmetical vanishing that the project's independent Bullach–Honnor Fitting gate has already certified at p19. IT IS NOT a proof of the conjecture for any unbounded family of p.

## 5. New exact reformulation of the global conjecture, with Sha factor visible

BKS §2.2, equation (8), writes the rank-two Mazur–Tate leading term (in its ORIGINAL MT normalization) as a CONJECTURE
\[
\Theta_{\mathrm{MT},S}
\overset?=(-1)^{\nu(m)}\,\#\Sha(E/\mathbf Q)\,
J_S\operatorname{Reg}^{MT}_S
\quad \text{in }I^2/I^3
\]
when Sha finite. For m=q1q2, ν(m)=2 so the sign is +.

Our new **unconditional** algebraic identity (1) turns the *right side* into
\[
\boxed{\Theta_{\mathrm{MT},S}
\overset?=\#\Sha(E/\mathbf Q)\,
M_1M_2\det\mathscr H\pmod p,}
\tag{4}
\]
before any choice of plus-period normalization. With the project's factor-2 period convention this becomes
\[
\boxed{\delta^{\mathrm{project}}_{q_1q_2}
\overset?=2\,\#\Sha(E/\mathbf Q)\,
M_1M_2\det\mathscr H\pmod p.}
\tag{5}
\]
If Sha is nonfinite, (4)–(5) cannot be asserted or even read literally as statements involving \(\#\Sha\); one must use a derived Selmer determinant/Fitting replacement.

Thus the globally fixed experimental scalar TWO in p5/7/11/13/17/19 has a **precise natural explanation via real-period conventions**. It is *NOT* an independently established arithmetic unit that can be used to kill Sha across all large p: the actual BSD/Mazur–Tate conjecture includes a factor \(\#\Sha\), and its rank-two proof remains the essential obstacle.

This observation prevents a dangerous mistake: claiming the 138 congruences themselves constitute a uniform Kato-to-regulator theorem would simply delete the unknown Sha factor from equation (5).

## 6. Source links and strict verification boundary

1. BKS 2025, §2.1 period definition and factor-of-two note, §2.2 original Mazur–Tate equation (8): https://arxiv.org/pdf/2103.11535 .
2. Sage plus modular-symbol normalization by least positive real period: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html .
3. LMFDB 389a1 period, discriminant, Tamagawa: https://www.lmfdb.org/EllipticCurve/Q/389a1/ .
4. Tan 1995 finite tame biextension height definition and q-local splitting: https://www.numdam.org/article/AIF_1995__45_2_317_0.pdf .
5. Robert 2024 Cor.3.12 finite-field monodromy and Tate pairing: https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/articles/biextensions.pdf .

**Final status:** a NEW exact global regulator-index theorem and an independent true p19 MW-lattice computation. The factor-two normalization is located in the periods, subject to confirming the frozen Manin normalization. The entire Kato-to-regulator leading term and uniform Sha vanishing remain unproved; the previous full tame local splitting comparison is not independently audited by a direct height computation, so its numerical determinant should NOT be reported as such.
