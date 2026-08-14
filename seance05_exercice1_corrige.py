"""
Séance 5 — Exercice 1 : Héritage simple (CORRIGÉ)
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis {self.nom}.")


class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)
        self.race = race


c = Chien("Rex", "Labrador")
c.se_presenter()   # attendu : Je suis Rex.
print(c.race)       # attendu : Labrador
