"""
Séance 2 — Exercice 2 : Plusieurs objets
Notions : plusieurs instances d'une même classe

Réutilise la classe Personne (recopiée ci-dessous, déjà complète).
Crée DEUX objets (p1 et p2) avec des noms et âges différents, et
appelle se_presenter() sur chacun.
"""

class Personne:
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")


# TODO : crée p1 avec un nom et un âge, puis appelle p1.se_presenter()

# TODO : crée p2 avec un AUTRE nom et âge, puis appelle p2.se_presenter()
