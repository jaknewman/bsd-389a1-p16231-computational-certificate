# E389a1: parité du Selmer et critère de détection par trois primes

Date : 5 novembre 2026.

## Théorème : la dimension du p-Selmer est paire pour tout premier impair

Soit E = 389a1, définie par y²+y=x³+x²−2x, de rang de Mordell–Weil certifié 2 et de torsion rationnelle triviale. Sage documente un nombre de racine global w(E)=+1.

Notons rho_p le corang sur Z_p du Selmer p-infini et delta_p le corang de Sha[p-infini]. La suite de Kummer donne rho_p = 2 + delta_p.

Le théorème de p-parité de T. et V. Dokchitser, démontré pour toute courbe elliptique sur Q et tout premier, fournit (-1)^rho_p = w(E)=+1. Donc delta_p est pair, sans hypothèse de finitude de Sha.

La partie p-primaire de Sha est de cotype fini : elle est isomorphe, non canoniquement, à (Q_p/Z_p)^delta_p ⊕ F_p avec F_p un groupe fini p-primaire. Sur le quotient par le sous-groupe divisible maximal, l'accouplement de Cassels–Tate est non dégénéré et alterné pour les courbes elliptiques. Pour p impair, F_p se décompose en paires de facteurs cycliques de même ordre, donc dim_Fp F_p[p] est pair.

Ainsi dim_Fp Sha[p] = delta_p + dim_Fp F_p[p] est pair. Comme la torsion rationnelle de E est triviale et le rang vaut 2 :

**dim_Fp Sel(E[p]/Q) = 2 + dim_Fp Sha[p] appartient à {2,4,6,...}.**

Références primaires :
- Dokchitser–Dokchitser, On the Birch–Swinnerton-Dyer quotients modulo squares, Annals of Mathematics 172 (2010): https://annals.math.princeton.edu/2010/172-1/p11
- Poonen–Stoll, The Cassels–Tate pairing on polarized abelian varieties, Annals of Mathematics 150 (1999): https://annals.math.princeton.edu/1999/150-3/p09
- Documentation Sage sur le nombre de racine de E389a1 : https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html

## Critère à trois localisations

Fixons p impair et trois premiers auxiliaires distincts q1,q2,q3, de bonne réduction, différents de p, tels que chaque quotient local E(F_qi)/p soit une droite sur F_p.

Supposons démontrée l'injectivité de la localisation sur **tout le groupe de Selmer** :

Sel(E[p]/Q) → E(F_q1)/p ⊕ E(F_q2)/p ⊕ E(F_q3)/p.

Alors dim Sel(E[p]/Q) ≤ 3. Comme cette dimension est paire et au moins 2, elle vaut exactement 2. La suite de Kummer entraîne Sha[p]=0, et donc Sha[p-infini]=0. En outre, par algèbre linéaire, parmi ces trois coordonnées il existe une paire qui détecte déjà le Selmer entier.

**ATTENTION :** vérifier uniquement que les images des deux points rationnels P,Q ont rang 2 ne prouve PAS l'injectivité de la localisation du Selmer entier. Si Sha[p] est non nul, sa dimension est au moins 2, le Selmer a dimension au moins 4, et aucune application vers trois droites ne peut être injective.

Pour k droites auxiliaires dont les images de P,Q sont indépendantes, si t_p = dim Sha[p], alors dim ker(localisation) ≥ 2+t_p−k. En particulier, lorsque k=3 et t_p≥2, le noyau n'est pas nul.

## Conséquence du théorème de Chebotarev antérieur

Sous surjectivité résiduelle GL2(F_p), le théorème de détection par Chebotarev antérieurement prouvé identifie le nombre minimal d'auxiliaires de dimension locale 1 détectant le Selmer entier à dim Sel(E[p]/Q). Ce minimum appartient donc à {2,4,6,...}. Toute borne **indépendante** ≤3 forcerait donc exactement 2.

Il ne s'agit PAS d'une borne déjà établie, ni d'un progrès démontrant l'annulation uniforme de Sha. La parité exclut simplement une obstruction de dimension 1 et fournit une manière alternative de formuler un certificat. Les certificats Sage p=2,5,7,11,13,107 et le témoin publié pour p=3 conservent leur statut antérieur.

## Question de recherche précise

Produire, sans supposer Sha fini, une présentation arithmétique du Selmer modulo p, un complexe de Selmer ou une loi de réciprocité montrant que **trois localisations auxiliaires suffisent à détecter toutes les classes de Selmer** pour presque tous les p. La parité donnerait alors automatiquement l'annulation. Aucun argument uniforme de ce type n'est actuellement fourni ici.
