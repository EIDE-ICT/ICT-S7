"""
Séance 5 — Exercice 3 : Polymorphisme sur une liste
Notions : parcourir une liste d'objets de classes différentes

Les classes Chien et Vache héritent d'Animal et redéfinissent
se_presenter() chacune à sa façon (déjà écrites ci-dessous). Crée
une liste "animaux" contenant un Chien, un Chat et une Vache, puis
parcours-la avec une boucle for en appelant se_presenter() sur
chacun : c'est le polymorphisme — le même appel de méthode déclenche
un comportement différent selon la classe réelle de l'objet.
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


# TODO : crée la liste animaux = [Chien("Rex"), Chat("Félix"), Vache("Marguerite")]

# TODO : boucle for qui appelle animal.se_presenter() pour chaque animal
