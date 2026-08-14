"""
Séance 6 — Exercice 3 : Un dictionnaire d'objets
Notions : dictionnaire dont les valeurs sont des objets

Un dictionnaire "bibliotheque" est déjà créé. Ajoute-lui deux objets
Livre, en utilisant leur titre comme clé, puis affiche l'auteur du
livre "1984" en passant par le dictionnaire.
"""

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


bibliotheque = {}

# TODO : bibliotheque["1984"] = Livre("1984", "George Orwell")

# TODO : bibliotheque["Le Petit Prince"] = Livre("Le Petit Prince", "Saint-Exupéry")

# TODO : affiche bibliotheque["1984"].auteur
