# Essential correction: residual core rank 2 at fixed auxiliary primes does NOT lift to an integral rank-two system

Date 2026-11-06. This is a **universal theorem for every residual prime satisfying the previously proved auxiliary-line hypotheses**, not an additional finite prime check. It corrects the interpretation of \`paper/bsd389_Poitou_Tate_core_rank_two_exact_Sha_dual_2026-11-06.md\`, while retaining that document's valid **n=1** assertions.

## Setup

Let \(E/\mathbf Q=389a1\), \(E(\mathbf Q)=\mathbf Z^2\), and fix \(p\ge5\). Let \(q_1,q_2\ne p,389\) be two good auxiliary primes for which
\[
E(\mathbf F_{q_i})[p]\simeq \mathbf F_p,\qquad
\lambda_1:E(\mathbf Q)/pE(\mathbf Q)\xrightarrow{\sim}
  \bigoplus_{i=1}^2 E(\mathbf Q_{q_i})/pE(\mathbf Q_{q_i}).
\]
The latter isomorphism is the certified two-MW-point local determinant condition. Since the local \(p\)-rank is one, the \(p\)-Sylow of \(E(\mathbf F_{q_i})\) is cyclic of order \(p^{e_i}\), where
\[
e_i=v_p(\#E(\mathbf F_{q_i}))\in\mathbf Z_{\ge1}.
\]
**Each \(e_i\) is finite**, because \(\#E(\mathbf F_{q_i})\) is a fixed positive integer.

For \(n\ge1\), let \(M_n=E[p^n]\), \(S_n=\mathrm{Sel}_{p^n}(E/\mathbf Q)\), \(U_{i,n}=E(\mathbf Q_{q_i})/p^nE(\mathbf Q_{q_i})\). Define \(\mathcal R_n\) by relaxing the Kummer condition to all local \(H^1(\mathbf Q_{q_i},M_n)\) at both \(q_i\), and \(\mathcal S_n\) by imposing zero local conditions at both places.

## Theorem 1 — exact finite-level saturation and correction term

For every \(n\ge1\) there are exact statements
\[
\boxed{\mathrm{Sel}_{\mathcal R_n}(\mathbf Q,M_n)=S_n,}
\]
\[
\boxed{0\longrightarrow
 \ker\!\left((\mathbf Z/p^n)^2\xrightarrow{\lambda_n}
 U_{1,n}\oplus U_{2,n}\right)
\longrightarrow\mathrm{Sel}_{\mathcal S_n}(\mathbf Q,M_n)
\longrightarrow\Sha(E/\mathbf Q)[p^n]\longrightarrow0,}
\]
and
\[
\boxed{\#\ker\lambda_n=
p^{\,2n-\min(n,e_1)-\min(n,e_2)}.}
\]
Consequently,
\[
\boxed{
\frac{\#\mathrm{Sel}_{\mathcal R_n}}
 {\#\mathrm{Sel}_{\mathcal S_n}}
 =p^{\min(n,e_1)+\min(n,e_2)}.
}
\]

**Proof.**
Since \(E/\mathbf Q_{q_i}\) has good reduction and \(q_i\ne p\), the kernel of reduction is pro-\(q_i\). Hence
\[
U_{i,n}\simeq E(\mathbf F_{q_i})/p^nE(\mathbf F_{q_i})
          \simeq\mathbf Z/p^{\min(n,e_i)}.
\]
The assumed determinant condition \(\lambda_1\) is an isomorphism mod \(p\). Nakayama's lemma applied to the finite \(p\)-groups \(U_{1,n}\oplus U_{2,n}\) shows that
\(\lambda_n:E(\mathbf Q)/p^nE(\mathbf Q)\to U_{1,n}\oplus U_{2,n}\)
is surjective **for all \(n\)**. Thus \(\#\ker\lambda_n=p^{2n}/\#U_{1,n}\#U_{2,n}\) as asserted.

Kummer gives
\(0\to(\mathbf Z/p^n)^2\to S_n\to\Sha[p^n]\to0\).
As \(\lambda_n\) is onto the local Kummer target, every Sha class has a Selmer lift whose localization can be corrected by an MW class. Taking kernels yields the second exact sequence.

The finite-level Poitou–Tate comparison for \(\mathcal F_n\subset\mathcal R_n\), using \(\mathcal R_n^*=\mathcal S_n\), identifies the map
\(\oplus_i H^1(\mathbf Q_{q_i},M_n)/H^1_f
\to S_n^\vee\)
as the transpose of the full localization \(S_n\to\oplus_i U_{i,n}\), under local duality. This localization is surjective because its MW restriction is. Its transpose is injective; hence no new relaxed global Selmer classes occur:
\(\mathrm{Sel}_{\mathcal R_n}=S_n\).
Taking orders from the two exact Kummer descriptions gives the quotient formula. QED.

### Sharp consequence

At \(n=1\), \(\min(1,e_1)+\min(1,e_2)=2\), and \(\ker\lambda_1=0\). Thus the earlier theorem
\(\mathrm{Sel}_{\mathcal S_1}\cong\Sha[p]\) and the **residual** core-rank difference 2 are **correct**.

For any \(n>\max(e_1,e_2)\), however,
\[
\#\ker\lambda_n=p^{2n-e_1-e_2},\qquad
\log_p\frac{\#\mathrm{Sel}_{\mathcal R_n}}
{\#\mathrm{Sel}_{\mathcal S_n}}=e_1+e_2
\quad \text{(constant in \(n\)).}
\]
A genuine free core-rank-two \(p\)-adic Selmer structure would have a
length difference growing with slope **two** in \(n\); the current finite-level modifications have asymptotic slope **zero**. Therefore the previous residual construction cannot simply be lifted to the integral rank-two Kolyvagin/Stark framework, and the old note's invitation to do so was unjustified.

## Theorem 2 — independent local rational-cohomology obstruction

At every fixed prime \(q\ne p,389\) of good reduction,
\[
\boxed{H^1(\mathbf Q_q,V_pE)=0,\qquad V_pE=T_pE\otimes\mathbf Q_p.}
\]
Indeed, \(V_pE\) is unramified at \(q\). Let \(F_q\) denote Frobenius with eigenvalues satisfying \(X^2-a_qX+q=0\). Since
\[
\det(1-F_q)=q+1-a_q=\#E(\mathbf F_q)\ne0,
\]
and
\[
\det(q-F_q)=q(q+1-a_q)\ne0,
\]
there is neither a \(1\)-eigenvector nor a \(q\)-eigenvector. The local inflation–restriction/tame-inertia sequence computes \(H^1\) from the corresponding \(1\) and \(q\) eigenspaces; both vanish. Thus changing local conditions at finitely many fixed good \(q\ne p\) changes only finite \(p\)-power torsion, never the \(\mathbf Q_p\)-dimension.

This independently proves the impossibility of obtaining a **stable \(\mathbf Z_p\)-core-rank increase 2** from these two *fixed* good auxiliary places.

## A genuine integral rank-two setting: quadratic base change

Let \(K=\mathbf Q(\sqrt{-3})\). The project's archived exact-rational positive L-value for the twist \(E^{(-3)}\) and standard analytic-rank-zero theorem give \(\mathrm{rank}\,E^{(-3)}(\mathbf Q)=0\) and finite \(\Sha(E^{(-3)}/\mathbf Q)\). Hence
\[
\mathrm{rank}\,E(K)=\mathrm{rank}\,E(\mathbf Q)
+\mathrm{rank}\,E^{(-3)}(\mathbf Q)=2.
\]
For odd \(p\), restriction and corestriction yield an actual quadratic \(\pm\) decomposition
\[
\boxed{\Sha(E/K)[p^\infty]
  \simeq\Sha(E/\mathbf Q)[p^\infty]
   \oplus\Sha(E^{(-3)}/\mathbf Q)[p^\infty].}
\]
The second factor has a **proven, uniform, finite** arithmetic bound, albeit not explicitly factored; the first factor is the genuine all-prime BSD obstruction.

The canonical \(p\)-adic Selmer structure over the quadratic number field K has **integral core rank 2** in the standard Mazur–Rubin formalism (one per degree \([K:\mathbf Q]\)). Unlike the residual two-\(q\) construction, this is a stable rank statement for the actual \(T_pE\).

**Important further obstruction:** the two rational MW generators of E are \(+1\)-eigenvectors under \(\operatorname{Gal}(K/\mathbf Q)\). At split \(p\), the pair of local \(p\)-adic elliptic logarithms at the two conjugate \(p\)-adic places are **identical on rational points** (under conjugate local identifications). Thus the map
\[
E(K)\otimes\mathbf Q_p\longrightarrow
\bigoplus_{v\mid p} H_f^1(K_v,V_pE)
\]
has image of dimension **at most one**, not two. At inert \(p\) the same restriction is confined to the \(+1\)-eigenline of \(K_p/\mathbf Q_p\). So even the honest integral core-rank-two setting does **not** turn \(P\wedge Q\) into a primitive higher-rank Euler/Kolyvagin system merely by taking two local logarithms.

## What remains genuinely constructive

To exploit the quadratic canonical structure, produce an *actual* norm-compatible rank-two zeta/Euler system over K with verified **nonzero initial class in the appropriate exterior bidual** and prove its **integral comparison to the \(+\)-eigenspace Selmer Fitting ideal**. Check the dual local conditions and Galois signs explicitly. An unproven "integral primitive system" or a fake p-adic lifting of the residual two-q construction cannot be used.

This note **corrects** but does not repeat any previously certified prime-specific computation and does not claim global Sha finiteness or the exact complex BSD leading-term identity.

### References
- Mazur–Rubin, *Controlling Selmer groups in the higher core rank case* (2016), DOI 10.5802/jtnb.933, especially core rank formula for \(T_p\) of abelian varieties over number fields: https://jtnb.centre-mersenne.org/item/JTNB_2016__28_1_145_0/
- Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2* (2022), DOI 10.1017/fms.2021.85.
- Existing project proof of odd-primary quadratic Sha splitting and rank-zero twist: \`paper/389a1_quadratic_base_change_twist_rank0_finite_minus_sha_2026-10-27.md\`.
- Earlier **residual-only** two-q construction: \`paper/bsd389_Poitou_Tate_core_rank_two_exact_Sha_dual_2026-11-06.md\`.
