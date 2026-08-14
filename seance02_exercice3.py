"""
Séance 2 — Exercice 3 : Une méthode qui calcule
Notions : méthode avec paramètre, calcul sur des attributs

Ajoute à la classe Personne une méthode dans_x_ans(self, x) qui
renvoie l'âge de la personne dans x années (self.age + x).
"""

class Personne:
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

    def dans_x_ans(self, x):
        pass  # TODO : remplace "pass" par ton code (return self.age + x)


p1 = Personne()
p1.nom = "Léa"
p1.age = 15
print(p1.dans_x_ans(5))   # attendu : 20
