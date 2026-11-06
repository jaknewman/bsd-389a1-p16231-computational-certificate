# A TRUE global rank-two-only modular motive at level 389: the 21-dimensional Atkin–Lehner MINUS Jacobian

Date: 2026-11-06. This is a new, exact, p-UNIFORM arithmetic reduction using primary published sources, not another high-p GroSS/local certificate. It does NOT prove Sha(E) finite or the complex second-derivative BSD coefficient. The target now contains NO positive-rank modular complements.

## Sources and accepted data

E/Q is 389a1 with analytic and algebraic rank 2, torsion 1, optimal parametrization φ:X_0(389)→E of modular degree d=40. The associated normalized newform has global root number +1, so its Atkin–Lehner eigenvalue for weight two is w_389(f_E)=−1.

William Stein, *The Unusual Hecke Algebra of X_0(389)* (1999), introduction, proves:
- J=J_0(389) has genus/dimension 32 and decomposes up to Q-isogeny as A_1 × A_2 × A_3 × A_6 × A_20, where dim A_d=d and A_1=E.
- The Atkin–Lehner MINUS factor J^- has dimension 21 and Q-isogeny type
\[
\boxed{J_0(389)^-\ \sim_\mathbf Q\ E\times A_{20}.}\tag{1}
\]
- L(A_20,1)≠0.
Source: https://wstein.org/Tables/389/389/node1.html .

For the modular GL2-type abelian variety A_20 with nonzero central L-value, the Kolyvagin–Logachev rank-zero theorem establishes BOTH
\[
\boxed{\operatorname{rank}A_{20}(\mathbf Q)=0,
\qquad \Sha(A_{20}/\mathbf Q)\ \text{finite}.}\tag{2}
\]
This is not a claim about the full J, which has several other positive-rank factors. Rank-zero modular Sha finiteness is explicitly recorded, e.g. Michael Stoll, Algebra & Number Theory 1(4) (2007), Corollary 6.3, https://msp.org/ant/2007/1-4/ant-v1-n4-s.pdf .

The Agashe–Ribet–Stein congruence theorem for the optimal strong Weil elliptic curve implies its modular congruence number r_E differs from its modular degree by prime factors q with q²|N. Since N=389 is prime, r_E=40 EXACTLY: https://wstein.org/papers/ars-congruence/current.pdf . Hence the E eigensystem has no level-389 congruence with other forms at any p>=7. This is distinct from any claim that its Sha vanishes at those primes.

## Theorem 1: a fixed rank-zero-complement abelian subvariety and a uniformly bounded isogeny degree

Let w=w_389 be the Atkin–Lehner involution on J and define
\[
J^-=\operatorname{im}(1-w)=\ker(1+w)^0,
\quad \dim J^-=21.
\]
The optimal maps α=φ_*:J→E, β=φ^*:E→J obey αβ=[40] and β(E)⊂J^- (because w f_E=−f_E).

Put \(B^-=\ker(\alpha|_{J^-})^0\), the identity component of the kernel. By (1), \(\dim B^-=20\), and the non-E isotypic decomposition shows
\(B^-\sim_\mathbf Q A_{20}\).
It therefore has rank-zero rational points and finite Sha. (The latter are invariant under Q-isogeny.)

The fixed Q-homomorphism
\[
\Phi^-:E\times B^-\to J^-,
\qquad (P,b)\mapsto\beta(P)+b
\]
is a surjective Q-ISOGENY. Its geometric kernel is a subgroup of E[40]: indeed \(\Phi^-(P,b)=0\) implies b=−βP and αβP=[40]P=0. Therefore
\[
\boxed{\deg\Phi^-\mid40^2=1600=2^6 5^2.}\tag{3}
\]
It need NOT equal 1600, because \(B^-\) is the connected minus part of the full ker α. Claiming exact 1600 for Φ^- without checking component groups would be unjustified. The divisibility is all we need.

## Theorem 2: EXACT global Selmer and Sha splitting for EVERY p>=7

For every rational prime p∉{2,5}, \(\Phi^-\) has degree prime to p and so induces an isomorphism of p-divisible Galois representations preserving Kummer local conditions at EVERY place, including the bad conductor 389. Hence
\[
\boxed{
\operatorname{Sel}_{p^\infty}(J^-/\mathbf Q)
\simeq
\operatorname{Sel}_{p^\infty}(E/\mathbf Q)
\oplus
\operatorname{Sel}_{p^\infty}(B^-/\mathbf Q)
\quad(p\ne2,5),}\tag{4}
\]
and
\[
\boxed{
\Sha(J^-/\mathbf Q)[p^\infty]
\simeq
\Sha(E/\mathbf Q)[p^\infty]\oplus
\Sha(B^-/\mathbf Q)[p^\infty]
\quad(p\ne2,5).}\tag{5}
\]
This is a single universal theorem, NOT a statement checked p-by-p or based on congruences alone.

Let \(D_B=\#\Sha(B^-/\mathbf Q)\), a fixed PROVED-TO-EXIST positive integer, though not explicitly evaluated in this note.
For EVERY rational prime p∉{2,5} with p∤D_B,
\[
\boxed{\Sha(J^-/\mathbf Q)[p^\infty]
\simeq\Sha(E/\mathbf Q)[p^\infty].}\tag{6}
\]
Thus the two Sha groups agree outside ONE genuinely finite, p-INDEPENDENT set \(S=\{2,5\}\cup\{p:p\mid D_B\}\).

In particular, \(J^-(\mathbf Q)\) has **free rank EXACTLY 2** by the isogeny and (2). There are no unknown additional MW rank contributions, unlike on full J where A_2,A_3,A_6 have positive ranks.

## Theorem 3: GLOBAL full-Sha INJECTION, even at 2 and 5

The composite
\[
E\xrightarrow{\beta}J^-\xrightarrow{\alpha|_{J^-}}E
\]
is still [40]. Thus the kernel of \(\Sha(E)\to\Sha(J^-)\) is annihilated by 40 for the ENTIRE group. The project's ALREADY authenticated, not rerun, 2-Selmer and p=5 Kato/Kurihara certificates establish
\(\Sha(E)[2^\infty]=\Sha(E)[5^\infty]=0\).
Hence
\[
\boxed{
\Sha(E/\mathbf Q)\hookrightarrow\Sha(J^-/\mathbf Q)
}\tag{7}
\]
at ALL primes, without assuming either group finite. This strengthens the previous injection into the full 32-dimensional J by replacing it with the rank-two-only 21-dimensional Atkin–Lehner part.

**Crucial equivalence:** Since \(B^-\) is independently known to have finite Sha and Φ^- is an isogeny, the finiteness of \(\Sha(J^-/\mathbf Q)\) is EQUIVALENT to that of \(\Sha(E/\mathbf Q)\). This is an exact global reduction; it is NOT a finiteness proof, and Kolyvagin–Logachev applied only to B^- does NOT imply J^- has finite Sha.

## Theorem 4: EXACT complex leading-term factorization, and the still missing arithmetic pairing

The isogeny (1) gives \(L(J^-,s)=L(E,s)L(A_{20},s)\). With \(L(E,1)=L'(E,1)=0\) and \(L(A_{20},1)\ne0\),
\[
\boxed{
\frac{L''(J^-,1)}2
=L(A_{20},1)\frac{L''(E,1)}2.
}\tag{8}
\]
Thus \(\operatorname{ord}_{s=1}L(J^-,s)=2\), and the free MW rank is also exactly 2. The exact rank-two complex BSD leading coefficient for J^- STILL requires a genuine higher-height reciprocity theorem; equation (8) alone merely transports the same missing identity.

The two global modular divisors D_P=βP, D_Q=βQ in J^- have polarisation-induced Néron–Tate pairings
\(\langle\beta P,\beta Q\rangle_J=40\langle P,Q\rangle_E\)
and determinant \(1600\operatorname{Reg}(E)\), exactly as in the earlier Faltings–Hriljac note. Their rational span constitutes ALL free Mordell–Weil directions in J^-(Q), with a finite index killed by 40 (hence saturated p-adically for every p>=7). This is more precise than placing them in J(Q) of rank 13.

No proof here identifies the real analytic L'' with this determinant. Nor is a fixed D proving a uniform Sha(E) Fitting ideal inclusion constructed.

## What the new theorem enables, and the hard stop

The new **rank-two-only modular space** is the correct place to look for a truly global primitive rank-two Euler/motivic class: the complementary motive A_20 has analytic rank0 and independently finite Sha, so all **uncontrolled positive rank** on J^- comes from E itself. The integral Hecke projector is already available away 2,5.

However, \(\Sha(E)\) finiteness remains an equally hard piece of \(\Sha(J^-)\). Neither rank-zero A20 nor congruence number40 supplies a Selmer-Fitting annihilator. Any argument asserting otherwise is circular. This note does not establish full BSD.

## Source-based proof dependencies

- Stein 1999, explicit 389 splitting and nonvanishing A20: https://wstein.org/Tables/389/389/node1.html
- Kolyvagin–Logachev finite Sha for modular rank0 abelian varieties, Stoll 2007, Corollary 6.3: https://msp.org/ant/2007/1-4/ant-v1-n4-s.pdf
- Agashe–Ribet–Stein, squarefree conductor congruence=modular degree: https://wstein.org/papers/ars-congruence/current.pdf
- Official Sage example for 389a modular degree 40: https://sources.debian.org/src/sagemath/10.10-2/src/sage/lfunctions/sympow.py
- Project's authenticated older p2/p5 Selmer logs, and PR #12 global modular degree40 projector/Faltings height notes, are reused WITHOUT rerunning.
