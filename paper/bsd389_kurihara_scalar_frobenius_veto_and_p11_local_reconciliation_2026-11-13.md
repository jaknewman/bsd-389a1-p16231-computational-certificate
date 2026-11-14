# E389a1 — scalar-Frobenius veto for unit two-prime Kurihara numbers; exact p11 local reconciliation

Date 2026-11-13. **Proved using published Kim 1.8 and 1.10 plus Kummer:** the veto theorem below. **Executed independently:** exact p11 finite-field Kummer matrix and normalization. **2026-11-14 execution update:** the independent full p11 Kurihara sum **was executed by the user on Ubuntu Sage** and returned delta=1 mod11, with all 392040 units checked and full-vs-half-sum PASS. See [authenticated stdout transcription](../results/bsd389_p11_kurihara_397x991_FULL_USER_PASS_2026-11-14.md). The present note originally predates the actual run. No uniform Sha or strong BSD claim.

## A. Scalar-Frobenius veto (theorem)

Let E: y²+y=x³+x²−2x, conductor 389, Mordell–Weil rank exactly 2, torsion 0, Tamagawa product 1. Fix p≥5 satisfying all the hypotheses of Chan-Ho Kim, *The Structure of Selmer Groups...*, Theorems 1.8 and 1.10: surjective residual representation, p-unit Manin constant, E(Q_p)[p]=0, and p-unit Tamagawa factors. Reference: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf (printed pp. 6–8).

Let q1,q2 be distinct good p-admissible primes (q≡1, a_q≡2 modp) and delta_tilde their correctly period-normalized two-prime Kurihara number, with modulus I_n=I_q1+I_q2, **not the product**.

**Theorem:**
$$
\widetilde\delta_{q_1q_2}\ne0\pmod p
\ \Longrightarrow\
\rho_{E,p}(\mathrm{Frob}_{q_i})
\sim\begin{pmatrix}1&1\\0&1\end{pmatrix}\quad(i=1,2).
\tag{1}
$$
So if any q has **scalar identity Frobenius** on E[p] then its two-factor delta is necessarily zero modulo p.

**Proof.** A unit degree-two delta forces the minimal Kurihara degree to equal 2 because Kummer gives Sel_{p∞} corank≥2. Kim 1.8 then gives corankSel=2 and, since the two-prime unit yields partial^(2)=partial^(∞)=0, no finite nondivisible Selmer quotient. Thus Sel_{p∞}≅(Q_p/Z_p)^2 and Sha[p∞]=0 by the saturated MW Kummer injection. In particular dim_Fp Sel(E[p])=2. Kim 1.10 gives an isomorphism
$$
\mathrm{Sel}(E[p])\simeq
E(\mathbf F_{q_1})/p\oplus E(\mathbf F_{q_2})/p.
$$
Both local spaces have positive dimension by p-admissibility, and their sum is dimension 2, so each is dimension 1. On E[p], admissible Frobenius has characteristic polynomial (X−1)², so a 1D fixed space forces the **nonidentity unipotent** class. QED.

The converse is not asserted: both unipotent types and a unit MW local determinant do NOT alone imply a unit delta.

**Independent explanation for an old zero:** at p=7, E(F281)[7] has two independent 7-torsion generators R=(20,74), S=(22,61), hence Frob_281=I. Thus theorem (1) forces delta_tilde_(113·281)=0 mod7, confirming the previously archived exact Sage/eclib zero without redoing its large sum. The other pair 113·673 has only 1D local Kummer spaces and archived delta=2 mod7.

## B. Fully executed p11 exact local arithmetic

Take p=11, q1=397, q2=991, P=(−1,1), Q=(0,−1). Exact finite-field Legendre counts give
$$
a_{397}=24,\ #E(\mathbf F_{397})=374=11\cdot34,
\qquad
a_{991}=-53,\ #E(\mathbf F_{991})=1045=11\cdot95.
$$
Both primes are 11-admissible, and both local mod11 Kummer spaces are 1D (group order valuation one).
The genuine pointwise group law gives
$$
34P=(217,30),\quad34Q=(217,366)=-34P\pmod{397},
$$
$$
95P=(68,61),\quad95Q=(744,857)=7(95P)\pmod{991}.
$$
Therefore
$$
\boxed{A_{11}=\begin{pmatrix}1&10\\1&7\end{pmatrix},
\quad\det A_{11}=8\pmod{11}.}\tag{2}
$$
This was independently executed as a standard-library Python program; no Sage and no Sha inference from local data alone. Also I_397=(22)Z11, I_991=(55)Z11, hence I_n=11Z11.

## C. Complete normalization reconciliation

Independent external p11 research source:
https://amral.evemisslab.com/en/bsd/papers/kurihara-389a1/
reported local matrix A'=[[1,2],[1,4]], det 2, using rational generators P'=(0,0), Q'=(1,0). These are related **over Q** by
$$P'=-Q,\qquad Q'=P-Q.$$
The exact basis matrix is
$$B=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\quad\det B=1.$$
The finite-field change of local generator at the second auxiliary is scaling by 3, and the complete identity is
$$
\boxed{
\begin{pmatrix}1&0\\0&3\end{pmatrix}
\begin{pmatrix}1&10\\1&7\end{pmatrix}
\begin{pmatrix}0&1\\-1&-1\end{pmatrix}
=\begin{pmatrix}1&2\\1&4\end{pmatrix}\pmod{11}.}\tag{3}
$$
Thus the external determinant 2 =3·8 mod11 matches all four entries exactly. This establishes normalization compatibility of *local* data; it does not certify any particular Kurihara coefficient.

The external source separately reports delta_tilde_(397·991) nonzero mod11 (the displayed coefficient 5 or 6 depends on primitive-root/period conventions), over phi(397·991)=392040 units. **Execution update (2026-11-14):** The user's genuine Sage/eclib 390-Manin full-sum run calculated **delta=1 mod11**, with moments [0,0,0,1], 392040 units and exact half/full sum agreement. The full transcript is [archived here](../results/bsd389_p11_kurihara_397x991_FULL_USER_PASS_2026-11-14.md). This is now a second, code-independent-of-Sage-p_primary_bound Kurihara–Kim route to Sha11 triviality, not a new all-prime bound.

Under verified full p11 delta nonvanishing and the theorem conditions (residual surjectivity, Manin 11-unit, E(Q11)[11]=0 since #E(F11)=16, Tamagawa=1), Kim 1.8/1.10 gives another proof of Sha[11∞]=0. That conclusion is separately known from the project's genuine user-run Sage p_primary_bound(11)=0; the present result supplies **new local and normalization evidence, not the first p11 proof**.

## D. Uniform limit

Theorem (1) removes scalar-Frobenius two-factor candidates **before** any expensive modular symbol sum and proves that a genuine two-prime unit also forces the MW local matrix determinant to be a unit. Yet there is no established theorem guaranteeing a unit δ at some pair for all large p. Strong BSD further requires exact complex leading term.

**Updated verdict (2026-11-14):** scalar-Frobenius veto proved under Kim's published hypotheses; p11 local arithmetic and full basis reconciliation independently executed; user-executed **full authentic p11 Kurihara coefficient=1 mod11 PASS**. Consequently Kim 1.8/1.10 proves p11 Kato primitivity, semilocal Selmer isomorphism and 11-adic Sha triviality, and yields the Iwasawa main conjecture in the theorem's formulation (see the complete hypothesis audit in the archived log note). No uniform Sha or full BSD proof.
