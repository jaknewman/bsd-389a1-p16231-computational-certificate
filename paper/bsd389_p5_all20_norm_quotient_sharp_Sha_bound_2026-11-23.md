# E389a1 — Exact norm-quotient lemma and sharper 5-primary Sha bounds in cyclic degree-25 fields

**2026-11-23. Status:** Theorem in module theory; conditional arithmetic application to the genuine-VAL1 all-20 Smith transcript. The underlying modular-symbol files are not yet on GitHub main; this is not an independent verification of them, nor a proof of full BSD.

## Proposition

Let E be 389a1, p=5, K/Q cyclic of degree 25, G=Gal(K/Q), R=Z_5[G], N=sum_{g in G}g. Define X=Sel_{5-infinity}(E/K)^vee and Y=Sha(E/K)[5-infinity]^vee. Assume:

(A) rank E(Q)=2 and Sha(E/Q)[5-infinity]=0.

(B) A **genuine integral Mazur–Tate element** theta belongs to Fitt_{0,R}(X).

(C) The group-ring quotient A=R/(N,theta) is finite with size 5^a and additive exponent at most 5^e.

(D) X needs at most d generators over R.

Then rank E(K)=2, Y is finite, its exponent divides 5^e, and

\[
\boxed{\#Y\leq5^{ad-4}.}
\]

### Proof

Kummer duality gives the exact sequence of R-modules

\[
0\longrightarrow Y\longrightarrow X\longrightarrow
\operatorname{Hom}_{\mathbf Z_5}(E(K)\otimes\mathbf Z_5,\mathbf Z_5)\longrightarrow0.
\]

For the right-hand side the finite Mordell–Weil torsion is discarded, as usual in the p-infinity Kummer exact sequence.

1. Since Fitt_0(X) is contained in Ann(X), theta annihilates X and hence Y. Norm N acts on Sha(E/K) as res_{K/Q} o cor_{K/Q}; its corestriction has image in the zero group Sha(E/Q)[5-infinity], so NY=0. Thus Y is a finitely generated module over the finite ring A. Hence Y is finite and 5^e Y=0.

2. The semisimple algebra Q_5[G] is a product of its trivial and nontrivial simple components. N is 25 on the trivial component and zero on all others. Finiteness of R/(N,theta) implies theta is a unit on every nontrivial component. Since theta X=0, the Q_5[G]-module X tensor Q_5 is supported solely on the trivial component. It follows that E(K) tensor Q_5 is G-trivial. Its G-invariants are E(Q) tensor Q_5 (rational descent), of dimension 2, hence rank E(K)=2.

3. As E(K) has rank 2 with trivial G-action on its free quotient, the Kummer-dual sequence becomes an exact R-sequence

\[
0\longrightarrow Y\longrightarrow X\longrightarrow\mathbf Z_5^2\longrightarrow0
\]

where N acts as 0, N, and 25 on the three terms, respectively. The snake lemma gives not merely a comparison but the exact identities

\[
\boxed{Y=\ker(N:X\to X)},\qquad
\boxed{0\to Y\to X/NX\to(\mathbf Z_5/25)^2\to0}.
\]

In particular \(\#Y=\#(X/NX)/25^2=\#(X/NX)/5^4\).

4. A minimal d-generator surjection R^d -> X descends, using theta X=0, to a surjection (R/(N,theta))^d -> X/NX. Hence \(\#(X/NX)\leq(5^a)^d\) and therefore \(\#Y\leq5^{ad-4}\), as claimed. QED.

**Important logical correction:** Y is a SUBMODULE of X. The claim that at most d generators for X forces at most d for Y is generally false over R. The above snake-lemma proof avoids that mistake completely.

## Conditional numerical consequence of the user-reported all-20 Smith certificates

The transcript for verification/bsd389_p5_val1_all20_true_Sha_exponent_order_bound_gate.py reports exactly these two cases:

| r mod 5 | number of r | nonunit Smith factors for R/(N,theta_r) | a | e | old bound | sharpened bound when d<=3 |
|---|---:|---|---:|---:|---|---|
| 1 or 2 | 10 | 25,25,25,25 | 8 | 2 | 5^24 | **5^20** |
| 3 or 4 | 10 | 5,5,25,25,125,125 | 12 | 3 | 5^36 | **5^32** |

If (A)–(D) are verified for each genuine theta_r, we obtain rank E(K_r)=2, finite Sha(E/K_r)[5-infinity], exponent dividing 25 (respectively 125), and cardinality at most 5^20 (respectively 5^32).

This gives neither Sha(E/K_r)[5-infinity]=0 nor an all-prime control of Sha(E/Q), and does not establish the exact complex BSD leading-term identity.

## Auditing prerequisites

- Verify the **actual group ring** R and the identification of each 24 x 24 integral matrix as multiplication by the *genuine* theta_r on R/(N), not an unrelated auxiliary matrix.
- Check the assumptions of Bullach–Honnor, Theorem 1.4(b) and Hypothesis 1.2: the 5-adic Galois image contains SL_2(Z_5), the alternative K_r contains no zeta_5 (for real cyclic K_r), and the additive-reduction condition. This source proves theta^# in Fitt_0; for semistable E their Remark 1.5(a) controls the involution.
- Certify d_R(X)<=3. A sufficient local criterion is theta in Fitt_0(X) and theta not in m^4, where m=(5,sigma-1) is the maximal ideal of R: a module needing d generators has Fitt_0 contained in m^d. A claimed coefficient c_2 mod 25 or first mod-5 unit degree is not itself a complete verification until the augmentation expansion and its class in m^3/m^4 are checked in the true group ring.
- Retain the established independent base vanishing Sha(E/Q)[5-infinity]=0. Do not rerun the old p=107 archive checks.
- The actual all-20 local script and histogram were not found on GitHub main on 2026-11-23. A pasted PASS line does not replace code/provenance review.

**Reference:** D. Bullach and M. H. L. Honnor, *On the refined Birch–Swinnerton-Dyer type conjectures of Mazur and Tate*, Theorem 1.4(b), Hypothesis 1.2, Remark 1.5(a). https://dominikbullach.github.io/MazurTate.pdf
