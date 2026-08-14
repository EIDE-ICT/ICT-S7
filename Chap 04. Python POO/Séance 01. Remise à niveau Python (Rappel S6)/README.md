# 🐍 Python — S7 — Séance 01

## Remise à niveau Python — Rappel S6

Cette première séance permet de revoir les principales notions de Python étudiées en S6 avant de commencer la **programmation orientée objet (POO)**.

Vous allez réutiliser :

- les variables ;
- les types de données ;
- les conditions ;
- les boucles ;
- les listes ;
- les fonctions.

---

## 🎯 Objectifs

À la fin de cette séance, vous devez être capable de :

- créer et utiliser des variables ;
- manipuler les principaux types de données ;
- utiliser `if`, `elif` et `else` ;
- utiliser les boucles `for` et `while` ;
- créer et parcourir une liste ;
- écrire une fonction avec des paramètres ;
- utiliser `return` ;
- combiner ces notions dans un programme Python.

---

# 1. Variables et types

Une variable permet de stocker une valeur.

```python
nom = "Alice"
age = 17
taille = 1.72
admis = True
```

Python possède différents types de données.

| Type | Exemple | Utilisation |
|---|---|---|
| `str` | `"Alice"` | texte |
| `int` | `17` | nombre entier |
| `float` | `1.72` | nombre décimal |
| `bool` | `True` | vrai / faux |

Pour connaître le type d'une variable :

```python
print(type(age))
```

---

# 2. Affichage

La fonction :

```python
print()
```

permet d'afficher une information.

```python
nom = "Alice"

print(nom)
```

Nous pouvons également utiliser une **f-string** :

```python
age = 17

print(f"{nom} a {age} ans.")
```

Résultat :

```text
Alice a 17 ans.
```

---

# 3. Saisie utilisateur

La fonction :

```python
input()
```

permet de demander une information à l'utilisateur.

```python
nom = input("Votre nom : ")

print(f"Bonjour {nom}")
```

⚠️ `input()` retourne du texte.

Pour demander un entier :

```python
age = int(input("Votre âge : "))
```

Pour demander un nombre décimal :

```python
taille = float(input("Votre taille : "))
```

---

# 4. Conditions

Une condition permet au programme de prendre une décision.

```python
age = 17

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

Nous pouvons ajouter plusieurs possibilités avec `elif` :

```python
note = 14

if note >= 16:
    print("Très bien")

elif note >= 10:
    print("Admis")

else:
    print("Non admis")
```

---

# 5. Opérateurs de comparaison

Les principaux opérateurs sont :

```text
==    égal à
!=    différent de
>     supérieur à
<     inférieur à
>=    supérieur ou égal à
<=    inférieur ou égal à
```

Exemple :

```python
if note >= 10:
    print("Admis")
```

---

# 6. Boucle `for`

Une boucle permet de répéter des instructions.

```python
for i in range(5):
    print(i)
```

Résultat :

```text
0
1
2
3
4
```

Pour compter de `1` à `5` :

```python
for i in range(1, 6):
    print(i)
```

---

# 7. Boucle `while`

La boucle `while` continue tant qu'une condition est vraie.

```python
compteur = 1

while compteur <= 5:

    print(compteur)

    compteur += 1
```

Résultat :

```text
1
2
3
4
5
```

---

# 8. Listes

Une liste permet de stocker plusieurs valeurs.

```python
notes = [12, 15, 9, 18]
```

Pour accéder à une valeur :

```python
print(notes[0])
```

Résultat :

```text
12
```

⚠️ Les indices commencent à `0`.

---

# 9. Parcourir une liste

Nous pouvons utiliser une boucle :

```python
notes = [12, 15, 9, 18]

for note in notes:
    print(note)
```

Nous pouvons également appliquer une condition :

```python
for note in notes:

    if note >= 10:
        print(note)
```

---

# 10. Ajouter un élément dans une liste

La méthode :

```python
append()
```

permet d'ajouter un élément.

```python
notes = [12, 15]

notes.append(18)

print(notes)
```

Résultat :

```text
[12, 15, 18]
```

---

# 11. Fonctions

Une fonction permet de regrouper des instructions que l'on souhaite réutiliser.

```python
def bonjour():
    print("Bonjour !")
```

Pour appeler la fonction :

```python
bonjour()
```

---

# 12. Fonctions avec paramètres

Une fonction peut recevoir des valeurs.

```python
def bonjour(nom):
    print(f"Bonjour {nom} !")
```

Utilisation :

```python
bonjour("Alice")
bonjour("Tom")
```

---

# 13. Utiliser `return`

Une fonction peut également **retourner une valeur**.

```python
def carre(nombre):
    return nombre * nombre
```

Utilisation :

```python
resultat = carre(5)

print(resultat)
```

Résultat :

```text
25
```

---

# 🧠 À retenir

Vous devez maîtriser les structures suivantes :

### Condition

```python
if condition:
    ...

elif autre_condition:
    ...

else:
    ...
```

### Boucle

```python
for element in liste:
    ...
```

### Fonction

```python
def fonction(parametre):
    ...
    return resultat
```

### Liste

```python
liste = []

liste.append(element)
```

---

# 💻 Exercices

Cette séance contient **4 exercices**.

Vous devez compléter les fichiers fournis sans modifier leur nom.

---

# Exercice 1

📄 Fichier :

```text
seance01_exercice1.py
```

Ouvrez le fichier et réalisez le travail demandé dans les commentaires.

Cet exercice permet de revoir :

- les variables ;
- les calculs ;
- l'affichage ;
- les conditions.

---

# Exercice 2

📄 Fichier :

```text
seance01_exercice2.py
```

Cet exercice permet de revoir :

- les boucles ;
- les conditions ;
- la répétition d'instructions.

---

# Exercice 3

📄 Fichier :

```text
seance01_exercice3.py
```

Cet exercice permet de revoir :

- les listes ;
- le parcours d'une liste ;
- les conditions appliquées aux éléments d'une liste.

---

# Exercice 4

📄 Fichier :

```text
seance01_exercice4.py
```

Cet exercice permet de revoir :

- les fonctions ;
- les paramètres ;
- `return` ;
- la combinaison de plusieurs notions Python.

---

# 🚀 Exécuter un exercice

Ouvrez le terminal dans VS Code.

Pour exécuter l'exercice 1 :

```bash
python seance01_exercice1.py
```

Pour l'exercice 2 :

```bash
python seance01_exercice2.py
```

et ainsi de suite.

Vous pouvez également utiliser **Run Python File** dans VS Code.

---

# 🧪 Tester votre programme

Ne vous contentez pas d'écrire le code.

Testez-le avec plusieurs valeurs.

Par exemple, si votre programme utilise une condition :

```python
if note >= 10:
```

testez :

```text
note = 15
note = 10
note = 5
```

Vous devez vérifier que votre programme fonctionne dans plusieurs situations.

---

# 🐞 En cas d'erreur

Lisez attentivement le message affiché par Python.

Regardez notamment :

```text
Type d'erreur
Fichier
Numéro de ligne
```

Les erreurs fréquentes sont :

```text
SyntaxError
NameError
TypeError
IndentationError
```

Essayez d'identifier la cause avant de modifier votre programme.

---

# 💾 Sauvegarder votre travail sur GitHub

Après chaque exercice fonctionnel :

1. ouvrez **Source Control** ;
2. vérifiez les fichiers modifiés ;
3. écrivez un message de commit ;
4. cliquez sur **Commit** ;
5. cliquez sur **Sync Changes**.

Exemples de messages :

```text
Termine exercice 1
```

```text
Corrige exercice 2
```

```text
Termine séance 01
```

---

# ⚠️ Fichiers `corrige`

Le dossier peut également contenir des fichiers comme :

```text
seance01_exercice1_corrige.py
```

Ces fichiers contiennent les **corrigés**.

Vous devez d'abord travailler dans :

```text
seance01_exercice1.py
```

et chercher votre propre solution.

N'utilisez le corrigé qu'après avoir réellement essayé de résoudre l'exercice.

---

# ✅ Avant de terminer

Vérifiez que :

- [ ] je sais créer une variable ;
- [ ] je connais `str`, `int`, `float` et `bool` ;
- [ ] je sais utiliser `input()` ;
- [ ] je sais utiliser `if / elif / else` ;
- [ ] je sais utiliser une boucle `for` ;
- [ ] je sais utiliser une boucle `while` ;
- [ ] je sais créer et parcourir une liste ;
- [ ] je sais utiliser `append()` ;
- [ ] je sais créer une fonction ;
- [ ] je sais utiliser des paramètres ;
- [ ] je comprends le rôle de `return` ;
- [ ] les 4 exercices fonctionnent ;
- [ ] mon travail a été **commit et push** sur GitHub.

---

# 🎯 Critère de réussite

À la fin de cette séance, vous devez être capable de :

> **Écrire un programme Python utilisant des variables, des conditions, des boucles, des listes et des fonctions sans aide importante.**

---

# 🔜 Prochaine séance

## Séance 02 — Premiers pas en programmation orientée objet

Lors de la prochaine séance, nous découvrirons une nouvelle manière d'organiser nos programmes : la **programmation orientée objet (POO)**.

Nous découvrirons notamment :

```text
Classe
Objet
Attribut
Méthode
self
```

Nous apprendrons à créer nos premiers objets Python :

```python
class Personne:
    ...

p1 = Personne()
```

🐍 Nous passerons ainsi de programmes organisés principalement autour de fonctions à des programmes organisés autour **d'objets possédant des données et des comportements**.