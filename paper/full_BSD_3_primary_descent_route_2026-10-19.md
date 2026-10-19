# Global BSD — p=3 descent: tool availability and exact isogeny obstruction

Date: 2026-10-19. Curve: E/Q y²+y=x³+x²−2x, Cremona 389a1.

User's SageMath 10.9 IONOS terminal:
```text
MAGMA_EXECUTABLE None
THREE_SELMER_AVAILABLE True
RANK 2
TORSION 1
```

The Sage method `E.three_selmer_rank()` exists, but its implementation delegates to Magma and cannot run locally when the `magma` executable is absent. This is **not** a failure of a mathematical 3-Selmer computation; the group has not been computed.

## Exact obstruction to 3-isogeny descent

For `[a1,a2,a3,a4,a6]=[0,1,1,-2,0]` the invariants are `b2=4,b4=-4,b6=1,b8=-3`. The 3-division polynomial is

```text
psi_3(x) = 3x^4 + 4x^3 - 12x^2 + 3x - 3.
```

Rational-root candidates by the rational-root theorem: `±1,±3,±1/3`. Direct substitution gives nonzero values in every case; consequently there is **no rational root**. A Q-rational cyclic subgroup of order 3 would have rational x-coordinate for its nonzero points, so this curve has **no rational 3-isogeny**. Full 3-descent, not isogeny descent, is the appropriate algorithmic route.

## Online Magma computation requested (NOT YET RUN)

Magma's official web calculator: https://magma-maths.org/calc/

```magma
Q := Rationals();
E := EllipticCurve([Q | 0, 1, 1, -2, 0]);
S, phi := ThreeSelmerGroup(E);
print "THREE_SELMER_ORDER", #S;
print "THREE_SELMER_ABSTRACT_GROUP", S;
```

Magma's handbook documents `ThreeSelmerGroup(E)` as returning an abelian group together with a map. It performs general full 3-descent even without a rational 3-isogeny.

If `#S = 9` (dimension 2) and MW rank=2, torsion=1, the Kummer sequence yields `Sha(E/Q)[3]=0`, hence `Sha(E/Q)[3^infinity]=0`, regardless of the overall finiteness of Sha. If `#S` exceeds 9, interpret the excess as potential 3-torsion Sha and analyze the computation rather than assert expected values.

**Proof rigor note:** do not enable Magma `SetClassGroupBounds("GRH")` in this test if the goal is a result free from GRH assumptions. The online browser calculator can impose short runtime limits. Capture the actual output, Magma version and any warnings or conditional flags. No 3-primary triviality can be claimed before a certified Selmer output.

Sage documentation: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html

Magma documentation: https://magma.maths.usyd.edu.au/magma/handbook/text/1565

Magma browser calculator: https://magma-maths.org/calc/
