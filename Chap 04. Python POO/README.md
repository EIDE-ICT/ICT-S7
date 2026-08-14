# ICT — Programmation orientée objet en Python

## S7 — Python POO

**10 séances · 20 périodes**

Support de cours consacré à la **programmation orientée objet (POO) en Python**.

Ce module s'appuie sur les connaissances de programmation acquises en **S6** et amène progressivement les élèves de la création de classes simples jusqu'à la réalisation d'une **application Python orientée objet complète**.

---

# Avant-propos

## 🎯 Objectifs du module

À l'issue de ces dix séances, l'élève est capable de :

- concevoir une classe Python ;
- créer et manipuler des objets ;
- utiliser des attributs et des méthodes ;
- comprendre et utiliser `self` ;
- utiliser un constructeur `__init__` ;
- comprendre le principe d'encapsulation ;
- utiliser des méthodes spéciales comme `__str__` ;
- créer des relations d'héritage entre plusieurs classes ;
- utiliser `super()` ;
- comprendre et mettre en œuvre le polymorphisme ;
- gérer des collections d'objets ;
- faire interagir plusieurs classes ;
- analyser un problème et identifier les classes nécessaires ;
- concevoir et développer une petite application orientée objet ;
- tester, corriger et documenter un programme Python.

L'objectif du module n'est donc plus uniquement d'apprendre la syntaxe Python, mais de comprendre **comment structurer un programme plus important autour d'objets possédant des données et des comportements**.

---

# 📚 Prérequis

Ce module suppose que les bases de Python étudiées en **S6** sont acquises.

Les élèves doivent notamment connaître :

- les variables ;
- les types de données ;
- les opérateurs ;
- `input()` et `print()` ;
- les conditions `if / elif / else` ;
- les boucles `for` et `while` ;
- les listes ;
- les fonctions ;
- les paramètres ;
- `return`.

La **séance 01** est consacrée à une remise à niveau de ces notions avant de commencer la programmation orientée objet.

---

# 💻 Environnement de travail

Le cours est conçu pour être réalisé avec un environnement de développement moderne accessible directement en ligne.

Visual Studio Code (VS Code) avec GitHub Codespaces : permet de programmer directement dans le navigateur, sans installation complexe.
Dans un premier temps, les environnements nécessitant une installation locale sont évités afin que les élèves puissent se concentrer sur l'apprentissage de la programmation.

---

# 🔄 Méthode de travail

Le module suit une progression allant d'un apprentissage guidé vers un travail de plus en plus autonome :

```text
Rappels Python
      ↓
Classes et objets
      ↓
Constructeurs
      ↓
Encapsulation
      ↓
Méthodes spéciales
      ↓
Entraînement autonome
      ↓
Héritage
      ↓
Polymorphisme
      ↓
Collections d'objets
      ↓
Conception d'une application
      ↓
Développement
      ↓
Tests
      ↓
Mini-projet
```

L'objectif est de passer progressivement de :

> **« Je sais reproduire un exemple. »**

à :

> **« Je sais concevoir et programmer ma propre solution. »**

---

# 📅 Organisation du module

| Séance | Contenu | Type de travail |
|---|---|---|
| **01** | Remise à niveau Python — rappel S6 | Révision guidée |
| **02** | Premiers pas en POO : classes et objets | Cours + exercices |
| **03** | Constructeurs, encapsulation et méthodes spéciales | Cours + exercices |
| **04** | Entraînement autonome : classes et objets | Autonomie guidée |
| **05** | Héritage et polymorphisme | Cours + exercices |
| **06** | Collections d'objets | Cours + exercices |
| **07** | Mini-projet — conception | Projet |
| **08** | Mini-projet — développement | Projet |
| **09** | Mini-projet — intégration et tests | Projet |
| **10** | Mini-projet — finalisation et présentation | Projet |

---

# 📖 Progression détaillée

## Séance 01 — Remise à niveau Python

Révision des principales notions étudiées en S6 :

```text
variables
types
conditions
boucles
listes
fonctions
return
```

🎯 **Objectif :** disposer des bases nécessaires avant de commencer la programmation orientée objet.

---

## Séance 02 — Premiers pas en POO : classes et objets

Introduction aux concepts fondamentaux :

```text
classe
objet
instance
attribut
méthode
self
```

Les élèves créent leurs premières classes et plusieurs objets à partir d'un même modèle.

🎯 **Objectif :** comprendre la relation entre une classe et ses instances.

---

## Séance 03 — Constructeurs, encapsulation et méthodes spéciales

Introduction à :

```python
__init__
```

et :

```python
__str__
```

Les élèves apprennent également à initialiser correctement les attributs et découvrent le principe d'encapsulation.

🎯 **Objectif :** construire des classes correctement structurées.

---

## Séance 04 — Entraînement autonome

Les élèves doivent progressivement concevoir eux-mêmes leurs classes à partir d'un énoncé.

La démarche devient :

```text
Analyser
   ↓
Identifier les attributs
   ↓
Identifier les méthodes
   ↓
Programmer
   ↓
Tester
```

🎯 **Objectif :** passer de la reproduction d'exemples à la conception autonome d'une classe.

---

## Séance 05 — Héritage et polymorphisme

Introduction aux relations entre classes :

```text
classe parente
classe enfant
héritage
super()
redéfinition
polymorphisme
```

Exemple :

```text
        Animal
        /    \
       /      \
    Chien     Chat
```

🎯 **Objectif :** comprendre comment réutiliser et spécialiser des classes existantes.

---

## Séance 06 — Collections d'objets

Les élèves apprennent à gérer plusieurs objets :

```python
livres = [
    Livre(...),
    Livre(...),
    Livre(...)
]
```

Les principales opérations étudiées sont :

- ajouter ;
- parcourir ;
- rechercher ;
- filtrer ;
- modifier.

Les élèves commencent également à créer des classes chargées de gérer d'autres objets.

Exemple :

```text
Bibliotheque
      │
      └── contient plusieurs
                │
                ▼
              Livre
```

🎯 **Objectif :** faire interagir plusieurs objets dans une même application.

---

# 🚀 Séances 07 à 10 — Mini-projet POO

Les quatre dernières séances sont consacrées à la réalisation d'une **application Python orientée objet**.

---

## Séance 07 — Conception

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
```

Les élèves définissent le cahier des charges de leur application dans :

```text
PROJET.md
```

---

## Séance 08 — Développement

Les élèves développent progressivement :

- les classes ;
- les constructeurs ;
- les méthodes ;
- les collections d'objets ;
- les principales fonctionnalités ;
- le programme `main.py`.

---

## Séance 09 — Intégration et tests

Les différentes parties du projet sont assemblées.

Les élèves doivent tester :

```text
cas normaux
cas limites
cas incorrects
```

Les bugs sont identifiés, corrigés puis testés à nouveau.

---

## Séance 10 — Finalisation et présentation

Dernière étape :

```text
TESTER
  ↓
CORRIGER
  ↓
NETTOYER
  ↓
DOCUMENTER
  ↓
PRÉSENTER
```

Les élèves finalisent leur documentation et présentent leur application.

---

# 📂 Organisation du dépôt

Le chapitre est organisé de la manière suivante :

```text
Chap 04. Python POO
│
├── Séance 01. Remise à niveau Python (Rappel S6)
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
├── Séance 02. Premiers pas en POO : classes et objets
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
├── Séance 03. Constructeurs, encapsulation, méthodes spéciales
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
├── Séance 04. Entraînement autonome : classes et objets
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
├── Séance 05. Héritage et polymorphisme
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
├── Séance 06. Collections d'objets
│   ├── README.md
│   ├── exercices.py
│   └── corrigés.py
│
└── Séance 07 à 10. Mini-projet
    ├── README.md
    └── fichiers du projet
```

---

# 📄 Contenu d'une séance

Chaque séance contient généralement :

- un `README.md` présentant le cours et les consignes ;
- les exercices Python `.py` ;
- les fichiers corrigés ;
- éventuellement des ressources complémentaires.

Les fichiers :

```text
*_corrige.py
```

contiennent les solutions.

Les élèves doivent d'abord travailler dans les fichiers sans :

```text
_corrige
```

avant de consulter les solutions.

---

# 💾 Utilisation de GitHub

Le travail est sauvegardé régulièrement grâce à Git.

Les élèves doivent adopter le cycle :

```text
MODIFIER
   ↓
TESTER
   ↓
COMMIT
   ↓
SYNC CHANGES
   ↓
GITHUB
```

Les messages de commit doivent décrire le travail réalisé.

Exemples :

```text
Termine exercice 1
```

```text
Ajoute classe Livre
```

```text
Ajoute méthode rechercher_livre
```

```text
Corrige gestion du stock
```

```text
Finalise mini-projet POO
```

---

# 🧪 Importance des tests

Un programme qui s'exécute une fois sans erreur n'est pas nécessairement correct.

Les élèves doivent progressivement apprendre à tester :

```text
CAS NORMAL
     +
CAS LIMITE
     +
CAS INCORRECT
```

Exemple :

```python
compte.retirer(20)     # cas normal
compte.retirer(100)    # solde insuffisant
compte.retirer(-10)    # valeur incorrecte
```

La phase de test fait partie intégrante du développement.

---

# 🤖 Utilisation de l'intelligence artificielle

Les outils d'intelligence artificielle peuvent être utilisés comme **aide à l'apprentissage**.

Ils peuvent notamment servir à :

- expliquer une notion ;
- expliquer un message d'erreur ;
- proposer des pistes de résolution ;
- aider à identifier un bug ;
- proposer des cas de test ;
- expliquer une partie du code.

Cependant :

> **L'élève doit être capable de comprendre et d'expliquer l'ensemble du code qu'il remet.**

Une solution générée automatiquement mais non comprise ne constitue pas un travail maîtrisé.

---

# 📝 Évaluation

Les activités et le mini-projet permettent notamment d'évaluer les compétences suivantes :

- **Interprétation** ;
- **Création de liens et application** ;
- **Résolution de problèmes** ;
- **Travailler dans des projets**.

Une attention particulière est portée à :

- la compréhension de la programmation orientée objet ;
- la qualité de la conception ;
- le fonctionnement du programme ;
- la capacité à tester et corriger ;
- l'organisation du code ;
- l'utilisation de GitHub ;
- la documentation ;
- la capacité à expliquer son propre programme.

---

# ✅ Compétences finales

À la fin du chapitre, l'élève doit pouvoir affirmer :

- [ ] je sais créer une classe ;
- [ ] je sais créer plusieurs objets ;
- [ ] je comprends les attributs et les méthodes ;
- [ ] je sais utiliser `self` ;
- [ ] je sais utiliser `__init__` ;
- [ ] je sais utiliser `__str__` ;
- [ ] je comprends le principe d'encapsulation ;
- [ ] je comprends le principe d'héritage ;
- [ ] je sais utiliser `super()` ;
- [ ] je comprends le polymorphisme ;
- [ ] je sais gérer une collection d'objets ;
- [ ] je sais faire travailler plusieurs classes ensemble ;
- [ ] je sais analyser un problème avant de programmer ;
- [ ] je sais tester et corriger mon programme ;
- [ ] je sais utiliser GitHub pour sauvegarder mon travail ;
- [ ] je suis capable de réaliser une petite application orientée objet.

---

# 🏁 Objectif final

À l'issue du chapitre, l'élève doit être capable de passer de :

```text
PROBLÈME
```

à :

```text
PROBLÈME
   ↓
ANALYSE
   ↓
CLASSES
   ↓
ATTRIBUTS
   ↓
MÉTHODES
   ↓
OBJETS
   ↓
PROGRAMMATION
   ↓
TESTS
   ↓
APPLICATION FONCTIONNELLE
```

---

**Bon apprentissage de la programmation orientée objet et bon codage ! 🐍🚀**
