# Actual user Sage run: integral Hecke Smith determinant 2 for T2,T3,T5 (2026-11-02)

**Provenance:** exact terminal stdout supplied by the user from their Sage-enabled Ubuntu host. This is a true user-executed computation, not a GitHub CI claim. Source was successfully fast-forwarded to repository commit `f849511` immediately before the command.

Executed:
```bash
python -u verification/bsd389_hecke_smith_all_prime_exception_refinement.py \
  --max-operators 3 \
  --output ~/bsd389_hecke_smith_refinement.json \
  2>&1 | tee ~/bsd389_hecke_smith_refinement.log
```

Exact user stdout:

```text
HECKE_SMITH_BASELINE_CANONICAL_SHA256_PASS afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64
HECKE_SMITH_BASELINE_T2_MINOR_29000_RECONSTRUCTED_PASS det 29000 rank_Q 32
HECKE_SMITH_BASELINE_MOD5_7_107_RANKS_PASS rank_p5 29 rank_p7 32 rank_p107 32
HECKE_SMITH_STACK_CERTIFICATE ell 2 ap -2 operators 1 rows 33 exact_gcd_maximal_minors 14500 factorization 2^2 * 5^3 * 29 rank_p2 31 rank_p5 29 rank_p29 31
HECKE_SMITH_STACK_CERTIFICATE ell 3 ap -2 operators 2 rows 66 exact_gcd_maximal_minors 2 factorization 2 rank_p2 31 rank_p5 32 rank_p29 32
HECKE_SMITH_STACK_CERTIFICATE ell 5 ap -3 operators 3 rows 99 exact_gcd_maximal_minors 2 factorization 2 rank_p2 31 rank_p5 32 rank_p29 32
HECKE_SMITH_FINAL_INTEGER 2
HECKE_SMITH_FINAL_EXACT_EXCEPTIONAL_PRIMES [2]
HECKE_SMITH_CANONICAL_JSON_SHA256 86e79229d1c60d38ec59ecd8776c0c471716a1ffdf1098d46d58a8a59253f02a
HECKE_SMITH_REPORT /home/bsdadmin/bsd389_hecke_smith_refinement.json
BOUNDARY_CONGRUENCE_EIGENLINE_ONLY_NOT_SHA_OR_BSD
```

## Exactly certified by this run

On the genuine Sage-defined **integral** weight-2, sign-plus, level-389 modular-symbol lattice of rank 33, let
[
A_{ell}=T_ell-a_ell(389a1)I,quad
A_{2,3}=egin{pmatrix}A_2\\A_3end{pmatrix}.
]

The (66\times33) stack (A_{2,3}) has rational rank **32**, and its 32 nonzero Smith invariants multiply to **exactly (2)**. Thus (since each invariant is a positive integer) **31 are 1 and one is 2**. In particular:
[
\boxed{\operatorname{coker}(A_{2,3}^{t}:\mathbf Z^{66}\to\mathbf Z^{33})
\simeq\mathbf Z\oplus\mathbf Z/2\mathbf Z.}
]
The primitive integral rational common eigenvector was verified against each operator. For **every odd rational prime** p, the integer Smith reduction gives
[
\boxed{\dim_{\mathbf F_p}\ker(A_{2,3}\bmod p)=1,}
]
whereas at p=2 the dimension is **2**. These are exact all-prime conclusions for the **same integral lattice**, not extrapolations from p5/7/107 samples.

The same Smith product remains 2 after adding (A_5). Thus **T5 does not remove the last 2-congruence exception**. At p5, T2 alone had kernel dimension 4, but T2 and T3 reduce it to **1**; this independently establishes that modular-symbol Hecke eigenspace uniqueness for p5 coexists with an already-proved p5 Sha result, while neither is the cause of the other.

**No Sha result:** (D=2) is a fixed Hecke-matrix determinantal divisor. It does not belong to the rank-two Selmer/Fitting ideal automatically and does not give a p-independent two-auxiliary-prime Kurihara witness. It therefore does not prove finite Sha or strong BSD. The mod2 difference between plus-eigenspaces and full characteristic-2 Manin symbols and possible integral base-change issues remain outside this statement.

## Next targeted check

One [new small script](../verification/bsd389_hecke_mod2_exception_targeted_scan.py), not yet user executed, authenticates the actual existing SHA-pinned JSON and directly checks **only mod2 ranks** for additional integral Hecke operators up to primes ≤61. It avoids all further Smith computations. If some operator raises rank to 32, then the last `2` obstruction is eliminated for the enlarged fixed stack; otherwise the extra mod2 class persists for those tested operators. Nothing is preclaimed.

Source proof: [complete all-odd-prime Smith theorem](../paper/bsd389_integral_hecke_smith_2_global_odd_prime_rigidity_2026-11-02.md). Open Sha issue: [#8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
