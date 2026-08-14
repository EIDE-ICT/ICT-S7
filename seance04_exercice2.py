"""
Séance 4 — Exercice 2 : Classe CompteBancaire avec retrait sécurisé
Notions : condition à l'intérieur d'une méthode

Complète la classe CompteBancaire : deposer(montant) augmente le
solde ; retirer(montant) le diminue SEULEMENT si le solde est
suffisant, sinon affiche "Solde insuffisant" sans rien changer.
"""

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        pass  # TODO

    def retirer(self, montant):
        pass  # TODO : if montant > self.solde -> "Solde insuffisant", sinon retire


c = CompteBancaire("Tom", 100)
c.retirer(150)   # doit afficher "Solde insuffisant", solde reste 100
print(c.solde)   # attendu : 100
c.retirer(40)
print(c.solde)   # attendu : 60
