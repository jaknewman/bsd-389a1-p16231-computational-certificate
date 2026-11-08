# BSD 389a1 — Castella's rank-two Kato criterion at p=16231 (2026-11-08)

**Scope:** an independently checked admissible auxiliary family and a precise conditional Selmer theorem. This note does **not** establish nonvanishing of the generalized Kato class, finiteness of Sha(389a1)[16231^∞], or global BSD. All existing p=16231 and rank-zero twist certificates are reused, not rerun.

## 1. The published-source theorem

F. Castella, *Nonvanishing of Generalised Kato Classes and Iwasawa Main Conjectures* (June 20, 2024), Theorem A / Theorem 5.2.3 and Choice 5.2.1: https://web.math.ucsb.edu/~castella/GKC-IMC.pdf .

For good ordinary p>3, absolutely irreducible E[p], a prime q||N satisfying the article's ramification condition, an image condition, and an admissible auxiliary pair (K,chi), the generalized Kato class kappa_p(E) in Sel(Q,V_pE) satisfies

    kappa_p(E) != 0 ==> dim_{Q_p} Sel(Q,V_pE)=2.

Conversely, if dim=2, then kappa_p(E) !=0 iff the localization to E(Q_p) tensor Q_p is nonzero. For E=389a1 this latter condition is automatic: an infinite-order P in E(Q) stays infinite-order in E(Q_p), and the kernel of the local p-adic logarithm consists of torsion.

The standard V_p Kummer exact sequence identifies the excess of dim Sel(Q,V_pE) above the known MW rank 2 with (T_p Sha(E)) tensor Q_p. Since Sha(E)[p] is finite by finite p-Selmer, its p-primary part is finite iff this excess vanishes. Thus, under the source theorem's hypotheses,

    kappa_p(E) != 0 <==> dim_{Q_p} Sel(Q,V_pE)=2
                       <==> Sha(E/Q)[p^infty] is FINITE.

**This proves neither kappa_p(E) !=0 nor Sha[p^infty]=0.** An integral theorem would still be required to determine the order.

## 2. Exact p=16231 specialization

E has minimal model y²+y=x³+x²−2x, N=389, minimal discriminant +389, and multiplicative I_1 reduction at 389. The existing independent residual-image certificate establishes surjectivity of E[16231]; the q=389 condition in Castella's theorem is also satisfied. Elementary F_p point counting gives a_16231=128, so p=16231 is good ordinary.

Take K=Q(sqrt(-3)) and ell=7. The field K has discriminant -3, 389 is inert (389=2 mod 3), 16231 splits (16231=1 mod 3), and 7 splits (7=1 mod 3). Also 7 is coprime to 6*389*16231, with a_7(E)=-5 (good ordinary). The project already certified L(E^(-3),1)!=0 exactly, so the quadratic twist of E by K is rank zero.

## 3. An explicit Frobenius witness for nontrivial local chi

Write O_K=Z[omega], omega²+omega+1=0, and pi=51−94 omega. Then

    Norm(pi) = 51² + 51*94 + 94² = 16231.

The two roots of omega²+omega+1 modulo 7 are 2 and 4. Hence pi maps to (3,4) in F_7×F_7, with quotient ratio 3/4=6 mod 7. The six global units project to the subgroup {1,2,4} in the ratio group F_7^×. Therefore the class of pi is nontrivial in the ring-class group of conductor 7, of order 2. In particular infinitely many characters of ring-class conductor a power of 7 detect Frobenius at pi, satisfying chi|_{G_{K_p}} !=1.

Castella's Choice 5.2.1 / Remark 5.2.2 cites the nonvanishing theorem of Vatsal ensuring L(E/K,chi,1)!=0 for all but finitely many suitable 7-power ring-class characters. Since infinitely many detect pi, there exist admissible chi of sufficiently large 7-power conductor meeting both conditions. This existence uses the cited analytic theorem; **no explicit chi, central value, or generalized Kato class has been computed** in this note.

## 4. Exact next gate

For any such chi,

    kappa_16231(E;K,chi)!=0
       <==> dim_{Q_16231} Sel(Q,V_16231 E)=2
       <==> Sha(E/Q)[16231^infty] finite.

The missing assertion is **kappa_16231(E;K,chi) !=0**. Nonvanishing of L(E/K,chi,1), of archived Manin/Jref coefficients, or of a rank-zero twist does NOT prove it. A genuine computation or theorem identifying a nonzero p-adic Abel–Jacobi/diagonal-cycle specialization is required.

Even success at p=16231 would not imply global Sha finiteness; the 2024 result is an ordinary-prime criterion, not a uniform all-prime theorem, and it does not prove the complex rank-two leading-coefficient BSD formula.

## Sources

- Castella (2024): https://web.math.ucsb.edu/~castella/GKC-IMC.pdf (Theorem A, Choice 5.2.1, Theorem 5.2.3).
- Castella–Hsieh (2022), *Forum of Mathematics, Sigma* 10, e12: https://doi.org/10.1017/fms.2021.85 .
- LMFDB E=389a1: https://www.lmfdb.org/EllipticCurve/Q/389a1/ .
- This PR #12: earlier twist E^(-3) exact nonvanishing and residual-image certificates.
