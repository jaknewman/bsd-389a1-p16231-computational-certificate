# A constructive split-local quaternion chart for the anticyclotomic Gross-point tower at p=16231

**Date:** 2026-11-05. Code has been committed, **not yet user-run**.

## Setup

Let B/Q denote the quaternion algebra ramified at 389 and infinity, R_i the maximal left order of a certified Brandt ideal representative at E389a1. From genuine Stage14 with conductor-53 optimal embedding choose q∈R_i satisfying q²−q+2107=0. Put ω=(q−27)/53, so ω²+ω+1=0. Although ω is not in R_i globally (conductor53 optimal), it belongs to the *p-adic completion* R_i⊗Z_p because 53∈Z_p× for p=16231.

Let p=16231, M=p²=263445361. Fix exact Hensel roots r0=49689135, r1=213756225 of t²+t+1 mod M. Their difference is a p-adic unit.

## Step 1: primitive local idempotents

In B⊗Z/M define

e=(ω−r1)/(r0−r1), f=1−e.

The quadratic polynomial factors as (ω−r0)(ω−r1)=0 mod M, and hence e²=e, f²=f, ef=fe=0, e+f=1 in B⊗Z/M; reduced traces are 1,1. This gives a split torus chart whose first diagonal entry corresponds to ω=r0 and second to ω=r1. This *does not* require choosing a global maximal-order embedding at p-power conductor yet.

## Step 2: find an integral off-diagonal matrix unit

Choose an integral Z-basis b0,...,b3 of R_i and search for a pair with x=e b_i f, y0=f b_j e such that the scalar c=Trd(x y0) is a unit mod p. Since R_i is maximal at p and B splits, its completion is M2(Z_p); such a pair must exist.

Put y=c^(−1)y0 mod M. Peirce multiplication gives xy=e, yx=f, x²=y²=0, e x=x=x f and f y=y=y e. Thus e,x,y,f are 2×2 matrix units E11,E12,E21,E22 over Z/M.

## Step 3: construct and verify algebra isomorphism

For each b∈R_i⊗Z/M define

rho(b)= [[Trd(e b e), Trd(e b y)],
          [Trd(x b e), Trd(f b f)]].

Each entry is reduced modulo M using denominator inversion only at p-adic units. Matrix-unit relations prove rho is a unital algebra homomorphism carrying ω to diag(r0,r1). Because the four matrix units span M2(Z/M), rho is surjective. Checking invertibility modulo p of the 4×4 matrix sending the chosen integral order basis to the four entries gives an isomorphism of free Z/M-modules as well.

The source-level Sage script [verification/bsd389_p16231_brandt_local_split_matrix_units.py](../verification/bsd389_p16231_brandt_local_split_matrix_units.py) checks every identity with exact rational quaternions and reduction modulo M, including all 16 products b_i*b_j, determinant/trace identities, and the diagonalization of the historic q. It records the local 2×2 images of each order basis vector in a compact JSON report.

**Important:** this is an explicit local chart for a genuine previously certified global *conductor53* embedding; it is NOT an optimal embedding of the higher conductor O_(p²) into the same left order. Next, one must construct the actual adelic Gross-point representatives associated to p-power conductor, with the correct orientation/normalization, before classifying them into the 33 Brandt indices.

## Scope

The script has not been executed on user's Ubuntu as of note creation. A successful run establishes the local splitting and chart needed for the p-adic unipotent action, **but neither the 263 million actual Gross evaluations nor a theta coefficient**. The trivial-character anticyclotomic theta series is different from the order-nine character of conductor53. The p-primary Sha group and full BSD are not resolved by this local chart.

For the exact first-layer norm19 generator and change of local coordinate, see [norm19 generator paper](bsd389_norm19_exact_generator_of_first_pro_p_anticyclotomic_layer_2026-11-05.md). For the real CH theta expression, see [the first layer research plan](bsd389_castella_hsieh_theta_trivial_character_first_p_layer_exact_plan_2026-11-05.md).
