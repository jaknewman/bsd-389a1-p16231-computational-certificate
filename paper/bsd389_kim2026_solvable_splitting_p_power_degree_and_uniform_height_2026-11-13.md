# E389a1 — Kim 2026 ring-class solvable splitting, p-power-degree descent, and exact uniform-height criterion

**2026-11-13. Status: rigorous corollaries of a newly published (October 2026) theorem of Chan-Ho Kim plus elementary restriction–corestriction and finite-group algebra.** No claim that Sha is globally finite, no new Kurihara unit, no complex BSD identity.

## 1. External arithmetic input (genuine theorem, not an inference from numerical checks)

Chan-Ho Kim, *On the arithmetic of Tate–Shafarevich groups via Kolyvagin's conjecture*, arXiv:2609.15328v2, dated 2026-10-28, **Theorem 1.7**, states that for a semistable elliptic curve over Q of conductor N, every Sha element of order prime to N splits in a finite ring-class extension of a suitable imaginary quadratic field, hence in a finite solvable extension over Q.

Primary source (HTML with theorem statement): https://arxiv.org/abs/2609.15328 .
For E389a1, N=389 is squarefree, so the theorem applies to every p-primary Sha class with p>=5 and p!=389. The p=2,3 case is not needed here; the applicability to p=389 is NOT asserted.

**One-element splitting:** For every p>=5, p!=389, and every $\xi\in\Sha(E/\mathbf Q)[p^\infty]$, there is an imaginary quadratic K and an associated ring-class field F=K[c], Galois and generalized-dihedral over Q, such that $\operatorname{res}_{F/\mathbf Q}(\xi)=0$.

## 2. Explicit odd-p ring-class Hall descent

For a ring-class extension F/Q associated to an imaginary quadratic field K, let
$$G=\operatorname{Gal}(F/\mathbf Q)=A\rtimes\langle c\rangle,\qquad
A=\operatorname{Gal}(F/K),\quad c^2=1,\quad cac^{-1}=a^{-1}.$$
The abelian group A decomposes canonically as $A=A_p\times A_{p'}$ into its p-primary and prime-to-p components. For odd p, the subgroup
$$H=A_{p'}\rtimes\langle c\rangle$$
has $|H|=2|A_{p'}|$ prime to p. Its fixed field L=F^H satisfies
$$[L:\mathbf Q]=[G:H]=|A_p|=p^{v_p(|A|)}.$$
The extension L/Q need **not** be Galois; its explicit construction, however, is entirely group-theoretic.

If $\xi$ becomes trivial over F, then the restricted $\xi_L=\operatorname{res}_{L/\mathbf Q}\xi$ satisfies
$$
0=\operatorname{cor}_{F/L}(\operatorname{res}_{F/L}\xi_L)
=[F:L]\,\xi_L.
$$
Because $[F:L]=|H|$ is prime to p and $\xi_L$ has p-power order, $\xi_L=0$.

**Theorem A (proved):** each individual p-primary Sha class of E389a1, with p>=5 and p!=389, becomes trivial over some extension L/Q of p-power degree. This deduction uses Kim's theorem plus the explicit ring-class Galois structure, **not** an assumption of Sha finiteness.

**Necessity of the p-power degree:** If the class $\xi$ has exact order $p^m$, any finite extension M/Q that kills it satisfies
$$p^m\mid[M:\mathbf Q],$$
by applying $\operatorname{cor}\circ\operatorname{res}=[M:\mathbf Q]$. Hence in Theorem A the exponent of $[L:\mathbf Q]$ is at least m.

## 3. Simultaneous annihilation of all of Sha[p^n]

For each n>=1, the group $\Sha(E/\mathbf Q)[p^n]$ is finite, as it injects into the finite-level p^n-Selmer quotient.

Choose finitely many generators $\xi_1,\ldots,\xi_r$ and use Kim's theorem to split each over a finite Galois solvable extension $F_i/\mathbf Q$. Let F be their compositum. It is finite Galois with solvable Galois group and all these classes restrict to zero in F. By P. Hall's theorem, $\operatorname{Gal}(F/\mathbf Q)$ has a Hall p'-subgroup H. Put L=F^H. Then $[L:\mathbf Q]=p^a$ and $[F:L]$ is prime to p. Restriction-corestriction implies the restriction to L of **each** $\xi_i$ is zero.

**Theorem B (proved):** for every n>=1 and every p>=5 with p!=389, there exists a finite extension $L_{p,n}/\mathbf Q$ of degree $p^{a_{p,n}}$ such that
$$
\operatorname{res}_{L_{p,n}/\mathbf Q}
\left(\Sha(E/\mathbf Q)[p^n]\right)=0.
$$
No assumption that $\Sha[p^\infty]$ is finite is made. Here the fields $F_i$ need **not** share the same imaginary quadratic field, so F need not itself be a single ring-class extension; that is why the general Hall theorem is used.

## 4. Exact bounded-degree criterion for p-primary finiteness

Define $a_p(n)$ as the least nonnegative integer a such that there exists some (not necessarily Galois) finite extension L/Q of degree $p^a$ on which every element of $\Sha[p^n]$ becomes zero. Theorem B proves $a_p(n)<\infty$ for every n.

**Theorem C (proved):**
$$
\boxed{\Sha(E/\mathbf Q)[p^\infty]\text{ finite}
\quad\Longleftrightarrow\quad
\sup_{n\ge1}a_p(n)<\infty}
$$
for every p>=5, p!=389.

**Proof:** If the supremum is at most A, then for each $\xi\in\Sha[p^\infty]$ take $n$ with $\xi\in\Sha[p^n]$ and a field of degree p^a with a<=A that kills $\xi$. Restriction-corestriction implies $p^a\xi=0$, hence $p^A\xi=0$. The group $\Sha[p^\infty]$ therefore equals $\Sha[p^A]$, which is finite by finite descent. For A=0, this says $\Sha[p^\infty]=0$.

Conversely, if $\Sha[p^\infty]$ is finite, it has a finite exponent p^m and equals $\Sha[p^m]$; Theorem B supplies a single p-power-degree extension splitting this group, and that same field works for every n. QED.

**Critical non-circular boundary:** Theorem B yields some finite $a_p(n)$ for every fixed n. No uniform bound on $a_p(n)$ as n grows, much less any p-independent bound, is derived from Kim's theorem. Theorem C identifies the still-missing arithmetic input; it does not prove it.

## 5. Exact 16231 first-layer transfer obstruction from existing USER PASS

The user's previously certified [ring-class preflight](../results/bsd389_p16231_anticyclotomic_first_layer_PREFLIGHT_USER_PASS_2026-11-05.md) for K=Q(sqrt(-3)), p=16231, has

$$
h_{p^2}=|\operatorname{Pic}(\mathcal O_{p^2})|
=87\,809\,710=5410\cdot16231,
$$
with $p\nmid5410$. Let $F=K[p^2]$ be this specific conductor-p² ring-class field. Then
$$
[F:\mathbf Q]=2h_{p^2}=175\,619\,420
=10820\cdot16231,\qquad
v_{16231}([F:\mathbf Q])=1.
$$
For any class $\xi\in\Sha(E/\mathbf Q)[16231^\infty]$ that becomes trivial over **this particular F**, restriction–corestriction gives $[F:\mathbf Q]\xi=0$, hence
$$
\boxed{\ker(\operatorname{res}_{F/\mathbf Q}:
\Sha(E/\mathbf Q)[16231^\infty]\to
\Sha(E/F)[16231^\infty])
\subseteq\Sha(E/\mathbf Q)[16231].}
$$

Thus this finite first ring-class layer can **never** kill a class of exact order $16231^2$. This is an exact necessary constraint on any claimed Sha-killing interpretation of the user-certified conductor-p² Gross-point data. **It does not claim** that Kim's abstract theorem chooses this particular K or ring-class field, nor does it assert any nonzero Sha class exists.

An independent short integer-arithmetic verifier is [here](../verification/bsd389_kim2026_ringclass_p_power_transfer_audit.py); it does not compute Sha.

## 6. Implications for the global BSD strategy

- We now have **unconditional-on-Sha-finiteness**, theorem-supported splitting of any one good-p Sha class, and simultaneous splitting of each finite-level $\Sha[p^n]$, using solvable fields of p-power degree.
- The still-missing step is a uniform bound **in n** for such degrees (even for one fixed p). A further all-large-p bound plus exclusion of a finite exceptional prime set would give Sha finiteness. Strong BSD's complex leading-term identity is a separate theorem obligation.
- Restriction–corestriction along p-power degrees can kill p-primary elements, but never makes restriction automatically injective. Avoid inferring $\Sha=0$ from the mere existence of these splitting fields.
- Theorem C is a new geometric formulation of p-primary finiteness, complementary to the fixed-integer Selmer-Fitting criterion. It is not an independently proved finite-support bound.

**Verdict:** Theorems A, B, C, and the explicit p=16231 transfer obstruction follow rigorously from Kim's 2026 Theorem 1.7, standard ring-class Galois structure, Hall's theorem, and restriction–corestriction. Global Sha finiteness and BSD remain unproved.
