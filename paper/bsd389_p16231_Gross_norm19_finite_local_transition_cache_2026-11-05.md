# A finite exact transition cache for all 87,809,710 oriented Gross norm-19 states

**Date:** 2026-11-05. Curve E389a1, p=16231, K=Q(sqrt(-3)), m=p², genuine conductor-one Gross CM base R32. Previously USER-executed real CM-normalized 19-neighbor chain has now reached n=5410, bridged to independently calculated first Teich principal-unit orbit i=1805, class14 eigenvalue1, with 11 direct exact embedding anchors. Verified prefix moments [50,3175,7] mod p; 102.582 seconds elapsed. The authentic user PASS is archived at [results/bsd389_p16231_norm19_stream5410_teich1805_bridge_USER_PASS_2026-11-05.md](../results/bsd389_p16231_norm19_stream5410_teich1805_bridge_USER_PASS_2026-11-05.md).

## Main new algebraic reduction

Let I_j be fixed one of the 33 Brandt right ideals, R_j its left maximal order, and q∈R_j the transported CM element of trace −m and norm m². The oriented norm-19 left ideal is

D_j(q)=R_j.left_ideal([q−9,19]).

If q'≡q mod19 R_j then D_j(q')=D_j(q) **as exact integral quaternion ideals**, because both contain 19 R_j and their other generators differ by a 19-multiple. Thus the 19-neighbor depends only on the finite key

key=(j, q coordinates in the fixed basis of R_j mod19).

Over F19, the quaternion maximal order splits as M2(F19). The characteristic polynomial x²+m x+m² has two distinct roots 9,4 mod19, so the reduction of every q is conjugate to diag(9,4). The number of such matrices is

|GL2(F19)| / |F19× × F19×| = 19*(19+1) = **380**.

With 33 base orders, there are at most **12,540 keys** for the entire enormous ring-class cycle.

## Precompute and reuse an exact matrix

For a new finite key, construct D=D_j(q) ONCE, compute the right ideal

N=conjugate(D)*I_j,

and find its Brandt class k and an **exact quaternion witness** beta with beta*N=I_k. This result depends only on the finite key.

On the other hand the actual Gross norm19 neighbor is

T_next = (g(q)/19) * N, g(q)=5+(3/m)q.

Since g(q) is a polynomial in q, q COMMUTES with g(q). Thus the normalized CM embedding after mapping T_next to I_k by alpha=beta*(19/g(q)) satisfies

q_next = alpha*q*alpha^(-1) = **beta*q*beta^(-1)**.

This cancels the q-dependent global prefactor and leaves a conjugation by a beta that is CONSTANT on the finite key.

Conjugation by beta is a fixed Q-linear transformation on the four rational quaternion coordinates. Express it in bases of R_j and R_k to obtain

z_next = C_(j,key)*z, C in M4(Q).

Store a single common denominator d>0 and numerator integer matrix A∈M4(Z), so that

z_next = (A*z)/d.

All four numerator entries must be exactly divisible by d for each admitted q of the key, and the resulting vector must represent an integral CM embedding in R_k. A cache HIT now requires only four integer dot products, no Sage ideal construction, no expensive is_right_equivalent search and no rational quaternion inverse.

The data of a cache edge must include the **original rational quaternion witness beta** and the exact 4x4 matrix, independently cross-checkable against the ideal identity beta*N=I_k and the conjugation action. The new pilot validates each new edge and lazily revalidates restored persisted edges.

## Correct orientation and residual unit ambiguity

Different equivalence witnesses can differ by a unit in R_k. All R_k have only ±1 units except the unique weight3 maximal order R32, which has six units ±1, ±omega, ±omega². Therefore two valid normalized CM states may have q representations differing by conjugation by an integral R_k unit at k=32, even though the corresponding class and genuine Gross point agree. The fast-vs-slow audit checks equal Brandt class and exactly equal CM embedding (k !=32) or exact conjugation by one of the three cubic unit powers (k=32).

This is not a 33-state transition: the finite local mod19 key is essential. The whole full ring-class orbit still has 87,809,710 points and must be accumulated; the claim is reduced **per-step complexity after finitely many certified edge types**, not an already-established theta value.

## Exact benchmark pilot, not yet user-run

[verification/bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py](../verification/bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py)

Starts from the user's *already certified* n=5410 slow checkpoint, without overwriting it. Generates edge certificates dynamically, applies the integer matrix to every state, validates the transition against the independent unoptimized Sage quaternionic step every 128 steps, and independently reconstructs a true Gross point every 512 steps. The target n=7168 will measure the empirical cache hit count, new edge count, runtime and coefficient bound. It saves the cached edges and fast state to **new separate files** using atomic writes so the original slow run remains intact. No claim that it is faster until user timing proves it.

Proposed command:

\`\`\`bash
git pull --ff-only origin main
set -o pipefail
timeout 240s python -u verification/bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py \
 --target-n 7168 --audit-every 128 --oracle-every 512 --checkpoint-every 256 \
 2>&1 | tee ~/bsd389_p16231_cached_norm19_pilot.log
echo "NORM19_CACHED_PILOT_STATUS=$?"
\`\`\`

## One mathematical shortcut DISPROVED by already certified moments

The first *complete* principal-unit i-orbit a=1 has exact moments

M0(1)=0, M1(1)=10775, M2(1)=5515 mod16231.

If the Brandt values had naive inversion symmetry f_i=f_(c−i) for any fixed c modp, then changing variable gives

M1 = c*M0 − M1, hence 2*M1=c*M0=0 modp,

contradicting M1=10775!=0. Therefore **there is NO simple shifted inversion symmetry** of the first true Gross principal-unit orbit that would halve enumeration. There is no need to spend computational effort testing a full i↔−i equality: the previously certified moments already refute it.

## Boundary and next priority

The measured slow streaming rate of ~102.6 seconds for 5282 new steps suggests the naive approach would be impractical over all 87.8 million points. The finite cached local matrices are a mathematically exact way to remove repeated class searches and quaternionic ideal construction. However pilot PASS does not establish any full-layer throughput. Wait for the true Ubuntu benchmark to decide whether to implement a compiled 4x4 integer step backend.

Neither the full theta quadratic coefficient nor ord_T Theta=2 nor finite Sha[p∞]/BSD is certified by this finite-state transition reduction alone.
