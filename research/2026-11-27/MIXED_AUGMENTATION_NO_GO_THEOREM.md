# BSD 389a1 — Le noyau multivarié que les normes ne voient pas

**27 novembre 2026. Théorème algébrique démontré; pas une preuve de BSD ni de l'hypothèse de saturation au degré deux.**

## Théorème : noyau entièrement mixte des projections

Soient `p` un nombre premier, `r>=1` et

\[
R_r=\mathbf F_p[C_p^r]\simeq
\mathbf F_p[T_1,\ldots,T_r]/(T_1^p,\ldots,T_r^p),
\quad T_i=\sigma_i-1.
\]

Pour chaque `i`, notons `pi_i` la projection obtenue en posant `T_i=0`. Soient `I=(T_1,...,T_r)` l'idéal d'augmentation et `K=cap_i ker(pi_i)`. Alors

\[
\boxed{ K=(T_1\cdots T_r),\qquad
\dim_{\mathbf F_p} K=(p-1)^r,\qquad
K/IK\simeq\mathbf F_p\cdot[T_1\cdots T_r]. }
\]

**Preuve.** Les monômes `T_1^{e_1}...T_r^{e_r}`, avec `0<=e_i<p`, forment une base de `R_r`. La projection `pi_i` conserve exactement les monômes avec `e_i=0` et annule ceux avec `e_i>=1`. L'intersection des noyaux est donc engendrée par les monômes où *tous* les exposants sont au moins un. C'est l'idéal principal `K=(T_1...T_r)`, de dimension `(p-1)^r`. Modulo `IK`, tous ces monômes disparaissent sauf celui dont les `r` exposants sont exactement 1. CQFD.

Le projecteur linéaire explicite sur l'espace complètement mixte est

\[
D=\prod_{i=1}^r(1-\iota_i\pi_i),
\]

avec `iota_i` l'inclusion des polynômes indépendants de `T_i`. Ainsi `D theta` est la somme des seuls monômes contenant toutes les variables. Cela **ne** fournit pas une contraction: pour calculer `D theta`, il faut déjà connaître la classe complète `theta`, pas seulement ses projections.

## Application aux coefficients de Kurihara

Pour un conducteur auxiliaire sans facteur carré `n=q_1...q_r`, projeter chaque groupe cyclique `Gal(Q(zeta_qi)/Q)` sur son quotient d'ordre `p`, choisir un générateur `sigma_i` et écrire la distribution de Mazur–Tate réduite modulo `p` sous la forme

\[
\Theta_n=\sum_{a\in(\mathbf Z/n)^\times}
 m_E^+(a/n)\prod_{i=1}^r(1+T_i)^{j_{q_i}(a)},
\quad j_{q_i}(a)\in\mathbf F_p.
\]

Pour **la même convention de logarithmes discrets et de normalisation** des symboles, le coefficient de `T_1...T_r` est

\[
\boxed{[T_1\cdots T_r]\Theta_n
=\sum_a m_E^+(a/n)\prod_{i=1}^r j_{q_i}(a)
=\delta_n^{(p)}\pmod p.}
\]

On a également `D Theta_n mod IK = delta_n (T_1...T_r) mod IK`.

**Obstacle strict aux seules relations de projection.** Pour tout `c in F_p`, les deux éléments

\[
\Theta_n \quad\text{et}\quad \Theta_n+c T_1\cdots T_r
\]

ont *toutes* les images `pi_i` identiques, alors que leurs coefficients de Kurihara diffèrent de `c`. Même la connaissance de toutes les projections immédiates ne suffit donc pas à déterminer la composante entièrement mixte. Cette affirmation porte sur des **éléments arbitraires de cette algèbre de groupe à conducteur fixé**; les conditions supplémentaires provenant de classes globales de Kato/Selmer peuvent restreindre les possibilités et ne sont pas écartées par ce théorème.

## Conséquences pour l'hypothèse H2

1. Le calcul universel `P_q(1+Y)=Y² mod p`, valable à un premier de Kolyvagin, garantit un *second jet local inversible* mais ne produit pas un morphisme canonique descendant de `r` à `r-2` facteurs.
2. Les seules normes/projections vers des conducteurs plus petits ne déterminent même pas le coefficient mixte d'ordre `r`. Une formule de contraction basée uniquement sur elles est donc insuffisante.
3. L'élément arithmétique supplémentaire requis doit *relier* la partie mixte à des données Selmer : cartes localement finies-singulières, Bockstein du complexe parfait, compatibilité des classes dérivées de Kato et contrôle de primitivité. L'existence d'une telle opération intégrale et primitive **n'est pas démontrée**.
4. Les exemples exacts `p=5` de quadruplets (`41,61,131,211` et `41,61,131,251`) montrent séparément que le coefficient Kurihara à quatre facteurs ne se déduit pas d'un pfaffien naïf des six coefficients à deux facteurs; voir `QUADRATIC_EULER_EVEN_GAP_AND_FOUR_SUPPORT_OBSTRUCTION.md`.

### Test monomial autonome

`python3 verification/bsd389_mixed_augmentation_kernel_gate.py` vérifie les bases de monômes et les dimensions pour `(p,r)=(5,2),(5,4),(7,4)`; il constitue une vérification combinatoire du théorème, dont la preuve est indépendante de tout calcul.

**Verdict :** on a démontré pourquoi la double annulation du facteur d'Euler et les normes classiques **ne peuvent pas, seules**, fermer la saturation H2. Une *comparaison cohomologique primitive globale* est indispensable; ni H2 ni la finitude de `Sha` à tous les premiers n'en découlent.