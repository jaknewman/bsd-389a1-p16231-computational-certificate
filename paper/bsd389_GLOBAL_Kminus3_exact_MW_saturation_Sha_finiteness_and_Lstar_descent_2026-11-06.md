# BSD 389a1: unconditional GLOBAL quadratic Mordell–Weil saturation and Sha finiteness equivalence (no auxiliary p)

**Date: 2026-11-06. Global theorem, not a proof of BSD.** This note uses NO further prime-specific certificate and adds a precise comparison of the two GLOBAL BSD obligations, via the fixed quadratic twist whose nonvanishing was previously certified. It is part of PR #12, not the de-prioritized p=16231 local branch.

Let E/Q: y²+y=x³+x²−2x, K=Q(sqrt(-3)), D=-3, tau the nontrivial automorphism of K/Q, and E^D its quadratic twist. Accepted previous exact-rational proof gives L(E^D,1)>9/2; the standard modular analytic-rank-zero theorem (Kolyvagin/Logachev) yields

rank E^D(Q)=0 and Sha(E^D/Q) finite.

The original curve has a proved rank-two saturated basis P,Q, and L(E,s) has analytic rank exactly 2.

## Theorem A — the free Mordell–Weil group does not grow at all over K

\[
\boxed{E(K)=E(Q)+E(K)_{\rm tors},
\quad E(K)/E(K)_{\rm tors}=E(Q)/E(Q)_{\rm tors}
=\mathbf ZP\oplus\mathbf ZQ.}
\]

**Proof.**
The nonzero 2-torsion points of E satisfy y=-1/2, hence
\[
f_2(x)=4x^3+4x^2-8x+1=0.
\]
By the rational-root theorem a rational root would belong to {±1,±1/2,±1/4}, and none is a root, so f2 is irreducible of degree 3 over Q. An irreducible cubic cannot acquire a root in a quadratic extension, so E(K)[2]=0. Consequently E(K)_tors is a finite group of ODD order and multiplication by 2 is an automorphism of it.

For any R∈E(K), set T=R−tau(R). It satisfies tau(T)=−T, and under the fixed K-isomorphism E^D_K≅E_K corresponds to an element of E^D(Q). Since rank E^D(Q)=0, T is torsion, so T∈E(K)_tors. There is a UNIQUE torsion H with [2]H=T. Necessarily tau(H)=−H. Then
tau(R−H)=tau(R)+H=R−T+H=R−H,
so R−H∈E(Q). This proves E(K)=E(Q)+E(K)_tors. The intersection E(Q)∩E(K)_tors is E(Q)_tors, so the induced map on free quotients is an isomorphism. QED.

**Consequences.** P,Q form a saturated integral MW basis over K as well as over Q, with NO hidden index 2 or 4. With the **absolute field-normalized** Néron–Tate height (independent of the base field),
\[
\boxed{\operatorname{Reg}_{E/K}^{\rm absolute}
=\operatorname{Reg}_{E/Q}.}
\]
If using an unnormalized trace-of-local-heights convention over K, each pairing gets a factor [K:Q]=2 and its rank-two determinant a factor 4; this is a PERIOD/REGULATOR CONVENTION, not an arithmetic MW index.

This theorem is global and p-independent. It is stronger than the prior observation rank E(K)=2 or merely "the MW index is a 2-power."

## Theorem B — exact global Sha FINITENESS equivalence (no conjectural finiteness input)

\[
\boxed{
\Sha(E/K)\text{ finite}
\iff
\Sha(E/\mathbf Q)\text{ finite}.
}\tag{B}
\]

**Odd-primary proof.** For every odd rational p, quadratic restriction/corestriction, local Shapiro and the idempotents (1±tau)/2 identify
\[
\boxed{
\Sha(E/K)[p^\infty]
\simeq\Sha(E/Q)[p^\infty]\oplus\Sha(E^D/Q)[p^\infty].
}
\]
This is an exact group decomposition, not merely an equality of coranks. As the twist's Sha is a single FINITE group, the direct sum of ALL odd primary parts upstairs is finite iff the direct sum of all odd primary parts downstairs is finite.

**2-primary proof.** At p=2, do NOT claim the above integral idempotent decomposition (1/2 is not a Z2-unit). Over Q2, however, 1/2 IS a scalar, and Shapiro plus the quadratic character decomposition of the *rational* Galois representation gives
\[
H^1_f(K,V_2E)\simeq
H^1_f(Q,V_2E)\oplus H^1_f(Q,V_2E^D).
\]
The rational Tate-module Kummer exact sequence identifies
\[
\operatorname{corank}_{Z_2}\Sha(E/K)[2^\infty]
=\operatorname{corank}_{Z_2}\Sha(E/Q)[2^\infty]
+\operatorname{corank}_{Z_2}\Sha(E^D/Q)[2^\infty].
\]
The last term is zero because Sha of the twist is finite. For a fixed elliptic curve over a number field, the p-primary Sha is cofinitely generated, so zero Zp-corank is EQUIVALENT to its p-primary part being finite. This proves finiteness of the two-primary parts is equivalent. Combining p=2 and all odd primes proves (B). QED.

**Important caveat:** This equivalence does NOT establish either finiteness; it cleanly transfers the SAME global obstruction to the quadratic base change. No fixed p-adic theta result can be substituted for finiteness in this proof.

## Theorem C — exact analytic base-change leading term

Artin formalism for the quadratic extension gives an identity of entire L-functions:
\[
\boxed{L(E/K,s)=L(E,s)\,L(E^D,s).}
\]
Because L(E,1)=L'(E,1)=0 EXACTLY and L(E^D,1) is NONZERO, differentiation gives
\[
\boxed{
\frac{L''(E/K,1)}2
=L(E^D,1)\frac{L''(E,1)}2
}\tag{C}
\]
without any p-adic hypothesis. It follows that analytic rank E/K is exactly two, independently of any conjectural BSD formula.

The rank-zero twist's L(E^D,1) has a known, independently certified **positive exact-rational interval** (9/2,23/5), so the factor in (C) is nonzero and explicitly controllable.

## Theorem D — a SINGLE (still unproved) global rank-two BSD statement over K would imply both BSD global obligations over Q, once rank-zero BSD for the twist is supplied

Let
\[
A=\operatorname{Res}_{K/Q}(E_K),\qquad
B=E\times E^D.
\]
There is a Q-isogeny \(B\to A\) of degree 4: after base change to K it is given by the sum/difference matrix \(\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}\) (using the twist's K-isomorphism). The isogeny covariance of the *full* BSD formula and the Weil-restriction compatibility (Cassels–Milne) imply:

**Conditional global theorem:** If the complete strong BSD conjecture is proved for E/K and the rank-zero twist E^D/Q, then the complete strong BSD conjecture follows for E/Q. Conversely, if strong BSD holds for E/Q and the twist, it holds over K. No restriction on rank is needed for this formal implication.

This transfers **both finiteness of Sha and the exact COMPLEX leading coefficient** together. It is NOT an unconditional proof: its missing E/K rank-two theorem is of essentially the same difficulty as BSD for E/Q. A definite quaternionic theta nonvanishing or a single p-adic Selmer theorem is NOT a substitute for that full global E/K theorem.

This equivalence can guide genuine global work only if a **new higher-rank integral arithmetic theorem** is independently found or proved over K (all primes + archimedean regulator), not by treating the equivalence itself as the desired solution.

## What genuinely changed vs previous p-by-p notes

- A complete **global** proof that the rational MW lattice is **already saturated over K**, excluding a hidden quadratic index for ALL p at once.
- A clean **full Sha finiteness equivalence, including p=2**, with no Sha finiteness assumption silently imposed.
- An exact analytic leading coefficient factorization with a separately certified nonzero rank-zero twist value.
- A source-backed but explicitly CONDITIONAL equivalence of the FULL refined BSD formula by a degree-4 isogeny, eliminating any unjustified claim that base change magically resolves the rank-two obstruction.

The global missing theorem is still rank-two arithmetic regulator reciprocity/ETNC + all-prime Selmer finiteness (or an equivalent global theorem that proves both). The previous exact Mellin–Fricke formula remains a rigorous analytic evaluation, not an archimedean arithmetic comparison.

## Sources

- W. Stein, *The Birch–Swinnerton-Dyer Conjecture*, E389a Open Problem 2.18, https://wstein.org/books/bsd/bsd.pdf.
- Cassels–Milne Weil restriction and isogeny invariance of BSD: Milne (1972), and the derivation by Daniel Loughran https://mathoverflow.net/questions/179764/a-question-on-bsd-conjecture/179770 ; Jeremy Booher, *Isogeny invariance of the BSD conjecture*, https://people.clas.ufl.edu/jeremybooher/files/L6.pdf.
- Previously proved twist central L-value positivity: paper/389a1_quadratic_base_change_twist_rank0_finite_minus_sha_2026-10-27.md .
- Previously certified analytic rank: results/full_BSD_exact_analytic_rank2_PASS_2026-10-19.md .
- Entirely global previous direct attack: paper/bsd389_DIRECT_GLOBAL_exact_Mellin_Lstar_uniform_Sha_two_gates_2026-11-06.md .
