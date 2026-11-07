# GLOBAL BSD 389a1 — A mathematically decisive counterexample to a proposed uniform Sha theorem (Destrempes–Malinin 2018)

Date: 2026-11-07. PR #12. This is a mathematically sourced **negative result** which protects the global BSD project against falsely importing an all-prime Sha-vanishing theorem. No previous p=16231 / p=107 or local historical data were rerun.

## Statement being scrutinized

Destrempes–Malinin, arXiv:1703.02215v2 (2018), Theorem 5 on printed pp. 5–6, asserts that for a non-CM elliptic curve given by integral short Weierstrass equation y²=x³+Ax+B, a prime ell not in {2,3,5,7,13}, with full ell-adic GL2-image and ell∤(4A³+27B²), has no ell-primary Sha. For semistable curves it explicitly concludes this for ALL ell>=17 not dividing the discriminant. Published source: https://arxiv.org/pdf/1703.02215 , Theorem 5, printed pp.5–6, §4.5 proof pp.51–52.

The following is an *explicit incompatible test case* using a peer-reviewed theorem plus John Cremona's public exact rank-zero modular-symbol data; it is not a claim to have identified the offending line in the preprint's long cohomology proof.

## A precise semistable counterexample to the claimed implication

Take Cremona curve C = **226802e1**, with globally minimal Weierstrass equation
\[
C:\quad y^2+xy=x^3+x^2-4433709274x-120882223686060.
\]
Public original data: John Cremona repository `JohnCremona/ecdata/allbigsha/allbigsha.220000-229999`, exact line:
\[
\texttt{226802 e 1 [1,1,0,-4433709274,-120882223686060]\quad 0\quad1\quad289.}
\]
The fields represent MW rank 0, rational torsion order 1, and analytically predicted Sha order 289. For **analytic rank 0**, the L-value-over-real-period ratio is an **exact rational modular-symbol value**, unlike the rank-two conjectural ratio. Cremona's published ecdata description explicitly states this exactness for analytic rank 0: https://johncremona.github.io/ecdata/ .

Independent elementary integer calculations (short Python verifier added in the companion file) yield
\[
\boxed{N_C=226802=2\cdot151\cdot751,}
\]
\[
\boxed{\Delta_{\min}(C)=-2^6\cdot151\cdot751^9.}
\]
N is squarefree, so C is semistable, p=17 does NOT divide N or Delta, and the local reduction at 151 is type I_1. At p=17, independently count exactly 24 F17-points, hence
\[
\boxed{a_{17}(C)=17+1-24=-6\not\equiv0\bmod17.}
\]
Thus C has GOOD ORDINARY reduction at p=17.

The minimal discriminant exponents at the three bad primes are 6,1,9, so every local Tamagawa number is a divisor of the corresponding number (multiplicative I_n type). Thus every Tamagawa factor is a 17-adic unit. The MW torsion order is 1. The residual Galois image for this semistable non-CM curve at the good ordinary prime p=17 is surjective by Mazur's semistable result; independently, the *Cremona galrep file* `galrep/galrep.220000-229999` lists **226802e1 with no exceptional-image code**. Because v_151(Delta)=1 and p=17 does not divide 151-1=150, the mod-17 representation is ramified at q=151 (Tate curve with multiplicative parameter of valuation1). In fact the general Skinner–Urban corollary covers all semistable curves with good ordinary p>=11.

**Peer-reviewed arithmetic theorem:** Skinner–Urban, *The Iwasawa Main Conjectures for GL2*, Inventiones Math. 195 (2014), Theorem 3.6.11(a) (printed p.46), states for a semistable elliptic curve with good ordinary p>=11, surjective residual image, and a suitable ramified semistable bad prime:
\[
v_p\!\left(\frac{L(C,1)}{\Omega_C}\right)
=v_p(\#\Sha(C/\mathbf Q)[p^\infty])
+\sum_{\ell\mid N_C} v_p(c_\ell(C)).
\]
Primary source: https://www.math.columbia.edu/~urban/eurp/MC.pdf , Theorem 3.6.11 and following remark.

The **exact** rank-zero modular-symbol analytic data in Cremona give
\[
v_{17}\!\left(\frac{L(C,1)}{\Omega_C}\right)=2
\quad\text{(analytic Sha order 289=17², all Tamagawa p-units).}
\]
Applying Skinner–Urban therefore gives the genuinely ARITHMETIC conclusion
\[
\boxed{\#\Sha(226802e1/\mathbf Q)[17^\infty]=17^2=289>1.}
\]

This direct consequence of the cited established theorem, together with a catalogued exact central modular-symbol value, contradicts Destrempes–Malinin Theorem 5 for ell=17, as all its ell>=17 semistable hypotheses are satisfied. In particular the 2018 theorem must NOT be used to conclude Sha(389a1)[p∞]=0 for all p>=17.

## Short integral model confirms discriminant condition of Theorem 5

The standard change to integral short Weierstrass form y²=x³+Ax+B is
\(A=-27c_4,\ B=-54c_6\), with \(c_4=b_2²-24b_4\) and \(c_6=-b_2³+36b_2b_4-216b_6\). The elementary identity
\[
4A^3+27B^2=-2^8 3^{12}\Delta_{\min}(C)
\]
shows the **set of prime divisors of the short-model cubic discriminant** is exactly {2,3,151,751}; p=17 is not excluded.

## What this does and does not prove for 389a1

- It is a fully testable, concrete contradiction between the proposed broad 2018 theorem and a known rank-zero p-part BSD theorem with a catalogued exact rank-zero L-value.
- The contradiction is **not** based merely on a floating-point numerical coincidence, nor an assertion that all analytic BSD quantities in higher rank are exact. Skinner–Urban supplies the genuine Sha conclusion for this rank-zero example under verified hypotheses.
- The counterexample **does not prove or disprove** Sha finiteness for the original rank-two curve E=389a1, nor the rank-two exact complex L''/Omega/Reg equality.
- The original E=389a1 has conductor 389, and if the 2018 claim were sound it would appear to eliminate all p>=17 except p=389. This promised shortcut is invalid; do not record it as a proof.
- We have not identified the exact invalid sentence inside the 63-page preprint's §4.5 proof. The original theorem's broad conclusion cannot be simultaneously true with the validated rank-zero counterexample. Locating the specific failing lemma remains optional; it is unnecessary for rejecting the theorem as a dependency.

## References

1. Destrempes–Malinin, arXiv:1703.02215v2, Theorem 5, https://arxiv.org/pdf/1703.02215 .
2. Skinner–Urban, Invent. Math. 195 (2014), Theorem 3.6.11, https://www.math.columbia.edu/~urban/eurp/MC.pdf .
3. John Cremona ecdata, curve 226802e1 and analytic Sha 289, https://github.com/JohnCremona/ecdata/blob/master/allbigsha/allbigsha.220000-229999 .
4. John Cremona description of exact rank-zero analytic special values, https://johncremona.github.io/ecdata/ .
5. Cremona exceptional mod-p image list: https://github.com/JohnCremona/ecdata/blob/master/galrep/galrep.220000-229999 .
