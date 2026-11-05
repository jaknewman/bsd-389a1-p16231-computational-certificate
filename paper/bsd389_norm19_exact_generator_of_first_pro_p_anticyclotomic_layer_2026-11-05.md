# 389a1, K=Q(sqrt(-3)): the old norm-19 ideal GENERATES the first p=16231 anticyclotomic layer

**Date:** 2026-11-05. A new *exact local/Galois* bridge from the previously studied norm-19 class to the p-power conductor tower. This note does NOT construct the Gross points or compute theta derivatives. It is independent of Sha.

## 1. The natural order-p quotient

Let p=16231, O_K=Z[omega], omega²+omega+1=0, and O_m=Z+m O_K. The prime p splits (p=1 mod3), and K has class number 1. The ring-class exact sequence yields

Pic(O_(p^n)) ≅ (O_K / p^n O_K)× / ((Z/p^n)× O_K×).

For n≥1, |Pic(O_(p^n))|=p^(n−1)(p−1)/3. Thus Pic(O_p) has order 5410, prime to p, whereas Pic(O_(p²)) has order 5410·16231. The kernel of the natural projection Pic(O_(p²))→Pic(O_p) is cyclic of order p.

Hensel lifts of the two omega embeddings to Z/p² are
r0=49689135 and r1=213756225, with r0+r1≡−1 and r0 r1≡1 mod p².

## 2. A canonical explicit character

For a local unit β=a+b omega mod p² define the split ratio

w(β) = (a+b r0)/(a+b r1)  (mod p²).

Define

L_p(β) = [w(β)^(p−1)−1]/p (mod p).

Since w^(p−1)≡1 modp, the quotient is well-defined. It is additive under multiplication: L_p(βγ)=L_p(β)+L_p(γ) modp. Rational scalars have ratio 1, and O_K×=mu_6 has split ratio a third root of unity (killed by the (p−1)th power). Therefore L_p descends to a homomorphism Pic(O_(p²))→F_p. It is surjective because L_p(1+p omega)=4142 !=0. Since the entire p-primary subgroup has order p, L_p restricts to an isomorphism there.

This is a coordinate on the **first p-primary Galois layer**, not a Gross-point evaluation. Swapping the chosen p-adic embedding order sends L_p to −L_p.

## 3. The norm-19 ideal from conductor 53

Let g=5+3omega. Norm(g)=19, so g represents a prime ideal above 19 (up to inverse orientation), coprime to the p-power conductor. Direct exact modular calculations give

L_p(g)=5415 (mod16231).

Put h=|Pic(O_p)|=5410 and G=[g]^h ∈ Pic(O_(p²)). Its image in Pic(O_p) is 1, and

L_p(G)=5410·5415=14426 (mod16231) !=0.

Therefore **G generates the entire kernel Pic(O_(p²))→Pic(O_p)** of order p. The exact multiplicative inverse 14426^(-1) is 15071 modulo p. Thus the norm-19 class, after killing its p'-part, supplies an explicit generator of the first anti-cyclotomic p-layer.

The local 2-component representation of g^5410 modulo p² is exactly
G=(144261128,166000481) in the basis (1,omega). Its split ratio is w(G)=148945842 modulo p². Its cube is nontrivial mod p² but its 3p-th power is 1: this independently confirms order p **after quotient by the global unit ratios mu_3**.

An assistant-side standard-library Python calculation checked **all 16,231 successive powers G^i**, i=0,...,p−1, by comparing the independently computed split CRT log to i·14426 mod p, with zero collisions. This is an executed algebraic check in the assistant runtime; the published source needs user Ubuntu replay for the project provenance.

## 4. Convert to a local ratio 1+p

Put U=12089+p·omega. The exact CRT ratio is

w(U) = 1+p (mod p²).

Thus L_p(U)=p−1=−1. The comparison

U=G^1160  in Pic(O_(p²)),    G=U^1805

holds, since 1160·14426≡−1 and 1160·1805≡1 mod p. Explicitly the ratio w(U)/w(G)^1160 is a root of unity of order three, so the equality holds in the **actual** ring-class quotient, not merely after comparing an abstract log.

If gamma_G=gamma_U^1805, then for a theta series represented in these normalized first-layer coordinates,
F_U(T)=F_G((1+T)^1805−1), so a quadratic leading term transforms by
c_(2,U)=1805² c_(2,G)=11825 c_(2,G) (mod p).
The reciprocal change has square 1160²=14658, and 11825·14658≡1 mod p. These scalars are units, so existence of a nonzero quadratic term is invariant.

**Convention caveat:** the local Artin map, placement of r0/r1 in the chosen quaternionic embedding, and the normalizations used by Castella–Hsieh can replace either generator by its inverse. The equality above is exact in the explicitly defined CRT convention; it must be checked against any actual quaternionic Gross-point construction before identifying the authors' canonical gamma. The vanishing order and p-adic unit/nonunit status of c2 are independent of such unit-coordinate changes.

## 5. Exactly what this does (and does not) solve

**New:** produces an explicit generator of the order-16231 ring-class quotient using the already known norm-19 prime; exact coordinate/discrete logarithm in first layer, no new large q and no abstract Chebotarev argument. This offers a direct route to label future p² Gross points by the same norm-19 ideal action that drove the previous conductor-53 quaternion orbit.

**Not done:** the conductor-53 orbit itself is **not** an orbit at conductor p². A genuine optimal embedding O_(p²) into a suitable Brandt left order and exact 19-neighbor transport data at that conductor are required before applying these coordinates to Gross points. Neither theta coefficient c2 nor its order of vanishing has been computed. No new Sha result follows from the local generator alone.

Run [the independent exact first-layer generator verifier](../verification/bsd389_p16231_ringclass_norm19_first_layer_generator.py) and see [the authenticated Ubuntu preflight](../results/bsd389_p16231_anticyclotomic_first_layer_PREFLIGHT_USER_PASS_2026-11-05.md).

Published theta point construction: Castella–Hsieh, *On the non-vanishing of generalized Kato classes for elliptic curves of rank two*, Appendix, https://web.math.ucsb.edu/~castella/Kato.pdf .
