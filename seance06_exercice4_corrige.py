"""
Séance 6 — Exercice 4 : À toi de jouer (CORRIGÉ)
"""

class Panier:
    def __init__(self):
        self.produits = []

    def ajouter(self, produit, prix):
        self.produits.append((produit, prix))

    def total(self):
        return sum(prix for produit, prix in self.produits)


p = Panier()
p.ajouter("Stylo", 2.50)
p.ajouter("Cahier", 3.20)
print(p.total())   # attendu : 5.7
