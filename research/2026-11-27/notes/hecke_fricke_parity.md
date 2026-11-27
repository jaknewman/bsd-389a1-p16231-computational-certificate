# 389a1 — Sélection uniforme des dérivées de Kurihara par Hecke et Fricke

**Date : 27 novembre 2026. Statut : identité algébrique prouvée, contrôles indépendants exécutés.**

Ce document prouve une annulation **uniforme en p** pour les coefficients de Kurihara associés à un nombre impair de premiers auxiliaires. Il ne démontre **pas** la non-annulation à deux facteurs pour tous les premiers, ni la finitude de la totalité de Sha, ni l'égalité complexe BSD.

## 1. Définitions

On travaille sur la courbe modulaire de signe fonctionnel `w(E)=+1`

\[
E: y^2+y=x^3+x^2-2x,\quad N=389.
\]

Le symbole modulaire `m(a/n)=m_E^+(a/n)` est le symbole plus dans la normalisation entière du dépôt, égal à la normalisation de Néron certifiée par les ancres `m(7/389)=-1`, `m(5/389)=-2`. On prend un premier `p>=5` et des premiers distincts `q_1,...,q_r`, tous premiers à `pN`, tels que

\[
q_i\equiv1\pmod p,\quad a_{q_i}(E)\equiv2\pmod p.
\]

Posons `n=product(q_i)` et choisissons une racine primitive `g_i` de `F_{q_i}^×`. Écrivons `j_i(a)` pour le logarithme discret de `a mod q_i` en base `g_i`, réduit modulo p. Définissons

\[
\Theta_n(X_1,\ldots,X_r)
=\sum_{a\in(\mathbb Z/n\mathbb Z)^\times}
 m(a/n)\prod_{i=1}^r X_i^{j_i(a)},
\qquad \widetilde\delta_n=\sum_a m(a/n)\prod_{i=1}^r j_i(a)\bmod p.
\]

Dans la formule de \(\Theta\), un relèvement entier des logarithmes discrets est entendu avant la réduction de la relation cyclique `X_i^(q_i-1)=1`; cette définition est indépendante du choix du relèvement.

## 2. Relation exacte de Hecke pour les marginales

Pour chaque `j`, écrivons `n'=n/q_j` et, pour `i!=j`,
`d_i=j_i(q_j mod q_i)`; posons `U_j=product_{i!=j} X_i^{d_i}`.
La formule de Hecke des symboles modulaires de poids 2 donne **sur les entiers**

\[
\boxed{\Theta_n(X_1,\ldots,X_{j-1},1,X_{j+1},\ldots,X_r)
=(a_{q_j}-U_j-U_j^{-1})\Theta_{n'}.}\tag{H}
\]

**Justification.** Appliquons
\(a_qm(x/n')=m(qx/n')+\sum_{t=0}^{q-1}m((x+tn')/(qn'))\).
Pour `x` inversible modulo `n'`, la somme possède un unique terme dont le numérateur est divisible par q; il devient `m(q^{-1}x/n')`. Les autres termes sont exactement les `q-1` classes de dénominateur `n` et de résidu `x mod n'`. La multiplication par `q` et par `q^{-1}` se traduit respectivement par des décalages opposés des logarithmes discrets. D'où (H).

Pour `r=1`, l'identité à `x/n'=0` donne
\[
\Theta_q(1)=(a_q-2)m(0)\equiv0\pmod p.\tag{H0}
\]

## 3. Théorème sans aucune borne sur r (nombres duaux)

Dans
\[
B_r=\mathbb F_p[T_1,\ldots,T_r]/(T_1^2,\ldots,T_r^2),
\]
la substitution `X_i -> 1+T_i` est un homomorphisme bien défini depuis la réduction du groupe cyclique `X_i^(q_i-1)=1`, car `(1+T_i)^(q_i-1)=1+(q_i-1)T_i=1` dans `B_r`.

**Théorème A (projection entièrement mixte).** Pour `r>=1`,
\[
\boxed{\Theta_n(1+T_1,\ldots,1+T_r)
=\widetilde\delta_n\,T_1\cdots T_r\quad\text{dans }B_r.}\tag{A}
\]

**Preuve.** Au rang `r=1`, (H0) prouve que le coefficient constant est nul, donc la somme est son seul coefficient linéaire `delta_q*T_1`. Supposons (A) au rang `r-1`. En spécialisant `T_j=0` dans (H), le membre droit est `(a_{q_j}-U_j-U_j^{-1}) delta_{n'} product_{i!=j} T_i`. Son premier facteur a un terme constant nul modulo p. Tous ses termes non constants sont annihilés par le produit `product_{i!=j} T_i` dans `B_{r-1}`. Ainsi chaque spécialisation `T_j=0` de `Theta_n` est zéro. Un élément de `B_r` nul dans toutes ces spécialisations est nécessairement un multiple du monôme `T_1...T_r`. L'expansion de `X_i^{j_i(a)}=(1+T_i)^{j_i(a)}=1+j_i(a)T_i` identifie ce multiple à `delta_n`. CQFD.

## 4. Fricke et parité

La relation fonctionnelle des symboles modulaires plus, pour la forme de poids 2 de signe global `w(E)`, est
\[
 m(a/n)=w(E) m(a'/n),\qquad a'aN\equiv-1\pmod n.
\tag{F}
\]
C'est le cas de poids 2 de la formule (2.4) et de la proposition 2.5 de Kazuto Ota, *On the rank-part of the Mazur–Tate refined conjecture for higher weight modular forms*, Ann. Inst. Fourier 73 (2023), p. 1327, <https://aif.centre-mersenne.org/item/10.5802/aif.3557.pdf>.

Soit `ι` l'involution du groupe algébrique induite par `X_i -> X_i^{-1}`. La relation (F) signifie
\[
\Theta_n=w(E)\,[(-N)^{-1}]\cdot\iota(\Theta_n),
\]
avec `[(-N)^{-1}]` l'élément du groupe des unités modulo n. Après projection dans `B_r`, on a `X_i^{-1}=1-T_i`; l'involution multiplie le terme `T_1...T_r` par `(-1)^r`. La multiplication par `[(-N)^{-1}]`, dont le terme constant est 1, laisse inchangé le coefficient supérieur puisque tous les autres termes de la projection (A) sont nuls. Donc
\[
\boxed{\widetilde\delta_n=w(E)(-1)^r\widetilde\delta_n\pmod p.}\tag{P}
\]
Comme p est impair, `delta_n=0` dès que `(-1)^r != w(E)`. En particulier, pour **389a1, w(E)=+1**, on a
\[
\boxed{r\text{ impair}\Longrightarrow\widetilde\delta_n\equiv0\pmod p\quad\text{pour tout }p\ge5.}\tag{P+}
\]
La démonstration n'utilise ni Sha, ni la rationalité du quotient BSD, ni une borne sur le nombre r de facteurs.

## 5. Renforcement de l'ordre d'augmentation pour r<p

Si `1<=r<p`, écrivons `J=(T_1,...,T_r)` dans la réduction du groupe ring. Les relations `(1+T_i)^(q_i-1)-1` n'ont pas de terme de degré inférieur à p modulo p. Les jets jusqu'au degré r sont donc ceux d'une algèbre polynomiale tronquée par `J^(r+1)`.

En partant de (H0), supposons que `Theta_{n'}` soit dans `J_rest^(r-1)`. Pour tout j, l'expression `a_{q_j}-U_j-U_j^{-1}` a **un terme constant et un terme linéaire nuls modulo p**; elle est dans `J_rest^2`. Ainsi la spécialisation `T_j=0` de `Theta_n` appartient à `J_rest^(r+1)`.

Tout monôme de degré <=r manquant au moins une variable est donc nul. Le seul monôme de degré r qui contient toutes les variables est `T_1...T_r`. Par récurrence,
\[
\boxed{\Theta_n\equiv \widetilde\delta_n\prod_{i=1}^r T_i\pmod{p,J^{r+1}},\qquad 1\le r<p.}\tag{J}
\]
Si r est impair, (P+) donne même `Theta_n in J^(r+1)` modulo p. Ce renforcement porte sur le jet **complet** et non seulement sur les exposants 0 ou 1.

## 6. Vérifications exécutées (non utilisées dans les preuves)

1. Table universelle entière : SHA-256 `9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360`. Le certificat existant a passé 1 170 relations exactes de Manin, 1 307 relations Hecke T2 et 2 643 relations T3/T5/T7; unicité rationnelle par rang 389 modulo 7.
2. Contre-vérification de Fricke **sur les entiers** : 40/40 pour n=41, 60/60 pour n=61, 130/130 pour n=131, 2 400/2 400 pour n=2501, 312 000/312 000 pour n=327631, via `bsd389_fricke_exact_certificate.cpp`.
3. Jet cubique entier modulo 5 sur n=41*61*131=327631 : **les 20 coefficients de degré total <=3 sont nuls**, incluant le terme entièrement mixte. Programme `bsd389_higher_mixed_jet_certificate.cpp`.
4. Le calcul Python entièrement indépendant `bsd389_mixed_jet_independent.py` retrouve `delta_(41*61)=4 mod 5` sur 2 400 unités et `delta_(41*61*131)=0 mod 5` sur 312 000 unités.
5. Quatre tests supplémentaires avec `q3=131,211,251,271` donnent tous un coefficient mixte cubique nul et les 19 autres coefficients de degré <=3 nuls.

Les codes et sorties correspondants sont archivés dans le ZIP d'accompagnement. Un résultat d'exécution n'est pas une preuve de l'identification des modèles, mais apporte ici un contrôle indépendant à la preuve théorique (Hecke + Fricke).

## 7. Limite stratégique et prochaine question ciblée

Le théorème élimine **tous les nombres impairs de facteurs** des recherches de certificats non nuls de Kurihara pour 389a1. Il démontre la structure exacte du terme entièrement mixte pour les nombres pairs de facteurs, mais **n'oblige pas le coefficient à être non nul lorsque r=2**.

Le fait que r=2 reste la première possibilité non nulle, combiné à l'équivalence prime par prime de Kim–Castella–Sano déjà documentée dans le dépôt, donne une cible inchangée et parfaitement circonscrite : produire une preuve uniforme de `delta_(q1*q2) != 0` pour tout p suffisamment grand, ou un autre contrôle global intégral des idéaux de Fitting.

Une classe non nulle avec r=4 est compatible avec une obstruction de Selmer non triviale à r=2 : la parité ne permet pas de descendre automatiquement du degré 4 au degré 2. La finitude globale de Sha et l'identité archimédienne BSD restent donc ouvertes.