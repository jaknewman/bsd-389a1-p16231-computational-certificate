# A fully unconditional rank-two Fitting identity — valid at **every** rational prime

**Date 2026-10-30. Result:** an elementary exact theorem deduced solely from the rank-two Mordell–Weil group, the Kummer exact sequence, Pontryagin duality and standard algebra of Fitting ideals. **No** Kurihara, Castella–Sano, Kato, analytic BSD, Iwasawa main conjecture, finiteness of Sha or p-integral comparison theorem is assumed. The identity applies **also to p=2,3,389**.

## Theorem

Let E/Q be 389a1, for which \(E(\mathbf Q)\cong\mathbf Z^2\) (torsion trivial). Fix **any** rational prime p. Let
\[
 S_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q),\qquad
 A_p=\Sha(E/\mathbf Q)[p^\infty],\qquad
 X_p=S_p^\vee=\operatorname{Hom}_{\mathrm{cont}}(S_p,\mathbf Q_p/\mathbf Z_p).
\]
Then, as **finitely generated \(\mathbf Z_p\)-modules**,
\[
\boxed{X_p\ \cong\ \mathbf Z_p^2\oplus A_p^\vee.}\tag{1}
\]
This is a noncanonical splitting, sufficient for Fitting ideals. Consequently,
\[
\boxed{\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
       =\operatorname{Fitt}_{0,\mathbf Z_p}(A_p^\vee).}\tag{2}
\]

**Exact classification, for EVERY p (not just good ordinary/supersingular):**

1. \(A_p=0\) iff \(\operatorname{Fitt}_2(X_p)=\mathbf Z_p\).
2. \(A_p\) finite iff \(\operatorname{Fitt}_2(X_p)\ne(0)\). If finite,
   \[
   \operatorname{Fitt}_2(X_p)=(\#A_p)\mathbf Z_p
   =p^{v_p(\#A_p)}\mathbf Z_p.
   \]
   Here \(\#A_p\) is a p-power, and the zero group has order 1.
3. \(A_p\) infinite iff \(\operatorname{Fitt}_2(X_p)=(0)\); its dual has positive free \(\mathbf Z_p\)-rank.

## Proof (no mathematical black box specific to BSD)

For every p, the Kummer sequence in arithmetic Galois cohomology gives
\[
0\longrightarrow E(\mathbf Q)\otimes(\mathbf Q_p/\mathbf Z_p)
\longrightarrow S_p\longrightarrow A_p\longrightarrow0.
\]
As the complete free Mordell–Weil rank is exactly two, the left-hand term is \((\mathbf Q_p/\mathbf Z_p)^2\). Applying Pontryagin duality, which is exact on these discrete p-primary groups, we obtain
\[
0\longrightarrow A_p^\vee\longrightarrow X_p
\longrightarrow\mathbf Z_p^2\longrightarrow0.
\]
Since \(\mathbf Z_p^2\) is projective over \(\mathbf Z_p\), every surjection onto it **splits**. This proves (1). The p-primary Selmer group is cofinitely generated; therefore \(X_p\) and \(A_p^\vee\) are finitely generated \(\mathbf Z_p\)-modules.

For any finitely presented module \(M\) over a commutative ring \(R\), the direct-sum formula and \(\operatorname{Fitt}_i(R^2\oplus M)=\operatorname{Fitt}_{i-2}(M)\) for \(i\ge2\) yield (2).

The structure theorem for finitely generated modules over the discrete valuation ring \(\mathbf Z_p\) writes
\[
A_p^\vee\cong\mathbf Z_p^{t_p}\oplus
\bigoplus_{j=1}^s\mathbf Z_p/p^{e_j}\mathbf Z_p .
\]
If \(t_p>0\), then \(\operatorname{Fitt}_0(A_p^\vee)=(0)\), and \(A_p\) contains \((\mathbf Q_p/\mathbf Z_p)^{t_p}\). If \(t_p=0\), the finite dual has \(\operatorname{Fitt}_0=(p^{\sum e_j})\) and \(\#A_p=p^{\sum e_j}\). If \(t_p=s=0\), its Fitting ideal is the unit ideal. All three assertions follow.

## What Kim + Castella–Sano add

The completely unconditional equality (2) already identifies the **correct p-local arithmetic obstruction** for every p. The extra 2026 results tell us what this obstruction is in terms of computable modular symbols *for good p with appropriate Galois/Manin hypotheses*:

- Mazur + Castella–Sano prove \(\mathcal M_\infty(\delta_p)=0\) for all p≥11, p≠389.
- Kim's Theorem 1.8 then identifies \(\operatorname{Fitt}_2(X_p)=p^{m_2(p)}\mathbf Z_p\), where \(m_2(p)\) is the minimal valuation of **two-prime** Kurihara numbers.

**No logical circularity:** (2) does not require Kim or the finiteness of Sha. Kim supplies only a *computational/arithmetic expression* for that unconditional Fitting ideal.

## Exactly what would provide a genuinely uniform Sha bound

Find an explicit nonzero fixed integer \(C\) and a finite explicitly specified set S such that, by a **proved p-integral comparison** (not a numerical analogy),
\[
\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)\supseteq C\,\mathbf Z_p
\quad\text{for every prime }p\notin S.
\]
For p∉S and p∤C, C is a p-adic unit, so the ideal is all \(\mathbf Z_p\), hence \(A_p=0\) from (2), without any further argument by Kim.

**Still OPEN:** construction of this C and this p-uniform comparison. In particular \(C=729\) cannot be inserted merely because 729 is the norm of an unrelated fixed Gross-orbit toric factor.

A finite set of exceptional p remains to be checked even after such a comparison; finite **support** alone need not imply finite Sha if one exceptional p-primary part is infinitely divisible.

## Cassels–Tate crosscheck for finite Sha

At odd p (indeed for the finite p-primary part in the standard principal-polarization setting), Cassels's alternating pairing shows that if \(A_p\ne0\) is finite, its order is a **perfect square**, so \(v_p(\#A_p)\) is a positive **even** integer. This independently matches the paired-cyclic structure in Kim's Theorem 1.8. A p-primary certificate claiming finite Sha of order p (odd exponent) must be audited.

## Full BSD is still a separate second theorem obligation

Even if the global arithmetic argument above established \(\Sha(E/\mathbf Q)=0\), the strong **complex** BSD formula
\[
\frac{L''(E,1)}2=\Omega_E\operatorname{Reg}(E)
\]
would remain to be proved **exactly**. Numerical ratio approximately 1, or one/finitely many p-adic coefficient congruences, does not imply it.

References: [Kim, Theorem 1.8](https://arxiv.org/pdf/2203.12159) (for computable prime-local Fitting ideals); [Castella–Sano, Theorem B](https://web.math.ucsb.edu/~castella/Kurihara.pdf) (unrestricted Kurihara nonvanishing); [Grigorov et al., equations in §1.2.1 and Cassels Theorem 1.5](https://www.wstein.org/papers/bsdalg/bsdalg2.pdf) (Kummer exact sequence, order-square theorem).
