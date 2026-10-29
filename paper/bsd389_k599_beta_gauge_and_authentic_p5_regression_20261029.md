# 389a1: removing the Artin–Schreier embedding constant; exact p=5 Fourier regression

**Date:** 2026-10-29. **Status:** elementary proof of gauge normalization, source code regression ready to be executed under SageMath; NOT a completed p599 Kurihara/Sha computation.

## 1. A removable embedding constant

Fix `p=599`, `q1=6912461`, `q2=13963889`, and fixed multiplicative logarithms `ell_i: F_qi^* -> F_p` associated with the primitive roots `(g1,g2)=(2,3)`; set `c1=ell_1(p)=187` and `c2=ell_2(p)=56`. Given a primitive `n=q1*q2` root `zeta` in a common cyclotomic extension, set `zeta_1=zeta^q2`, `zeta_2=zeta^q1` and `A_i=sum_(x != 0) ell_i(x) zeta_i^x`. The established change-of-variable identity is `F_i(t)=A_i+ell_i(t)` for `t!=0`.

The Artin–Schreier equations `A_1^p-A_1=c1`, `A_2^p-A_2=c2` give `beta=A_2-lambda*A_1 in F_p`, where `lambda=c2/c1=500 mod p`.

**Proposition (gauge normalization).** There exists a primitive `n`-th root `zeta'` such that `A_1'=A_1` and `A_2'=lambda*A_1'` (so `beta'=0`).

**Proof.** Choose a unit `t mod n` with `t ≡ 1 mod q1` and `ell_2(t mod q2)=-beta` (surjectivity of the discrete logarithm and CRT). Put `zeta'=zeta^t`. Then `zeta_1'=zeta_1`, while the Fourier change-of-variable identity yields `A_2'=F_2(t)=A_2+ell_2(t)=A_2-beta=lambda*A_1`. Since `t` is a unit, `zeta'` remains primitive of order `n`. QED.

In the normalized embedding the two-prime Fourier factor becomes

`W_hat(m) = (A_1+ell_1(mu_1))*(lambda*A_1+ell_2(mu_2))`

for unit frequencies, with `u_1=q2^{-1} mod q1` and `u_2=q1^{-1} mod q2`. The Fourier-modular-symbol transform **must be evaluated using the same new choice of `zeta'`**; a numerical replacement of beta by zero while keeping the old transform is invalid. This removes one arbitrary embedding scalar but does not shorten the modular-symbol computation by itself.

## 2. The genuinely missing computational gate

For the real `p=599`, computing one modular-symbol Fourier coefficient by its literal definition still scans `n=96524838120829` residues; the `4792`-class formula and its top-three Artin–Schreier coordinates do **not** change that complexity. Building the full finite field of extension degree `ord_n(599)=10071454220` is also infeasible. A valid sublinear algorithm must compute the projected traces without constructing the field or the original `n`-term sums.

## 3. An actual end-to-end test at p=5 with genuine 389a1 modular symbols

The new SageMath script [`verification/bsd389_kurihara_fourier_trace_p5_authentic.py`](../verification/bsd389_kurihara_fourier_trace_p5_authentic.py) implements a stringent small-case test with `p=5`, `q1=41`, `q2=61`, `n=2501`. Here `ord_n(5)=60`, the full field `GF(5^60)` is reasonable, and there are `phi(n)/(2*60)=20` sign/Frobenius frequency classes.

The script:

1. Constructs the 390 authentic ECModularSymbol Manin weights (or loads the Sage-exported 393-integer table); computes every `S(a/2501)` exactly modulo 5 and confirms the known direct `delta_2501=4`.
2. Builds a primitive 2501st root in `GF(5^60)` and checks both Artin–Schreier equations.
3. Checks the `beta=0` gauge normalization by an explicit CRT change of root.
4. Enumerates the 20 sign/Frobenius orbits; computes the true modular-symbol Fourier coefficients; forms the relative traces into the degree-5 Artin–Schreier subfield.
5. Extracts the top three coordinates of each relative trace and checks that the signed trace pairing reconstructs `delta_2501=4`.

The script has been Python syntax-checked in the assistant environment. **Its Sage/eclib full regression has not yet been run here.** No PASS claim should be made for step 5 until the Ubuntu Sage execution is supplied.

Suggested command:

```bash
python -u verification/bsd389_kurihara_fourier_trace_p5_authentic.py \
  2>&1 | tee ~/bsd389_fourier_trace_p5.log
```

Expected terminal gate *if successful*:

`K5_AUTHENTIC_FOURIER_ARTIN_SCHREIER_DELTA_PASS 4 classes 20 target_coefficients 60`

**Limitations:** This test will certify a complete symbolic/Fourier pipeline on a manageable *small* arithmetic example. It cannot prove `delta_599 != 0`, or bound `Sha[599^infinity]`, or yield a uniform all-prime Sha support bound.