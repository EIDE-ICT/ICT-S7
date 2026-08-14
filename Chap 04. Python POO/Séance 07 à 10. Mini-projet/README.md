# 🐍 Python — S7 — Séances 07 à 10

# 🚀 Mini-projet POO

Vous connaissez maintenant les principales notions de programmation orientée objet étudiées dans ce chapitre :

```text
Classes et objets
      ↓
Attributs et méthodes
      ↓
Constructeur __init__
      ↓
Encapsulation
      ↓
Méthodes spéciales
      ↓
Héritage
      ↓
Polymorphisme
      ↓
Collections d'objets
```

Vous allez maintenant utiliser ces connaissances pour réaliser votre propre **mini-application Python orientée objet**.

Le projet se déroule sur **4 séances**.

---

# 🎯 Objectif général

Vous devez concevoir et développer une petite application Python utilisant la programmation orientée objet.

Votre projet devra notamment comporter :

- plusieurs classes ;
- des attributs ;
- des méthodes ;
- des constructeurs `__init__` ;
- une collection d'objets ;
- plusieurs fonctionnalités ;
- un programme principal ;
- une interaction avec l'utilisateur ;
- des tests ;
- une documentation.

L'objectif n'est pas de créer une application très complexe.

L'objectif est de montrer que vous êtes capable de **concevoir et organiser correctement un programme orienté objet**.

---

# 📅 Organisation du projet

```text
Séance 07
CONCEPTION
     ↓
Séance 08
DÉVELOPPEMENT
     ↓
Séance 09
INTÉGRATION & TESTS
     ↓
Séance 10
FINALISATION & PRÉSENTATION
```

---

# 📁 Fichiers du projet

Le dossier contient :

```text
seance07_projet_lancement.py
seance08_projet_developpement.py
seance09_projet_tests.py
seance10_projet_finalisation.py
```

ainsi que les fichiers de correction correspondants.

Vous créerez également progressivement les fichiers nécessaires à votre propre projet.

Par exemple :

```text
PROJET.md
main.py
```

et éventuellement :

```text
livre.py
bibliotheque.py
```

ou d'autres fichiers correspondant à vos propres classes.

---

# 💡 Choisir un sujet

Votre projet doit permettre de gérer une **collection d'objets**.

Quelques exemples :

### 📚 Bibliothèque

```text
Livre
Bibliotheque
```

Fonctionnalités possibles :

- ajouter un livre ;
- afficher les livres ;
- rechercher un livre ;
- emprunter un livre ;
- rendre un livre.

---

### 🛒 Gestion de stock

```text
Produit
Magasin
```

Fonctionnalités possibles :

- ajouter un produit ;
- afficher le stock ;
- rechercher un produit ;
- vendre un produit ;
- restocker.

---

### 🎬 Collection de films

```text
Film
CollectionFilms
```

Fonctionnalités possibles :

- ajouter un film ;
- rechercher un film ;
- filtrer par genre ;
- noter un film ;
- afficher la collection.

---

### 🎮 Gestion de personnages

```text
Personnage
Equipe
```

Fonctionnalités possibles :

- créer un personnage ;
- afficher les personnages ;
- modifier les points de vie ;
- rechercher un personnage ;
- gérer une équipe.

---

### 🏫 Gestion d'étudiants

```text
Etudiant
Classe
```

Fonctionnalités possibles :

- ajouter un étudiant ;
- ajouter des notes ;
- calculer une moyenne ;
- rechercher un étudiant ;
- afficher les étudiants admis.

---

# ⚠️ Taille du projet

Choisissez un projet **simple mais complet**.

Un bon projet avec :

```text
2 ou 3 classes
+
5 fonctionnalités qui fonctionnent
```

est préférable à :

```text
8 classes
+
20 fonctionnalités incomplètes
```

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 SÉANCE 07 — CONCEPTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Objectif

Avant de programmer, vous devez **concevoir votre application**.

Aujourd'hui :

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
PREMIERS TESTS
```

---

# 1. Créer `PROJET.md`

Créez à la racine de votre projet :

```text
PROJET.md
```

Ce document constituera le **cahier des charges de votre application**.

---

# 2. Présenter le projet

Commencez par :

```markdown
# Nom du projet

## Description

Expliquez en quelques lignes ce que fera votre application.
```

Votre description doit permettre de comprendre immédiatement l'objectif du programme.

---

# 3. Définir les fonctionnalités

Ajoutez :

```markdown
## Fonctionnalités

1. ...
2. ...
3. ...
4. ...
5. ...
```

Essayez de prévoir environ **5 fonctionnalités principales**.

---

# 4. Identifier les classes

Posez-vous la question :

> Quels sont les objets importants de mon application ?

Exemple :

```text
Bibliothèque

Objets importants :

Livre
Bibliotheque
```

Vous obtenez alors vos premières classes.

---

# 5. Identifier les attributs

Pour chaque classe, identifiez les données nécessaires.

Exemple :

```text
Livre
│
├── titre
├── auteur
├── annee
└── disponible
```

---

# 6. Identifier les méthodes

Demandez-vous maintenant :

> Que peut faire cet objet ?

Par exemple :

```text
Bibliotheque
│
├── ajouter_livre()
├── rechercher_livre()
├── afficher_livres()
├── emprunter_livre()
└── rendre_livre()
```

---

# 7. Représenter les relations

Vous pouvez représenter votre conception simplement :

```text
Bibliotheque
│
└── contient
      ↓
   plusieurs
      ↓
    Livre
```

Vous n'avez pas besoin de réaliser un diagramme UML complexe.

L'objectif est de comprendre **comment vos classes travaillent ensemble**.

---

# 8. Commencer les classes

Une fois votre conception validée, vous pouvez commencer à programmer.

Exemple :

```python
class Livre:

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True
```

Puis testez immédiatement :

```python
livre = Livre(
    "Dune",
    "Frank Herbert"
)

print(livre.titre)
```

---

# ✅ Fin de la séance 07

Vous devez avoir :

- [ ] choisi votre sujet ;
- [ ] créé `PROJET.md` ;
- [ ] décrit votre application ;
- [ ] défini environ 5 fonctionnalités ;
- [ ] identifié vos classes ;
- [ ] identifié leurs attributs ;
- [ ] identifié leurs méthodes ;
- [ ] représenté les relations entre les classes ;
- [ ] commencé au moins une classe ;
- [ ] effectué plusieurs commits.

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💻 SÉANCE 08 — DÉVELOPPEMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Objectif

Vous allez maintenant transformer votre conception en **programme fonctionnel**.

La méthode de travail sera :

```text
CLASSE
  ↓
CONSTRUCTEUR
  ↓
MÉTHODE
  ↓
TEST
  ↓
MÉTHODE SUIVANTE
  ↓
TEST
  ↓
COMMIT
```

---

# 1. Implémenter les classes

Créez vos classes principales.

Exemple :

```python
class Livre:

    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def __str__(self):
        return f"{self.titre} — {self.auteur}"
```

---

# 2. Tester les objets

Créez plusieurs objets :

```python
l1 = Livre(
    "1984",
    "George Orwell",
    1949
)

l2 = Livre(
    "Dune",
    "Frank Herbert",
    1965
)

print(l1)
print(l2)
```

Ne continuez que lorsque cette première partie fonctionne.

---

# 3. Créer une collection

Votre application doit gérer plusieurs objets.

Par exemple :

```python
class Bibliotheque:

    def __init__(self):
        self.livres = []
```

Puis :

```python
def ajouter_livre(self, livre):
    self.livres.append(livre)
```

---

# 4. Ajouter une recherche

Exemple :

```python
def rechercher_livre(self, titre):

    for livre in self.livres:

        if livre.titre.lower() == titre.lower():
            return livre

    return None
```

---

# 5. Commencer `main.py`

Votre programme principal doit progressivement utiliser vos classes.

Exemple :

```python
bibliotheque = Bibliotheque()

bibliotheque.ajouter_livre(
    Livre("1984", "George Orwell", 1949)
)

bibliotheque.ajouter_livre(
    Livre("Dune", "Frank Herbert", 1965)
)
```

---

# 6. Commencer le menu

Vous pouvez ensuite commencer l'interface :

```python
while True:

    print()
    print("===== BIBLIOTHÈQUE =====")
    print("1. Afficher les livres")
    print("2. Rechercher un livre")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        bibliotheque.afficher_livres()

    elif choix == "2":
        titre = input("Titre : ")
        livre = bibliotheque.rechercher_livre(titre)

        if livre is not None:
            print(livre)
        else:
            print("Livre introuvable")

    elif choix == "3":
        break

    else:
        print("Choix invalide")
```

Adaptez évidemment ce menu à votre projet.

---

# ✅ Fin de la séance 08

Vous devez avoir :

- [ ] vos classes principales ;
- [ ] vos constructeurs `__init__` ;
- [ ] plusieurs méthodes fonctionnelles ;
- [ ] plusieurs objets de test ;
- [ ] une collection d'objets ;
- [ ] une fonctionnalité d'ajout ;
- [ ] une recherche ou un filtrage ;
- [ ] commencé `main.py` ;
- [ ] commencé le menu ;
- [ ] effectué plusieurs commits ;
- [ ] pushé votre travail sur GitHub.

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧪 SÉANCE 09 — INTÉGRATION ET TESTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Objectif

Votre application doit maintenant devenir **complète et robuste**.

Aujourd'hui :

```text
TERMINER
   ↓
INTÉGRER
   ↓
TESTER
   ↓
CORRIGER
   ↓
RETESTER
```

---

# 1. Faire le point

Reprenez votre :

```text
PROJET.md
```

Pour chaque fonctionnalité, indiquez :

```text
✅ terminée
🟡 en cours
❌ pas commencée
```

Terminez en priorité les fonctionnalités indispensables.

---

# 2. Terminer le menu

Toutes les fonctionnalités principales doivent être accessibles depuis votre programme.

Par exemple :

```text
===== MON APPLICATION =====

1. Afficher
2. Ajouter
3. Rechercher
4. Modifier
5. Supprimer
6. Quitter
```

Votre menu dépend évidemment de votre projet.

---

# 3. Tester les cas normaux

Pour chaque fonctionnalité :

```text
ACTION
   ↓
RÉSULTAT ATTENDU
   ↓
RÉSULTAT OBTENU
```

Vérifiez que les deux correspondent.

---

# 4. Tester les cas particuliers

Testez également :

```text
Objet inexistant
Collection vide
Champ vide
Valeur négative
Choix incorrect
Quantité insuffisante
```

Choisissez les situations pertinentes pour votre projet.

---

# 5. Gérer les erreurs de saisie

Si nécessaire, utilisez :

```python
try:
    valeur = int(input("Valeur : "))

except ValueError:
    print("Veuillez entrer un nombre entier.")
```

Votre application ne doit pas s'arrêter brutalement à la première mauvaise saisie.

---

# 6. Créer un plan de tests

Ajoutez dans :

```text
PROJET.md
```

une section :

```markdown
## Tests

| Test | Résultat attendu | Résultat |
|---|---|---|
| Afficher les objets | Liste affichée | ✅ |
| Ajouter un objet | Objet ajouté | ✅ |
| Rechercher objet existant | Objet trouvé | ✅ |
| Rechercher objet absent | Message adapté | ✅ |
| Saisie incorrecte | Programme continue | ❌ |
```

Corrigez ensuite les tests qui échouent.

---

# 7. Corriger les bugs

Utilisez cette méthode :

```text
REPRODUIRE
    ↓
IDENTIFIER
    ↓
COMPRENDRE
    ↓
CORRIGER
    ↓
RETESTER
    ↓
COMMIT
```

Après une correction, vérifiez que vous n'avez pas cassé une autre fonctionnalité.

---

# 8. Nettoyer progressivement le code

Commencez à supprimer :

```python
print("TEST")
print("ICI")
print("DEBUG")
```

Supprimez également :

- les variables inutilisées ;
- les anciennes versions du code ;
- les fonctions inutiles ;
- les duplications évidentes.

---

# ✅ Fin de la séance 09

Votre application doit être **pratiquement terminée**.

Vérifiez :

- [ ] toutes les classes sont terminées ;
- [ ] les principales méthodes fonctionnent ;
- [ ] le menu fonctionne ;
- [ ] toutes les fonctionnalités sont accessibles ;
- [ ] les recherches infructueuses sont gérées ;
- [ ] les collections vides sont gérées ;
- [ ] les principales mauvaises saisies sont gérées ;
- [ ] plusieurs cas particuliers ont été testés ;
- [ ] les bugs principaux sont corrigés ;
- [ ] `PROJET.md` contient le plan de tests ;
- [ ] le projet est à jour sur GitHub.

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏁 SÉANCE 10 — FINALISATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Objectif

Cette dernière séance n'est pas destinée à développer une grosse nouvelle fonctionnalité.

Votre objectif est de :

```text
TESTER
  ↓
CORRIGER
  ↓
NETTOYER
  ↓
DOCUMENTER
  ↓
PRÉPARER
  ↓
PRÉSENTER
```

---

# 1. Test final

Lancez :

```bash
python main.py
```

Puis testez votre application **comme si vous étiez un utilisateur qui la découvre pour la première fois**.

Vous ne devez pas avoir besoin de modifier le code pour utiliser le programme.

---

# 2. Nettoyer le code

Supprimez :

- les tests inutiles ;
- les affichages de débogage ;
- les variables inutilisées ;
- les anciennes versions commentées ;
- les fonctions qui ne servent plus.

---

# 3. Vérifier la qualité du code

Utilisez des noms compréhensibles.

Évitez :

```python
x
a
truc
liste1
fct1
```

Préférez :

```python
livre
utilisateur
produits
livre_recherche
rechercher_livre
```

---

# 4. Ajouter des commentaires utiles

Il n'est pas nécessaire de commenter chaque ligne.

Évitez :

```python
# affiche le livre
print(livre)
```

Préférez des commentaires qui expliquent une décision ou une partie moins évidente :

```python
# Recherche insensible aux majuscules/minuscules
if livre.titre.lower() == titre.lower():
```

---

# 5. Vérifier `PROJET.md`

Votre cahier des charges doit correspondre à **l'application réellement réalisée**.

Mettez-le à jour si votre projet a évolué.

Il doit contenir au minimum :

```text
Nom du projet
Description
Fonctionnalités
Classes
Attributs
Méthodes
Tests
```

---

# 6. Créer le README final du projet

Votre projet doit posséder son propre :

```text
README.md
```

Vous pouvez utiliser cette structure :

```markdown
# Nom du projet

## Description

Expliquez ce que fait votre application.

## Fonctionnalités

- ...
- ...
- ...

## Classes

### Classe 1

Rôle : ...

### Classe 2

Rôle : ...

## Lancer le programme

```bash
python main.py
```

## Utilisation

Expliquez rapidement comment utiliser l'application.

## Auteur

Nom : ...
Classe : ...
```

---

# 7. Préparer la présentation

Vous présenterez votre projet pendant environ :

```text
3 à 5 minutes
```

Aucun PowerPoint n'est nécessaire.

Vous allez principalement présenter et exécuter votre programme.

---

# 🎤 Présentation attendue

Présentez dans cet ordre :

```text
1. Sujet du projet
        ↓
2. Fonctionnalités
        ↓
3. Classes utilisées
        ↓
4. Démonstration
        ↓
5. Partie intéressante du code
        ↓
6. Difficulté rencontrée
```

---

# 8. Présenter vos classes

Vous devez être capable d'expliquer :

```text
Pourquoi cette classe existe-t-elle ?

Quels sont ses attributs ?

Quelles sont ses méthodes ?

Comment travaille-t-elle avec les autres classes ?
```

---

# 9. Faire une démonstration

Préparez votre démonstration à l'avance.

Par exemple :

```text
Lancer l'application
        ↓
Afficher les objets
        ↓
Ajouter un objet
        ↓
Rechercher cet objet
        ↓
Modifier son état
        ↓
Afficher le résultat
```

---

# 10. Expliquer une difficulté

Préparez un exemple de problème rencontré pendant le développement.

Expliquez :

```text
Quel était le problème ?
        ↓
Comment l'avez-vous identifié ?
        ↓
Comment l'avez-vous corrigé ?
```

---

# 🤖 Utilisation de l'IA

Vous pouvez utiliser une IA pour :

- expliquer un message d'erreur ;
- comprendre une notion ;
- proposer des cas de test ;
- obtenir une explication sur une partie du code ;
- chercher une piste de correction.

Mais vous devez être capable d'expliquer **tout le code présent dans votre projet**.

Pendant la présentation, l'enseignant pourra vous demander d'expliquer une partie précise de votre programme.

---

# 💾 GitHub

Pendant les quatre séances, effectuez régulièrement des commits.

Évitez :

```text
projet
```

ou :

```text
modifications
```

Préférez :

```text
Ajoute classe Livre
```

```text
Ajoute recherche de livres
```

```text
Corrige gestion du stock
```

```text
Ajoute validation des saisies
```

```text
Finalise mini-projet POO
```

---

# ☁️ Vérification finale GitHub

À la fin :

```text
Commit
   ↓
Sync Changes
   ↓
Ouvrir GitHub
   ↓
Vérifier les fichiers
```

⚠️ Un fichier présent uniquement dans votre Codespace mais qui n'a pas été **commit et push** n'est pas considéré comme remis.

---

# ✅ Checklist finale du projet

Avant de remettre votre projet :

## Programmation

- [ ] mon programme démarre avec `python main.py` ;
- [ ] j'utilise plusieurs classes ;
- [ ] mes classes utilisent `__init__` ;
- [ ] mes classes possèdent des méthodes pertinentes ;
- [ ] j'utilise correctement `self` ;
- [ ] j'utilise une collection d'objets ;
- [ ] mes principales fonctionnalités fonctionnent ;
- [ ] mon menu fonctionne ;
- [ ] mon application ne plante pas lors d'une utilisation normale.

## Tests

- [ ] j'ai testé les fonctionnalités principales ;
- [ ] j'ai testé des cas particuliers ;
- [ ] j'ai testé une recherche infructueuse ;
- [ ] j'ai corrigé les bugs identifiés.

## Qualité

- [ ] les noms des variables sont compréhensibles ;
- [ ] les noms des méthodes sont compréhensibles ;
- [ ] mon code est correctement indenté ;
- [ ] les anciens tests ont été supprimés ;
- [ ] les commentaires sont utiles.

## Documentation

- [ ] `PROJET.md` est à jour ;
- [ ] mon projet possède un `README.md` ;
- [ ] les instructions de lancement sont indiquées.

## GitHub

- [ ] j'ai effectué plusieurs commits ;
- [ ] j'ai effectué `Sync Changes` ;
- [ ] ma dernière version est visible sur GitHub.

## Présentation

- [ ] je sais expliquer mon projet ;
- [ ] je sais expliquer mes classes ;
- [ ] je sais expliquer mes principales méthodes ;
- [ ] je sais expliquer une difficulté rencontrée ;
- [ ] ma démonstration est prête.

---

# 🎯 Critères de réussite

Le projet sera notamment évalué sur :

| Domaine | Attendu |
|---|---|
| 🧱 POO | Classes, objets, attributs, méthodes |
| ⚙️ Fonctionnement | Application fonctionnelle |
| 📚 Collections | Gestion de plusieurs objets |
| 🧪 Tests | Cas normaux et particuliers |
| 🧹 Code | Lisibilité et organisation |
| 📝 Documentation | `PROJET.md` et `README.md` |
| 💾 GitHub | Travail sauvegardé et commits |
| 🎤 Présentation | Compréhension du projet |

---

# 🏁 Fin du chapitre Python POO

Vous avez maintenant parcouru les principales étapes :

```text
Remise à niveau Python
        ↓
Classes et objets
        ↓
Constructeurs
        ↓
Encapsulation
        ↓
Méthodes spéciales
        ↓
Héritage
        ↓
Polymorphisme
        ↓
Collections d'objets
        ↓
Conception
        ↓
Développement
        ↓
Tests
        ↓
Mini-projet
```

L'objectif de ce chapitre n'était pas seulement d'apprendre de nouvelles instructions Python.

Vous avez appris à **organiser un programme autour d'objets possédant des données et des comportements**, puis à utiliser ces objets pour construire une petite application.

---

# 🎉 Projet terminé !

Avant de fermer votre environnement :

```text
TEST
  ↓
COMMIT
  ↓
SYNC CHANGES
  ↓
VÉRIFICATION SUR GITHUB
```

🐍 **Votre mini-projet Python POO est terminé !**