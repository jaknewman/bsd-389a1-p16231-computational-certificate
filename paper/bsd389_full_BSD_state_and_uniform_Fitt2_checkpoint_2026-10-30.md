# BSD complète pour 389a1 — état exact et prochaine étape

**30 octobre 2026 — BSD complète NON DÉMONTRÉE.** Bilan distinguant résultats classiques, calculs historiques exécutés, implications assistées par ordinateur et obligations théoriques restantes.

## La courbe et la formule

\[
E:y^2+y=x^3+x^2-2x,\quad N=389,\quad \Delta_{\min}=389.
\]

E est semi-stable, de rang de Mordell–Weil 2 avec deux générateurs saturés certifiés dans Sage, torsion rationnelle triviale, produit Tamagawa 1 et signe fonctionnel +1. Le rang analytique est 2 : annulation de L(E,1) via symboles modulaires et L''(E,1) non nul dans la littérature classique. **BSD faible est démontrée pour cette courbe.**

BSD forte demande EN PLUS :
1. \(\Sha(E/\mathbf Q)\) **fini** ;
2. l'**égalité exacte**
\[
\boxed{\frac{L''(E,1)}{2}=\Omega_E\,\operatorname{Reg}(E)\,\#\Sha(E/\mathbf Q).}
\]

Valeurs publiées : \(L''(E,1)=1.51863300057685354046\ldots\), \(\Omega_E\approx4.980425\), \(\operatorname{Reg}(E)\approx0.152460\), donc quotient analytique \(\#\Sha_{\mathrm{an}}\approx1\). **Ce quotient n'est pas un entier prouvé, ni une égalité exacte démontrée.** Même \(\Sha=0\), si cela venait à être démontré, ne prouverait pas à lui seul l'identité réelle \(L''/2=\Omega_E\operatorname{Reg}\).

**Références établies** :
- John Cremona, [Numerical evidence for BSD, diapositive 26](https://people.maths.bris.ac.uk/~matyd/BSD2011/bsd2011-Cremona.pdf) (rang 2, \(L''\), période, régulateur, Sha[2]=0 par 2-descente).
- [Sage Elliptic Curves tutorial — Bounding Sha](https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html) (résultats démontrés des bornes p-primaires pour 5 et 7, mais pas de borne globale pour 389a1).
- [Grigorov–Jorza–Patrikis–Stein–Tarnita-Pătrașcu](https://www.wstein.org/papers/bsdalg/bsdalg2.pdf), §1, BSD et son ordre analytique seulement conjectural.

## État des premiers de Sha

| Premier | Portée prouvée ou certifiée |
|---|---|
| 2 | Sha[2]=0 par 2-descente classique ; donc Sha[2^\infty]=0. |
| 5,7 | Sha[p^\infty]=0 par les résultats p-primary_bound(5)=p-primary_bound(7)=0 documentés dans Sage. |
| 107 | Témoin complet de Kurihara à deux auxiliaires, valeur 34 mod107, 710 blocs archivés et SHA256 confirmé ; l'implication Sha[107^\infty]=0 via Kim dépend de l'authenticité et de la normalisation de cette archive. Calcul cyclotomique indépendant C2=86, coordinate 43. |
| 599 | Authentique tableau Manin 390/390 vérifié ; C2=543, coordinate 571. L'emploi du théorème supersingulier dans la normalisation Reg_p/Reg_gamma attend encore résolution ; ne pas déclarer un résultat primaire inconditionnel. |
| 16231 | Deux calculs complets indépendants J=4486, correction 8335, coefficient dérivé 9534, comparaison régulateur unité ; test Sage V65 PASS. Implication Sha[16231^\infty]=0 encore assujettie à la correspondance des sources/compilateurs et au théorème ; aucune exécution directe complète de la L-série n3 ou p_primary_bound(16231). |
| 3,389 et tous les autres p | Aucune preuve de support fini global de Sha. p389 est le seul de mauvaise réduction. |

Une liste de p-contrôles, même considérable, ne constitue pas une borne uniforme.

## Ce qui EST prouvé uniformément grâce à Mazur et Castella–Sano

Pour tout premier \(p\ge11\), E est semi-stable et la représentation \(E[p]\) est surjective par Mazur (1978, théorème 4), comme cité dans Grigorov et al., Théorème 2.1. Pour \(p\ne389\), la réduction est bonne, le conducteur 389 est sans facteur carré, le Manin constant optimal est p-unité et Tamagawa(E)=1.

[Castella–Sano, Theorem B, prépublication janvier 2026](https://web.math.ucsb.edu/~castella/Kurihara.pdf) entraîne :
\[
\boxed{\mathcal M_\infty(\delta_p)=0
\quad\text{pour TOUS les premiers }p\ge11,\ p\ne389.}
\]
Cela fournit au moins un témoin Kurihara de **degré auxiliaire non borné** à chaque p, **pas** nécessairement à deux auxiliaires, donc ne prouve pas Sha[p]=0.

## Exacte réduction au deuxième idéal de Fitting : Kim

Pour \(p\ge11\), \(p\ne389\), Kim [Theorem 1.8](https://arxiv.org/pdf/2203.12159) et le rang de Mordell–Weil 2 donnent, avec \(m_2(p)\) le minimum des valuations des témoins à EXACTEMENT DEUX premiers auxiliaires :
\[
\boxed{\operatorname{Fitt}_{2,\mathbf Z_p}
  \bigl(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\bigr)
 =p^{m_2(p)}\mathbf Z_p,}
\]
où \(p^\infty\mathbf Z_p=(0)\). En particulier, Sha[p^\infty]=0 si et seulement si cet idéal vaut tout \(\mathbf Z_p\).

**Nouveau contrôle intégral (conséquence de Cassels–Tate / Kim) :** si \(m_2(p)\) est **positif et fini**, il est **pair et au moins 2**. En effet, Kim décompose la partie finie du Selmer en sommes de p-groupes apparaissant par **paires**, tandis que Cassels démontre que la partie p-primaire finie de Sha a un ordre carré. Une future valeur \(m_2(p)=1\) serait donc une alerte contre les conventions ou les calculs.

**Obstacle réellement restant :** construire un unique entier **non nul et indépendant de p** \(C\), avec un ensemble fini explicite S, et démontrer une comparaison **intégrale** assurant
\[
\forall p\notin S:\quad
\operatorname{Fitt}_2(\operatorname{Sel}_{p^\infty}^\vee)
\supseteq C\mathbf Z_p.
\]
Cela annulerait Sha[p^\infty] pour tous les p hors de S et des diviseurs de C, mais ne prouverait toujours pas l'égalité complexe BSD. **Aucune telle comparaison n'a été établie**. La norme exacte 729 du facteur torique chi53 n'est PAS, jusqu'à preuve contraire, un tel entier de Fitting.

## Renforcement inconditionnel découvert après rédaction

La formule du **deuxième idéal de Fitting** elle-même ne nécessite en réalité **aucun théorème d'Iwasawa**, et est vraie pour p arbitraire, même p=2,3,389. En dualisant la suite exacte de Kummer de rang deux, la surjection vers \(\mathbf Z_p^2\) se scinde, donc
\[
\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee
\simeq\mathbf Z_p^2\oplus\Sha(E/\mathbf Q)[p^\infty]^\vee
\]
et
\[
\boxed{\operatorname{Fitt}_2(\operatorname{Sel}_{p^\infty}^\vee)
=\operatorname{Fitt}_0(\Sha[p^\infty]^\vee).}
\]
Cette égalité donne pour chaque p une classification exacte : idéal unité iff \(\Sha[p^\infty]=0\); idéal \((p^e)\) iff \(\Sha[p^\infty]\) est fini, d'ordre \(p^e\); idéal nul iff la composante p-primaire est infinie. Kim est nécessaire uniquement pour exprimer numériquement cet idéal au moyen des nombres de Kurihara pour les p où ses hypothèses sont satisfaites.

[Preuve formelle élémentaire intégrale](bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md). Le passage à une **borne uniforme** exige toujours de construire le déterminant fixe C et l'application de comparaison intégrale absents à ce jour. L'égalité complexe forte de BSD reste une obligation distincte.

---

## Les deux chantiers pour BSD complète

**Chantier arithmétique :** obtenir une vraie borne uniforme sur les premiers de Sha, puis démontrer la finitude et la valeur de toutes les composantes exceptionnelles.

**Chantier analytico-arithmétique :** démontrer le terme dominant complexe **exact** \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha\), avec les facteurs normalisés. Les décimales, les unités modulo différents p et les égalités de valuations p-adiques ne suffisent pas.

**Conclusion : rang BSD établi ; la finitude globale de Sha et l'égalité forte du terme dominant ne sont pas établies.** Ce document n'emploie pas le statut historique de BSD comme argument d'impossibilité : il spécifie les deux étapes logiques à construire et leurs obligations testables.
