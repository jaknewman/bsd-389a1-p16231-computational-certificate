# BSD complète, 389a1 — audit des hypothèses uniformes en l (2026-10-19)

**Objet :** distinguer une borne uniformément démontrée sur les *exceptions de représentation galoisienne* d'une borne (encore inconnue) sur les *premiers divisant Sha*. Ceci n'est pas une preuve de finitude de Sha.

## 1. Quantificateur global à établir

Soit E: y²+y=x³+x²−2x (conductor N=389, rang 2, non-CM, semi-stable). Pour établir Sha(E/Q)=0, il faut prouver Sha(E/Q)[l]=0 **pour tout nombre premier l**. Un schéma suffisant serait un entier explicite C_E>0 tel que l ∤ C_E entraîne Sha(E/Q)[l]=0, puis éliminer toutes les composantes aux premiers l | C_E. Ce **C_E contrôlant Sha n'est pas construit**.

Un entier qui borne les exceptions de **surjectivité de rho_{E,l}** n'est **pas** un entier qui borne les exceptions de Sha. La surjectivité n'implique pas que Sel_l(E/Q) ait dimension 2. La trivialité de la torsion et une base saturée du groupe E(Q) ne prouvent pas non plus Sha[l]=0.

## 2. Théorème élémentaire : une famille finie de corps imaginaires ne couvre pas tous les premiers décomposés

Soient D_1,...,D_m<0 des discriminants quadratiques fondamentaux et M=ppcm(|D_1|,...,|D_m|). Chacun des caractères quadratiques primitifs chi_{D_i} est impair : chi_{D_i}(-1)=-1. Pour tout premier l≡-1 (mod M), l est premier à M et chi_{D_i}(l)=chi_{D_i}(-1)=-1 pour chaque i. Par Dirichlet, il existe une infinité de tels l. **Donc l est inerte dans chacun des K_i=Q(sqrt(D_i)).** En particulier un argument qui exige « l décomposé dans au moins un K_i » ne peut pas devenir uniforme par un nombre fini de K_i.

Pour K=Q(sqrt(-19)), tout l≡18 (mod 19) est inerte (exemple : l=37). Cela ne contredit aucun résultat de la torsion E^(-19) de rang analytique 1, mais limite sa réutilisation automatique pour tous les l.

Si l'on recourt à une théorie avec hypothèse de décomposition, les corps K_l doivent donc varier avec l, ou il faut utiliser une méthode sans cette hypothèse.

## 3. Audit uniforme disponible pour les représentations résiduelles

L'API officielle SageMath 10.9 pour les courbes sur Q documente :

```python
rho = E.galois_representation()
candidates = rho.non_surjective(A=1000)
```

La sortie est une **liste finie contenant tous les premiers l où rho_{E,l} pourrait ne pas être surjective**. Sage garantit que pour chaque premier l absent, rho_{E,l}:Gal_Q→GL_2(F_l) est surjective. Un premier figurant dans la liste est un *candidat*, pas nécessairement une véritable exception.

**À exécuter sur IONOS** (Sage activé, utiliser `python -u` et non `sage -python`) :

```bash
set -o pipefail
python -u - <<'PY' 2>&1 | tee ~/bsd389_uniform_galois.log
from sage.all import EllipticCurve, ZZ, is_prime
E = EllipticCurve('389a1')
assert E.conductor() == 389 and not E.has_cm()
assert E.conductor().is_squarefree()
rho = E.galois_representation()
S = [ZZ(l) for l in rho.non_surjective(A=1000)]
assert S != [0]
assert all(is_prime(l) for l in S)
print('BSD389_UNIFORM_MODP_EXCEPTION_SUPERSET', S, flush=True)
for l in S:
    print('EXCEPTION_CANDIDATE',l,'IMAGE',rho.is_surjective(l),flush=True)
print('BSD389_UNIFORM_MODP_SURJECTIVE_OUTSIDE_FINITE_SET_PASS',flush=True)
print('BOUNDARY: residual surjectivity for almost all l does not imply Sha[l]=0',flush=True)
PY
echo "EXIT_STATUS=$?"
```

**Status: not yet run.** Do not write S=[] or any other output before it is observed. Even if S=[], all-prime residual surjectivity is not an all-prime Sha bound.

Official Sage source/docs: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/gal_reps.html

## 4. Why nearby theorems do not yet close the gap

- Gross–Zagier–Kolyvagin gives finiteness globally for the rank-one **twist** E^(-19), not for original rank-two E/Q; E/K has analytic/algebraic rank three.
- Chan-Ho Kim (arXiv:2609.15328, 2026) addresses **fixed p** in higher rank via derived Heegner/Kolyvagin classes; the ordinary split-prime hypothesis does not cover all primes for one fixed K. Full statement, independent mathematical review and exact nonvanishing of the required derived classes remain obligations.
- Recent 2026 announcements on "full BSD from *low Selmer corank*" assume corank 0 or 1; our E has known Mordell–Weil rank 2, so at every p its full Selmer corank is **at least 2**, making those criteria inapplicable even if their announced proofs were accepted.
- Numerically L''/2≈Omega*Reg and p=16231 or small-p certificates do not provide a uniform support bound for Sha. A nonzero real regulator is not an integer annihilator of Sha.

## 5. Genuine next mathematical gate

**Derive an actual uniform implication:** for every l outside a finite *computable* set, demonstrate `dim_{F_l} Sel_l(E/Q) = 2` (equivalently Sha(E/Q)[l]=0) using a rigorous higher-rank reciprocity/Euler-system theorem and verifiable certificates for any required derived classes. Until then, global Sha finiteness and exact complex BSD remain **OPEN**.

A realistic intermediate objective is to **uniformly remove representation-image exceptional primes**, via the Sage test above, and then identify precisely which additional Selmer/Euler-system nonvanishing condition must hold for almost every l. This is meaningful progress in controlling theorem hypotheses, not the desired Sha theorem itself.
