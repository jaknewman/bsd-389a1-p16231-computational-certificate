# Universal source-to-C++ identity for the cyclotomic \(J_{\mathrm{ref}}\) at \(p=16231\)

Date: 2026-11-06. **This is an algebraic proof for EVERY input pair, not a spot-check.**

Scope: The exact scalar returned by \`verification/independent_c01_scalar_J.cpp\`, fed the declared Manin relation export and a table of genuinely normalized modular-symbol values, equals the mathematically defined
\[
J_{\rm ref}=-\sum_{a=1}^{p-1}\sum_{b=0}^{p-1}
 w(a,b)\bigl[M_1(D_x)-\kappa(a,b)M_0(D_x)\bigr]\pmod p,
\quad x=a+pb,\quad D_x=\begin{pmatrix}1&x\\0&p^2\end{pmatrix}.
\]
It does not assert that an arbitrary untrusted binary file contains genuine modular symbols. That distinct provenance assumption is explicitly separated below.

Here \(N=389\), \(p=16231\), \(a_p=128\), \(P=\operatorname{diag}(p,1)\), \(\beta_t=\begin{pmatrix}1&t\\0&p\end{pmatrix}\), and \(m\) is the *actual* plus modular symbol with Sage/eclib \`L_ratio\` normalization. Set
\[
F(D)=m(D\infty)-m(D0),\quad
M_0(D)=F(D)-\alpha^{-1}F(PD),\quad
M_1(D)=\alpha^{-1}\sum_{t\bmod p}tF(\beta_tD)\pmod p
\]
where \(\alpha\equiv a_p=128\pmod p\).

## Lemma 1: exact universal action of \(\Gamma_0(Np)\)

For **every** \(h=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(Np)\), every degree-zero cusp divisor \(D\), and any modular symbol \(F\) with \(T_p F=a_pF\),
\[
\boxed{M_0(hD)=M_0(D),\qquad
M_1(hD)=a^2M_1(D)-abM_0(D)\pmod p.}
\]
Proof: \(PhP^{-1}=\begin{pmatrix}a&pb\\c/p&d\end{pmatrix}\in\Gamma_0(N)\), hence \(F(PhD)=F(PD)\), and also \(F(hD)=F(D)\).
For each \(t\bmod p\), put
\[
s\equiv (b+td)(a+tc)^{-1}\equiv a^{-1}b+a^{-2}t\pmod p.
\]
The denominator is invertible because \(c\equiv0\pmod p\) and \(ad\equiv1\pmod p\). The exact matrix \(\beta_t h\beta_s^{-1}\) is in \(\Gamma_0(N)\) (the integrality condition is precisely the defining congruence for \(s\)). Thus \(F(\beta_t hD)=F(\beta_sD)\) and \(t\equiv a^2s-ab\). Summing weighted \(t\) gives \(M_1(hD)=a^2M_1(D)-ab\,\alpha^{-1}\sum_sF(\beta_sD)\). The Hecke identity
\(\sum_sF(\beta_sD)+F(PD)=a_pF(D)\) and \(\alpha\equiv a_p\pmod p\) give \(\alpha^{-1}\sum_sF(\beta_sD)\equiv M_0(D)\). QED.

The exact C++ expression \`q=-h.a*h.b; r=h.a*h.a; m1=q*m0+r*m1\` is **precisely this identity**. This includes every generic and exceptional Shapiro coset, because it applies to any \(h\in\Gamma_0(Np)\).

## Lemma 2: all \(p+1\) base Shapiro moments are computed correctly

The C++ uses \(r_j=\begin{pmatrix}1&0\\Nj&1\end{pmatrix}\) for \(0\le j<p\), and \(r_\infty=\begin{pmatrix}-40&-1669\\N&p\end{pmatrix}\) for the last coset. The latter has determinant one (\(-40p+1669N=1\)). All \(r_j\in\Gamma_0(N)\). The binary table stores
\[
f_G=F(G),\quad f_P=F(PG),\quad f_s=F(\beta_sG)
\]
for each of the 67 Manin generators \(G\).

**The zero-th moment.** \(F(r_jG)=f_G\). For \(j=0\), \(P r_0=P\). For \(1\le j<p\), let \(s=(Nj)^{-1}\bmod p\); then
\(P r_j=H_j\beta_s\), where
\(H_j=\begin{pmatrix}p&-s\\Nj&(1-Njs)/p\end{pmatrix}\in\Gamma_0(N)\).
For \(j=\infty\), \(P r_\infty=H_\infty\beta_0\), with
\(H_\infty=\begin{pmatrix}-40p&-1669\\N&1\end{pmatrix}\in\Gamma_0(N)\).
Therefore the code's \`sel = fP / fs[inv(Nj)] / fs[0]\` for these three cases is **exactly** \(F(P r_jG)\), and \`m0=fG-alpha_inv*sel\` is \(M_0(r_jG)\).

**The first moment, finite \(j\).** For \(t\ne0\), set \(z=(Nt)^{-1}\bmod p\). The matrix \(\beta_t r_j\) belongs to the \(\Gamma_0(N)\)-coset represented by \(\beta_{(N(z+j))^{-1}}\) when \(z+j\ne0\), and to the coset \(P\) when \(z+j=0\). Therefore
\[
M_1(r_jG)=\alpha^{-1}\sum_{z\in\mathbb F_p^\times}
 (Nz)^{-1}\, B[z+j],\quad
 B[0]=f_P,\;\;B[y]=f_{(Ny)^{-1}}\ (y\ne0).
\]
This is precisely the code's \`shifted\`, \`twist\`, and modular cyclic convolution \`cyc[j]\`. The exact NTT/CRT routine reconstructs an integer convolution with a checked upper bound below the product of its two NTT primes; it is not a floating approximation.

**The first moment, \(j=\infty\).** \(\beta_t r_\infty\) belongs to \(\Gamma_0(N)\beta_s\) with
\(s=-1669(-40+Nt)^{-1}\pmod p\) if the denominator is nonzero, and to \(\Gamma_0(N)P\) otherwise. Thus
\[
M_1(r_\infty G)=\alpha^{-1}\sum_{t\bmod p} t
\begin{cases}
f_{-1669(-40+Nt)^{-1}},&-40+Nt\not\equiv0,\\
f_P,&-40+Nt\equiv0.
\end{cases}
\]
This is exactly the special-case loop \`mspecial\` in the frozen C++.

Hence **all 67 × (p+1) input base-moment pairs** are given by these identities, rather than being verified only at sample cosets.

## Lemma 3: all 390 Manin representatives and all Shapiro transports

The SHA-pinned original relation export specifies for each nongenerator \(R_i\) the *integer divisor identity*
\[
[R_i\infty]-[R_i0]=
\sum_{(e,A,G)\in {\rm rel}(i)}
e\bigl([A^{-1}G\infty]-[A^{-1}G0]\bigr),\quad A\in\Gamma_0(N).
\]
The repository's \`verification/audit_c01_exact_manin_cusps_and_exceptional_cosets.py\` verifies this equality as exact rational cusp divisors for **all 390** representatives and all **2012** relation terms, not just a mod-\(p\) equality. The 390 bottom-row projective classes modulo \(N\) are complete and unique.

For any \(j\), apply \(r_j\) to the divisor identity. For each relation term, write \(r_j A^{-1}=h' r_k\) with \(h'\in\Gamma_0(Np)\), using the complete Shapiro projective-key lookup. Lemma 1 gives its moment action. The code \`build_all_manin_moments\` does exactly this with \`X=r_j*A^-1\`, \`k=shapiro_key(X)\`, \`h=X*r_k^-1\`, and accumulates \(e(M_0, M_1)\) with the Lemma 1 affine transformation. Therefore all 390 × (p+1) precomputed moment pairs are correct.

For an arbitrary \(\mathrm{SL}_2(\mathbb Z)\) fragment \(B\), its bottom-row key modulo \(N\) selects a unique \(R_i\) with \(B=\gamma R_i\), \(\gamma\in\Gamma_0(N)\). The Shapiro key selects \(j\) and \(h\in\Gamma_0(Np)\) with \(\gamma=h r_j\). Lemma 1 gives exactly the code's \`Direct.fragment\` moment contribution. No exceptional branch is omitted: \`j=p\` invokes \(r_\infty\) and the preceding formulas.

## Lemma 4: all \(x=a+pb\) are covered by the continued-fraction resolution

For any unit \(x\pmod{p^2}\), the Euclidean convergents used by \`Direct.pair\` construct determinant-one matrices \(B_k\) whose oriented divisors telescope:
\[
\sum_k ([B_k\infty]-[B_k0])=[\infty]-[x/p^2].
\]
This is an exact continued-fraction identity (also audited in
\`audit_c01_exact_manin_cusps_and_exceptional_cosets.py\` for representative edge cases). By linearity, Lemmas 1–3 imply that the sums of \`Direct.fragment\` outputs equal \(M_0(D_x)\) and \(M_1(D_x)\).

The C++ enumerates
\[
0\le {\tt id}<p(p-1),\qquad
a=1+\lfloor{\tt id}/p\rfloor,\quad b={\tt id}\bmod p,
\]
so it covers each \(x=a+pb\) **exactly once**. Its parameter formulas \`fermat,u,teich,kappa,w\` agree identically with the Teichmüller expansion at level \(p^3\); \`Direct.pair\` returns
\[
-w(M_1(D_x)-\kappa M_0(D_x))\pmod p.
\]
Thus the mathematical identity \(\boxed{J_{\rm C++}=J_{\rm ref}\pmod p}\) is proved for every pair, **assuming the binary table stores the declared \(F(G),F(PG),F(\beta_tG)\)**. This is not an extrapolation from the four local tests.

## Exact numeric substitution and connection with \(L_p\)

The user-executed and hash-audited complete C++ run on **263,429,130** pairs recorded \(J_{\rm C++}=4486\pmod{16231}\). Both independent global aggregation implementations agree (the original V19 and independent dual scalar engine).

The Sage 10.9 \`pAdicLseriesOrdinary.series\` and \`measure\` definitions yield for the \(\eta=0,D=1\) branch
\[
A_2^{(3)}-A_2^{(2)}\equiv\frac{p\,J_{\rm ref}}{4\alpha^2}\pmod{p^2}.
\]
Proof: write \(x=\omega(a)(1+p)^u\bmod p^2\) and \(x+p^2c=\omega(a)(1+p)^{u+pv}\bmod p^3\), where \(v=(c-\kappa)/a\bmod p\). The binomial difference is \(pv(2u-1)/2\bmod p^2\). Exact Hecke distribution of the measures cancels the level-2 weight; the additional \(\tfrac12\) factor is \`E.real_components()==2\`. Finally \(\mu_3=\alpha^{-3}(m(y/p^3)-\alpha^{-1}m(y/p^2))\); summing \((c-\kappa)\) kills the level-2 cusp term modulo \(p\). The remaining two moments give \(J_{\rm ref}\). See original derivation \`paper/c01_to_sage_quadratic_coefficient_identity_2026-10-24.md\`.

For \(p=16231\),
\[
 (4\cdot128^2)^{-1}=9362,\quad
 4486\cdot9362=8335\pmod p,\quad
 A_2^{(2)}/p=1199,\quad
 A_2^{(3)}/p=9534\pmod p.
\]
With the archived p-adic regulator \(\operatorname{Reg}_p/p^3\equiv1930\pmod p\), Sage's algebraic BSD factor satisfies \(B_p/p=9534\pmod p\); the normalized quotient has residue **1** and valuation **0**.

In SageMath 10.9 \`sha_tate.py\`, \`p_primary_bound\` returns \`an_padic(p).valuation()\` after surjectivity/reducibility and reduction checks, and its documented Kato/Stein–Wuthrich result gives a **provable** upper exponent. Thus **provided the frozen full-domain computations and table provenance are accepted as a valid computer-assisted certificate**, the arithmetic implication to \(\Sha(E/\mathbb Q)[16231^\infty]=0\) holds. An actual invocation of \`E.sha().p_primary_bound(16231)\` is *not logically necessary* once its exact coefficient and precision have been obtained by an equivalent certified computation.

## Scope and explicit residual trust assumptions

1. The **universal identity** \`J_C++=J_ref\` has no remaining mathematical exceptional cases. It is proved above by formulas, not sampling.
2. The actual numeric value **4486** is from the frozen user-run C++ computation, with two full-domain implementations and a completed source/binary/input/hash/checkpoint audit. No new 263-million-loop execution is claimed here.
3. The frozen binary table's 67 complete Hecke fibres were all checked for the Hecke relation, and available Sage source-oracle checks sample entries (not all \(\sim\!1.09\) million). The entire table's correct provenance as authentic normalized symbols is a machine/eclib trust dependency. A standalone formal proof of every binary table entry is not provided.
4. The archived level-2 coefficient and regulator, and Sage 10.9 semantics/precision, are distinct certified computational inputs. Their verification is referenced, not rerun here.
5. The resulting conditional-on-authenticated-computational-evidence p-primary statement is **not a proof of the full BSD conjecture**, which also requires all other primes and exact complex leading-term equality. It is also not an exact equality of the full p-adic quotient to 1: only \(\equiv1\bmod p\).
