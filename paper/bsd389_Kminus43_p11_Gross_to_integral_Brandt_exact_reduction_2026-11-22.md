# Exact global identification of all Gross P1/P2 ideals and 110-term Brandt formula at p=11

**22 November 2026.** E=389a1, K=Q(sqrt(-43)), p=11; quaternion algebra B=(-43,-389) with maximal order R=Z[1,omega,J,omega J] as certified in the companion notes. This note settles **the source-level adelic fractional-ideal identification** which had remained open in those notes. **No real Brandt-class weight has been newly evaluated** by this proof and hence no new theta-value / Sha conclusion is claimed.

## 1. The source Gross ideal and a global integral multiplier

The Castella–Hsieh Appendix §6 defines P_n^a=(r_n(a)Rhat)∩B for p-adic unit a, where r_n(a)_p=[[1,a/p^n],[0,1]] and r_n(a)_ell=1 for ell !=p. Set omega=(1+sqrt(-43))/2 ∈R, with omega^2-omega+11=0 and Nrd(omega)=11. At p=11, choose the **same fixed split chart** as in our maximal-order note, with rho(omega)=diag(s,t), s≡11 mod121 and t≡111 mod121, where s*t=11 exactly over Z_11, v11(s)=1 and t is an 11-unit. The roots exist uniquely by Hensel.

For n=1,2, let m=11^n. Multiplying every local fractional ideal on the left by the **global** element omega^n gives

    rho(omega^n) r_n(a) = [[s^n,(s^n/m)*a],[0,t^n]] =: L_n(a).

All displayed entries are 11-integral since v11(s)=1. Its determinant is (st)^n=m. Define b=kappa_n*a mod m, where

    kappa_n=((s^n/m)/t^n) mod m = t^(-2n) mod m.

The columns of L_n(a) satisfy `(1,-b)L_n(a)=0 mod m`. Consequently the whole local right lattice L_n(a)M2(Z_11) is contained in the row-kernel lattice

    I_(n,b)_11={X ∈M2(Z_11):(1,-b)X=0 mod m}.

Both lattices have exact index m^2 in M2(Z_11): the first by det(L_n(a))=m (twice, one for each column), the second by surjectivity of the row map modulo m. Hence they are **equal**. At every prime ell!=11, omega is a unit of R_ell because Nrd(omega)=11 and omega∈R, and P_n^a has local component R_ell. Thus omega^n P_n^a and I_(n,b) have exactly the same local lattices at every finite prime. Equality of full Z-lattices follows:

    **omega^n P_n^a = I_(n,kappa_n*a)** for n=1,2 and every unit a.

Global left multiplication by omega^n∈B^× does not change the *right-ideal class*. The equality does not use a global conjugation by the norm-13 generator.

At n=1, t≡1 mod11, so kappa_1=1. At n=2, t≡111 mod121 and `111^(-4) mod121 = 45`, hence

    **omega P_1^a=I_(1,a mod11); omega² P_2^a=I_(2,45a mod121)**.

The pure-Python verifier enumerates all 10 and all 110 units, Hensel lifts s,t to 11^(2n), and checks every congruence; it prints `SOURCE_GROSS_GLOBAL_LEFT_MULTIPLIER_PASS` for both n.

## 2. An explicit quaternion-algebra isomorphism into Sage's Brandt module

Sage's `BrandtModule(389,base_ring=QQ).quaternion_algebra()` uses the algebra (-2,-389). Denote its standard quaternion generators by u^2=-2, v^2=-389, uv=-vu. In this *same* rational algebra define

    i'=(17u-7uv)/30,       j'=v.

Then `(i')²=-43`, `(j')²=-389` and `i'j'=-j'i'` by exact rational arithmetic, using `17²+389·7²=19350=86·15²`. This gives a **rational global algebra isomorphism** from B=(-43,-389) to Sage's Brandt quaternion algebra. Under it:

    omega'=(1+i')/2,    J'=(16i'+i'j')/43,
    R'=Z[1,omega',J',omega' J'].

The reduced-trace Gram determinant is still `−389²`, so R' is maximal. The ideals I_(2,39^k) transfer as **literal right ideals of R'** via their explicit four integral generators in the fixed basis, not through an assumed ideal-class identification.

Each Brandt representative `R_k=BM.right_ideals()[k]` has a maximal **left** order `L_k` and a common right order `R0`. At least one L_k is conjugate to R' (the Brandt list represents all classes and hence all maximal-order types). Sage's documented method `R'.isomorphism_to(L_k,conjugator=True)` returns a quaternion gamma with `L_k=gamma^{-1}R'gamma`. Therefore

    T_a = (I_(2,a) * gamma) * R_k

is a right R0-ideal, whose Brandt class can be certified by `R_j.is_right_equivalent(T_a,certificate=True)` and the exact witness `w*T_a==R_j`. This makes the classification an **actual global exact ideal computation**, with no unverified cross-algebra identification.

The previously archived primitive Brandt eigenvector for E=389a1, checked at Hecke primes 2,3,5,7 with a common rational eigenline of dimension one, is

    V=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,
       2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0).

If the authenticated class index of I_(2,39^k) is j(k), its primitive E-eigenform value is `V[j(k)]` up to the single global p-unit normalization inherent in the JL eigenline. All 110 j(k) remain to be evaluated on Sage; the accompanying runnable script computes and checkpoints them.

## 3. Exact formula for the true n=1 theta coefficient modulo 11

Put r=39 mod121; r has order110. Its Teichmüller factor is `r^11 mod121 =94`, and `r/94 mod121 = 12 = 1+11`. Thus r itself has **principal-unit exponent 1**. The class parameter is b=r^k and the source Gross parameter is `a=45^(-1)b`; since `45=1+4·11`, the source's principal-unit exponent is

    **i(k)=(k-4) mod11**, taking the representative in {0,...,10}.

The 110 k correspond bijectively to source parameters `a=eta*(1+11)^i` with eta in mu_10 and i in {0,...,10}. Castella–Hsieh's source finite formula at level n=1 is

    Theta_1(T)=alpha^(-2) Σ_(i=0)^10 Σ_(eta∈mu10)
        [alpha·phi(P_1^(eta(1+11)^i)) - phi(P_2^(eta(1+11)^i))](1+T)^i.

The P1-class is independent of i (the source a only matters modulo11 there), and

    Σ_i binom(i,2)=binom(11,3)=165≡0 mod11.

Therefore the P1 contribution to the quadratic coefficient is **exactly zero modulo 11**. Moreover `a_11(E)=-4`, so the ordinary unit root obeys `alpha≡-4≡7 mod11` and `−alpha^(−2) ≡ 2 mod11`.

Thus the **genuine** theta coefficient is determined by 110 global Brandt classifications alone:

    **[T²]Theta_1 ≡ 2·Σ_(k=0)^109 V[j(k)]·binom( (k−4 mod11), 2) (mod11)**,

up to the common primitive p-unit eigenvector normalization. It is nonzero iff the explicitly given weighted sum is nonzero modulo 11. This is the final finite computational test for the theta-order-two *unit* at p=11, K=-43. The P1 term need not be computed at all for this mod-11 test. The full theta/Selmer/Kim hypotheses and the true gamma-action remain logically distinct from this test.

## 4. Verification status and references

- **PROVED AND EXECUTED:** global multiplier identity for all source P1/P2, exact 11-adic root and 45-scalar arithmetic, class group r39 generator order110, principal-unit index `i=k−4`, all 110 row-kernel global lattices, and rational quaternion isomorphism formula.
- **PROGRAM READY, NOT EXECUTED IN SAGE HERE:** compute gamma and all 110 Brandt equivalence witnesses, then the weighted quadratic sum and its normalized nonvanishing.
- **NOT CLAIMED:** theta unit for K=-43, a real 11-adic Selmer action rank, global Sha finiteness, exact complex BSD formula.

References: Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Appendix §6 (https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864). SageMath Quaternion Order and right ideal class documentation (https://doc.sagemath.org/html/en/reference/quat_algebras/sage/algebras/quatalg/quaternion_algebra.html). The primitive eigenvector source is `verification/bsd389_p16231_CH_Brandt_unique_JL_eigenline_gate.py` already user-authenticated in this repository.