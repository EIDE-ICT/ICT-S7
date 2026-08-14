"""
Séance 7 — Lancement du mini-projet (CORRIGÉ / EXEMPLE ENSEIGNANT)

Ce fichier illustre un cahier des charges complété pour le Sujet A
(Gestion d'une bibliothèque) — à utiliser comme référence de
correction, ou à montrer aux élèves comme modèle de ce qui est
attendu. Le code sera développé progressivement aux séances 8, 9 et 10.
"""

# =================================================================
# ÉTAPE 1 — Sujet choisi
# =================================================================
# Sujet choisi : A — Gestion d'une bibliothèque


# =================================================================
# ÉTAPE 2 — Cahier des charges (exemple de réponses recevables)
# =================================================================
# 1) Classes prévues :
#    - Livre (titre, auteur, disponible) — sait s'afficher avec __str__
#    - Membre (nom, livres_empruntes : une liste) — pas de méthode propre
#    - Bibliotheque (livres, membres) — méthodes ajouter_livre(),
#      inscrire_membre(), emprunter(membre, livre), retourner(membre, livre)
#
# 2) Pas d'héritage prévu pour ce sujet (contrairement au sujet C, le
#    "petit zoo", qui réutiliserait l'héritage vu en séance 5).
#
# 3) Message d'accueil : "=== Bibliothèque scolaire ===", suivi d'une
#    courte démonstration (ajout de livres, inscription d'un membre).
#
# 4) Tests prévus : emprunter un livre disponible (doit réussir),
#    emprunter un livre déjà emprunté (doit échouer proprement),
#    rendre un livre emprunté (doit le rendre disponible à nouveau).


# =================================================================
# ÉTAPE 3 — Squelette de départ
# =================================================================
class Livre:
    def __init__(self, titre, auteur):
        pass  # sera complété à la séance 8


class Membre:
    def __init__(self, nom):
        pass  # sera complété à la séance 8


class Bibliotheque:
    def __init__(self):
        pass  # sera complété à la séance 8


if __name__ == "__main__":
    print("=== Bibliothèque scolaire ===")
    # La démonstration complète sera écrite à la séance 8
