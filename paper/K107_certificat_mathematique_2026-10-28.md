# Certificat conditionnel de Kurihara — E = 389a1, p = 107

**Date :** 28 octobre 2026. **Statut :** résultat computationnel audité; proposition de théorème conditionnelle à la vérification formelle des calculs et de la convention de normalisation; ne pas présenter comme preuve publiée de BSD.

## Énoncé

Soit E/Q donnée par y²+y=x³+x²−2x, N=389. Posons p=107, q1=369793, q2=383917 et n=141969819181. En adoptant les symboles modulaires pairs normalisés par la période de Néron et les logarithmes discrets associés aux racines primitives 5 et 5, les calculs archivés donnent

δ_n ≡ 34 (mod 107).

**Proposition conditionnelle :** si les entrées de la table eclib représentent exactement les symboles de Kurihara et si l'exécution des boucles du noyau est correctement certifiée, alors Sha(E/Q)[107^∞]=0.

## Hypothèses arithmétiques

- E a conducteur 389, discriminant minimal +389, produit de Tamagawa 1 et torsion rationnelle triviale (sorties Sage).
- Rang rationnel 2 : à rattacher à un certificat de rang établi, non seulement à l'indépendance de deux points.
- p=107 est un bon premier; Sage a retourné `rho.is_surjective(107)=True`.
- Les nombres q1,q2 sont premiers, satisfont q_i≡1 (mod 107) et 107 | #E(F_qi) ; contrôles via comptages exacts.
- E est le quotient optimal de conducteur premier, et 107 ne divise pas la constante de Manin (hypothèse à relier explicitement au théorème de Mazur et à l'identification de la courbe optimale).
- La torsion 107-primaire locale est triviale car #E(F_107)=108.

## Lemme d'arêtes unimodulaires (identité générale)

Pour un symbole de poids 2 et une matrice γ=(a b; c d) dans SL₂(Z), définir

 F(γ) = [γ(0)]⁺ − [γ(∞)]⁺ = [b/d]⁺ − [a/c]⁺,

avec les interprétations habituelles aux pointes. L'invariance du symbole par Γ₀(389) et les translations intégrales montre que F(γ) dépend de la classe projective de (c,d) modulo 389 (avec les conventions de représentants et d'orientation appliquées à la table).

Pour tout 0<a/n<1, soient r₀=0/1, r₁, …, r_k=a/n les convergents de sa fraction continue. Les arêtes successives sont unimodulaires et on a l'identité de télescopage

 [a/n]⁺ = [0]⁺ + Σ_{j=1}^k ([r_j]⁺ − [r_{j−1}]⁺).

La table M contient la contribution de la première arête ∞→0, puis les 389 autres classes; les orientations sont déterminées par le signe des déterminants des convergents. Le noyau C++ doit satisfaire, à chaque itération, l'invariant suivant : les deux couples de convergents consécutifs sont réduits, leur déterminant est ±1, la somme courante est la somme de toutes les arêtes précédentes, et les indices (c,d) de la classe correspondent à la matrice unimodulaire orientée. Cet invariant, joint à la terminaison de l'algorithme d'Euclide, prouve l'identité de calcul **pour tout** a, indépendamment des tests statistiques.

L'audit Sage indépendant reproduit les 390 valeurs de la table et 160 exemples d'invariance d'arêtes, plus 131 fractions testées. Il ne remplace pas à lui seul la preuve que l'implémentation C++ préserve cet invariant pour toutes ses entrées; ce contrôle de code est requis dans un certificat définitif.

## Agrégation et résidu exact

Le noyau ignore les a non inversibles modulo n. Pour chaque unité a, il calcule w(a)=log_{q1}(a)log_{q2}(a) (mod 107), puis la contribution w(a)[a/n]⁺. Par parité, [−a/n]⁺=[a/n]⁺; les deux logarithmes de −1 sont nuls modulo 107 car (q_i−1)/2 est divisible par 107. Ainsi

 δ_n = 2 Σ_{1≤a≤(n−1)/2, gcd(a,n)=1} w(a)[a/n]⁺ (mod 107).

Cette plage contient 70 984 909 590 entiers. Les 710 blocs de taille 100 000 000 (dernier bloc raccourci) couvrent cette plage sans lacune ni recouvrement. Leur fusion donne une demi-somme égale à 17 (mod 107) et donc δ_n=34 (mod 107).

Sorties archivées : `K107_FINAL_PAYLOAD_AND_COVERAGE_PASS 710/710`, `K107_FINAL_DOT_AND_MERGE_PASS HALF 17 DELTA 34`, `K107_REPRODUCIBLE_ARTIFACT_AUDIT_PASS`, et `K107_INDEPENDENT_MANIN_AUDIT_PASS`.

Empreintes SHA-256 :

- Vecteur W390 : `ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0`.
- Table M390 : `00cdb5cd7ad9c7093877836412a77fe3f67985aa2e1878ddd03b8092ab90ee2f`.
- Exécutable natif : `dfe879e69947b51b9762f6c72772ea80c56a8c7dfb8efe3a4823414cfa7e16b4`.
- Archive : `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754`.

## Application conditionnelle du théorème de Kim

D'après Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, théorème 1.8, sous surjectivité résiduelle et constante de Manin première à 107, la non-annulation d'un nombre de Kurihara à deux facteurs implique ρ≤2, où ρ est le plus petit nombre de facteurs d'un témoin non nul. Comme le rang de E(Q) est égal à 2, le corang de Selmer vaut au moins 2; le théorème donne donc ρ=2. De plus, M₂=0 puisque le témoin est non nul modulo 107. La monotonie M₂≥M₄≥…≥0 entraîne M∞=0. La formule de Kim implique que le quotient de Selmer par son sous-groupe divisible maximal est trivial. Étant donné la suite exacte de Kummer et le rang rationnel égal au corang, Sha(E/Q)[107^∞] est fini et s'identifie à ce quotient; il est donc trivial.

**Attention :** le théorème de Castella–Sano (Thm B) n'est pas nécessaire dans cette implication témoin→trivialité; il intervient pour les énoncés d'existence et la réciproque. Éviter de confondre les deux rôles.

## Points restant à fermer avant diffusion comme démonstration

1. Vérifier ligne à ligne le lien entre les indices du tableau C++, les fractions continues et les classes projectives, avec une preuve de correction de l'arithmétique 64 bits et des signes; un petit vérificateur formel serait idéal.
2. Conserver les versions exactes des bibliothèques Sage/eclib et une copie du tableau utilisé; l'égalité eclib/Sage sur sept pointes et le contrôle de 390 entrées renforcent mais ne démontrent pas seuls le bon facteur de période pour toutes les valeurs.
3. Relier la preuve du rang rationnel 2 et le caractère optimal de E à des données certifiées et citables.
4. Vérifier la reproductibilité depuis l'archive sur un environnement frais et documenter précisément la provenance de tous les fichiers.

## Références

- C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, théorème 1.8 : https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- F. Castella et T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, §1.1, théorème B : https://web.math.ucsb.edu/~castella/Kurihara.pdf