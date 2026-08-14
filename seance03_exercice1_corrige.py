"""
Séance 3 — Exercice 1 : Le constructeur __init__ (CORRIGÉ)
"""

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")


p1 = Personne("Nora", 16)
p1.se_presenter()
