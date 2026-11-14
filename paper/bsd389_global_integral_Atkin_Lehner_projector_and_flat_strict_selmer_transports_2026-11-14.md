# E389a1 — an actual p-independent integral modular projector, flat pairwise strict-Selmer transports, and the precise missing annihilator

**2026-11-14. Status:** an exact geometric construction (based on Stein's published decomposition and the already archived modular degree 40), a new general elementary finite-level Selmer-transport lemma, and a proof that their *mere existence* cannot force the missing all-large-p \(\Sha\) vanishing. These are **not** a BSD proof or a nonzero common integral Fitting element.

## 1. The genuinely global p-independent projector

Let
$$
E:y^2+y=x^3+x^2-2x,\quad N=389,\quad J=J_0(389),\quad
J^-=\operatorname{im}(1-w_{389})\subseteq J.
$$
William A. Stein, *The unusual Hecke algebra of \(X_0(389)\)* (1999), established
$$
J^-\sim_{\mathbf Q} E\times A_{20},
\qquad L(A_{20},1)\ne0,
$$
where \(A_{20}\) is a simple modular abelian variety of dimension 20. Primary HTML: https://wstein.org/Tables/389/389/node1.html .

Let \(\alpha:J^-\to E\) be the restriction of the optimal modular quotient and \(\beta:E\to J^-\) the dual embedding. The actual modular degree is 40, independently recorded by LMFDB https://www.lmfdb.org/EllipticCurve/Q/389a1/ , and the maps satisfy
$$
\boxed{\alpha\circ\beta=[40].}\tag{1}
$$

**Theorem A (an exact, constructed, p-independent geometric object).** Over the coefficient ring \(\mathbf Z[1/40]\) the endomorphism
$$
\boxed{e_E=\frac{\beta\circ\alpha}{40}\in
\operatorname{End}_{\mathbf Q}(J^-)\otimes_{\mathbf Z}\mathbf Z[1/40]}
\tag{2}
$$
is idempotent:
$$e_E^2=\frac{\beta\alpha\beta\alpha}{40^2}
=\frac{\beta[40]\alpha}{40^2}=e_E.$$
Its image on rational Tate modules is exactly the \(E\)-isotypic subspace, and the complementary image is the \(A_{20}\)-isotypic subspace.

For **every** p≥7, including p=389, 40 is a unit in \(\mathbf Z_p\). The same idempotent therefore acts integrally on \(T_p(J^-)\), on the natural \(p\)-power Selmer groups, and on their Tate–Shafarevich quotients. This is a common geometric morphism, *not a separately chosen p-local determinant*.

Put \(B^-=\ker(\alpha)^0\); it is \(\mathbf Q\)-isogenous to \(A_{20}\). The addition map
$$
\Phi:E\times B^-\to J^-,\qquad(P,b)\mapsto\beta(P)+b
$$
is an isogeny. Every point in \(\ker\Phi\) has its first coordinate in \(E[40]\), so
$$
\boxed{\deg\Phi\mid 40^2=1600.}\tag{3}
$$
Thus for **all p≥7** the map is a p-prime isogeny, so it induces isomorphisms preserving the finite Kummer local conditions,
$$
\boxed{
\operatorname{Sel}_{p^\infty}(J^-/\mathbf Q)
\cong\operatorname{Sel}_{p^\infty}(E/\mathbf Q)
\oplus\operatorname{Sel}_{p^\infty}(B^-/\mathbf Q),}
\tag{4}
$$
$$
\boxed{
\Sha(J^-/\mathbf Q)[p^\infty]
\cong\Sha(E/\mathbf Q)[p^\infty]
\oplus\Sha(B^-/\mathbf Q)[p^\infty].}
\tag{5}
$$
The first summand is specifically the image of \(e_E\), and the second the kernel of \(e_E\).

Since \(L(A_{20},1)\ne0\), the classical rank-zero theorem of Kolyvagin–Logachev implies \(A_{20}(\mathbf Q)\) finite and \(\Sha(A_{20}/\mathbf Q)\) finite. This passes through isogeny to \(B^-\). Secondary HTML source: https://mathe2.uni-bayreuth.de/stoll/papers/covers8.pdf (Corollary 6.3, note its source is a PDF; the complete proof belongs to the published theorem).

Consequently there is a **genuine fixed but currently not calculated** integer
$$
D_B=\#\Sha(B^-/\mathbf Q)\in\mathbf Z_{>0}
$$
such that, for all p≥7 with p∤D_B,
$$
\Sha(J^-/\mathbf Q)[p^\infty]\cong\Sha(E/\mathbf Q)[p^\infty].
\tag{6}
$$

**Crucial limitation:** Equations (2)–(6) isolate the E component; they do not annihilate it. \(\Sha(E)\) is not a quotient of the *finite* \(\Sha(B^-)\), and there is no injection from the unknown E torsion to that rank-zero complement. Indeed finiteness of \(\Sha(J^-)\) is equivalent, not an implication already proved, to finiteness of \(\Sha(E)\). A nontrivial p-Sha may lie entirely in the *image* of e_E, with no congruence to \(B^-\).

This sharpens the earlier rank-two Atkin–Lehner reduction in the research branch by identifying the **explicit p-independent idempotent on the actual p-primary Selmer objects**. It does not import that earlier reduction as a proof of BSD.

## 2. Finite-level strict Selmer projectors at arbitrary p^k

Fix a prime p and k≥1, set \(R=\mathbf Z/p^k\mathbf Z\),
$$
S=\operatorname{Sel}_{p^k}(E/\mathbf Q),\qquad
M=E(\mathbf Q)/p^kE(\mathbf Q)\cong R^2.
$$
The global Kummer exact sequence is
$$0\to M\xrightarrow{\iota}S\to\Sha(E/\mathbf Q)[p^k]\to0.$$

For a pair \(I=\{q,r\}\) of good auxiliary primes, suppose its two finite Kummer local conditions are **free rank-one \(R\)-modules**, \(L_q\oplus L_r\cong R^2\), and the MW localization
$$
A_I:=\lambda_I\circ\iota:M\xrightarrow{\sim}L_q\oplus L_r
$$
is invertible over \(R\) (equivalently, its determinant is a unit modulo p).

**Theorem B (strict-Selmer projection, unconditional on Sha vanishing).**
The map
$$
\boxed{e_I:=\operatorname{id}_S-\iota A_I^{-1}\lambda_I}
\tag{7}
$$
is an \(R\)-linear idempotent, with
$$
\boxed{\ker e_I=\iota(M),\quad
\operatorname{im}e_I=\ker\lambda_I=K_I,\quad
K_I\xrightarrow{\sim}\Sha(E/\mathbf Q)[p^k].}
\tag{8}
$$

**Proof.** Set \(f_I=A_I^{-1}\lambda_I:S\to M\). Then \(f_I\iota=\operatorname{id}_M\). Therefore \(e_I=\operatorname{id}-\iota f_I\) is a projection with kernel \(\iota(M)\). Further \(\lambda_I e_I=\lambda_I-A_I f_I=0\), and \(e_I\) is the identity on \(\ker\lambda_I\). Hence \(\operatorname{im}e_I=K_I\). By Kummer, \(S/\iota(M)\cong\Sha[p^k]\); \(e_I\) identifies this quotient with \(K_I\). QED.

This theorem **does not** require an a priori splitting of the finite-level Kummer extension (7) constructs one under its two-local MW-unit hypothesis. Nor does it require \(\Sha[p^k]\) to be finite as an independent assumption: finite-level Selmer makes it finite.

## 3. A genuinely global-in-the-pair flat transport law

Suppose \(I,J,K\) are three arbitrary qualifying auxiliary pairs for the *same p^k*, with associated strict kernels \(K_I,K_J,K_K\).

**Theorem C (pairwise transport and zero holonomy).**
$$
\boxed{e_Ie_J=e_I,\qquad e_Je_I=e_J.}\tag{9}
$$
The restricted transition
$$
T_{J\leftarrow I}:=e_J|_{K_I}:K_I\xrightarrow{\sim}K_J
$$
is an isomorphism with inverse \(T_{I\leftarrow J}\), and for every third pair
$$
\boxed{T_{K\leftarrow J}\circ T_{J\leftarrow I}
=T_{K\leftarrow I}.}\tag{10}
$$

**Proof.** For arbitrary s∈S,
\(e_Ie_J(s)=e_I(s-\iota f_J(s))=e_I(s)\)
since \(e_I\iota=0\). Interchanging I,J gives the other absorption identity. Hence on K_I,
\(e_Ie_J=\operatorname{id}\),
so the restricted maps are mutually inverse. The cocycle relation is the same absorption identity. QED.

Moreover
$$
\boxed{e_I-e_J=\iota(f_J-f_I),}
\tag{11}
$$
so every difference between strict-Selmer projectors factors **entirely through the known MW module**. On the common quotient \(S/M=\Sha[p^k]\), all such projectors induce the same identity.

Thus a product of these canonical transition maps around ANY loop has **identity holonomy**. Varying the auxiliary pair changes only the choice of complementary representative of each Sha class, not the abstract arithmetic obstruction.

## 4. Sharp countermodel to “stacking many pairs kills Sha”

The underlying Selmer decomposition can have nonzero paired torsion even when two distinct strict kernels intersect only at zero:

Take \(R=\mathbf Z/p^k\), \(1\le a\le k\), \(T=(\mathbf Z/p^a)^2\) with its perfect alternating pairing and \(S=R^2\oplus T\), \(M=R^2\). Let \(c=p^{k-a}\) and interpret \(c\,t\in R^2\) from a representative of t (well-defined independently of representative). Define two synthetic localizations
$$
\lambda_I(x,t)=x,\qquad
\lambda_J(x,t)=x+c\,t.
$$
Both restrict to the identity on M and satisfy all algebraic rank-one local conditions. Then
$$
K_I=\{(0,t):t\in T\},\quad
K_J=\{(-c\,t,t):t\in T\},
\quad
\boxed{K_I\cap K_J=0\quad\text{but}\quad K_I\cong K_J\cong T\ne0.}
\tag{12}
$$
Therefore **trivial intersection of strict Selmer kernels for several auxiliary pairs does not imply individual strict Selmer vanishing**, and product/transport identities give no finite p-support annihilator.

The modules in (12) are explicitly labelled *synthetic*. They are not claims that E389a1 has nonzero Sha at any p.

## 5. Exact tests and decisive arithmetic boundary

[Verification source](../verification/bsd389_integral_projector_strict_transports_audit.py) checks:
- 21-dimensional exact rational matrix model with αβ=40 and \(e^2=e\);
- 16 finite-ring configurations across p=5,7,11,107 and depths k=1,2,3;
- exact historical actual two-by-two MW matrices as the initial local blocks (the other pair local blocks are **toy**, not actual E);
- idempotency, all absorption laws, flat transports, and zero pairwise intersections with paired torsion.

It was executed locally in the assistant's container on November 14, 2026, with all tests passing. Local file SHA256:
5b3832e951be23b401f3b9fc89c97c1b31ac6a8cddc6b7ffdb253f4e86acf690.

**The still-missing decisive arithmetic comparison:** construct, independently of Sha and with a proof of compatibility at all good p outside a fixed finite S, an **actual injection**
$$
\Sha(E/\mathbf Q)[p^\infty]^\vee
\hookrightarrow
\operatorname{coker}\left(
A_{\mathbf Z}\otimes\mathbf Z_p\right)
$$
for some **fixed** square integral matrix \(A_{\mathbf Z}\) with \(\det A_{\mathbf Z}\ne0\), or an equivalent uniform integral Selmer-complex Fitting comparison.

Such a construction would give a true fixed integer \(D=\det A_{\mathbf Z}\) annihilating all those primary Sha groups, hence no prime support outside the prime divisors of D (exceptions require separate Sha-finiteness controls). But neither e_E in (2) nor e_I in (7) provides such a map: the former projects onto the unknown E torsion, and the latter merely identifies its p^k-torsion with strict kernels in different coordinates.

**Verdict:** a real prime-independent modular projector and exact all-depth strict-Selmer transport theorem are constructed; a second potential shortcut through pair stacking is rigorously excluded. The uniform annihilator and the exact complex BSD leading term remain unproved.
