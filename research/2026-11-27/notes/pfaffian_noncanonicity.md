# BSD 389a1 — Audit exact de la stratégie pfaffienne et du jet mixte

Date : 27 novembre 2026. **Statut : preuve algébrique autonome de deux limitations ; aucun nouveau théorème de finitude de Sha.**

## 1. Données reprises du certificat précédent

Pour p=5, dans l'ordre des auxiliaires (41,61,131,251), les valeurs
(delta12,delta13,delta14,delta23,delta24,delta34) sont (4,1,3,2,1,1).
Pour p=7, dans l'ordre (113,673,1429,2423), elles sont (2,1,6,2,3,3).
Ce document prend ces valeurs comme **entrées du certificat antérieur**, et ne refait pas la somme de Kurihara.

## 2. L'antisymétrisation n'est pas intrinsèque

La somme a deux variables delta(q_i,q_j) est symétrique dans l'ordre de ses facteurs, compte tenu d'un choix cohérent des logarithmes discrets. Poser artificiellement D_ij=delta_ij pour i<j et D_ji=-delta_ij n'est pas une opération compatible à toutes les permutations des premiers.

En effet, Pf(D)=delta12 delta34 - delta13 delta24 + delta14 delta23. Si l'on échange les positions 2 et 3, **en réappliquant la règle conventionnelle** de signe aux nouvelles positions, la valeur devient delta13 delta24 - delta12 delta34 + delta14 delta23 ; ce n'est pas, en général, -Pf(D).

- p=5 : Pf=4 et Pf_apres_transposition=3, alors que -Pf=1 modulo 5.
- p=7 : Pf=1 et Pf_apres_transposition=2, alors que -Pf=6 modulo 7.

Conclusion : le pfaffien construit ainsi peut servir à réfuter une factorisation **pour l'ordre fixé**, mais ce n'est pas le pfaffien d'une forme alternée canoniquement définie sur l'ensemble non ordonné des auxiliaires. Il ne justifie pas un nouveau symbole de réciprocité invariant par permutation.

## 3. Un invariant symétrique ne force pas davantage la non-annulation uniforme

Le *hafnien* à quatre points, H=delta12 delta34 + delta13 delta24 + delta14 delta23, est bien invariant par permutation des quatre indices. Sous des renormalisations delta_ij -> u_i u_j delta_ij, il est multiplié par u1 u2 u3 u4. Les données donnent H=1 modulo 5 et H=0 modulo 7. Le hafnien n'est donc pas un remplacement universel du pfaffien non nul.

## 4. Théorème de non-détermination du coefficient mixte par les seules contraintes de bas degré

Soit p impair et B=F_p[T,U]/(T²,U²). Une classe Theta satisfaisant les deux identités marginales Theta(T,0)=0 et Theta(0,U)=0 a la forme unique Theta=c T U pour c∈F_p.

L'involution d'inversion des deux variables se lit T -> (1+T)^(-1)-1 = -T, U -> -U. Son action sur TU est +1. Le signe fonctionnel +1 impose donc Theta(T,U)=Theta(-T,-U), qui est satisfaite pour **tout** c∈F_p.

Ainsi les seules contraintes de Hecke sur les marges et la symétrie de Fricke, à ce degré, autorisent c=0 aussi bien que c=1 : elles ne peuvent pas forcer une unité mixte.

Cela n'affirme pas qu'il existe une forme modulaire globale réelle réalisant n'importe quel c à tous les niveaux. L'énoncé concerne exactement la force logique des contraintes de bas degré, et montre qu'un ingrédient arithmétique supplémentaire est indispensable.

## 5. Reste substantiel

Pour chaque p sous les hypothèses du théorème de Kim, un vrai coefficient de Kurihara a deux facteurs qui soit non nul donne Sha(E/Q)[p∞]=0. Pour conclure à tous les p, il faut une preuve de non-annulation globale à deux facteurs hors d'un ensemble fini, ou un contrôle uniforme indépendant des complexes de Selmer. Ni une table fixe de Manin, ni la parité Hecke–Fricke, ni le pfaffien conventionnel ne démontrent cette existence.

Séparément, la formule BSD complexe requiert une comparaison motivique archimédienne exacte ; elle ne découle pas de ces critères p-adiques.