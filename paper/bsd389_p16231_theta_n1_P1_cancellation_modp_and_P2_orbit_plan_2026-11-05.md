# Genuine Gross P0,P1,P2: exact theta-n1 coefficient reduction modulo p

**Date:** 2026-11-05. E=389a1, p=16231, K=Q(sqrt(-3)), **trivial character**, global conductor-one quaternionic CM base Brandt index32. This is about the actual Castella–Hsieh anticyclotomic theta, **not** the conductor-53/chi9 auxiliary toric polynomial.

## Real new finite arithmetic

The user's Sage execution certified the actual n=2 Gross point at unit a=1, with global right ideal lattice index p^8, independent two-congruence/HNF equality and sixteen right-order closure checks, plus exact quaternionic right-ideal equivalence witness for Brandt class9, hence phi_f(P_2^1)=v[9]=−1. Earlier Sage user execution independently certified phi_f(P_1^1)=v[29]=−2 and conductor-zero phi_f(P_0^1)=v[32]=0.

Therefore one **individual n=1 bracket** at a=1,i=0 is alpha_p*(−2)−(−1)=1−2alpha_p ≡−255 modp. This is not a whole theta value, coefficient or derivative. The actual user's final n=2 output and source are recorded in [results/bsd389_p16231_P2_a1_class9_USER_PASS_2026-11-05.md](../results/bsd389_p16231_P2_a1_class9_USER_PASS_2026-11-05.md).

## Exact P1 independence of the anticyclotomic i-exponent

The n=1 finite-theta formula of Castella–Hsieh, Appendix, with u=1+p, is

Theta_(f/K,1)(T) =
alpha_p^(−2) ∑_(i=0)^(p−1)∑_(a∈mu_(p−1))
[alpha_p phi_f(P_1^(a u^i)) − phi_f(P_2^(a u^i))] (1+T)^i.

For *every* p-adic unit a and every integer i,

a u^i ≡ a (mod p).

Since the local adelic representative r_1(b)=[[1,b/p],[0,1]] satisfies
r_1(b+p z)=r_1(b)*[[1,z],[0,1]] and the right factor belongs to GL2(Z_p), the right quaternionic Gross ideal P_1^(a u^i) equals P_1^a as an adelic right class. Its Brandt eigenvalue is therefore independent of i:

phi_f(P_1^(a u^i))=phi_f(P_1^a).

Consequently for k=0,1,2,

[T^k]Theta_(f/K,1)(T) =
alpha_p^(−2) [alpha_p S_1 ∑_(i=0)^(p−1) binom(i,k)
           − ∑_(i=0)^(p−1) binom(i,k)∑_a phi_f(P_2^(a u^i))],

where S_1 =∑_a phi_f(P_1^a) is independent of i.

The hockey-stick identity ∑_(i=0)^(p−1)binom(i,k)=binom(p,k+1) and prime p>3 imply binom(p,k+1)≡0 (modp) for k=0,1,2. Thus we obtain the exact *mod-p* reduction

**[T^k]Theta_(f/K,1) ≡ −alpha_p^(−2)∑_i binom(i,k)∑_a phi_f(P_2^(a u^i)) (modp), k=0,1,2.**

Here alpha_p^(−2)≡4986 modp. In particular

c2 modp ≡ −4986 ∑_(i=0)^(p−1)binom(i,2)∑_(a∈mu_(p−1)) phi_f(P_2^(a u^i)).

The P1 half of the naive summands is **unnecessary for all three degree ≤2 coefficients mod p**. This is an exact simplification, not just a heuristic optimization.

**Precision warning:** the cancellation is modulo p, not an identity in characteristic zero; binom(p,k+1) is nonzero but p-divisible for k=0,1,2. Therefore it does not establish the exact vanishing of the constant or linear coefficients in the completed Iwasawa algebra, nor ord_T Theta=2. Full arithmetic/lifting or independent theoretical vanishing still needed.

The p² Gross right ideal P_2^b is likewise unchanged when b is replaced by b+p² z because r_2(b+p²z)=r_2(b)*[[1,z],[0,1]], so its class depends only on b mod p². The index pair (a∈mu_(p−1),i∈Z/p) parametrizes all p(p−1)=263429130 unit classes mod p². The true computational task is therefore the **P2 class-function weighted moments** on this finite unit group.

## Immediate source-level sample

An exact Sage sample script is committed at [verification/bsd389_p16231_P2_u_orbit_first_samples.py](../verification/bsd389_p16231_P2_u_orbit_first_samples.py). It reuses the *same* already Sage-certified conductor-one p⁴ split chart, HNF lattice and ideal-class equivalence routine rather than re-running all earlier CM gates per point. Default samples: a=1 and i∈{0,1,2,3,4,8,16}, with exact class right-ideal equality witnesses.

The sample script itself is **NOT YET USER EXECUTED**. Its output is only a short genuine distribution sample along one Teichmüller coset, not the global second moment. In particular nonzero samples alone cannot prove nonzero whole c2. Work toward a class-function algorithm that batches all i and a while preserving exact global-to-local ideal identification and proving a finite certification error bound if sampling is used; sampling without such a bound cannot establish nonvanishing.

**Sources:** Castella–Hsieh original Appendix https://web.math.ucsb.edu/~castella/Kato.pdf and the project's user-run Stage22/30, conductor-one local chart, P1 and P2 Gross ideals.
