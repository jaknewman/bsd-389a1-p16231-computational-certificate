# Towards D_+ for 389a1: unconditional 2-primary vanishing and the exact rank-two integral determinant gate

Date: 2026-10-27. **Outcome:** a genuine unconditional new-to-project 2-primary result, plus a sharper source-backed description of the arithmetic step missing to construct a global nonzero Fitting integer. This does **not** construct D_+ and does **not** prove global finiteness of Sha(E/Q).

## 1. Actual proved p=2 input for E=389a1

Let `E: y^2+y=x^3+x^2-2*x`. Magma's published official handbook, 'Mordell-Weil Groups and Descent Methods', contains the exact example

```
E := EllipticCurve("389a1");
time rank, gens, sha := MordellWeilShaInformation(E);
\u00a0\u00a0Torsion Subgroup is trivial
\u00a0\u00a0Analytic rank = 2
\u00a0\u00a0The 2-Selmer group has rank 2
\u00a0\u00a0After 2-descent:
\u00a0\u00a0\u00a0\u00a0 2 <= Rank(E) <= 2
\u00a0\u00a0\u00a0\u00a0 Sha(E)[2] is trivial
```

Original verifiable HTML source: https://www.math.uzh.ch/sepp/magma-2.25.2-ds/html/text1488.htm (exact same example). The Sage documentation independently gives `E.simon_two_descent() = (2,2,[(1:0:1),(-11/9:28/27:1)])`, and clarifies that for a curve with no rational 2-torsion its upper bound is precisely the 2-Selmer rank (https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html).

The global Kummer exact sequence yields

`0 -> E(Q)/2 E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0`.

Since `E(Q)_tors=0` and rank=2, the left vector space has dimension 2, and the published 2-descent verifies the middle one has dimension 2. Thus Sha[2]=0. Any nonzero 2-primary torsion group has a nonzero element of order 2, so

`Sha(E/Q)[2^infinity]=0` **unconditionally**, whether or not the full Sha group is finite.

Consequently `X_2=Sha[2^infinity]^vee=0` and `Fitt_0,Z_2(X_2)=Z_2`. This is an authentic proved D_+ **local** Fitting ideal equality.

## 2. Exact odd-square restriction on any hypothetical global D_+

The previous project proved the following equivalence for *all* primes:

`exists nonzero integer D_+ such that D_+ in Fitt_0,Z_p(Sha[p^infinity]^vee) for every p  <=>  Sha(E/Q) finite`.

The Magma 2-descent independently proves that if a global D_+ exists, we may take it **odd** (replace the original bound by `#Sha`, which then has no 2 factor). Furthermore, when Sha is finite the perfect alternating Cassels–Tate pairing implies that its order is a perfect square. Therefore

`[Sha finite] => [D_+ may be chosen as m^2, with m odd, hence D_+ ≡1 mod 8]`.

These are structural restrictions on a *future* D_+. They do not prove its existence, and a transcendental approximation to the BSD quotient near one does not create a Fitting annihilator.

## 3. A source-backed *precise* integral rank-two determinant target

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves* (JMSJ 76 (2024), 855–919), proves under mild assumptions an order-of-vanishing statement for a Darmon-type derived zeta element in arbitrary rank. Its **Generalized Perrin-Riou Conjecture** predicts the full leading-term equality in an appropriate integral determinant line in rank ≥2. The 2025 companion gives unconditional evidence for Mazur–Tate but not the required full equality.

For a prime p, a valid Fitting control would require a comparison between:

1. An **integral**, canonically normalized second-leading-term Euler/Kato class, viewed in the determinant lattice of a Selmer complex for `T_p(E)`, not merely in a rational H^1 line;
2. The exterior square of a **saturated** integral Mordell–Weil basis of E(Q), together with local period/regulator corrections at p and the bad prime 389;
3. The zeroth Fitting ideal of the finite Tate–Shafarevich dual `Sha[p^infinity]^vee`, with the correct local-condition and duality complexes.

A useful hypothetical **bounded defect** assertion has the shape

`D_+ ∈ Fitt_0,Z_p(Sha[p^infinity]^vee)` for every p,

where D_+ is a single nonzero **arithmetic integer obtained with a globally compatible integral normalization** of the derived zeta element. It is essential to prove this inclusion; choosing the term of the complex BSD quotient or an auxiliary quaternionic period norm as D_+ without a theorem is invalid.

**Mathematical no-go for the tempting shortcut:** Since `rank E(Q)=2`, the complex leading coefficient `L''(E,1)/2` and the Neron–Tate regulator are positive real numbers, but their ratio has no presently proved interpretation as a rational integer *without the very integral BSD leading-term theorem one is trying to establish*. Even a numerical interval containing exactly 1 among nearby squares does not establish finiteness of Sha.

At p=16231 the project's specific source-conditional Kato/Sage bound supplies a prime-primary result without such a global D_+. The order-nine Gross toric period gives a separate, conditionally nonzero generalized-Kato class over a cubic p-adic field, but does not produce the required integral Fitting comparison.

## 4. Why the rank-zero twist does not transfer an integral bound

Over `K=Q(sqrt(-3))`, for every odd p:

`Sha(E/K)[p^infinity] ≅ Sha(E/Q)[p^infinity] (+) ⊕ Sha(E^(-3)/Q)[p^infinity] (-)`.

The exact rational `L(E^(-3),1)>9/2` certificate plus Kolyvagin gives a genuine existential fixed bound D_- on the **minus** component, but no map of Selmer complexes is known in this project whose Fitting ideal of the minus component contains or controls that of the **plus** component. A direct-sum decomposition never bounds one summand by the other. This prevents an invalid 'transfer of D_- to D_+' claim.

## 5. Narrow research action, not another numerical checkpoint

Attempt to prove a **rank-two integral leading-term / finite-Sha Fitting inclusion** for E=389a1, starting with the BKS determinant-line theorem and an integral zeta element, rather than with the ordinary p-adic unit quotient or an auxiliary ring-class period. A genuine proof would have to show that the construction is compatible across *all primes*, including infinitely many supersingular ones. At present the required theorem is not established.

**Verified status:** p=2 component trivial unconditionally (Magma 2-descent). p=16231 component trivial only under project's previously documented source/computation hypotheses. D_- existence proved by rank-zero twist/Kolyvagin. D_+ existence, all-prime finiteness, full BSD are **NOT proved**.

## Sources

- Magma 2-descent for the exact model: https://www.math.uzh.ch/sepp/magma-2.25.2-ds/html/text1488.htm
- Independent Sage two-descent: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html
- BKS 2024 leading-term/vanishing distinction: https://doi.org/10.2969/jmsj/90699069
- BKS 2025 companion: https://doi.org/10.1093/imrn/rnaf012
- Earlier D_+ equivalence: [global Fitting integer ⇔ Sha finiteness](389a1_uniform_integer_fitting_equivalent_to_sha_finiteness_2026-10-26.md).
