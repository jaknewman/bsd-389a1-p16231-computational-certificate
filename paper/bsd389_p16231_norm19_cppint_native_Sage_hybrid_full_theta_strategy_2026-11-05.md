# The exact fast path toward the 87,809,710-point Gross theta moment

**2026-11-05.** Curve E389a1, K=Q(sqrt(-3)), ordinary p=16231, m=p². The user's authentic Sage computations have reached n=p with 7216 certified norm-19 mod19 transition keys. Last USER PASS checkpoint:

- n=16231, class 24, a=121898074, genuine direct P2(a) checked and CM embedding equal
- exact raw cyclic prefix moments [33,348,11277] mod16231
- Sage 33D fixed Brandt module, q reduced CM quadratic embedding, 7216 witnessed local edges
- SHA256 of USER fast state 36c1e557221416bc943fd5ab1637a90c1d2b149fe330f7f8f7c32087d89f6a95
- SHA256 of USER edge table 111ea4dfc9109dc8cabef4d44e6fc74543ce139394e3e070cf8adfc9f5c7c3f1

See [actual user log](../results/bsd389_p16231_norm19_cached_matrix_16231_Teich_bridge_USER_PASS_2026-11-05.md).

## Essential exact arithmetic, and why pure C++ can be trustworthy

Every transition of the **oriented** Gross norm-19 chain from state (j,q) uses an exact integral left ideal

D=R_j.left_ideal([q−9,19]).

Since D contains 19 R_j, it depends only on j and q modulo 19 R_j. The reduction of q has distinct eigenvalues 9 and 4 in M2(F19), giving at most 19×20=380 distinct local conjugates per Brandt order, and 33×380=12540 possible cache keys.

For a new key, **Sage**, not C++, constructs the actual quaternionic ideal conjugate(D)*I_j, proves an exact right equivalence beta*conjugate(D)*I_j=I_k, and checks the entire rational 4x4 coordinate conjugation matrix

z_next=A_(j,key)*z / d_(j,key),

corresponding to q_next=beta*q*beta^(−1). The extra actual Gross factor (5+3q/m)/19 commutes with q and cancels in the conjugation, so the beta-only matrix truly transports the CM embedding.

For repeated keys, C++ needs only four integer dot-products and EXACT division checks. It does **not** implement or guess quaternion equivalences, and stops as soon as an unrecognized key occurs. Sage then proves/registers that single new edge.

The [native C++ core](../verification/bsd389_p16231_norm19_native_matrix_core.cpp) uses arbitrary-precision boost::multiprecision::cpp_int for all CM coordinates and matrix entries, ruling out silent 64-bit overflow. It checks that every matrix numerator is exactly divisible by its positive denominator, and accumulates the 33-class histogram and three coefficients modulo p with fixed 64-bit integers that stay within safe ranges.

The [hybrid Sage/ctypes driver](../verification/bsd389_p16231_norm19_native_exact_stream.py) compiles the core with g++/Boost headers, reuses exactly the authenticated USER n=16231 state and 7216 edge table, invokes Sage only on unseen keys, and periodically reconstructs independent true Gross P2 states. It saves native edge-table and chain-state snapshots under fresh home paths, separately from all prior user certificates.

The actual compiled native core was tested locally by the assistant (g++17) on a synthetic constant-key one-million-step smoke test: all million states completed with integer matrix division. This verifies interoperability and arithmetic mechanics but **is not a Sage/real quaternion benchmark**. Neither the hybrid code nor the new C++ source has yet been run by the user.

## Independent full 16231-point Teich orbit audit during the full ring-class cycle

In the fully cyclic indexing by generator w=138112843, the already completed single Teich principal-unit orbit occurs at precisely the 16231 decimated indices

n=5410*t, t=0,...,16230,

with principal unit exponent i=(10816*n) mod p = (1805*t) mod p.

At every such index, the Brandt class/eigenvalue must equal the historical certified true P2^(1+p)^i class/eigenvalue, because the residual Teich difference lies in the global mu3 order-three group. This is an exact identity of represented CM right-ideal classes, not a probabilistic check.

The hybrid driver optional flag --teich-crosscheck loads the original complete 32 JSON chunks (validated records, correct first SHA256, complete i coverage, exact per-chunk moments), then compares each encountered decimated n step to the independent record. The first real overlap at n=5410 was already independently USER-certified: class14, value1 at i=1805. The native run starts from n=p=16231, so it verifies new decimated indices n>p. A future full 0..H−1 replay could cover all 16231 independently recorded points if desired.

## Correct finite theta moments, not an invented BSD theorem

The exact coefficient-reduction formula is

c_k(Theta_(f/K,1)) ≡ −3·4986 · ∑_(n=0)^(H−1) binom(i_n,k) v_n (modp), k=0,1,2,

where H=87809710 and i_n=(10816*n mod 16231).

The factor 3 restores the global mu3 redundancy; the original P1 contribution cancels modulo p for k=0,1,2 by the finite binomial identity ∑_(i=0)^(p−1) binom(i,k)=binom(p,k+1)≡0 modp, since P1 is invariant when a changes by p.

The hybrid driver outputs **only partial moments** until the true final index n=H−1 has been processed and the histogram contains exactly H entries. It never asserts nonzero c2 from a partial sum. At full coverage it prints the three finite theta coefficients modp and marks that the comparison with the actual infinite Iwasawa power series and the exact order in T, the hypotheses of Castella–Hsieh and p-primary Sha control are separate obligations.

## First safe real Ubuntu hybrid benchmark

\`\`\`bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only origin main
set -o pipefail
timeout 240s python -u \
  verification/bsd389_p16231_norm19_native_exact_stream.py \
  --target-n 50000 --checkpoint-every 8192 --oracle-every 8192 \
  --teich-crosscheck \
  2>&1 | tee ~/bsd389_p16231_norm19_native50k.log
echo "NORM19_NATIVE50K_STATUS=$?"
\`\`\`

If the new C++/Sage hybrid runs successfully it should bootstrap the previously SHA-pinned USER n=p checkpoint, show new witnessed cache edges (unless they are already cached), perform exact independent Gross anchor checks at steps 24576,32768,40960,49152, and compare the decimated true Teich orbit at n=21640,27050,32460,37870,43280,48690. It may resume from the latest exact native checkpoint if timeout interrupts; the target has NOT YET been user-run.

## Next move after benchmark

If the native hybrid cache saturates and maintains correctness under direct Gross independent reconstructions, a run with target_n=H−1 will compute all 87.8 million points with restartable checkpoints. The final sum and lower coefficients must actually be obtained before any c2 nonvanishing, Iwasawa theta order, Sha or BSD statements. The new implementation is a concrete algorithmic approach, not an already certified theorem-level proof.
