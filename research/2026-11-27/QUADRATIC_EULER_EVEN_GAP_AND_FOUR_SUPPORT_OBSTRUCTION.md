# BSD 389a1 — Quadratic Euler symbol, even Kurihara gap and a genuine four-support obstruction

**27 November 2026 | theorem-level arithmetic + exact finite computations | NOT a proof of H₂ or full BSD.**

## A. Universal second augmentation jet (proved)

Let p>=5 be a good prime for E: y²+y=x³+x²−2x, and let q be a Kurihara prime: q≡1 (mod p), a_q(E)≡q+1 (mod p). Its Euler factor P_q(X)=1−a_qX+qX² satisfies the **exact identity over Z**

    P_q(1+Y) = (q+1−a_q) + (2q−a_q) Y + qY².

Both constant and linear terms are in p Z, whereas q is a p-unit. Therefore

    P_q(1+Y) ≡ Y² (mod p).

If q≡1 (mod p^m) and a_q≡q+1 (mod p^m), the same identity holds (mod p^m). Equivalently, for any group-ring element sigma, P_q(sigma^{-1}) lies in pR+I² and its degree-2 symbol in R/(p,I³) is (sigma^{-1}−1)². As a **formal polynomial in Y** it has a double zero and no triple zero; in a specialized group ring the image of (sigma^{-1}−1)² can itself vanish, which does not change the formal coefficient statement. This is only a statement about the Euler factor, *not* a construction of a derived Kato class.

**Consequence**: corestriction alone has augmentation P_q(1)=#E(F_q) divisible by p, and its first augmentation jet is also zero modulo p. A primitive descent therefore cannot be produced merely by evaluating the ordinary norm relation at augmentation or by extracting its first jet. The quadratic associated-graded term has coefficient one, and is a concrete target for a **secondary Bockstein** comparison.

For examples, direct finite-field point counts show:

| p | q | a_q | #E(F_q) | (2q−a_q) | minimal p-adic congruence |
|--:|--:|--:|--:|--:|--:|
|5|41|−3|45|85|p|
|5|61|−8|70|130|p|
|7|113|9|105|217|p|
|7|1429|−5|1435|2863|p|
|5|5351|−23|5375|10725|p²|
|5|10651|2|10650|21300|p²|
|7|9311|−96|9408|18718|p²|

The script `verification/bsd389_double_augmentation_gate.py` tests 11 Kolyvagin primes by exact integer point counts and quadratic polynomial coefficients.

## B. Deep congruence rigidity (published, carefully scoped)

Castella–Sano (2026), Proposition 2.1.5, proves for **Kato's Kolyvagin system** that its eventual minimal p-divisibility is unchanged when all Kolyvagin primes are required to satisfy arbitrary prescribed p^m-level congruences. Their proof uses prime replacement while **preserving the number of factors** of a primitive witness.

This means we may work with very deeply congruent auxiliary primes without automatically losing global primitive classes. The proposition does NOT itself lower an r-factor primitive class to degree r−2, and the Kato-to-Kurihara comparison can carry the local factor #E(Q_p)[p∞] (Castella–Sano, Theorem 2.1.3). Any claimed transfer to delta's must account for that factor.

## C. Even valuation-gap theorem (deduced, not conjectural)

Let M_{2j}(p) be the minimum p-adic divisibility of Kurihara numbers with exactly 2j auxiliary factors, and let rho denote the least support of a nonzero Kurihara coefficient in its full p-primary quotient. Under residual surjectivity and p-integral Manin constant:

- Castella–Sano, Theorem B: M_infty(p)=0 at all good p>3 for this semistable squarefree-conductor curve, since c_389=1.
- Kim, Theorem 1.8(1): rho = corank_{Z_p} Sel_{p∞}(E/Q). Since rank E(Q)=2, rho>=2.
- If M_2(p)<∞, then rho=2. Kim's Theorem 1.8 explicitly writes the **finite** part of Selmer as paired cyclic modules with exponents (M_{2j}−M_{2j+2})/2. Hence every consecutive finite difference is even; in particular

    M_2(p) ∈ 2 Z_{>=0} ∪ {∞}.

If M_2<∞, the equality M_infty=0 and rho=2 also imply

    v_p(#Sha(E/Q)[p∞]) = M_2(p),

and the finite p-primary Sha has square order. This uses Kim's theorem, not a prior assumption that Sha is finite: rho=2 forces the divisible Selmer corank to be entirely accounted for by the two Mordell–Weil classes.

**New useful criterion.** If at some *two-factor* admissible level n=q1 q2 with p² | I_n we find delta_n ∈ p(Z_p/I_n) but delta_n ∉ p²(Z_p/I_n), then M_2<=1. Since M_2 is even, M_2=0. Therefore a **different p-unit two-factor witness must exist**, and Sha(E/Q)[p∞]=0. Thus a valuation-one certificate suffices even though it is not itself a unit witness.

This is a corollary of known theorems sharpened for our curve, not a solution of the uniform case. The filtration profile M_2=2, M_4=0, M_infty=0 remains algebraically permitted (it corresponds to Sha[p∞]≈(Z/p)^2), so global primitivity does not automatically imply degree-two primitivity.

## D. New four-support calculations: two-sided failure of Pfaffian contraction

Using exact integral Manin continued fractions and discrete logs modulo 5, compute delta at 2 and 4 auxiliary primes, all within {41,61,131,211,251}. The code scans one half of the units using plus symmetry; for two pivotal quadruples it independently scans **every unit** and obtains the same result.

For a fixed ascending quadruple (q1,q2,q3,q4), set

    Pf(q) = δ12 δ34 − δ13 δ24 + δ14 δ23 (mod 5).

This is the pfaffian of a *conventionally antisymmetrized* matrix and is not intrinsically a symmetric arithmetic scalar. The exact outputs are:

| quadruple | δ_{q1q2q3q4} mod 5 | Pf of pair δ mod 5 | symmetric Wick pair sum | connected four-way defect |
|---|---:|---:|---:|---:|
| 41,61,131,211 | **2** | **0** | 3 | 4 |
| 41,61,131,251 | **0** | **4** | 1 | 4 |
| 41,61,211,251 | 0 | 3 | 2 | 3 |
| 41,131,211,251 | 4 | 0 | 4 | 0 |

The first two results were checked by **full and half residue scans**, agreeing exactly. Thus no formula of the form δ4 = u·Pf(δ2) with u a p-adic unit can work on all quadruples, **independently of ordering or primitive-root choices**: we have both δ4 unit / Pf zero and δ4 zero / Pf unit.

The *symmetric, root-unit covariant* diagnostic

    K4 = δ1234 − (δ12δ34 + δ13δ24 + δ14δ23)

is 4,4,3,0 (mod 5) in these four tests. Each δ2 and δ4 changes by the product of the corresponding individual log-generator units; the entire K4 scales by the product over all four primes. Hence zero/nonzero of K4 does not depend on primitive-root choices, although it depends on the fixed Néron symbol normalization. **K4 is currently a numerical connected-four-factor diagnostic, not an identified cohomological class.** Its cohomological identification is a concrete new research target.

## E. The precise remaining global theorem

Construct and verify a **secondary (quadratic) Bockstein** map for Kato-derived classes, with the following three separately audited properties:

1. It is well-defined and integral in the *global Selmer complex* (not merely in the group ring after reduction modulo p).
2. Its reciprocity formula includes the nonseparable connected four-factor correction observed above; it is **not** a purely separable 2-by-2 pfaffian.
3. It transfers a primitive class of r>=4 auxiliary factors to some class of r−2 factors without creating p-divisibility. This cannot follow just from the local Euler polynomial identity: the obstruction lies in global cohomology / Selmer H².

With those properties, the Castella–Sano primitive witness at some finite support could be descended to support 2, proving the good-prime components of Sha vanish. They are **not currently proved**, so neither H2 nor global BSD is claimed.

### Primary sources

- F. Castella & T. Sano (2026), *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B, Theorem 2.1.3, Proposition 2.1.5: https://arxiv.org/abs/2601.14504
- C.-H. Kim (2025), *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- D. Burns, M. Kurihara & T. Sano (2024), *On derivatives of Kato's Euler system for elliptic curves*: https://doi.org/10.2969/jmsj/90699069