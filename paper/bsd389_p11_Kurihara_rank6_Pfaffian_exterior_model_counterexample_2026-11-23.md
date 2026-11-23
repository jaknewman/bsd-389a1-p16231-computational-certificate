# 389a1: a rank-SIX Kurihara two-prime matrix at p=11 disproves naive rank-two and four-dimensional determinant transfer

**23 November 2026. Mathematical status: an EXACT arithmetic counterexample to a candidate shortcut for all-large-prime Sha finiteness.** All **15** distinct genuine two-prime Kurihara coefficients were evaluated by complete integer Manin-symbol enumeration in the assistant's Python runtime, with independently archived Sage/eclib p=5 and p=11 normalization anchors. No result about Sha[p] at *new* p is being claimed, and no all-prime Sha bound or strong BSD formula is proved.

## 1. Arithmetic setup

Curve: E:y²+y=x³+x²−2x (389a1); rank(E(Q))=2, P=(-1,1), Q=(0,-1), torsion=0, minimal model. Fix p=11.

We use the **same independently authenticated integral Néron-normalized 390-edge plus modular-symbol vector**, shifted-digit SHA256

    31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee.

For each auxiliary q we choose the **least positive primitive root g_q modulo q**, giving the ordinary discrete-log convention \log_{g_q}. Our six distinct good 11-admissible primes, in **increasing order**, are

    q=(397,991,1321,2113,3389,3433).

Each satisfies q≡1 mod11 and 11||#E(F_q), hence dim_F11(E(F_q)/11)=1. Direct finite-field point counts and elliptic group arithmetic give:

| q | #E(Fq) | smallest primitive root gq | local coordinates of (P,Q) |
|--:|--:|--:|:--|
|397|374|5|(1,10)|
|991|1045|6|(1,7)|
|1321|1320|13|(1,2)|
|2113|2167|5|(1,7)|
|3389|3465|3|(1,8)|
|3433|3421|5|(1,9)|

The local coordinates are computed by multiplying P,Q by #E(Fq)/11 and expressing the second resulting 11-torsion point relative to the first, not by guessing local bases.

## 2. Fifteen REAL Kurihara coefficients vs local MW minors

For i<j, form

    d_ij = \tildeδ_{q_i q_j}(E) mod11
         = Σ_(a ∈ (Z/q_i q_j)^×) m_E^+(a/(q_i q_j))
             log_(g_qi)(a) log_(g_qj)(a) mod11.

The program uses the exact full even-symbol reduction a ↔ −a and an independently preverified 390-edge continued-fraction expansion to compute **every term**, not sampled or conjectural values. It reproduces the archived p5 benchmark δ_(41·61)=4 (primitive roots 6,2) and the user-executed p11 benchmark δ_(397·991)=1 (roots 5,6).

The resulting 15 d_ij are:

| q_i | q_j | d_ij | w_ij=det(loc_qi(P,Q),loc_qj(P,Q)) mod11 |
|:--|:--|--:|--:|
|397|991|1|8|
|397|1321|9|3|
|397|2113|3|8|
|397|3389|4|9|
|397|3433|7|10|
|991|1321|10|6|
|991|2113|0|0|
|991|3389|7|1|
|991|3433|9|2|
|1321|2113|8|5|
|1321|3389|2|6|
|1321|3433|5|7|
|2113|3389|10|1|
|2113|3433|5|2|
|3389|3433|1|1|

The q=991,2113 pair has the same local MW row (1,7) at both primes and correspondingly d_ij=0; this zero was ALSO obtained by a complete global Kurihara sum, not imposed by local algebra.

Define the **ordered alternating matrices** D=(D_ij) and W=(W_ij) by D_ij=d_ij and W_ij=w_ij for i<j, D_ji=−D_ij, W_ji=−W_ij. Note that the arithmetic Kurihara coefficient is originally associated with an UNORDERED pair; the increasing-q convention makes an artificial orientation for a precise proposed exterior-factorization test.

## 3. Exact Pfaffian theorem (new, unconditional finite arithmetic)

The six-by-six Kurihara coefficient matrix is

    D =
    [ 0,  1,  9,  3,  4,  7 ]
    [-1,  0, 10,  0,  7,  9 ]
    [-9,-10,  0,  8,  2,  5 ]
    [-3,  0, -8,  0, 10,  5 ]
    [-4, -7, -2,-10,  0,  1 ]
    [-7, -9, -5, -5, -1,  0 ]   mod 11.

Direct exact recursive Pfaffian expansion and independent modular Gaussian elimination give:

    **Pf(D)=4 mod11;  det(D)=Pf(D)^2=5 mod11; rank_F11(D)=6.**

For the authentic MW-local determinant 2-form W,

    **Pf(W)=0; rank_F11(W)=2**.

Thus there do NOT exist vectors A,B∈F11^6 such that
    D_ij=A_i B_j-A_j B_i
for all fifteen pairs. More generally D cannot be a sum of **two** decomposable exterior forms: such a sum has rank≤4.

These assertions remain valid after **any nonzero per-prime scaling** d_ij↦u_i u_j d_ij, as these scalings conjugate the skew matrix D by an invertible diagonal matrix and preserve its rank.

They disprove a naive would-be Kato determinant identity replacing the conductor-dependent two-prime Kurihara coefficient by a single fixed global rank-two MW wedge or even a sum of two global rank-two wedge channels, under the explicit increasing-q orientation.

## 4. A sharper *pencil* obstruction and the five-prime false lead

A first subset of FIVE primes (397,991,1321,2113,3389) exhibited an accidental exact factorization:
    **D|five = 8·W|five + R|five**
where R|five has rank 2. One can reconstruct this residue as a single exterior product of the vectors

    u=(0,3,7,5,9),  v=(10,0,2,0,7) in F11^5.

This is a rigorously CHECKED identity on all ten pairs of those five primes. It suggested a second "derived Kato channel" could complement MW.

The sixth prime q=3433 DISPROVES that extrapolation: on the six-prime matrix the entire one-parameter pencil has Pfaffian

    **Pf(D−λW) = 4 + 5λ mod11**     for every λ∈F11.

If λ≠8, this Pfaffian is nonzero and rank(D−λW)=6. For the unique root λ=8, the matrix has rank EXACTLY 4 (not 2). Therefore

    **for NO λ∈F11 is D−λW decomposable**.

The extra conductor dependence persists beyond a single "MW wedge + another fixed wedge" correction. The five-prime decomposition was a bounded-sample coincidence, not a valid universal identity.

## 5. What this DOES and DOES NOT mean for the p-uniform Sha project

The result proves **a mathematical obstruction to a specific shortcut**, not a no-go theorem for all possible motivic Euler systems. In particular, authentic derived Kato cohomology classes depend on their squarefree auxiliary conductor n, so it is not surprising that no single fixed two-dimensional local coefficient space globally controls all d_ij.

The established **deep Kummer-axis Chebotarev theorem** still gives, for all sufficiently large p, q_P and q_Q making the MW localization invertible modulo every p^k. The new arithmetic data show why replacing the *global* δ_(q_P q_Q) with that local wedge is NOT justified: their complete pairwise value tables are different, and no global rank-two or rank-four exterior interpolation works in the tested natural orientation.

The remaining genuine all-large-p task is to prove **some deep admissible two-prime δ has p-valuation <=1**, or to establish a p-INDEPENDENT integral Fitting/Euler system bound. Neither is supplied by the proved Pfaffian statement.

## 6. Reproducibility and provenance

- Full 4-prime p11 genuine arithmetic and Plücker test (p5/p11 anchoring):
  \`verification/bsd389_p11_Kurihara_Plucker_non_decomposability_gate.py\`.
- Six-prime 15-value, local MW, rank6, Pfaffian4 and pencil test:
  \`verification/bsd389_p11_Kurihara_six_prime_Pfaffian_rank6_gate.py\`.

Default six-prime run audits the frozen values and true MW rows. Passing \`--full\` recomputes ALL FIFTEEN exact modular-symbol sums, which were executed in several independent assistant Python batches on 2026-11-23. Reproduction of the earlier p=11 q397*991 certificate on the user's Ubuntu Sage is archived in
\`results/bsd389_p11_Kurihara_397_991_USER_SAGE_PASS_2026-11-23.md\`;
the new five q pairs have not been independently rerun by the user.

The independence here is a NEW algorithmic execution from the frozen integer Manin symbol vector, not a brand-new derivation of that vector using eclib. The p5 and p11 independent Sage/eclib anchor residues validate convention and normalization.

**Verdict: genuine exact counterexample and a precise new limit on naive rank-two global determinant models. Full BSD remains a distinct target.**
