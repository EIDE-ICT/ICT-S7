"""
Séance 4 — Exercice 1 : Classe Rectangle (CORRIGÉ)
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)


r = Rectangle(5, 3)
print(r.aire())        # attendu : 15
print(r.perimetre())   # attendu : 16
