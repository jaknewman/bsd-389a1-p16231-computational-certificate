# E = 389a1: independent rank-two Kurihara witness at p = 11

**Computed 2026-11-26; status: reproducible finite calculation plus published theorem, subject to independent review of the modular-symbol implementation.** This note does **not** claim full Birch–Swinnerton-Dyer.

## Curve and rank

\(E: y^2+y=x^3+x^2-2x\), conductor \(N=389\), minimal discriminant \(+389\). Rank \(2\), torsion order \(1\); a saturated basis is \(P=(-1,1),Q=(0,-1)\). The optimal Manin constant equals \(1\). Its only bad prime is \(389\), with Tamagawa number \(c_{389}=1\).

## Prime and auxiliary data

Let \(p=11\), \(q_1=397\), \(q_2=991\), \(n=393427\). Direct exact point counting gives

| q | a_q | #E(F_q) | q mod 11 | a_q mod 11 | v_11(#E(F_q)) |
|---:|---:|---:|---:|---:|---:|
|397|24|374|1|2|1|
|991|-53|1045|1|2|1|

Thus both primes belong to the admissible set \(\mathcal P_1\) of Kim, and each local \(E(\mathbb F_q)/11\) has dimension \(1\). Moreover \(\#E(\mathbb F_{11})=16\), so \(E(\mathbb Q_{11})[11]=0\).

## Independent modular symbols

The accompanying pure-Python program builds the 390 formal \(\Gamma_0(389)\) Manin-edge variables, imposes the S/R relations, the plus involution, and the exact T_2 relation \(a_2=-2\) at 1307 rational cusps. Its coefficient matrix over \(\mathbb F_{11}\) has rank 389, so its nullspace is 1-dimensional. We normalize the resulting line using the independently Sage/eclib-verified Néron modular-symbol value \(m^+(7/389)=-1\), then separately check \(m^+(5/389)=-2\). All imposed relations are checked again after solving, as are T_3,T_5,T_7 equations at further rational cusps.

For \(q_1,q_2\), primitive roots are \(g_1=5\), \(g_2=6\). The program evaluates the genuine Kurihara sum, with the convention from Kim §1.4,

\[
\widetilde\delta_n=\sum_{a\in(\mathbb Z/n)^{\times}}m^+(a/n)\,\log_{g_1}(a\bmod q_1)\,\log_{g_2}(a\bmod q_2)\pmod{11}.
\]

Independent half-symmetry and unpaired full enumeration yield the same value

\[
\boxed{\widetilde\delta_{397\cdot991}\equiv1\pmod{11}.}
\]

Full computation scans 393426 residues, 324000 nonzero-weight terms. As a normalization regression, the same reconstruction at \(p=7\) gives the previously certified \(\widetilde\delta_{113\cdot673}=2\pmod7\).

Independently of symbols, direct elliptic-group arithmetic gives the local Mordell–Weil rows \((1,10)\) and \((1,7)\); their determinant equals \(-3=8\pmod{11}\), a unit.

## Residual representation and local hypotheses

The mod-11 Galois representation is surjective. Indeed, Frobenius at 2 has characteristic polynomial \(X^2+2X+2\), whose discriminant is \(-4\equiv7\pmod{11}\), a nonsquare: the representation is irreducible. At 389, multiplicative reduction with \(v_{389}(\Delta)=1\) gives a nontrivial transvection of order 11 in inertia on \(E[11]\). Dickson's classification of subgroups of \(\mathrm{GL}_2(\mathbb F_{11})\) implies that an irreducible subgroup containing a transvection contains \(\mathrm{SL}_2(\mathbb F_{11})\). The determinant is the full mod-11 cyclotomic character, so the image is all \(\mathrm{GL}_2(\mathbb F_{11})\).

The Manin constant is \(1\) for the optimal curve (LMFDB 389.a1; also the semistable Manin constant theorem). The only Tamagawa factor is \(1\), and the local 11-torsion is zero, as checked above.

## Consequence using Kim's theorem

Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8 gives, once the Kurihara collection is nonzero, \(\operatorname{ord}(\widetilde\delta) = \operatorname{corank}_{\mathbb Z_{11}}\operatorname{Sel}_{11^\infty}\ge\operatorname{rk} E(\mathbb Q)=2\). The nonzero 2-factor witness gives the opposite inequality, hence \(\operatorname{ord}(\widetilde\delta)=2\). Therefore the hypotheses of Kim Theorem 1.10 hold with \(n=397\cdot991\), and

\[
\operatorname{Sel}(\mathbb Q,E[11])\simeq E(\mathbb F_{397})/11\oplus E(\mathbb F_{991})/11\simeq (\mathbb F_{11})^2.
\]

As \(E(\mathbb Q)/11\simeq (\mathbb F_{11})^2\), the Kummer exact sequence implies \(\Sha(E/\mathbb Q)[11]=0\), hence

\[
\boxed{\Sha(E/\mathbb Q)[11^\infty]=0.}
\]

This conclusion is conditional only on the independently reviewable *finite modular-symbol computation* and the applicability of the published theorem, **not** on full BSD or on assuming Sha finiteness.

## References

- C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf (Theorems 1.8, 1.10; §1.4).
- LMFDB curve 389.a1, https://www.lmfdb.org/EllipticCurve/Q/389a1/
- Earlier 389a1 exact cusp unit check: `results/bsd389_single_cusp_global_unit_USER_RUN_PASS_2026-11-01.md` in the connected research repository.
- Earlier p7 independent coefficient: `verification/kurihara_manin_390_fast.py` in the same repository.

## Scope

This identifies one additional prime-primary component of Sha. It does **not** prove full \(\Sha\)-finiteness, all-prime Sha triviality, or the exact complex rank-two BSD leading-term equality. The script has been run inside the assistant's container, not on the user's Ubuntu machine or by an external referee.