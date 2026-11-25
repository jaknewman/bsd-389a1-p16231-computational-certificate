# BSD 389a1 — Exact Bockstein factorization and obstruction to a universal integral Selmer matrix (9 Nov 2026)

**Status: new proved algebraic theorem, independently checked exact non-diagonal integer matrices; source-based 13 actual p-adic regulators for 389a1; precise unsolved arithmetic comparison. NO global Sha annihilator and NO complex BSD proof.**

## I. Exact sharp Bockstein leading term

Let A(T)∈Mat_m(Z[[T]]), rank_Q A(0)=m−2. Put K=ker_Z A(0), C=coker_Z A(0), F=C_tors, L=C/F. Both K,L are free of rank two. Let

  β_A:K→L,   x↦[A'(0)x] mod F,

the integral specialization Bockstein map. Then

  **|[T²]det A(T)| = #F · |det β_A|.**

*Proof.* Smith-normalize A(0) over Z as diag(d1,...,d_(m−2),0,0). The constant-row and -column vanishing forces the coefficient T² to be (∏d_i) multiplied by the determinant of the lower-right 2×2 block of the first T derivative, which represents β_A. ∏|d_i|=#F; unimodular basis changes affect signs only. Thus the equality holds, including if the Bockstein is degenerate.

The earlier result that c2 annihilates the torsion is only one consequence; the new exact equality identifies **both** the torsion factor and the independent rank-two Bockstein factor. A unit determinant β is needed to make c2 have the exact torsion order.

**Executed exact tests** (torsion order, Bockstein determinant, quadratic coefficient) on non-diagonal 4×4 unimodular transforms:
(30,7,210), (7,7,49), (25,1,25), (48,−2,−96), (1,0,0). Every determinant and torsion order checked by SymPy/Smith normal form. These are algebraic models, not a computation of the actual Selmer complex of E389a1.

## II. Cohomological meaning and a *real* rank-two input

Nekovář's Selmer complexes support a cyclotomic Bockstein H¹→H²; the p-adic height pairing is given by pairing β(x) with y under the duality (Benois, §4.2). Castella–Sano 2026 §2.2 use the determinant of a perfect Λ_p-complex RΓ(Z[1/(Np)], T). The condition that Kato's element *generate its integral determinant line* is the determinantal main-conjecture problem, **not** a consequence of the abstract factorization above.

For **389A itself**, Mazur–Stein–Tate 2006, §4.3, published nonzero unit-leading cyclotomic p-adic regulators at **13 good ordinary primes**:

p:       5  7  11 13 17 19 23 29 31 37 41 43 47
R_p mod p:1  6   4  9  4  3 17  9  1 28 20 40 25

Thus the relevant *rational* cyclotomic p-adic height/Bockstein pairing is nondegenerate at those 13 primes (with the standard height comparison). The table is a published numerical computation, not independently recomputed in this work, and it does **not** prove that the integral Bockstein determinant equals those residues without further unit comparisons. Nor does it bound Sha for all primes.

## III. An integral rank-2 Galois lattice is impossible

For any p≥5, a rank-two G_Q-module L=Z² with image in GL₂(Z) cannot reduce to E[p]. Its determinant always lies in {±1} modulo p; however Weil's pairing gives det(E[p])=χ_p with surjective image Fp×, which has more than two elements. Hence a *single* Galois-equivariant integral Z² lattice packaging the full T_pE by reduction is impossible.

The actual common object is the adelic Tate module T_hatZ(E)=∏_p T_pE over hatZ=∏_p Z_p, with determinant the full cyclotomic character. This no-go does NOT preclude more sophisticated integral motivic or cohomological constructions.

## IV. Explicit adelic failure of a common integer annihilator

For every p≥5, set A_p(T)=diag(T,T,T+p,T+p). Each det A_p=T²(T+p)² is primitive (T⁴ coefficient=1), each specialized rank is precisely two, each Bockstein is the identity, and each specialized finite torsion module equals (Z/p)² with a perfect alternating pairing.

Nonetheless the group G=⊕_{p≥5}(Z/p)² is infinite, with G[n] finite for every n. NO nonzero integer kills G: choose p∤D. Equivalently the common ideal of leading coefficients intersects Z trivially, (∩_p p²Z_p)∩Z=0.

Thus **even all-p primitive Iwasawa determinants plus nondegenerate Bocksteins and finite self-dual local torsion do not themselves give a global integer annihilator**. An extra arithmetic theorem of finite prime support (or a genuinely shared nonzero integer determinant controlling every p) is indispensable. These modules are *toy models*, not Sha(389a1).

## Exact remaining BSD gates

1. Construct for this specific E a cohomological integral specialization with an actual injection/bound for Sha(E)[p∞] and canonical Bockstein comparison.
2. Prove these leading coefficients are p-units outside a finite set (or construct a shared nonzero integer annihilator). The 13 published regulator units and 5000+ Stein–Wuthrich local certificates do not establish that for all p.
3. Separately prove the *complex* exact identity L''(E,1)/2=Ω_E Reg_E·#Sha.

**Sources:** Castella–Sano arXiv:2601.14504, §2.2 https://arxiv.org/pdf/2601.14504 ; Nekovář, *Selmer Complexes*, Astérisque 310 (2006) https://smf.emath.fr/publications/complexes-de-selmer ; Benois, *Selmer complexes and the p-adic Hodge theory* §4.2 https://arxiv.org/abs/1404.7386 ; Mazur–Stein–Tate *Computation of p-adic heights and log convergence* §4.3 https://www2.math.ethz.ch/EMIS/journals/DMJDMV/vol-coates/mazur_stein_tate.pdf .

**Reproducible exact verification** provided as conversation ZIP: \`bsd389_exact_bockstein_adelic_certificate_20261109.zip\`.
