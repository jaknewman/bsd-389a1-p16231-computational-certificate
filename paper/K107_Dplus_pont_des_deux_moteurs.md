# BSD 389a1 — Pont algébrique exact entre Kurihara K107 et le moteur des moments (28 octobre 2026)

## Proposition 1 — Extraction par algèbre de groupe

Soit p un premier impair, q1,q2 des premiers distincts tels que p | (qi−1), et n=q1*q2. Fixons des racines primitives gi modulo qi. Le groupe G=C_p×C_p est le quotient des unités modulo n par les noyaux des logarithmes li(a)=log_{gi}(a) mod p. Soit R un anneau dans lequel les symboles modulaires normalisés sont définis, et supposons leur réduction modulo p intégrale. Posons

Θ=Σ_{a∈(Z/nZ)^×} [a/n]^+ [g1]^{l1(a)}[g2]^{l2(a)}∈ F_p[G].

Il existe un morphisme d'anneaux φ:F_p[G]→F_p[ε1,ε2]/(ε1²,ε2²) défini par [g1]↦1+ε1, [g2]↦1+ε2. Il est bien défini puisque (1+εi)^p=1 en caractéristique p. Pour chaque paire (i,j),

φ([g1]^i[g2]^j) = 1+iε1+jε2+ij ε1ε2.

Par conséquent le coefficient [ε1ε2]φ(Θ) égale exactement δ_{q1q2}=Σ[a/n]^+ l1(a)l2(a) (mod p). Aucune hypothèse sur le rang ou sur Sha n'intervient dans cette identité combinatoire.

## Proposition 2 — Factorisation par le module de Manin

Pour N=389, soit S=P¹(F_389), |S|=390, et M_s le symbole de l'arête unimodulaire indexée par s, avec les signes d'orientation fixés. La décomposition euclidienne de {∞,a/n} donne des entiers signés e_s(a) tels que [a/n]^+=Σ_s e_s(a)M_s. Alors

δ_{q1q2} = Σ_{s∈S} M_s W_s, où W_s=Σ_{a∈(Z/nZ)^×} e_s(a)l1(a)l2(a) (mod p).

Pour la symétrie a↦n−a, si li(−1)=0 modulo p, alors δ=2 Σ_{1≤a≤(n−1)/2,(a,n)=1} ... . La preuve requiert p | (qi−1)/2, vrai lorsque p est impair et qi≡1 (mod p), qi étant impair.

L'évaluation par fractions continues est une décomposition d'une application linéaire du module de symboles, non une preuve automatique d'une accélération sous-linéaire.

## Deux moteurs : quel est le véritable lien ?

- K107 calcule le coefficient mixte [ε1ε2] d'un élément de Mazur–Tate au **niveau auxiliaire q1q2**, en caractéristique 107.
- Le moteur historique 16231 construit des moments p-adiques ordinaires d'une distribution et une contraction terminale J, en caractéristique 16231 (et parfois à précision supérieure).
- Ces coefficients sont de même *type algébrique* (fonctionnelles linéaires de symboles et extraction d'un moment d'ordre 2), mais ils vivent dans des anneaux, groupes de variables et systèmes de distribution différents. Une égalité J=δ, ou une implication de non-annulation d'un premier vers un autre, **ne découle pas** des identités précédentes.

## Interface à construire pour p=16231

1. Fixer précisément le domaine des deux fonctions de moment (groupe de classes auxiliaires vs unités p-adiques) et les modules de symboles sur lesquels elles agissent.
2. Définir des transformations de distribution/trace à partir des matrices de Manin ; pour chaque opérateur T, prouver sur les générateurs de relations de Manin que la fonctionnelle projetée est bien définie.
3. Établir une vraie identité de compatibilité (par exemple de la forme λ_K∘T = λ_J), **avec la même caractéristique p**, normalisation et precision; sinon signaler l'obstruction.
4. Si cette compatibilité n'existe pas, utiliser Kurihara comme une voie distincte de certificats pour chaque p et préserver l'autre moteur pour son propre objectif.

## Frontière uniforme D+

Pour obtenir une conclusion « hors d'un ensemble fini de premiers », un certificat à p=107 ne suffit pas. Il faudrait un mécanisme uniforme assurant, pour tous les p assez grands, l'existence d'auxiliaires donnant δ_{q1q2}≠0, ou une borne indépendante des composantes p-primaires de Sha. La surjectivité résiduelle uniforme ne suffit pas en soi.

## Données computationnelles K107 à associer

E=389a1, p=107, (q1,q2)=(369793,383917), n=141969819181. Somme sur demi-plage =17, double =34 modulo 107. 710 blocs et cinq rejeux audités. SHA256 W390 ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0. Archive complète SHA256 b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754. Ces données attestent une exécution; ne remplacent pas la vérification des hypothèses du théorème de Selmer ni une preuve de correction du binaire.