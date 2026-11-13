# E389a1: exact two-prime oldform degeneracy tensor and its mixed p²-divisible direction

**2026-11-13.** A rigorous statement about modular-curve correspondences, **not** an Euler/Kolyvagin primitivity theorem, a Selmer Fitting theorem or BSD.

## 1. Integral 2x2 degeneracy pairing

For a prime $q\nmid N=389$, let $\alpha,\beta:X_0(Nq)\rightrightarrows X_0(N)$ be the two standard degeneracy morphisms, with induced pullbacks $\alpha^*,\beta^*:J_0(N)\to J_0(Nq)$ and pushforwards $\alpha_*,\beta_*:J_0(Nq)\to J_0(N)$. The standard degree/Hecke correspondence identities are
$$
\alpha_*\alpha^*=\beta_*\beta^*=[q+1],\qquad
\alpha_*\beta^*=\beta_*\alpha^*=T_q.
$$
They follow respectively from the degree $q+1$ of the degeneracy maps and the Hecke correspondence. For discussion and original notation see:
- standard modular oldform/degeneneracy formalism: https://doc.sagemath.org/html/en/reference/modabvar/sage/modular/abvar/homspace.html;
- Hecke correspondence via the two degeneracy maps, e.g. https://www.math.fsu.edu/~agashe/math/urbana.pdf.

Let $E=389a1$ with $T_q$ eigenvalue $a_q$. The action on the two *E-old factors* is therefore the symmetric integral operator
$$
D_q=\begin{pmatrix}q+1&a_q\\a_q&q+1\end{pmatrix}.
$$
Equivalently, if $i:E\to J_0(N)$ is the optimal dual embedding and $\pi:J_0(N)\to E$ its dual quotient, the composite at level $Nq$ is $\pi\circ(\alpha_*,\beta_*)\circ(\alpha^* i,\beta^* i)=[40]\circ D_q$, because the **independent** modular degree is 40. This 40 factor is important at p=5; the normalized matrix $D_q$ alone is not the actual composite on E² at p=5.

Since $p\ge5$ is odd, the basis vectors $e_+=(1,1)$, $e_-=(1,-1)$ give a $\mathbf Z_p$-integral diagonalization (determinant -2 is a p-adic unit):
$$
D_q e_\pm=(q+1\pm a_q)e_\pm.
$$

## 2. The precise link to p-admissibility

For a p-admissible good auxiliary prime q we have $q\equiv1\bmod p$ and $a_q\equiv q+1\equiv2\bmod p$.
Thus
$$
q+1-a_q=\#E(\mathbf F_q)\equiv0\bmod p,\qquad
q+1+a_q\equiv4\bmod p.
$$
The second eigenvalue is a p-adic unit, while the first has valuation $t_q=v_p(\#E(\mathbf F_q))\ge1$. Consequently
$$
\operatorname{rank}_{\mathbf F_p}(D_q\bmod p)=1,\quad
\operatorname{coker}(D_q)_{(p)}\simeq\mathbf Z/p^{t_q}\mathbf Z.
$$
The subscript (p) denotes p-primary part, and the canonical direction for the torsion is $e_-$.

## 3. Two distinct auxiliary primes and the mixed direction

For $n=q_1q_2$ with the primes distinct and both coprime to N, the Hecke/degeneracy correspondences in the two prime directions commute. The four $E$-old maps from level N to level Nn give a normalized composite pairing
$$
D_{q_1q_2}=D_{q_1}\otimes D_{q_2},
$$
up to the harmless reordering of the four basis vectors. The **actual** E⁴ pairing via the fixed modular quotient is $40D_{q_1q_2}$, not $40^2D_{q_1q_2}$, because the pushdown and pullback pass through the degree-40 map once.

Put $t_i=v_p(\#E(\mathbf F_{q_i}))$. The integral change-of-basis $e_\pm\otimes e_\pm$ diagonalizes the tensor product with p-adic diagonal valuations
$$
\boxed{\{0,t_1,t_2,t_1+t_2\}.}
$$
Hence for odd p≥5 the p-primary normalized Smith invariants are exactly
$$
1,\quad p^{t_1},\quad p^{t_2},\quad p^{t_1+t_2}
$$
up to unit factors and ordering, and
$$
\operatorname{coker}(D_{q_1q_2})_{(p)}
\simeq\mathbf Z/p^{t_1}\oplus\mathbf Z/p^{t_2}
\oplus\mathbf Z/p^{t_1+t_2}.
$$

Most importantly the *fully mixed anti-diagonal vector*
$$
v_{\rm mix}=e_-\otimes e_-=(1,-1,-1,1)
$$
has exact integral eigenvalue
$$
\boxed{\lambda_{\rm mix}=
(q_1+1-a_{q_1})(q_2+1-a_{q_2})
=\#E(\mathbf F_{q_1})\#E(\mathbf F_{q_2}).}
$$
Thus $v_p(\lambda_{\rm mix})=t_1+t_2\ge2$ for any admissible pair.
This is a **true integral modular double-degeneracy divisibility**, distinct from the conjectural degree-two **unit** Kurihara coefficient.

## 4. Independently rerun exact sample values

The [pure-Python verifier](../verification/bsd389_two_prime_degeneracy_tensor_audit.py), executed in the assistant's container on 2026-11-13, recomputed every trace $a_q$ via finite-field Legendre sums and checked matrix/tensor ranks over finite fields for all six q. Results:

| p | q1,q2 | #E(F_q1),#E(F_q2) | (t1,t2) | normalized Smith p-valuations |
|---|---|---|---|---|
| 5 | 41,61 | 45,70 | (1,1) | (0,1,1,2) |
| 7 | 113,673 | 105,672 | (1,1) | (0,1,1,2) |
| 107 | 369793,383917 | 369792,384772 | (1,1) | (0,1,1,2) |

For p=5 the full E⁴ pairing has the extra modular-degree factor $40$, increasing all valuations by one; the table is explicitly **for the normalized $D$ matrices**, not the 40-scaled actual map.

## 5. Sharp arithmetic limit and the next missing morphism

This normalized torsion module is **not** $\Sha(E/\mathbf Q)[p^\infty]$. For p=7 and 107, it is nontrivial with elementary divisors $(p,p,p^2)$, while the user-certified actual Sha[p∞] vanishes. This is a direct proof by comparison that any attempt to identify a pure oldform-degeneracy cokernel with Sha is false.

To turn this structural double-degeneracy line into a useful BSD tool, one must construct a **new arithmetic map** from a derived Kato/Kurihara system or a Selmer complex whose induced mixed scalar is *not* simply the Euler product $\#E(\mathbf F_{q_1})\#E(\mathbf F_{q_2})$ but the normalized genuine Kurihara coefficient; then prove the comparison with the transverse Selmer group from [the exact Poitou–Tate identity](bsd389_strict_selmer_chebotarev_detection_and_norm_projection_no_go_2026-11-05.md).

For the same p=7,107 already Sha=0, a nonzero normalized Kurihara coefficient has been archived; the current $D_q$ calculation does **not** reproduce it. This note is an exact modular *framework and warning*, not an existence theorem for all p.

**Verdict:** new exact p-admissibility/degeneracy identity and mixed p²-divisibility; no new Sha vanishing and no complete BSD.
