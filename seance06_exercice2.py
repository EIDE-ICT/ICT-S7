"""
Séance 6 — Exercice 2 : Calculer une moyenne sur une liste d'objets
Notions : parcourir une liste d'objets, calcul

Ajoute à la classe Classe une méthode moyenne(self) qui renvoie la
moyenne des notes de tous les élèves de self.eleves.
Indice : sum(e.note for e in self.eleves) additionne toutes les notes.
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
        self.eleves.append(eleve)

    def moyenne(self):
        pass  # TODO : renvoie la moyenne des notes de self.eleves


c = Classe("S7-B")
c.ajouter_eleve(Eleve("Nora", 15))
c.ajouter_eleve(Eleve("Tom", 12))
c.ajouter_eleve(Eleve("Léa", 18))
print(c.moyenne())   # attendu : 15.0
