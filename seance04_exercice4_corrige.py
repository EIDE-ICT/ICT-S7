"""
Séance 4 — Exercice 4 : Classe Produit avec TVA (CORRIGÉ)
"""

class Produit:
    def __init__(self, nom, prix_ht):
        self.nom = nom
        self.prix_ht = prix_ht

    def prix_ttc(self):
        return round(self.prix_ht * 1.20, 2)


p = Produit("Stylo", 2.50)
print(p.prix_ttc())   # attendu : 3.0
