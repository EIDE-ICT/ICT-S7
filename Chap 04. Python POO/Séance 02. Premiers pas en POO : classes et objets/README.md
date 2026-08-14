# 🐍 Python — S7 — Séance 02

## Premiers pas en POO : classes et objets

Lors de la séance précédente, nous avons révisé les principales notions de Python étudiées en S6.

Nous allons maintenant découvrir une nouvelle manière d'organiser nos programmes : la **programmation orientée objet (POO)**.

Nous allons apprendre à créer nos propres types d'objets possédant :

- des **attributs** : les données de l'objet ;
- des **méthodes** : les actions que l'objet peut effectuer.

---

# 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- expliquer ce qu'est une **classe** ;
- expliquer ce qu'est un **objet** ;
- distinguer une classe d'une instance ;
- créer une classe simple ;
- créer plusieurs objets à partir d'une classe ;
- ajouter des attributs à un objet ;
- créer une méthode ;
- comprendre le rôle de `self` ;
- appeler une méthode sur un objet.

---

# 1. Pourquoi la programmation orientée objet ?

Jusqu'à présent, nos programmes étaient principalement organisés autour :

- de variables ;
- de listes ;
- de fonctions.

Par exemple, pour représenter une personne :

```python
nom = "Alice"
age = 17
```

Pour une deuxième personne :

```python
nom2 = "Tom"
age2 = 16
```

Avec beaucoup de personnes, cette organisation devient rapidement difficile à gérer.

Nous aimerions pouvoir regrouper les informations :

```text
Personne
│
├── nom
└── age
```

C'est l'un des objectifs de la programmation orientée objet.

---

# 2. Qu'est-ce qu'une classe ?

Une **classe** est un modèle permettant de créer des objets.

On peut comparer une classe à un plan de construction.

```text
        CLASSE
       Personne
          │
          │ permet de créer
          ▼
       des objets
```

En Python :

```python
class Personne:
    pass
```

Nous venons de créer une classe appelée :

```text
Personne
```

`pass` signifie simplement :

> Il n'y a encore aucune instruction dans cette classe.

---

# 3. Qu'est-ce qu'un objet ?

Un **objet** est une instance d'une classe.

À partir de :

```python
class Personne:
    pass
```

nous pouvons créer un objet :

```python
p1 = Personne()
```

`p1` est maintenant un objet de type `Personne`.

Nous pouvons vérifier son type :

```python
print(type(p1))
```

---

# 4. Une classe peut créer plusieurs objets

Une même classe peut être utilisée pour créer autant d'objets que nécessaire.

```python
class Personne:
    pass


p1 = Personne()
p2 = Personne()
p3 = Personne()
```

Nous avons maintenant :

```text
          Personne
          /   |   \
         /    |    \
       p1     p2     p3
```

`p1`, `p2` et `p3` sont trois objets différents.

---

# 5. Les attributs

Un **attribut** est une information appartenant à un objet.

Nous pouvons par exemple donner un nom à `p1` :

```python
p1.nom = "Alice"
```

et un âge :

```python
p1.age = 17
```

Notre objet peut être représenté ainsi :

```text
p1
│
├── nom → "Alice"
└── age → 17
```

---

# 6. Accéder à un attribut

Pour accéder à un attribut, nous utilisons :

```text
objet.attribut
```

Par exemple :

```python
print(p1.nom)
print(p1.age)
```

Résultat :

```text
Alice
17
```

---

# 7. Chaque objet possède ses propres attributs

Créons deux personnes :

```python
p1 = Personne()
p1.nom = "Alice"
p1.age = 17

p2 = Personne()
p2.nom = "Tom"
p2.age = 16
```

Nous obtenons :

```text
Personne
│
├── p1
│   ├── nom → Alice
│   └── age → 17
│
└── p2
    ├── nom → Tom
    └── age → 16
```

Modifier `p1` ne modifie pas `p2`.

Les deux objets sont indépendants.

---

# 8. Modifier un attribut

Un attribut peut être modifié comme une variable.

```python
p1.age = 18
```

Nous pouvons également écrire :

```python
p1.age = p1.age + 1
```

ou :

```python
p1.age += 1
```

---

# 9. Les méthodes

Une classe peut également contenir des **méthodes**.

Une méthode est une fonction qui appartient à une classe.

Exemple :

```python
class Personne:

    def dire_bonjour(self):
        print("Bonjour !")
```

Nous pouvons maintenant écrire :

```python
p1 = Personne()

p1.dire_bonjour()
```

Résultat :

```text
Bonjour !
```

---

# 10. Le rôle de `self`

Vous avez certainement remarqué :

```python
def dire_bonjour(self):
```

`self` représente **l'objet qui utilise la méthode**.

Prenons :

```python
p1.dire_bonjour()
```

Dans cette méthode :

```python
self
```

représente :

```text
p1
```

Si nous écrivons :

```python
p2.dire_bonjour()
```

alors `self` représente `p2`.

---

# 11. Utiliser les attributs dans une méthode

Grâce à `self`, une méthode peut accéder aux attributs de l'objet.

```python
class Personne:

    def dire_bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")
```

Puis :

```python
p1 = Personne()
p1.nom = "Alice"

p1.dire_bonjour()
```

Résultat :

```text
Bonjour, je m'appelle Alice.
```

---

# 12. Pourquoi `self.nom` ?

Dans une méthode :

```python
self.nom
```

signifie :

> l'attribut `nom` de l'objet qui utilise actuellement cette méthode.

Par exemple :

```python
p1.nom = "Alice"
p2.nom = "Tom"
```

Puis :

```python
p1.dire_bonjour()
p2.dire_bonjour()
```

Résultat :

```text
Bonjour, je m'appelle Alice.
Bonjour, je m'appelle Tom.
```

La même méthode produit donc un résultat différent selon l'objet.

---

# 13. Méthode avec un paramètre

Une méthode peut recevoir d'autres paramètres en plus de `self`.

Exemple :

```python
class Personne:

    def anniversaire(self):
        self.age += 1

    def changer_nom(self, nouveau_nom):
        self.nom = nouveau_nom
```

Utilisation :

```python
p1.changer_nom("Alicia")
```

Ici :

```text
self        → p1
nouveau_nom → "Alicia"
```

---

# 14. Exemple complet

```python
class Personne:

    def dire_bonjour(self):
        print(
            f"Bonjour, je m'appelle {self.nom} "
            f"et j'ai {self.age} ans."
        )

    def anniversaire(self):
        self.age += 1


p1 = Personne()

p1.nom = "Alice"
p1.age = 17

p1.dire_bonjour()

p1.anniversaire()

p1.dire_bonjour()
```

Résultat :

```text
Bonjour, je m'appelle Alice et j'ai 17 ans.
Bonjour, je m'appelle Alice et j'ai 18 ans.
```

---

# 🧠 À retenir

## Une classe

Une classe est un modèle :

```python
class Personne:
    ...
```

---

## Un objet

Un objet est créé à partir d'une classe :

```python
p1 = Personne()
```

---

## Un attribut

Un attribut contient une information :

```python
p1.nom = "Alice"
```

On y accède avec :

```python
p1.nom
```

---

## Une méthode

Une méthode représente un comportement :

```python
def dire_bonjour(self):
    ...
```

On l'appelle avec :

```python
p1.dire_bonjour()
```

---

## `self`

`self` représente l'objet qui utilise la méthode.

```python
self.nom
self.age
```

permettent d'accéder aux attributs de cet objet.

---

# 🔍 Vocabulaire

| Terme | Signification |
|---|---|
| **Classe** | Modèle permettant de créer des objets |
| **Objet** | Instance d'une classe |
| **Instance** | Objet créé à partir d'une classe |
| **Attribut** | Donnée appartenant à un objet |
| **Méthode** | Fonction appartenant à une classe |
| **self** | Référence vers l'objet courant |

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Travaillez dans les fichiers :

```text
seance02_exercice1.py
seance02_exercice2.py
seance02_exercice3.py
seance02_exercice4.py
```

Ne modifiez pas le nom des fichiers.

---

# Exercice 1 — `Personne`

📄 Fichier :

```text
seance02_exercice1.py
```

Créez une classe :

```python
Personne
```

Puis créez deux objets :

```python
p1
p2
```

Ajoutez à chaque personne :

```text
nom
age
```

Par exemple :

```python
p1 = Personne()
p1.nom = "Alice"
p1.age = 17
```

Affichez ensuite les informations des deux personnes.

---

## Résultat possible

```text
Alice a 17 ans.
Tom a 16 ans.
```

---

# Exercice 2 — Ajouter une méthode

📄 Fichier :

```text
seance02_exercice2.py
```

Créez une classe :

```python
Personne
```

avec une méthode :

```python
se_presenter()
```

La méthode doit utiliser :

```python
self.nom
self.age
```

pour afficher par exemple :

```text
Je m'appelle Alice et j'ai 17 ans.
```

Créez plusieurs personnes et appelez :

```python
p1.se_presenter()
p2.se_presenter()
```

---

# Exercice 3 — Classe `Livre`

📄 Fichier :

```text
seance02_exercice3.py
```

Créez une classe :

```python
Livre
```

Chaque livre possède :

```text
titre
auteur
nb_pages
```

Créez plusieurs livres.

Par exemple :

```python
l1 = Livre()

l1.titre = "1984"
l1.auteur = "George Orwell"
l1.nb_pages = 328
```

Ajoutez une méthode :

```python
afficher_infos()
```

qui affiche par exemple :

```text
1984 — George Orwell — 328 pages
```

Testez la méthode avec plusieurs livres.

---

# Exercice 4 — Classe `Compte`

📄 Fichier :

```text
seance02_exercice4.py
```

Créez une classe :

```python
Compte
```

Chaque compte possède :

```text
titulaire
solde
```

Ajoutez une méthode :

```python
deposer(montant)
```

qui augmente le solde.

Ajoutez également :

```python
retirer(montant)
```

qui diminue le solde.

---

## Exemple

```python
c1 = Compte()

c1.titulaire = "Alice"
c1.solde = 100

c1.deposer(50)

print(c1.solde)
```

Résultat :

```text
150
```

Puis :

```python
c1.retirer(30)

print(c1.solde)
```

Résultat :

```text
120
```

---

# ⭐ Défi

Améliorez la méthode :

```python
retirer(montant)
```

pour empêcher un retrait supérieur au solde disponible.

Par exemple, si :

```text
solde = 120
```

et que l'on demande :

```python
c1.retirer(200)
```

le programme doit afficher :

```text
Solde insuffisant
```

et le solde doit rester égal à :

```text
120
```

---

# 🚀 Exécuter les exercices

Dans le terminal :

```bash
python seance02_exercice1.py
```

puis :

```bash
python seance02_exercice2.py
```

```bash
python seance02_exercice3.py
```

```bash
python seance02_exercice4.py
```

---

# 🧪 Testez plusieurs objets

Ne testez pas vos classes avec un seul objet.

Par exemple :

```python
p1 = Personne()
p2 = Personne()
p3 = Personne()
```

Donnez des valeurs différentes à chaque objet.

L'objectif est de vérifier que les objets sont **indépendants**.

---

# ⚠️ Erreurs fréquentes

## Oublier `self`

Incorrect :

```python
def dire_bonjour():
    print("Bonjour")
```

Correct :

```python
def dire_bonjour(self):
    print("Bonjour")
```

---

## Oublier `self.` devant un attribut

Incorrect :

```python
def se_presenter(self):
    print(nom)
```

Correct :

```python
def se_presenter(self):
    print(self.nom)
```

---

## Oublier les parenthèses lors de la création

Incorrect :

```python
p1 = Personne
```

Correct :

```python
p1 = Personne()
```

---

## Confondre classe et objet

```python
Personne
```

est la **classe**.

```python
p1
```

est un **objet** créé à partir de cette classe.

---

# 💾 Sauvegarder votre travail

Après chaque exercice fonctionnel :

1. ouvrez **Source Control** ;
2. vérifiez les fichiers modifiés ;
3. ajoutez un message de commit ;
4. cliquez sur **Commit** ;
5. cliquez sur **Sync Changes**.

Exemples :

```text
Termine exercice Personne
```

```text
Ajoute classe Livre
```

```text
Termine séance 02
```

---

# ⚠️ Fichiers `corrige`

Vous trouverez également :

```text
seance02_exercice1_corrige.py
seance02_exercice2_corrige.py
...
```

Ces fichiers contiennent les corrigés.

Travaillez d'abord dans :

```text
seance02_exercice1.py
```

et cherchez votre propre solution.

N'utilisez le corrigé qu'après avoir réellement essayé.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je sais expliquer ce qu'est une classe ;
- [ ] je sais expliquer ce qu'est un objet ;
- [ ] je comprends le terme « instance » ;
- [ ] je sais créer une classe ;
- [ ] je sais créer plusieurs objets ;
- [ ] je sais ajouter des attributs à un objet ;
- [ ] je sais accéder à un attribut ;
- [ ] je sais créer une méthode ;
- [ ] je comprends le rôle de `self` ;
- [ ] je sais utiliser `self.attribut` ;
- [ ] je sais appeler une méthode ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Créer une classe simple, instancier plusieurs objets, leur attribuer des données et créer des méthodes utilisant `self`.**

---

# 🔜 Prochaine séance

## Séance 03 — Constructeurs, encapsulation et méthodes spéciales

Pour l'instant, nous créons un objet puis nous ajoutons ses attributs :

```python
p1 = Personne()

p1.nom = "Alice"
p1.age = 17
```

Lors de la prochaine séance, nous apprendrons à écrire directement :

```python
p1 = Personne("Alice", 17)
```

Nous découvrirons notamment :

```text
__init__
self
paramètres
encapsulation
_attribut
__str__
```

🐍 Nos classes vont devenir plus structurées et plus pratiques à utiliser.