# E389a1 — Quadratic local-volume factorization of 115 authentic Kurihara residues

**Date: 2026-11-24. Status:** Exact finite arithmetic computations and a proved elementary Cauchy–Binet lemma. Proposed infinite four-prime reciprocity law remains UNPROVED. No global Sha finiteness or full BSD claimed.

## 1. Newly verified finite arithmetic phenomenon

E: y²+y=x³+x²−2x, saturated Mordell–Weil generators P=(-1,1), Q=(0,-1).

For each good p-admissible auxiliary q with exactly one p dividing #E(Fq), the local quotient E(Fq)/p is one-dimensional. Define its (P,Q) localization vector v_q=(1,s_q) when P is a generator, with s_q defined by Q=s_q P modp; use v_q=(0,1) when P=0 and Q is a generator. Define Δ_ij=det(v_i,v_j) in Fp.

The true two-prime Kurihara number δ_ij is computed as the COMPLETE modular-symbol weighted sum over units modulo q_iq_j with the smallest primitive roots at the q's, using the authenticated integral 390-Manin edge vector. Each output is independently checked against known benchmarks: p5 pair (41,61) gives 4, and p7 pair (113,673) gives 2.

**p=5:** fifteen primes

    q      41 61 131 211 251 271 571 641 751 991 1031 1181 1321 1381 1811
    slope   3  0   4   4   ∞   2   1   0   2   ∞    2    1    3    3    1

give exactly 105 pairs. All 105 actual δ values satisfy

\[
\boxed{\delta_{ij}=3\,u_i u_j\,\Delta_{ij}^{2}\pmod5}
\]

for the explicitly reconstructed unit vector

    u       1  2   2   4   1   1   4   4   4   3    3    2    1    3    1.

Exactly 93 pairs have both determinant and δ nonzero; exactly 12 have both zero. There are 558 four-distinct-prime configurations with all six determinants nonzero, and every one satisfies all three quadratic cross relations. An alternative enumeration checking individual cross pairings returned 2,455 valid comparisons with zero failures.

**p=7:** five primes

    q      113 673 1429 2423 3389
    slope    3   6    4    ∞    4
    u        1   4    4    3    4

give exactly 10 independently computed true δ values. All 10 satisfy

\[
\boxed{\delta_{ij}=2\,u_i u_j\,\Delta_{ij}^{2}\pmod7}.
\]

Nine pairs have both determinant and δ nonzero, and pair (1429,3389) has both zero. Both nondegenerate four-prime configurations obey the quadratic cross relations.

**IMPORTANT:** u_i and constants C_p=3,2 were RECONSTRUCTED from observed two-prime residues. The formula is a highly overdetermined FINITE identity, NOT a predictive universal arithmetic law or proof of Sha0.

The complete actual self-contained compiled C++17 verifier was executed in the model environment, uses the archived authentic 390-edge vector, checks every finite-field point count and local slope, recomputes every δ from the full half-range of residue units and validates all 115 identities. File available as accompanying generated artifact bsd389_quadratic_volume_small_pairs.cpp. Benchmarks above are embedded as mandatory assertions.

## 2. A PROVED new elementary explanation of the squared determinant

**Rank-two local-volume determinant lemma.** Over any commutative ring R, take local column vectors v_i=(a_i,b_i), weights w_i and commuting variables X_i. Put

\[
H(\mathbf X)=\sum_i w_iX_i\,v_i v_i^{\mathsf T}.
\]

Then an exact polynomial identity is

\[
\boxed{\det H(\mathbf X)=
\sum_{i<j} w_iw_j(a_ib_j-a_jb_i)^2 X_iX_j.}
\]

Proof: direct expansion of H_11 H_22 − H_12²; each X_i² coefficient is zero because each v_i v_i^T has determinant zero; each mixed coefficient is
w_iw_j(a_i²b_j²+a_j²b_i²−2a_ib_ia_jb_j)=w_iw_j det(v_i,v_j)². No Selmer or BSD hypotheses enter this linear-algebra identity.

This is a potential structural explanation of the observed factorization IF genuine Mazur–Tate/Bockstein heights admit a compatible decomposition into rank-one local forms H_q=w_q ℓ_q⊗ℓ_q and the Kurihara derivative is identified with a single global scalar times the mixed regulator determinant. This arithmetic identification has NOT been constructed.

## 3. New falsifiable four-prime arithmetic research conjecture

For any four admissible one-dimensional primes i,j,k,l with all six Δ values nonzero, put R_ij=δ_ij/Δ_ij² in Fp. The *quadratic local-volume reciprocity* hypothesis QLVR is:

\[
\boxed{R_{ij}R_{kl}=R_{ik}R_{jl}=R_{il}R_{jk}.}
\]

These equalities are invariant under independent rescaling of each local Kummer generator AND changing primitive roots used for each auxiliary discrete logarithm: each R_ij changes by a product of an i-only and a j-only unit, which cancels from the cross products.

QLVR is confirmed for the finite p=5 and p=7 data above. It is NOT proved for all q or all p. A single four-prime violation would refute the universal conjecture.

When enough Δ's are nonzero and QLVR holds, elementary graph-factorization recovers a representation δ_ij=C_p u_i u_j Δ_ij² with q-local units. But this reconstruction from δ is not independent arithmetic evidence that C_p is a unit.

## 4. A sharp proven local obstruction

Kim's published Theorems 1.8 and 1.10 imply under their Galois, Manin, good local p-torsion and Tamagawa hypotheses that a p-unit two-factor Kurihara coefficient for a rank-two E requires both local p-quotients to have dimension exactly one and the full localization of the rational MW basis to have nonzero determinant. If one q has two-dimensional local p-torsion, or if the two local rows are dependent, then δ_(q1q2)=0 modp. This explains earlier authentic zero witnesses:
- p=5, (5351,13001): at 13001 the local p-quotient dimension is 2;
- p=7, (113,281): at 281 the local p-quotient dimension is 2;
- p=5, (131,211): same local slope4 and δ=0;
- p=7, (1429,3389): same local slope4 and δ=0.

This is a useful theoretical filtering theorem, NOT a proof that any remaining pair is a unit.

## 5. The genuine next arithmetic proof obligation

Produce the local rank-one forms H_q and the global scalar C_p **independently of knowing the δ_ij** (e.g., via a rank-two derived Kato/Bockstein reciprocity morphism). Prove that the true Mazur–Tate mixed second derivative is C_p times the mixed determinant of these forms. This would prove QLVR as a mathematical theorem rather than an observation.

Even this would not force C_p≠0: Kim identifies two-factor p-unit existence with Sha(E/Q)[p∞]=0 at the relevant large primes. To prove global Sha finiteness, we must further show C_p is a p-unit for all sufficiently large p, or control its exceptional prime support by one independently constructed integer. Any argument that silently assumes this nonvanishing is circular.

The rank-two derived Kato leading-term/Bockstein comparison that would support this is explicitly CONJECTURAL in Burns–Kurihara–Sano (2024), Conjecture 1.1(iii); Cauchy–Binet alone does not fill that gap.

## References

- Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorems 1.8, 1.10: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Castella–Sano (2026), *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Burns–Kurihara–Sano (2024), *On derivatives of Kato's Euler system for elliptic curves*, Conjecture 1.1(iii): https://kurihara.math.keio.ac.jp/bks4.pdf

**Verdict:** 115 genuine finite congruences and the quadratic rank-two linear algebra theorem VERIFIED. Universal QLVR and the global arithmetic identification OPEN. No global Sha finiteness or exact complex BSD claimed.


## 6. Conditional new *single-scalar* theorem: why the QLVR program would reduce the infinite search

**Proposition (proved implication).** Fix a good prime p satisfying the hypotheses of Kim's Theorems 1.8 and 1.10, with E(Q) of rank2, two-prime MW-independent Kolyvagin primes available by the independently proved Kummer–Chebotarev theorem, and Castella–Sano's minimum Kurihara valuation zero. Assume the following two additional ARITHMETIC hypotheses:

(H1) an infinite local-volume factorization valid for **all suitable** pairs of nonidentity-unipotent Frobenius primes q,r:
\[
\delta_{qr}=\mathcal C_p\,w_qw_r\,\det(v_q,v_r)^2\pmod p
\]
with a scalar \(\mathcal C_p\in\mathbf F_p\) and local weights \(w_q\in\mathbf F_p^\times\) **constructed independently of the two-prime values**;

(H2) Kim's p-unit two-prime witness can be taken among the suitable pairs above (for this, the published semi-local isomorphism forces both local dimensions one, and the remaining v_p(#E(F_q))=1 condition should be omitted from the theorem unless separately justified; the factorization may instead be formulated for all one-dimensional local quotients, including p^m-order groups).

Then
\[
\boxed{\mathcal C_p\ne0\iff\Sha(E/\mathbf Q)[p^\infty]=0.}
\]
*Proof*: If C_p≠0, choose a Chebotarev MW-independent suitable pair q,r, so δ_qr≠0. Kim+Castella–Sano imply Sha[p∞]=0. Conversely if Sha[p∞]=0, the full Kurihara system and Kim imply the existence of a nonzero two-prime δ; by (H2) this pair lies in the factorization domain and has nonzero determinant and nonzero local weights, forcing C_p≠0. QED.

The forward implication alone needs H1 and the pair-existence theorem, not H2. The backward implication needs H2 or a suitably strengthened all-one-dimensional-primes factorization.

**WARNING:** This proposition is conditional on a genuinely new, still unproved ARITHMETIC H1. Even after H1 is proved, nonvanishing of C_p at every sufficiently large p remains **equivalent in difficulty** to Sha's p-tail vanishing. The program becomes useful for BSD only if the independently defined C_p can be bounded by a **single prime-independent nonzero integral object**, or if a new global theorem proves C_p unit uniformly. Constructing C_p by fitting two-prime residues is circular for that purpose.


## 7. ADDENDUM 2026-11-24 — third prime p=11, 15 new authentic pairs, and OUT-OF-SAMPLE predictions

A completely independent C++17 computation using the same historically authenticated 390-entry integral Manin vector (not any solved QLVR weights) evaluated the COMPLETE half-unit ranges at all **15 pairs** from the six primes
\[
q=(397,991,1321,3389,3433,4643).
\]
All six satisfy the p=11 admissibility criteria and have exactly one factor 11 in \(\#E(\mathbf F_q)\); independent finite-field arithmetic of the genuine P,Q reductions gives local slopes
\[
s=(10,7,2,8,9,4)\in\mathbf F_{11}^6.
\]
The genuine two-prime residues, ordered lexicographically by pairs, are
\[
\begin{array}{c|rrrrr}
q_i\backslash q_j&991&1321&3389&3433&4643\\\hline
397&1&9&4&7&5\\
991&&10&7&9&6\\
1321&&&2&5&2\\
3389&&&&1&8\\
3433&&&&&5
\end{array}
\]
The historically independently archived **(397,991) gives 1 mod 11**, recovered exactly by this independent direct enumerator.

For all 15 pairs:
\[
\boxed{\delta_{ij}=7\,u_i u_j(s_j-s_i)^2\bmod 11,\quad
u=(1,7,8,8,1,6).}
\]
All **15 independent four-prime triples of cross-product equalities** pass (the 15 choices of four among six, all local slopes pairwise distinct), with no exceptions. Explicit normalized cross-products for the first quadruple 397,991,1321,3389 are (7,7,7) mod11.

**OUT-OF-SAMPLE TEST:** Only the five star edges \((397,q)\), q in the remaining five primes, plus the single edge (991,1321) were used to determine **C=7 and six u_i**. These are SIX calibrating Kurihara values; the remaining **NINE** pair residues were predicted BEFORE comparison and the nine independent full Manin sums match *exactly*:
\[
\begin{array}{c|rrrrrrrrr}
(q_i,q_j)&(991,3389)&(991,3433)&(991,4643)&(1321,3389)&(1321,3433)&(1321,4643)&(3389,3433)&(3389,4643)&(3433,4643)\\\hline
\text{predicted=actual}&7&9&6&2&5&2&1&8&5
\end{array}
\]
This is a genuinely predictive **finite sample** test, though it still uses two-prime values to calibrate the local units; it is NOT an independent q-only arithmetic construction.

The totals across three distinct primes are now **130 genuine completed two-factor sums: 105 at p5, 10 at p7, and 15 at p11**. The arithmetic p11 six-prime run took approximately **3.7 seconds** in optimized C++17 in the assistant runtime. The existing repo verifier verification/bsd389_quadratic_volume_small_pairs.cpp was extended to include the p11 six-prime test and a mandatory known benchmark. It recalculates local point counts and slopes, whereas the independent compact p11 C++ used the separately computed slope array. This adds implementation diversity; the newly updated repo verifier itself has not yet been user-executed.

### 7.1. The first genuinely q-only weight proposal FAILS — exact arithmetic counterexample

A natural attempt to build the q-local units **without using any pairwise δ** is to extract the quadratic coefficient of the single-prime Mazur–Tate polynomial
\[
\Theta_q(X)=\sum_{a\bmod q}^{*}m_E^+(a/q)\,X^{\log_g(a)\bmod p}.
\]
This is an independently calculable scalar from the SAME authentic 390-entry Manin vector, involving no two-prime conductor.

However the direct exact finite computations show
\[
\boxed{\Theta_{41}(X)=0,\qquad \Theta_{61}(X)=0\ \text{in }\mathbf Z[X]/(X^5-1)}
\]
for p=5 and the smallest primitive roots g41=6, g61=2 (the entire five-coefficient histograms vanish, not only their quadratic coefficients). Yet
\[
\boxed{\delta_{41\cdot61}\equiv4\bmod5\ne0.}
\]
The full two-prime benchmark was independently recomputed with the same Manin path algorithm and agrees with the historically audited value 4.

Thus one cannot define the **necessary unit** local factor u_q solely as a multiple of \([T^2]\Theta_q(1+T)\) or any other coefficient of the *single-prime* theta polynomial: the one-prime theta vanishes even though the mixed two-prime derivative is a unit. The proposed independent local weights must use a richer object, e.g. finite-singular comparison of actual Kato cohomology classes or a q-indexed local height, not the scalar one-prime Mazur–Tate group-ring element.

This falsification is a substantive research outcome: a tempting low-cost independent weight construction is mathematically unavailable on these true q values.

### 7.2. What is PROVEN and what remains OPEN

Proven algebraically: Cauchy–Binet local-volume determinant formula; rank-one four-product factorization criterion; exact 130 finite-sample modular-symbol congruences; independently benchmarked p11 out-of-sample predictions; the explicit single-prime theta-zero counterexample to a scalar weight construction.

Open: universal QLVR; existence of independently constructed canonical local Kato/Bockstein weights w_q and one global regulator scalar C_p; nonvanishing of C_p at every sufficiently large p; uniform finiteness and triviality of Sha(E/Q) and the exact complex rank-two BSD identity.

This specifically **rules out** replacing all the missing arithmetic Kato–Bockstein comparison by a one-prime theta Hessian.
