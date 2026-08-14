"""
Séance 9 — Développement du projet : fonctionnalités, tests
(CORRIGÉ / EXEMPLE ENSEIGNANT)
Version avec méthodes complètes du projet "Gestion d'une bibliothèque".
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
# Checklist de tests (résultats de la vérification enseignant)
# ---------------------------------------------------------------
# [x] Cas normal : un membre emprunte un livre disponible -> réussit.
# [x] Cas limite : un second membre essaie d'emprunter le même livre
#     -> échoue proprement (message clair, pas de plantage).
# [x] Retour d'un livre emprunté -> le livre redevient disponible.

def _tests():
    biblio = Bibliotheque()
    l1 = Livre("1984", "George Orwell")
    biblio.ajouter_livre(l1)
    nora = Membre("Nora")
    tom = Membre("Tom")
    biblio.inscrire_membre(nora)
    biblio.inscrire_membre(tom)

    assert biblio.emprunter(nora, l1) == True
    assert l1.disponible == False
    assert biblio.emprunter(tom, l1) == False   # cas limite : déjà emprunté
    assert biblio.retourner(nora, l1) == True
    assert l1.disponible == True

_tests()
print("Tests automatisés séance 9 : OK")


if __name__ == "__main__":
    print("=== Bibliothèque scolaire ===")
    biblio = Bibliotheque()
    biblio.ajouter_livre(Livre("1984", "George Orwell"))
    biblio.ajouter_livre(Livre("Le Petit Prince", "Saint-Exupéry"))
    nora = Membre("Nora")
    biblio.inscrire_membre(nora)

    biblio.emprunter(nora, biblio.livres[0])
    for livre in biblio.livres:
        print(livre)
