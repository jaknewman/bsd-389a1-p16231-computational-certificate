# General local-defect theorem for genuine Sha after p-divisible ramification; explicit E389a1 application

**Date:** 2026-11-23. Theorem of arithmetic Galois cohomology, conditional on explicitly stated arithmetic data. No direct global Selmer or Sha computation is claimed, nor any consequence for full rank-two BSD over Q.

## Theorem

Let E/Q be an elliptic curve, p an odd prime, with E(Q)[p]=0 and Sha(E/Q)[p]=0, so that
\(S=\operatorname{Sel}_p(E/\mathbf Q)=E(\mathbf Q)/p\), of dimension \(r=\operatorname{rank}E(\mathbf Q)\).
Let \(\Sigma\) be a finite set of primes q different from p where E has good reduction.
Let K/Q be a finite **Galois** extension, G=Gal(K/Q), such that:
1. for every q in \(\Sigma\), the ramification index of K_w/Q_q is divisible by p for every w|q;
2. E[p](K)=0;
3. E(K)=E(Q) and E(K)[p]=0.

Write \(d_q=\dim_{\mathbf F_p} E(\mathbf F_q)/pE(\mathbf F_q)\), and let \(t_\Sigma\) denote the rank of the simultaneous local Kummer map
\[
\lambda_\Sigma:E(\mathbf Q)/p\longrightarrow\bigoplus_{q\in\Sigma}E(\mathbf F_q)/p.
\]
Then
\[
\boxed{\dim_{\mathbf F_p}\Sha(E/K)[p]^G\ge\sum_{q\in\Sigma}d_q-t_\Sigma.}
\]

### Proof

At good q != p, local \(H_f^1(Q_q,E[p])\) is the unramified Kummer subspace, of dimension \(d_q\). Its singular quotient \(H_s^1=H^1/H_f^1\) has dimension \(d_q\) by Tate local duality and the self-orthogonality of Kummer conditions.

The Poitou–Tate comparison between the standard Selmer structure and the structure **relaxed at \(\Sigma\)** supplies an exact sequence
\[
0\to S\to S^{\mathrm{rel}(\Sigma)}
  \to\bigoplus_{q\in\Sigma}H_s^1(Q_q,E[p])
  \xrightarrow{\delta} S^\vee.
\]
By self-duality the rank of \(\delta\) equals \(t_\Sigma\), the rank of the local reduction map on S=MW(Q)/p. Thus
\[
\dim S^{\mathrm{rel}(\Sigma)}=r+\sum_q d_q-t_\Sigma.
\]

The p-primary tame inertia quotient at q != p is \(\mathbf Z_p(1)\), and E[p] is unramified. Since the inertia subgroup of K_w has index divisible by p, restricting any p-torsion inertia cocycle to it makes that cocycle zero. Therefore every relaxed class becomes unramified (hence locally Kummer) above all q in \(\Sigma\). Elsewhere restriction preserves Kummer conditions. We obtain
\[
\operatorname{res}S^{\mathrm{rel}(\Sigma)}
 \subseteq\operatorname{Sel}_p(E/K)^G.
\]
The inflation–restriction kernel vanishes because E[p](K)=0, so restriction is injective. The subspace S of dimension r maps to E(K)/p=E(Q)/p, which is the entire Kummer subspace of dimension r. Its quotient of dimension \(\sum d_q-t_\Sigma\) therefore injects into \(\Sha(E/K)[p]^G\) via finite-level Kummer exactness. QED.

## The twenty real cyclic fields of degree 25

For E:y²+y=x³+x²−2x and p=5, the user's two independent finite-field point counts give
\[
\#E(\mathbf F_{5351})=5375=125\cdot43,\quad d_{5351}=1,
\]
\[
\#E(\mathbf F_{13001})=13075=25\cdot523,\quad d_{13001}=2.
\]
The rational generators P=(-1,1), Q=(0,-1) obey Q=-P in the first local mod5 quotient and Q=2P in the second. Their joint localization matrix has determinant 3 mod5, so \(t_{\{5351,13001\}}=2\). Hence the defect is
\[
1+2-2=\boxed{1}.
\]
Even \(\Sigma=\{13001\}\) alone gives \(d-t=2-1=1\).

All twenty fields K_r cut out by the depth-25 diagonal characters at 5351 and 13001 have total ramification index 25 at both primes. The existing residual GL2(F5) certificate gives E[5](K_r)=0, while the previously archived twist nonvanishing/rank-stability certificate gives E(K_r)=E(Q). Therefore, assuming those established inputs,
\[
\boxed{\Sha(E/K_r)[5]^{G_r}\ne0\quad\text{for all 20 }r.}
\]
This nonvanishing needs **no Bullach–Honnor theta/Fitting inclusion** once rank stability and base Sha5=0 have been established. The separate Fitting/Smith proof supplies finiteness, the upper cardinality bounds, and the upper limit of 3 on the invariant Selmer dimension. Combining them gives exactly 3 invariant Selmer directions and \(\#\Sha(E/K_r)[5^\infty]\ge25\) by finite Cassels–Tate alternation.

### Explicit complete local 5-torsion basis at q=13001

The pure-Python elliptic-curve law independently computes
\[
A=[523]P=(1365,7777),\qquad
B=[523](2,1880)=(11168,5591).
\]
Both have order 5. B is not in \(\langle A\rangle\), and there are 25 points of 5-torsion in E(F_13001), so A,B form an explicit basis. Furthermore \([523]Q=2A\), showing the rational image has exactly one local direction.

**Caution:** B is a local finite-field point, not itself a global Sha class. The global nonvanishing follows through Poitou–Tate; one cannot replace that argument by a point count.

## Scope

This explains the observed contrast: in the previously certified unit-Kurihara families the two local 1-dimensional targets were fully spanned by MW, leaving no defect; here the second target is 2-dimensional while rational MW maps to a line. The theorem proves a genuine nonzero arithmetic obstruction over the twenty extensions but gives **no exact order of Sha there and no all-prime BSD conclusion over Q**.

See verification/bsd389_p5_all20_local_13001_relaxed_selmer_sha_nonzero_gate.py and paper/bsd389_p5_all20_relaxed_Selmer_nonzero_Sha_theorem_2026-11-23.md.
