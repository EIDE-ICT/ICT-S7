"""
Séance 3 — Exercice 2 : La méthode spéciale __str__
Notions : __str__(self)

Ajoute à la classe Livre une méthode spéciale __str__(self) qui
renvoie "<titre> de <auteur>". Grâce à elle, print(mon_livre)
affichera directement ce texte, sans avoir besoin d'appeler une
méthode explicitement.
"""

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        pass  # TODO : remplace "pass" par ton code (return f"...")


l1 = Livre("1984", "George Orwell")
print(l1)   # attendu : 1984 de George Orwell
