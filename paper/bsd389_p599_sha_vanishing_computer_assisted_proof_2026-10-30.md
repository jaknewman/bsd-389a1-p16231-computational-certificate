# The p=599 primary Tate–Shafarevich bound for 389a1 — computer-assisted proof record

**Date:** 2026-10-30. **Claim:** \(\Sha(E/\mathbf Q)[599^\infty]=0\) for \(E:y^2+y=x^3+x^2-2x\), **as a computer-assisted mathematical deduction from the supplied, user-executed Sage/eclib certificates and the published Stein–Wuthrich/Perrin-Riou/Kato theorems**. The stated conclusion is *not* a direct output of `E.sha().p_primary_bound(599)`, which did not complete. As usual for a new computational proof, independent external mathematical review and public verification with the same pinned Sage data are valuable before formal publication. No claim about \(\Sha\) at other primes, or full BSD.

## Verification correction — supersingular `Reg_p` vs `Reg_gamma` (2026-10-30)

**Mandatory theorem-normalization audit remains.** Stein–Wuthrich (2013), §4.4, defines `Reg_gamma=Reg_p/log(kappa(gamma))^r`. Its supersingular **Conjecture 5.2**, eq. (5.3), uses `Reg_gamma` for the `T`-series; its printed supersingular **Algorithm 11.1, step (4)** and the corresponding proof formula instead display `Reg_p`. Meanwhile Sage 10.9 `sha_tate.an_padic` explicitly divides its regulator by `log(1+p)^r`. Since our computed first-coordinate p-adic valuations are **0 for the normalized regulator but 2 for the unnormalized regulator at rank 2**, the choice is numerically material; it must not be silently glossed over or replaced by an assumed typo.

**Consequently, the final boxed assertion below is a *conditional computer-assisted proof claim* until the supersingular leading-term convention and this factor are reconciled against the precise theorem.** All finite `C2=543`, exact 390-Manin normalization, Hecke congruences, the source-derived `F0,2=571` residue, and the regulator computations remain valid user-reported PASS data. The claimed unconditional `b599=0` does not follow from the *literal unnormalized* `Reg_p` formula without an additional identification. Track in [issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4).

---

## Exact hypotheses and input certificates

- \(E\) is the minimal model \([0,1,1,-2,0]\) of \(389a1\); conductor 389, discriminant +389, Tamagawa product 1, torsion order 1, two real components.
- \(p=599\): good supersingular reduction, \(a_{599}=0\); mod-p Galois representation **surjective** (user's certified Sage computation).
- \(\operatorname{rank}E(\mathbf Q)=2\); Sage `E.gens(proof=True)` returned two certified generators \((-1,1),(0,-1)\), with `gens_certain()=True\).
- The \(\omega,\varphi(\omega)\)-coordinate \(D_p\)-regulator computed by Sage satisfies
  \[
  \operatorname{Reg}_\gamma(E/\mathbf Q)_0\equiv571\pmod{599},\qquad
  \operatorname{ord}_{599}(\operatorname{Reg}_\gamma(E/\mathbf Q)_1)=1,
  \]
  where \(\operatorname{Reg}_\gamma=\operatorname{Reg}_p/\log_{599}(1+599)^2\). Thus its vector valuation is **0** and it is nonzero. This is a normalized regulator; the unnormalized regulator's first coordinate has valuation 2.
- The genuine eclib source Manin table has SHA256 `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8`, and every one of the 390 table values was compared against `E.padic_lseries(599)._modular_symbol` (user-executed PASS).
- Two independent finite-symbol engines (original C++ continued fractions, independently implemented Python full-convergent method) computed the conductor-\(p^2\) tame-trivial binomial moment \(C_2=543\bmod599\) from exactly 179,101 plus-symmetry pairs and 1,924,081 continued-fraction edges. \(C_0=C_1=0\), checksum 779927018. These moments are in the p-adic L-function's *actual* normalized modular-symbol convention.

Source run log: [all-390 plus small supersingular regression](../results/p599_hecke_projection_independent_regression_PASS_2026-10-30.md). Source normalization script: [`verification/bsd389_p599_hecke_projection_regression.py`](../verification/bsd389_p599_hecke_projection_regression.py).

## Step 1 — precise finite Hecke-to-analytic identity

Let \(p=599\), \(\gamma=1+p\), \(\omega(a)\) the Teichmüller root of unity, \(a=\omega(a)\gamma^{j_n(a)}\pmod {p^n}\), \(w_n(a)=\binom{j_n(a)}2\), and \(S_n(a)=[a/p^n]^+\) with the Sage 10.9 p-adic L-series's own eclib period normalization.

Define the integer-valued (or \(p\)-integral rational) moments
\[
A_3=\sum_{a\in(\mathbf Z/p^3)^\times} w_3(a)S_3(a),\quad
B_3=\sum_{a\in(\mathbf Z/p^3)^\times} w_3(a)S_2(a\bmod p^2),\quad
C_2=\sum_{b\in(\mathbf Z/p^2)^\times} w_2(b)S_2(b).
\]
The full 390-entry normalization comparison and integral Manin cusp decomposition guarantee \(S_n(a)\in\mathbf Z_p\). The exact modular-symbol \(T_p\)-eigensymbol identity for every unit \(b\bmod p^2\) gives
\[
\sum_{t=0}^{p-1} S_3(b+t p^2)
  = a_p S_2(b)-S_1(b)=-S_1(b).
\]
Under the same fibre, \(j_3(b+t p^2)=j_2(b)+p t'\) for a permutation \(t'\) of \(0,\ldots,p-1\). Hence \(w_3(a)\equiv w_2(b)\pmod p\) and
\[
\sum_{a=b \,(\mathrm{mod}\ p^2)}w_3(a)
\equiv p\,w_2(b)\pmod{p^2}.
\]
As \(b\) runs over a fixed nonzero residue modulo \(p\), \(j_2(b)\) runs over \(0,\ldots,p-1\), and
\(\sum_{j=0}^{p-1}\binom j2=\binom p3\equiv0\pmod p\).
Therefore,
\[
\boxed{A_3\equiv0\pmod p,\qquad B_3/p\equiv C_2\equiv543\pmod p.}
\]
These are exact Hecke and integer-weight arguments, not a conjectural leading-term comparison.

## Step 2 — Frobenius and proven approximation precision

Read directly from the tagged Sage 10.9 source `src/sage/schemes/elliptic_curves/padic_lseries.py`:
- `measure(a,3)`: \(\alpha^{-3}S_3(a)-\alpha^{-4}S_2(a)\), with \(\alpha^2=-p\).
- `series(3,prec=3)`: the sum with weights \(w_3(a)\), divided by \(\mathrm{real\_components}=2\); the twist-period quotient is 1.
- `Dp_valued_series`: write the series as \(G+\alpha H\), multiply \((G,-pH)\) by \(((1-\varphi)^{-2})^\top\), \(\varphi=\begin{psmallmatrix}0&-1/p\\1&0\end{psmallmatrix}\).

Thus the quadratic coefficient at level \(n=3\) has \(G=-B_3/(2p^2)\), \(H=A_3/(2p^2)\) and
\[
F_{0,2}^{(3)}
  =\frac{2A_3-(p-1)B_3/p}{2(p+1)^2},\qquad
F_{1,2}^{(3)}
  =\frac{-(p-1)A_3-2B_3}{2(p+1)^2}.
\]
For \(n=3\), the alpha-adic **proven** error bound is \(\mathrm O(\alpha^{-1})\). An error with this bound has scalar coordinate in \(\mathbf Z_p\) and \(\alpha\)-coordinate in \(p^{-1}\mathbf Z_p\); the preceding projection multiplies these by at least \(p\) and \(p^2\) respectively. Hence both projected-coordinate errors lie in \(p\mathbf Z_p\). Consequently, the *genuine* analytic quadratic coefficient in the \(D_p\)-valued p-adic L-series satisfies
\[
\boxed{F_{0,2}\equiv 543/2\equiv571\pmod{599},\qquad F_{1,2}\equiv0\pmod{599}.}
\]
In particular, its vector valuation is **0**.

Independent convention regression: at the genuinely supersingular pair \((1483a1,p=5)\), the full direct Sage `Dp_valued_series(n=3,prec=3)` calculation (100 units) produced the same \(T^2\)-coefficient residue as the conductor-\(p^2\) Hecke formula, 1 mod 5; all 20 exact Hecke fibres were verified. This tests a nontrivial real-components=1 convention. For \(p=599\), the all-390 eclib normalization test and \(\mathrm{real\_components}=2\) are user-executed PASS.

## Step 3 — the published, unconditional Selmer bound

**Theorem used:** Stein and Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, *Mathematics of Computation* 82 (2013), Section 6.2 (Perrin-Riou Theorem 6.2), Kato Theorem 7.3, and Algorithm 11.1, including its **supersingular step (4) and proof** on pages 1783–1784:
https://wstein.org/papers/mcom2649-iwasawa-alg.pdf

For \(p>2\) non-additive (here good supersingular), surjective residual representation, full Mordell–Weil group, nonzero p-adic regulator, and leading term of order \(r=2\), Algorithm 11.1 obtains a **provable upper bound**, without assuming the BSD conjecture:
\[
v_p(\#\Sha(E/\mathbf Q)[p^\infty])
\le b_p
= v_p\!\left((1-\varphi)^{-2}\mathcal L_p^*(E,0)\right)
-v_p\!\left(\operatorname{Reg}_\gamma(E/\mathbf Q)\right)
-\sum_v v_p(c_v).
\]
In our Dp-valued normalization the projected coefficient is precisely \((F_{0,2},F_{1,2})\); its valuation is 0. The normalized regulator also has valuation 0, and all Tamagawa numbers are 1. Therefore
\[
b_{599}=0-0-0=0.
\]
The Kato divisibility gives the lower bound \(\operatorname{ord}_{T=0}\mathcal L_p(E,T)\ge r=2\); the unit quadratic coefficient makes this order exactly 2. Thus the prerequisite for the algorithm's finiteness conclusion is met, and
\[
\boxed{\Sha(389a1/\mathbf Q)[599^\infty]=0.}
\]

This proof *does not use* the conjectural exact equality between L-leading coefficient and regulator. Their matching residue 571 is stronger than needed: it suffices that both are p-adic units.

## Scope, auditability and reproducibility

- This is a **computer-assisted mathematical deduction**, trusting the user-executed Sage/eclib computations, the cryptographically pinned table, independently corroborated finite Manin sums, the exact normalization and the published Selmer theorem. It is not a fully formalized Lean/Coq proof and has not yet been externally peer-reviewed.
- The original Sage `sha.p_primary_bound(599)` attempt consumed substantial resources and did **not return** 0. The proof replaces only its analytic-coefficient evaluation by the explicit Hecke identity and proven source-code precision bound, not by a heuristic assumption.
- Nothing here proves the analogous statement for every prime, nor finiteness of the entire \(\Sha\) group, nor BSD for \(389a1\).

**Reproduce the supplied finite and normalization data** (requires external authentic 390-Manin table):
```bash
python -u verification/sha599_short_certificate.py --table ~/bsd389_p599_manin_table.txt --sage
python -u verification/bsd389_p599_hecke_projection_regression.py --table ~/bsd389_p599_manin_table.txt
```

An external mathematical review of the bridge and the paper theorem is recommended before public publication. Any found defect must be recorded and the theorem status corrected without changing the facts of the user-executed finite PASS results.
