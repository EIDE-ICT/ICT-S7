"""
Séance 10 — Finalisation et présentation du mini-projet
(CORRIGÉ / EXEMPLE ENSEIGNANT — version finale complète et testée)

Ce fichier est autonome : il peut être exécuté tel quel pour une
démonstration en classe (gestion d'une bibliothèque).
"""

class Livre:
    """Un livre de la bibliothèque : titre, auteur, et disponibilité."""

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} de {self.auteur} ({statut})"


class Membre:
    """Un membre inscrit à la bibliothèque, avec la liste de ses emprunts en cours."""

    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []


class Bibliotheque:
    """Gère la collection de livres, les membres inscrits, et les emprunts/retours."""

    def __init__(self):
        self.livres = []
        self.membres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def inscrire_membre(self, membre):
        self.membres.append(membre)

    def emprunter(self, membre, livre):
        if not livre.disponible:
            print(f"{livre.titre} n'est pas disponible.")
            return False
        livre.disponible = False
        membre.livres_empruntes.append(livre)
        print(f"{membre.nom} a emprunté {livre.titre}.")
        return True

    def retourner(self, membre, livre):
        if livre not in membre.livres_empruntes:
            print(f"{membre.nom} n'a pas emprunté {livre.titre}.")
            return False
        livre.disponible = True
        membre.livres_empruntes.remove(livre)
        print(f"{membre.nom} a rendu {livre.titre}.")
        return True


# ---------------------------------------------------------------
# Tests automatisés (démontrent que le programme est fiable)
# ---------------------------------------------------------------
def _tests():
    biblio = Bibliotheque()
    l1 = Livre("1984", "George Orwell")
    biblio.ajouter_livre(l1)
    nora = Membre("Nora")
    tom = Membre("Tom")
    biblio.inscrire_membre(nora)
    biblio.inscrire_membre(tom)

    assert biblio.emprunter(nora, l1) == True
    assert biblio.emprunter(tom, l1) == False
    assert biblio.retourner(nora, l1) == True
    assert l1.disponible == True

_tests()
print("Tests automatisés : OK\n")


# ---------------------------------------------------------------
# Programme principal (démonstration)
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Bibliothèque scolaire ===\n")
    biblio = Bibliotheque()
    biblio.ajouter_livre(Livre("1984", "George Orwell"))
    biblio.ajouter_livre(Livre("Le Petit Prince", "Saint-Exupéry"))

    nora = Membre("Nora")
    tom = Membre("Tom")
    biblio.inscrire_membre(nora)
    biblio.inscrire_membre(tom)

    biblio.emprunter(nora, biblio.livres[0])
    biblio.emprunter(tom, biblio.livres[0])   # doit échouer proprement
    biblio.retourner(nora, biblio.livres[0])

    print("\nÉtat final de la collection :")
    for livre in biblio.livres:
        print(livre)

# Notes pour la présentation orale (exemple de réponses attendues) :
# - Sujet choisi : gestion d'une bibliothèque.
# - Classes : Livre (données + affichage), Membre (données), et
#   Bibliotheque (logique métier : emprunter/retourner).
# - Difficulté rencontrée : empêcher qu'un livre soit emprunté deux
#   fois -> résolue en testant livre.disponible avant l'emprunt.
# - Amélioration possible avec plus de temps : une date d'emprunt et
#   une limite du nombre de livres empruntés par membre.
