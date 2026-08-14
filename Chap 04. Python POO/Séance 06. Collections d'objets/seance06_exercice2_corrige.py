"""
Séance 6 — Exercice 2 : Calculer une moyenne sur une liste d'objets (CORRIGÉ)
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
        return sum(e.note for e in self.eleves) / len(self.eleves)


c = Classe("S7-B")
c.ajouter_eleve(Eleve("Nora", 15))
c.ajouter_eleve(Eleve("Tom", 12))
c.ajouter_eleve(Eleve("Léa", 18))
print(c.moyenne())   # attendu : 15.0
