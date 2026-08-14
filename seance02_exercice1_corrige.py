"""
Séance 2 — Exercice 1 : Ma première classe (CORRIGÉ)
"""

class Personne:
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")


p1 = Personne()
p1.nom = "Nora"
p1.age = 16
p1.se_presenter()
