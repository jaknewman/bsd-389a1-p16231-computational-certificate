# Kato's proved p-primary exponent bound: installed Sage semantics and arithmetic closure

**Date:** 2026-10-19. **Research status:** arithmetic implication rigorously justified, conditional on the historical analytic C01 certificate representing the true Sage-normalized level-3 coefficient.

## Verified Sage source behavior

In SageMath `src/sage/schemes/elliptic_curves/sha_tate.py`:

- `Sha.p_primary_bound(p)` explicitly promises a **provable upper bound** for `#Sha(E/Q)[p^infinity]`; it applies in rank `>1` under the documented local/Galois hypotheses.
- The checked algorithm accepts ordinary good reduction and a surjective residual Galois representation. It obtains `shan=self.an_padic(p,prec=0,use_twists=True)`, rejects zero, and returns `shan.valuation()`.
- `Sha.an_padic` computes, in the rank-2 ordinary branch, `bsdp=tam*reg*eps/tors/lg**r` where `eps=(1-Kronecker(D,p)/alpha)^2`; it computes `lstar=lp.series(n,quadratic_twist=D,prec=r+1)[r]`, then `shan=lstar/bsdp`.
- For `389a1`, `D=1`, `r=2`, `tam=1`, `tors=1`, and `E.real_components()=2`, consistent with the C01 source-to-reference mathematical bridge.

These statements were checked against the public Sage source; the installed version-specific source signatures are checked by the attached standalone Sage audit script **once executed on the IONOS host**.

Sources:
- https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py
- https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/padic_lseries.py

## Finite integer arithmetic

```text
p                       16231
p²                      263445361
inv(4*128²) modulo p     9362
J = (16014+4703) mod p   4486
(J * 9362) mod p         8335
A2^(2)/p mod p           1199
A2^(3)/p mod p           9534
Reg_p/p³ mod p           1930
alpha mod p              128
alpha^(-1) mod p         5199
(1-alpha^(-1))² mod p   10820
Bp/p mod p               9534
A2/Bp mod p              1
v_p(A2/Bp)               0
```

The **logical theorem** is: If the historical computation `J_V19=4486` equals the mathematically defined `J_ref` for Sage's normalized series, and the previously certified rank/regulator/precision inputs are correct, then `p_primary_bound` has exponent 0, so `#Sha(E/Q)[16231^infinity]<=1`, hence `Sha(E/Q)[16231^infinity]=0`.

**Critical:** This is a rigorously established implication from those premises, *not* a new independent determination of the coefficient or a call to Sage's potentially expensive `Sha.p_primary_bound(16231)`. Exact `u_p=1` and global BSD are not implied by the first p-adic digit.

## Final, inexpensive IONOS test

Run `sage -python bsd389_porte_finale_kato_p16231.py`. The script checks the installed `Sha.p_primary_bound` and `Sha.an_padic` methods via `inspect.getsource`, known local/regulator gates and the exact arithmetic; **it does not compute the level-3 p-adic series**.

Report both the terminal PASS labels and `EXIT_STATUS=0` to freeze a version-specific certificate. If a source-string assertion fails, audit the installed method instead of modifying the expected arithmetic constants.
