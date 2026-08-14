"""
Séance 8 — Développement du projet : structure des classes
(CORRIGÉ / EXEMPLE ENSEIGNANT)
Suite de l'exemple "Gestion d'une bibliothèque" commencé à la séance 7.
"""

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} de {self.auteur} ({statut})"


class Membre:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []


class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.membres = []


# ---------------------------------------------------------------
# Test rapide de la structure
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Bibliothèque scolaire ===")
    l1 = Livre("1984", "George Orwell")
    l2 = Livre("Le Petit Prince", "Saint-Exupéry")
    print(l1)
    print(l2)

    nora = Membre("Nora")
    print(nora.nom, nora.livres_empruntes)

    biblio = Bibliotheque()
    print(biblio.livres, biblio.membres)

# Point de vigilance pour la correction (séance 8) : à ce stade, les
# objets se créent et s'affichent correctement, mais Bibliotheque n'a
# pas encore de méthode pour ajouter des livres/membres ou gérer les
# emprunts — c'est l'objectif de la séance 9.
