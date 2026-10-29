# 389a1 — Un théorème uniforme de réduction Kurihara–Kim

**Date :** 29 octobre 2026. **Statut :** théorème conditionnel *seulement à la non-annulation d'un témoin pour chaque premier*, et lemmes uniformes démontrés par les théorèmes cités. **Ce document ne prétend pas établir la finitude globale de Sha.**

## 1. Les données globales indépendantes de p

Soit E/Q la courbe `y^2+y=x^3+x^2-2*x`, modèle minimal `[0,1,1,-2,0]`. Elle est de conducteur et discriminant minimal +389, de rang rationnel 2, sans torsion rationnelle, de réduction semi-stable, et elle est la courbe X_0(389)-optimale. La constante de Manin est **1**, en vertu du théorème de Česnavičius sur les quotients optimaux semi-stables. Les représentations résiduelles `rho_{E,p}` sont surjectives pour **chaque** premier p, résultat connu pour 389a1 et contrôlé par Sage/LMFDB. Les facteurs de Tamagawa sont tous égaux à 1.

Sources :
- Česnavičius, *The Manin constant in the semistable case*, Compositio Math. 154 (2018), arXiv:1703.02951, https://arxiv.org/abs/1703.02951
- LMFDB, https://www.lmfdb.org/EllipticCurve/Q/389/a/1
- Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, théorème 1.8, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

## 2. Existence uniforme de bons auxiliaires

**Proposition.** Pour chaque premier `p>=5`, l'ensemble des nombres premiers `q` de bonne réduction, tels que le Frobenius sur `E[p]` soit conjugué à `U=[[1,1],[0,1]]`, a une densité naturelle de Dirichlet égale à `1/(p(p-1))`. Il est donc infini. Tout tel q satisfait simultanément

- `q = 1 (mod p)` ;
- `a_q(E) = 2 = q+1 (mod p)` ;
- `dim_{F_p} E(F_q)[p] = 1`.

**Démonstration.** Comme `Gal(Q(E[p])/Q)=GL_2(F_p)`, Chebotarev attribue à la classe de conjugaison de U une densité égale au rapport de sa cardinalité sur `|GL_2(F_p)|`. Le centralisateur de U comprend les matrices `aI+b(U-I)` avec `a∈F_p^×`, `b∈F_p`, et a cardinal `p(p-1)`. La classe contient donc `(p^2-1)` éléments, d'où la densité `1/[p(p-1)]`. Pour un premier de bonne réduction q, le déterminant du Frobenius est `q mod p` et sa trace est `a_q mod p` ; la partie fixe de U a dimension un. CQFD.

La proposition est valable **également quand p est supersingulier**, et ne dépend pas d'un ordre p-adique d'annulation. Il existe pour tout p une infinité de paires distinctes (q1,q2) de tels premiers.

## 3. Critère *uniforme* de trivialité de la composante p-primaire

**Théorème.** Fixons `p>=5`. Soit `n=q1*q2` un produit de deux premiers auxiliaires distincts vérifiant `q_i≡1 (mod p)` et `a_{q_i}(E)≡q_i+1 (mod p)`. Si le **nombre de Kurihara normalisé par la période de Néron** satisfait `\tilde delta_n != 0 (mod p)`, alors

`Sha(E/Q)[p^infinity] = 0`.

**Preuve.** La surjectivité résiduelle et `c_E=1` autorisent l'application du théorème 1.8 de Chan-Ho Kim. Le nombre non nul à deux facteurs montre `ord(\tilde delta) <=2`. Puisque le rang rationnel est 2, la suite de Kummer donne `corank_{Z_p} Sel(Q,E[p^infinity]) >=2`. Le théorème 1.8(1) identifie le corang à `ord(\tilde delta)` : ils valent donc 2. La non-annulation modulo p implique que la valuation minimale `partial^(2)(\tilde delta)=0`; toutes les valuations considérées sont non négatives par intégralité p-adique, donc `partial^(infinity)(\tilde delta)=0`. Le théorème 1.8(3) donne ainsi `length_{Z_p}(Sel/div)=0`. Le Selmer est divisible de corang 2, donc isomorphe à `(Q_p/Z_p)^2`. L'injection de Kummer `E(Q)⊗Q_p/Z_p -> Sel`, entre deux groupes p-divisibles de corang 2, est un isomorphisme (une injection entre deux copies de `(Q_p/Z_p)^2` est inversible). Par exactitude, `Sha(E/Q)[p^infinity]=0`. CQFD.

Ce théorème s'applique à **tous les p>=5 sans exception liée au type de réduction**. Il ne requiert ni `E(Q_p)[p]=0` (condition additionnelle propre au théorème 1.10), ni une fonction L p-adique, ni la finitude préalable de Sha.

## 4. Limite : Chebotarev ne fournit pas la non-annulation de Kurihara

La proposition prouve l'abondance des q admissibles, **pas** la non-annulation de `\tilde delta_{q1*q2}`. L'existence d'un témoin avec exactement deux facteurs pour tous les p assez grands (ou pour tous les p>=5) reste à démontrer ; l'assumer reviendrait, dans ce cadre, à supposer l'obstruction centrale qu'on cherche à lever.

Une collection **finie** de couples fixes ne peut pas suffire pour tous les p : chaque p d'admissibilité doit diviser `gcd(q1-1,q2-1)` pour l'un des couples fixes. Un nombre fini de tels entiers n'a qu'un nombre fini de diviseurs premiers. Ainsi la preuve globale devra exploiter une *famille variant avec p*, ou une comparaison intégrale uniforme (par exemple un véritable entier de Fitting sur les Selmer) qui élimine les p assez grands sans passer par un témoin distinct à chacun.

La non-annulation déjà calculée pour p=5,7,107 est un exemple de la condition suffisante, non une preuve de sa validité pour tous les autres p. Les composants 2 et 3 exigent leurs propres arguments. Même la connaissance de `Sha[p^infinity]=0` pour une très grande liste finie de p n'établit pas, à elle seule, la finitude globale de Sha ou la formule exacte de BSD.