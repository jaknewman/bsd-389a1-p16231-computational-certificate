# E389a1 p=11: full 397×991 Kurihara witness — actual Sage USER PASS

**Date recorded:** 2026-11-14.
**Provenance:** Terminal stdout pasted by the user from their Sage-enabled Ubuntu session, after git fetch and checkout of branch proof/p11-local-and-kurihara-scalar-veto-2026-11-13. NOT a ChatGPT/Sage execution, GitHub CI run, or SHA-pinned bitwise copy of the original local log.

## User's command and full run output

Source: verification/bsd389_p11_kurihara_full_two_prime_sage_gate.py on this branch.

~~~bash
python -u verification/bsd389_p11_kurihara_full_two_prime_sage_gate.py \
  2>&1 | tee ~/bsd389_p11_kurihara_full_gate.log
~~~

~~~text
K11_ADMISSIBILITY_AND_I_N_MOD11_PASS n 393427
K11_DIRECT_ECLIB_MANIN390_SAMPLES_PASS
K11_PROGRESS 1 sum 0 seconds 0.0
K11_PROGRESS 100001 sum 4 seconds 1.02
K11_PROGRESS 200001 sum 10 seconds 2.35
K11_PROGRESS 300001 sum 2 seconds 3.73
K11_HALF_FULL_EXACT_AGREEMENT_PASS 1 6 primitive_roots 5 6
K11_LOWER_MOMENTS_ZERO_PASS [0, 0, 0]
K11_GENUINE_TWO_PRIME_KURIHARA_UNIT_PASS 1
K11_CONSEQUENCE_KIM_1_8_1_10_IF_RESIDUAL_MANIN_TAMAGAWA_GATES
BOUNDARY_ONE_P_ONLY_NOT_GLOBAL_SHA_OR_COMPLEX_BSD
~~~

The user returned to a shell prompt without a Python traceback; the program's final PASS appears after all its internal assertions. The command did not separately print a pipefail-protected exit code.

## Reconciliation and arithmetic

- E: y²+y=x³+x²−2x, conductor 389; p=11.
- q1=397, q2=991, n=393427, phi(n)=(396)(990)=392040; half-sum has 196020 units.
- a397=24, a991=−53; the two primes satisfy q≡1 and a_q≡2 modulo 11.
- I397=(396,−374) Z11=11 Z11, I991=(990,−1045) Z11=11 Z11, and **I_n=I397+I991=11 Z11**, not an ideal product.
- Primitive roots in this run: g397=5, g991=6.
- Full modular-symbol moment vector: (M0,M1,M2,M12)=(0,0,0,1) modulo 11. Independent half-sum=6, with 2×6≡1 modulo11.
- Hence the genuine coefficient computed in this program's plus modular-symbol, period, and primitive-root conventions is

$$
\boxed{\widetilde\delta_{397\cdot991}(389a1)\equiv1\pmod{11}.}
$$

Changing primitive roots can multiply the residue by a unit. Nonvanishing is invariant.

## Published-theorem hypotheses, checked independently of any prior Sha claim

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorems 1.8 and 1.10:
https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

1. The mod11 image is GL2(F11): LMFDB says the ell-adic images of 389a1 are maximal for every ell; no exceptional prime other than the Serre discriminant invariant: https://www.lmfdb.org/EllipticCurve/Q/389a1/ .
2. Manin constant c_E=1: LMFDB original data field manin_constant=1; theoretically the optimal semistable case follows from K. Cesnavicius's Manin constant theorem: https://arxiv.org/abs/1703.02951 .
3. E(Q11)[11]=0: good reduction and exact #E(F11)=16 (a11=−4); the formal-group kernel is torsionfree at odd p≥5.
4. All Tamagawa factors are p-units: only bad prime is 389, type I_1, Tamagawa c389=1 (LMFDB).
5. The source implements genuinely p-integral plus modular symbols; eclib values are compared against 390-Manin evaluations at several independent sample rationals before the full sum.

The degree-two witness is **minimal** under Kim 1.8: Kummer and the certified MW rank 2 imply corankSel11∞≥2; the observed nonzero two-factor coefficient gives ord(delta)≤2. Kim 1.8 gives equality corankSel=ord(delta), hence ord(delta)=2; no coefficient with fewer factors can be nonzero mod11. This verifies the minimality hypothesis of Kim 1.10.

## Consequences via published Kim results

Kim Theorem 1.8 and Kummer give, from the 11-unit two-prime witness:

$$
\operatorname{Sel}(E[11^\infty]/\mathbf Q)\simeq(\mathbf Q_{11}/\mathbf Z_{11})^2,
\qquad
\operatorname{Fitt}_{2,\mathbf Z_{11}}
(\operatorname{Sel}(E[11^\infty]/\mathbf Q)^\vee)=\mathbf Z_{11},
$$

hence

$$
\boxed{\operatorname{Sha}(E/\mathbf Q)[11^\infty]=0.}
$$

This is **a new independent Kurihara–Kim route** to the same p11 Sha conclusion separately proved by the earlier genuine Sage p_primary_bound(11)=0 (see results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md).

Kim Theorem 1.10 also yields: nontriviality of the mod11 Kato Kolyvagin system; the cyclotomic Iwasawa main conjecture in that theorem's precise form; and the semilocal isomorphism

$$
\operatorname{Sel}(E[11]/\mathbf Q)
\simeq E(\mathbf F_{397})/11\oplus E(\mathbf F_{991})/11.
$$

The separate user/assistant-verified local Mordell–Weil matrix [[1,10],[1,7]] with determinant 8 modulo11 agrees with this isomorphism.

**Limit:** This certifies a *single prime p=11*, not all sufficiently large primes. It does not prove global Sha finiteness or exact complex BSD.

## Audit metadata

Source code is committed and visible in this branch. User-provided stdout has been transcribed as above, but its original ~/bsd389_p11_kurihara_full_gate.log is not currently a SHA256-authenticated uploaded artifact. That distinction is retained. If requested, the user can hash that original local log for archival provenance.

**Verdict:** Full user-executed p11 unit coefficient 1 modulo11 and theorem-level new Iwasawa/Sha implications. Global BSD remains unproved.
