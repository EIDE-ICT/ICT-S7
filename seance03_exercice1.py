"""
Séance 3 — Exercice 1 : Le constructeur __init__
Notions : __init__(self, ...)

Réécris la classe Personne avec un CONSTRUCTEUR __init__(self, nom, age)
qui reçoit le nom et l'âge directement, au lieu de les ajouter après
coup (comme en séance 2). Crée ensuite un objet en lui passant
directement nom et âge : Personne("Nora", 16).
"""

class Personne:
    def __init__(self, nom, age):
        pass  # TODO : remplace "pass" par ton code (self.nom = nom, self.age = age)

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")


# TODO : crée p1 = Personne("Nora", 16) puis appelle p1.se_presenter()
