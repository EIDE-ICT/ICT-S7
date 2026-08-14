# 🐍 Python — S7 — Séance 06

## Collections d'objets

Lors des séances précédentes, nous avons appris à créer des classes et des objets.

Nous savons maintenant utiliser :

- `class` ;
- `__init__` ;
- les attributs ;
- les méthodes ;
- `__str__` ;
- l'héritage ;
- `super()` ;
- le polymorphisme.

Nous allons maintenant apprendre à **gérer plusieurs objets ensemble**.

C'est une étape essentielle avant de commencer notre mini-projet.

---

# 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- stocker plusieurs objets dans une liste ;
- parcourir une collection d'objets ;
- ajouter un objet à une collection ;
- rechercher un objet ;
- filtrer une collection ;
- modifier un objet présent dans une collection ;
- créer une classe qui gère une collection d'autres objets ;
- utiliser plusieurs classes ensemble.

---

# 1. Pourquoi utiliser une collection d'objets ?

Imaginons une classe :

```python
class Livre:

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} — {self.auteur}"
```

Nous pouvons créer plusieurs livres :

```python
l1 = Livre("1984", "George Orwell")
l2 = Livre("Dune", "Frank Herbert")
l3 = Livre("Fondation", "Isaac Asimov")
```

Mais comment gérer facilement 10, 100 ou 1000 livres ?

Nous pouvons les placer dans une **liste**.

---

# 2. Une liste d'objets

```python
livres = [
    Livre("1984", "George Orwell"),
    Livre("Dune", "Frank Herbert"),
    Livre("Fondation", "Isaac Asimov")
]
```

La liste contient maintenant trois objets de type :

```text
Livre
```

Nous pouvons la représenter ainsi :

```text
livres
│
├── Livre("1984", ...)
├── Livre("Dune", ...)
└── Livre("Fondation", ...)
```

---

# 3. Parcourir une collection d'objets

Comme pour n'importe quelle liste, nous pouvons utiliser :

```python
for
```

Exemple :

```python
for livre in livres:
    print(livre)
```

Résultat :

```text
1984 — George Orwell
Dune — Frank Herbert
Fondation — Isaac Asimov
```

Grâce à `__str__`, chaque objet est affiché proprement.

---

# 4. Accéder aux attributs

Pendant le parcours, nous pouvons accéder aux attributs de chaque objet.

```python
for livre in livres:
    print(livre.titre)
```

Résultat :

```text
1984
Dune
Fondation
```

Ou :

```python
for livre in livres:
    print(f"{livre.titre} a été écrit par {livre.auteur}.")
```

---

# 5. Ajouter un objet

Pour ajouter un nouvel objet à la liste :

```python
nouveau_livre = Livre(
    "Le Petit Prince",
    "Antoine de Saint-Exupéry"
)

livres.append(nouveau_livre)
```

Nous pouvons également écrire directement :

```python
livres.append(
    Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
)
```

---

# 6. Rechercher un objet

Nous pouvons rechercher un livre grâce à une boucle.

```python
titre_recherche = "Dune"

for livre in livres:

    if livre.titre == titre_recherche:
        print(livre)
```

Résultat :

```text
Dune — Frank Herbert
```

---

# 7. Retourner l'objet trouvé

Dans un programme plus important, il est souvent préférable de créer une fonction.

```python
def rechercher_livre(livres, titre):

    for livre in livres:

        if livre.titre == titre:
            return livre

    return None
```

Nous pouvons ensuite écrire :

```python
resultat = rechercher_livre(
    livres,
    "Dune"
)
```

Puis :

```python
if resultat is not None:
    print(resultat)
else:
    print("Livre introuvable")
```

---

# 8. Recherche insensible aux majuscules

Avec :

```python
if livre.titre == titre:
```

les recherches :

```text
Dune
```

et :

```text
dune
```

sont différentes.

Nous pouvons améliorer notre recherche avec :

```python
.lower()
```

Exemple :

```python
if livre.titre.lower() == titre.lower():
```

Ainsi :

```text
DUNE
Dune
dune
```

peuvent tous permettre de retrouver le même livre.

---

# 9. Filtrer une collection

Rechercher signifie généralement trouver **un objet particulier**.

Filtrer signifie sélectionner **plusieurs objets correspondant à une condition**.

Imaginons :

```python
class Produit:

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
```

Avec :

```python
produits = [
    Produit("Clavier", 49.90),
    Produit("Souris", 29.90),
    Produit("Écran", 249.90),
    Produit("Webcam", 59.90)
]
```

Nous voulons afficher les produits coûtant moins de `60 €`.

```python
for produit in produits:

    if produit.prix < 60:
        print(produit.nom)
```

---

# 10. Créer une nouvelle liste filtrée

Nous pouvons également créer une nouvelle collection :

```python
produits_pas_chers = []

for produit in produits:

    if produit.prix < 60:
        produits_pas_chers.append(produit)
```

Nous avons maintenant :

```text
produits
        ↓
    FILTRAGE
        ↓
produits_pas_chers
```

---

# 11. Modifier un objet dans une collection

Les éléments de la liste sont des objets.

Nous pouvons donc appeler leurs méthodes.

Prenons :

```python
class Produit:

    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def vendre(self, quantite):

        if quantite <= self.stock:
            self.stock -= quantite
```

Puis :

```python
produits = [
    Produit("Clavier", 49.90, 10),
    Produit("Souris", 29.90, 15)
]
```

Nous pouvons écrire :

```python
produits[0].vendre(2)
```

Le stock du premier produit est maintenant modifié.

---

# 12. Rechercher puis modifier

Une opération très fréquente consiste à :

```text
RECHERCHER
    ↓
TROUVER L'OBJET
    ↓
APPELER UNE MÉTHODE
    ↓
MODIFIER L'OBJET
```

Par exemple :

```python
for produit in produits:

    if produit.nom == "Clavier":
        produit.vendre(2)
```

L'objet présent dans la liste est directement modifié.

---

# 13. Une classe qui contient des objets

Nous pouvons aller plus loin.

Au lieu de gérer directement :

```python
livres = []
```

nous pouvons créer une classe :

```python
Bibliotheque
```

Cette classe contiendra les livres.

```python
class Bibliotheque:

    def __init__(self):
        self.livres = []
```

Nous avons alors :

```text
Bibliotheque
│
└── livres
    ├── Livre
    ├── Livre
    └── Livre
```

---

# 14. Ajouter un objet avec une méthode

Nous pouvons créer :

```python
def ajouter_livre(self, livre):
    self.livres.append(livre)
```

La classe devient :

```python
class Bibliotheque:

    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
```

Utilisation :

```python
bibliotheque = Bibliotheque()

l1 = Livre("1984", "George Orwell")
l2 = Livre("Dune", "Frank Herbert")

bibliotheque.ajouter_livre(l1)
bibliotheque.ajouter_livre(l2)
```

---

# 15. Afficher les objets

Ajoutons :

```python
def afficher_livres(self):

    for livre in self.livres:
        print(livre)
```

Nous pouvons maintenant écrire :

```python
bibliotheque.afficher_livres()
```

---

# 16. Rechercher un objet

Ajoutons une méthode :

```python
def rechercher_livre(self, titre):

    for livre in self.livres:

        if livre.titre.lower() == titre.lower():
            return livre

    return None
```

Utilisation :

```python
livre = bibliotheque.rechercher_livre("Dune")

if livre is not None:
    print(livre)
else:
    print("Livre introuvable")
```

---

# 17. Deux classes qui travaillent ensemble

Nous avons maintenant :

```text
Livre
│
├── titre
├── auteur
└── ...

        utilisé par

Bibliotheque
│
├── livres
├── ajouter_livre()
├── afficher_livres()
└── rechercher_livre()
```

`Livre` représente **un élément**.

`Bibliotheque` représente **un ensemble de livres et les opérations permettant de les gérer**.

Cette organisation sera très utile pour le mini-projet.

---

# 18. Exemple complet

```python
class Livre:

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} — {self.auteur}"


class Bibliotheque:

    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):

        for livre in self.livres:
            print(livre)

    def rechercher_livre(self, titre):

        for livre in self.livres:

            if livre.titre.lower() == titre.lower():
                return livre

        return None
```

Utilisation :

```python
bibliotheque = Bibliotheque()

bibliotheque.ajouter_livre(
    Livre("1984", "George Orwell")
)

bibliotheque.ajouter_livre(
    Livre("Dune", "Frank Herbert")
)

bibliotheque.afficher_livres()
```

---

# 🧠 À retenir

## Collection d'objets

```python
objets = [
    Objet(...),
    Objet(...),
    Objet(...)
]
```

---

## Parcourir

```python
for objet in objets:
    print(objet)
```

---

## Ajouter

```python
objets.append(nouvel_objet)
```

---

## Rechercher

```python
for objet in objets:

    if objet.attribut == valeur:
        return objet

return None
```

---

## Filtrer

```python
resultats = []

for objet in objets:

    if condition:
        resultats.append(objet)
```

---

## Collection dans une classe

```python
class Gestionnaire:

    def __init__(self):
        self.objets = []
```

Cette organisation permet de regrouper les opérations concernant la collection dans une même classe.

---

# 🔍 Vocabulaire

| Terme | Signification |
|---|---|
| Collection | Ensemble de plusieurs éléments |
| Liste d'objets | Liste Python contenant des instances de classes |
| Parcours | Utilisation d'une boucle pour examiner les objets |
| Recherche | Trouver un objet particulier |
| Filtrage | Sélectionner plusieurs objets selon une condition |
| Gestionnaire | Classe chargée de gérer une collection d'objets |

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Travaillez dans :

```text
seance06_exercice1.py
seance06_exercice2.py
seance06_exercice3.py
seance06_exercice4.py
```

Ne modifiez pas le nom des fichiers.

---

# Exercice 1 — Liste de livres

📄 Fichier :

```text
seance06_exercice1.py
```

Créez une classe :

```python
Livre
```

avec :

```text
titre
auteur
annee
```

Ajoutez :

```python
__str__()
```

Puis créez au moins **5 livres** dans une liste :

```python
livres = [
    ...
]
```

---

## Travail demandé

Utilisez une boucle pour :

1. afficher tous les livres ;
2. afficher uniquement leur titre ;
3. afficher uniquement les livres publiés après une année donnée.

Par exemple :

```text
Livres publiés après 2000
```

---

# Exercice 2 — Rechercher un produit

📄 Fichier :

```text
seance06_exercice2.py
```

Créez une classe :

```python
Produit
```

avec :

```text
nom
prix
stock
```

Créez ensuite une liste contenant plusieurs produits.

---

## Recherche

Créez une fonction :

```python
rechercher_produit(produits, nom)
```

qui :

- parcourt la liste ;
- recherche le produit ;
- retourne l'objet s'il existe ;
- retourne `None` s'il n'existe pas.

---

## Test

```python
produit = rechercher_produit(
    produits,
    "Clavier"
)

if produit is not None:
    print(produit)
else:
    print("Produit introuvable")
```

La recherche doit fonctionner indépendamment des majuscules et minuscules.

---

# Exercice 3 — Filtrer des étudiants

📄 Fichier :

```text
seance06_exercice3.py
```

Créez une classe :

```python
Etudiant
```

avec :

```text
nom
notes
```

Ajoutez :

```python
moyenne()
```

qui retourne la moyenne de l'étudiant.

Créez plusieurs étudiants dans une liste :

```python
etudiants = [
    ...
]
```

---

## Travail demandé

Créez une fonction :

```python
etudiants_admis(etudiants)
```

qui retourne une nouvelle liste contenant uniquement les étudiants dont :

```text
moyenne >= 10
```

Puis affichez les étudiants admis.

---

## Bonus

Créez également :

```python
meilleur_etudiant(etudiants)
```

qui retourne l'étudiant possédant la meilleure moyenne.

---

# Exercice 4 — Bibliothèque

📄 Fichier :

```text
seance06_exercice4.py
```

Cet exercice rassemble plusieurs notions étudiées jusqu'à présent.

Créez deux classes :

```text
Livre
Bibliotheque
```

---

## Classe `Livre`

Un livre possède :

```text
titre
auteur
disponible
```

Lors de sa création :

```text
disponible = True
```

Ajoutez :

```python
__str__()
```

---

## Classe `Bibliotheque`

Une bibliothèque possède :

```python
self.livres = []
```

Ajoutez les méthodes suivantes :

```python
ajouter_livre(livre)
```

```python
afficher_livres()
```

```python
rechercher_livre(titre)
```

---

## Méthode `emprunter_livre()`

Ajoutez ensuite :

```python
emprunter_livre(titre)
```

La méthode doit :

```text
rechercher le livre
        ↓
vérifier qu'il existe
        ↓
vérifier qu'il est disponible
        ↓
modifier son état
```

Après un emprunt :

```text
disponible = False
```

---

## Méthode `rendre_livre()`

Ajoutez :

```python
rendre_livre(titre)
```

qui remet :

```text
disponible = True
```

---

# ⭐ Défi — Recherche et filtrage

Ajoutez à `Bibliotheque` :

```python
rechercher_par_auteur(auteur)
```

Cette méthode doit retourner **une liste de tous les livres écrits par cet auteur**.

Par exemple :

```python
livres = bibliotheque.rechercher_par_auteur(
    "Isaac Asimov"
)
```

Puis :

```python
for livre in livres:
    print(livre)
```

---

# 🧪 Tester votre classe

Ne testez pas uniquement les cas normaux.

Pour `Bibliotheque`, testez :

```text
Ajouter plusieurs livres            ✅
Afficher les livres                 ✅
Rechercher un livre existant        ✅
Rechercher un livre inexistant      ✅
Emprunter un livre disponible       ✅
Emprunter un livre déjà emprunté    ✅
Rendre un livre                     ✅
```

---

# ⚠️ Erreurs fréquentes

## Ajouter une classe au lieu d'un objet

Incorrect :

```python
livres.append(Livre)
```

Correct :

```python
livres.append(
    Livre("Dune", "Frank Herbert")
)
```

---

## Oublier de parcourir la liste

Une collection contient plusieurs objets.

Il faut généralement utiliser :

```python
for objet in objets:
```

pour examiner chaque élément.

---

## Confondre `return` et `print`

Une recherche doit généralement :

```python
return objet
```

plutôt que :

```python
print(objet)
```

Cela permet de réutiliser ensuite l'objet trouvé.

---

## Oublier `None`

Si aucun objet n'est trouvé :

```python
return None
```

permet au programme de détecter clairement l'échec de la recherche.

---

## Modifier une copie inutilement

Lorsque vous parcourez :

```python
for produit in produits:
```

`produit` représente directement l'objet contenu dans la liste.

Ainsi :

```python
produit.stock -= 1
```

modifie bien l'objet de la collection.

---

# 🚀 Exécuter les exercices

Dans le terminal :

```bash
python seance06_exercice1.py
```

```bash
python seance06_exercice2.py
```

```bash
python seance06_exercice3.py
```

```bash
python seance06_exercice4.py
```

---

# 💾 Sauvegarder votre travail

Travaillez progressivement :

```text
Créer la classe
       ↓
Créer plusieurs objets
       ↓
Tester
       ↓
Créer la collection
       ↓
Tester
       ↓
Ajouter une recherche
       ↓
Tester
       ↓
Ajouter une modification
       ↓
Tester
       ↓
Commit
```

Exemples de commits :

```text
Ajoute collection de livres
```

```text
Ajoute recherche de produits
```

```text
Ajoute filtrage des étudiants
```

```text
Termine classe Bibliotheque
```

```text
Termine séance 06
```

---

# ⚠️ Fichiers `corrige`

Vous trouverez également :

```text
seance06_exercice1_corrige.py
seance06_exercice2_corrige.py
seance06_exercice3_corrige.py
seance06_exercice4_corrige.py
```

Travaillez d'abord dans les fichiers sans :

```text
_corrige
```

N'utilisez les corrigés qu'après avoir réellement essayé de résoudre les exercices.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je sais créer une liste d'objets ;
- [ ] je sais parcourir une collection d'objets ;
- [ ] je sais accéder aux attributs des objets d'une liste ;
- [ ] je sais ajouter un objet avec `append()` ;
- [ ] je sais rechercher un objet ;
- [ ] je sais retourner `None` lorsqu'une recherche échoue ;
- [ ] je sais filtrer une collection ;
- [ ] je sais modifier un objet présent dans une collection ;
- [ ] je sais créer une classe contenant une liste d'autres objets ;
- [ ] je sais faire travailler deux classes ensemble ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Créer et gérer une collection d'objets, rechercher et filtrer ces objets, puis organiser cette collection dans une classe dédiée.**

---

# 🔜 Prochaine séance

## Séance 07 — Mini-projet POO : conception

Vous connaissez maintenant les principales notions nécessaires pour construire une petite application orientée objet :

```text
Classes
    ↓
Objets
    ↓
Attributs
    ↓
Méthodes
    ↓
Constructeurs
    ↓
Encapsulation
    ↓
Héritage
    ↓
Polymorphisme
    ↓
Collections d'objets
```

Lors de la prochaine séance, vous commencerez votre **mini-projet POO**.

Vous devrez d'abord réfléchir avant de programmer :

```text
IDÉE
  ↓
FONCTIONNALITÉS
  ↓
CLASSES
  ↓
ATTRIBUTS
  ↓
MÉTHODES
  ↓
RELATIONS
  ↓
PROGRAMMATION
```

Le mini-projet se déroulera sur les **séances 07 à 10** :

```text
Séance 07 → conception
Séance 08 → développement
Séance 09 → intégration et tests
Séance 10 → finalisation et présentation
```

🚀 À partir de la prochaine séance, vous allez utiliser les notions étudiées pour construire **votre propre application Python orientée objet**.