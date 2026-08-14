"""
Séance 3 — Exercice 2 : La méthode spéciale __str__ (CORRIGÉ)
"""

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} de {self.auteur}"


l1 = Livre("1984", "George Orwell")
print(l1)   # attendu : 1984 de George Orwell
