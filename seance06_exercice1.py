"""
Séance 6 — Exercice 1 : Une classe qui contient une liste d'objets
Notions : attribut de type liste, .append()

La classe Classe (un groupe d'élèves) a un attribut "eleves" qui est
une LISTE d'objets Eleve. Complète la méthode ajouter_eleve(self, eleve)
qui ajoute un élève à cette liste.
"""

class Eleve:
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note


class Classe:
    def __init__(self, nom_classe):
        self.nom_classe = nom_classe
        self.eleves = []

    def ajouter_eleve(self, eleve):
        pass  # TODO : ajoute "eleve" à self.eleves


c = Classe("S7-A")
c.ajouter_eleve(Eleve("Nora", 15))
c.ajouter_eleve(Eleve("Tom", 12))
print(len(c.eleves))   # attendu : 2
