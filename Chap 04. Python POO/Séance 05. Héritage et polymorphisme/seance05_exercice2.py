"""
Séance 5 — Exercice 2 : Redéfinir une méthode (polymorphisme)
Notions : redéfinition de méthode (override)

La classe Chat hérite d'Animal. Redéfinis sa méthode se_presenter()
pour qu'elle affiche "Miaou, je suis <nom>." au lieu du message
générique de la classe Animal.
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Je suis {self.nom}.")


class Chat(Animal):
    def se_presenter(self):
        pass  # TODO : remplace "pass" par ton code


chat = Chat("Félix")
chat.se_presenter()   # attendu : Miaou, je suis Félix.
