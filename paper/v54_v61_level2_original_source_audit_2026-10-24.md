# V54 and V61 original level-2 coefficient audit — 2026-10-24

Source commit: `69f1783`. Mathematical target: elliptic curve `389a1`, ordinary prime `p=16231`, Sage eclib modular symbol normalized `L_ratio`, cyclotomic parameter `gamma=1+p`, `eta=0`, `D=1`.

## Independently checked, from original committed data

The V54 summary has `a_covered=8115`, `terms=131714565`, `raw_half_sum_mod_p=0` and `a2_mod_p=0`. V54 computes the sum over `a=1,...,(p-1)/2`, `b=0,...,p-1`, with `u=(b/a-q_p(a)) mod p`, `q_p(a)=(a^(p-1)-1)/p mod p`, and weight `binom(u,2)`. It evaluates the eclib modular symbol `m((a+p*b)/p^2)` exactly as a rational and reduces it mod p.

V61 independently computes those raw eclib symbols mod `p^2` over the same half-range and checks each newly computed chunk against the corresponding V54 mod-p residue. Its level-2 `n=2` output is **not obtained from C01**. The original V61 summary records

```
p² = 263445361
alpha mod p² = 179060520
raw_f2 mod p² = 79629286
sum_f1 mod p² = 0
lower_term mod p² = 0
A2(n=2) mod p² = 19460969 = 1199*p
```

Independent modular arithmetic confirms

```
alpha²-128*alpha+p == 0 (mod p²)
alpha^(-1) == 249670441 (mod p²)
alpha^(-2)*79629286 == 19460969 (mod p²)
```

The main source formula is

`A2^(2) = alpha^-2 [ S2 - alpha^-1 * BINOM_SUM * S1 ] (mod p²)`,

where `S2` is the half-range weighted sum of `m(x/p²)`, `S1` the half-range sum of `m(a/p)`, and `BINOM_SUM=sum_(u=0)^(p-1) binom(u,2)=p(p-1)(p-2)/6`.

### Why only half of a ranges are needed

For the sign-plus modular symbol `m(-r)=m(r)`. The involution
`x=a+p*b -> p²-x = (p-a)+p*(p-b-1)`
identifies the `a` and `p-a` classes at level 2. Their cyclotomic exponents `u` agree, since `omega(-a)=-omega(a)`. Because `E.real_components()=2`, the two symmetric contributions cancel the factor `1/2` in the normalization. This justifies the half-range loop used by V54 and V61.

Furthermore `m(0)=0` because the original exact modular-symbol rank-2 certificate proves `L(E,1)=0`. The Hecke eigenrelation at `p`,
`sum_(a=0)^(p-1) m(a/p) + m(0) = a_p*m(0)`,
and the plus symmetry imply `S1=0` as a rational identity (assuming the stated normalization). Thus the V61 recorded `sum_f1=0 mod p²` has an independent conceptual explanation.

### What is and isn't independently computed

- V54 independently computes the finite-level coefficient modulo `p`.
- V61 independently computes the **finite-level `n=2`** coefficient modulo `p²`, through rational eclib modular symbols, not from C01.
- The direct source of V61 writes `C01_J=4486`, `V56_B_OVER_P=9534`, and explicitly marks the level-3 value **conditional**. No direct level-3 full enumeration occurs in V61.
- The source has 254 chunk intervals of at most 32 values of `a`, and each V61 chunk requires equality to the corresponding V54 residue. Previously, the current audit checked their original summary math, but not all 254 on-disk chunk records.
- The new `scripts/audit_v54_v61_level2_archive.py` performs that missing read-only all-chunk SHA and modular recomposition, including cross-version agreement, using historical files on IONOS.

### Precise bridge and theorem boundary

Mathematical identification of the C01 historical terminal with `J_ref`, plus the distribution/Teichmüller derivation from Sage, gives

`A2^(3)-A2^(2) == p*J_ref/(4*alpha²) (mod p²)`.

Since `J_ref = 4486` in the source-to-specification identification, the **conditionally inferred** analytic coefficient is

`A2^(3)/p = 1199+8335 = 9534 (mod p)`,

and the regulator gives `B_p/p=9534 (mod p)`. The quotient is a p-adic unit `A2/B_p = 1 (mod p)` **only in that sense**, not exact equality in `Q_p`. Applying Sage's proved `Sha.p_primary_bound` would then give exponent zero under the independently documented Galois/ordinary/precision gates.

**This audit does not claim that the direct Sage 10.9 `Sha.p_primary_bound(16231)` was executed or that full BSD is proved.** It does establish the exact source semantics and independent level-2 arithmetic reduction, leaving the trust chain for full C01 production/terminal and the historical chunk archives to be finalized.
