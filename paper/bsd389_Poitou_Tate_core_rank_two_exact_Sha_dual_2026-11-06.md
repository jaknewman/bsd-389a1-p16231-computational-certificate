# 389a1: a genuine core-rank-two Selmer structure with strict dual exactly Sha[p]

2026-11-06. **A universal algebraic/duality theorem**, for each residual prime satisfying the already proved MW auxiliary-line hypothesis. No prime-specific certificate is rerun. This is a *new structural bridge* toward higher-rank Kolyvagin systems, **not** a proof that such a primitive system has been constructed.

## Definitions

Let \(p\ge 5\) be an odd prime, \(M=E[p]\) with \(E/\mathbb Q=389a1\), and
\[
S=\operatorname{Sel}_p(E/\mathbb Q)=H^1_{\mathcal F}(\mathbb Q,M)
\]
for the **usual self-dual local Kummer conditions** \(\mathcal F\). Since \(M\simeq M^\vee(1)\) via the Weil pairing, \(\mathcal F^*=\mathcal F\).

Assume that there exist two distinct primes \(q_1,q_2\) of good reduction, both different from p, with
\[
L_i=E(\mathbb Q_{q_i})/pE(\mathbb Q_{q_i})\simeq H_f^1(\mathbb Q_{q_i},M)\simeq \mathbb F_p
\]
and the **MW-localization matrix is invertible**:
\[
\lambda_{\rm MW}:E(\mathbb Q)/pE(\mathbb Q)
    \longrightarrow L_1\oplus L_2
\quad \text{is an isomorphism}.
\]
Such pairs already exist by the previously proved Kummer–Chebotarev theorem under the residual-surjectivity hypotheses; concrete pairs for p=5,7,107 are already recorded in the project. **No new prime search is necessary.**

Define three Selmer structures:
- \(\mathcal F\): usual local Kummer conditions at every place.
- \(\mathcal R\): same as \(\mathcal F\) away from \(q_1,q_2\), but impose **no local restriction** at these two places, i.e. \(H^1_{\mathcal R}(\mathbb Q_{q_i},M)=H^1(\mathbb Q_{q_i},M)\).
- \(\mathcal S\): same as \(\mathcal F\) away from these places, but impose local condition \(0\) at \(q_1,q_2\).

By local Tate duality, \(\mathcal R^*=\mathcal S\). The local \(L_i\) is maximally isotropic/self-annihilating.

## Theorem (unconditional given the explicit two-line MW hypothesis)

Under the above conditions:

\[
\boxed{\operatorname{Sel}_{\mathcal R}(\mathbb Q,E[p])
        = \operatorname{Sel}_{\mathcal F}(\mathbb Q,E[p])=S,}
\]
\[
\boxed{\operatorname{Sel}_{\mathcal S}(\mathbb Q,E[p])
       \cong\Sha(E/\mathbb Q)[p],}
\]
and the finite residual Selmer core-rank difference of the modified structure is
\[
\boxed{\chi(\mathcal R)=
 \dim_{\mathbb F_p}\operatorname{Sel}_{\mathcal R}(M)
 -\dim_{\mathbb F_p}\operatorname{Sel}_{\mathcal R^*}(M^\vee(1))
 =2.}
\]
The equalities hold even when \(\Sha(E/\mathbb Q)[p]\ne0\). No finiteness of the *total* \(\Sha\) or BSD hypothesis is used.

### Proof 1: exact Kummer splitting

The Mordell–Weil group is \(\mathbf Z^2\) with no torsion, so Kummer gives
\[
0\to M_{\rm MW}:=E(\mathbb Q)/pE(\mathbb Q)
 \to S\to A:=\Sha(E/\mathbb Q)[p]\to0,
\quad M_{\rm MW}\simeq\mathbb F_p^2.
\]
Localization \(\lambda:S\to U:=L_1\oplus L_2\) is surjective because its restriction to \(M_{\rm MW}\) is the assumed isomorphism. Therefore the projector
\[
\pi=(\lambda|_{M_{\rm MW}})^{-1}\circ\lambda:S\to M_{\rm MW}
\]
splits Kummer exactly:
\[
S\simeq M_{\rm MW}\oplus\ker\lambda,\qquad
\ker\lambda=\operatorname{Sel}_{\mathcal S}(M)\simeq A.
\]
This proves the second box with no assumption \(A=0\).

### Proof 2: Poitou–Tate eliminates extra relaxed classes

At each \(q_i\), local Tate duality supplies a perfect pairing
\[
\big(H^1(\mathbb Q_{q_i},M)/L_i\big)\times L_i\to\mathbb F_p.
\]
Write \(V=\bigoplus_iH^1(\mathbb Q_{q_i},M)/L_i\cong U^\vee\). The Poitou–Tate comparison of \(\mathcal F\le\mathcal R\) gives the exact sequence
\[
0\to S\to\operatorname{Sel}_{\mathcal R}(M)
 \to V \xrightarrow{\lambda^\vee}S^\vee
 \to \operatorname{Sel}_{\mathcal S}(M)^\vee\to0.
\]
The connecting map \(V\to S^\vee\) is **precisely the dual of localization** \(\lambda:S\to U\), via the local Tate pairings. Since \(\lambda\) is surjective, \(\lambda^\vee\) is injective. Hence the first displayed map
\(S\to\operatorname{Sel}_{\mathcal R}(M)\) is surjective as well as injective. This proves the first box.

### Proof 3: exact core rank

Because \(\mathcal R^*=\mathcal S\), the preceding two identities yield
\[
\chi(\mathcal R)
 =\dim S-\dim A
 =(2+\dim A)-\dim A=2.
\]
This **constructs an honest core-rank-two local Selmer structure for the actual residual representation**, even though the self-dual usual Selmer structure has core rank \(0\) and the Mazur–Rubin canonical (relaxed-at-\(p\)) structure has core rank \(1\). Thus rank-two MW alone was not the explanation; the **two controlled local modifications** and exact Poitou–Tate comparison are.

## Sharp implication for higher-rank Kolyvagin systems

There is now a well-specified target for applying theorems of Mazur–Rubin and Burns–Sakamoto–Sano:

1. Use the **explicit \(\mathcal R\)** as the desired core-rank-two Selmer structure; the corresponding **dual** \(\mathcal R^*=\mathcal S\) is exactly \(A=\Sha[p]\), rather than an unspecified modified Selmer group.
2. **Check all additional hypotheses** required by the chosen higher Kolyvagin/Stark-system theorem (cartesian local conditions, Gorenstein coefficient ring, ramification/residual irreducibility, core vertices, etc.) for this \(\mathcal R\). The existence of two local MW lines alone does not verify all of these.
3. Construct an **actual norm-compatible rank-two Euler/Kolyvagin system** for \((M,\mathcal R)\) with a mod-p primitive initial wedge. It is not enough to observe that \(\bar P\wedge\bar Q\) is nonzero in the MW lattice. The cohomological system relations must be checked.
4. Under an applicable *leading-term/Fitting* theorem, prove that this primitive system makes the Fitting ideal of the true strict dual **a unit**. Then \(A=0\). Achieving this for all good residual primes outside an explicit finite set, plus certified exceptions, would give global \(\Sha=0\).

The key non-circular advance here is the **proved choice of local structure and exact identification of its dual**; what remains genuinely unproved is the primitive global higher-rank system and a uniform integral/nonvanishing statement.

### Fixed-p versus global support

The \(q_i\) generally **depend on p** (indeed p-admissibility requires \(q_i\equiv1\bmod p\)). Therefore this theorem does **not** furnish one fixed rational comparison integer \(C\) or prove anything about all-p support by itself. One must not replace the missing integral motivic descent by a formal product of the varying \(p\)-local constructions.

## Sources and project dependencies

- Mazur–Rubin, *Kolyvagin Systems*, Poitou–Tate comparison theorem 2.3.4. Also the published explicit formulation in higher-rank Selmer literature: https://msp.org/ant/2018/12-10/ant-v12-n10-s.pdf, Theorem 3.7.
- Mazur–Rubin, *Controlling Selmer groups in the higher core rank case*, https://www.numdam.org/articles/10.5802/jtnb.933/ .
- Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, https://arxiv.org/abs/1805.08448 .
- Already certified exact MW-local determinant pairs and Kummer–Chebotarev theorem, repository files \`results/bsd389_MW_local_determinants_USER_RUN_PASS_2026-11-02.md\` and \`paper/bsd389_uniform_Chebotarev_Kummer_MW_local_two_auxiliary_wedge_2026-11-02.md\`; their calculations are not repeated.
- Existing strict-splitting statement \`paper/bsd389_strict_selmer_chebotarev_detection_and_norm_projection_no_go_2026-11-05.md\`. The new ingredient here is the **Poitou–Tate comparison of the relaxed structure and exact proof of core rank 2**.
