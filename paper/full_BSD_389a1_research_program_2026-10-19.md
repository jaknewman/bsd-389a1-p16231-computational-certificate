# Programme BSD complète — 389a1 (ouverture 2026-10-19)

**Auteur : Jerry Armando Kasa.** Statut : programme de recherche, **aucune preuve de BSD complète annoncée**.

## Objet exact

Pour `E: y² + y = x³ + x² − 2x` de conducteur 389, rang algébrique certifié 2 et rang analytique 2 (travail antérieur), démontrer :

`L''(E,1)/2 = Ω_E · Reg(E) · #Sha(E/Q) · ∏c_l / #E(Q)_tors²`.

Notre premier audit donne `∏c_l=1` et `#E(Q)_tors=1`, donc la cible se réduit à `L''(E,1)/2 = Ω_E Reg(E) #Sha(E/Q)`.

**Ne pas confondre :** `Sha(E/Q)[16231^infty]=0`, sous les hypothèses computationnelles auditées du certificat de C01, avec `Sha(E/Q)=0`. Une infinité de bornes indépendantes pour des premiers distincts ne démontre pas à elle seule la finitude globale du groupe.

## Phase 0 — Normalisation classique : audit numérique reproductible

Réaliser sur le même environnement SageMath 10.9, de manière indépendante de la série cyclotomique p-adique :

- `E=EllipticCurve('389a1')`, rang/générateurs, minimalité, torsion, nombres de Tamagawa.
- Période Néron–BSD `Ω_E=E.period_lattice().omega(prec=120)` : **deux composantes réelles comprises**, sans les compter deux fois.
- Régulateur archimédien `Reg(E)=E.regulator(proof=True,precision=120)` sur les deux générateurs.
- Coefficient classique `L''(E,1)/2` via `E.lseries().dokchitser(prec=120,algorithm='gp').derivative(1,2)/2`, corroboration facultative avec `algorithm='pari'`.
- Quotient numérique `Sha_an = (L''/2)/(Ω_E Reg(E))`.

Valeurs de référence documentées (non nouvellement exécutées sur notre IONOS) :

```text
Ω_E                    ≈ 4.98042512171010
Reg(E)                 ≈ 0.152460177943144
Ω_E * Reg(E)           ≈ 0.759316500288427
L''(E,1)/2              ≈ 0.759316500288427
Sha_analytic_prediction ≈ 1
```

**Ne pas faire d'arrondi 1→preuve**. L'accord même à 100 décimales est une identité approchée, non une égalité prouvée.

Sources primaires :
- https://doc.sagemath.org/html/en/reference/lfunctions/sage/lfunctions/dokchitser.html
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/period_lattice.html
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html
- https://doc-gitlab.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html

## Phase I — Analytique rigoureuse

1. Reprendre le certificat de `ord_{s=1}L(E,s)=2`; audit indépendant de l'encadrement.
2. Produire un **intervalle rigoureux** du coefficient `L''(E,1)/2` par équation fonctionnelle et bornes explicites sur les queues (pas uniquement les chiffres Dokchitser).
3. Produire des encadrements rigoureux séparés de la période et du régulateur réel, avec contrôle des erreurs et de la base de Mordell–Weil.
4. Préciser ce que ces intervalles démontrent et n'utilisent jamais une vérification numérique comme preuve de l'égalité transcendante exacte.

## Phase II — Arithmétique globale (le principal obstacle)

1. Certifier éventuellement la partie 2 par 2-descente et utiliser les bornes p-primaires connues : exemples Sage 5 et 7; notre certificat de 16231.
2. Déterminer un argument **fini, effectif et rigoureux** qui exclut toutes les autres composantes sans passer simplement par une liste arbitraire de premiers.
3. Démontrer la **finitude globale** de `Sha(E/Q)`, puis son ordre (objectif attendu `1`). Les p-primary bounds pour chaque p ne suffisent pas, sans borne de support ou théorème global.
4. Étudier les outils théoriques de rang 2 (Euler systems dérivés, comparaisons Iwasawa/ETNC, cycles de Heegner généralisés) seulement sous hypothèses explicitement vérifiées, sans supposer qu'une conjecture de rang 2 est déjà un théorème.

## Phase III — Égalité exacte BSD

Même `Sha=0` et `L''/2 ≈ Ω_E Reg(E)` ne suffisent pas : il faut **un théorème de comparaison exacte** entre le coefficient analytique complexe et le régulateur, avec toutes les périodes et facteurs locaux correctement normalisés. Isoler cette implication comme un lemme/théorème à prouver et signaler toute conjecture encore requise.

## Stratégie de rédaction

Établir trois étiquettes distinctes : `NUMERIC_PASS`, `CONDITIONAL_MATH`, `PROVED`. Ne jamais promouvoir l'une en l'autre sans démonstration autonome. Archiver entrées, empreintes, code, versions de logiciels et journaux. Ne pas annoncer la BSD complète avant les trois phases I–III entièrement fermées.

Le calcul au premier 16231 est conservé comme contribution spécifique forte mais **pas** comme raccourci automatique vers la formule BSD complète.
