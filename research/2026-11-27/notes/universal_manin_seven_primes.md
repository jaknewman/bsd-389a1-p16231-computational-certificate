# 389a1 : reconstruction universelle entière de Manin et sept nouveaux témoins de Kurihara

**26 novembre 2026 — note arithmétique et calculatoire.** Les exécutions ont été effectuées dans le conteneur de cette conversation. Elles sont reproductibles avec Python standard et C++17, mais n'ont pas encore fait l'objet d'un audit indépendant ou d'une relecture scientifique externe. **Ce travail ne démontre pas BSD complète**, ni la finitude de la totalité de Sha.

## 1. Courbe et conventions

\[
E/\mathbb Q:y^2+y=x^3+x^2-2x,\quad N=\Delta_{\min}=389.
\]

Rang exact 2; base entière \(P=(-1,1),\ Q=(0,-1)\), torsion 1, constante de Manin optimale 1, Tamagawa \(c_{389}=1\). Ces données sont consultables à [LMFDB](https://www.lmfdb.org/EllipticCurve/Q/389a1/). On utilise le symbole modulaire **plus** normalisé par la période de Néron, avec valeurs exactes précédemment certifiées par Sage et eclib :

\[
m^+(7/389)=-1,\qquad m^+(5/389)=-2.
\]

## 2. Un unique vecteur entier pour tous les premiers

Les 390 cosets de Manin sur \(\mathbb P^1(\mathbb F_{389})\) sont indexés par \([1:t]\) pour \(t=0,\ldots,388\) et \([0:1]\) pour \(t=389\). Notons \(v\in\mathbb Z^{390}\) le vecteur du fichier `bsd389_universal_manin_390.txt`, SHA-256

`9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360`.

Sa distribution exacte est

\[
\#\{v_j=-2,-1,0,1,2\}=(30,84,162,84,30).
\]

Le vérificateur indépendant `bsd389_universal_manin_exact_certificate.py` établit par **calcul entier exact** les faits suivants :

1. \(v\) satisfait 1 170 relations (S, R, plus) de Manin.
2. \(v\) satisfait 1 307 identités \(T_2=-2\), évaluées sur les cusps \(a/n\) de dénominateur \(2\le n\le65\).
3. Les 2 477 relations réunies ont rang **389 modulo 7**. Elles ont donc rang **au moins 389 sur \(\mathbb Q\)** ; et comme \(v\ne0\) appartient à leur noyau entier, elles ont rang **exactement 389 sur \(\mathbb Q\)**.
4. \(v\) vérifie encore 881 identités entières pour chacun des opérateurs de contrôle indépendants \(T_3=-2,T_5=-3,T_7=-5\) ; total 2 643.
5. Les chemins en fractions continues donnent exactement \(m_v(7/389)=-1\), \(m_v(5/389)=-2\), \(m_v(0)=0\).

**Conclusion démontrée par unicité rationnelle** : le véritable vecteur du symbole modulaire plus de \(E\) appartient à ce noyau car les identités de Manin et de Hecke sont exactes. La valeur indépendante \(m^+(7/389)=-1\) fixe le scalaire ; le véritable vecteur est donc exactement \(v\). Ce raisonnement n'utilise ni Sha, ni BSD. La table est primitive (PGCD des coordonnées égal à 1) et **la même table entière s'utilise pour tout \(p\)**, y compris les premiers où l'espace propre modulo \(p\) a plusieurs dimensions (notamment \(p=29\)).

En particulier, pour tout rationnel \(a/n\), la décomposition en arêtes de Manin par fractions continues et la table \(v\) donnent une valeur entière de \(m^+(a/n)\). C'est une généralisation algorithmique démontrée de la normalisation des symboles.

## 3. Sommes de Kurihara calculées intégralement

Pour \(p\ge5\), deux premiers admissibles distincts \(q_1,q_2\) satisfont \(q_i\equiv1\bmod p\) et \(a_{q_i}(E)\equiv2\bmod p\). On choisit une racine primitive \(g_i\) et la fonction de logarithme discret \(j_i\). La somme utilisée est exactement

\[
\widetilde\delta_{q_1q_2} =
\sum_{\substack{1\le a<q_1q_2\\(a,q_1q_2)=1}}
 m^+\left(\frac a{q_1q_2}\right)
 j_1(a\bmod q_1)j_2(a\bmod q_2)\pmod p.
\]

Chaque somme ci-dessous a été parcourue sur la **totalité des \(n-1\) résidus**, sans employer la réduction par symétrie. Tous les nombres de points et tous les déterminants locaux ont été contrôlés par des lois de groupe et des dénombrements exacts indépendants du calcul modulaire.

| \(p\) | \(q_1\) | \(q_2\) | \(n=q_1q_2\) | \(\tilde\delta_n\pmod p\) | \(\det_{\rm loc}\pmod p\) | \(\#E(\mathbb F_p)\) |
|---:|---:|---:|---:|---:|---:|---:|
|19|2243|3877|8696111|**4**|1|15|
|23|1289|3727|4804103|**17**|7|28|
|29|12007|18329|220076303|**5**|1|36|
|31|9859|16369|161381971|**2**|27|28|
|37|15541|17539|272573599|**35**|32|46|
|41|11399|16319|186020281|**3**|36|45|
|43|2237|15137|33861469|**42**|31|32|

Le point délicat \(p=29\) illustre la puissance de la table rationnelle : la reconstruction *modulo 29* à partir du petit système a un noyau de dimension 2, alors que la table rationnelle entière est unique et se réduit de façon non ambiguë.

Les certificats précédemment calculés pour \(p=5,7,11,13,17\) se retrouvent aussi à partir de cette unique table par le programme natif, avec coefficients \(4,2,1,6,4\) respectivement. **Tous les premiers \(p\) de 5 à 43 sont donc couverts prime par prime.**

## 4. Passage de la somme non nulle à la composante de Sha

**Sources :** Chan-Ho Kim, [The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves, Theorems 1.8 et 1.10](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf) ; [LMFDB : 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389a1/).

Pour \(p\in\{19,23,29,31,37,41,43\}\), les conditions suivantes ont été contrôlées :

- \(p\) est bon, tous les \(q_i\) sont premiers, \(q_i\equiv1\pmod p\), \(a_{q_i}\equiv2\pmod p\) ; et \(p^2\nmid \#E(\mathbb F_{q_i})\), assurant une ligne locale de dimension 1.
- \(p\nmid\#E(\mathbb F_p)\), donc \(E(\mathbb Q_p)[p]=0\).
- \(c_E=1\) et tous les Tamagawa sont égaux à 1.
- La représentation résiduelle est surjective. Une trace de Frobenius de discriminant caractéristique non carré est donnée par \(q=2\) aux premiers \(p=19,23,31,43\), \(q=3\) aux premiers \(p=29,37\), et \(q=5\) à \(p=41\). L'inertie de la réduction multiplicative \(I_1\) au premier \(389\), avec \(v_{389}(\Delta_{\min})=1\), fournit une transvection non triviale ; avec l'irréductibilité et le déterminant cyclotomique surjectif, cela donne \(\mathrm{GL}_2(\mathbb F_p)\).
- \(\widetilde\delta_{q_1q_2}\not\equiv0\pmod p\). Par le théorème 1.8 de Kim et \(\operatorname{rang}E(\mathbb Q)=2\), l'ordre minimal \(\operatorname{ord}(\tilde\delta)=2\). Le couple satisfait alors la condition \(\nu(n)=\operatorname{ord}(\tilde\delta)\) du théorème 1.10.

Ainsi \(\dim_{\mathbb F_p}\mathrm{Sel}(E[p])=2\). La base entière de Mordell–Weil fournit déjà \(E(\mathbb Q)/p\simeq\mathbb F_p^2\), donc la suite exacte de Kummer montre \(\Sha(E/\mathbb Q)[p]=0\). Une composante de cotype fini \(p\)-primaire non nulle possède du \(p\)-torsion, donc \(\Sha(E/\mathbb Q)[p^\infty]=0\).

Ce raisonnement **n'utilise pas l'égalité BSD complexe** et ne suppose pas la finitude globale de Sha. Il doit néanmoins être repris et audité indépendamment avant toute revendication publique de preuve certifiée.

## 5. Reproduction

Tous les fichiers de l'archive sont dans le même répertoire. Environnement : Python 3 et compilateur C++17 ; pas de Sage requis.

```bash
python3 bsd389_universal_manin_exact_certificate.py --table bsd389_universal_manin_390.txt
g++ -std=c++17 -O3 bsd389_kurihara_native_general.cpp -o bsd389_kurihara_native_general
python3 bsd389_uniform_kurihara_prime_witness_audit.py \
  --native ./bsd389_kurihara_native_general --primes 19 23 29 31 37 41 43 \
  --output bsd389_recomputed.json
```

Attention : le balayage est \(O(q_1q_2\log(q_1q_2))\) et peut être long pour les plus grands couples. Un mode `--half` est disponible pour refaire un contrôle plus rapide à partir de la symétrie \(m^+(a/n)=m^+((n-a)/n)\).

## 6. Frontière mathématique de cette généralisation

La table entière est **uniforme en \(p\)**. L'algorithme l'est aussi. Mais rien dans sa construction ne prouve

\[
\forall p\ge47,\quad\exists q_1\ne q_2:\ \widetilde\delta_{q_1q_2}\not\equiv0\pmod p.
\]

C'est toujours l'étape *uniforme de non-annulation mixte* qui manque pour la finitude et la trivialité globale de Sha. Les composantes 2, 3, le mauvais premier 389 et les premiers non traités au-delà de 43 restent à examiner, et la rationalité motivique exacte / identité complexe \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\) demeurent ouvertes.

**Acquis réel :** preuve finie d'une table intégrale universelle, application uniforme de l'algorithme, et sept nouveaux témoins explicites apportant une information arithmétique nouvelle sur Sha.