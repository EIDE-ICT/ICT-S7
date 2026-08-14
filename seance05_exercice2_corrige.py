"""
Séance 5 — Exercice 2 : Redéfinir une méthode (polymorphisme) (CORRIGÉ)
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis {self.nom}.")


class Chat(Animal):
    def se_presenter(self):
        print(f"Miaou, je suis {self.nom}.")


chat = Chat("Félix")
chat.se_presenter()   # attendu : Miaou, je suis Félix.
