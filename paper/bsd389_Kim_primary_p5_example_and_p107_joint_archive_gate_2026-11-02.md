# Direct primary-source validation of Kim's 389a1 p5 Selmer result, and a fast p107 two-source cross-certificate

**2026-11-02.** The user's new independent local MW determinant calculation has now **genuinely run and passed on Ubuntu**, with SHA256 of canonical JSON
`3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e`.
The actual user log is [here](../results/bsd389_MW_local_determinants_USER_RUN_PASS_2026-11-02.md).

This note performs two concrete tasks: (a) independently verifies the theorem and the **specific 389a1 p5 case** from the primary source, rather than relying on an imprecise analogy; and (b) publishes a new short p107 joint provenance gate that can cross-check the freshly authenticated MW local determinant **38** against the *previously frozen* global Kurihara archive reporting δ=34. Neither component supplies a uniform all-p Sha bound.

## 1. Kim's own 389a1 example already establishes p5

**Primary source:** Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, author PDF dated 2025-05-12, [printed page 35, §8 Example (1)](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=35). It explicitly identifies exactly
\[
E_{389.a1}: y^2+y=x^3+x^2-2x,\qquad n=41\cdot61,\quad p=5,
\]
and states that the mod5 Kurihara number is nonzero, then obtains the precise conclusions
\[
\boxed{\Sha(E_{389.a1}/\mathbf Q)[5^\infty]=0},
\]
and the canonical semi-local isomorphism
\[
\boxed{
\operatorname{Sel}(\mathbf Q,E_{389.a1}[5])
\xrightarrow{\ \sim\ }
E_{389.a1}(\mathbf Q_{41})/5\oplus
E_{389.a1}(\mathbf Q_{61})/5.
}
\]

**Exactly what our new computation adds:** independently, via the actual finite-field group law on the rational generators \(P=(-1,1),Q=(0,-1)\), it computes local rows \((1,3)\) at q41 and \((1,0)\) at q61, with determinant \(2\ne0\bmod5\). This concretely shows **P,Q map to a basis of Kim's published two local Selmer lines**, using no modular-symbol input in the new computation. It is confirmation and a more explicit *basis calculation*, **not** a claim that the published p5 Sha result is our new theorem.

## 2. Kim's exact mod-p theorem and correct logical order

**Primary source**, printed page 8, [Theorem 1.10](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8): for p≥5 require
(i) \(\bar\rho_{E,p}\) surjective;
(ii) optimal Manin constant prime to p;
(iii) \(E(\mathbf Q_p)[p]=0\);
(iv) all Tamagawa factors prime to p.

Then one needs a nonzero **mod-p** Kurihara coefficient \(\widetilde\delta^{(1)}_n\ne0\) with \(\nu(n)=\operatorname{ord}(\widetilde\delta^{(1)})\). Under these hypotheses the canonical modp Selmer localization is an **isomorphism**:
\[
\operatorname{Sel}(\mathbf Q,E[p])\simeq
\bigoplus_{\ell\mid n} E(\mathbf Q_\ell)/p
\simeq\bigoplus_{\ell\mid n}E(\mathbf F_\ell)/p.
\]

For E389a1 with **certified saturated MW rank2** and a genuine degree-two \(\delta_n\ne0\), the rank lower bound in Kim [Corollary 1.13] gives \(\operatorname{ord}\widetilde\delta^{(1)}\ge2\). The witnessed n with two primes gives \(\operatorname{ord}\le2\). Thus equality holds and Thm1.10 applies.

Our local p107 data:
\[
\begin{gathered}
(q_1,q_2)=(369793,383917),\quad
(a_{q_1},a_{q_2})=(2,-854),\\
\#E(\mathbf F_{q_1})=369792,\quad
\#E(\mathbf F_{q_2})=384772,\\
R_{107}=\begin{pmatrix}1&15\\1&53\end{pmatrix},
\quad\boxed{\det R_{107}=38\ne0\bmod107},\\
\#E(\mathbf F_{107})=108,\ \ 107\nmid108.
\end{gathered}
\]
The local p-adic E(Q107)[107]=0 gate follows for the good-reduction curve over unramified \(\mathbf Q_{107}\) from reduction and the absence of \(\mathbf Q_{107}\)-rational odd p torsion in the formal group. The other Galois, Manin, Tamagawa and MW saturation prerequisites are independent inputs previously recorded in the project; they are **not proved by the new local JSON**.

If a **mathematically valid**, Manin-normalized archived global two-prime p107 Kurihara computation indeed gives \(\delta_{q_1q_2}=34\in\mathbf F_{107}^\times\), Kim gives Sel(E[107]) a 2-dimensional space equal to the two local lines. The local basis matrix identifies P,Q as a basis of it; the Kummer sequence gives
\[
\operatorname{Sel}(\mathbf Q,E[107])/(E(\mathbf Q)/107)\simeq
\Sha(E/\mathbf Q)[107]=0.
\]
Then \(\Sha[107^\infty]=0\). **This is a conditional single-prime consequence of an already old global Kurihara certificate, NOT a theorem for all p.**

**Logical economy:** once rankMW2 and Kim's two-dimensional Selmer space are known, MW/p→Sel is an injection between two-dimensional Fp spaces and therefore automatically an isomorphism. Thus the new nonzero **local determinant is an additional independent mathematical cross-check, NOT a missing necessary step in that dimension argument.**

## 3. Fast dual-provenance certificate — no massive rerun

The new [`verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py`](../verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py), published **but not yet run on the user's Ubuntu server**, reads:

- The user's NEW canonical local MW JSON `~/bsd389_MW_local_determinants_5_7_107.json` pinned SHA256 `3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e`; validates the exact q, a_q, finite group orders, p-unit det38, and local p-torsion zero.
- The previously completed p107 full Kurihara archive `~/bsd389_k107_certificate_COMPLETE_20261028.tar.gz`, pinned SHA256 `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754`. The prior historical calculation reports δ=34, but **its sum is not recomputed by the short program**. SHA agreement verifies the saved bytes, **not correctness of the long Kurihara algorithm**.

It emits a new **SHA-pinned canonical JSON with explicit external mathematical assumptions**, no arbitrary p extrapolation, and does not silently mark any unexecuted verification as completed.

Suggested command:

```bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only origin main
set -o pipefail
python -u verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py \
  --output ~/bsd389_p107_joint_Kim_bridge.json \
  2>&1 | tee ~/bsd389_p107_joint_Kim_bridge.log
```

The frozen p107 archive filename is the last previously recorded artifact; if it has been moved, use `--k107-archive /exact/path/to/archive.tar.gz` rather than claiming it was checked.

## 4. What is still open for uniform BSD

Kim's p5 example and the p5/p7/p107 *finite* local determinant PASSes do not imply a \(\Sha\) bound at arbitrary p. The independently proved uniform Kummer–Chebotarev theorem supplies **infinitely many p-admissible pairs with nonzero MW local determinant**, but does **not** guarantee a globally nonzero two-prime Kurihara δ on any chosen pair.

**Exact missing bridge:** an all-large-p theorem forcing one nonzero **global** two-prime Kato-derived \(\widetilde\delta\), or an independently proved integral Selmer Fitting comparison that bounds global \(\Sha\)-support. In addition, exact complex rank-two BSD leading-term equality remains unresolved.

[Open rank-two Sha-support issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
