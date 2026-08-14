"""
Séance 3 — Exercice 3 : Encapsulation (CORRIGÉ)
"""

class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire
        self._solde = solde_initial

    def obtenir_solde(self):
        return self._solde

    def deposer(self, montant):
        self._solde += montant


c = CompteBancaire("Nora", 100)
c.deposer(50)
print(c.obtenir_solde())   # attendu : 150
