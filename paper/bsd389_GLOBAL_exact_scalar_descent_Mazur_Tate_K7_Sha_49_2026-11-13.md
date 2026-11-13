# BSD 389a1 — Exact scalar contraction from the full Mazur–Tate theta over the degree-49 bicyclic extension

**13 November 2026. Independently executed exact 7-adic Smith/Bezout certificate. NOT the full BSD conjecture.**

Let E be 389a1 and K7/Q the real C7×C7 extension of conductor 76049=113·673. Write R=Z7[G], N_G=sum_{g∈G}g and θ the full canonical 49-coefficient integral Mazur–Tate group-ring element from the previously archived November 13 certificate. The involution and 7-adic period-unit normalization do not affect the scalar ideal contraction.

## The exact optimal ideal identity

**(θ,N_G)∩Z7 = 49·Z7.**

Construct the exact 49×50 integer convolution matrix [L_θ | N_G]. Its DVR Smith valuations, checked independently modulo 7^4, 7^8 and 7^12, are exactly **36 zeros, 6 ones, 7 twos**. Hence

    R/(θ,N_G) ≅ (Z/7)^6 ⊕ (Z/49)^7,

so 49 lies in the ideal while 7 does not. The complete reproducible 7^12 certificate provides A_12∈(Z/7^12)[G] and scalar B_12=1 such that

    θ A_12 + N_G B_12 ≡ 49 (mod 7^12 R),

checked again by all 49 group-ring convolution coordinates. All Smith valuations are <4, proving the exact p-adic identity independently of a mere finite-precision hypothesis.

**Second independent check:** the eight cyclotomic character-orbit norms of θ are nonzero, with 7-valuations (4,2,2,2,2,2,2,4). Their product D is a positive 98-digit integer with v7(D)=20, matching the Smith valuation sum 6+7·2=20. This proves that multiplication by θ is invertible on the nontrivial rational characters and cross-checks the full matrix determinant.

## Arithmetic implication for actual Sha over K7

Bullach–Honnor (2026), Theorem 1.4(b), applicable by prior large-image checks and the real field K7 (so ζ7∉K7), gives θ^#∈Fitt0_R(Sel_{7∞}(E/K7)^∨) and therefore an annihilator of the corresponding 7-primary Sha component after dualizing. Meanwhile Galois norm N_G=restriction∘corestriction annihilates Sha(E/K7)[7∞] because the prior independently archived E/Q Kurihara certificate proved Sha(E/Q)[7∞]=0.

The exact scalar identity proves, with these explicitly identified mathematical inputs:

    **49 · Sha(E/K7)[7∞] = 0.**

This gives finiteness and a *bound on exponent*, NOT the vanishing of Sha(K7)[7∞]. Optimality means only that 7∉(θ,N_G); it does not assert the actual Sha exponent is 49.

## Sharp p5 contrast

At K5/Q, the real C5×C5 extension of conductor 2501, the corresponding full 25-coefficient theta vanishes at the pure-character lines (1,0) and (0,1), eight nontrivial characters in total. N_G vanishes on these too; thus

    **(θ_K5,N_G) ∩ Z5 = 0**.

The direct 25×26 p-adic Smith computation confirms 8 zero pivots. Therefore the SAME scalar-descent strategy cannot produce any nonzero integer at p5, even though the primitive mixed jet is 4XY.

## Separate countermodel: mixed primitive jet is insufficient

For each p=5,7, set X=σ−1, Y=τ−1 and M=R/(X²,Y) ⊕ R/(X,Y²). Then M≅_{Zp}Zp²⊕(Z/p)² with a perfect G-invariant alternating pairing on the finite part. Its Fitting ideal equals (X³,XY,Y³), and the FULL authentic theta of both K5 and K7 belongs to that ideal, as checked from all 25/49 coefficients. Thus a primitive mixed jet plus a Fitting annihilator cannot by itself prove that Sha torsion is trivial.

## Additional arithmetic lattice result

GL2(F7) has no nontrivial 7-group quotient; hence K7 and Q(E[7]) are linearly disjoint. So E(K7)[7]=0 and E(Q)/7 injects into E(K7)/7. Using the rank E(K7)=2 previously inferred from Bullach–Honnor Thm 1.4(a), the p-adic Mordell–Weil lattices on Q and K7 agree.

## Reproducibility

The independently executed pure Python+SymPy source, full 25 and 49 integer theta coefficient grids, eight exact resultants, three 7-adic Smith reductions, modular Bezout witnesses including all 49 coefficients, complete logs, report JSON, proof note and SHA-256 manifest are in the current-conversation download:

    bsd389_exact_scalar_descent_K7_Sha_49_20261113.zip
    SHA256 42d787a5bf27ba336041561565fe3733e5674e11116eddcf9045e820580632d0.

Source: Bullach–Honnor, Theorem 1.4, https://dominikbullach.github.io/MazurTate.pdf . Neither a nonzero global Sha(E/Q) integer annihilator nor the exact complex rank-two BSD identity is asserted.