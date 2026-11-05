# Reduced oriented norm-19 Gross states and a single cyclic accumulator for the whole theta layer

**Date:** 2026-11-05. E=389a1, K=Q(sqrt(-3)), p=16231, m=p², f the exact 33D weight-2 Hecke eigenvector.

## Certified starting point

The user has genuinely run the conductor-one p4 local chart, built and classified P2(a=1), computed all 16231 points on the principal-unit coset a=(1+p)^i (moments [0,10775,5515]), and verified five nontrivial forward/backward norm19 strict ideal identities and an eight-step forward chain. The last real execution completed in 0.834 seconds. Source:
[results/bsd389_p16231_norm19_general5_forward8_chain_USER_PASS_2026-11-05.md](../results/bsd389_p16231_norm19_general5_forward8_chain_USER_PASS_2026-11-05.md).

The class of g=5+3omega is an exact primitive generator of Pic(O_m), cardinality H=87809710, with w=(5+3r0)/(5+3r1)=138112843 mod m. The split ratio's principal-unit component has exponent s=10816, i.e.

w = tau * (1+p)^10816 mod p²,
tau = w^p = 121898074.

## Key improvement: normalize BOTH the right ideal and its CM embedding

A state is not merely a 33-element Brandt class: it is

**(j,q)**, where 0≤j<33 and q∈R_j=left_order(I_j) satisfies
q²+m q+m²=0, Trd(q)=−m, Nrd(q)=m², and R_j∩Q(q) is the order of conductor m.

The initial state comes from the actual Gross point T(1)=J2(1)*I32 and q0=m*omega. Obtain its right equivalence witness alpha0 with alpha0*T(1)=I9, then put q_start=alpha0*q0*alpha0^(-1).

For each state (j,q), form

G(q) = 5+3q/m,   Nrd(G(q))=19,
D9(q) = R_j.left_ideal([q−9,19]),
T_new = (G(q)/19) * conjugate(D9(q)) * I_j.

Classify **with an exact witness** alpha*T_new=I_k. The successor is

**(k, q_next)** with q_next=alpha*q*alpha^(-1).

The orientation of q is transported along with the right ideal. Every q_next has the **same trace and norm** and lives in one of the same 33 fixed maximal orders. Since the definite quaternion norm is positive definite, for each fixed order R_j there are only finitely many integral q of the prescribed norm. Thus the normalized state cannot have coefficient blowup as n increases, unlike the naive iterated fractional ideals. An exact coefficient bound can be derived from each order's positive-definite norm Gram matrix.

Conjugating the existing all-a transport identity by alpha shows this normalized next-step construction represents the true Gross T(w a), not an arbitrary Hecke-19 neighbor. The general identity was derived and previously multi-anchor-tested in
[paper/bsd389_p16231_norm19_universal_Gross_transport_identity_local_global_proof_2026-11-05.md](../paper/bsd389_p16231_norm19_universal_Gross_transport_identity_local_global_proof_2026-11-05.md).

This is **not** a 33-state Markov transition: the exact CM embedding q is indispensable. Right ideal class j alone cannot determine the next j.

## Exact theta weights in ONE ring-class generator cycle

The old genuine n=1 theta formula is indexed by a∈mu_(p−1) and i∈Z/p via a*(1+p)^i, and has 3-fold redundancy from the globally certified CM order-3 unit. The norm19 ratio w is primitive in the quotient by that mu3, so the H values w^n, 0≤n<H, represent the complete ring-class set without duplication.

Write w=tau*(1+p)^s with s=10816. Then for w^n, the principal-unit coordinate is **i_n=s*n mod p**. The global mod-p coefficients k=0,1,2 of the finite n=1 theta are, using the exact P1 cancellation modulo p,

**c_k ≡ −3 alpha_p^(-2) sum_(n=0)^(H−1) binom(i_n,k) * phi_f(P2^(w^n)) (mod p),**

where alpha_p^(-2)=4986 mod p.

This formula is exact for the finite theta coefficients modulo p, provided the earlier CM-unit invariance and the Artin/local coordinate orientation are retained as certified. It is the crucial route from a nested (5410×16231) sum to a **single cyclic accumulator with small arithmetic weights**.

For n multiple of 5410, Teich(w^n) is one of mu3 and the resulting Brandt class/value equals that of the a=1 principal-unit orbit. Since s*5410 mod p = **1805**, the complete 16231-point run provides an independent check of this cyclic scheme **along the decimated subsequence** n=5410*t (t=0..p−1), with index i=1805*t modp. The full moment transformation must take into account this reordering of i, not naively compare moment vectors with the original i=0..p−1 order.

For the first 64 normalized steps (n=0,...,64), one accumulates only a **partial** cyclic moment. This number cannot prove any global c2 property and must not be compared to the first Teich i-orbit moment.

## New concrete Sage pilot, not yet user-run

[verification/bsd389_p16231_P2_norm19_reduced_oriented_chain_moment_pilot.py](../verification/bsd389_p16231_P2_norm19_reduced_oriented_chain_moment_pilot.py).

It normalizes P2^1 to class9 with exact right equivalence witness, transports q, iterates the oriented 19-neighbor, normalizes each next ideal back to I_j with a new exact witness, checks trace/norm/embedding integrality, compares periodic states to **independently reconstructed genuine P2(w^n)**, and builds the *partial* cyclic moments for k=0,1,2 using i_n=10816*n mod p.

The **previous user-certified eight classes** are a regression oracle:
n=0..8 classes = [9,2,1,21,9,1,26,3,12].

The pilot prints a bound on the observed integer coordinates of q in the fixed order bases. No assertion of reduced-orbit speedup is made until it actually runs and provides measured timings.

## Remaining prerequisites for a full 87.8-million-step certificate

1. Verify the normalized oriented state truly matches independent P2 anchors including embeddings, with no ambiguity from left-order unit groups.
2. Design checkpoint/restart and a compact stream of class indices and moment residues, not JSON entries per step for millions of steps.
3. Benchmark and accelerate exact class equivalence, which might still dominate. State normalization controls coefficient size but does not automatically remove expensive 33-class comparisons.
4. Obtain full cyclic coverage H and independently cross-check the previously certified complete Teich a=1 orbit through decimation.
5. Even if global c2 is proven nonzero mod p, check the exact lower-order vanishing hypotheses and the other Castella–Hsieh theorem conditions before asserting ord_T Theta=2 or any Sha p-primary conclusion.

**No global theta order-two, Sha finiteness or BSD result is asserted by the 64-step pilot.**
