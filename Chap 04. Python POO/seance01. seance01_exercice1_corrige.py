"""
Séance 1 — Exercice 1 : Rappel — conditions (CORRIGÉ)
"""

note = float(input("Entre une note sur 20 : "))
if note < 10:
    print("Insuffisant")
elif note < 12:
    print("Passable")
elif note < 14:
    print("Assez bien")
elif note < 16:
    print("Bien")
elif note < 18:
    print("Très bien")
else:
    print("Excellent")
