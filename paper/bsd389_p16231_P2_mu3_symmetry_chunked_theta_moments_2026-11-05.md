# The first honest Gross theta moment: exact mu3 symmetry and checkpointed full i orbit

Date: 2026-11-05. E389a1, K=Q(sqrt(-3)), p=16231, trivial-character Castella–Hsieh theta. The global optimal conductor-one CM base (Brandt class32), p4 local Peirce chart and genuine P1/P2 right-ideal constructors are already certified on the user's Sage Ubuntu host.

## Seven verified genuine points

A real Sage user run of verification/bsd389_p16231_P2_u_orbit_first_samples.py yielded the class/eigenvector pairs

i = 0,1,2,3,4,8,16
class = 9,15,21,9,11,17,23
v[class] = −1,−1,+1,−1,−1,0,0.

The seven points were independently reconstructed via integral congruence kernels of index p8, inverse-image HNF checks, right ideal closure, and actual quaternionic ideal-equivalence witnesses. See [verbatim user-run abbreviated record](../results/bsd389_p16231_P2_u_orbit_7samples_USER_PASS_2026-11-05.md).

## NEW: factor-three symmetry by actual maximal-order global units

Let omega∈R_32 be the proven global integral unit of order 3, satisfying omega²+omega+1=0, with p-adic matrix rho(omega)=diag(r0,r1). Define the unit lambda=r0/r1 ∈ (Z/p²)×; with the user's Hensel roots the exact value is

lambda = 213756225 (mod 263445361), lambda²=49689135, lambda³=1.

It is not 1. Let t_n(a)=[[p^n,a],[0,p^n]]. In the local M2 chart,

rho(omega) t_n(a) rho(omega)^(−1) = t_n(lambda a).

Outside p, omega lies in R_ell× because it is a global unit of the base maximal order. Hence the *adelic* right ideal t_n(lambda a) Rhat differs from t_n(a) Rhat by left multiplication by a global quaternion omega and right multiplication by an adelic integral unit. In the standard Brandt double-quotient, their class and phi_f values coincide, for every n and a:

**phi_f(P_n^(lambda a)) = phi_f(P_n^a) = phi_f(P_n^(lambda² a)).**

This is an exact consequence of the valid **conductor-one** CM embedding and the split chart; the old conductor53 quaternion does NOT provide this global order-3 unit.

For n=2, multiplying any Teichmuller unit a by lambda stays within the Teichmuller subgroup mu_(p−1), while retaining its anticyclotomic 1+p coordinate i. Thus the complete a-sum has 3-fold redundancy. Instead of p−1=16230 distinct Teichmuller residues for each i, only (p−1)/3=5410 residue-orbits are necessary:

∑_(a∈mu_(p−1)) ∑_i binom(i,2)phi_f(P_2^(a u^i))
=3∑_(a mod mu3) ∑_i binom(i,2)phi_f(P_2^(a u^i)).

These 5410*16231=87,809,710 distinct unit orbits agree with h(O_(p²)). The theta coefficient still requires the entire orbit sum, not one sample. The coefficient of degree 2 modulo p is then

c2 ≡ −3*(4986) ∑_(a mod mu3) ∑_i binom(i,2) phi_f(P_2^(a(1+p)^i)) (mod p).

This symmetry divides computational work by 3 but does **not** change the status of ord_T Theta.

## NEW: complete single-Teich i-orbit in small restartable exact chunks

The new [verification/bsd389_p16231_P2_u_orbit_chunked_moments.py](../verification/bsd389_p16231_P2_u_orbit_chunked_moments.py) loads the already-proved p4 Peirce chart (pinned to SHA256 63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35), reconstructs **each** P2 Gross-point HNF lattice and 16 closure identities, and verifies the exact right-equivalence witness to one of the 33 Brandt representatives.

Every chunk contains source hash, each actual parameter a, all class/eigenvector values and quaternionic witnesses, and exactly computed moments for k=0,1,2 mod p. It is written atomically and has independent aggregate-side checks for overlaps, complete coverage, class/value consistency, local parameter progression and each per-chunk moment. A complete 16231-index orbit produces a compact full-orbit moment summary M0,M1,M2 mod p. No extrapolation from the seven samples is permitted.

The flag --mu3-check independently classifies the 9 Gross points at i=0,1,2 for a,lambda a,lambda² a to test the predicted exact unit symmetry. The result is **not yet user-executed**, so report any actual failure instead of asserting a PASS.

Commands, all within the user's checked-out repo and activated Sage:

\`\`\`bash
git pull --ff-only origin main
set -o pipefail
timeout 240s python -u verification/bsd389_p16231_P2_u_orbit_chunked_moments.py --residue 1 --start 0 --count 512 --mu3-check \
  2>&1 | tee ~/bsd389_p16231_P2_chunk0.log
echo "P2_CHUNK_STATUS=$?"
\`\`\`

The remaining 15719 indices are then processed in non-overlapping subsequent chunks, and aggregation is run only on actual completed files. A missing portion causes an explicit exit status 2, not a fabricated complete certificate.

## True remaining obstacle

Even if the **entire** first Teich coset i=0..16230 is computed, the global quadratic theta coefficient is the sum across **5410** Teich cosets modulo mu3. Only after all genuine Gross class values, their exact weighted sums and an appropriate vanishing theorem for lower degrees can one conclude ord_T Theta=2 and apply Castella–Hsieh. The enormous remaining computation motivates developing a recurrence or a faster exact class-count algorithm; no efficient full-layer algorithm is claimed yet. The prior p-primary Sha and all-prime BSD gaps remain.
