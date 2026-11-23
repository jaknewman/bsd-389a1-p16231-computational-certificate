# Explicit maximal quaternion order for discriminant 389 containing O_{Q(sqrt(-43))}

**22 November 2026. Unconditional exact arithmetic theorem.** This note constructs an explicit global maximal order, checks every multiplication exactly, and gives an invertible integral local split chart at p=11 modulo 121. This is a valid starting point for the genuine norm-13 CM Gross orbit, but does **not** yet produce any Brandt eigenvector weights or a Selmer/Sha result.

## 1. The quaternion algebra really has discriminant 389

Take the rational quaternion algebra

    B = ( -43, -389 / Q ),
    i² = -43,  j² = -389,  ij=-ji,
    k = ij,   k² = -43*389 = -16727.

It is ramified at infinity (both parameters negative). At 389, Hilbert_389(-43,-389) is the Legendre symbol (-43/389)=-1. At 43, Hilbert_43(-43,-389)=(-389/43)=(-2/43)=+1. At 2, the odd parameters are 5 and 3 mod8, and the 2-adic Hilbert symbol is +1, since `(5-1)/2` is even. At every other odd prime both entries are units and the local Hilbert symbol is +1. Therefore the finite discriminant is precisely 389, as required for the definite Jacquet–Langlands algebra of E=389a1.

## 2. A genuinely maximal order, not just a local embedding

Let

    omega = (1+i)/2,         pi = 1+omega=(3+i)/2,
    J = (16*i + i*j)/43.

Then `omega² = omega-11`, `Norm(pi)=13`, `J²=-15` (thus Norm(J)=15) and, by direct quaternion multiplication,

    J*omega = (1-omega)*J - 16.

Consequently the rank-four lattice

    R = Z*1 + Z*omega + Z*J + Z*omega*J

is a subring containing 1: the displayed relations reduce every word in omega and J to a Z-linear combination of its four basis elements. Hence R is an **order**. Moreover R contains the full integer ring `O_K=Z[omega]` for K=Q(sqrt(-43)).

The integral Gram matrix of the reduced-trace product `trd(e_a e_b)` for the ordered basis `(1,omega,J,omega*J)` is

    G = [[  2,   1,   0, -16],
         [  1, -21, -16, -16],
         [  0, -16, -30, -15],
         [-16, -16, -15, -74]].

Exact integer determinant:

    det(G) = -151321 = -(389)^2.

The reduced discriminant of this order is therefore 389, **equal to the reduced discriminant of B**. Since a quaternion order is maximal iff its reduced discriminant is the algebra discriminant, **R is a maximal order**. The companion standard-library-only verifier checks the 16 basis products by exact rational-coordinate solving, not just the few defining relations.

## 3. A true local isomorphism R/121R --> M_2(Z/121)

At p=11, define the mod-121 splitting by

    i -> [[21, 0], [0, -21]],
    j -> [[ 0, 1], [-389, 0]].

These satisfy all three quaternion relations modulo121. In this matrix chart,

    omega -> [[11, 0], [0, 111]],
    pi    -> [[12, 0], [0, 112]],
    J     -> [[ 5,23], [114,116]],
    omega*J -> [[55,11], [70,50]].

In the matrix coordinate order `(x11,x12,x21,x22)`, the four columns for `(1,omega,J,omega*J)` form

    V = [[1, 11,   5, 55],
         [0,  0,  23, 11],
         [0,  0, 114, 70],
         [1,111, 116, 50]].

Its determinant is `35600 ≡ 26 (mod 121)`, which is **a unit modulo11**. Thus this chart sends the actual lattice R modulo121 **isomorphically** onto the full matrix ring `M_2(Z/121)`. An explicit verified inverse modulo121 is

    V^(-1) = [[12, 50, 77,110],
              [98,  5, 70, 23],
              [ 0,111, 88,  0],
              [ 0,120, 14,  0]] (mod121).

Therefore one can translate any matrix in the p=11 local split chart into **unique coordinates in the four-element global maximal-order basis modulo121**, without a Sage black box. This is the exact local lattice tool needed for implementing the 121-conductor Gross ideals.

## 4. Independent verification of the norm-13 cyclic CM class

Since `pi=(3+i)/2`, its split matrix is `diag(12,112)`, so the ratio of eigenvalues is

    12/112 ≡ 39 (mod 121).

The element 39 has order 110 modulo121; it generates the full ring-class group `Pic(O_121)≅C_110` established independently in the companion ring-class note. The 11-primary quotient has exactly 11 classes, each aggregating 10 right-ideal/class labels. Therefore the *same* global maximal-order element pi has

- quaternionic reduced norm exactly 13;
- class generator order 110 in the ring class group;
- split p=11 local matrix diagonal entries 12 and 112;
- quotient ratio 39 of order 110;
- an integral coordinate inverse in R modulo121.

This is a precise arithmetic foundation for source-normalized Gross computations. A **global oriented adelic right-ideal construction** and the Jacquet–Langlands/Brandt eigenform values have **not** yet been evaluated; this theorem cannot be used to assert a nonzero theta coefficient or an all-p Sha statement.

## 5. Next computation contract

Use the explicit maximal order R and its mod121 coordinate inverse to construct genuine right ideals `P_1^a` and `P_2^a` with the *exact* local Gross matrices from the published theta definition. Transport the first-layer class labels by the norm-13 class of pi, check full closure at 110 classes, compute their Brandt/Hecke eigenform values in the correct 389a1 eigenspace, then form the actual p-stabilized theta coefficients. Only after checking the complete source normalization can a nonzero quadratic coefficient be inserted into the p11 Selmer criterion.

This route avoids the previous enormous p=16231 orbit. It also never assumes that multiplying a global quaternion right ideal by pi automatically implements the required ring-class action: local adelic reciprocity and right-ideal conventions must be proved separately.

## References

- Kim (2026), anticyclotomic Selmer Fitting theorem, https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-the-fitting-ideals-of-anticyclotomic-selmer-groups-of-elliptic-curves-with-good-ordinary-reduction/D7D2EA9FA52A23B92319F3D44F5E9884
- Companion notes on the norm-13 ring-class generator and the rank-four Selmer augmentation reduction in this PR.