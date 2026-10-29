# 389a1 — Chebotarev–Kummer à deux directions (29 octobre 2026)

## Domaine et résultat

Soit

\[
E/\mathbb Q:\ y^2+y=x^3+x^2-2x,
\quad P=(0,0),\quad Q=(1,0).
\]

Ces points forment une base de \(E(\mathbb Q)\), qui est libre de rang 2 (tables de Cremona). Le certificat précédent `rho.non_surjective(A=1000)==[]`, interprété avec la spécification démontrée de Sage, établit pour notre courbe la surjectivité de \(\rho_{E,p}\) pour tout premier \(p\).

**Théorème (sous cette entrée galoisienne déjà certifiée).** Pour chaque premier \(p\ge5\), il existe deux ensembles disjoints de premiers de bonne réduction \(\mathcal Q_P(p)\) et \(\mathcal Q_Q(p)\), chacun de densité naturelle exacte \(1/p^3\), tels que pour tout \(q\in\mathcal Q_P(p)\) :

- \(q\equiv1\pmod p\), \(a_q(E)\equiv2\pmod p\);
- \(E(\mathbb F_q)/pE(\mathbb F_q)\) est de dimension 1;
- l'image de \(P\) dans ce quotient est non nulle, celle de \(Q\) est nulle.

Pour \(q\in\mathcal Q_Q(p)\), les deux dernières conditions sont inversées. Par conséquent, pour tous \(q_P\in\mathcal Q_P(p)\) et \(q_Q\in\mathcal Q_Q(p)\), la réduction de Mordell–Weil induit un isomorphisme

\[
E(\mathbb Q)/pE(\mathbb Q)\xrightarrow{\sim}
 E(\mathbb F_{q_P})/p\oplus E(\mathbb F_{q_Q})/p.
\]

**Ce n'est pas une assertion sur tout le groupe de Selmer.** Elle ne donne pas directement \(\Sha(E/\mathbb Q)[p]=0\), ni la non-annulation de \(\widetilde\delta_{q_Pq_Q}\).

## Preuve galoisienne

Fixons \(p\ge5\). Posons \(V=E[p]\cong\mathbb F_p^2\), \(L=\mathbb Q(E[p])\), et choisissons des divisions \(pR_P=P\), \(pR_Q=Q\). La représentation affine de Kummer sur
\(M=L(R_P,R_Q)\) prend ses valeurs dans \(V^2\rtimes\operatorname{GL}_2(\mathbb F_p)\).

Par hypothèse, la projection vers \(\operatorname{GL}_2(\mathbb F_p)\) est surjective. Soit \(H=\operatorname{Gal}(M/L)\subseteq V^2\). Il est stable sous l'action diagonale de \(\operatorname{GL}_2(\mathbb F_p)\).

Le module naturel \(V\) est simple et \(\operatorname{End}_{\operatorname{GL}_2}(V)=\mathbb F_p\). Si \(H\ne V^2\), la semi-simplicité du module \(V\oplus V\) permet de trouver \((a,b)\ne(0,0)\) dans \(\mathbb F_p^2\) tel que la projection linéaire \((v,w)\mapsto av+bw\) annule \(H\). Alors la classe de Kummer de \(aP+bQ\) s'annule après restriction à \(G_L\). Mais \(H^1(\operatorname{GL}_2(\mathbb F_p),V)=0\) par le lemme de Sah (élément central \(-I\), avec \(-2\) inversible). L'inflation–restriction rend cette restriction injective : donc \(aP+bQ\in pE(\mathbb Q)\), contradiction avec le fait que \(P,Q\) forment une base. Ainsi \(H=V^2\), et l'image affine entière est le produit semi-direct \(V^2\rtimes\operatorname{GL}_2(\mathbb F_p)\).

Considérons le Frobenius matriciel \(U=\begin{pmatrix}1&1\\0&1\end{pmatrix}\), non trivialement unipotent. Sa classe de conjugaison compte \(p^2-1\) matrices. Pour chacune, \(\operatorname{Im}(U-I)\) a \(p\) éléments, et le quotient \(V/(U-I)V\) a dimension 1. Les classes de Kummer de \(P,Q\) localisées à \(q\) sont respectivement les classes des deux vecteurs de translation \(v_P,v_Q\) dans ce quotient. Chebotarev garantit toutes les classes affines de Frobenius correspondant aux conditions non-nullité/nullité ci-dessus.

Dans chaque fibre affine au-dessus de \(U\), la proportion de \(v_P\notin\operatorname{Im}(U-I)\) et \(v_Q\in\operatorname{Im}(U-I)\) vaut
\[
\frac{(p^2-p)p}{p^4}=\frac{p-1}{p^2}.
\]

Or \(|\operatorname{GL}_2(\mathbb F_p)|=p(p-1)^2(p+1)\), si bien que la densité des deux types est exactement
\[
\frac{p^2-1}{p(p-1)^2(p+1)}\cdot\frac{p-1}{p^2}
=\boxed{\frac1{p^3}}.
\]

La trace et le déterminant de \(U\) valent \(2\) et \(1\), ce qui assure \(a_q\equiv2\) et \(q\equiv1\pmod p\). Sa partie fixe \(V^U\) a dimension 1, donc les deux groupes locaux quotients ont dimension 1. Une ligne locale sélectionne la classe de \(P\), l'autre celle de \(Q\) : la matrice est diagonale non singulière après choix de bases locales. **CQFD.**

## Vérification arithmétique indépendante de Kurihara

Pour le couple \(p=107\), \(q_1=369793\), \(q_2=383917\), le programme `bsd389_p107_local_kummer_determinant.py` calcule **tous** les cardinaux par des sommes de symboles de Legendre, sans Sage, et applique la loi de groupe exacte sur le modèle général de Weierstrass :

| q | #E(F_q) | [#E(F_q)/107]P | [#E(F_q)/107]Q | coordonnées relatives |
|---|---:|---|---|---|
| 369793 | 369792 = 107×3456 | (254307,70688) | (11836,301059) | (1,58) |
| 383917 | 384772 = 107×3596 | (334889,236306) | (153546,353110) | (1,3) |

Les deux points de la colonne P ont ordre 107. La matrice des réductions vaut
\(\begin{pmatrix}1&58\\1&3\end{pmatrix}\), de déterminant \(-55=52\bmod107\).

**Régression additionnelle \(p=11\)** : aux premiers \(397\) et \(991\), les mêmes calculs donnent les lignes \((1,2)\), \((1,4)\), donc le déterminant \(2\bmod11\).

## Critère de localisation du Selmer : équivalence exacte

Pour l'un des couples \((q_P,q_Q)\) précédents, considérons la localisation canonique du \(p\)-Selmer :
\[
\mathrm{loc}_{q_P,q_Q}:\operatorname{Sel}_p(E/\mathbb Q)
\longrightarrow E(\mathbb F_{q_P})/p\oplus E(\mathbb F_{q_Q})/p.
\]
Les deux termes du but sont de dimension \(1\), et la restriction de cette flèche au sous-espace de Kummer \(E(\mathbb Q)/p\) est un isomorphisme par le théorème de Chebotarev–Kummer. La suite exacte \(0	o E(\mathbb Q)/p	o\operatorname{Sel}_p	o\Sha[p]	o0\) implique donc l'équivalence **inconditionnelle** :
\[
oxed{\mathrm{loc}_{q_P,q_Q}\ 	ext{est injective}\quad\Longleftrightarrow\quad\Sha(E/\mathbb Q)[p]=0.}
\]
Si l'injectivité est prouvée, alors \(\Sha[p^\infty]=0\) également. Le théorème ne prouve **pas** cette injectivité ; il construit des couples pour lesquels l'injectivité est équivalente à l'objectif recherché. Cette séparation est essentielle pour éviter un raisonnement circulaire.

## Frontière rigoureuse pour la conjecture BSD

Une matrice MW locale de rang maximal ne dit rien à elle seule sur une hypothétique *classe Selmer supplémentaire* qui se localise dans les mêmes groupes. Le théorème 1.10 de Chan-Ho Kim donne précisément un **isomorphisme du Selmer entier** à la somme locale lorsque le nombre de Kurihara à deux facteurs est non nul et les autres hypothèses sont satisfaites. Cela fait de la matrice ci-dessus une vérification indépendante indispensable mais non suffisante de ce théorème. Le programme existant a déjà certifié le témoin de Kurihara \(\widetilde\delta_{q_1q_2}=34\bmod107\) via ses archives ; ce fichier ne le recalcule pas.

Pour un \(p\) quelconque, la non-annulation d'un **témoin à deux facteurs** ne découle pas du seul groupe de Galois de Kummer, de la surjectivité résiduelle, ni de Chebotarev. La généraliser uniformément exigerait un contrôle du quotient de Selmer global. Le résultat de Kim « non-annulation de *quelque* \(\widetilde\delta_n\) » pour tous les premiers ordinaires (via l'IMC) est plus faible : le nombre de facteurs de ce \(n\) peut dépasser 2.

## Références

- Table de Cremona : https://www.wstein.org/Tables/cremona/INDEX.html
- Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, théorèmes 1.8 et 1.10 et conjecture 1.7 : https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Théorie de Kummer pour les courbes elliptiques (exposition) : https://link.springer.com/article/10.1007/s40574-024-00427-6
- État antérieur de la représentation résiduelle de 389a1 : `results/all_prime_galois_surjectivity_uniform_H1_vanishing_PASS_2026-10-19.md`