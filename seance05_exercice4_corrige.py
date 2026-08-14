"""
Séance 5 — Exercice 4 : À toi de jouer (CORRIGÉ)
"""

class Vehicule:
    def __init__(self, marque):
        self.marque = marque

    def rouler(self):
        print(f"{self.marque} roule.")


class Voiture(Vehicule):
    def __init__(self, marque, nb_portes):
        super().__init__(marque)
        self.nb_portes = nb_portes


v = Voiture("Renault", 5)
v.rouler()   # méthode héritée, pas redéfinie
print(v.nb_portes)
