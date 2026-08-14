"""
Séance 3 — Exercice 4 : À toi de jouer (CORRIGÉ)
"""

class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

    def __str__(self):
        return f"{self.marque} ({self.annee})"


v = Voiture("Renault", 2022)
print(v)
