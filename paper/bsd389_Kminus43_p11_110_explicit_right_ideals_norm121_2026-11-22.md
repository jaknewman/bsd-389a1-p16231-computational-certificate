# 110 explicit integral right ideals of norm 121 in the maximal order of discriminant 389

**22 November 2026 — proved exact integral lattice result.** This constructs 110 distinct global right ideals and verifies norm/index and 13-local transport. It does **not** identify them yet with the precise Gross right ideals `P_2^a` in Castella–Hsieh or evaluate a Jacquet–Langlands eigenvector.

## 1. The global maximal order and its exact p=11 matrix chart

Use B=(-43,-389)/Q and the **maximal** order R=Z[1,omega,J,omega J] constructed in the companion note, with omega=(1+i)/2 and J=(16i+ij)/43. The ordered basis of R maps modulo121 to

    e0 = [[ 1, 0], [ 0, 1]],
    e1 = [[11, 0], [ 0,111]],
    e2 = [[ 5,23], [114,116]],
    e3 = [[55,11], [70,50]].

The coordinate matrix V (columns these four vectorizations) has det=35600, a unit modulo121. Thus it induces an isomorphism `R/121R ≅ M_2(Z/121)`, with exact inverse

    V^(-1) = [[12, 50,77,110],
              [98,  5,70, 23],
              [ 0,111,88,  0],
              [ 0,120,14,  0]] (mod121).

## 2. Explicit family and proof of its ideal properties

For each a in `(Z/121)^×`, define the Z-lattice

    I_a = {x in R : (1,-a) rho_11(x) = (0,0) modulo121}.

Because `rho_11` is a ring homomorphism and the defining condition is stable under **right** multiplication by any 2×2 matrix, I_a is a right R-ideal. Since rho_11 is onto the full M_2(Z/121), the row map `x |-> (1,-a)rho_11(x)` is onto `(Z/121)^2`. Hence the **exact index** is

    [R:I_a] = 121^2 = 14641.

By the usual norm/index equality for integral right ideals in a quaternion maximal order, `Norm(I_a)=121`. The I_a are pairwise distinct: the matrix `[[a,0],[1,0]]` satisfies the a-relation but not the b-relation for b≠a.

The inverse chart gives two explicit column vectors in the global basis of R that, together with 121 times each basis vector, generate I_a:

    u_a = (12a+77, 98a+70, 88, 14) mod121,
    v_a = (50a+110, 5a+23, 111a, 120a) mod121.

Here coordinate representatives from 0 to120 are used, and `121 R` supplies the missing integer lifts. The 110 unit values of a give 110 distinct global ideals.

**Concrete example, a=1.** The Hermite-normal-form integral basis is

    I_1 = Z*(121)
        + Z*(121 omega)
        + Z*(32+73 omega+J)
        + Z*(4+89 omega+omega J).

The integer determinant of its four coefficient columns is exactly 14641. Substitution into the matrix chart verifies both row congruences for all four generators; multiplying by the four basis elements of R preserves the congruences.

## 3. Verified norm-13 local cyclic transport

Recall pi=1+omega of reduced norm13 and its matrix D=diag(12,112) modulo121. Since 11∤13, D is invertible in M_2(Z/121). Conjugating the local matrix ideals gives

    D^(-1) rho_11(I_a) D = rho_11(I_{a*(112/12)}).

But `(12/112)=39 mod121` has order110, so the transformation sends a to `a*39^(-1)` and cycles through **all 110** unit slopes starting from a=1. Both row generators and right closure have been checked by exact modular 2×2 integer arithmetic for every k=0,...,109.

This is a **local** conjugation statement, not a claim that global quaternion conjugation by pi preserves the selected global order at the primes dividing Norm(pi)=13. The global CM reciprocity/Brandt orientation still requires proof.

## 4. Meaning for the next genuine Gross computation

We now possess a maximal order with integral structure constants, an exact 121-local coordinate inverse, and 110 globally defined right ideals I_a of the expected norm for the conductor-121 stage, permuted locally by norm13 CM multiplication. The remaining **nontrivial** step is to establish the source-level identification with Chida–Hsieh / Castella–Hsieh `P_2^a` and their companion conductor-11 ideals, then compute the 389a1 Brandt eigenform on these classes. Only authenticated, p-stabilized weights could prove a quadratic theta coefficient and feed the p11 Selmer matrix test.

## Exact reproducibility

The companion Python checker `verification/bsd389_Kminus43_p11_norm13_right_ideal_orbit_110_certificate.py` uses only standard-library integers. It enumerates 110 distinct slopes, computes their global-coordinate generators, verifies right closure under all four maximal-order basis matrices, validates 121² index by the surjective row map, and checks transport. The example HNF basis may be independently reproduced by exact integer row/column operations.