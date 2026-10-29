# BSD 389a1 p=599 — exact finite-Fourier factorization of two Kurihara logarithmic weights

**Date 2026-10-29. Status: PROVED algebraic identity / new research avenue, NOT an accelerated Kurihara algorithm and NOT a Sha certificate.**

## Theorem: the additive Fourier spectrum of a discrete logarithm is a translate

Let `p` and `q` be distinct odd primes with `q ≡ 1 (mod p)`, let `g` be a primitive root modulo q, and define the additive-valued discrete logarithm `ell(g^k)=k mod p`. Extend `ell(0)=0`. Let `R=F_p[zeta_q]` with zeta_q a *formal primitive qth root* (the quotient `F_p[Z]/(1+Z+...+Z^(q-1))` is sufficient). Define

`F_q(t)=sum_{x in F_q^*} ell(x)*zeta_q^(t*x)` in R.

Then

- `F_q(0)=0` (as q−1 is a multiple of p);
- for all `t != 0 (mod q)`, **`F_q(t)=F_q(1)+ell(t)`** in R.

**Proof.** For `t != 0`, substitute `y=t*x` and use `ell(t^{-1}y)=ell(y)-ell(t)` modulo p. Thus

`F_q(t)=F_q(1)-ell(t)*sum_{y !=0} zeta_q^y = F_q(1)+ell(t)`

because `sum_{y !=0} zeta_q^y=-1`. Also `sum_{x !=0}ell(x)=((q-1)/p)*sum_{j=0}^{p-1}j=0 mod p` for odd p. QED.

## Two-prime CRT factorization

For distinct `q1,q2 ≡1 mod p`, define `n=q1*q2` and `w(a)=ell_1(a mod q1)*ell_2(a mod q2)` on units, and `w(a)=0` otherwise. For a primitive formal n-th root zeta_n, let `W(m)=sum_{a mod n}w(a)*zeta_n^(m*a)`. Put `u1=q2^{-1} mod q1` and `u2=q1^{-1} mod q2`, and let `A_i=F_{q_i}(1)`. The Chinese remainder isomorphism immediately yields

`W(m)=F_{q1}(m*u1)*F_{q2}(m*u2)`.

Hence `W(m)=0` whenever `q1|m` or `q2|m`. Otherwise

**`W(m)=(A_1+ell_1(m*u1))*(A_2+ell_2(m*u2))`.**

This is an exact identity after reducing in characteristic p. It holds for our actual `p=599`, `q1=6912461`, `q2=13963889`, independently of the elliptic curve.

## What this does and does not accomplish

This eliminates the need to compute a full additive Fourier transform of the **logarithmic weight** by a quadratic two-dimensional search. To obtain the actual Kurihara number, one must still pair that weight against **all** modular-symbol values `[a/n]^+`; equivalently one must calculate sufficiently many additive Fourier coefficients of those modular symbols, with a proven integral normalization and exact reduction modulo p. That step is **not constructed** by this identity. In particular, no new upper bound on `Sha[599^infinity]` follows.

Potential research target: an exact fast additive-twist/Hecke transform of the fixed-level `Gamma0(389)` modular symbol that interacts with the factorized `W(m)`, with rigorous arithmetic reconstruction. It would be a genuine improvement only after the symbol-side pairing is proven faster than `O(n)`.

Toy unit tests in the cyclotomic quotient `F_p[Z]/Phi_q(Z)` pass for `(p,q)=(5,11),(5,31),(7,29)`, testing all `q-1` nonzero frequencies, the zero-frequency condition, and the quotient relation. These validate a small implementation but the symbolic proof above is general.

**GLOBAL STATUS: no full delta_599, no proof Sha[599∞]=0, no global prime support bound.**