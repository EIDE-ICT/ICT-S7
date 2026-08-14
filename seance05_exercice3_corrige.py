"""
Séance 5 — Exercice 3 : Polymorphisme sur une liste (CORRIGÉ)
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis {self.nom}.")


class Chien(Animal):
    def se_presenter(self):
        print(f"Ouaf, je suis {self.nom}.")


class Chat(Animal):
    def se_presenter(self):
        print(f"Miaou, je suis {self.nom}.")


class Vache(Animal):
    def se_presenter(self):
        print(f"Meuh, je suis {self.nom}.")


animaux = [Chien("Rex"), Chat("Félix"), Vache("Marguerite")]
for animal in animaux:
    animal.se_presenter()
