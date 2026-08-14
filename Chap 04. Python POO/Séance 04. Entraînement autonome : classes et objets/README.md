# 🐍 Python — S7 — Séance 04

## Entraînement autonome : classes et objets

Lors des séances précédentes, nous avons découvert les principales bases de la programmation orientée objet.

Vous savez maintenant utiliser :

```text
class
objets
attributs
méthodes
self
__init__
__str__
```

Cette séance est consacrée à la **mise en pratique autonome** de ces notions.

Il n'y a pas de nouvelle notion importante à apprendre aujourd'hui.

L'objectif est maintenant de réussir à **concevoir vos propres classes à partir d'un énoncé**.

---

# 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- analyser un problème et identifier les objets nécessaires ;
- identifier les attributs d'une classe ;
- identifier les méthodes d'une classe ;
- écrire un constructeur `__init__` ;
- utiliser correctement `self` ;
- créer plusieurs objets ;
- modifier l'état d'un objet avec une méthode ;
- utiliser une méthode qui retourne une valeur ;
- utiliser `__str__` pour afficher un objet ;
- tester une classe de manière autonome.

---

# 1. Avant de programmer

Lorsque vous recevez un exercice de POO, ne commencez pas immédiatement à écrire du code.

Commencez par identifier :

```text
1. La classe
2. Les attributs
3. Les méthodes
4. Les objets à créer
5. Les tests à effectuer
```

---

# 2. Exemple d'analyse

Prenons l'énoncé suivant :

> Créer une classe `Voiture`.  
> Une voiture possède une marque, un modèle et une vitesse.  
> Elle peut accélérer et freiner.

Nous pouvons identifier :

```text
Classe
└── Voiture

Attributs
├── marque
├── modele
└── vitesse

Méthodes
├── accelerer()
└── freiner()
```

Nous pouvons alors commencer à programmer.

---

# 3. Construire la classe

```python
class Voiture:

    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.vitesse = 0
```

Puis créer un objet :

```python
v1 = Voiture("Toyota", "Corolla")
```

---

# 4. Ajouter les comportements

Nous pouvons maintenant ajouter les méthodes :

```python
def accelerer(self, valeur):
    self.vitesse += valeur
```

et :

```python
def freiner(self, valeur):
    self.vitesse -= valeur
```

Mais cette deuxième méthode pose un problème.

Si :

```text
vitesse = 20
```

et que nous faisons :

```python
v1.freiner(50)
```

nous obtenons :

```text
-30 km/h
```

Ce résultat n'est pas logique.

Nous devons donc améliorer notre méthode.

---

# 5. Ajouter des règles

Une méthode peut contenir des conditions :

```python
def freiner(self, valeur):

    self.vitesse -= valeur

    if self.vitesse < 0:
        self.vitesse = 0
```

Nous pouvons ainsi contrôler la manière dont l'état de l'objet est modifié.

C'est un des intérêts de la programmation orientée objet.

---

# 6. Méthodes qui retournent une valeur

Une méthode ne doit pas toujours utiliser `print()`.

Elle peut également retourner une valeur.

Exemple :

```python
class Rectangle:

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
```

Nous pouvons ensuite écrire :

```python
r = Rectangle(4, 5)

resultat = r.aire()

print(resultat)
```

---

# 7. Réutiliser une méthode dans une autre méthode

Une méthode peut appeler une autre méthode de la même classe.

Exemple :

```python
class Etudiant:

    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def admis(self):
        return self.moyenne() >= 10
```

Dans :

```python
self.moyenne()
```

nous appelons la méthode `moyenne()` de l'objet courant.

Cela évite de refaire le même calcul plusieurs fois.

---

# 8. Utiliser `__str__`

Pour rendre un objet facilement lisible :

```python
def __str__(self):
    return f"{self.nom} : moyenne = {self.moyenne():.1f}"
```

Nous pouvons ensuite écrire :

```python
print(etudiant)
```

au lieu de construire manuellement l'affichage à chaque fois.

---

# 🧠 Méthode de travail

Pour chaque exercice de cette séance, utilisez cette méthode :

```text
LIRE L'ÉNONCÉ
      ↓
IDENTIFIER LA CLASSE
      ↓
IDENTIFIER LES ATTRIBUTS
      ↓
IDENTIFIER LES MÉTHODES
      ↓
ÉCRIRE __init__
      ↓
CRÉER UN OBJET
      ↓
TESTER
      ↓
AJOUTER UNE MÉTHODE
      ↓
TESTER
      ↓
CONTINUER
```

Ne programmez pas toute la classe avant de commencer les tests.

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Travaillez dans :

```text
seance04_exercice1.py
seance04_exercice2.py
seance04_exercice3.py
seance04_exercice4.py
```

Ne modifiez pas le nom des fichiers.

---

# Exercice 1 — Classe `Etudiant`

📄 Fichier :

```text
seance04_exercice1.py
```

Créez une classe :

```python
Etudiant
```

Un étudiant possède :

```text
nom
notes
```

`notes` est une liste contenant plusieurs notes.

Exemple :

```python
e1 = Etudiant(
    "Alice",
    [12, 15, 9, 18]
)
```

---

## Méthode `moyenne()`

Ajoutez :

```python
moyenne()
```

qui calcule et **retourne** la moyenne des notes.

Vous pouvez utiliser :

```python
sum()
```

et :

```python
len()
```

Exemple :

```python
print(e1.moyenne())
```

---

## Méthode `admis()`

Ajoutez :

```python
admis()
```

qui retourne :

```python
True
```

si la moyenne est supérieure ou égale à `10`.

Sinon, elle retourne :

```python
False
```

Essayez de réutiliser :

```python
self.moyenne()
```

dans cette méthode.

---

## Méthode `__str__`

Ajoutez un affichage permettant d'obtenir par exemple :

```text
Alice — moyenne : 13.5 — admis
```

---

## Tests

Créez au moins **3 étudiants** :

```text
un étudiant avec une moyenne > 10
un étudiant avec une moyenne = 10
un étudiant avec une moyenne < 10
```

Vérifiez le résultat de :

```python
moyenne()
```

et :

```python
admis()
```

---

# Exercice 2 — Classe `Voiture`

📄 Fichier :

```text
seance04_exercice2.py
```

Créez une classe :

```python
Voiture
```

avec les attributs :

```text
marque
modele
vitesse
```

Lors de la création d'une voiture :

```text
vitesse = 0
```

On doit donc pouvoir écrire :

```python
v1 = Voiture("Toyota", "Corolla")
```

---

## Méthode `accelerer()`

Ajoutez :

```python
accelerer(valeur)
```

qui augmente la vitesse.

Exemple :

```python
v1.accelerer(20)
v1.accelerer(30)
```

La vitesse doit devenir :

```text
50 km/h
```

---

## Méthode `freiner()`

Ajoutez :

```python
freiner(valeur)
```

qui diminue la vitesse.

⚠️ La vitesse ne doit **jamais devenir négative**.

Par exemple :

```text
vitesse = 30 km/h

freiner(100)

→ vitesse = 0 km/h
```

et non :

```text
-70 km/h
```

---

## Méthode `__str__`

Ajoutez un affichage permettant par exemple :

```text
Toyota Corolla — 50 km/h
```

---

## Tests

Testez la séquence suivante :

```text
Départ        → 0 km/h
Accélérer 50  → 50 km/h
Accélérer 30  → 80 km/h
Freiner 20    → 60 km/h
Freiner 100   → 0 km/h
```

---

# Exercice 3 — Classe `Produit`

📄 Fichier :

```text
seance04_exercice3.py
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

Exemple :

```python
p1 = Produit(
    "Clavier",
    49.90,
    10
)
```

---

## Méthode `vendre()`

Ajoutez :

```python
vendre(qte)
```

qui diminue le stock.

Exemple :

```python
p1.vendre(3)
```

fait passer le stock de :

```text
10
```

à :

```text
7
```

---

## Stock insuffisant

Il ne doit pas être possible de vendre plus de produits qu'il n'en reste.

Si :

```text
stock = 7
```

et que l'on demande :

```python
p1.vendre(10)
```

le programme doit afficher :

```text
Stock insuffisant
```

Le stock doit rester égal à :

```text
7
```

---

## Méthode `restocker()`

Ajoutez :

```python
restocker(qte)
```

qui augmente le stock.

Exemple :

```python
p1.restocker(5)
```

Si le stock était de `7`, il devient :

```text
12
```

---

## Méthode `__str__`

Ajoutez un affichage permettant par exemple :

```text
Clavier — 49.90 EUR — stock : 12
```

---

# Exercice 4 — Classe `Rectangle`

📄 Fichier :

```text
seance04_exercice4.py
```

Créez une classe :

```python
Rectangle
```

avec :

```text
largeur
hauteur
```

---

## Méthode `aire()`

Ajoutez :

```python
aire()
```

qui retourne :

```text
largeur × hauteur
```

---

## Méthode `perimetre()`

Ajoutez :

```python
perimetre()
```

qui retourne :

```text
2 × (largeur + hauteur)
```

---

## Méthode `est_carre()`

Ajoutez :

```python
est_carre()
```

qui retourne :

```python
True
```

si :

```text
largeur == hauteur
```

et :

```python
False
```

sinon.

---

## Méthode `__str__`

Pour :

```python
r = Rectangle(4, 5)
```

vous devez pouvoir obtenir :

```text
Rectangle 4 x 5 — aire : 20 — périmètre : 18
```

---

# ⭐ Défi — Validation des données

Améliorez vos classes afin d'empêcher certaines opérations incorrectes.

Par exemple :

### Voiture

```python
v1.accelerer(-50)
```

ne doit pas faire diminuer la vitesse.

### Produit

```python
p1.vendre(-5)
```

ne doit pas augmenter le stock.

Et :

```python
p1.restocker(-10)
```

ne doit pas diminuer le stock.

### Rectangle

Une largeur ou une hauteur négative n'a pas de sens.

Réfléchissez aux vérifications nécessaires.

---

# 🧪 Tester correctement une classe

Pour chaque classe, ne testez pas uniquement un cas.

Testez :

```text
CAS NORMAL
CAS LIMITE
CAS INCORRECT
```

Par exemple pour `Voiture` :

```python
v = Voiture("Toyota", "Corolla")

v.accelerer(50)   # cas normal
v.freiner(50)     # vitesse exactement égale à 0
v.freiner(100)    # ne doit pas devenir négative
```

---

# ⚠️ Erreurs fréquentes

## Oublier `self`

Incorrect :

```python
def accelerer(valeur):
```

Correct :

```python
def accelerer(self, valeur):
```

---

## Oublier `self.` devant un attribut

Incorrect :

```python
vitesse += valeur
```

Correct :

```python
self.vitesse += valeur
```

---

## Confondre `print()` et `return`

Si une méthode doit **calculer une valeur**, utilisez généralement :

```python
return
```

Par exemple :

```python
def aire(self):
    return self.largeur * self.hauteur
```

Le programme principal peut ensuite décider quoi faire avec cette valeur :

```python
print(r.aire())
```

---

## Répéter inutilement un calcul

Si vous avez déjà :

```python
def moyenne(self):
    ...
```

dans `admis()`, préférez :

```python
return self.moyenne() >= 10
```

plutôt que de recalculer toute la moyenne.

---

# 🚀 Exécuter les exercices

Dans le terminal :

```bash
python seance04_exercice1.py
```

```bash
python seance04_exercice2.py
```

```bash
python seance04_exercice3.py
```

```bash
python seance04_exercice4.py
```

---

# 💾 Sauvegarder votre travail

Travaillez progressivement.

Par exemple :

```text
Constructeur
    ↓
Test
    ↓
Première méthode
    ↓
Test
    ↓
Deuxième méthode
    ↓
Test
    ↓
Commit
```

Exemples de commits :

```text
Termine classe Etudiant
```

```text
Ajoute accelerer et freiner
```

```text
Termine classe Produit
```

```text
Termine séance 04
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
seance04_exercice1_corrige.py
seance04_exercice2_corrige.py
seance04_exercice3_corrige.py
seance04_exercice4_corrige.py
```

Travaillez d'abord dans les fichiers sans :

```text
_corrige
```

N'utilisez le corrigé qu'après avoir réellement essayé de résoudre l'exercice.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je sais analyser un énoncé POO ;
- [ ] je sais identifier une classe ;
- [ ] je sais identifier les attributs nécessaires ;
- [ ] je sais identifier les méthodes nécessaires ;
- [ ] je sais écrire `__init__` sans modèle ;
- [ ] j'utilise correctement `self` ;
- [ ] je sais créer plusieurs objets ;
- [ ] je sais écrire une méthode qui modifie un objet ;
- [ ] je sais écrire une méthode qui retourne une valeur ;
- [ ] je sais réutiliser une méthode avec `self.methode()` ;
- [ ] je sais utiliser `__str__` ;
- [ ] j'ai testé plusieurs situations ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Concevoir de manière autonome une classe comportant plusieurs attributs et plusieurs méthodes, puis tester son comportement avec plusieurs objets.**

---

# 🔜 Prochaine séance

## Séance 05 — Héritage et polymorphisme

Jusqu'à présent, nos classes sont indépendantes.

Lors de la prochaine séance, nous verrons comment créer une classe à partir d'une autre classe.

Par exemple :

```text
        Animal
        /    \
       /      \
    Chien     Chat
```

Nous découvrirons :

```text
classe parente
classe enfant
héritage
super()
redéfinition de méthode
polymorphisme
```

Nous pourrons ainsi **réutiliser du code** et créer des relations entre nos classes.