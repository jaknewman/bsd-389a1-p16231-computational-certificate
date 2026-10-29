# BSD 389a1 — certificat local au premier supersingulier 599

**Date :** 29 octobre 2026  
**Statut :** calcul arithmétique local **PASS** sur le serveur Sage Ubuntu.  
**Portée :** indépendance des deux générateurs rationnels dans deux groupes locaux modulo 599. **Ne certifie pas** la non-annulation d'un nombre de Kurihara, la dimension du 599-Selmer, ni l'annulation de Sha[599^infinity].

## Courbe et primes

- Courbe E : `y^2 + y = x^3 + x^2 - 2*x`, Cremona `389a1`, rang rationnel 2, générateurs `P=(0,0)` et `Q=(1,0)`.
- Premier `p=599` supersingulier : `a_p=0`, `#E(F_p)=600`.
- Premier auxiliaire `q1=6912461` : `a_q1=1799`, `#E(F_q1)=6910663=599*11537`.
- Premier auxiliaire `q2=13963889` : `a_q2=-4191`, `#E(F_q2)=13968081=599*23319`.
- `q1 ≡ q2 ≡ 1 (mod 599)` ; `a_qi ≡ qi+1 (mod 599)` ; les cofacteurs 11537 et 23319 sont non divisibles par 599.

## Déterminant des réductions rationnelles

Les coordonnées des réductions de P et Q dans les quotients locaux par 599, exprimées dans les bases choisies par le programme, sont :

```
M_599 = [[1,536],
         [1,412]]
det(M_599) = 412 - 536 = -124 = 475 (mod 599) != 0.
```

Puisque E(Q) a rang 2 et n'a pas de 599-torsion rationnelle, le morphisme de réduction

`E(Q)/599 E(Q) -> E(F_q1)/599 E(F_q1) ⊕ E(F_q2)/599 E(F_q2)`

est un isomorphisme de `F_599`-espaces vectoriels de dimension 2.

## Journal de la reproduction exécutée par l'utilisateur

Commande :

```bash
python -u verification/bsd389_p599_auxiliary_local_certificate.py \
  2>&1 | tee ~/bsd389_p599_local.log
```

Sortie observée :

```text
P599_SUPERSINGULAR_EXACT_POINTCOUNT_PASS a_599 0 cardinality 600
P599_EXACT_POINT_COUNT_PASS 6912461 a_q 1799 cardinality 6910663 cofactor 11537
P599_LOCAL_COORDINATE_ROW_PASS 6912461 [1, 536]
P599_EXACT_POINT_COUNT_PASS 13963889 a_q -4191 cardinality 13968081 cofactor 23319
P599_LOCAL_COORDINATE_ROW_PASS 13963889 [1, 412]
P599_LOCAL_MORDELL_WEIL_DETERMINANT_NONZERO_PASS 475
P599_AUXILIARY_N 96524838120829
P599_AUXILIARY_PHI_N 96524817244480
P599_AUXILIARY_SYMMETRY_REPS 48262408622240
P599_MW_MOD_P_TO_TWO_LOCAL_GROUPS_ISOMORPHISM_PASS
BOUNDARY: no Kurihara nonzero witness; Selmer and Sha[599^infinity] NOT certified.
```

La formule `n=q1*q2` donne `n=96524838120829`, `phi(n)=96524817244480`. Le calcul direct des nombres de Kurihara par représentants modulo `±1` porterait sur `phi(n)/2=48262408622240` termes : **ne pas lancer une énumération brute**.

## Limite mathématique et suite du programme

- Le déterminant local mesure uniquement les images des points de Mordell–Weil. Il ne démontre **pas** l'injectivité de la localisation du groupe de 599-Selmer ni l'annulation de `Sha(E/Q)[599]`.
- Pour utiliser le critère Kurihara–Kim à rang 2, une non-annulation certifiée du **nombre de Kurihara normalisé** `delta_(q1*q2) (mod 599)` est encore nécessaire, avec la vérification des hypothèses et de la normalisation de son théorème.
- La routine Sage 10.9 de la série p-adique supersingulière requiert une attention particulière à sa précision : au niveau n=3 et `prec=3`, la borne de précision alpha-adique du terme de degré 2 est négative (`2*(3-1)-(3+2)=-1`) ; la boucle native compte `(599-1)*599^2=214562998` évaluations de mesure. Elle ne constitue donc pas un raccourci prouvé et économique.
- Pistes de recherche : algorithme exact accéléré pour `delta_(q1*q2)`, présentation de Selmer indépendante de ce symbole, ou comparaison de Fitting intégrale uniforme. Aucune de ces dernières étapes n'est encore démontrée.

**Traçabilité :** script `verification/bsd389_p599_auxiliary_local_certificate.py` et journal `results/bsd389_p599_local_2026-10-29.log` (à archiver ensemble dans Git). Les empreintes SHA-256 doivent être calculées sur les fichiers réellement sauvegardés, non inférées de cette note.