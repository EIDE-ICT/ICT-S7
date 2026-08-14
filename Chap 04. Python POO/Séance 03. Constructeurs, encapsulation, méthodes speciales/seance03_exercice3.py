"""
Séance 3 — Exercice 3 : Encapsulation
Notions : attribut "privé" (_attribut), méthode getter

Dans la classe CompteBancaire, le solde est stocké dans _solde (le
underscore indique par convention que cet attribut ne devrait pas
être modifié directement de l'extérieur). Complète la méthode
obtenir_solde(self) qui renvoie sa valeur, et deposer(self, montant)
qui l'augmente.
"""

class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire
        self._solde = solde_initial

    def obtenir_solde(self):
        pass  # TODO : remplace "pass" par ton code (return self._solde)

    def deposer(self, montant):
        pass  # TODO : remplace "pass" par ton code (self._solde += montant)


c = CompteBancaire("Nora", 100)
c.deposer(50)
print(c.obtenir_solde())   # attendu : 150
