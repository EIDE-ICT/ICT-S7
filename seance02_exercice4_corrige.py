"""
Séance 2 — Exercice 4 : À toi de jouer (CORRIGÉ)
"""

class Livre:
    def afficher_info(self):
        print(f"{self.titre} — {self.auteur}")


l1 = Livre()
l1.titre = "1984"
l1.auteur = "George Orwell"
l1.afficher_info()
