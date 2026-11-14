# E389a1: pairwise Kato–Kurihara core-vertex rigidity when Sha[p] is already zero

**2026-11-14. Status:** a proved conditional-on-published-results, **fixed-p** refinement with precise Selmer-structure proof and independently executed authentic modular-symbol tests. This does **not** establish Sha[p]=0 for a new p or the desired all-large-p bound. A genuine Sha[p]=0 hypothesis is essential.

## 1. Exact statement

Let E/Q: y²+y=x³+x²−2x, MW=Z² with saturated basis P=(−1,1), Q=(0,−1), conductor 389, Manin constant 1, Tamagawa product 1.

Fix p≥5 of good reduction, with surjective residual representation on E[p] and **E(Qp)[p]=0**. Let q≠r be good p-Kolyvagin auxiliary primes such that
- q,r≡1 modp and a_q,a_r≡2 modp;
- the local Kummer spaces L_q=E(F_q)/p, L_r=E(F_r)/p are each 1-dimensional (Frob modp nonidentity unipotent);
- the correct auxiliary ideal I_{qr}=I_q+I_r=(p) in Z_p (so the derived Kato class is defined at the simple residual level).

Define A_{qr} over Fp by localizing the saturated MW basis (P,Q) into L_q⊕L_r; det A≠0 is basis independent.

**Theorem (pairwise unit rigidity, assuming Sha[p]=0).** Under the above conditions, if Sha(E/Q)[p]=0, then
$$
\boxed{\widetilde\delta_{qr}(E)\ne0\pmod p
\quad\Longleftrightarrow\quad\det A_{qr}\ne0\pmod p.}\tag{1}
$$

The precise arithmetic prerequisites include the global **Kato Kolyvagin system primitivity** now proved under the good prime, residual image and Manin hypotheses by Castella–Sano Theorem B, equivalently the existence of some degree-unspecified unit Kurihara coefficient via the refined explicit reciprocity law. The theorem is not a new proof of that primitivity.

Sources:
- C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, §§2.4,3.3–3.4, Theorem 2.6, Proposition 2.9, Proposition 3.10, Theorem 3.11, Theorem 1.10, https://arxiv.org/pdf/2203.12159 .
- Mazur–Rubin, *Kolyvagin Systems*, Theorem 4.1.13 and Corollaries 4.5.2/4.5.4, core-vertex rigidity.
- F. Castella–T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B and Theorem 2.1.3 (2026), https://arxiv.org/html/2601.14504 .

## 2. Proof: localization unit ⇒ genuine Kurihara unit

**Step 1 — the pair is a classical strict core vertex.** By the actual Kummer exact sequence and assumption Sha[p]=0,
$$S_p=\mathrm{Sel}(E[p]/Q)=E(Q)/p=\langle P,Q\rangle\simeq F_p^2.$$
When det A_{qr} is a unit, localization λ:S_p→L_q⊕L_r is an isomorphism.

Form the three Selmer groups with ordinary local conditions away from q,r: $S_{\rm strict}$, $S_p$, $S_{\rm relaxed}$, where at q,r the local conditions are 0, finite Kummer and full H¹ respectively. Global Poitou–Tate plus L_q=L_q^\perp and L_r=L_r^\perp gives
$$
S_{\rm relaxed}=S_p,\qquad S_{\rm strict}=\ker\lambda=0.
$$
For the canonical **Mazur–Rubin transverse** local lines $L_q^{\rm tr},L_r^{\rm tr}$, which complement finite Kummer at these nonidentity-unipotent Kolyvagin primes, the *classical n-transverse Selmer* is
$$
S_{\mathrm{cl},n}=\{c\in S_{\rm relaxed}:
c_q\in L_q^{\rm tr},\ c_r\in L_r^{\rm tr}\}=S_{\rm strict}=0.
$$
The p-strict n-transverse group is a subgroup:
$$
S_{0,n}=\mathrm{Sel}_{0,n}(Q,E[p])\subseteq S_{\mathrm{cl},n}=0.
$$

**Step 2 — primitive Kato derivative generates the *actual* core-vertex line.** Kim Theorem 2.6 provides, for I_n=pZ_p,
$$
H(n):=\mathrm{Sel}_{\rm rel,n}(Q,E[p])
\simeq F_p\oplus S_{0,n}\simeq F_p.
$$
Kim Proposition 2.9 and Mazur–Rubin core-vertex rigidity show that any **primitive modp canonical Kolyvagin system** κ has κ_n generate the entire H(n) when S_{0,n}=0. The Kato system is primitive by the genuine published Castella–Sano Theorem B plus Kim's explicit reciprocity; so
$$
\boxed{\kappa^{\rm Kato}_{qr}\in H(n)\setminus\{0\}.}
$$
This step uses *global* primitivity, not just the two rational MW points or the Hecke Smith determinant 2.

**Step 3 — the p-singular localization is an isomorphism.** Poitou–Tate with the p-relaxed and p-classical n-transverse structures (Kim equation (5.1), second sequence) shows that the cokernel of
$$
\operatorname{loc}_p^s:H(n)\to H^1(\mathbb Q_p,E[p])/H^1_f(\mathbb Q_p,E[p])
$$
has Pontryagin dual embedded as a quotient of S_{\rm cl,n}/S_{0,n}. Both groups vanish from Step 1, so the map is surjective. Since H(n) is one-dimensional, and E(Q_p)[p]=0 implies H²(Q_p,T)[p]=0 in Kim equation (3.2), the singular local quotient is **also one-dimensional**. The map is therefore an isomorphism; the nonzero Kato class has nonzero singular localization.

**Step 4 — the integral reciprocity law sees this singular generator.** Kim Proposition 3.10 and §3.3–3.4 identify the extended dual exponential on the local singular quotient with a map onto Z_p/I_n=Fp, and for good nonanomalous p the scalar local correction \#E(Q_p)[p^\infty] equals 1. Kim Theorem 3.11 / Castella–Sano Theorem 2.1.3 give
$$
\exp^*_{\omega_E}(\mathrm{loc}_p^s\kappa^{\rm Kato}_{qr})
=u_n\widetilde\delta_{qr}\qquad
\text{in }F_p,\quad u_n\in F_p^\times.
$$
The left side is nonzero, hence δ̃_{qr} is a modp unit. This proves the forward direction.

**Step 5 — δ unit ⇒ local determinant unit.** If δ̃_{qr} is a unit at a degree-two conductor, Kim 1.8 gives Sel_{p∞} corank2, and (using Castella–Sano B or the unit directly) Sha[p∞]=0. The minimal Kurihara degree is exactly2 by the MW rank2 lower bound. Kim 1.10 then gives a semilocal isomorphism S_p→L_q⊕L_r. Since S_p=MW/p, det A_{qr} is nonzero. This direction is already a consequence of published semilocal theorems, and could drop the initial Sha[p]=0 assumption entirely.

**Verdict:** under the explicit nonanomalous and simple residual q,r gates, the *zero/nonzero loci* of local MW determinant and full two-factor Kurihara coefficient coincide **once the actual p-Sha has been killed**. Their *values* are NOT asserted proportional by a universal constant. The equality does NOT provide a new uniform p-Sha annihilator because the hypothesis Sha[p]=0 is the original missing all-large-p statement.

## 3. Exact real arithmetic regression (assistant execution)

A companion standalone Python3 script [here](../verification/bsd389_pairwise_kurihara_core_vertex_regression.py) was executed on 2026-11-14 with no Sage dependency. It directly recomputes all E(F_q) traces and MW q-local rows, and every plus-modular-symbol contribution to eight authentic E389a1 Kurihara sums. Its 390-entry integral Manin source is copied **byte for byte** from the earlier authenticated research branch; normalization is independently spot-tested by m_plus(7/389)=−1 and m_plus(5/389)=−2. For genuine original eclib independent source comparisons, see the archived prior p5/p7 user-run certificates; pure Python is not a brand-new full independent Néron-period proof.

| p | (q,r) | det local MW modp | δ̃(qr) modp | result |
|---|---|---:|---:|---|
| 5 | (41,61) | 2 | 4 | unit/unit |
| 5 | (41,131) | 1 | 1 | unit/unit |
| 5 | (41,211) | 1 | 2 | unit/unit |
| 5 | (41,1321) | 0 | 0 | zero/zero |
| 7 | (113,673) | 3 | 2 | unit/unit |
| 7 | (113,1429) | 1 | 1 | unit/unit |
| 7 | (113,2423) | 1 | 6 | unit/unit |
| 7 | (113,7589) | 0 | 0 | zero/zero |

The p7 pair (113,281) also has δ=0, but is *not eligible for this theorem* because its q=281 Frobenius is scalar and the local Kummer space dimension is 2; it remains an independent adversarial example in PR#19.

The local Kummer determinant rows depend on the arbitrary choice of generators of the order-p local group, and Kurihara residues on local primitive roots. The zero/nonzero status is canonical under the necessary unit changes.

The exact program's assistant-container SHA256 was c179de9024c6a8c37f8f630ba623539134f5d2fa4132a90f74897c5f7c47d277 for the *standalone* embedding; the copy committed alongside the JSON-based 390-vector has the same algorithm and regression, not necessarily the same bitwise hash. We do NOT claim actual Ubuntu user execution or original Sage replay in this turn.

## 4. Application to the 5004 already certified primes (finite-range, not uniform)

The 5004 good p≥5 below 48859 covered by Stein–Wuthrich 2013 and the independent p107 certificate satisfy Sha[p]=0. For every one of these with E(Qp)[p]=0 and for every pair q,r meeting the theorem's local 1D and I_{qr}=p conditions, *local MW determinant unit is a sufficient and necessary criterion for a genuine Kurihara modp unit*. This converts a Kurihara **sum** into a much faster **local point and determinant test**, but **only after Sha[p]=0 was certified independently**.

In particular our previously established p5,p7,p11 explicit units and the newly tested auxiliary pairs fit this pattern. No effective global cutoff beyond 48859 and no complex BSD leading coefficient identity is supplied.

## 5. The missing uniform all-p gate

To deduce the user's desired \(\mu_p\le3\) outside a finite set **without assuming Sha[p]=0**, one needs to prove that the strict transverse Selmer group at some MW-detecting pair is zero (equivalently Sha[p]=0) or construct an independent global integral comparison controlling it. The theorem above is a *conditional arithmetic rigidity refinement* of this goal, not a circular proof pretending to establish it.

Neither the universally primitive MW wedge P∧Q, fixed Hecke Smith minor 2, primitive Kato KS at unspecified auxiliary degree, nor Chebotarev MW local rows alone prove strict Selmer vanishing. The independent all-large-p determinant morphism has not been constructed.

**Final status: fixed-p pairwise correspondence proved under stated gates; all-large-p μ≤3, global Sha finiteness, and exact complex BSD remain open.**
