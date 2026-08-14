"""
Séance 4 — Exercice 3 : Classe Animal
Notions : __init__, méthode simple

Complète la classe Animal : le constructeur reçoit nom et espece,
la méthode se_presenter() affiche "<nom> est un(e) <espece>."
"""

class Animal:
    def __init__(self, nom, espece):
        pass  # TODO

    def se_presenter(self):
        pass  # TODO


a = Animal("Rex", "chien")
a.se_presenter()   # attendu : Rex est un(e) chien.
