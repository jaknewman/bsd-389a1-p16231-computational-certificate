# E389a1: ALL authentic diagonal cyclotomic resultants are PERFECT SQUARES — exact functional-equation theorem, not a coincidence

**2026-11-23. Status: NEW rigorous all-p^k arithmetic theorem from the published Mazur–Tate functional equation (Kazuto Ota, Annales de l'Institut Fourier 73 (2023), Proposition 2.5), combined with our existing universal deep diagonal quadratic Hecke congruence. Checked on THREE independent genuine Manin-conductor polynomials, including the 89-digit depth-25 example. The theorem does not prove Sha finite or full BSD.**

## 1. Published functional equation, with its exact Frobenius direction

For E=389a1:y²+y=x³+x²−2x, conductor N=389 and functional equation sign w(E)=+1, the Mazur–Tate element θ_n in the integral even group ring of (Z/n)^× satisfies

    **θ_n = Fr_{−N}^{−1} · ι(θ_n)**,

where ι sends each group element σ to σ^−1. Since all our order-p^k diagonal characters are EVEN (λ_i(−1)=0), one may replace −N by N in the projected cyclic group.

This follows directly from **Ota, *On the rank-part of the Mazur–Tate refined conjecture for higher weight modular forms*, Annales de l'Institut Fourier 73 (2023), Proposition 2.5**, which states

    θ_S = (−1)^{weight/2} ε_f Fr_{−N}^{−1} ι(θ_S).

For weight 2, (−1) ε_f is exactly the analytic sign w(E)=+1, hence the stated formula. The unprojected integral relation also comes from the Atkin–Lehner transformation of Néron-normalized modular symbols. **No Sha-finiteness hypothesis is used.**

Primary published source:
https://aif.centre-mersenne.org/item/10.5802/aif.3557.pdf
section 2.3, Proposition 2.5, printed p.1327.

## 2. Genuine cyclic diagonal polynomial and exact inversion shift

Fix an arbitrary prime p≥5, k≥1, m=p^k, and distinct good p^k-admissible auxiliary q1,q2. Let n=q1 q2 and use primitive roots g1,g2 and logs λ_i to Z/m. Define the actual integer diagonal Mazur–Tate element

    F(X)=Σ_(a∈(Z/n)^×) m_E^+(a/n) X^([λ1(a)+λ2(a)]_m)
          ∈ Z[X]/(X^m−1).

Let λ_N=λ1(N modq1)+λ2(N modq2)∈Z/m. Under the genuine quotient of the published functional equation,

    **F(X) = X^(−λ_N) F(X^−1) (mod X^m−1).**

Write F(X)=Σ_(j=0)^(m−1) a_j X^j, with the canonical representative. Putting s=−λ_N modm, the functional equation is the exact INTEGER coefficient involution

    **a_j = a_((s−j) modm)  for all j.**

The coefficients may be large integers and no modulo-p reduction is taken. This is stronger than the p-adic low quadratic-jet identity; the inversion relation is an EXACT finite-conductor symmetry.

## 3. New perfect-square RESULTANT theorem (all p,k,pairs, no unit assumption)

Let ζ be a primitive m-th root and S_m(X)=1+⋯+X^(m−1). The genuine integer resultant is

    B=Res_X(S_m(X),F(X))=∏_(t=1)^(m−1)F(ζ^t)∈Z.

Since m is odd, multiplication by 2 is invertible modulo m. Choose h∈Z/m satisfying 2h≡−s modm and define G(X)=X^h F(X) in the cyclic group ring.

Then the functional equation proves

    **G(X)=G(X^−1)**  in Z[X]/(X^m−1).

For t≠0 modulo m, set g_t=G(ζ^t). We have g_t=g_(−t). Moreover

    ∏_(t=1)^(m−1) g_t = ∏_(t=1)^(m−1) F(ζ^t)

because the factor ∏ζ^(ht)=ζ^(h*m(m−1)/2)=1.

Put
    H=∏_(t=1)^((m−1)/2) G(ζ^t).
Every g_t is an algebraic integer. Any automorphism ζ→ζ^u, u∈(Z/m)^×, permutes the PAIRS {t,−t} and hence permutes the factors of H (because g_t=g_−t). Thus H is Galois invariant, an algebraic integer in Q, and therefore an **honest rational INTEGER**.

It follows that

    **B=H² in Z.**

This is true even when some twisted L-values vanish (then B=H=0). In particular B≥0 and the entire normalized spectral resultant is not merely a p-adic number but a global integer square.

Our independently proved deep Hecke/norm quadratic-jet theorem further implies for the p^k-admissible pair that
    **m² | B** in Z.
Because B=H² and m=p^k is a prime power, this gives m|H. Therefore

    **R = B/m² = (H/m)² is a PERFECT SQUARE in Z.**

This is a STRICTLY STRONGER theorem than the earlier primewise Boolean congruence R≡0 or1 modp.

### Important mathematical boundary

This perfect-square property comes from the Atkin–Lehner/Mazur–Tate **inversion functional equation**, not from the Cassels–Tate pairing. It is NOT an identification of R with #Sha nor with a Selmer Fitting determinant. Its analogy with square-order Sha is not evidence of BSD.

Likewise, H/m depends on p, n, g1,g2 and the selected diagonal cyclic quotient; it is NOT a single p-independent annihilator of Sha.

## 4. THREE actual exact integer witness calculations (assistant CPU, not synthetic)

**p5, k1, q=(41,61), m=5:**

    coefficients F: [-50,34,32,34,-50]
    λ_N = 1, shift s=4, h=3
    B=52128400=(7220)^2
    R=B/25=2085136=(1444)^2
    H/m mod5 can be ±1; positive sqrt R=1444≡4.

**p11, k1, q=(397,991), m=11:**

    coefficients F: [564,-414,344,-230,60,-42,-42,60,-230,344,-414]
    λ_N=0, shift s=0, h=0
    B=156470779894879023760384=(395563875872)^2
    R=B/121=1293146941279991931904=(35960352352)^2
    positive sqrt R ≡1 mod11.

**p5, k2, q=(5351,10651), m=25:**

    coefficients F:
    [-7110,5550,17732,17732,5550,-7110,-9364,-21952,-6882,376,19002,14602,8698,2028,-12468,-20424,-12468,2028,8698,14602,19002,376,-6882,-21952,-9364]

    λ_N=20, shift s=5, h=10
    B=23029075931778856293480525074058280758975693396694573028552616039759085259154270453760000
      =(151753339112452007665001265791485409507737600)^2
    R=B/625
      =(6070133564498080306600050631659416380309504)^2
    positive sqrt R ≡4 mod5.

The exact Frobenius shifts were recomputed from g1,g2 logs of N=389, **not fitted to the palindrome patterns**. Every coefficient symmetry a_j=a_((s−j) modm) was checked over Z, including the 25 integer coefficients obtained from the 28,488,750 authentic Manin plus reps.

## 5. Reproducibility

The code
    verification/bsd389_authentic_integer_cyclotomic_resultants.py
now checks:
- authentic raw 390-Manin vector SHA256 and all exact symbol sums;
- the TRUE integer resultants at m=5 and 11, and m=25 if given the full C++ histogram;
- exact shift s=−λ_N from the two genuine primitive roots and 389;
- coefficient-by-coefficient exact inversion;
- perfect-square resultants, the integral square roots √B and √R.

For full m25 run:

\`\`\`bash
g++ -O3 -std=c++17 \
  verification/bsd389_p5_depth25_full_integer_hist_native.cpp \
  -o /tmp/bsd389_hist25
/tmp/bsd389_hist25 > /tmp/bsd389_hist25.txt
python verification/bsd389_authentic_integer_cyclotomic_resultants.py \
  --depth25-hist /tmp/bsd389_hist25.txt
\`\`\`

These three source computations genuinely evaluated the polynomial coefficients from Manin data, not the earlier artificial polynomials in the general resultant gate. The user has previously executed the depth25 low-jet computation independently; **the NEW full INTEGER histogram/resultant/square-root check has not yet been independently rerun by the user.**

## 6. Global Sha/complex BSD boundary

The genuine new uniform theorem is:

    For EVERY p>=5, EVERY k>=1 and EVERY genuinely p^k-deep two-prime admissible pair,
      the actual normalized diagonal Mazur–Tate cyclotomic resultant
      is a PERFECT SQUARE integer.

With p-unit Kurihara coefficient it is a p-adic-unit perfect square ≡1 modp; with nonunit coefficient it is a p-divisible square. This **does not force** existence of a unit pair for all large p and does NOT prove a single p-independent Fitting determinant, Sha finiteness or the exact complex BSD rank-two formula.

The strongest next mathematical target is to construct a true Selmer-complex comparison for the **canonical half-character norm H/m**, now an honest integral square root of the normalized full twisted-L product. Nothing in Ota's functional equation alone constructs that map.
