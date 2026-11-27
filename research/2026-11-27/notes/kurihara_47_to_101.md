# 389a1 — Extension des témoins de Kurihara au-delà de 43

**Date : 26 novembre 2026.** Calculs réellement exécutés dans le conteneur de cette conversation. Les fichiers de vérification accompagnent la présente note. Aucune revendication de BSD complète, de finitude globale de Sha ni de non-annulation uniforme en p.

## 1. Données fixes et reconstruction de Manin

Courbe : `y^2+y=x^3+x^2-2x`, conducteur 389, discriminant minimal +389, rang algébrique 2, base entière `P=(-1,1), Q=(0,-1)`.

Table entière de 390 symboles de Manin : `bsd389_universal_manin_390.txt`, SHA-256 `9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360`.

Le vérificateur entier fourni valide 1 170 relations de Manin, 1 307 relations de Hecke T2, une matrice de relations de rang 389 modulo 7, puis les 2 643 identités de Hecke supplémentaires T3/T5/T7 et les ancres `m(7/389)=-1`, `m(5/389)=-2`. Pour identifier cette table avec le symbole rationnel de Néron, on utilise ces valeurs indépendantes publiées dans le dépôt (Sage/eclib). Pas d'hypothèse BSD.

## 2. Nouveaux témoins explicites

La somme utilisée est celle des symboles modulaires plus, normalisés par la période de Néron :

`delta_(q1*q2) = sum_{1<=a<q1*q2, gcd(a,q1*q2)=1} m^+(a/(q1*q2)) * log_g1(a mod q1) * log_g2(a mod q2) (mod p)`.

| p | q1 | q2 | produit | delta mod p | det local mod p | parcours |
|---:|---:|---:|---:|---:|---:|---|
| 47 | 87421 | 96821 | 8464188641 | **31** | 22 | 4 232 094 320 termes, demi-somme exacte |
| 53 | 17597 | 44203 | 777840191 | **16** | 15 | intégral + demi-somme |
| 59 | 84017 | 109387 | 9190367579 | **10** | 28 | demi-somme exacte |
| 61 | 367 | 1709 | 627203 | **8** | 57 | intégral + demi-somme + second C++ historique |
| 67 | 32831 | 54941 | 1803767971 | **51** | 17 | intégral + demi-somme |
| 71 | 10651 | 81083 | 863615033 | **46** | 5 | intégral + demi-somme |
| 73 | 16937 | 169069 | 2863521653 | **44** | 11 | intégral + demi-somme |
| 79 | 22279 | 32233 | 718119007 | **28** | 31 | intégral + demi-somme |
| 83 | 16103 | 17597 | 283364491 | **15** | 18 | intégral + demi-somme |
| 101 | 15959 | 36563 | 583508917 | **92** | 30 | intégral + demi-somme |

Toutes les valeurs ont été obtenues par le moteur C++ `bsd389_kurihara_fast_parallel.cpp`. Les calculs intégral et par symétrie concordent pour 53,61,67,71,73,79,83,101. Pour 47 et 59, le contrôle intégral sur tous les résidus n'a pas été exécuté, mais l'identité de symétrie est algébrique et le moteur a subi des régressions croisées aux premiers 43 et 61. Les anciens et nouveaux certificats couvrent maintenant tous les premiers de 5 à 83, et aussi 101 (ancien certificat séparé à 107).

### Justification exacte de la demi-somme

Pour `n=q1*q2` impair et les deux symboles plus, `m^+(a/n)=m^+((n-a)/n)`. Pour des premiers admissibles, `p | q_i-1`, et puisque p est impair, `p | (q_i-1)/2`. Les logarithmes discrets satisfont `j_i(-a)=j_i(a)+(q_i-1)/2=j_i(a)` modulo p. Les termes `a` et `n-a` ont donc exactement le même poids modulo p, et aucun point fixe n'existe dans `1<=a<n`. La somme complète modulo p vaut exactement le double de la somme sur `1<=a<=(n-1)/2`.

### Gains de performance

L'ancienne version réduisait le symbole de Manin modulo p à chaque arête de fraction continue. Le nouveau moteur utilise le vecteur ENTIER, somme de petites valeurs signées, puis réalise une réduction mod p seulement après regroupement. Les fils de calcul utilisent des accumulateurs distincts. La complexité demeure O(q1*q2 log(q1*q2)) : ceci est une optimisation numérique, **pas** une preuve uniforme de non-annulation.

## 3. Hypothèses de Kim et portée

La déduction du témoin non nul à `Sha(E/Q)[p^infty]=0` repose sur Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, théorèmes 1.8 et 1.10, en les appliquant avec rang MW=2. Pour chaque p ci-dessus, le script de contrôle arithmétique exécute :

- primalité et admissibilité de q1,q2, `q_i ≡1 (mod p)` et `a_q ≡2 (mod p)`;
- `v_p(#E(F_qi))=1` (donc une ligne p-locale), indépendance des images P,Q (`det local !=0`);
- `p` ne divise pas `#E(F_p)`, donc `E(Q_p)[p]=0` en bonne réduction pour p impair;
- un Frobenius de polynôme caractéristique irréductible modulo p. À cela s'ajoutent la transvection d'inertie au mauvais premier 389, avec `v_389(Delta_min)=1`, et le déterminant cyclotomique surjectif; cela certifie l'image résiduelle GL2(F_p) par la classification des sous-groupes (p>=47);
- la constante de Manin optimale égale à 1 et les Tamagawa égaux à 1, donnés dans la documentation de la courbe.

La non-annulation d'un témoin à deux facteurs donne `ord(delta)<=2`; le rang de MW et le théorème 1.8 donnent `ord(delta)>=2`. Le théorème 1.10 identifie alors Sel(E[p]) aux deux lignes locales (dimension 2), et la suite exacte de Kummer donne `Sha(E/Q)[p]=0`, donc `Sha(E/Q)[p^infty]=0`.

Cette conséquence arithmétique est **conditionnée à l'identification précise de la somme calculée avec la normalisation (1) du théorème de Kim et à l'exactitude des programmes**. Une reproduction externe indépendante et une relecture du code restent souhaitables avant une revendication de certificat public.

## 4. Reproduction

Depuis le répertoire contenant les fichiers :

```sh
python3 bsd389_universal_manin_exact_certificate.py --table bsd389_universal_manin_390.txt
c++ -O3 -std=c++17 -pthread bsd389_kurihara_fast_parallel.cpp -o bsd389_kurihara_fast_parallel
python3 bsd389_extension_2026_11_26_audit.py --output bsd389_extension_audit.json
python3 bsd389_extension_2026_11_26_audit.py --compute --primes 61 83 --output bsd389_extension_recomputed_61_83.json
# Calcul long de p=47 :
python3 bsd389_extension_2026_11_26_audit.py --compute --primes 47 --output bsd389_extension_recomputed_47.json
```

Le mode `--compute` du script **exécute vraiment** les sommes et compare les résidus; sans `--compute`, il ne vérifie que les entrées arithmétiques et la cohérence des paramètres, et ne prétend pas refaire les sommes.

## 5. Ce que cette généralisation ne démontre pas

Malgré l'existence de nombreux témoins pour des premiers distincts, aucune borne théorique globale ne donne `delta !=0` à deux facteurs pour **chaque** premier p, et la trivialité des composantes déjà certifiées n'assure pas la finitude de l'ensemble des autres premières composantes. Les premiers 2,3,389 exigent des méthodes distinctes. Enfin, la rationalité motivique et l'égalité archimédienne exacte du terme dominant de L restent des questions séparées et non résolues ici. BSD complète n'est pas démontrée.