# 389a1 — an exact finite-depth gate for the quadratic theta coefficient

**22 November 2026.** Status: rigorous formal coefficient lemma and executable arithmetic interface, **not** a BSD or uniform nonvanishing proof.

## The coefficient comparison

Let \(p>2\) be an ordinary split prime and \(F(T)=\Theta_{E/K,p}(T)\in\mathbb Z_p[[T]]\). Denote by \(F_n\) the actual finite theta approximants of Castella–Hsieh Appendix §6. Assume the source's exact integral congruence
\[
F(T)\equiv F_n(T)\pmod{(1+T)^{p^n}-1}.
\]
Writing \(c_j=[T^j]F\) and \(c_{j,n}=[T^j]F_n\), for \(j=0,1,2\) and \(p>2\),
\[
c_0=c_{0,n},\qquad c_1\equiv c_{1,n}\pmod{p^n},\qquad
c_2\equiv c_{2,n}\pmod{p^n}.
\]
Indeed \(\binom{p^n}{1}=p^n\) and \(\binom{p^n}{2}=p^n(p^n-1)/2\); the constant term of \((1+T)^{p^n}-1\) is zero. In fact all coefficients of degree \(j<p\) are divisible by \(p^n\).

**Corollary (necessary and sufficient):**
\[
c_2\neq0\quad\Longleftrightarrow\quad
\exists n\ge1:\ c_{2,n}\not\equiv0\pmod {p^n}.
\]
This is stronger as a detection method than requiring nonvanishing modulo \(p\). For \(c_2=p^v u\) with \(u\) a unit, every \(n\le v\) fails and every \(n>v\) detects it.

## Exact order-two lemma

Assume \(c_0=0\) exactly and the functional equation has the form
\[
F(-T/(1+T))=\varepsilon U(T)F(T),\quad \varepsilon\in\{+1,-1\},\quad U(0)=1,\quad U(T)\in 1+T\mathbb Z_p[[T]].
\]
Suppose a **genuine**, properly normalized finite Gross theta \(F_n\) has
\[
c_{1,n}\equiv0\pmod {p^n},\qquad c_{2,n}\not\equiv0\pmod {p^n}.
\]
Then \(\operatorname{ord}_T F=2\). Proof: \(c_1\equiv0\) and \(c_2\not\equiv0\pmod{p^n}\). If \(\varepsilon=+1\), the degree-one coefficient gives \(-c_1=c_1\), hence \(c_1=0\). If \(\varepsilon=-1\), the degree-two coefficient gives \(2c_2=-(1+u_1)c_1\), which contradicts nonvanishing of \(c_2\bmod p^n\) since \(p\) is odd. Thus \(\varepsilon=+1\), \(c_1=0\), \(c_2\neq0\).

The degree-one congruence **cannot be omitted** unless the exact sign/functional-equation symmetry has already been proved.

## Finite sums and authentication

With \(\alpha\) the ordinary unit root of \(X^2-a_p(E)X+p\), define the actual aggregated Gross weights \(W_i\) from the Appendix §6 formula (the full \(a\)-sum and orientations must be sourced, not inferred). Then the exact finite coefficients are
\[
c_{j,n}=\alpha^{-n-1}\sum_{i=0}^{p^n-1}W_i\binom{i}{j},
\qquad j=0,1,2.
\]
The companion standard-library Python gate accepts a CSV containing all rows \((i,W_i)\) for \(0\le i<p^n\), lifts \(\alpha\bmod p^n\), and evaluates the three moments modulo \(p^n\).

**Critical distinction:** its self-tests use only synthetic weights. It does **not** establish the provenance of quaternionic Gross points, adelic orientation, the weight-one auxiliary nonvanishing, or a new genuine nonzero theta coefficient.

Changing the principal-unit generator by \(1+T=(1+S)^k\) with \(k\in\mathbb Z_p^\times\) transforms \(c_1\) to \(kc_1\) and \(c_2\) to \(k^2c_2+\binom{k}{2}c_1\). Once \(c_1=0\), quadratic nonvanishing is invariant.

## BSD scope

The theta order-two criterion, together with all Castella–Hsieh A/B hypotheses, would imply the expected rational \(p\)-adic Selmer dimension \(2\) for that prime, hence finiteness of \(\Sha[p^\infty]\) given the proven rank \(2\). It does **not** imply \(\Sha[p^\infty]=0\), finite prime support of \(\Sha\), or the exact complex BSD leading-coefficient formula. None of those conclusions is asserted here.

**Next source-dependent proof obligation:** supply actual Gross \(W_i\) with authenticated normalization, then prove a prime-uniform integral relation between a fixed arithmetic object and the rank-two Selmer/Fitting defect (or independently establish the all-prime BSD leading term).

**Reference:** F. Castella and M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Theorems A/B and Appendix §6, https://web.math.ucsb.edu/~castella/Kato.pdf .


## Published genuine example on this exact curve

**Castella–Hsieh, Appendix §6, Table 1 (printed p. 27)** reports for **E=389a1, p=11, K=Q(sqrt(-2))** the actual Gross theta series
\[
\Theta_{E/K,11}(T)\equiv10T^2+69T^3+T^4+103T^5+106T^6+66T^7+11T^8+55T^9+110T^{10}\pmod{(11^2,T^{11})}.
\]
In particular, \(c_1=0\bmod 11^2\) and \(c_2=10\bmod 11^2\) is nonzero. This is **a published numerical computation for 389a1**, not a newly executed verification of the source Gross orbit here. Subject to the Theorem A/B hypotheses, it establishes the **prime-specific** theta-order-two and generalized Kato nonvanishing result. It does **not** generalize to all p and does not yield the full BSD leading coefficient.

The same Table 2 records a useful contrasting example **E=571b1, p=5** with \(c_2=100\bmod125\): nonzero at depth three but zero at depths one and two. This directly motivates the finite-depth criterion above.
