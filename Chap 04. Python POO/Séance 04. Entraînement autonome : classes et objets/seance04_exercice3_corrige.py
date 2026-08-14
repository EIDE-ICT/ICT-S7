"""
Séance 4 — Exercice 3 : Classe Animal (CORRIGÉ)
"""

class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def se_presenter(self):
        print(f"{self.nom} est un(e) {self.espece}.")


a = Animal("Rex", "chien")
a.se_presenter()   # attendu : Rex est un(e) chien.
