"""
Séance 5 — Exercice 1 : Héritage simple
Notions : class Enfant(Parent), super().__init__()

La classe Chien HÉRITE de la classe Animal (elle a tout ce qu'Animal
a, plus un attribut race en plus). Complète son constructeur en
appelant d'abord super().__init__(nom) pour initialiser la partie
"Animal", puis ajoute self.race.
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis {self.nom}.")


class Chien(Animal):
    def __init__(self, nom, race):
        pass  # TODO : appelle super().__init__(nom), puis self.race = race


c = Chien("Rex", "Labrador")
c.se_presenter()   # attendu : Je suis Rex.
print(c.race)       # attendu : Labrador
