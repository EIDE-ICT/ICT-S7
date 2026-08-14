# 🐍 Python — S7 — Séance 03

## Constructeurs, encapsulation et méthodes spéciales

Lors de la séance précédente, nous avons découvert les premières notions de programmation orientée objet :

- les classes ;
- les objets ;
- les attributs ;
- les méthodes ;
- `self`.

Nous allons maintenant améliorer nos classes afin de créer des objets plus facilement et de mieux organiser leurs données.

---

# 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- comprendre le rôle du constructeur `__init__` ;
- initialiser les attributs lors de la création d'un objet ;
- utiliser des paramètres dans `__init__` ;
- utiliser une valeur par défaut ;
- comprendre le principe d'encapsulation ;
- comprendre la convention `_attribut` ;
- utiliser la méthode spéciale `__str__` ;
- afficher proprement un objet avec `print()`.

---

# 1. Le problème de la séance précédente

Lors de la séance 02, nous créions un objet ainsi :

```python
p1 = Personne()

p1.nom = "Alice"
p1.age = 17
```

Cela fonctionne, mais cette méthode présente plusieurs problèmes.

Nous pouvons par exemple oublier un attribut :

```python
p2 = Personne()

p2.nom = "Tom"

# Nous avons oublié p2.age !
```

Nous aimerions pouvoir créer directement une personne complète :

```python
p2 = Personne("Tom", 16)
```

C'est précisément le rôle du **constructeur**.

---

# 2. Le constructeur `__init__`

`__init__` est une méthode spéciale appelée automatiquement lors de la création d'un objet.

```python
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Nous pouvons maintenant créer une personne directement :

```python
p1 = Personne("Alice", 17)
```

Python appelle automatiquement :

```python
__init__
```

avec les valeurs :

```text
nom → "Alice"
age → 17
```

L'objet obtenu contient :

```text
p1
│
├── nom → "Alice"
└── age → 17
```

---

# 3. Comprendre `self.nom = nom`

Regardons cette instruction :

```python
self.nom = nom
```

Les deux `nom` n'ont pas le même rôle.

Dans :

```python
def __init__(self, nom, age):
```

`nom` est un **paramètre** reçu par le constructeur.

Dans :

```python
self.nom
```

`nom` est un **attribut de l'objet**.

Ainsi :

```python
self.nom = nom
```

signifie :

> Stocker la valeur reçue dans l'attribut `nom` de cet objet.

Même principe pour :

```python
self.age = age
```

---

# 4. Créer plusieurs objets

Une même classe permet de créer plusieurs objets indépendants :

```python
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


p1 = Personne("Alice", 17)
p2 = Personne("Tom", 16)
p3 = Personne("Nora", 18)
```

Chaque objet possède ses propres données :

```text
Personne
│
├── p1
│   ├── nom → Alice
│   └── age → 17
│
├── p2
│   ├── nom → Tom
│   └── age → 16
│
└── p3
    ├── nom → Nora
    └── age → 18
```

---

# 5. Paramètres avec une valeur par défaut

Un constructeur peut avoir des paramètres possédant une valeur par défaut.

Exemple :

```python
class Compte:

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
```

Nous pouvons écrire :

```python
c1 = Compte("Alice", 100)
```

Le solde vaut :

```text
100
```

Mais nous pouvons également écrire :

```python
c2 = Compte("Tom")
```

Comme aucun solde n'est indiqué, Python utilise automatiquement :

```text
solde = 0
```

---

# 6. Encapsulation

Une classe ne contient pas seulement des données.

Elle peut également contrôler **la manière dont ces données sont utilisées et modifiées**.

Prenons un compte bancaire :

```python
class CompteBancaire:

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde
```

Vous remarquez :

```python
_solde
```

et non simplement :

```python
solde
```

---

# 7. Pourquoi `_solde` ?

En Python, un attribut commençant par `_` indique par convention :

> ⚠️ Cet attribut est destiné principalement à être utilisé à l'intérieur de la classe.

Il vaut donc mieux éviter de faire directement :

```python
compte._solde = 1000000
```

On préfère modifier le solde avec des méthodes prévues pour cela.

Par exemple :

```python
compte.deposer(100)
```

---

# 8. Contrôler les modifications avec des méthodes

Nous pouvons créer une méthode :

```python
def deposer(self, montant):
    self._solde += montant
```

et :

```python
def retirer(self, montant):

    if montant <= self._solde:
        self._solde -= montant
    else:
        print("Solde insuffisant")
```

La classe devient :

```python
class CompteBancaire:

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde

    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant
        else:
            print("Solde insuffisant")
```

Utilisation :

```python
compte = CompteBancaire("Alice", 100)

compte.deposer(50)
compte.retirer(30)
```

Le solde vaut maintenant :

```text
120
```

---

# 9. Le problème de `print(objet)`

Créons un objet :

```python
compte = CompteBancaire("Alice", 100)
```

Puis essayons :

```python
print(compte)
```

Sans configuration particulière, Python affiche quelque chose ressemblant à :

```text
<__main__.CompteBancaire object at 0x...>
```

Ce n'est pas très lisible.

Nous pouvons améliorer cet affichage grâce à :

```python
__str__
```

---

# 10. La méthode spéciale `__str__`

`__str__` permet de définir la représentation textuelle d'un objet.

```python
def __str__(self):
    return f"Compte de {self.titulaire} : {self._solde} EUR"
```

La classe complète devient :

```python
class CompteBancaire:

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde

    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant
        else:
            print("Solde insuffisant")

    def __str__(self):
        return f"Compte de {self.titulaire} : {self._solde} EUR"
```

Nous pouvons maintenant écrire :

```python
compte = CompteBancaire("Alice", 100)

compte.deposer(50)
compte.retirer(30)

print(compte)
```

Résultat :

```text
Compte de Alice : 120 EUR
```

---

# 11. Pourquoi `return` dans `__str__` ?

Attention :

```python
__str__
```

doit **retourner une chaîne de caractères**.

Correct :

```python
def __str__(self):
    return f"{self.nom} — {self.age} ans"
```

Incorrect :

```python
def __str__(self):
    print(f"{self.nom} — {self.age} ans")
```

`__str__` doit donc utiliser :

```python
return
```

---

# 🧠 À retenir

## Constructeur

```python
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Création :

```python
p1 = Personne("Alice", 17)
```

---

## Valeur par défaut

```python
def __init__(self, nom, solde=0):
```

permet :

```python
Compte("Alice", 100)
```

mais également :

```python
Compte("Alice")
```

---

## Convention `_attribut`

```python
self._solde
```

indique qu'un attribut est destiné principalement à être manipulé depuis la classe.

---

## Méthode spéciale `__str__`

```python
def __str__(self):
    return "..."
```

permet ensuite :

```python
print(objet)
```

---

# 🔍 Vocabulaire

| Terme | Signification |
|---|---|
| `__init__` | Constructeur de la classe |
| Paramètre | Valeur reçue par une méthode |
| Attribut | Donnée appartenant à un objet |
| Encapsulation | Regroupement et contrôle des données dans une classe |
| `_attribut` | Convention indiquant un usage interne |
| `__str__` | Définit la représentation textuelle d'un objet |

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Travaillez dans :

```text
seance03_exercice1.py
seance03_exercice2.py
seance03_exercice3.py
seance03_exercice4.py
```

Ne modifiez pas le nom des fichiers.

---

# Exercice 1 — `Personne` avec constructeur

📄 Fichier :

```text
seance03_exercice1.py
```

Reprenez la classe :

```python
Personne
```

Mais cette fois, utilisez un constructeur :

```python
__init__
```

pour initialiser :

```text
nom
age
```

Vous devez pouvoir écrire :

```python
p1 = Personne("Alice", 17)
p2 = Personne("Tom", 16)
```

Ajoutez également :

```python
__str__
```

afin que :

```python
print(p1)
```

affiche :

```text
Alice — 17 ans
```

---

# Exercice 2 — Classe `Livre`

📄 Fichier :

```text
seance03_exercice2.py
```

Créez une classe :

```python
Livre
```

avec les attributs :

```text
titre
auteur
nb_pages
```

Ces attributs doivent être initialisés dans :

```python
__init__
```

Vous devez pouvoir écrire :

```python
livre = Livre(
    "1984",
    "George Orwell",
    328
)
```

Ajoutez :

```python
__str__
```

afin que :

```python
print(livre)
```

affiche :

```text
1984 par George Orwell (328 pages)
```

---

# Exercice 3 — Classe `Rectangle`

📄 Fichier :

```text
seance03_exercice3.py
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

Ajoutez une méthode :

```python
aire()
```

qui retourne l'aire du rectangle.

Rappel :

```text
aire = largeur × hauteur
```

Exemple :

```python
r = Rectangle(4, 5)

print(r.aire())
```

Résultat :

```text
20
```

Ajoutez ensuite :

```python
__str__()
```

afin que :

```python
print(r)
```

affiche :

```text
Rectangle 4 x 5 — aire : 20
```

---

# Exercice 4 — `CompteBancaire`

📄 Fichier :

```text
seance03_exercice4.py
```

Créez une classe :

```python
CompteBancaire
```

avec :

```text
titulaire
_solde
```

Le constructeur doit permettre :

```python
c1 = CompteBancaire("Alice", 100)
```

mais également :

```python
c2 = CompteBancaire("Tom")
```

Dans ce deuxième cas :

```text
_solde = 0
```

---

## Méthode `deposer()`

Ajoutez :

```python
deposer(montant)
```

qui augmente le solde.

---

## Méthode `retirer()`

Ajoutez :

```python
retirer(montant)
```

qui diminue le solde uniquement si le montant disponible est suffisant.

Sinon, affichez :

```text
Solde insuffisant
```

---

## Méthode `__str__`

Ajoutez :

```python
__str__()
```

afin que :

```python
print(c1)
```

affiche par exemple :

```text
Compte de Alice : 120 EUR
```

---

# ⭐ Défi

Améliorez `CompteBancaire` afin de refuser :

```python
compte.deposer(-100)
```

et :

```python
compte.retirer(-50)
```

Un montant négatif ne doit jamais permettre de modifier le solde.

---

# 🚀 Exécuter les exercices

Dans le terminal :

```bash
python seance03_exercice1.py
```

```bash
python seance03_exercice2.py
```

```bash
python seance03_exercice3.py
```

```bash
python seance03_exercice4.py
```

---

# ⚠️ Erreurs fréquentes

## Oublier `self`

Incorrect :

```python
def __init__(nom, age):
```

Correct :

```python
def __init__(self, nom, age):
```

---

## Oublier `self.`

Incorrect :

```python
def __init__(self, nom):
    nom = nom
```

Correct :

```python
def __init__(self, nom):
    self.nom = nom
```

---

## Oublier un argument

Si le constructeur est :

```python
def __init__(self, nom, age):
```

alors ceci est incorrect :

```python
p1 = Personne("Alice")
```

Python attend également une valeur pour :

```text
age
```

---

## Utiliser `print()` dans `__str__`

Incorrect :

```python
def __str__(self):
    print(self.nom)
```

Correct :

```python
def __str__(self):
    return self.nom
```

---

# 💾 Sauvegarder votre travail

Après chaque exercice fonctionnel :

1. ouvrez **Source Control** ;
2. vérifiez les fichiers modifiés ;
3. écrivez un message de commit ;
4. cliquez sur **Commit** ;
5. cliquez sur **Sync Changes**.

Exemples :

```text
Ajoute constructeur Personne
```

```text
Termine classe Rectangle
```

```text
Termine séance 03
```

---

# ⚠️ Fichiers `corrige`

Vous trouverez également :

```text
seance03_exercice1_corrige.py
seance03_exercice2_corrige.py
seance03_exercice3_corrige.py
seance03_exercice4_corrige.py
```

Travaillez d'abord dans les fichiers sans :

```text
_corrige
```

Cherchez votre propre solution avant de consulter les corrigés.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je comprends le rôle de `__init__` ;
- [ ] je sais utiliser des paramètres dans `__init__` ;
- [ ] je comprends `self.attribut = parametre` ;
- [ ] je sais utiliser une valeur par défaut ;
- [ ] je comprends le principe d'encapsulation ;
- [ ] je comprends la convention `_attribut` ;
- [ ] je sais créer `__str__` ;
- [ ] je sais utiliser `return` dans `__str__` ;
- [ ] je sais afficher un objet avec `print()` ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Créer une classe utilisant `__init__`, initialiser correctement ses attributs et définir son affichage avec `__str__`.**

---

# 🔜 Prochaine séance

## Séance 04 — Entraînement autonome : classes et objets

Lors de la prochaine séance, nous n'introduirons pas une nouvelle notion importante.

Vous devrez utiliser de manière plus autonome ce que nous avons appris :

```text
class
self
__init__
attributs
méthodes
__str__
```

Vous travaillerez notamment avec différentes classes telles que :

```text
Etudiant
Voiture
Produit
```

🎯 L'objectif sera de passer progressivement de :

> **« Je sais suivre un exemple »**

à :

> **« Je sais concevoir une classe moi-même. »**