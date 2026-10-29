# BSD 389a1 at p=599 — Artin–Schreier and sign/Frobenius Fourier trace reduction

**29 October 2026 — exact algebraic theorem, code-tested small-field identities; NOT an accelerated modular-symbol algorithm and NOT a Kurihara/Sha certificate.**

## Set-up

Let `p=599`, `q1=6912461`, `q2=13963889`, `n=q1*q2=96524838120829`. Let `g1=2` and `g2=3` be primitive roots, and `ell_i(g_i^k)=k mod p`; extend the logarithms by zero at zero. Let `S(a)=[a/n]^+ mod p` for `gcd(a,n)=1` and zero elsewhere. The Néron-normalized plus modular symbol is even: `S(-a)=S(a)` (as usual subject to normalization and mod-p integrality). Set `w(a)=ell_1(a)*ell_2(a)` on units, zero elsewhere. The desired Kurihara number is `delta_n=sum_a w(a)S(a) mod p`.

Choose a primitive n-th root `zeta` in `K=F_(p^d)` with `d=ord_n(p)`. Because `p` and `n` are coprime, Fourier inversion/Parseval holds over `K`. Set `zeta_i=zeta^(n/q_i)` and `A_i=sum_(x != 0 mod q_i) ell_i(x)*zeta_i^x`. Let `u_1=q2^(-1) mod q1` and `u_2=q1^(-1) mod q2`.

## The exact new Artin–Schreier restriction

In characteristic p, Frobenius and the change-of-variable Fourier identity give

`A_i^p = sum_x ell_i(x)*zeta_i^(p*x) = A_i+ell_i(p)`.

Exact primitive-root and order checks give

- `ell_1(599)=187`, with primitive root `g1=2`;
- `ell_2(599)=56`, with primitive root `g2=3`;
- `ord_(q1)(599)=3456230`, `ord_(q2)(599)=3490972`, `d=lcm(...)=10071454220`.

Since both translation constants are nonzero, `A_1` and `A_2` generate the unique degree-p subfield `K0=F_(p^p)` of K. More precisely, let `A=A_1`, `lambda=56/187=500 mod 599`; the element

`beta=A_2-lambda*A` satisfies `beta^p=beta`, hence `beta in F_p`.

**Important:** `beta` depends on the compatible choices of roots `zeta_i` in `K`; its numerical value has NOT been computed. There is no claim that it is zero.

For nonzero frequencies `m mod n` coprime to n, put `b1=ell_1(m*u1 mod q1)`, `b2=ell_2(m*u2 mod q2)`. The Chinese remainder factorization gives

`W_hat(m)=(A+b1)*(lambda*A+beta+b2)`

`= lambda*A^2 + (beta+b2+lambda*b1)*A + b1*(beta+b2)`.

If `m` is not coprime to n, `W_hat(m)=0` because `F_q(0)=0`. Hence **all Fourier weight values lie in the three-dimensional Fp-span of 1, A, A²**, although the original n-th roots require a degree-10-billion extension.

## Frobenius orbits and sign reduction

The number of unit frequencies is `phi(n)=(q1-1)(q2-1)=96524817244480`. Frobenius acts on unit frequencies as `m -> p*m mod n`, and every orbit has size `d=10071454220`. Therefore there are exactly

`phi(n)/d = 9584` Frobenius-orbits.

Moreover, `(q_i-1)/2` is divisible by p, hence `ell_i(-1)=0`: the weight `w` is even. Since the plus symbol `S` is even, `W_hat(-m)=W_hat(m)` and `S_hat(-m)=S_hat(m)`. The order-two element of `<p>` modulo n is `p^(d/2)`, which equals `+1 mod q1` and `-1 mod q2`, and therefore is NOT `-1 mod n`. The sign pairing between Frobenius orbits is free. Thus there are exactly

**`9584/2 = 4792` sign-and-Frobenius frequency classes.**

## Exact three-coefficient trace identity

Let `h=d/p=16813780`, `K0=F_(p^p) subset K`, and for a representative `m` define the *unknown modular-symbol-side trace*

`H_m=Tr_(K/K0)(S_hat(-m)) in K0`.

Write uniquely `H_m=sum_(k=0)^(p-1) h_(m,k)*A^k`, with `h_(m,k) in F_p`. For any `U(A)=u0+u1*A+u2*A^2` and `H=sum_(k=0)^(p-1) h_k*A^k`,

`Tr_(K0/Fp)(U*H) = -(u2*h_(p-3)+u1*h_(p-2)+u0*h_(p-1))`.

**Proof:** The Fp-conjugates of A are `A+j*c1` (`j in F_p`). For `0<=r<=p+1`, the elementary finite-field power sums imply `Tr(A^r)=0` except `Tr(A^(p-1))=-c1^(p-1)=-1`. Since `deg(UH)<=p+1`, only the coefficient of `A^(p-1)` contributes.

Combining Parseval, tower traces, and sign pairing yields the exact formula

`delta_n = -2*n^(-1)*sum_(m in ((Z/n)^* / <p,-1>)) [lambda*h_(m,596) + (beta+b2+lambda*b1)*h_(m,597) + b1*(beta+b2)*h_(m,598)] mod 599`.

Since `n≡1 mod 599`, `n^(-1)≡1 mod 599`. The formula therefore has **4792 terms, each involving only three special Fp coefficients** of an explicitly defined relative trace of the modular-symbol Fourier transform. This represents **14376 specified coefficient positions** and the one shared embedding constant beta.

### Limitation that must not be blurred

This is an **exact algebraic compression of the target information, not a proven sublinear algorithm**. The `H_m` values are not yet calculated. Computing even one `H_m` from its definition may entail a huge trace of a Fourier transform whose naive construction still requires the original `n` modular-symbol values. The scalar `beta` is also not yet computed in a chosen compatible field embedding. We do **not** infer `delta_n != 0`, `Sha[p^infinity]=0`, or global Sha finiteness. The next substantive research problem is to give a certified fast algorithm for those 14376 projected coefficients (or just their weighted total), exploiting the fixed level 389 Hecke/Manin structure.

## Reproducible verification

Run `python verification/bsd389_k599_artin_schreier_trace_gate.py`. The stand-alone program checks 599-primality and exact multiplicative orders, 599-torsion logarithms of 599, all orbit numbers, the sign condition, the cyclotomic Artin–Schreier identity in small formal quotient rings `(p,q)=(5,41),(5,61),(7,113),(7,673)`, full CRT group-ring factorization for seven frequencies at `p=5,n=2501`, and the three-coefficient trace formula in two independent small Artin–Schreier fields. No Sage, eclib or elliptic-curve computations are used in these *algebraic* tests.

The p599 numerical values follow from exact modular arithmetic, not extrapolation from toy tests. All assertions about the actual mod-599 modular-symbol table continue to depend on the separately certified Sage/eclib normalization and on the user-executed bounded pilots.