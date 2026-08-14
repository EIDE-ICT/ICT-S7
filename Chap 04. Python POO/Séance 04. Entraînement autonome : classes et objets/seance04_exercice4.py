"""
Séance 4 — Exercice 4 : Classe Produit avec TVA
Notions : __init__, méthode avec calcul, round()

Complète la classe Produit : le constructeur reçoit nom et prix_ht,
la méthode prix_ttc() renvoie le prix avec 20% de TVA en plus,
arrondi à 2 décimales.
"""

class Produit:
    def __init__(self, nom, prix_ht):
        pass  # TODO

    def prix_ttc(self):
        pass  # TODO : return round(self.prix_ht * 1.20, 2)


p = Produit("Stylo", 2.50)
print(p.prix_ttc())   # attendu : 3.0
