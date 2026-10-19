# 389a1 — 3-primary Tate–Shafarevich subgroup trivial by full 3-Selmer descent

**Date:** 2026-10-19. **Magma:** V2.29-10; reported wall time 3.1 s (CPU 2.68 s); memory 32.09 MB; seed `2502566654`.

## Source (online Magma, run provided by researcher)

```magma
Q := Rationals();
E := EllipticCurve([Q | 0, 1, 1, -2, 0]);
S, phi := ThreeSelmerGroup(E);
print "THREE_SELMER_ORDER", #S;
print "THREE_SELMER_GROUP", S;
```

Original output:

```text
CURVE Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field
THREE_SELMER_ORDER 9
THREE_SELMER_GROUP 
Abelian Group isomorphic to Z/3 + Z/3
Defined on 2 generators
Relations:
3*S.1 = 0
3*S.2 = 0

# 3.1s · Magma V2.29-10 | 2.68s | 32.09MB | seed 2502566654
```

## Rigorous interpretation

The official Magma manual states that `ThreeSelmerGroup(E)` computes the full 3-Selmer group as an abelian group. For rational `E=389a1` the output has order 9, hence `dim_F3 Sel_3(E/Q)=2`.

From the independently certified Mordell–Weil rank `r=2` and torsion subgroup `E(Q)_tors=0`, `E(Q)/3E(Q) ≅ (Z/3)^2` also has order 9. The exact Kummer sequence

`0 → E(Q)/3E(Q) → Sel_3(E/Q) → Sha(E/Q)[3] → 0`

therefore implies `Sha(E/Q)[3]=0`. If an element had order `3^k` for any `k≥1`, multiplication by `3^(k-1)` would give nonzero 3-torsion, impossible. Thus

`Sha(389a1/Q)[3^infinity]=0`.

This is a **single-prime exact algebraic conclusion** based on a full 3-descent, not an assumption of the BSD formula or the 16231 C01 calculation.

## Verification assumptions and sources

Magma official documentation describes `ThreeSelmerGroup` as returning the *3-Selmer group*, not merely an experimental list. Its class-group computations use mathematically guaranteed bounds by default; a GRH-conditional mode is enabled by an explicit `SetClassGroupBounds("GRH")` command. The supplied one-off Magma input did **not** enable GRH mode, and the supplied output contains no warning. A reviewer may rerun in a clean session for independent reproducibility.

- Magma's 3-Selmer documentation (historical official manual): https://www.math.uzh.ch/sepp/magma-2.20.4-cr/HandbookVolume10.pdf
- Current Magma class-group proof settings: https://docs.magma-maths.org/GlobalFields/NumberFieldsAndOrders/ideal-class-group.html
- [Full BSD exact 2-primary certificate](full_BSD_sha_2_primary_TRIVIAL_PASS_2026-10-19.md)
- [Full BSD 5/7/11/13 certificates](full_BSD_sha_5_7_11_13_primary_TRIVIAL_PASS_2026-10-19.md)

## Remaining global obstacles

This does not imply `Sha(E/Q)=0` or even global finiteness without control at every other prime; nor does it demonstrate exact `L''(E,1)/2 = Ω_E Reg(E)`. `p=16231` continues to have a separate computer-assisted conditional certificate.
