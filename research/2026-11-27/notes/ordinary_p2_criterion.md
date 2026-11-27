# BSD 389a1 : critère cyclotomique quadratique exact, balayage des premiers < 2000

**Statut (27 novembre 2026).** Preuve algébrique du critère, calculs finis exécutés, table de Manin entière réutilisée de la session précédente. Ce document ne prouve pas BSD complexe et ne prouve pas que le critère est satisfait à *tous* les premiers.

## 1. Données

La courbe est \(E:y^2+y=x^3+x^2-2x\), de conducteur et discriminant minimal 389, de rang Mordell–Weil certifié 2 et de torsion rationnelle nulle. Le fichier `manin_390.txt` est la table entière de 390 arêtes de Manin du symbole modulaire plus normalisé de Néron ; sa somme de contrôle SHA256 est

`9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360`.

Cette identification repose sur les relations de Manin et Hecke entières, l'unicité rationnelle, et les deux ancres Sage/eclib \(m_E^+(7/389)=-1\) et \(m_E^+(5/389)=-2\), antérieurement testées. L'identification à la normalisation de Néron est une hypothèse de provenance du certificat qu'un audit de publication doit reconstruire indépendamment.

## 2. Théorème de la mesure quadratique

Fixons un premier \(p\ge5\) de bonne réduction **ordinaire** et \(a_p=a_p(E)\in\mathbb Z_p^\times\). Définissons \(j_p(a)\equiv-(a^{p-1}-1)/p\pmod p\) pour \(p\nmid a\) et

\[
C_p=\sum_{a\in(\mathbb Z/p^2\mathbb Z)^\times}
 m_E^+(a/p^2)\binom{j_p(a)}{2}\pmod p.
\]

Écrivons \(\alpha\in\mathbb Z_p^\times\) pour la racine unité de \(X^2-a_pX+p\). La mesure ordinaire normalisée est

\[
\mu(a+p^2\mathbb Z_p)=\alpha^{-2}m_E^+(a/p^2)-\alpha^{-3}m_E^+(a/p).
\]

La composante de caractère modéré trivial de la mesure est \(L_p(E,T)\in\mathbb Z_p[[T]]\). Au niveau \(p^2\), le quotient \(\Gamma/\Gamma^p\) se paramètre par \(j_p(a)\). Pour chaque \(r\in(\mathbb Z/p\mathbb Z)^\times\), lorsque \(a\) parcourt les \(p\) relèvements de \(r\), \(j_p(a)\) parcourt \(\mathbb F_p\). Par conséquent, pour \(k=0,1,2\) (et \(p\ge5\)),

\[
 \sum_{a\equiv r\bmod p}\binom{j_p(a)}k=\binom p{k+1}\equiv0\pmod p.
\]

Le terme correctif \(\alpha^{-3}m(a/p)\) ne contribue donc pas aux trois premiers coefficients modulo \(p\). Comme \(\alpha\equiv a_p\pmod p\),

\[
\boxed{[T^2]L_p(E,T)\equiv a_p^{-2} C_p\pmod p.}
\]

Le calcul montre également \([T^0]L_p\equiv[T^1]L_p\equiv0\pmod p\) pour tous les premiers ordinaires audités (ces zéros sont vérifiés numériquement et ne sont pas supposés pour le critère général). Donc, si \(C_p\ne0\), les invariants de Weierstrass de \(L_p\) sont \(\mu=0,\lambda=2\).

## 3. Critère de trivialité de Sha

**Proposition.** Supposons \(E(\mathbb Q)\simeq\mathbb Z^2\), les résultats de Wuthrich et Greenberg applicables, et \([T^0]L_p\equiv[T^1]L_p\equiv0\pmod p\) avec \(C_p\ne0\). Alors \(\Sha(E/\mathbb Q)[p^\infty]=0\).

**Preuve.** Le corollaire 19 de Wuthrich (2014), au premier de bonne réduction ordinaire, donne \(\operatorname{char}_\Lambda X_p\mid L_p\), pour \(X_p=\operatorname{Sel}_{p^\infty}(E/\mathbb Q_\infty)^\vee\) et \(\Lambda=\mathbb Z_p[[T]]\). Il s'ensuit \(\mu(X_p)=0\) et \(\lambda(X_p)\le2\). La proposition 4.15 de Greenberg (1998) assure que \(X_p\) n'a pas de sous-module fini non nul. Ainsi \(X_p\) est \(\mathbb Z_p\)-libre de rang \(s\le2\). L'injection de Kummer des deux générateurs rationnels, suivie de la restriction à \(\mathbb Q_\infty\), donne deux copies de \(\mathbb Q_p/\mathbb Z_p\) dans \(\operatorname{Sel}_{p^\infty}(E/\mathbb Q_\infty)^\Gamma\) (la restriction est injective car \(E(\mathbb Q_\infty)[p]=0\)). Par dualité, \(X_p/TX_p\) surjecte sur \(\mathbb Z_p^2\). Donc \(s=2\) et \(T\) agit trivialement sur \(X_p\). Les invariants du Selmer sont exactement \((\mathbb Q_p/\mathbb Z_p)^2\), remplis par les classes de Kummer rationnelles, et \(\Sha(E/\mathbb Q)[p^\infty]=0\). \(\square\)

Sources : [Wuthrich, Corollaire 19](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/int_kato.pdf), [Greenberg, Proposition 4.15](https://arxiv.org/pdf/math/9809206), [formule de mesure SageMath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html).

## 4. Audit exhaustif exécuté

Pour tous les nombres premiers \(5\le p<2000\), le vérificateur natif reconstruit les valeurs \(m(a/p^2)\) par fractions continues et évalue les coefficients de degré 0,1,2,3, sans arithmétique à virgule flottante. On a **301 premiers** au total : **297 ordinaires**, **3 supersinguliers** \(107,599,1049\), et **1 premier de mauvaise réduction** \(389\). Pour les **297 premiers ordinaires** :

* \(C_{p,0}=C_{p,1}=0\pmod p\) ;
* \(C_p\ne0\pmod p\) pour chacun ;
* le nombre de classes parcourues est exactement \(p(p-1)\) par premier.

En particulier, le critère donne \(\Sha[p^\infty]=0\) pour ces 297 premiers, **sous réserve de l'audit indépendant des données exactes**. L'implémentation `bsd389_ordinary_p2_independent.py`, entièrement distincte du noyau C++, vérifie les six premiers d'essai \(p=5,7,11,89,103,109\) par fractions rationnelles, en incluant le terme correctif de la mesure et la relation de distribution \(U_p\).

Échantillon :

| \(p\) | \(a_p\) | \(C_p\) |
|---:|---:|---:|
| 89 | -8 | 8 |
| 97 | -9 | 40 |
| 103 | -6 | 59 |
| 109 | 2 | 31 |
| 127 | 11 | 48 |
| 131 | 2 | 30 |
| 397 | 24 | 209 |
| 593 | 44 | 543 |
| 997 | -22 | 275 |
| 1009 | — | 247 |
| 1721 | 54 | 1382 |
| 1999 | 40 | 458 |

Le document CSV complet `bsd389_ordinary_5_1999_manifest.csv` est validé contre la liste indépendante des nombres premiers calculés par SymPy ; son SHA256 est `cd0cfbb3f9c216433eb95966c0896f0ab64eabfa38f17480e93e98f15090afe9`.

**Cas distincts :** pour les premiers supersinguliers 107, 599 et 1049, les coefficients bruts au niveau \(p^2\) valent respectivement \(86,543,202\pmod p\). Ils sont non nuls mais le critère ordinaire ne s'y applique pas. À 389, il faut le facteur exceptionnel ; un certificat cyclotomique spécifique a été fourni dans une session précédente. Ce document ne prétend ni conclure pour les premiers \(p\ge2000\), ni établir la formule complexe de BSD.

## 5. Reproduction

```
python bsd389_make_ordinary_manifest.py
python bsd389_ordinary_p2_independent.py
c++ -O3 -std=c++17 bsd389_ordinary_p2_audit.cpp -o ordinary_full
c++ -O3 -std=c++17 bsd389_ordinary_p2_audit_half.cpp -o ordinary_half
```

Le fichier CSV fournit tous les résultats exécutés. Le noyau "half" exploite les identités \(m(-a/n)=m(a/n)\) et \(j_p(-a)=j_p(a)\), et a été comparé au noyau intégral sur les premiers 5, 7, 89, 997 et 1721.