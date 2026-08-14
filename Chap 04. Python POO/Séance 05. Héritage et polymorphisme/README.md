# 🐍 Python — S7 — Séance 05

## Héritage et polymorphisme

Lors des séances précédentes, nous avons appris à créer nos propres classes avec :

- des attributs ;
- des méthodes ;
- un constructeur `__init__` ;
- la méthode spéciale `__str__`.

Jusqu'à présent, nos classes étaient indépendantes.

Nous allons maintenant découvrir comment créer des **relations entre les classes** grâce à l'**héritage**.

---

# 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- expliquer le principe de l'héritage ;
- distinguer une classe parente d'une classe enfant ;
- créer une classe qui hérite d'une autre classe ;
- utiliser `super()` ;
- réutiliser le constructeur d'une classe parente ;
- ajouter des attributs spécifiques à une classe enfant ;
- redéfinir une méthode ;
- comprendre le principe du polymorphisme ;
- manipuler plusieurs objets ayant une classe parente commune.

---

# 1. Pourquoi utiliser l'héritage ?

Imaginons que nous souhaitions représenter plusieurs types d'animaux.

Nous pourrions créer :

```python
class Chien:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


class Chat:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Nous remarquons immédiatement un problème.

Les deux classes possèdent exactement les mêmes attributs :

```text
nom
age
```

Nous avons donc du code répété.

---

# 2. Créer une classe commune

Un chien et un chat sont tous les deux des animaux.

Nous pouvons donc créer une classe :

```python
Animal
```

qui contient les caractéristiques communes.

```python
class Animal:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Puis créer :

```text
          Animal
          /    \
         /      \
      Chien     Chat
```

`Animal` devient la **classe parente**.

`Chien` et `Chat` deviennent des **classes enfants**.

---

# 3. Créer une classe enfant

Pour indiquer qu'une classe hérite d'une autre classe :

```python
class Chien(Animal):
    pass
```

Les parenthèses :

```python
(Animal)
```

indiquent que `Chien` hérite de `Animal`.

Nous pouvons alors écrire :

```python
chien = Chien("Rex", 5)

print(chien.nom)
print(chien.age)
```

Même si `Chien` ne contient aucun code supplémentaire, il bénéficie des éléments définis dans `Animal`.

---

# 4. Vocabulaire

Dans :

```python
class Chien(Animal):
```

nous avons :

```text
Animal
   ↓
classe parente
classe mère
superclasse
```

et :

```text
Chien
   ↓
classe enfant
classe fille
sous-classe
```

Dans ce cours, nous utiliserons principalement :

```text
classe parente
classe enfant
```

---

# 5. Hériter des méthodes

La classe enfant hérite également des méthodes de la classe parente.

```python
class Animal:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")


class Chien(Animal):
    pass
```

Nous pouvons écrire :

```python
chien = Chien("Rex", 5)

chien.se_presenter()
```

Résultat :

```text
Je m'appelle Rex et j'ai 5 ans.
```

La méthode :

```python
se_presenter()
```

n'est pas définie dans `Chien`.

Elle est héritée de `Animal`.

---

# 6. Ajouter une méthode spécifique

Une classe enfant peut ajouter ses propres méthodes.

```python
class Chien(Animal):

    def aboyer(self):
        print("Wouf !")
```

Nous pouvons maintenant écrire :

```python
chien = Chien("Rex", 5)

chien.se_presenter()
chien.aboyer()
```

`Chien` possède donc :

```text
Méthodes héritées
└── se_presenter()

Méthodes spécifiques
└── aboyer()
```

---

# 7. Ajouter des attributs avec `super()`

Imaginons maintenant qu'un chien possède également une race.

Nous voulons pouvoir écrire :

```python
chien = Chien(
    "Rex",
    5,
    "Labrador"
)
```

Nous pourrions écrire :

```python
class Chien(Animal):

    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race
```

Mais nous répétons :

```python
self.nom = nom
self.age = age
```

qui existent déjà dans `Animal`.

---

# 8. Utiliser `super()`

Nous pouvons appeler le constructeur de la classe parente :

```python
class Chien(Animal):

    def __init__(self, nom, age, race):

        super().__init__(nom, age)

        self.race = race
```

`super()` permet ici d'accéder à la classe parente.

Cette instruction :

```python
super().__init__(nom, age)
```

appelle :

```python
Animal.__init__()
```

pour initialiser :

```text
nom
age
```

Puis :

```python
self.race = race
```

ajoute l'attribut spécifique au chien.

---

# 9. Exemple complet avec `super()`

```python
class Animal:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


class Chien(Animal):

    def __init__(self, nom, age, race):

        super().__init__(nom, age)

        self.race = race


chien = Chien(
    "Rex",
    5,
    "Labrador"
)

print(chien.nom)
print(chien.age)
print(chien.race)
```

Résultat :

```text
Rex
5
Labrador
```

---

# 10. Redéfinir une méthode

Une classe enfant peut remplacer une méthode héritée par sa propre version.

Prenons :

```python
class Animal:

    def parler(self):
        print("L'animal fait un bruit.")
```

Puis :

```python
class Chien(Animal):

    def parler(self):
        print("Wouf !")
```

et :

```python
class Chat(Animal):

    def parler(self):
        print("Miaou !")
```

Nous avons **redéfini** la méthode :

```python
parler()
```

dans chaque classe enfant.

---

# 11. Tester la redéfinition

```python
chien = Chien()
chat = Chat()

chien.parler()
chat.parler()
```

Résultat :

```text
Wouf !
Miaou !
```

Même nom de méthode :

```python
parler()
```

mais comportement différent selon l'objet.

---

# 12. Le polymorphisme

Le mot **polymorphisme** signifie littéralement :

```text
plusieurs formes
```

En programmation orientée objet, plusieurs objets peuvent répondre différemment au **même appel de méthode**.

Exemple :

```python
chien.parler()
chat.parler()
```

Nous appelons toujours :

```python
parler()
```

mais le résultat dépend de l'objet.

---

# 13. Exemple de polymorphisme

```python
class Animal:

    def parler(self):
        print("Bruit inconnu")


class Chien(Animal):

    def parler(self):
        print("Wouf !")


class Chat(Animal):

    def parler(self):
        print("Miaou !")
```

Créons plusieurs objets :

```python
animaux = [
    Chien(),
    Chat(),
    Chien()
]
```

Puis :

```python
for animal in animaux:
    animal.parler()
```

Résultat :

```text
Wouf !
Miaou !
Wouf !
```

La même instruction :

```python
animal.parler()
```

produit différents comportements.

C'est le **polymorphisme**.

---

# 14. Redéfinir `__str__`

Les méthodes spéciales peuvent également être redéfinies.

```python
class Animal:

    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Animal : {self.nom}"
```

Puis :

```python
class Chien(Animal):

    def __init__(self, nom, race):
        super().__init__(nom)
        self.race = race

    def __str__(self):
        return f"Chien : {self.nom} — {self.race}"
```

Ainsi :

```python
chien = Chien("Rex", "Labrador")

print(chien)
```

affiche :

```text
Chien : Rex — Labrador
```

---

# 🧠 À retenir

## Héritage

```python
class Chien(Animal):
    ...
```

signifie :

```text
Chien hérite de Animal
```

---

## Classe parente

```python
class Animal:
    ...
```

contient les caractéristiques communes.

---

## Classe enfant

```python
class Chien(Animal):
    ...
```

hérite des caractéristiques de la classe parente et peut en ajouter de nouvelles.

---

## `super()`

```python
super().__init__(nom, age)
```

permet d'appeler le constructeur de la classe parente.

---

## Redéfinition

Une classe enfant peut remplacer une méthode héritée :

```python
def parler(self):
    ...
```

---

## Polymorphisme

Plusieurs objets peuvent répondre différemment au même appel :

```python
objet.parler()
```

---

# 🔍 Vocabulaire

| Terme | Signification |
|---|---|
| Héritage | Création d'une classe à partir d'une autre |
| Classe parente | Classe dont les éléments sont hérités |
| Classe enfant | Classe qui hérite d'une autre |
| `super()` | Permet d'accéder à la classe parente |
| Redéfinition | Remplacement d'une méthode héritée |
| Polymorphisme | Même méthode, comportements différents |

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Travaillez dans :

```text
seance05_exercice1.py
seance05_exercice2.py
seance05_exercice3.py
seance05_exercice4.py
```

Ne modifiez pas le nom des fichiers.

---

# Exercice 1 — `Animal`, `Chien` et `Chat`

📄 Fichier :

```text
seance05_exercice1.py
```

Créez une classe :

```python
Animal
```

avec :

```text
nom
age
```

Utilisez un constructeur :

```python
__init__
```

Ajoutez également une méthode :

```python
se_presenter()
```

qui affiche par exemple :

```text
Je m'appelle Rex et j'ai 5 ans.
```

---

## Créer les classes enfants

Créez ensuite :

```python
Chien
```

et :

```python
Chat
```

qui héritent de :

```python
Animal
```

Ajoutez :

```python
aboyer()
```

dans `Chien`.

Ajoutez :

```python
miauler()
```

dans `Chat`.

---

## Test

Vous devez pouvoir écrire :

```python
chien = Chien("Rex", 5)
chat = Chat("Milo", 3)

chien.se_presenter()
chien.aboyer()

chat.se_presenter()
chat.miauler()
```

---

# Exercice 2 — Utiliser `super()`

📄 Fichier :

```text
seance05_exercice2.py
```

Créez une classe :

```python
Vehicule
```

avec les attributs :

```text
marque
modele
```

Puis créez une classe :

```python
Voiture
```

qui hérite de :

```python
Vehicule
```

Une voiture possède en plus :

```text
nombre_portes
```

Utilisez :

```python
super()
```

pour appeler le constructeur de `Vehicule`.

---

## Exemple

Vous devez pouvoir écrire :

```python
v = Voiture(
    "Toyota",
    "Corolla",
    5
)
```

Ajoutez :

```python
__str__
```

afin d'obtenir :

```text
Toyota Corolla — 5 portes
```

---

# Exercice 3 — Redéfinition et polymorphisme

📄 Fichier :

```text
seance05_exercice3.py
```

Créez :

```python
class Animal:

    def parler(self):
        ...
```

Puis créez trois classes enfants :

```text
Chien
Chat
Vache
```

Chaque classe doit redéfinir :

```python
parler()
```

afin d'obtenir :

```text
Chien → Wouf !
Chat  → Miaou !
Vache → Meuh !
```

---

## Tester le polymorphisme

Créez une liste :

```python
animaux = [
    Chien(),
    Chat(),
    Vache(),
    Chien()
]
```

Puis utilisez :

```python
for animal in animaux:
    animal.parler()
```

Vous devez obtenir différents comportements avec **la même instruction**.

---

# Exercice 4 — Employés

📄 Fichier :

```text
seance05_exercice4.py
```

Créez une classe :

```python
Employe
```

avec :

```text
nom
salaire_base
```

Ajoutez une méthode :

```python
calculer_salaire()
```

qui retourne :

```python
self.salaire_base
```

---

## Classe `Manager`

Créez :

```python
Manager
```

qui hérite de :

```python
Employe
```

Un manager possède également :

```text
prime
```

Utilisez :

```python
super()
```

dans son constructeur.

Redéfinissez :

```python
calculer_salaire()
```

pour retourner :

```text
salaire_base + prime
```

---

## Classe `Commercial`

Créez :

```python
Commercial
```

qui hérite également de :

```python
Employe
```

Un commercial possède :

```text
salaire_base
commission
```

Redéfinissez :

```python
calculer_salaire()
```

pour prendre en compte la commission.

---

## Tester le polymorphisme

Créez plusieurs employés :

```python
employes = [
    Employe(...),
    Manager(...),
    Commercial(...)
]
```

Puis :

```python
for employe in employes:
    print(employe.calculer_salaire())
```

La même méthode doit produire un résultat adapté au type d'employé.

---

# ⭐ Défi — Ajouter une nouvelle classe

Ajoutez une nouvelle classe enfant sans modifier les classes existantes.

Par exemple :

```text
Animal
├── Chien
├── Chat
├── Vache
└── Canard
```

Ajoutez :

```python
class Canard(Animal):

    def parler(self):
        print("Coin coin !")
```

Puis ajoutez un `Canard` dans votre liste.

Votre boucle :

```python
for animal in animaux:
    animal.parler()
```

doit fonctionner sans aucune autre modification.

C'est l'un des avantages du polymorphisme.

---

# 🧪 Tester correctement l'héritage

Pour chaque classe enfant, vérifiez :

```text
Les attributs hérités fonctionnent-ils ?
        ↓
Les méthodes héritées fonctionnent-elles ?
        ↓
Les nouveaux attributs fonctionnent-ils ?
        ↓
Les nouvelles méthodes fonctionnent-elles ?
        ↓
Les méthodes redéfinies fonctionnent-elles ?
```

---

# ⚠️ Erreurs fréquentes

## Oublier la classe parente

Incorrect :

```python
class Chien:
```

Correct :

```python
class Chien(Animal):
```

---

## Oublier `super()`

Si la classe enfant possède son propre constructeur :

```python
def __init__(self, nom, age, race):
```

pensez à initialiser les attributs de la classe parente :

```python
super().__init__(nom, age)
```

---

## Réécrire inutilement les attributs

Évitez :

```python
class Chien(Animal):

    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race
```

Préférez :

```python
class Chien(Animal):

    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race
```

---

## Confondre héritage et création d'objet

Ceci crée un objet :

```python
chien = Chien()
```

Ceci crée une relation d'héritage :

```python
class Chien(Animal):
```

---

# 💾 Sauvegarder votre travail

Travaillez progressivement :

```text
Classe parente
      ↓
Test
      ↓
Classe enfant
      ↓
Test
      ↓
super()
      ↓
Test
      ↓
Redéfinition
      ↓
Test
      ↓
Commit
```

Exemples de commits :

```text
Ajoute héritage Animal
```

```text
Ajoute classes Chien et Chat
```

```text
Ajoute polymorphisme
```

```text
Termine séance 05
```

Puis :

1. ouvrez **Source Control** ;
2. vérifiez les fichiers modifiés ;
3. cliquez sur **Commit** ;
4. cliquez sur **Sync Changes**.

---

# ⚠️ Fichiers `corrige`

Vous trouverez également :

```text
seance05_exercice1_corrige.py
seance05_exercice2_corrige.py
seance05_exercice3_corrige.py
seance05_exercice4_corrige.py
```

Travaillez d'abord dans les fichiers sans :

```text
_corrige
```

Cherchez votre propre solution avant de consulter les corrigés.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je comprends le principe de l'héritage ;
- [ ] je sais identifier une classe parente ;
- [ ] je sais identifier une classe enfant ;
- [ ] je sais créer une classe qui hérite d'une autre ;
- [ ] je comprends ce qui est hérité ;
- [ ] je sais utiliser `super()` ;
- [ ] je sais ajouter un attribut spécifique à une classe enfant ;
- [ ] je sais ajouter une méthode spécifique ;
- [ ] je sais redéfinir une méthode ;
- [ ] je comprends le principe du polymorphisme ;
- [ ] je sais utiliser plusieurs objets dans une même boucle ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Créer une hiérarchie simple de classes, réutiliser le code d'une classe parente avec l'héritage et `super()`, puis utiliser le polymorphisme pour obtenir différents comportements avec une même méthode.**

---

# 🔜 Prochaine séance

## Séance 06 — Collections d'objets

Nous savons maintenant créer différents types d'objets :

```text
Livre
Personne
Produit
Animal
Chien
Chat
Employe
Manager
...
```

Lors de la prochaine séance, nous allons apprendre à **gérer plusieurs objets ensemble**.

Par exemple :

```python
livres = [
    Livre("1984", "George Orwell"),
    Livre("Dune", "Frank Herbert"),
    Livre("Fondation", "Isaac Asimov")
]
```

Nous apprendrons notamment à :

```text
stocker plusieurs objets
parcourir une collection
ajouter un objet
rechercher un objet
filtrer des objets
modifier un objet
```

Ces notions nous permettront ensuite de commencer notre **mini-projet POO**.