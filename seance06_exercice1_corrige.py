"""
Séance 6 — Exercice 1 : Une classe qui contient une liste d'objets (CORRIGÉ)
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


c = Classe("S7-A")
c.ajouter_eleve(Eleve("Nora", 15))
c.ajouter_eleve(Eleve("Tom", 12))
print(len(c.eleves))   # attendu : 2
