"""
Séance 4 — Exercice 2 : Classe CompteBancaire avec retrait sécurisé (CORRIGÉ)
"""

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            print("Solde insuffisant")
        else:
            self.solde -= montant


c = CompteBancaire("Tom", 100)
c.retirer(150)
print(c.solde)   # attendu : 100
c.retirer(40)
print(c.solde)   # attendu : 60
