"""
Séance 6 — Exercice 3 : Un dictionnaire d'objets (CORRIGÉ)
"""

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


bibliotheque = {}
bibliotheque["1984"] = Livre("1984", "George Orwell")
bibliotheque["Le Petit Prince"] = Livre("Le Petit Prince", "Saint-Exupéry")

print(bibliotheque["1984"].auteur)   # attendu : George Orwell
