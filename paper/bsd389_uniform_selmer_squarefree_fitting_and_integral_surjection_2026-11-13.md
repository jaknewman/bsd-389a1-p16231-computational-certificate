# 389a1: squarefree uniform Fitting criterion and the exact direction of the missing arithmetic map

**13 November 2026.** **Status:** the two algebraic criteria in §§1–2 are unconditionally proved; their hypotheses are **not** established for E389a1. Neither global finiteness of Sha nor strong BSD is claimed.

## 1. A squarefree integer in all second Fitting ideals forces Sha = 0

Let E/Q be an elliptic curve of proven Mordell–Weil rank 2 and with trivial rational torsion. Set for every rational prime p

$$
X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee.
$$

The Kummer exact sequence and the projectivity of \(\mathbf Z_p^2\) give an abstract split exact sequence

$$
X_p\simeq \mathbf Z_p^2\oplus
\operatorname{Sha}(E/\mathbf Q)[p^\infty]^\vee.
$$

For the finitely generated \(\mathbf Z_p\)-module \(T_p=\operatorname{Sha}[p^\infty]^\vee\), the direct sum formula for Fitting ideals yields

$$
\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
=\operatorname{Fitt}_{0,\mathbf Z_p}(T_p).
\tag{1}
$$

**Theorem 1.** If there exists an **independently constructed**, nonzero integer \(C\) for which

$$
C\in\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
\quad\text{for all rational primes }p,
\tag{2}
$$

then the entire group \(\operatorname{Sha}(E/\mathbf Q)\) is finite and its order divides \(|C|\). In fact, by Cassels–Tate,

$$
\#\operatorname{Sha}(E/\mathbf Q)
\mid\prod_{p} p^{\,2\lfloor v_p(C)/2\rfloor}.
\tag{3}
$$

In particular, if \(C\) is squarefree, then \(\operatorname{Sha}(E/\mathbf Q)=0\).

**Proof.** Over the PID \(\mathbf Z_p\), every finitely generated module has a decomposition \(T_p\simeq \mathbf Z_p^{d_p}\oplus\bigoplus_i\mathbf Z_p/p^{e_i}\). Its zero-th Fitting ideal is zero if \(d_p>0\), and otherwise is \(p^{\sum_i e_i}\mathbf Z_p\). Thus (1)–(2) with \(C\ne0\) force \(d_p=0\) for all p and yield \(\#\operatorname{Sha}[p^\infty]\mid p^{v_p(C)}\). For p not dividing C this order is 1. Therefore only finitely many finite primary parts are nonzero, so global Sha is finite with order dividing C.

For an elliptic curve with finite Sha, its Cassels–Tate pairing is alternating and perfect, hence **each** primary subgroup has square cardinality. Thus every \(\sum_i e_i\) is even and (3) follows. If C is squarefree, each upper bound \(v_p(C)\le1\) forces \(\sum_i e_i=0\). QED.

**Source on the alternating pairing and square order:** Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, global duality, Thm 17.2 / Cor 17.2.1 (https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf); Poonen–Stoll, *Annals* 150 (1999), introduction (https://www.maths.tcd.ie/EMIS/journals/Annals/150_3/poonen.pdf).

**Critical status:** Existence of \(C\) in (2) is the unsolved uniform Sha support problem expressed as an independently verifiable arithmetic construction. One cannot define C to be \(\#\operatorname{Sha}\) and then call (2) an independent proof.

## 2. An exact sufficient integral surjection criterion

Let \(M\) be a **fixed finitely generated abelian group of rank exactly 2** with a specified p-independent integral presentation

$$
\mathbf Z^m \overset{D}{\longrightarrow}\mathbf Z^{m+2}
\longrightarrow M\longrightarrow0
$$

where D has rational rank \(m\). Put

$$
C_M=\gcd\{\text{all }m\times m\text{ minors of }D\}\ne0.
$$

The Smith normal form gives \(M\simeq\mathbf Z^2\oplus T\), with \(T\) finite and \(\#T=C_M\) (taking absolute values).

**Theorem 2.** Assume for each p there is a **specified, mathematically justified surjective homomorphism**

$$
\phi_p:M\otimes_{\mathbf Z}\mathbf Z_p\twoheadrightarrow X_p.
\tag{4}
$$

Then \(\operatorname{Sha}(E/\mathbf Q)\) is finite and \(\#\operatorname{Sha}\mid C_M\). If \(C_M\) is squarefree, Sha is trivial.

**Proof.** \(\operatorname{rank}_{\mathbf Z_p}X_p\ge2\) by Kummer. Surjectivity of (4) implies its rank is at most the rank 2 of \(M\otimes\mathbf Z_p\); hence equality. The kernel of (4) therefore has rank zero, so it lies in the finite torsion \(T\otimes\mathbf Z_p\). Thus \(X_p\simeq \mathbf Z_p^2\oplus (T\otimes\mathbf Z_p)/\ker\phi_p\), with the torsion order dividing \(\#T[p^\infty]\). The Kummer splitting implies \(\Sha[p^\infty]^\vee\) has the same torsion order. Product over all p proves \(\#\Sha\mid C_M\); apply Theorem 1 and Cassels–Tate. QED.

Equivalently, the standard **surjection-monotonicity** of Fitting ideals gives

$$
(C_M)\mathbf Z_p
=\operatorname{Fitt}_2(M\otimes\mathbf Z_p)
\subseteq\operatorname{Fitt}_2(X_p).
\tag{5}
$$

**A less stringent version:** if (4) is proved only for p outside a finite exceptional set S, the same conclusion holds **outside S**. The p-primary Sha parts at S must be controlled independently to conclude global finiteness or Sha=0.

**Logical risk:** Asserting the existence of an abstract surjection without arithmetic construction is circular. The required proof is a *natural integral construction of (4) compatible with actual Galois cohomology/Selmer conditions*, not a comparison of abstract modules chosen after determining Sha.

## 3. The already-certified Hecke determinant 2: wrong direction of comparison

The real user Sage 10.9 run [saved here](../results/bsd389_integral_hecke_smith_2_3_5_USER_PASS_2026-11-02.md) proves for the genuine integral plus modular-symbol lattice of level 389 that

$$
A=\begin{pmatrix}T_2+2I\\T_3+2I\end{pmatrix}
:\mathbf Z^{33}\to\mathbf Z^{66}
$$

has rank 32 and exact Smith product 2. Therefore the concrete abelian module

$$
H=\operatorname{coker}(A^{t}:\mathbf Z^{66}\to\mathbf Z^{33})
\simeq\mathbf Z\oplus\mathbf Z/2,
$$

and \(M_\mathrm{Hecke}:=\mathbf Z\oplus H\simeq\mathbf Z^2\oplus\mathbf Z/2\) has \(C_M=2\).

If one could **independently construct a valid surjection** \(M_\mathrm{Hecke}\otimes\mathbf Z_p\twoheadrightarrow X_p\) for every odd p, Theorem 2 would imply all odd p-primary Sha groups are zero. Together with the separately certified \(p=2\) vanishing, this would prove \(\operatorname{Sha}(E/\mathbf Q)=0\).

**But this crucial map has NOT been constructed.** The integral Hecke eigenline does not automatically map *surjectively* onto the full Galois Selmer dual. In fact the natural Kummer-dual map goes in the **opposite direction**:

$$
X_p\twoheadrightarrow
(E(\mathbf Q)\otimes\mathbf Q_p/\mathbf Z_p)^\vee
\simeq\mathbf Z_p^2.
$$

The missing opposite surjection is the Sha obstruction itself. The module \(M_\mathrm{Hecke}\) has the correct convenient algebraic size, but this is **not** evidence it satisfies the arithmetic comparison (4). The proof cannot be completed by renaming the Smith determinant \(2\) as a Selmer Fitting determinant.

## 4. Valid next target: integral Selmer-complex Euler/Kolyvagin comparison

Rather than use an arbitrary finite Hecke module, look for a **canonical integral arithmetic construction** (e.g. a derived Euler/Kolyvagin system via a Nekovář Selmer complex) supplying either (2) directly or a genuine morphism (4). Such a theorem must:

1. Establish a map/projection on the **actual p-primary Selmer dual**, not only the modular-symbol lattice, the rational MW wedge, or the ordinary Kato rank-one core-rank complex.
2. Control denominators and primitivity for **all but finitely many p**, *uniformly*, without assuming finiteness of Sha or rank of Selmer exactly 2.
3. Track all p-local and Tamagawa corrections, including bad 389 and the small primes.
4. Exhibit a **nonzero integer C** from fixed arithmetic input such that (2) holds, ideally with squarefree part or explicit valuations.

Relevant machinery (not claiming these hypotheses are already met for this curve): Burns–Sakamoto–Sano, *Higher rank Euler, Kolyvagin and Stark systems II*, Thm 5.25 (https://nms.kcl.ac.uk/david.burns/web_page/bss.pdf), and Bullach–Burns, *On Euler systems and Nekovář-Selmer complexes* (https://arxiv.org/abs/2509.13894). The general literature does not by itself supply p-independent primitivity for E389a1.

**Mathematical verdict:** Theorems 1 and 2 and the Hecke comparison obstruction are rigorous, but no new arithmetic Selmer surjection or independent nonzero uniform C has been produced; neither complete Sha finiteness nor complex BSD follows yet.
