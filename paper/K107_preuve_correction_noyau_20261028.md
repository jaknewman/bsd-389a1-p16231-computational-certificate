# K107 — Preuve de correction arithmétique du noyau natif (version auditée)

**Date :** 28 octobre 2026. **Courbe :** \(E:y^2+y=x^3+x^2-2x\), \(N=389\). **Paramètres :** \(p=107\), \(q_1=369793\), \(q_2=383917\), \(n=141969819181\). **Source audité :** `verification/kurihara_k107_native.cpp` (empreinte de l'exécutable de production distincte de la source). **Portée :** preuve de correction du modèle d'algorithme décrit par le code examiné, avec obligations de confiance détaillées ci-dessous. Ne constitue pas une vérification formelle machine du binaire, ni une preuve indépendante de l'intégralité de la somme.

## Lemme 1 — Chemins de fractions continues et orientation

Pour \(0<a<n/2\) avec \(\gcd(a,n)=1\), écrivons les convergents de \(a/n=[0;b_1,\ldots,b_k]\) comme \(r_0=0/1,r_1=u_1/v_1,\ldots,r_k=a/n\). Avec \(r_{-1}=1/0\), les relations de continuants \(u_j=b_j u_{j-1}+u_{j-2}\), \(v_j=b_j v_{j-1}+v_{j-2}\) impliquent \(u_{j-1}v_j-u_j v_{j-1}\in\{+1,-1\}\), alternativement. L'identité de chemins est :

\[
\{\infty,a/n\}=\{\infty,0\}+\sum_{j=1}^{k}\{r_{j-1},r_j\}.
\]

Pour l'arête \(r_{j-1}=u/v\to r_j=w/z\), si \(uz-wv=+1\), la matrice de colonnes \((u,v)^T,(w,z)^T\) a déterminant 1 et ligne inférieure \((v,z)\) ; la contribution est \(+M_{[v:z]}\). Si \(uz-wv=-1\), l'inversion des colonnes donne \(SL_2(\mathbb Z)\), ligne inférieure \((z,v)\), et contribution \(-M_{[z:v]}\).

Dans le code : `pn,pd=1,0`, `ln,ld=0,1`, `x=n,y=a`, `sign=-1`, puis la boucle Euclide produit le premier convergent non nul et alterne `sign`. Le branchement `sign==1?ld:nd` pour `c`, et `sign==1?nd:ld` pour `d`, est précisément la règle précédente. L'arête initiale \(\infty\to0\) est `M[389]`.

**Hypothèse de convention nécessaire :** `M[[c:d]]` est le symbole de l'arête orientée \(\gamma\infty\to\gamma0\) pour une matrice \(\gamma\in SL_2(\mathbb Z)\) de ligne inférieure \((c,d)\). L'invariance \(\Gamma_0(389)\) et les relations de Manin identifient ce symbole à une valeur dépendant seulement de la classe projective. Sa vérification mathématique ne dépend pas du test statistique ; le contrôle Sage des 390 entrées confronte son implémentation.

## Lemme 2 — Indices projectifs et réduction modulo p

Puisque \(N=389\) est premier, toute paire \((c,d)\not\equiv(0,0)\pmod N\) représente une classe de \(\mathbb P^1(\mathbb F_N)\). Dans notre indexation, si \(c\not\equiv0\), cette classe a l'indice \(t=d c^{-1}\pmod{389}\), compris entre 0 et 388 ; si \(c\equiv0\), l'indice vaut 389. Les lignes inférieures des matrices unimodulaires sont primitives, donc jamais simultanément nulles modulo 389. `inv[c]` est bien l'inverse de tout \(c\in\{1,\ldots,388\}\), grâce à la double boucle qui le recherche. Ainsi `idx` est toujours entre 0 et 389. L'indexation `tab[0..388],tab[389]` correspond à l'exporteur de production ; les 390 valeurs ont été recalculées avec Sage indépendant.

Chaque racine primitive \(g_i\) est testée par les facteurs premiers de \(q_i-1\) ; `T[g_i^k mod q_i] = k mod 107`. Comme \(107\mid(q_i-1)\), cette table induit bien le logarithme discret modulo 107. Le produit des deux valeurs est réduit modulo 107. Tous les \(a\) multiples de \(q_1\) ou \(q_2\) sont omis, correspondant exactement à \((a,n)=1\).

## Lemme 3 — Invariant du vecteur W et de la contraction

Pour une plage entière \(I=[A,B]\subseteq[1,(n-1)/2]\), définir \(w(a)=\log_{q_1}(a)\log_{q_2}(a)\bmod 107\) pour les unités. A chaque arête orientée associée à la classe \(s\), le code ajoute \(\pm w(a)\) dans `W[s]`, en stockant les signes négatifs comme \(107-w(a)\). Après traitement des premiers \(t\) numérateurs, l'invariant est

\[
W_s\equiv\sum_{\substack{a\in I\text{ déjà parcourus}\\(a,n)=1}}w(a)\sum_{e\in\mathrm{path}(a)}\varepsilon(e)\mathbf{1}_{s(e)=s}\pmod{107}.
\]

Simultanément `partial` est la somme des \(w(a)\) multipliés par la valeur télescopique `val` modulo 107. Par distributivité, en sortie `partial = Σ_s (W_s mod 107)M_s mod 107`, ce qui est aussi vérifié par l'assertion du programme. La réunion disjointe des 710 plages démontre l'additivité de la fusion. La symétrie \(a\leftrightarrow n-a\) double cette demi-somme : les symboles **pairs** sont invariants, et \(\log_{q_i}(-1)=0\bmod107\) puisque \((q_i-1)/2\) est divisible par 107.

**Données de la production :** 710 checkpoints couvrent \([1,70984909590]\), demi-somme \(17\bmod107\), résidu final \(34\bmod107\), vecteur W390 `ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0` (SHA-256). Ce sont les résultats des fichiers produits, non recalculés dans cette note.

## Bornes de sûreté arithmétique pour cette instance

- Les quotients euclidiens, convergents et dénominateurs sont des entiers naturels bornés par \(n=141969819181<2^{38}\). Les opérations `quot*ln+pn`, `quot*ld+pd` sont **exactement** des continuants positifs, bornés par \(n\) avant l'affectation ; il n'y a pas de multiplication intermédiaire excédant le résultat positif.
- Le nombre d'itérations euclidiennes est inférieur à 64 : pour autant d'itérations, les plus petits dénominateurs croissent comme Fibonacci ; or \(F_{64}=10610209857723>n\). Cette majoration est volontairement lâche.
- Les poids sont dans \([0,106]\), `wt <= 106`, les produits entiers `L1*L2 <= 11236`, les indices projectifs `d*inv[c] <= 388^2=150544` en `int64_t`.
- Les accumulateurs `W[s]` ne diminuent pas ; à chaque \(a\) il y a au plus 64 arêtes et une arête initiale, chacune apportant au plus 107. Même en prenant tous les \(70984909590\) numérateurs, \(W[s] < 70984909590\cdot65\cdot107 < 5\cdot10^{14}\ll2^{64}\).
- `val` commence au plus à 106 et reçoit au plus 64 fois une valeur de taille 106 avec signe : sa valeur absolue reste inférieure à 7000, donc la somme `partial + wt * imod(val,p)` tient dans un `int` signé 32 bits. La contraction `contracted + (W[i]%p)*M[i]` reste aussi sous 11236 plus le résidu précédent.
- Les champs `q1,q2` et leur produit sont ceux de l'en-tête authentifié par l'empreinte de table, et le binaire a une empreinte enregistrée. **Attention :** le binaire source accepte arbitrairement d'autres paramètres ; les bornes précédentes ne sont démontrées que pour l'instance K107 authentifiée.

## Limites et chaîne de confiance

1. Cette note explicite une preuve par invariants pour le **code source examiné** ; elle ne démontre pas formellement l'équivalence compilateur–binaire, ni l'intégrité d'une machine exécutant la production.
2. Les audits `K107_ALL_390_TABLE_ENTRIES_INDEPENDENT_PASS`, `K107_INDEPENDENT_SAGE_CF_CUSP_PASS 131`, `K107_END_TO_END_DISTRIBUTED_AUDIT_PASS 31`, et les rejeux renforcent la chaîne de confiance, mais ne remplacent pas le raisonnement général ci-dessus.
3. Les entrées de table proviennent de Sage/eclib. La convention des symboles et le facteur de période doivent correspondre à ceux de Kim ; la comparaison `sage` contre `eclib` effectuée sur sept fractions est une corroboration. Une note de théorème définitive doit expliciter les hypothèses de Kim avec référence à la version exacte de l'article, ainsi que le certificat du rang rationnel 2 et du quotient optimal.
4. L'audit de l'archive complète doit comprendre les empreintes du code source et une reconstruction du binaire, afin de figer la provenance.

**Conclusion mesurée :** la décomposition en arêtes et la contraction utilisée dans le code C++ ont une justification algébrique générale et des bornes d'entiers sûres pour K107. La valeur \(34\ne0\pmod{107}\) est appuyée par le calcul exhaustif et les contrôles archivés. Une affirmation inconditionnelle \(\Sha(E/\mathbb Q)[107^\infty]=0\) doit en outre fermer la chaîne de confiance et les hypothèses exactes du théorème de structure.