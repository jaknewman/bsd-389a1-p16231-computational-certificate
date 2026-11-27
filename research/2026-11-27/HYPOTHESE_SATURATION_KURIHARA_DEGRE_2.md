# BSD 389a1 — Hypothèse de saturation de Kurihara en degré deux

**27 novembre 2026 — nouvelle direction de recherche, non démontrée.**

## 1. Ce que donne déjà le théorème de Castella–Sano (2026)

Pour E: y²+y=x³+x²−2x, N=389 premier, cφ=1. Pour chaque bon p>3 à représentation résiduelle surjective, le théorème B de Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, arXiv:2601.14504, démontre :

    M_infty(p)=v_p(prod_{l|N} c_l)=0,

car c_389=1. Ce résultat couvre bons premiers ordinaires et supersinguliers, puisque N est sans facteur carré. Il en résulte qu'il existe un produit auxiliaire n de *longueur non spécifiée* tel que delta_n est une unité modulo p.

Cette conclusion est plus faible que l'existence d'un témoin à deux facteurs, nécessaire pour démontrer Sha[p∞]=0 dans le cas rang deux.

## 2. Deux notions différentes d'ordre minimal

Écrire I_n le module p-primaire des congruences de Kurihara et omega(n) le nombre de ses facteurs premiers. Poser

    r_p = min{omega(n): delta_n != 0 dans Z_p/I_n},
    d_p = min{omega(n): delta_n != 0 modulo p}.

Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, th. 1.8, démontre corang Sel_{p∞}(E/Q) = r_p, **pas d_p**. Il est possible que r_p=2 et d_p>2 si une delta à deux facteurs est p-divisible mais non nulle modulo p².

La fonctionnelle positive de rang pair impose r_p,d_p pairs; rang MW=2 impose r_p>=2. L'existence de delta unitaire quelque part rend d_p fini (Castella–Sano).

## 3. Hypothèse nouvelle, propre à 389a1 : H2 (saturation immédiate)

Définir les idéaux de Z_p

    J_{p,2j} = (delta_n : omega(n)=2j),
    J_{p,∞} = union_j J_{p,2j}.

Le théorème B et les relations connues impliquent J_{p,∞}=Z_p. Les raffinements de Kurihara assurent la progression des idéaux J_{p,2} ⊆ J_{p,4} ⊆ ... pour les choix standards.

**H2(E=389a1) :** pour chaque bon p>=5 de représentation résiduelle surjective,

    J_{p,2} = J_{p,∞} = Z_p.

Autrement dit, il existe q1,q2 admissibles tels que delta_{q1q2} !=0 mod p. Cette conjecture est **une condition de non-annulation purement explicite**, définie par symboles modulaires, et non une assertion postulant Sha=0. **Cependant**, par Kim elle est arithmétiquement équivalente à la nullité des composantes p-primaires visées; elle ne devient une avancée que lorsqu'on établit un mécanisme *indépendant* donnant la saturation.

**Conséquence conditionnelle prouvée :** si H2 vaut, le premier idéal de Fitting de Selmer pertinent est unitaire au degré 2, la dimension/corang global vaut 2, sa partie finie est nulle. Avec le sous-groupe de Mordell–Weil libre de rang 2, cela entraîne Sha(E/Q)[p∞]=0 sans supposer la finitude préalable de Sha. Les premiers p=2,3,389 demandent un traitement séparé.

## 4. Proposition de preuve : contraction sans perte de primitivité

Le défi n'est plus de trouver des delta non nulles : cela est fait par Castella–Sano. Le défi est d'abaisser le support de 2 à chaque fois *sans perdre la classe unité*.

**Propriété mécanistique à construire (Hcontr)** : pour toute classe dérivée de Kato primitive correspondant à un auxiliaire n de longueur paire >=4, il existe un opérateur canonique de contraction Bockstein à deux facteurs, à coefficients p-entiers, qui produit une combinaison primitive des classes de longueur omega(n)-2, avec un théorème de réciprocité explicite identifiant leur image sous les symboles de Kurihara.

Si Hcontr est vraie, on itère jusqu'à 2, et H2 découle du théorème B de Castella–Sano. Le lieu précis où une nouvelle preuve est exigée : construction des contractions **et preuve de leur primitivité p-adique**. Une identité formelle modulo p sur les seules marges Hecke–Fricke n'y suffit pas.

Cette hypothèse ne peut **pas** être universelle pour toutes les courbes de rang deux : il existe des courbes avec Sha non trivial. La spécificité éventuelle de 389a1 doit apparaître dans l'intégralité de son système dérivé, pas dans une propriété abstraite de toutes les formes modulaires.

## 5. Test falsificateur d'une approximation trop simple

On pourrait conjecturer à tort que delta_{q1q2} est, à unités près, le permanent des coordonnées locales de P,Q :

    delta_{q1q2} = u_{q1}u_{q2}(P_{q1}Q_{q2}+Q_{q1}P_{q2}).

Cette formule est **fausse pour E389a1**. Pour p=7, q1=113, q3=1429, les quotients locaux (lignes cycliques de 7-torsion) ont pour coordonnées respectives (1,3) et (1,4). Le permanent est 1·4+3·1=0 mod7, alors que le certificat antérieur donne delta_{113·1429}=1 mod7. Aucune multiplication par des unités ne transforme 0 en 1.

Le script `verification/bsd389_local_bridge_obstruction.py` recalcule les groupes E(F_q), les points réduits, leurs coordonnées et cet échec. Il faudra donc un *vrai* opérateur dérivé de Kato/Bockstein, pas une simple identification bilinéaire des réductions de Mordell–Weil.

## 6. Nouveaux tests au-delà de p=1999

L'algorithme C++17 indépendant du manifeste a évalué douze nouveaux bons premiers ordinaires p=2003, 2011, 2017, 2027, 2029, 2053, 2063, 2081, 2083, 2087, 2089, 2099. À tous : c0=c1=0 et c2 unité mod p (voir `results/ordinary_2003_2099.log`, SHA-256 c03ad6916ce573693c51ed4efa60a46b24335ffae4eed26f79da48df89c43184). Cela donne douze témoins cyclotomiques supplémentaires, mais aucune preuve uniforme de H2.

## 7. Prochain test décisif, et indépendance de BSD complexe

1. Construire sur un exemple p=5 ou p=7 de longueur 4 un opérateur Bockstein de *contraction de support* qui reproduit une unité à longueur 2, plutôt que de postuler l'unité de longueur 2.
2. Vérifier l'intégralité exacte et la compatibilité avec Kim/Castella–Sano au même niveau, en particulier les orientations et les p-unités.
3. Prouver l'existence d'une contraction primitive pour tout bon p, d'abord en degré 4 vers 2, puis par induction.

Cette démarche, si elle aboutit, ferme **l'arithmétique Sha** aux bons premiers. La formule complexe exacte de BSD reste une comparaison distincte à construire dans une ligne déterminante motivique/archimédienne commune.

## Sources

- Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, 2026 : https://arxiv.org/abs/2601.14504, théorème B.
- Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, th. 1.8 : https://arxiv.org/abs/2203.12159.
- Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, 2024 : https://doi.org/10.2969/jmsj/90699069.